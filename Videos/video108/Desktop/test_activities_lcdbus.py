# test_activities_lcdbus.py v1.0
#
# Created: 25 September 2026
# Updated: 27 September 2026
#
# Copyright (C) 2025 KW Services.
# MIT License
#
# Verified on:
# MicroPython 78ff170de9-dirty on 2026-09-18;
# Generic ESP32S3 module with Octal-SPIRAM with ESP32S3
# LCD_Bus with LVGL 9.4.0
#
import lvgl as lv
from display_driver import display
import time
from machine import reset, RTC
import gc

#print(f"Heap:{gc.mem_free()}")

# ===================== GLOBAL CONFIGURATION =====================
# List of people allowed in the scheduler (international users can modify names)
PERSONS = ["Tom", "Mary", "Sam"]

# Activity task names (optional predefined activities for quick selection)
ACTIVITY_TASKS = ["Work", "Meet", "Break", "Study", "Call", "Email"]

# Filename for persistence
FILENAME = "activity.txt"
SAVE_FILENAME = "backup.txt"
LOAD_AT_STARTUP = True

# ----------------------------------------------------------------
TITLE = "Family Activities"

# Month names (1-indexed, index 0 unused) - allow localization
MONTH_NAMES = [
    "",  # placeholder
    "January", "February", "March", "April", "May", "June",
    "July", "August", "September", "October", "November", "December"
]

# Weekday names (Monday=0 ... Sunday=6 for LVGL calendar)
WEEKDAY_NAMES = [
    "Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"
]

# Load external font file
FONT_PATH = None
# Uncomment to use an external font (if flash drive has the extra font file)
FONT_PATH = "font/montserrat-med-20-2.bin"

############################################################################
#### Optional Theme Changes
############################################################################

# ===================== THEME =====================
class Theme:
    def __init__(self):
        self.bg = lv.color_hex(0x000000)
        self.fg = lv.color_white()
        self.accent = lv.color_hex(0x008080)
        self.highlight = lv.color_hex(0xFFDD00)
        self.button_bg = lv.color_hex(0x4CAF50)
        self.button_active = lv.color_hex(0x45A049)
        self.text_dark = lv.color_black()
        self.text_light = lv.color_hex(0xffff00) # yellow
        self.text_font = lv.font_montserrat_14
        self.header_font = lv.font_montserrat_16
        #### Optional external font
        self.montserrat_med_20 = None
        if FONT_PATH:
            self.verify_font_path(FONT_PATH)
        if self.montserrat_med_20:
            self.header_font = self.montserrat_med_20

    def verify_font_path(self, font_path):
        ready = False
        try:
            import os
            try:
                # check if MicroPython sees the font file
                os.stat(font_path) 
                ready = True
            except:
                ready = False
                print("Warning external font not found. Using alt font.")
            if ready:
                import fs_driver
                fs_drv = lv.fs_drv_t()
                fs_driver.fs_register(fs_drv, 'S')
                font_path = "S:" + font_path
                self.montserrat_med_20 = lv.binfont_create(font_path)
                print(f"Loaded external font: {font_path}")
        except:
            print("font did not load.")

theme = Theme()

#######################################################
####  AVOID CHANGES BELOW HERE
#######################################################

# ===================== DATA MODEL =====================
class ActivityScheduler:
    def __init__(self, names):
        """
        Initialize the scheduler with a list of people.
        schedule structure: {person: {date: {time: activity}}}
        """
        self.schedule = {name: {} for name in names}

    def add_activity(self, person, date, time, activity):
        """
        Adds an activity to a nested dictionary structured as:
        {Person: {Date: {Time: Activity}}}
        """
        #print(f"Add activity: p:{person:10} d:{date} t:{time} a:{activity}")
        if person not in self.schedule:
            self.schedule[person] = {}
        if date not in self.schedule[person]:
            self.schedule[person][date] = {}
        self.schedule[person][date][time] = activity
        return self.schedule

    def get_activities_for_date(self, date):
        """
        Returns a list of (person, time, activity) tuples for a given date string.
        """
        results = []
        for person, dates in self.schedule.items():
            if date in dates:
                for time, activity in dates[date].items():
                    results.append((person, time, activity))
        results.sort(key=lambda x: x[1])  # Sort by time
        return results

    def get_all_dates(self):
        """
        Returns a set of all dates that have any activities.
        """
        dates = set()
        for person, dates_dict in self.schedule.items():
            dates.update(dates_dict.keys())
        return list(dates)

    def show_schedule(self):
        """Print a formatted view of everyone's schedule."""
        print("\n--- DAILY ACTIVITY SCHEDULE ---")
        for person, activities in self.schedule.items():
            print("\n[{}]".format(person))
            if not activities:
                print("  No activities scheduled.")
                continue
            for date, times in activities.items():
                print(f"  {date}:")
                for t, act in sorted(times.items()):
                    print(f"    {t}: {act}")

