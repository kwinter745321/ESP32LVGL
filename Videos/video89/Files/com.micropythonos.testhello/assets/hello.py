import lvgl as lv
from mpos import Activity

class Hello(Activity):

    def onCreate(self):
        screen = lv.obj()
        label = lv.label(screen)
        label.set_text('test hello')
        label.center()
        self.setContentView(screen)
        