# ===================== UI CLASSES =====================

class MonthView:
    def __init__(self, scheduler):
        self.scheduler = scheduler
        self.cal = None
        self.highlighted_days = []
        self.selected_date = None
        self.year = 0
        self.month = 0
        self.day = 0
        self.scr = None
        self.day_view = DayView(self.scheduler, '2026-09-01')
        
    def today(self):
        text = f"{self.year}-{self.month}-{self.day}"
        return text

    def get_today(self):
        dt = time.localtime()
        self.year= dt[0]
        self.month=dt[1]
        self.day=dt[2]
        if self.year == 2000:
            rtc = RTC()
            rtc.datetime((2026, 9, 25,4,12,30,0,0))
            self.year = 2026
            self.month = 9
            self.day = 25
        return self.year,self.month,self.day

    def show(self):
        """Call this to display the MonthView screen."""
        if self.scr is None:
            self._build_ui()
        lv.screen_load(self.scr)
        gc.collect()
        #print(f"Heap:{gc.mem_free()}")


    def _build_ui(self):
        if self.scr is not None:
            return

        self.scr = lv.obj()
        lv.screen_load(self.scr)

        # Get today's date
        year, month, day = self.get_today()

        # Main container
        mv_box = lv.obj(self.scr)
        mv_box.set_size(lv.pct(100), lv.pct(100))
        mv_box.set_flex_flow(lv.FLEX_FLOW.COLUMN_WRAP)
        mv_box.set_flex_align(lv.FLEX_ALIGN.START, lv.FLEX_ALIGN.START, lv.FLEX_ALIGN.START)
        mv_box.set_style_bg_color(theme.bg, 0)

        first = lv.obj(mv_box)
        first.set_size(lv.pct(40),lv.pct(100))
        first.set_flex_flow(lv.FLEX_FLOW.COLUMN_WRAP)
        first.set_flex_align(lv.FLEX_ALIGN.START,lv.FLEX_ALIGN.START,lv.FLEX_ALIGN.START)
        title_obj = lv.obj(first)
        title_obj.set_size(lv.pct(100),50)
        title_lbl = lv.label(title_obj)
        title_lbl.set_text(TITLE)
        title_lbl.set_style_text_font(theme.header_font, 0)
        hold = title_lbl
        # Load/Save buttons
 
        load_btn = lv.button(first)
        load_btn.set_size(lv.pct(100),50)
        load_lbl = lv.label(load_btn)
        load_lbl.set_text("Load")
        load_lbl.set_style_text_font(theme.header_font, 0)
        load_lbl.set_style_text_color(theme.text_dark,0)
        load_btn.add_event_cb(self._load_cb, lv.EVENT.CLICKED, None)

        save_btn = lv.button(first)
        save_btn.set_size(lv.pct(100),50)
        save_lbl = lv.label(save_btn)
        save_lbl.set_text("Save")
        save_lbl.set_style_text_font(theme.header_font, 0)
        save_lbl.set_style_text_color(theme.text_dark,0)
        save_btn.add_event_cb(self._save_cb, lv.EVENT.CLICKED, None)

        cont = lv.obj(mv_box)
        cont.set_size(lv.pct(60), lv.pct(100))
        cont.align(lv.ALIGN.RIGHT_MID,0,0)
        cont.set_flex_flow(lv.FLEX_FLOW.COLUMN)
        cont.set_flex_align(lv.FLEX_ALIGN.START, lv.FLEX_ALIGN.CENTER, lv.FLEX_ALIGN.CENTER)
        cont.set_style_pad_all(10, 0)
        cont.set_style_pad_row(10, 0) # Spacing between rows
        cont.set_style_border_width(1,0)

        # Header
        header = lv.label(cont)
        header.set_text(f"{MONTH_NAMES[month]} {year}")
        header.set_style_text_color(theme.text_light, 0)
        header.set_style_text_font(theme.header_font, 0)
        header.set_style_text_align(lv.TEXT_ALIGN.CENTER, 0)
        header.set_width(lv.pct(100))
        header.set_align(lv.ALIGN.CENTER)

        # Calendar
        self.cal = lv.calendar(cont)
        self.cal.set_size(400,lv.pct(85))
        self.cal.add_event_cb(self._calendar_event_cb, lv.EVENT.CLICKED, None)
        # Set current date
        cal_date = lv.calendar_date_t()
        cal_date.year = year
        cal_date.month = month
        cal_date.day = day
        self.cal.set_today_date(year, month, day)
        self.cal.set_month_shown(year, month)         ###lvgl 9.4
        self.cal.add_event_cb(self._calendar_event_cb, lv.EVENT.CLICKED, None)
        # Highlight existing dates
        self._update_highlights()


    def _update_highlights(self):
        self.highlighted_days = []
        dates = self.scheduler.get_all_dates()
        if dates:
            for date_str in dates:
                yr, mn, dy = date_str.split('-')
                highlight = lv.calendar_date_t()
                highlight.year = int(yr)
                highlight.month = int(mn)
                highlight.day = int(dy)
                self.highlighted_days.append(highlight)
            self.cal.set_highlighted_dates(self.highlighted_days, len(self.highlighted_days))

    def _calendar_event_cb(self, e):
        code = e.get_code()
        if code == lv.EVENT.PRESSING or code == lv.EVENT.CLICKED:
            cal = e.get_current_target_obj()
            date = lv.calendar_date_t()
            cal.get_pressed_date(date)
            self.selected_date = f"{date.year:04}-{date.month:02}-{date.day:02}"
            self.day_view.update_date(self.selected_date)
            self.day_view.show()

    def load_activity_file(self):
        self._file_load()
        self._update_highlights()
        print(f"Activity file {FILENAME} loaded.")

    def _load_cb(self, e):
        code = e.get_code()
        btn = e.get_target_obj()
        time.sleep_ms(100)
        self._file_load()
        self._update_highlights()
        btn.set_style_text_color(theme.text_light,0)
        btn.set_style_bg_color(theme.fg, 0)
        

    def _save_cb(self, e):
        code = e.get_code()
        btn = e.get_target_obj()
        time.sleep_ms(100)
        self._file_save()
        btn.set_style_text_color(theme.text_light,0)
        btn.set_style_bg_color(theme.fg, 0)

    def _file_load(self):
        self.highlighted_days = []
        with open(FILENAME, "rt") as file:
            for line in file:
                line = line.strip()
                if not line:
                    continue
                fields = line.split(",")
                try:
                    person = fields[0].strip()
                    date = fields[1].strip()
                    time_str = fields[2].strip()
                    activity = fields[3].strip()
                    self.scheduler.add_activity(person, date, time_str, activity)
                    # Add highlight
                    yr, mn, dy = date.split('-')
                    highlight = lv.calendar_date_t()
                    highlight.year = int(yr)
                    highlight.month = int(mn)
                    highlight.day = int(dy)
                    self.highlighted_days.append(highlight)
                except (IndexError, ValueError):
                    print("Skipping malformed line:", line)
        #print("Load done.")

    def _file_save(self):
        with open(SAVE_FILENAME, 'wt') as file:
            for person, dates in self.scheduler.schedule.items():
                for date, times in dates.items():
                    for time_str, activity in times.items():
                        line = f"{person},{date},{time_str},{activity}"
                        file.write(line + "\n")
        print("File written successfully!")


class DayView:
    def __init__(self, scheduler, date_str):
        self.scheduler = scheduler
        self.date_str = date_str
        self.selected_person = None
        self.maxsize = 34 # text for schedule
        self.scr = None
        self.event_form = EventForm(self.scheduler, PERSONS[0], '2026-09-01')

    def update_date(self, new_date):
        self.date_str = new_date
        self.scr = None

    def show(self):
        if self.scr is None:
            self._build_ui()
        lv.screen_load(self.scr)
        gc.collect()
        #print(f"Heap:{gc.mem_free()}")

    def _build_ui(self):
        if self.scr is not None:
            return
        self.scr = lv.obj()
        lv.screen_load(self.scr)
        gc.collect()
        #scr.set_style_bg_color(lv.color_black(), 0)

        # Header
        btn_header = lv.button(self.scr)
        btn_header.set_size(lv.pct(100),50)
        btn_header.set_style_bg_color(theme.bg, 0)
        btn_header.add_event_cb(self._back_cb, lv.EVENT.CLICKED, None)
        lbl_header = lv.label(btn_header)
        lbl_header.set_text(f"Schedule for {self.date_str}")
        lbl_header.set_style_text_color(theme.text_light, 0)
        lbl_header.set_style_text_font(theme.header_font, 0)
        lbl_header.set_style_text_align(lv.TEXT_ALIGN.CENTER, 0)
        lbl_header.set_width(lv.pct(100))
        lbl_header.set_align(lv.ALIGN.CENTER)

        # # Back button
        back_btn = lv.button(self.scr)
        back_btn.set_size(80, 50)
        back_btn.set_align(lv.ALIGN.TOP_LEFT)
        back_lbl = lv.label(back_btn)
        back_lbl.set_text("< Back")
        back_lbl.set_style_text_color(theme.text_dark, 0)
        back_btn.add_event_cb(self._back_cb, lv.EVENT.CLICKED, None)

        # List of people
        list_box = lv.obj(self.scr)
        list_box.set_pos(0,50)
        list_box.set_size(lv.pct(100),430)
        #list_box.set_align(lv.ALIGN.CENTER)
        list_box.set_flex_flow(lv.FLEX_FLOW.COLUMN_WRAP)
        list_box.set_flex_align(lv.FLEX_ALIGN.START, lv.FLEX_ALIGN.START, lv.FLEX_ALIGN.START)
        #list_box.set_style_bg_color(lv.color_hex(0xF5F5F5), 0)
        list_box.set_style_pad_all(21, 0) 
        list_box.set_style_pad_gap(15,0)
        list_box.add_flag(lv.obj.FLAG.SCROLLABLE)
        list_box.set_style_width(32, lv.PART.SCROLLBAR)

        for person in PERSONS:
            btn = lv.button(list_box)
            btn.set_size(240,50)
            #btn.set_style_bg_color(theme.bg, 0)
            btn_lbl = lv.label(btn)
            btn_lbl.set_text(person)
            btn_lbl.set_style_text_color(theme.text_dark, 0)
            btn_lbl.set_style_text_font(theme.header_font, 0)
            btn_lbl.set_style_text_align(lv.TEXT_ALIGN.CENTER, 0)
            btn.add_event_cb(self._person_cb, lv.EVENT.CLICKED, None)

            contact = lv.obj(list_box)
            contact.set_size(240,lv.pct(80))
            contact.set_flex_flow(lv.FLEX_FLOW.COLUMN)
            contact.set_flex_align(lv.FLEX_ALIGN.START, lv.FLEX_ALIGN.START,lv.FLEX_ALIGN.START)
            contact.set_style_pad_all(0, 0) 
            contact.set_style_pad_gap(5,0)
            dates = self.scheduler.schedule[person]
            sorted_dates = sorted(dates.keys())

            if self.date_str in sorted_dates:
                times = self.scheduler.schedule[person][self.date_str]
                sorted_times = sorted(times.keys() )
                for time in sorted_times:
                    activity = self.scheduler.schedule[person][self.date_str][time]
                    if not time and flag == 0:
                        btnact = lv.button(contact)
                        btnact.set_size(230, 40)
                        btnact.set_style_bg_color(theme.bg, 0)
                        lblact.set_style_text_color(theme.text_dark, 0)
                        lblact.set_style_text_font(lv.font_montserrat_16, 0)
                        lblact = lv.label(btnact)
                        lblact.set_text("No activities scheduled.")
                        continue
                    btnact = lv.button(contact)
                    text = f"{time}: {activity}"
                    if len(text) > self.maxsize:
                        btnact.set_size(230, 80)
                    else:
                        btnact.set_size(230, 40)
                        lblact = lv.label(btnact)
                        lblact.set_style_text_color(theme.text_dark, 0)
                        lblact.set_style_text_font(lv.font_montserrat_16, 0)
                        lblact.set_text(text)
                        flag = 1
            else:
                btnact = lv.button(contact)
                btnact.set_size(240, 40)
                btn.set_style_bg_color(theme.bg, 0)
                btn_lbl.set_style_text_color(theme.text_light, 0)
                lblact = lv.label(btnact)
                lblact.set_style_text_font(lv.font_montserrat_16, 0)
                lblact.set_style_text_color(theme.text_dark, 0)
                lblact.set_text("No activities scheduled.")

    def _back_cb(self, e):
        month_view.show()
        month_view._update_highlights()


    def _person_cb(self, e):
        code = e.get_code()
        btnperson = e.get_target_obj()
        if btnperson:
            lbl = btnperson.get_child(0)
            person = lbl.get_text()
            self.selected_person = person
            self.event_form.update_person_date(person, self.date_str)
            self.event_form.show()


class EventForm:
    def __init__(self, scheduler, person, date_str):
        self.scheduler = scheduler
        self.person = person
        self.date_str = date_str
        self.ta_time = None
        self.ta_activity = None
        self.btn_submit = None
        self.scr = None

    def update_person_date(self, new_person, new_date):
        self.person = new_person
        self.date_str = new_date
        self.scr = None

    def show(self):
        if self.scr is None:
            self._build_ui()
            self._balloons()
        lv.screen_load(self.scr)
        gc.collect()
        #print(f"Heap:{gc.mem_free()}")

    def _build_ui(self):
        if self.scr is not None:
            return

        self.scr = lv.obj()
        self.scr.set_style_bg_color(lv.color_black(), 0)
        lv.screen_load(self.scr)

        # Header
        header = lv.label(self.scr)
        header.set_text(f"Add Event - {self.person}")
        header.set_style_text_color(theme.text_dark, 0)
        header.set_style_text_font(theme.header_font, 0)
        header.set_style_text_align(lv.TEXT_ALIGN.CENTER, 0)
        header.set_width(lv.pct(100))
        header.set_align(lv.ALIGN.CENTER) #, 0, 0)
  
        # Back button
        back_btn = lv.button(self.scr)
        back_btn.set_size(280, 50)
        back_btn.set_align(lv.ALIGN.BOTTOM_MID) #, 10, 40)
        back_lbl = lv.label(back_btn)
        back_lbl.set_text("Return to DayView")
        back_lbl.set_style_text_align(lv.TEXT_ALIGN.CENTER, 0)
        back_btn.add_event_cb(self._back_cb, lv.EVENT.CLICKED, None)

        container = lv.obj(self.scr)
        container.set_size(lv.pct(100), lv.pct(90))
        container.set_flex_flow(lv.FLEX_FLOW.COLUMN)
        container.set_flex_align(lv.FLEX_ALIGN.START, lv.FLEX_ALIGN.CENTER, lv.FLEX_ALIGN.CENTER)
        container.set_style_pad_all(10, 0)
        container.set_style_pad_row(10, 0) # Spacing between rows

        self.ta_person   = self.create_form_row(container, "Person:", "Name")
        self.ta_date     = self.create_form_row(container, "Date:", "YYYY-MM-DD")
        self.ta_time     = self.create_form_row(container, "Time:", "HH:MM")
        self.ta_activity = self.create_form_row(container, "Activity:", "What are you doing?")
        self.ta_person.set_text(self.person)
        self.ta_date.set_text(self.date_str)

        self.ta_time.add_event_cb(self._ta_event_cb, lv.EVENT.FOCUSED, None)
        self.ta_time.add_event_cb(self._ta_event_cb, lv.EVENT.DEFOCUSED, None)
        self.ta_activity.add_event_cb(self._ta_event_cb, lv.EVENT.FOCUSED, None)
        self.ta_activity.add_event_cb(self._ta_event_cb, lv.EVENT.DEFOCUSED, None)

        # Submit button
        self.btn_submit = lv.button(container)
        self.btn_submit.set_size(lv.pct(90), 40)
        #self.btn_submit.set_align(lv.ALIGN.CENTER)  #, 0, 300)
        submit_lbl = lv.label(self.btn_submit)
        submit_lbl.set_text("Submit")
        self.btn_submit.set_style_bg_color(lv.color_hex(0xCCCCCC), 0)
        self.btn_submit.add_event_cb(self._submit_cb, lv.EVENT.CLICKED, None)

    def create_form_row(self, parent, label_text, placeholder):
        """Helper function to create a label and text area row"""
        # Create a row container
        row = lv.obj(parent)
        row.set_size(lv.pct(100), lv.SIZE_CONTENT)
        row.set_flex_flow(lv.FLEX_FLOW.ROW)
        row.set_flex_align(lv.FLEX_ALIGN.SPACE_BETWEEN, lv.FLEX_ALIGN.CENTER, lv.FLEX_ALIGN.CENTER)
        row.set_style_pad_all(0, 0)
        row.set_style_bg_opa(lv.OPA.TRANSP, 0)
        row.set_style_border_width(0, 0)
        # Create Label
        label = lv.label(row)
        label.set_text(label_text)
        label.set_style_text_font(theme.header_font, 0)
        label.set_width(lv.pct(30))
        # Create Text Area
        ta = lv.textarea(row)
        ta.set_one_line(True)
        ta.set_placeholder_text(placeholder)
        ta.set_width(lv.pct(65))
        ta.set_style_text_font(theme.header_font, 0)
        # ta.add_event_cb(self._ta_event_cb, lv.EVENT.FOCUSED, None)
        # ta.add_event_cb(self._ta_event_cb, lv.EVENT.DEFOCUSED, None)
        return ta

    @micropython.native # type: ignore
    def time_cb(self,e):
        global ta_time
        code = e.get_code()
        btnx = e.get_target_obj()
        lblx = btnx.get_child(0)
        txt = lblx.get_text()
        self.ta_time.set_text(txt)

    @micropython.native # type: ignore
    def time2_cb(self,e):
        global ta_time
        txt = self.ta_time.get_text()
        code = e.get_code()
        btn = e.get_target_obj()
        lbl = btn.get_child(0)
        txt = txt + lbl.get_text()
        self.ta_time.set_text(txt[:5])
        self.balloon_time.add_flag(lv.obj.FLAG.HIDDEN)
        self.have_data()

    @micropython.native # type: ignore
    def act_cb(self,e):
        global ta_activity
        code = e.get_code()
        btn = e.get_target_obj()
        lbl = btn.get_child(0)
        self.ta_activity.set_text(lbl.get_text())
        self.have_data()

    def _balloons(self):
        self.balloon_time = lv.obj(self.scr)
        self.balloon_time.set_pos(50,220)
        self.balloon_time.set_size(lv.pct(90), lv.pct(40))
        self.balloon_time.set_flex_flow(lv.FLEX_FLOW.ROW_WRAP)
        self.balloon_time.set_flex_align(lv.FLEX_ALIGN.START, lv.FLEX_ALIGN.CENTER, lv.FLEX_ALIGN.CENTER)
        self.balloon_time.set_style_pad_all(5, 0)
        self.balloon_time.set_style_pad_row(5, 0) # Spacing between rows
        self.balloon_time.add_flag(lv.obj.FLAG.HIDDEN)
        for i in range(1,24):
            btn_time = lv.button(self.balloon_time)
            btn_time.set_size(60,50)
            btn_time.set_style_radius(20, 0)
            btn_time.set_style_bg_color(lv.color_hex(0x00ffff),0)
            btn_time.add_event_cb(self.time_cb, lv.EVENT.CLICKED, None)
            lbl_time = lv.label(btn_time)
            lbl_time.set_style_text_color(theme.text_dark,0)
            lbl_time.set_style_text_font(lv.font_montserrat_16, 0)
            lbl_time.set_text(f"{i:02}")
            lbl_time.center()
        for t in [":00",":15",":30",":45"]:
            btn_time2 = lv.button(self.balloon_time)
            btn_time2.set_size(60,50)
            btn_time2.set_style_radius(20, 0)
            btn_time2.set_style_bg_color(lv.color_hex(0xffff00),0)
            btn_time2.add_event_cb(self.time2_cb, lv.EVENT.CLICKED, None)
            lbl_time2 = lv.label(btn_time2)
            lbl_time2.set_style_text_color(theme.text_dark,0)
            lbl_time2.set_style_text_font(lv.font_montserrat_16, 0)
            lbl_time2.set_text(f"{t}")
            lbl_time2.center()

        self.balloon_act = lv.obj(self.scr)
        self.balloon_act.set_pos(50,220)
        self.balloon_act.set_size(lv.pct(90), lv.pct(40))
        self.balloon_act.set_flex_flow(lv.FLEX_FLOW.ROW_WRAP)
        self.balloon_act.set_flex_align(lv.FLEX_ALIGN.START, lv.FLEX_ALIGN.CENTER, lv.FLEX_ALIGN.CENTER)
        self.balloon_act.set_style_pad_all(5, 0)
        self.balloon_act.set_style_pad_row(5, 0) # Spacing between rows
        self.balloon_act.add_flag(lv.obj.FLAG.HIDDEN)
        for t in ACTIVITY_TASKS:
            btn_act = lv.button(self.balloon_act)
            btn_act.set_size(lv.SIZE_CONTENT,50)
            btn_act.set_style_radius(20, 0)
            btn_act.set_style_bg_color(lv.color_hex(0x00ffff),0)
            btn_act.add_event_cb(self.act_cb, lv.EVENT.CLICKED, None)
            lbl_act = lv.label(btn_act)
            lbl_act.set_style_text_color(theme.text_dark,0)
            lbl_act.set_style_text_font(lv.font_montserrat_16, 0)
            lbl_act.set_text(f"{t}")
            lbl_act.center()

    def show_balloons_time(self):
        self.balloon_time.remove_flag(lv.obj.FLAG.HIDDEN)

    def hide_balloons_time(self):
        self.balloon_time.add_flag(lv.obj.FLAG.HIDDEN)

    def show_balloons_act(self):
        self.balloon_act.remove_flag(lv.obj.FLAG.HIDDEN)

    def hide_balloons_act(self):
        self.balloon_act.add_flag(lv.obj.FLAG.HIDDEN)


    def _ta_event_cb(self, e):
        code = e.get_code()
        ta = e.get_target_obj()
        text = ""
        if code == lv.EVENT.CLICKED or code == lv.EVENT.FOCUSED:
            text = ta.get_placeholder_text()
            lv.group_focus_obj(ta)
            if text == "HH:MM":
                #self.balloon_time.remove_flag(lv.obj.FLAG.HIDDEN)
                self.show_balloons_time()
            else:
                #self.balloon_act.remove_flag(lv.obj.FLAG.HIDDEN)
                self.show_balloons_act()
        if code == lv.EVENT.DEFOCUSED:
            #self.balloon_act.add_flag(lv.obj.FLAG.HIDDEN)
            self.hide_balloons_act()
        if code == lv.EVENT.DEFOCUSED and len(text) > 4:
            #self.balloon_time.add_flag(lv.obj.FLAG.HIDDEN)
            self.hide_balloons_time()


    def _submit_cb(self, e):
        time_text = self.ta_time.get_text().strip()
        act_text = self.ta_activity.get_text().strip()
        if not time_text or not act_text:
            return
        self.scheduler.add_activity(self.person, self.date_str, time_text, act_text)
        DayView(self.scheduler, self.date_str).show()

    def _back_cb(self, e):
        DayView(self.scheduler, self.date_str).show()

    def have_data(self):
        time = self.ta_time.get_text()
        act = self.ta_activity.get_text()
        if len(time) > 4 and len(act) > 1:
            self.btn_submit.set_style_bg_color(lv.color_hex(0x008080),0)
            self.btn_submit.add_event_cb(self._submit_cb, lv.EVENT.CLICKED, None)


# ===================== MAIN =====================
if __name__ == "__main__":
    scheduler = ActivityScheduler(PERSONS)
    month_view = MonthView(scheduler)
    month_view.show()
    if LOAD_AT_STARTUP:
        #month_view.load_activity_file()
        #DayView(scheduler,month_view.today() )
        pass
else:
    # assumes you did not add a battery for the RTC
    rtc = RTC()
    rtc.datetime((2026, 9, 25,4,12,30,0,0))
    scheduler = ActivityScheduler(PERSONS)
    month_view = MonthView(scheduler)
    month_view.show()
    if LOAD_AT_STARTUP:
        #month_view.load_activity_file()
        #DayView(scheduler,'2026-09-21')
        pass