from typing import ClassVar, Final, Callable, Any, Optional, Self, TypedDict


opa_t = int
state_t = int
part_t = int
result_t = int
anim_t = int
rb_color_t = int
align_t = int
dir_t = int
color_format_t = int
palette_t = int
thread_prio_t = int
font_glyph_format_t = int
font_subpx_t = int
font_kerning_t = int
text_flag_t = int
text_align_t = int
base_dir_t = int
layout_t = int
flex_align_t = int
flex_flow_t = int
grid_align_t = int
blend_mode_t = int
text_decor_t = int
border_side_t = int
grad_dir_t = int
grad_extend_t = int
style_res_t = int
event_t = int
fs_res_t = int
fs_mode_t = int
draw_task_type_t = int
draw_task_state_t = int
display_rotation_t = int
display_render_mode_t = int
scr_load_anim_t = int
scrollbar_mode_t = int
scroll_snap_t = int
style_state_cmp_t = int
layer_type_t = int
key_t = int
group_refocus_policy_t = int
indev_type_t = int
indev_state_t = int
indev_mode_t = int
cover_res_t = int
span_overflow_t = int
span_mode_t = int
subject_type_t = int
draw_sw_mask_res_t = int
draw_sw_mask_type_t = int
draw_sw_mask_line_side_t = int

style_prop_t = int
grad_color_t = int
event_code_t = int
style_selector_t = int
anim_enable_t = int
event_list_t = int
ll_node_t = int
value_precise_t = float
fs_whence_t = int
screen_load_anim_t = int



class Blob(object):

    def __dereference__(self, *, size: Optional[int] = None) -> memoryview | None:
        ...
        
    def __cast__(self, *, type: Any=None) -> Any:
        ...

    def __eq__(self, other: Any) -> bool:
        ...
        
    def __ne__(self, other: Any) -> bool:
        ...
        

class Struct(object):

    def __cast_instance__(self, ptr_obj: "Struct") -> Self:
        ...

    def __dereference__(self, *, size: Optional[int] = None) -> memoryview | None:
        ...
        
    def __cast__(self, *, type: Any=None) -> Any:
        ...
        
    def __get_item__(self, index: int) -> Any:
        ...
        
    def __eq__(self, other: Any) -> bool:
        ...
        
    def __ne__(self, other: Any) -> bool:
        ...


class C_Array(object):

    def __cast_instance__(self, ptr_obj: "C_Array") -> Self:
        ...

    def __dereference__(self, *, size: Optional[int] = None) -> memoryview | None:
        ...
        
    def __cast__(self, *, type: Any=None) -> Any:
        ...

    def __get_item__(self, index: int) -> Any:
        ...
        
    def __eq__(self, other: Any) -> bool:
        ...
        
    def __ne__(self, other: Any) -> bool:
        ...


class C_Pointer(Struct):

    @property
    def ptr_val(self) -> Any:
        ...
        
    @ptr_val.setter
    def ptr_val(self, *, value: Any):
        ...
        
    @property
    def str_val(self) -> str:
        ...
        
    @str_val.setter
    def str_val(self, *, value: str):
        ...
        
    @property
    def int_val(self) -> int:
        ...
        
    @int_val.setter
    def int_val(self, *, value: int):
        ...
        
    @property
    def uint_val(self) -> int:
        ...
        
    @uint_val.setter
    def uint_val(self, *, value: int):
        ...


DPI_DEF: Final[int] = ...
DRAW_BUF_STRIDE_ALIGN: Final[int] = ...
DRAW_BUF_ALIGN: Final[int] = ...
ANIM_REPEAT_INFINITE: Final[int] = ...
ANIM_PLAYTIME_INFINITE: Final[int] = ...
SIZE_CONTENT: Final[int] = ...
COLOR_DEPTH: Final[int] = ...
IMAGE_HEADER_MAGIC: Final[int] = ...
STRIDE_AUTO: Final[int] = ...
GRID_CONTENT: Final[int] = ...
GRID_TEMPLATE_LAST: Final[int] = ...
SCALE_NONE: Final[int] = ...
RADIUS_CIRCLE: Final[int] = ...
LABEL_DOT_NUM: Final[int] = ...
LABEL_POS_LAST: Final[int] = ...
LABEL_TEXT_SELECTION_OFF: Final[int] = ...
BUTTONMATRIX_BUTTON_NONE: Final[int] = ...
CHART_POINT_NONE: Final[int] = ...
DROPDOWN_POS_LAST: Final[int] = ...
SCALE_TOTAL_TICK_COUNT_DEFAULT: Final[int] = ...
SCALE_MAJOR_TICK_EVERY_DEFAULT: Final[int] = ...
SCALE_LABEL_ENABLED_DEFAULT: Final[int] = ...
TEXTAREA_CURSOR_LAST: Final[int] = ...
TABLE_CELL_NONE: Final[int] = ...

class LOG_LEVEL(object):

    TRACE: ClassVar[int] = ...
    INFO: ClassVar[int] = ...
    WARN: ClassVar[int] = ...
    ERROR: ClassVar[int] = ...
    USER: ClassVar[int] = ...
    NONE: ClassVar[int] = ...
    
    def __init__(self, *, parent: "obj"):
        ...


class COORD(object):

    MAX: ClassVar[int] = ...
    MIN: ClassVar[int] = ...
    
    def __init__(self, *, parent: "obj"):
        ...


class _type_OPA(TypedDict, total=False):
    pass


class OPA(object):

    TRANSP: ClassVar[int] = ...
    _0: ClassVar[int] = ...
    _10: ClassVar[int] = ...
    _20: ClassVar[int] = ...
    _30: ClassVar[int] = ...
    _40: ClassVar[int] = ...
    _50: ClassVar[int] = ...
    _60: ClassVar[int] = ...
    _70: ClassVar[int] = ...
    _80: ClassVar[int] = ...
    _90: ClassVar[int] = ...
    _100: ClassVar[int] = ...
    COVER: ClassVar[int] = ...
    
    def __init__(self, *, kwargs: _type_OPA = dict()):
        ...


class STR_SYMBOL(object):

    BULLET: ClassVar[int] = ...
    AUDIO: ClassVar[int] = ...
    VIDEO: ClassVar[int] = ...
    LIST: ClassVar[int] = ...
    OK: ClassVar[int] = ...
    CLOSE: ClassVar[int] = ...
    POWER: ClassVar[int] = ...
    SETTINGS: ClassVar[int] = ...
    HOME: ClassVar[int] = ...
    DOWNLOAD: ClassVar[int] = ...
    DRIVE: ClassVar[int] = ...
    REFRESH: ClassVar[int] = ...
    MUTE: ClassVar[int] = ...
    VOLUME_MID: ClassVar[int] = ...
    VOLUME_MAX: ClassVar[int] = ...
    IMAGE: ClassVar[int] = ...
    TINT: ClassVar[int] = ...
    PREV: ClassVar[int] = ...
    PLAY: ClassVar[int] = ...
    PAUSE: ClassVar[int] = ...
    STOP: ClassVar[int] = ...
    NEXT: ClassVar[int] = ...
    EJECT: ClassVar[int] = ...
    LEFT: ClassVar[int] = ...
    RIGHT: ClassVar[int] = ...
    PLUS: ClassVar[int] = ...
    MINUS: ClassVar[int] = ...
    EYE_OPEN: ClassVar[int] = ...
    EYE_CLOSE: ClassVar[int] = ...
    WARNING: ClassVar[int] = ...
    SHUFFLE: ClassVar[int] = ...
    UP: ClassVar[int] = ...
    DOWN: ClassVar[int] = ...
    LOOP: ClassVar[int] = ...
    DIRECTORY: ClassVar[int] = ...
    UPLOAD: ClassVar[int] = ...
    CALL: ClassVar[int] = ...
    CUT: ClassVar[int] = ...
    COPY: ClassVar[int] = ...
    SAVE: ClassVar[int] = ...
    BARS: ClassVar[int] = ...
    ENVELOPE: ClassVar[int] = ...
    CHARGE: ClassVar[int] = ...
    PASTE: ClassVar[int] = ...
    BELL: ClassVar[int] = ...
    KEYBOARD: ClassVar[int] = ...
    GPS: ClassVar[int] = ...
    FILE: ClassVar[int] = ...
    WIFI: ClassVar[int] = ...
    BATTERY_FULL: ClassVar[int] = ...
    BATTERY_3: ClassVar[int] = ...
    BATTERY_2: ClassVar[int] = ...
    BATTERY_1: ClassVar[int] = ...
    BATTERY_EMPTY: ClassVar[int] = ...
    USB: ClassVar[int] = ...
    BLUETOOTH: ClassVar[int] = ...
    TRASH: ClassVar[int] = ...
    EDIT: ClassVar[int] = ...
    BACKSPACE: ClassVar[int] = ...
    SD_CARD: ClassVar[int] = ...
    NEW_LINE: ClassVar[int] = ...
    DUMMY: ClassVar[int] = ...
    
    def __init__(self, *, parent: "obj"):
        ...


class STYLE(object):

    PROP_INV: ClassVar[int] = ...
    WIDTH: ClassVar[int] = ...
    HEIGHT: ClassVar[int] = ...
    LENGTH: ClassVar[int] = ...
    MIN_WIDTH: ClassVar[int] = ...
    MAX_WIDTH: ClassVar[int] = ...
    MIN_HEIGHT: ClassVar[int] = ...
    MAX_HEIGHT: ClassVar[int] = ...
    X: ClassVar[int] = ...
    Y: ClassVar[int] = ...
    ALIGN: ClassVar[int] = ...
    RADIUS: ClassVar[int] = ...
    PAD_TOP: ClassVar[int] = ...
    PAD_BOTTOM: ClassVar[int] = ...
    PAD_LEFT: ClassVar[int] = ...
    PAD_RIGHT: ClassVar[int] = ...
    PAD_ROW: ClassVar[int] = ...
    PAD_COLUMN: ClassVar[int] = ...
    LAYOUT: ClassVar[int] = ...
    MARGIN_TOP: ClassVar[int] = ...
    MARGIN_BOTTOM: ClassVar[int] = ...
    MARGIN_LEFT: ClassVar[int] = ...
    MARGIN_RIGHT: ClassVar[int] = ...
    BG_COLOR: ClassVar[int] = ...
    BG_OPA: ClassVar[int] = ...
    BG_GRAD_DIR: ClassVar[int] = ...
    BG_MAIN_STOP: ClassVar[int] = ...
    BG_GRAD_STOP: ClassVar[int] = ...
    BG_GRAD_COLOR: ClassVar[int] = ...
    BG_MAIN_OPA: ClassVar[int] = ...
    BG_GRAD_OPA: ClassVar[int] = ...
    BG_GRAD: ClassVar[int] = ...
    BASE_DIR: ClassVar[int] = ...
    BG_IMAGE_SRC: ClassVar[int] = ...
    BG_IMAGE_OPA: ClassVar[int] = ...
    BG_IMAGE_RECOLOR: ClassVar[int] = ...
    BG_IMAGE_RECOLOR_OPA: ClassVar[int] = ...
    BG_IMAGE_TILED: ClassVar[int] = ...
    CLIP_CORNER: ClassVar[int] = ...
    BORDER_WIDTH: ClassVar[int] = ...
    BORDER_COLOR: ClassVar[int] = ...
    BORDER_OPA: ClassVar[int] = ...
    BORDER_SIDE: ClassVar[int] = ...
    BORDER_POST: ClassVar[int] = ...
    OUTLINE_WIDTH: ClassVar[int] = ...
    OUTLINE_COLOR: ClassVar[int] = ...
    OUTLINE_OPA: ClassVar[int] = ...
    OUTLINE_PAD: ClassVar[int] = ...
    SHADOW_WIDTH: ClassVar[int] = ...
    SHADOW_COLOR: ClassVar[int] = ...
    SHADOW_OPA: ClassVar[int] = ...
    SHADOW_OFFSET_X: ClassVar[int] = ...
    SHADOW_OFFSET_Y: ClassVar[int] = ...
    SHADOW_SPREAD: ClassVar[int] = ...
    IMAGE_OPA: ClassVar[int] = ...
    IMAGE_RECOLOR: ClassVar[int] = ...
    IMAGE_RECOLOR_OPA: ClassVar[int] = ...
    LINE_WIDTH: ClassVar[int] = ...
    LINE_DASH_WIDTH: ClassVar[int] = ...
    LINE_DASH_GAP: ClassVar[int] = ...
    LINE_ROUNDED: ClassVar[int] = ...
    LINE_COLOR: ClassVar[int] = ...
    LINE_OPA: ClassVar[int] = ...
    ARC_WIDTH: ClassVar[int] = ...
    ARC_ROUNDED: ClassVar[int] = ...
    ARC_COLOR: ClassVar[int] = ...
    ARC_OPA: ClassVar[int] = ...
    ARC_IMAGE_SRC: ClassVar[int] = ...
    TEXT_COLOR: ClassVar[int] = ...
    TEXT_OPA: ClassVar[int] = ...
    TEXT_FONT: ClassVar[int] = ...
    TEXT_LETTER_SPACE: ClassVar[int] = ...
    TEXT_LINE_SPACE: ClassVar[int] = ...
    TEXT_DECOR: ClassVar[int] = ...
    TEXT_ALIGN: ClassVar[int] = ...
    OPA: ClassVar[int] = ...
    OPA_LAYERED: ClassVar[int] = ...
    COLOR_FILTER_DSC: ClassVar[int] = ...
    COLOR_FILTER_OPA: ClassVar[int] = ...
    ANIM: ClassVar[int] = ...
    ANIM_DURATION: ClassVar[int] = ...
    TRANSITION: ClassVar[int] = ...
    BLEND_MODE: ClassVar[int] = ...
    TRANSFORM_WIDTH: ClassVar[int] = ...
    TRANSFORM_HEIGHT: ClassVar[int] = ...
    TRANSLATE_X: ClassVar[int] = ...
    TRANSLATE_Y: ClassVar[int] = ...
    TRANSFORM_SCALE_X: ClassVar[int] = ...
    TRANSFORM_SCALE_Y: ClassVar[int] = ...
    TRANSFORM_ROTATION: ClassVar[int] = ...
    TRANSFORM_PIVOT_X: ClassVar[int] = ...
    TRANSFORM_PIVOT_Y: ClassVar[int] = ...
    TRANSFORM_SKEW_X: ClassVar[int] = ...
    TRANSFORM_SKEW_Y: ClassVar[int] = ...
    BITMAP_MASK_SRC: ClassVar[int] = ...
    ROTARY_SENSITIVITY: ClassVar[int] = ...
    FLEX_FLOW: ClassVar[int] = ...
    FLEX_MAIN_PLACE: ClassVar[int] = ...
    FLEX_CROSS_PLACE: ClassVar[int] = ...
    FLEX_TRACK_PLACE: ClassVar[int] = ...
    FLEX_GROW: ClassVar[int] = ...
    GRID_COLUMN_ALIGN: ClassVar[int] = ...
    GRID_ROW_ALIGN: ClassVar[int] = ...
    GRID_ROW_DSC_ARRAY: ClassVar[int] = ...
    GRID_COLUMN_DSC_ARRAY: ClassVar[int] = ...
    GRID_CELL_COLUMN_POS: ClassVar[int] = ...
    GRID_CELL_COLUMN_SPAN: ClassVar[int] = ...
    GRID_CELL_X_ALIGN: ClassVar[int] = ...
    GRID_CELL_ROW_POS: ClassVar[int] = ...
    GRID_CELL_ROW_SPAN: ClassVar[int] = ...
    GRID_CELL_Y_ALIGN: ClassVar[int] = ...
    LAST_BUILT_IN_PROP: ClassVar[int] = ...
    NUM_BUILT_IN_PROPS: ClassVar[int] = ...
    PROP_ANY: ClassVar[int] = ...
    PROP_CONST: ClassVar[int] = ...
    
    def __init__(self, *, parent: "obj"):
        ...


class _type_STATE(TypedDict, total=False):
    pass


class STATE(object):

    DEFAULT: ClassVar[int] = ...
    CHECKED: ClassVar[int] = ...
    FOCUSED: ClassVar[int] = ...
    FOCUS_KEY: ClassVar[int] = ...
    EDITED: ClassVar[int] = ...
    HOVERED: ClassVar[int] = ...
    PRESSED: ClassVar[int] = ...
    SCROLLED: ClassVar[int] = ...
    DISABLED: ClassVar[int] = ...
    USER_1: ClassVar[int] = ...
    USER_2: ClassVar[int] = ...
    USER_3: ClassVar[int] = ...
    USER_4: ClassVar[int] = ...
    ANY: ClassVar[int] = ...
    
    def __init__(self, *, kwargs: _type_STATE = dict()):
        ...


class _type_PART(TypedDict, total=False):
    pass


class PART(object):

    MAIN: ClassVar[int] = ...
    SCROLLBAR: ClassVar[int] = ...
    INDICATOR: ClassVar[int] = ...
    KNOB: ClassVar[int] = ...
    SELECTED: ClassVar[int] = ...
    ITEMS: ClassVar[int] = ...
    CURSOR: ClassVar[int] = ...
    CUSTOM_FIRST: ClassVar[int] = ...
    ANY: ClassVar[int] = ...
    
    def __init__(self, *, kwargs: _type_PART = dict()):
        ...


class PART_TEXTAREA(object):

    PLACEHOLDER: ClassVar[int] = ...
    
    def __init__(self, *, parent: "obj"):
        ...


class _type_RESULT(TypedDict, total=False):
    pass


class RESULT(object):
    """
    LVGL error codes. 
    """

    INVALID: ClassVar[int] = ...
    OK: ClassVar[int] = ...
    
    def __init__(self, *, kwargs: _type_RESULT = dict()):
        ...


class _type_ANIM(TypedDict, total=False):
    pass


class ANIM(object):

    OFF: ClassVar[int] = ...
    ON: ClassVar[int] = ...
    
    def __init__(self, *, kwargs: _type_ANIM = dict()):
        ...


class _type_RB_COLOR(TypedDict, total=False):
    pass


class RB_COLOR(object):

    RED: ClassVar[int] = ...
    BLACK: ClassVar[int] = ...
    
    def __init__(self, *, kwargs: _type_RB_COLOR = dict()):
        ...


class _type_ALIGN(TypedDict, total=False):
    pass


class ALIGN(object):
    """
    Alignments 
    """

    DEFAULT: ClassVar[int] = ...
    TOP_LEFT: ClassVar[int] = ...
    TOP_MID: ClassVar[int] = ...
    TOP_RIGHT: ClassVar[int] = ...
    BOTTOM_LEFT: ClassVar[int] = ...
    BOTTOM_MID: ClassVar[int] = ...
    BOTTOM_RIGHT: ClassVar[int] = ...
    LEFT_MID: ClassVar[int] = ...
    RIGHT_MID: ClassVar[int] = ...
    CENTER: ClassVar[int] = ...
    OUT_TOP_LEFT: ClassVar[int] = ...
    OUT_TOP_MID: ClassVar[int] = ...
    OUT_TOP_RIGHT: ClassVar[int] = ...
    OUT_BOTTOM_LEFT: ClassVar[int] = ...
    OUT_BOTTOM_MID: ClassVar[int] = ...
    OUT_BOTTOM_RIGHT: ClassVar[int] = ...
    OUT_LEFT_TOP: ClassVar[int] = ...
    OUT_LEFT_MID: ClassVar[int] = ...
    OUT_LEFT_BOTTOM: ClassVar[int] = ...
    OUT_RIGHT_TOP: ClassVar[int] = ...
    OUT_RIGHT_MID: ClassVar[int] = ...
    OUT_RIGHT_BOTTOM: ClassVar[int] = ...
    
    def __init__(self, *, kwargs: _type_ALIGN = dict()):
        ...


class _type_DIR(TypedDict, total=False):
    pass


class DIR(object):

    NONE: ClassVar[int] = ...
    LEFT: ClassVar[int] = ...
    RIGHT: ClassVar[int] = ...
    TOP: ClassVar[int] = ...
    BOTTOM: ClassVar[int] = ...
    HOR: ClassVar[int] = ...
    VER: ClassVar[int] = ...
    ALL: ClassVar[int] = ...
    
    def __init__(self, *, kwargs: _type_DIR = dict()):
        ...


class _type_COLOR_FORMAT(TypedDict, total=False):
    pass


class COLOR_FORMAT(object):

    UNKNOWN: ClassVar[int] = ...
    RAW: ClassVar[int] = ...
    RAW_ALPHA: ClassVar[int] = ...
    L8: ClassVar[int] = ...
    I1: ClassVar[int] = ...
    I2: ClassVar[int] = ...
    I4: ClassVar[int] = ...
    I8: ClassVar[int] = ...
    A8: ClassVar[int] = ...
    RGB565: ClassVar[int] = ...
    ARGB8565: ClassVar[int] = ...
    RGB565A8: ClassVar[int] = ...
    AL88: ClassVar[int] = ...
    RGB888: ClassVar[int] = ...
    ARGB8888: ClassVar[int] = ...
    XRGB8888: ClassVar[int] = ...
    A1: ClassVar[int] = ...
    A2: ClassVar[int] = ...
    A4: ClassVar[int] = ...
    YUV_START: ClassVar[int] = ...
    I420: ClassVar[int] = ...
    I422: ClassVar[int] = ...
    I444: ClassVar[int] = ...
    I400: ClassVar[int] = ...
    NV21: ClassVar[int] = ...
    NV12: ClassVar[int] = ...
    YUY2: ClassVar[int] = ...
    UYVY: ClassVar[int] = ...
    YUV_END: ClassVar[int] = ...
    NATIVE: ClassVar[int] = ...
    NATIVE_WITH_ALPHA: ClassVar[int] = ...
    
    def __init__(self, *, kwargs: _type_COLOR_FORMAT = dict()):
        ...


class _type_PALETTE(TypedDict, total=False):
    pass


class PALETTE(object):

    RED: ClassVar[int] = ...
    PINK: ClassVar[int] = ...
    PURPLE: ClassVar[int] = ...
    DEEP_PURPLE: ClassVar[int] = ...
    INDIGO: ClassVar[int] = ...
    BLUE: ClassVar[int] = ...
    LIGHT_BLUE: ClassVar[int] = ...
    CYAN: ClassVar[int] = ...
    TEAL: ClassVar[int] = ...
    GREEN: ClassVar[int] = ...
    LIGHT_GREEN: ClassVar[int] = ...
    LIME: ClassVar[int] = ...
    YELLOW: ClassVar[int] = ...
    AMBER: ClassVar[int] = ...
    ORANGE: ClassVar[int] = ...
    DEEP_ORANGE: ClassVar[int] = ...
    BROWN: ClassVar[int] = ...
    BLUE_GREY: ClassVar[int] = ...
    GREY: ClassVar[int] = ...
    LAST: ClassVar[int] = ...
    NONE: ClassVar[int] = ...
    
    def __init__(self, *, kwargs: _type_PALETTE = dict()):
        ...


class _type_THREAD_PRIO(TypedDict, total=False):
    pass


class THREAD_PRIO(object):

    LOWEST: ClassVar[int] = ...
    LOW: ClassVar[int] = ...
    MID: ClassVar[int] = ...
    HIGH: ClassVar[int] = ...
    HIGHEST: ClassVar[int] = ...
    
    def __init__(self, *, kwargs: _type_THREAD_PRIO = dict()):
        ...


class CACHE_RESERVE_COND(object):

    OK: ClassVar[int] = ...
    TOO_LARGE: ClassVar[int] = ...
    NEED_VICTIM: ClassVar[int] = ...
    ERROR: ClassVar[int] = ...
    
    def __init__(self, *, parent: "obj"):
        ...


class _type_FONT_GLYPH_FORMAT(TypedDict, total=False):
    pass


class FONT_GLYPH_FORMAT(object):
    """
    The font format. 
    """

    NONE: ClassVar[int] = ...
    A1: ClassVar[int] = ...
    A2: ClassVar[int] = ...
    A4: ClassVar[int] = ...
    A8: ClassVar[int] = ...
    IMAGE: ClassVar[int] = ...
    VECTOR: ClassVar[int] = ...
    SVG: ClassVar[int] = ...
    CUSTOM: ClassVar[int] = ...
    
    def __init__(self, *, kwargs: _type_FONT_GLYPH_FORMAT = dict()):
        ...


class _type_FONT_SUBPX(TypedDict, total=False):
    pass


class FONT_SUBPX(object):
    """
    The bitmaps might be upscaled by 3 to achieve subpixel rendering. 
    """

    NONE: ClassVar[int] = ...
    HOR: ClassVar[int] = ...
    VER: ClassVar[int] = ...
    BOTH: ClassVar[int] = ...
    
    def __init__(self, *, kwargs: _type_FONT_SUBPX = dict()):
        ...


class _type_FONT_KERNING(TypedDict, total=False):
    pass


class FONT_KERNING(object):
    """
    Adjust letter spacing for specific character pairs. 
    """

    NORMAL: ClassVar[int] = ...
    NONE: ClassVar[int] = ...
    
    def __init__(self, *, kwargs: _type_FONT_KERNING = dict()):
        ...


class _type_TEXT_FLAG(TypedDict, total=False):
    pass


class TEXT_FLAG(object):
    """
    Options for text rendering. 
    """

    NONE: ClassVar[int] = ...
    EXPAND: ClassVar[int] = ...
    FIT: ClassVar[int] = ...
    BREAK_ALL: ClassVar[int] = ...
    
    def __init__(self, *, kwargs: _type_TEXT_FLAG = dict()):
        ...


class _type_TEXT_ALIGN(TypedDict, total=False):
    pass


class TEXT_ALIGN(object):
    """
    Label align policy 
    """

    AUTO: ClassVar[int] = ...
    LEFT: ClassVar[int] = ...
    CENTER: ClassVar[int] = ...
    RIGHT: ClassVar[int] = ...
    
    def __init__(self, *, kwargs: _type_TEXT_ALIGN = dict()):
        ...


class _type_BASE_DIR(TypedDict, total=False):
    pass


class BASE_DIR(object):

    LTR: ClassVar[int] = ...
    RTL: ClassVar[int] = ...
    AUTO: ClassVar[int] = ...
    NEUTRAL: ClassVar[int] = ...
    WEAK: ClassVar[int] = ...
    
    def __init__(self, *, kwargs: _type_BASE_DIR = dict()):
        ...


class _type_LAYOUT(TypedDict, total=False):
    pass


class LAYOUT(object):

    NONE: ClassVar[int] = ...
    FLEX: ClassVar[int] = ...
    GRID: ClassVar[int] = ...
    LAST: ClassVar[int] = ...
    
    def __init__(self, *, kwargs: _type_LAYOUT = dict()):
        ...


class _type_FLEX_ALIGN(TypedDict, total=False):
    pass


class FLEX_ALIGN(object):

    START: ClassVar[int] = ...
    END: ClassVar[int] = ...
    CENTER: ClassVar[int] = ...
    SPACE_EVENLY: ClassVar[int] = ...
    SPACE_AROUND: ClassVar[int] = ...
    SPACE_BETWEEN: ClassVar[int] = ...
    
    def __init__(self, *, kwargs: _type_FLEX_ALIGN = dict()):
        ...


class _type_FLEX_FLOW(TypedDict, total=False):
    pass


class FLEX_FLOW(object):

    ROW: ClassVar[int] = ...
    COLUMN: ClassVar[int] = ...
    ROW_WRAP: ClassVar[int] = ...
    ROW_REVERSE: ClassVar[int] = ...
    ROW_WRAP_REVERSE: ClassVar[int] = ...
    COLUMN_WRAP: ClassVar[int] = ...
    COLUMN_REVERSE: ClassVar[int] = ...
    COLUMN_WRAP_REVERSE: ClassVar[int] = ...
    
    def __init__(self, *, kwargs: _type_FLEX_FLOW = dict()):
        ...


class _type_GRID_ALIGN(TypedDict, total=False):
    pass


class GRID_ALIGN(object):

    START: ClassVar[int] = ...
    CENTER: ClassVar[int] = ...
    END: ClassVar[int] = ...
    STRETCH: ClassVar[int] = ...
    SPACE_EVENLY: ClassVar[int] = ...
    SPACE_AROUND: ClassVar[int] = ...
    SPACE_BETWEEN: ClassVar[int] = ...
    
    def __init__(self, *, kwargs: _type_GRID_ALIGN = dict()):
        ...


class _type_BLEND_MODE(TypedDict, total=False):
    pass


class BLEND_MODE(object):
    """
    Possible options for blending opaque drawings 
    """

    NORMAL: ClassVar[int] = ...
    ADDITIVE: ClassVar[int] = ...
    SUBTRACTIVE: ClassVar[int] = ...
    MULTIPLY: ClassVar[int] = ...
    
    def __init__(self, *, kwargs: _type_BLEND_MODE = dict()):
        ...


class _type_TEXT_DECOR(TypedDict, total=False):
    pass


class TEXT_DECOR(object):
    """
    Some options to apply decorations on texts. 'OR'ed values can be used. 
    """

    NONE: ClassVar[int] = ...
    UNDERLINE: ClassVar[int] = ...
    STRIKETHROUGH: ClassVar[int] = ...
    
    def __init__(self, *, kwargs: _type_TEXT_DECOR = dict()):
        ...


class _type_BORDER_SIDE(TypedDict, total=False):
    pass


class BORDER_SIDE(object):
    """
    Selects on which sides border should be drawn 'OR'ed values can be used. 
    """

    NONE: ClassVar[int] = ...
    BOTTOM: ClassVar[int] = ...
    TOP: ClassVar[int] = ...
    LEFT: ClassVar[int] = ...
    RIGHT: ClassVar[int] = ...
    FULL: ClassVar[int] = ...
    INTERNAL: ClassVar[int] = ...
    
    def __init__(self, *, kwargs: _type_BORDER_SIDE = dict()):
        ...


class _type_GRAD_DIR(TypedDict, total=False):
    pass


class GRAD_DIR(object):
    """
    The direction of the gradient. 
    """

    NONE: ClassVar[int] = ...
    VER: ClassVar[int] = ...
    HOR: ClassVar[int] = ...
    LINEAR: ClassVar[int] = ...
    RADIAL: ClassVar[int] = ...
    CONICAL: ClassVar[int] = ...
    
    def __init__(self, *, kwargs: _type_GRAD_DIR = dict()):
        ...


class _type_GRAD_EXTEND(TypedDict, total=False):
    pass


class GRAD_EXTEND(object):
    """
    Gradient behavior outside the defined range. 
    """

    PAD: ClassVar[int] = ...
    REPEAT: ClassVar[int] = ...
    REFLECT: ClassVar[int] = ...
    
    def __init__(self, *, kwargs: _type_GRAD_EXTEND = dict()):
        ...


class _type_STYLE_RES(TypedDict, total=False):
    pass


class STYLE_RES(object):

    NOT_FOUND: ClassVar[int] = ...
    FOUND: ClassVar[int] = ...
    
    def __init__(self, *, kwargs: _type_STYLE_RES = dict()):
        ...


class _type_EVENT(TypedDict, total=False):
    pass


class EVENT(object):

    ALL: ClassVar[int] = ...
    PRESSED: ClassVar[int] = ...
    PRESSING: ClassVar[int] = ...
    PRESS_LOST: ClassVar[int] = ...
    SHORT_CLICKED: ClassVar[int] = ...
    LONG_PRESSED: ClassVar[int] = ...
    LONG_PRESSED_REPEAT: ClassVar[int] = ...
    CLICKED: ClassVar[int] = ...
    RELEASED: ClassVar[int] = ...
    SCROLL_BEGIN: ClassVar[int] = ...
    SCROLL_THROW_BEGIN: ClassVar[int] = ...
    SCROLL_END: ClassVar[int] = ...
    SCROLL: ClassVar[int] = ...
    GESTURE: ClassVar[int] = ...
    KEY: ClassVar[int] = ...
    ROTARY: ClassVar[int] = ...
    FOCUSED: ClassVar[int] = ...
    DEFOCUSED: ClassVar[int] = ...
    LEAVE: ClassVar[int] = ...
    HIT_TEST: ClassVar[int] = ...
    INDEV_RESET: ClassVar[int] = ...
    HOVER_OVER: ClassVar[int] = ...
    HOVER_LEAVE: ClassVar[int] = ...
    COVER_CHECK: ClassVar[int] = ...
    REFR_EXT_DRAW_SIZE: ClassVar[int] = ...
    DRAW_MAIN_BEGIN: ClassVar[int] = ...
    DRAW_MAIN: ClassVar[int] = ...
    DRAW_MAIN_END: ClassVar[int] = ...
    DRAW_POST_BEGIN: ClassVar[int] = ...
    DRAW_POST: ClassVar[int] = ...
    DRAW_POST_END: ClassVar[int] = ...
    DRAW_TASK_ADDED: ClassVar[int] = ...
    VALUE_CHANGED: ClassVar[int] = ...
    INSERT: ClassVar[int] = ...
    REFRESH: ClassVar[int] = ...
    READY: ClassVar[int] = ...
    CANCEL: ClassVar[int] = ...
    CREATE: ClassVar[int] = ...
    DELETE: ClassVar[int] = ...
    CHILD_CHANGED: ClassVar[int] = ...
    CHILD_CREATED: ClassVar[int] = ...
    CHILD_DELETED: ClassVar[int] = ...
    SCREEN_UNLOAD_START: ClassVar[int] = ...
    SCREEN_LOAD_START: ClassVar[int] = ...
    SCREEN_LOADED: ClassVar[int] = ...
    SCREEN_UNLOADED: ClassVar[int] = ...
    SIZE_CHANGED: ClassVar[int] = ...
    STYLE_CHANGED: ClassVar[int] = ...
    LAYOUT_CHANGED: ClassVar[int] = ...
    GET_SELF_SIZE: ClassVar[int] = ...
    INVALIDATE_AREA: ClassVar[int] = ...
    RESOLUTION_CHANGED: ClassVar[int] = ...
    COLOR_FORMAT_CHANGED: ClassVar[int] = ...
    REFR_REQUEST: ClassVar[int] = ...
    REFR_START: ClassVar[int] = ...
    REFR_READY: ClassVar[int] = ...
    RENDER_START: ClassVar[int] = ...
    RENDER_READY: ClassVar[int] = ...
    FLUSH_START: ClassVar[int] = ...
    FLUSH_FINISH: ClassVar[int] = ...
    FLUSH_WAIT_START: ClassVar[int] = ...
    FLUSH_WAIT_FINISH: ClassVar[int] = ...
    VSYNC: ClassVar[int] = ...
    LAST: ClassVar[int] = ...
    PREPROCESS: ClassVar[int] = ...
    
    def __init__(self, *, kwargs: _type_EVENT = dict()):
        ...


class _type_FS_RES(TypedDict, total=False):
    pass


class FS_RES(object):
    """
    Errors in the file system module. 
    """

    OK: ClassVar[int] = ...
    HW_ERR: ClassVar[int] = ...
    FS_ERR: ClassVar[int] = ...
    NOT_EX: ClassVar[int] = ...
    FULL: ClassVar[int] = ...
    LOCKED: ClassVar[int] = ...
    DENIED: ClassVar[int] = ...
    BUSY: ClassVar[int] = ...
    TOUT: ClassVar[int] = ...
    NOT_IMP: ClassVar[int] = ...
    OUT_OF_MEM: ClassVar[int] = ...
    INV_PARAM: ClassVar[int] = ...
    UNKNOWN: ClassVar[int] = ...
    
    def __init__(self, *, kwargs: _type_FS_RES = dict()):
        ...


class _type_FS_MODE(TypedDict, total=False):
    pass


class FS_MODE(object):
    """
    File open mode. 
    """

    WR: ClassVar[int] = ...
    RD: ClassVar[int] = ...
    
    def __init__(self, *, kwargs: _type_FS_MODE = dict()):
        ...


class FS_SEEK(object):

    SET: ClassVar[int] = ...
    CUR: ClassVar[int] = ...
    END: ClassVar[int] = ...
    
    def __init__(self, *, parent: "obj"):
        ...


class _type_DRAW_TASK_TYPE(TypedDict, total=False):
    pass


class DRAW_TASK_TYPE(object):

    NONE: ClassVar[int] = ...
    FILL: ClassVar[int] = ...
    BORDER: ClassVar[int] = ...
    BOX_SHADOW: ClassVar[int] = ...
    LABEL: ClassVar[int] = ...
    IMAGE: ClassVar[int] = ...
    LAYER: ClassVar[int] = ...
    LINE: ClassVar[int] = ...
    ARC: ClassVar[int] = ...
    TRIANGLE: ClassVar[int] = ...
    MASK_RECTANGLE: ClassVar[int] = ...
    MASK_BITMAP: ClassVar[int] = ...
    VECTOR: ClassVar[int] = ...
    
    def __init__(self, *, kwargs: _type_DRAW_TASK_TYPE = dict()):
        ...


class _type_DRAW_TASK_STATE(TypedDict, total=False):
    pass


class DRAW_TASK_STATE(object):

    WAITING: ClassVar[int] = ...
    QUEUED: ClassVar[int] = ...
    IN_PROGRESS: ClassVar[int] = ...
    READY: ClassVar[int] = ...
    
    def __init__(self, *, kwargs: _type_DRAW_TASK_STATE = dict()):
        ...


class _type_DISPLAY_ROTATION(TypedDict, total=False):
    pass


class DISPLAY_ROTATION(object):

    _0: ClassVar[int] = ...
    _90: ClassVar[int] = ...
    _180: ClassVar[int] = ...
    _270: ClassVar[int] = ...
    
    def __init__(self, *, kwargs: _type_DISPLAY_ROTATION = dict()):
        ...


class _type_DISPLAY_RENDER_MODE(TypedDict, total=False):
    pass


class DISPLAY_RENDER_MODE(object):

    PARTIAL: ClassVar[int] = ...
    DIRECT: ClassVar[int] = ...
    FULL: ClassVar[int] = ...
    
    def __init__(self, *, kwargs: _type_DISPLAY_RENDER_MODE = dict()):
        ...


class _type_SCR_LOAD_ANIM(TypedDict, total=False):
    pass


class SCR_LOAD_ANIM(object):

    NONE: ClassVar[int] = ...
    OVER_LEFT: ClassVar[int] = ...
    OVER_RIGHT: ClassVar[int] = ...
    OVER_TOP: ClassVar[int] = ...
    OVER_BOTTOM: ClassVar[int] = ...
    MOVE_LEFT: ClassVar[int] = ...
    MOVE_RIGHT: ClassVar[int] = ...
    MOVE_TOP: ClassVar[int] = ...
    MOVE_BOTTOM: ClassVar[int] = ...
    FADE_IN: ClassVar[int] = ...
    FADE_ON: ClassVar[int] = ...
    FADE_OUT: ClassVar[int] = ...
    OUT_LEFT: ClassVar[int] = ...
    OUT_RIGHT: ClassVar[int] = ...
    OUT_TOP: ClassVar[int] = ...
    OUT_BOTTOM: ClassVar[int] = ...
    
    def __init__(self, *, kwargs: _type_SCR_LOAD_ANIM = dict()):
        ...


class _type_SCROLLBAR_MODE(TypedDict, total=False):
    pass


class SCROLLBAR_MODE(object):
    """
    Scrollbar modes: shows when should the scrollbars be visible 
    """

    OFF: ClassVar[int] = ...
    ON: ClassVar[int] = ...
    ACTIVE: ClassVar[int] = ...
    AUTO: ClassVar[int] = ...
    
    def __init__(self, *, kwargs: _type_SCROLLBAR_MODE = dict()):
        ...


class _type_SCROLL_SNAP(TypedDict, total=False):
    pass


class SCROLL_SNAP(object):
    """
    Scroll span align options. Tells where to align the snappable children when scroll stops. 
    """

    NONE: ClassVar[int] = ...
    START: ClassVar[int] = ...
    END: ClassVar[int] = ...
    CENTER: ClassVar[int] = ...
    
    def __init__(self, *, kwargs: _type_SCROLL_SNAP = dict()):
        ...


class _type_STYLE_STATE_CMP(TypedDict, total=False):
    pass


class STYLE_STATE_CMP(object):

    SAME: ClassVar[int] = ...
    DIFF_REDRAW: ClassVar[int] = ...
    DIFF_DRAW_PAD: ClassVar[int] = ...
    DIFF_LAYOUT: ClassVar[int] = ...
    
    def __init__(self, *, kwargs: _type_STYLE_STATE_CMP = dict()):
        ...


class _type_LAYER_TYPE(TypedDict, total=False):
    pass


class LAYER_TYPE(object):

    NONE: ClassVar[int] = ...
    SIMPLE: ClassVar[int] = ...
    TRANSFORM: ClassVar[int] = ...
    
    def __init__(self, *, kwargs: _type_LAYER_TYPE = dict()):
        ...


class _type_KEY(TypedDict, total=False):
    pass


class KEY(object):
    """
    Predefined keys to control focused object via lv_group_send(group, c) 
    """

    UP: ClassVar[int] = ...
    DOWN: ClassVar[int] = ...
    RIGHT: ClassVar[int] = ...
    LEFT: ClassVar[int] = ...
    ESC: ClassVar[int] = ...
    DEL: ClassVar[int] = ...
    BACKSPACE: ClassVar[int] = ...
    ENTER: ClassVar[int] = ...
    NEXT: ClassVar[int] = ...
    PREV: ClassVar[int] = ...
    HOME: ClassVar[int] = ...
    END: ClassVar[int] = ...
    
    def __init__(self, *, kwargs: _type_KEY = dict()):
        ...


class _type_GROUP_REFOCUS_POLICY(TypedDict, total=False):
    pass


class GROUP_REFOCUS_POLICY(object):

    NEXT: ClassVar[int] = ...
    PREV: ClassVar[int] = ...
    
    def __init__(self, *, kwargs: _type_GROUP_REFOCUS_POLICY = dict()):
        ...


class _type_INDEV_TYPE(TypedDict, total=False):
    pass


class INDEV_TYPE(object):
    """
    Possible input device types 
    """

    NONE: ClassVar[int] = ...
    POINTER: ClassVar[int] = ...
    KEYPAD: ClassVar[int] = ...
    BUTTON: ClassVar[int] = ...
    ENCODER: ClassVar[int] = ...
    
    def __init__(self, *, kwargs: _type_INDEV_TYPE = dict()):
        ...


class _type_INDEV_STATE(TypedDict, total=False):
    pass


class INDEV_STATE(object):
    """
    States for input devices 
    """

    RELEASED: ClassVar[int] = ...
    PRESSED: ClassVar[int] = ...
    
    def __init__(self, *, kwargs: _type_INDEV_STATE = dict()):
        ...


class _type_INDEV_MODE(TypedDict, total=False):
    pass


class INDEV_MODE(object):

    NONE: ClassVar[int] = ...
    TIMER: ClassVar[int] = ...
    EVENT: ClassVar[int] = ...
    
    def __init__(self, *, kwargs: _type_INDEV_MODE = dict()):
        ...


class _type_COVER_RES(TypedDict, total=False):
    pass


class COVER_RES(object):
    """
    Cover check results. 
    """

    COVER: ClassVar[int] = ...
    NOT_COVER: ClassVar[int] = ...
    MASKED: ClassVar[int] = ...
    
    def __init__(self, *, kwargs: _type_COVER_RES = dict()):
        ...


class FONT_FMT_TXT_CMAP(object):

    FORMAT0_FULL: ClassVar[int] = ...
    SPARSE_FULL: ClassVar[int] = ...
    FORMAT0_TINY: ClassVar[int] = ...
    SPARSE_TINY: ClassVar[int] = ...
    
    def __init__(self, *, parent: "obj"):
        ...


class FONT_FMT_TXT(object):

    PLAIN: ClassVar[int] = ...
    COMPRESSED: ClassVar[int] = ...
    COMPRESSED_NO_PREFILTER: ClassVar[int] = ...
    
    def __init__(self, *, parent: "obj"):
        ...


class ANIM_IMAGE_PART(object):

    MAIN: ClassVar[int] = ...
    
    def __init__(self, *, parent: "obj"):
        ...


class _type_SPAN_OVERFLOW(TypedDict, total=False):
    pass


class SPAN_OVERFLOW(object):

    CLIP: ClassVar[int] = ...
    ELLIPSIS: ClassVar[int] = ...
    LAST: ClassVar[int] = ...
    
    def __init__(self, *, kwargs: _type_SPAN_OVERFLOW = dict()):
        ...


class _type_SPAN_MODE(TypedDict, total=False):
    pass


class SPAN_MODE(object):

    FIXED: ClassVar[int] = ...
    EXPAND: ClassVar[int] = ...
    BREAK: ClassVar[int] = ...
    LAST: ClassVar[int] = ...
    
    def __init__(self, *, kwargs: _type_SPAN_MODE = dict()):
        ...


class _type_SUBJECT_TYPE(TypedDict, total=False):
    pass


class SUBJECT_TYPE(object):
    """
    Values for lv_submect_t's type field. 
    """

    INVALID: ClassVar[int] = ...
    NONE: ClassVar[int] = ...
    INT: ClassVar[int] = ...
    POINTER: ClassVar[int] = ...
    COLOR: ClassVar[int] = ...
    GROUP: ClassVar[int] = ...
    STRING: ClassVar[int] = ...
    
    def __init__(self, *, kwargs: _type_SUBJECT_TYPE = dict()):
        ...


class GRIDNAV_CTRL(object):

    NONE: ClassVar[int] = ...
    ROLLOVER: ClassVar[int] = ...
    SCROLL_FIRST: ClassVar[int] = ...
    HORIZONTAL_MOVE_ONLY: ClassVar[int] = ...
    VERTICAL_MOVE_ONLY: ClassVar[int] = ...
    
    def __init__(self, *, parent: "obj"):
        ...


class _type_DRAW_SW_MASK_RES(TypedDict, total=False):
    pass


class DRAW_SW_MASK_RES(object):

    TRANSP: ClassVar[int] = ...
    FULL_COVER: ClassVar[int] = ...
    CHANGED: ClassVar[int] = ...
    UNKNOWN: ClassVar[int] = ...
    
    def __init__(self, *, kwargs: _type_DRAW_SW_MASK_RES = dict()):
        ...


class _type_DRAW_SW_MASK_TYPE(TypedDict, total=False):
    pass


class DRAW_SW_MASK_TYPE(object):

    LINE: ClassVar[int] = ...
    ANGLE: ClassVar[int] = ...
    RADIUS: ClassVar[int] = ...
    FADE: ClassVar[int] = ...
    MAP: ClassVar[int] = ...
    
    def __init__(self, *, kwargs: _type_DRAW_SW_MASK_TYPE = dict()):
        ...


class _type_DRAW_SW_MASK_LINE_SIDE(TypedDict, total=False):
    pass


class DRAW_SW_MASK_LINE_SIDE(object):

    LEFT: ClassVar[int] = ...
    RIGHT: ClassVar[int] = ...
    TOP: ClassVar[int] = ...
    BOTTOM: ClassVar[int] = ...
    
    def __init__(self, *, kwargs: _type_DRAW_SW_MASK_LINE_SIDE = dict()):
        ...


class SYMBOL(object):

    BULLET: ClassVar[int] = ...
    AUDIO: ClassVar[int] = ...
    VIDEO: ClassVar[int] = ...
    LIST: ClassVar[int] = ...
    OK: ClassVar[int] = ...
    CLOSE: ClassVar[int] = ...
    POWER: ClassVar[int] = ...
    SETTINGS: ClassVar[int] = ...
    HOME: ClassVar[int] = ...
    DOWNLOAD: ClassVar[int] = ...
    DRIVE: ClassVar[int] = ...
    REFRESH: ClassVar[int] = ...
    MUTE: ClassVar[int] = ...
    VOLUME_MID: ClassVar[int] = ...
    VOLUME_MAX: ClassVar[int] = ...
    IMAGE: ClassVar[int] = ...
    TINT: ClassVar[int] = ...
    PREV: ClassVar[int] = ...
    PLAY: ClassVar[int] = ...
    PAUSE: ClassVar[int] = ...
    STOP: ClassVar[int] = ...
    NEXT: ClassVar[int] = ...
    EJECT: ClassVar[int] = ...
    LEFT: ClassVar[int] = ...
    RIGHT: ClassVar[int] = ...
    PLUS: ClassVar[int] = ...
    MINUS: ClassVar[int] = ...
    EYE_OPEN: ClassVar[int] = ...
    EYE_CLOSE: ClassVar[int] = ...
    WARNING: ClassVar[int] = ...
    SHUFFLE: ClassVar[int] = ...
    UP: ClassVar[int] = ...
    DOWN: ClassVar[int] = ...
    LOOP: ClassVar[int] = ...
    DIRECTORY: ClassVar[int] = ...
    UPLOAD: ClassVar[int] = ...
    CALL: ClassVar[int] = ...
    CUT: ClassVar[int] = ...
    COPY: ClassVar[int] = ...
    SAVE: ClassVar[int] = ...
    BARS: ClassVar[int] = ...
    ENVELOPE: ClassVar[int] = ...
    CHARGE: ClassVar[int] = ...
    PASTE: ClassVar[int] = ...
    BELL: ClassVar[int] = ...
    KEYBOARD: ClassVar[int] = ...
    GPS: ClassVar[int] = ...
    FILE: ClassVar[int] = ...
    WIFI: ClassVar[int] = ...
    BATTERY_FULL: ClassVar[int] = ...
    BATTERY_3: ClassVar[int] = ...
    BATTERY_2: ClassVar[int] = ...
    BATTERY_1: ClassVar[int] = ...
    BATTERY_EMPTY: ClassVar[int] = ...
    USB: ClassVar[int] = ...
    BLUETOOTH: ClassVar[int] = ...
    TRASH: ClassVar[int] = ...
    EDIT: ClassVar[int] = ...
    BACKSPACE: ClassVar[int] = ...
    SD_CARD: ClassVar[int] = ...
    NEW_LINE: ClassVar[int] = ...
    DUMMY: ClassVar[int] = ...
    
    def __init__(self, *, parent: "obj"):
        ...


class _type_color_t(TypedDict, total=False):
    blue: int
    green: int
    red: int


class color_t(Struct):

    __SIZE__: ClassVar[int] = ...
    
    def __init__(self, *, kwargs: _type_color_t = dict()):
        ...

    @property
    def blue(self) -> int:
        """
        :type value: int
        :rtype: int
        """
    
        ...    

    @blue.setter
    def blue(self, value: int):
        ...    

    @property
    def green(self) -> int:
        """
        :type value: int
        :rtype: int
        """
    
        ...    

    @green.setter
    def green(self, value: int):
        ...    

    @property
    def red(self) -> int:
        """
        :type value: int
        :rtype: int
        """
    
        ...    

    @red.setter
    def red(self, value: int):
        ...    


    def to_32(self, opa: opa_t) -> "color32_t":
        """
        Create an ARGB8888 color from RGB888 + alpha the ARGB8888 color 
        
        :param opa: the alpha value 
        :type opa: opa_t

        :returns: the ARGB8888 color 
        :rtype: "color32_t"
        """
        ...

    def to_int(self) -> int:
        """
        Convert an RGB888 color to an integer c as an integer 
        

        :returns: c as an integer 
        :rtype: int
        """
        ...

    def eq(self, c2: "color_t") -> bool:
        """
        Check if two RGB888 color are equal true: equal 
        
        :param c2: the second color 
        :type c2: "color_t"

        :returns: true: equal 
        :rtype: bool
        """
        ...

    def to_u16(self) -> int:
        """
        Convert am RGB888 color to RGB565 stored in uint16_t  color as RGB565 on uin16_t 
        

        :returns: color as RGB565 on uin16_t 
        :rtype: int
        """
        ...

    def to_u32(self) -> int:
        """
        Convert am RGB888 color to XRGB8888 stored in uint32_t  color as XRGB8888 on uin32_t (the alpha channel is always set to 0xFF) 
        

        :returns: color as XRGB8888 on uin32_t (the alpha channel is always set to 0xFF) 
        :rtype: int
        """
        ...

    def lighten(self, lvl: opa_t) -> "color_t":
        """
        Mix white to a color the mixed color 
        
        :param lvl: the intensity of white (0: no change, 255: fully white) 
        :type lvl: opa_t

        :returns: the mixed color 
        :rtype: "color_t"
        """
        ...

    def darken(self, lvl: opa_t) -> "color_t":
        """
        Mix black to a color the mixed color 
        
        :param lvl: the intensity of black (0: no change, 255: fully black) 
        :type lvl: opa_t

        :returns: the mixed color 
        :rtype: "color_t"
        """
        ...

    def to_hsv(self) -> "color_hsv_t":
        """
        Convert a color to HSV the given color in HSV 
        

        :returns: the given color in HSV 
        :rtype: "color_hsv_t"
        """
        ...

    def luminance(self) -> int:
        """
        Get the luminance of a color: luminance = 0.3 R + 0.59 G + 0.11 B the brightness [0..255] 
        

        :returns: the brightness [0..255] 
        :rtype: int
        """
        ...

    def mix(self, c2: "color_t", mix: int) -> "color_t":
        """
        Mix two colors with a given ratio. the mixed color 
        
        :param c2: the second color to mix (usually the background) 
        :type c2: "color_t"
        :param mix: The ratio of the colors. 0: full c2 , 255: full c1 , 127: half c1 and half c2 
        :type mix: int

        :returns: the mixed color 
        :rtype: "color_t"
        """
        ...

    def brightness(self) -> int:
        """
        Get the brightness of a color brightness in range [0..255] 
        

        :returns: brightness in range [0..255] 
        :rtype: int
        """
        ...



class _type_grad_dsc_t(TypedDict, total=False):
    stops: List["gradient_stop_t"]
    stops_count: int
    dir: "grad_dir_t"
    extend: "grad_extend_t"


class grad_dsc_t(Struct):

    __SIZE__: ClassVar[int] = ...
    
    def __init__(self, *, kwargs: _type_grad_dsc_t = dict()):
        ...

    @property
    def stops(self) -> List["gradient_stop_t"]:
        """
        :type value: List["gradient_stop_t"]
        :rtype: List["gradient_stop_t"]
        """
    
        ...    

    @stops.setter
    def stops(self, value: List["gradient_stop_t"]):
        ...    

    @property
    def stops_count(self) -> int:
        """
        :type value: int
        :rtype: int
        """
    
        ...    

    @stops_count.setter
    def stops_count(self, value: int):
        ...    

    @property
    def dir(self) -> "grad_dir_t":
        """
        :type value: "grad_dir_t"
        :rtype: "grad_dir_t"
        """
    
        ...    

    @dir.setter
    def dir(self, value: "grad_dir_t"):
        ...    

    @property
    def extend(self) -> "grad_extend_t":
        """
        :type value: "grad_extend_t"
        :rtype: "grad_extend_t"
        """
    
        ...    

    @extend.setter
    def extend(self, value: "grad_extend_t"):
        ...    


    def gradient_color_calculate(self, range: int, frac: int, color_out: "grad_color_t", opa_out: opa_t) -> None:
        """
        Compute the color in the given gradient and fraction Gradient are specified in a virtual [0-255] range, so this function scales the virtual range to the given range 
        
        :param range: The range to use in computation. 
        :type range: int
        :param frac: The current part used in the range. frac is in [0; range] 
        :type frac: int
        :param color_out: Calculated gradient color 
        :type color_out: "grad_color_t"
        :param opa_out: Calculated opacity 
        :type opa_out: opa_t

        :returns: 
        :rtype: None
        """
        ...

    def gradient_get(self, w: int, h: int) -> "grad_t":
        """
        Get a gradient cache from the given parameters 
        
        :param w: 
        :type w: int
        :param h: 
        :type h: int

        :returns: 
        :rtype: "grad_t"
        """
        ...

    def gradient_init_stops(self, colors: List["color_t"], opa: opa_t, fracs: List[int], num_stops: int) -> None:
        """
        Initialize gradient color map from a table 
        
        :param colors: color array 
        :type colors: List["color_t"]
        :param opa: opacity array: if NULL, then LV_OPA_COVER is assumed 
        :type opa: opa_t
        :param fracs: position array (0..255): if NULL, then colors are distributed evenly 
        :type fracs: List[int]
        :param num_stops: number of gradient stops (1..LV_GRADIENT_MAX_STOPS) 
        :type num_stops: int

        :returns: 
        :rtype: None
        """
        ...



class _type_gradient_stop_t(TypedDict, total=False):
    color: "color_t"
    opa: "opa_t"
    frac: int


class gradient_stop_t(Struct):

    __SIZE__: ClassVar[int] = ...
    
    def __init__(self, *, kwargs: _type_gradient_stop_t = dict()):
        ...

    @property
    def color(self) -> "color_t":
        """
        :type value: "color_t"
        :rtype: "color_t"
        """
    
        ...    

    @color.setter
    def color(self, value: "color_t"):
        ...    

    @property
    def opa(self) -> "opa_t":
        """
        :type value: "opa_t"
        :rtype: "opa_t"
        """
    
        ...    

    @opa.setter
    def opa(self, value: "opa_t"):
        ...    

    @property
    def frac(self) -> int:
        """
        :type value: int
        :rtype: int
        """
    
        ...    

    @frac.setter
    def frac(self, value: int):
        ...    



class _type_font_t(TypedDict, total=False):
    line_height: int
    base_line: int
    subpx: int
    kerning: int
    underline_position: int
    underline_thickness: int
    dsc: Any
    fallback: "font_t"
    user_data: Any


class font_t(Struct):

    __SIZE__: ClassVar[int] = ...
    
    def __init__(self, *, kwargs: _type_font_t = dict()):
        ...

    @property
    def line_height(self) -> int:
        """
        :type value: int
        :rtype: int
        """
    
        ...    

    @line_height.setter
    def line_height(self, value: int):
        ...    

    @property
    def base_line(self) -> int:
        """
        :type value: int
        :rtype: int
        """
    
        ...    

    @base_line.setter
    def base_line(self, value: int):
        ...    

    @property
    def subpx(self) -> int:
        """
        :type value: int
        :rtype: int
        """
    
        ...    

    @subpx.setter
    def subpx(self, value: int):
        ...    

    @property
    def kerning(self) -> int:
        """
        :type value: int
        :rtype: int
        """
    
        ...    

    @kerning.setter
    def kerning(self, value: int):
        ...    

    @property
    def underline_position(self) -> int:
        """
        :type value: int
        :rtype: int
        """
    
        ...    

    @underline_position.setter
    def underline_position(self, value: int):
        ...    

    @property
    def underline_thickness(self) -> int:
        """
        :type value: int
        :rtype: int
        """
    
        ...    

    @underline_thickness.setter
    def underline_thickness(self, value: int):
        ...    

    @property
    def dsc(self) -> Any:
        """
        :type value: Any
        :rtype: Any
        """
    
        ...    

    @dsc.setter
    def dsc(self, value: Any):
        ...    

    @property
    def fallback(self) -> "font_t":
        """
        :type value: "font_t"
        :rtype: "font_t"
        """
    
        ...    

    @fallback.setter
    def fallback(self, value: "font_t"):
        ...    

    @property
    def user_data(self) -> Any:
        """
        :type value: Any
        :rtype: Any
        """
    
        ...    

    @user_data.setter
    def user_data(self, value: Any):
        ...    


    def get_glyph_dsc(self, arg1: "font_glyph_dsc_t", letter: int, letter_next: int) -> bool:
        """
        Get the descriptor of a glyph true: descriptor is successfully loaded into dsc_out . false: the letter was not found, no data is loaded to dsc_out 
        
        :param arg1: store the result descriptor here 
        :type arg1: "font_glyph_dsc_t"
        :param letter: a UNICODE letter code 
        :type letter: int
        :param letter_next: the next letter after letter . Used for kerning 
        :type letter_next: int

        :returns: true: descriptor is successfully loaded into dsc_out . false: the letter was not found, no data is loaded to dsc_out 
        :rtype: bool
        """
        ...

    def get_glyph_width(self, letter: int, letter_next: int) -> int:
        """
        Get the width of a glyph with kerning the width of the glyph 
        
        :param letter: a UNICODE letter 
        :type letter: int
        :param letter_next: the next letter after letter . Used for kerning 
        :type letter_next: int

        :returns: the width of the glyph 
        :rtype: int
        """
        ...

    def get_line_height(self) -> int:
        """
        Get the line height of a font. All characters fit into this height the height of a font 
        

        :returns: the height of a font 
        :rtype: int
        """
        ...

    def set_kerning(self, kerning: font_kerning_t) -> None:
        """
        Configure the use of kerning information stored in a font 
        
        :param kerning: LV_FONT_KERNING_NORMAL (default) or LV_FONT_KERNING_NONE 
        :type kerning: font_kerning_t

        :returns: 
        :rtype: None
        """
        ...

    def get_glyph_dsc_fmt_txt(self, arg1: "font_glyph_dsc_t", letter: int, letter_next: int) -> bool:
        """
        Used as get_glyph_dsc callback in lvgl's native font format if the font is uncompressed. true: descriptor is successfully loaded into dsc_out . false: the letter was not found, no data is loaded to dsc_out 
        
        :param arg1: store the result descriptor here 
        :type arg1: "font_glyph_dsc_t"
        :param letter: a UNICODE letter code 
        :type letter: int
        :param letter_next: the unicode letter succeeding the letter under test 
        :type letter_next: int

        :returns: true: descriptor is successfully loaded into dsc_out . false: the letter was not found, no data is loaded to dsc_out 
        :rtype: bool
        """
        ...



class _type_font_glyph_dsc_t(TypedDict, total=False):
    resolved_font: "font_t"
    adv_w: int
    box_w: int
    box_h: int
    ofs_x: int
    ofs_y: int
    format: "font_glyph_format_t"
    is_placeholder: int
    gid: "font_glyph_dsc_gid_t"
    entry: "cache_entry_t"


class font_glyph_dsc_t(Struct):

    __SIZE__: ClassVar[int] = ...
    
    def __init__(self, *, kwargs: _type_font_glyph_dsc_t = dict()):
        ...

    @property
    def resolved_font(self) -> "font_t":
        """
        :type value: "font_t"
        :rtype: "font_t"
        """
    
        ...    

    @resolved_font.setter
    def resolved_font(self, value: "font_t"):
        ...    

    @property
    def adv_w(self) -> int:
        """
        :type value: int
        :rtype: int
        """
    
        ...    

    @adv_w.setter
    def adv_w(self, value: int):
        ...    

    @property
    def box_w(self) -> int:
        """
        :type value: int
        :rtype: int
        """
    
        ...    

    @box_w.setter
    def box_w(self, value: int):
        ...    

    @property
    def box_h(self) -> int:
        """
        :type value: int
        :rtype: int
        """
    
        ...    

    @box_h.setter
    def box_h(self, value: int):
        ...    

    @property
    def ofs_x(self) -> int:
        """
        :type value: int
        :rtype: int
        """
    
        ...    

    @ofs_x.setter
    def ofs_x(self, value: int):
        ...    

    @property
    def ofs_y(self) -> int:
        """
        :type value: int
        :rtype: int
        """
    
        ...    

    @ofs_y.setter
    def ofs_y(self, value: int):
        ...    

    @property
    def format(self) -> "font_glyph_format_t":
        """
        :type value: "font_glyph_format_t"
        :rtype: "font_glyph_format_t"
        """
    
        ...    

    @format.setter
    def format(self, value: "font_glyph_format_t"):
        ...    

    @property
    def is_placeholder(self) -> int:
        """
        :type value: int
        :rtype: int
        """
    
        ...    

    @is_placeholder.setter
    def is_placeholder(self, value: int):
        ...    

    @property
    def gid(self) -> "font_glyph_dsc_gid_t":
        """
        :type value: "font_glyph_dsc_gid_t"
        :rtype: "font_glyph_dsc_gid_t"
        """
    
        ...    

    @gid.setter
    def gid(self, value: "font_glyph_dsc_gid_t"):
        ...    

    @property
    def entry(self) -> "cache_entry_t":
        """
        :type value: "cache_entry_t"
        :rtype: "cache_entry_t"
        """
    
        ...    

    @entry.setter
    def entry(self, value: "cache_entry_t"):
        ...    


    def get_glyph_bitmap(self, arg1: "draw_buf_t") -> Any:
        """
        Return with the bitmap of a font. You must call :ref:`lv_font_get_glyph_dsc()` to get g_dsc ( :ref:`lv_font_glyph_dsc_t` ) before you can call this function.  pointer to the glyph's data. It can be a draw buffer for bitmap fonts or an image source for imgfonts. 
        
        :param arg1: a draw buffer that can be used to store the bitmap of the glyph, it's OK not to use it. 
        :type arg1: "draw_buf_t"

        :returns: pointer to the glyph's data. It can be a draw buffer for bitmap fonts or an image source for imgfonts. 
        :rtype: Any
        """
        ...

    def release_draw_data(self) -> None:
        """
        Release the bitmap of a font. You must call :ref:`lv_font_get_glyph_dsc()` to get g_dsc ( :ref:`lv_font_glyph_dsc_t` ) before you can call this function. 
        

        :returns: 
        :rtype: None
        """
        ...

    def get_bitmap_fmt_txt(self, arg1: "draw_buf_t") -> Any:
        """
        Used as get_glyph_bitmap callback in lvgl's native font format if the font is uncompressed. pointer to an A8 bitmap (not necessarily bitmap_out) or NULL if unicode_letter not found 
        
        :param arg1: a draw buffer that can be used to store the bitmap of the glyph, it's OK not to use it. 
        :type arg1: "draw_buf_t"

        :returns: pointer to an A8 bitmap (not necessarily bitmap_out) or NULL if unicode_letter not found 
        :rtype: Any
        """
        ...



class _type_font_glyph_dsc_gid_t(TypedDict, total=False):
    index: int
    src: Any


class font_glyph_dsc_gid_t(Struct):

    __SIZE__: ClassVar[int] = ...
    
    def __init__(self, *, kwargs: _type_font_glyph_dsc_gid_t = dict()):
        ...

    @property
    def index(self) -> int:
        ...    

    @index.setter
    def index(self, value: int):
        ...    

    @property
    def src(self) -> Any:
        ...    

    @src.setter
    def src(self, value: Any):
        ...    



class _type_draw_buf_t(TypedDict, total=False):
    header: "image"
    data_size: int
    data: Union[str, List[int]]
    unaligned_data: Any
    handlers: "draw_buf_handlers_t"


class draw_buf_t(Struct):

    __SIZE__: ClassVar[int] = ...
    
    def __init__(self, *, kwargs: _type_draw_buf_t = dict()):
        ...

    @property
    def header(self) -> "image":
        """
        :type value: "image"
        :rtype: "image"
        """
    
        ...    

    @header.setter
    def header(self, value: "image"):
        ...    

    @property
    def data_size(self) -> int:
        """
        :type value: int
        :rtype: int
        """
    
        ...    

    @data_size.setter
    def data_size(self, value: int):
        ...    

    @property
    def data(self) -> Union[str, List[int]]:
        """
        :type value: Union[str, List[int]]
        :rtype: Union[str, List[int]]
        """
    
        ...    

    @data.setter
    def data(self, value: Union[str, List[int]]):
        ...    

    @property
    def unaligned_data(self) -> Any:
        """
        :type value: Any
        :rtype: Any
        """
    
        ...    

    @unaligned_data.setter
    def unaligned_data(self, value: Any):
        ...    

    @property
    def handlers(self) -> "draw_buf_handlers_t":
        """
        :type value: "draw_buf_handlers_t"
        :rtype: "draw_buf_handlers_t"
        """
    
        ...    

    @handlers.setter
    def handlers(self, value: "draw_buf_handlers_t"):
        ...    


    def invalidate_cache(self, area: "area_t") -> None:
        """
        Invalidate the cache of the buffer 
        
        :param area: the area to invalidate in the buffer, use NULL to invalidate the whole draw buffer address range 
        :type area: "area_t"

        :returns: 
        :rtype: None
        """
        ...

    def flush_cache(self, area: "area_t") -> None:
        """
        Flush the cache of the buffer 
        
        :param area: the area to flush in the buffer, use NULL to flush the whole draw buffer address range 
        :type area: "area_t"

        :returns: 
        :rtype: None
        """
        ...

    def clear(self, a: "area_t") -> None:
        """
        Clear an area on the buffer 
        
        :param a: the area to clear, or NULL to clear the whole buffer 
        :type a: "area_t"

        :returns: 
        :rtype: None
        """
        ...

    def copy(self, dest_area: "area_t", src: "draw_buf_t", src_area: "area_t") -> None:
        """
        Copy an area from a buffer to another dest_area and src_area should have the same width and height  dest and src should have same color format. Color converting is not supported fow now. 
        
        :param dest_area: the area to copy from the destination buffer, if NULL, use the whole buffer 
        :type dest_area: "area_t"
        :param src: pointer to the source draw buffer 
        :type src: "draw_buf_t"
        :param src_area: the area to copy from the destination buffer, if NULL, use the whole buffer 
        :type src_area: "area_t"

        :returns: 
        :rtype: None
        """
        ...

    def dup(self) -> "draw_buf_t":
        """
        Duplicate a draw buf with same image size, stride and color format. Copy the image data too. the duplicated draw buf on success, NULL if failed 
        

        :returns: the duplicated draw buf on success, NULL if failed 
        :rtype: "draw_buf_t"
        """
        ...

    def init(self, w: int, h: int, cf: color_format_t, stride: int, data: Any, data_size: int) -> "result_t":
        """
        Initialize a draw buf with the given buffer and parameters. Clear draw buffer flag to zero. return LV_RESULT_OK on success, LV_RESULT_INVALID otherwise 
        
        :param w: the buffer width in pixels 
        :type w: int
        :param h: the buffer height in pixels 
        :type h: int
        :param cf: the color format 
        :type cf: color_format_t
        :param stride: the stride in bytes. Use 0 for automatic calculation 
        :type stride: int
        :param data: the buffer used for drawing. Unaligned data will be aligned internally 
        :type data: Any
        :param data_size: the size of the buffer in bytes 
        :type data_size: int

        :returns: return LV_RESULT_OK on success, LV_RESULT_INVALID otherwise 
        :rtype: "result_t"
        """
        ...

    def reshape(self, cf: color_format_t, w: int, h: int, stride: int) -> "draw_buf_t":
        """
        Keep using the existing memory, reshape the draw buffer to the given width and height. Return NULL if data_size is smaller than the required size. 
        
        :param cf: the new color format, use 0 or LV_COLOR_FORMAT_UNKNOWN to keep using the original color format. 
        :type cf: color_format_t
        :param w: the new width in pixels 
        :type w: int
        :param h: the new height in pixels 
        :type h: int
        :param stride: the stride in bytes for image. Use 0 for automatic calculation. 
        :type stride: int

        :returns: 
        :rtype: "draw_buf_t"
        """
        ...

    def destroy(self) -> None:
        """
        Destroy a draw buf by freeing the actual buffer if it's marked as LV_IMAGE_FLAGS_ALLOCATED in header. Then free the :ref:`lv_draw_buf_t` struct. 
        

        :returns: 
        :rtype: None
        """
        ...

    def goto_xy(self, x: int, y: int) -> Any:
        """
        Return pointer to the buffer at the given coordinates 
        
        :param x: 
        :type x: int
        :param y: 
        :type y: int

        :returns: 
        :rtype: Any
        """
        ...

    def adjust_stride(self, stride: int) -> "result_t":
        """
        Adjust the stride of a draw buf in place. LV_RESULT_OK: success or LV_RESULT_INVALID: failed 
        
        :param stride: the new stride in bytes for image. Use LV_STRIDE_AUTO for automatic calculation. 
        :type stride: int

        :returns: LV_RESULT_OK: success or LV_RESULT_INVALID: failed 
        :rtype: "result_t"
        """
        ...

    def premultiply(self) -> "result_t":
        """
        Premultiply draw buffer color with alpha channel. If it's already premultiplied, return directly. Only color formats with alpha channel will be processed. 
        
        LV_RESULT_OK: premultiply success  
        

        :returns: LV_RESULT_OK: premultiply success 
        :rtype: "result_t"
        """
        ...

    def has_flag(self, flag: "image") -> bool:
        """
        :param flag: 
        :type flag: "image"

        :returns: 
        :rtype: bool
        """
        ...

    def set_flag(self, flag: "image") -> None:
        """
        :param flag: 
        :type flag: "image"

        :returns: 
        :rtype: None
        """
        ...

    def clear_flag(self, flag: "image") -> None:
        """
        :param flag: 
        :type flag: "image"

        :returns: 
        :rtype: None
        """
        ...

    def from_image(self, img: "image") -> None:
        """
        As of now, draw buf share same definition as :ref:`lv_image_dsc_t` . And is interchangeable with :ref:`lv_image_dsc_t` . 
        
        :param img: 
        :type img: "image"

        :returns: 
        :rtype: None
        """
        ...

    def to_image(self, img: "image") -> None:
        """
        :param img: 
        :type img: "image"

        :returns: 
        :rtype: None
        """
        ...

    def set_palette(self, index: int, color: "color32_t") -> None:
        """
        Set the palette color of an indexed image. Valid only for LV_COLOR_FORMAT_I1/2/4/8 
        
        :param index: the palette color to set: for LV_COLOR_FORMAT_I1 : 0..1 for LV_COLOR_FORMAT_I2 : 0..3 for LV_COLOR_FORMAT_I4 : 0..15 for LV_COLOR_FORMAT_I8 : 0..255 
        :type index: int
        :param color: the color to set in :ref:`lv_color32_t` format 
        :type color: "color32_t"

        :returns: 
        :rtype: None
        """
        ...

    def save_to_file(self, path: str) -> "result_t":
        """
        Save a draw buf to a file LV_RESULT_OK: success; LV_RESULT_INVALID: error 
        
        :param path: path to the file to save 
        :type path: str

        :returns: LV_RESULT_OK: success; LV_RESULT_INVALID: error 
        :rtype: "result_t"
        """
        ...



class _type_draw_buf_handlers_t(TypedDict, total=False):
    pass


class draw_buf_handlers_t(Struct):
    
    def __init__(self, *, kwargs: _type_draw_buf_handlers_t = dict()):
        ...

    def init_with_default_handlers(self) -> None:
        """
        Initialize the draw buffer with the default handlers. 
        

        :returns: 
        :rtype: None
        """
        ...

    def init(self, buf_malloc_cb: "draw_buf_malloc_cb", buf_free_cb: "draw_buf_free_cb", align_pointer_cb: "draw_buf_align_cb", invalidate_cache_cb: "draw_buf_cache_operation_cb", flush_cache_cb: "draw_buf_cache_operation_cb", width_to_stride_cb: "draw_buf_width_to_stride_cb") -> None:
        """
        Initialize the draw buffer with given handlers. 
        
        :param buf_malloc_cb: the callback to allocate memory for the buffer 
        :type buf_malloc_cb: "draw_buf_malloc_cb"
        :param buf_free_cb: the callback to free memory of the buffer 
        :type buf_free_cb: "draw_buf_free_cb"
        :param align_pointer_cb: the callback to align the buffer 
        :type align_pointer_cb: "draw_buf_align_cb"
        :param invalidate_cache_cb: the callback to invalidate the cache of the buffer 
        :type invalidate_cache_cb: "draw_buf_cache_operation_cb"
        :param flush_cache_cb: the callback to flush buffer 
        :type flush_cache_cb: "draw_buf_cache_operation_cb"
        :param width_to_stride_cb: the callback to calculate the stride based on the width and color format 
        :type width_to_stride_cb: "draw_buf_width_to_stride_cb"

        :returns: 
        :rtype: None
        """
        ...

    def align_ex(self, buf: Any, color_format: color_format_t) -> Any:
        """
        Align the address of a buffer with custom draw buffer handlers. The buffer needs to be large enough for the real data after alignment the aligned buffer 
        
        :param buf: the data to align 
        :type buf: Any
        :param color_format: the color format of the buffer 
        :type color_format: color_format_t

        :returns: the aligned buffer 
        :rtype: Any
        """
        ...

    def width_to_stride_ex(self, w: int, color_format: color_format_t) -> int:
        """
        Calculate the stride in bytes based on a width and color format the stride in bytes 
        
        :param w: the width in pixels 
        :type w: int
        :param color_format: the color format 
        :type color_format: color_format_t

        :returns: the stride in bytes 
        :rtype: int
        """
        ...

    def create_ex(self, w: int, h: int, cf: color_format_t, stride: int) -> "draw_buf_t":
        """
        Note: Eventually, lv_draw_buf_malloc/free will be kept as private. For now, we use create to distinguish with malloc. 
        
        Create an draw buf by allocating struct for :ref:`lv_draw_buf_t` and allocating a buffer for it that meets specified requirements.  
        
        :param w: the buffer width in pixels 
        :type w: int
        :param h: the buffer height in pixels 
        :type h: int
        :param cf: the color format for image 
        :type cf: color_format_t
        :param stride: the stride in bytes for image. Use 0 for automatic calculation based on w, cf, and global stride alignment configuration. 
        :type stride: int

        :returns: 
        :rtype: "draw_buf_t"
        """
        ...

    def dup_ex(self, draw_buf: "draw_buf_t") -> "draw_buf_t":
        """
        Duplicate a draw buf with same image size, stride and color format. Copy the image data too. the duplicated draw buf on success, NULL if failed 
        
        :param draw_buf: the draw buf to duplicate 
        :type draw_buf: "draw_buf_t"

        :returns: the duplicated draw buf on success, NULL if failed 
        :rtype: "draw_buf_t"
        """
        ...



class _type_color_filter_dsc_t(TypedDict, total=False):
    user_data: Any


class color_filter_dsc_t(Struct):

    __SIZE__: ClassVar[int] = ...
    
    def __init__(self, *, kwargs: _type_color_filter_dsc_t = dict()):
        ...

    @property
    def user_data(self) -> Any:
        """
        :type value: Any
        :rtype: Any
        """
    
        ...    

    @user_data.setter
    def user_data(self, value: Any):
        ...    


    def init(self, cb: Callable[["color_filter_dsc_t", "color_t", "opa_t"], "color_t"]) -> None:
        """
        :param cb: 
        :type cb: Callable[["color_filter_dsc_t", "color_t", "opa_t"], "color_t"]

        :returns: 
        :rtype: None
        """
        ...



class _type_anim_t(TypedDict, total=False):
    var: Any
    user_data: Any
    start_value: int
    current_value: int
    end_value: int
    duration: int
    act_time: int
    playback_delay: int
    playback_duration: int
    repeat_delay: int
    repeat_cnt: int
    parameter: "anim_parameter_t"
    last_timer_run: int
    playback_now: int
    run_round: int
    start_cb_called: int
    early_apply: int


class anim_t(Struct):

    __SIZE__: ClassVar[int] = ...
    
    def __init__(self, *, kwargs: _type_anim_t = dict()):
        ...

    @property
    def var(self) -> Any:
        """
        :type value: Any
        :rtype: Any
        """
    
        ...    

    @var.setter
    def var(self, value: Any):
        ...    

    @property
    def user_data(self) -> Any:
        """
        :type value: Any
        :rtype: Any
        """
    
        ...    

    @user_data.setter
    def user_data(self, value: Any):
        ...    

    @property
    def start_value(self) -> int:
        """
        :type value: int
        :rtype: int
        """
    
        ...    

    @start_value.setter
    def start_value(self, value: int):
        ...    

    @property
    def current_value(self) -> int:
        """
        :type value: int
        :rtype: int
        """
    
        ...    

    @current_value.setter
    def current_value(self, value: int):
        ...    

    @property
    def end_value(self) -> int:
        """
        :type value: int
        :rtype: int
        """
    
        ...    

    @end_value.setter
    def end_value(self, value: int):
        ...    

    @property
    def duration(self) -> int:
        """
        :type value: int
        :rtype: int
        """
    
        ...    

    @duration.setter
    def duration(self, value: int):
        ...    

    @property
    def act_time(self) -> int:
        """
        :type value: int
        :rtype: int
        """
    
        ...    

    @act_time.setter
    def act_time(self, value: int):
        ...    

    @property
    def playback_delay(self) -> int:
        """
        :type value: int
        :rtype: int
        """
    
        ...    

    @playback_delay.setter
    def playback_delay(self, value: int):
        ...    

    @property
    def playback_duration(self) -> int:
        """
        :type value: int
        :rtype: int
        """
    
        ...    

    @playback_duration.setter
    def playback_duration(self, value: int):
        ...    

    @property
    def repeat_delay(self) -> int:
        """
        :type value: int
        :rtype: int
        """
    
        ...    

    @repeat_delay.setter
    def repeat_delay(self, value: int):
        ...    

    @property
    def repeat_cnt(self) -> int:
        """
        :type value: int
        :rtype: int
        """
    
        ...    

    @repeat_cnt.setter
    def repeat_cnt(self, value: int):
        ...    

    @property
    def parameter(self) -> "anim_parameter_t":
        """
        :type value: "anim_parameter_t"
        :rtype: "anim_parameter_t"
        """
    
        ...    

    @parameter.setter
    def parameter(self, value: "anim_parameter_t"):
        ...    

    @property
    def last_timer_run(self) -> int:
        """
        :type value: int
        :rtype: int
        """
    
        ...    

    @last_timer_run.setter
    def last_timer_run(self, value: int):
        ...    

    @property
    def playback_now(self) -> int:
        """
        :type value: int
        :rtype: int
        """
    
        ...    

    @playback_now.setter
    def playback_now(self, value: int):
        ...    

    @property
    def run_round(self) -> int:
        """
        :type value: int
        :rtype: int
        """
    
        ...    

    @run_round.setter
    def run_round(self, value: int):
        ...    

    @property
    def start_cb_called(self) -> int:
        """
        :type value: int
        :rtype: int
        """
    
        ...    

    @start_cb_called.setter
    def start_cb_called(self, value: int):
        ...    

    @property
    def early_apply(self) -> int:
        """
        :type value: int
        :rtype: int
        """
    
        ...    

    @early_apply.setter
    def early_apply(self, value: int):
        ...    


    def init(self) -> None:
        """
        Initialize an animation variable. E.g.: :ref:`lv_anim_t` a; lv_anim_init(&a); lv_anim_set_...(&a); lv_anim_start(&a); 
        

        :returns: 
        :rtype: None
        """
        ...

    def set_var(self, var: Any) -> None:
        """
        Set a variable to animate 
        
        :param var: pointer to a variable to animate 
        :type var: Any

        :returns: 
        :rtype: None
        """
        ...

    def set_exec_cb(self, exec_cb: "anim_exec_xcb_t") -> None:
        """
        Set a function to animate var 
        
        :param exec_cb: a function to execute during animation LVGL's built-in functions can be used. E.g. lv_obj_set_x 
        :type exec_cb: "anim_exec_xcb_t"

        :returns: 
        :rtype: None
        """
        ...

    def set_duration(self, duration: int) -> None:
        """
        Set the duration of an animation 
        
        :param duration: duration of the animation in milliseconds 
        :type duration: int

        :returns: 
        :rtype: None
        """
        ...

    def set_time(self, duration: int) -> None:
        """
        Legacy lv_anim_set_time API will be removed soon, use lv_anim_set_duration instead. 
        
        :param duration: 
        :type duration: int

        :returns: 
        :rtype: None
        """
        ...

    def set_delay(self, duration: int) -> None:
        """
        Set a delay before starting the animation 
        
        :param duration: delay before the animation in milliseconds 
        :type duration: int

        :returns: 
        :rtype: None
        """
        ...

    def set_values(self, start: int, end: int) -> None:
        """
        Set the start and end values of an animation 
        
        :param start: the start value 
        :type start: int
        :param end: the end value 
        :type end: int

        :returns: 
        :rtype: None
        """
        ...

    def set_custom_exec_cb(self, exec_cb: Callable[["anim_t", int], None]) -> None:
        """
        Similar to lv_anim_set_exec_cb but lv_anim_custom_exec_cb_t receives :ref:`lv_anim_t` * as its first parameter instead of void * . This function might be used when LVGL is bound to other languages because it's more consistent to have :ref:`lv_anim_t` * as first parameter. 
        
        :param exec_cb: a function to execute. 
        :type exec_cb: Callable[["anim_t", int], None]

        :returns: 
        :rtype: None
        """
        ...

    def set_path_cb(self, path_cb: Callable[["anim_t"], int]) -> None:
        """
        Set the path (curve) of the animation. 
        
        :param path_cb: a function to set the current value of the animation. 
        :type path_cb: Callable[["anim_t"], int]

        :returns: 
        :rtype: None
        """
        ...

    def set_start_cb(self, start_cb: Callable[["anim_t"], None]) -> None:
        """
        Set a function call when the animation really starts (considering delay ) 
        
        :param start_cb: a function call when the animation starts 
        :type start_cb: Callable[["anim_t"], None]

        :returns: 
        :rtype: None
        """
        ...

    def set_get_value_cb(self, get_value_cb: Callable[["anim_t"], int]) -> None:
        """
        Set a function to use the current value of the variable and make start and end value relative to the returned current value. 
        
        :param get_value_cb: a function call when the animation starts 
        :type get_value_cb: Callable[["anim_t"], int]

        :returns: 
        :rtype: None
        """
        ...

    def set_completed_cb(self, completed_cb: Callable[["anim_t"], None]) -> None:
        """
        Set a function call when the animation is completed 
        
        :param completed_cb: a function call when the animation is fully completed 
        :type completed_cb: Callable[["anim_t"], None]

        :returns: 
        :rtype: None
        """
        ...

    def set_deleted_cb(self, deleted_cb: Callable[["anim_t"], None]) -> None:
        """
        Set a function call when the animation is deleted. 
        
        :param deleted_cb: a function call when the animation is deleted 
        :type deleted_cb: Callable[["anim_t"], None]

        :returns: 
        :rtype: None
        """
        ...

    def set_playback_duration(self, duration: int) -> None:
        """
        Make the animation to play back to when the forward direction is ready 
        
        :param duration: duration of playback animation in milliseconds. 0: disable playback 
        :type duration: int

        :returns: 
        :rtype: None
        """
        ...

    def set_playback_time(self, duration: int) -> None:
        """
        Legacy lv_anim_set_playback_time API will be removed soon, use lv_anim_set_playback_duration instead. 
        
        :param duration: 
        :type duration: int

        :returns: 
        :rtype: None
        """
        ...

    def set_playback_delay(self, duration: int) -> None:
        """
        Make the animation to play back to when the forward direction is ready 
        
        :param duration: delay in milliseconds before starting the playback animation. 
        :type duration: int

        :returns: 
        :rtype: None
        """
        ...

    def set_repeat_count(self, duration: int) -> None:
        """
        Make the animation repeat itself. 
        
        :param duration: repeat count or LV_ANIM_REPEAT_INFINITE for infinite repetition. 0: to disable repetition. 
        :type duration: int

        :returns: 
        :rtype: None
        """
        ...

    def set_repeat_delay(self, duration: int) -> None:
        """
        Set a delay before repeating the animation. 
        
        :param duration: delay in milliseconds before repeating the animation. 
        :type duration: int

        :returns: 
        :rtype: None
        """
        ...

    def set_early_apply(self, en: bool) -> None:
        """
        Set a whether the animation's should be applied immediately or only when the delay expired. 
        
        :param en: true: apply the start value immediately in lv_anim_start ; false: apply the start value only when delay ms is elapsed and the animations really starts 
        :type en: bool

        :returns: 
        :rtype: None
        """
        ...

    def set_user_data(self, var: Any) -> None:
        """
        Set the custom user data field of the animation. 
        
        :param var: pointer to the new user_data. 
        :type var: Any

        :returns: 
        :rtype: None
        """
        ...

    def set_bezier3_param(self, x1: int, y1: int, x2: int, y2: int) -> None:
        """
        Set parameter for cubic bezier path 
        
        :param x1: first control point X 
        :type x1: int
        :param y1: first control point Y 
        :type y1: int
        :param x2: second control point X 
        :type x2: int
        :param y2: second control point Y 
        :type y2: int

        :returns: 
        :rtype: None
        """
        ...

    def start(self) -> "anim_t":
        """
        Create an animation pointer to the created animation (different from the a parameter) 
        

        :returns: pointer to the created animation (different from the a parameter) 
        :rtype: "anim_t"
        """
        ...

    def get_delay(self) -> int:
        """
        Get a delay before starting the animation delay before the animation in milliseconds 
        

        :returns: delay before the animation in milliseconds 
        :rtype: int
        """
        ...

    def get_playtime(self) -> int:
        """
        Get the time used to play the animation. the play time in milliseconds. 
        

        :returns: the play time in milliseconds. 
        :rtype: int
        """
        ...

    def get_time(self) -> int:
        """
        Get the duration of an animation the duration of the animation in milliseconds 
        

        :returns: the duration of the animation in milliseconds 
        :rtype: int
        """
        ...

    def get_repeat_count(self) -> int:
        """
        Get the repeat count of the animation. the repeat count or LV_ANIM_REPEAT_INFINITE for infinite repetition. 0: disabled repetition. 
        

        :returns: the repeat count or LV_ANIM_REPEAT_INFINITE for infinite repetition. 0: disabled repetition. 
        :rtype: int
        """
        ...

    def get_user_data(self) -> Any:
        """
        Get the user_data field of the animation the pointer to the custom user_data of the animation 
        

        :returns: the pointer to the custom user_data of the animation 
        :rtype: Any
        """
        ...

    def custom_delete(self, exec_cb: Callable[["anim_t", int], None]) -> bool:
        """
        Delete an animation by getting the animated variable from a . Only animations with exec_cb will be deleted. This function exists because it's logical that all anim. functions receives an :ref:`lv_anim_t` as their first parameter. It's not practical in C but might make the API more consequent and makes easier to generate bindings. true: at least 1 animation is deleted, false: no animation is deleted 
        
        :param exec_cb: a function pointer which is animating 'var', or NULL to ignore it and delete all the animations of 'var 
        :type exec_cb: Callable[["anim_t", int], None]

        :returns: true: at least 1 animation is deleted, false: no animation is deleted 
        :rtype: bool
        """
        ...

    def custom_get(self, exec_cb: Callable[["anim_t", int], None]) -> "anim_t":
        """
        Get the animation of a variable and its exec_cb . This function exists because it's logical that all anim. functions receives an :ref:`lv_anim_t` as their first parameter. It's not practical in C but might make the API more consequent and makes easier to generate bindings. pointer to the animation. 
        
        :param exec_cb: a function pointer which is animating 'var', or NULL to return first matching 'var' 
        :type exec_cb: Callable[["anim_t", int], None]

        :returns: pointer to the animation. 
        :rtype: "anim_t"
        """
        ...

    def path_linear(self) -> int:
        """
        Calculate the current value of an animation applying linear characteristic the current value to set 
        

        :returns: the current value to set 
        :rtype: int
        """
        ...

    def path_ease_in(self) -> int:
        """
        Calculate the current value of an animation slowing down the start phase the current value to set 
        

        :returns: the current value to set 
        :rtype: int
        """
        ...

    def path_ease_out(self) -> int:
        """
        Calculate the current value of an animation slowing down the end phase the current value to set 
        

        :returns: the current value to set 
        :rtype: int
        """
        ...

    def path_ease_in_out(self) -> int:
        """
        Calculate the current value of an animation applying an "S" characteristic (cosine) the current value to set 
        

        :returns: the current value to set 
        :rtype: int
        """
        ...

    def path_overshoot(self) -> int:
        """
        Calculate the current value of an animation with overshoot at the end the current value to set 
        

        :returns: the current value to set 
        :rtype: int
        """
        ...

    def path_bounce(self) -> int:
        """
        Calculate the current value of an animation with 3 bounces the current value to set 
        

        :returns: the current value to set 
        :rtype: int
        """
        ...

    def path_step(self) -> int:
        """
        Calculate the current value of an animation applying step characteristic. (Set end value on the end of the animation) the current value to set 
        

        :returns: the current value to set 
        :rtype: int
        """
        ...

    def path_custom_bezier3(self) -> int:
        """
        A custom cubic bezier animation path, need to specify cubic-parameters in a->parameter.bezier3 the current value to set 
        

        :returns: the current value to set 
        :rtype: int
        """
        ...



class _type_anim_parameter_t(TypedDict, total=False):
    bezier3: "anim_bezier3_para_t"


class anim_parameter_t(Struct):

    __SIZE__: ClassVar[int] = ...
    
    def __init__(self, *, kwargs: _type_anim_parameter_t = dict()):
        ...

    @property
    def bezier3(self) -> "anim_bezier3_para_t":
        ...    

    @bezier3.setter
    def bezier3(self, value: "anim_bezier3_para_t"):
        ...    



class _type_anim_bezier3_para_t(TypedDict, total=False):
    x1: int
    y1: int
    x2: int
    y2: int


class anim_bezier3_para_t(Struct):

    __SIZE__: ClassVar[int] = ...
    
    def __init__(self, *, kwargs: _type_anim_bezier3_para_t = dict()):
        ...

    @property
    def x1(self) -> int:
        """
        :type value: int
        :rtype: int
        """
    
        ...    

    @x1.setter
    def x1(self, value: int):
        ...    

    @property
    def y1(self) -> int:
        """
        :type value: int
        :rtype: int
        """
    
        ...    

    @y1.setter
    def y1(self, value: int):
        ...    

    @property
    def x2(self) -> int:
        """
        :type value: int
        :rtype: int
        """
    
        ...    

    @x2.setter
    def x2(self, value: int):
        ...    

    @property
    def y2(self) -> int:
        """
        :type value: int
        :rtype: int
        """
    
        ...    

    @y2.setter
    def y2(self, value: int):
        ...    



class _type_style_transition_dsc_t(TypedDict, total=False):
    props: "style_prop_t"
    user_data: Any
    time: int
    delay: int


class style_transition_dsc_t(Struct):

    __SIZE__: ClassVar[int] = ...
    
    def __init__(self, *, kwargs: _type_style_transition_dsc_t = dict()):
        ...

    @property
    def props(self) -> "style_prop_t":
        """
        :type value: "style_prop_t"
        :rtype: "style_prop_t"
        """
    
        ...    

    @props.setter
    def props(self, value: "style_prop_t"):
        ...    

    @property
    def user_data(self) -> Any:
        """
        :type value: Any
        :rtype: Any
        """
    
        ...    

    @user_data.setter
    def user_data(self, value: Any):
        ...    

    @property
    def time(self) -> int:
        """
        :type value: int
        :rtype: int
        """
    
        ...    

    @time.setter
    def time(self, value: int):
        ...    

    @property
    def delay(self) -> int:
        """
        :type value: int
        :rtype: int
        """
    
        ...    

    @delay.setter
    def delay(self, value: int):
        ...    


    def init(self, props: List["style_prop_t"], path_cb: Callable[["anim_t"], int], time: int, delay: int, tr: "style_transition_dsc_t") -> None:
        """
        Initialize a transition descriptor. const static lv_style_prop_t trans_props[] = { LV_STYLE_BG_OPA, LV_STYLE_BG_COLOR, 0 }; static lv_style_transition_dsc_t trans1;  lv_style_transition_dsc_init(&trans1, trans_props, NULL, 300, 0, NULL); 
        
        :param props: an array with the properties to transition. The last element must be zero. 
        :type props: List["style_prop_t"]
        :param path_cb: an animation path (ease) callback. If NULL liner path will be used. 
        :type path_cb: Callable[["anim_t"], int]
        :param time: duration of the transition in [ms] 
        :type time: int
        :param delay: delay before the transition in [ms] 
        :type delay: int
        :param tr: any custom data that will be saved in the transition animation and will be available when path_cb is called 
        :type tr: "style_transition_dsc_t"

        :returns: 
        :rtype: None
        """
        ...



class _type_display_t(TypedDict, total=False):
    pass


class display_t(Struct):
    
    def __init__(self, *, kwargs: _type_display_t = dict()):
        ...

    def draw_dispatch_layer(self, layer: "layer_t") -> bool:
        """
        Used internally to try dispatching draw tasks of a specific layer at least one draw task is being rendered (maybe it was taken earlier) 
        
        :param layer: pointer to a layer 
        :type layer: "layer_t"

        :returns: at least one draw task is being rendered (maybe it was taken earlier) 
        :rtype: bool
        """
        ...

    def delete(self) -> None:
        """
        Remove a display 
        

        :returns: 
        :rtype: None
        """
        ...

    def set_default(self) -> None:
        """
        Set a default display. The new screens will be created on it by default. 
        

        :returns: 
        :rtype: None
        """
        ...

    def get_next(self) -> "display_t":
        """
        Get the next display. the next display or NULL if no more. Gives the first display when the parameter is NULL. 
        

        :returns: the next display or NULL if no more. Gives the first display when the parameter is NULL. 
        :rtype: "display_t"
        """
        ...

    def set_resolution(self, hor_res: int, ver_res: int) -> None:
        """
        Sets the resolution of a display. LV_EVENT_RESOLUTION_CHANGED event will be sent. Here the native resolution of the device should be set. If the display will be rotated later with lv_display_set_rotation LVGL will swap the hor. and ver. resolution automatically. 
        
        :param hor_res: the new horizontal resolution 
        :type hor_res: int
        :param ver_res: the new vertical resolution 
        :type ver_res: int

        :returns: 
        :rtype: None
        """
        ...

    def set_physical_resolution(self, hor_res: int, ver_res: int) -> None:
        """
        It's not mandatory to use the whole display for LVGL, however in some cases physical resolution is important. For example the touchpad still sees whole resolution and the values needs to be converted to the active LVGL display area. 
        
        :param hor_res: the new physical horizontal resolution, or -1 to assume it's the same as the normal hor. res. 
        :type hor_res: int
        :param ver_res: the new physical vertical resolution, or -1 to assume it's the same as the normal hor. res. 
        :type ver_res: int

        :returns: 
        :rtype: None
        """
        ...

    def set_offset(self, hor_res: int, ver_res: int) -> None:
        """
        If physical resolution is not the same as the normal resolution the offset of the active display area can be set here. 
        
        :param hor_res: X offset 
        :type hor_res: int
        :param ver_res: Y offset 
        :type ver_res: int

        :returns: 
        :rtype: None
        """
        ...

    def set_rotation(self, rotation: display_rotation_t) -> None:
        """
        Set the rotation of this display. LVGL will swap the horizontal and vertical resolutions internally. 
        
        :param rotation: LV_DISPLAY_ROTATION_0/90/180/270 
        :type rotation: display_rotation_t

        :returns: 
        :rtype: None
        """
        ...

    def set_dpi(self, dpi: int) -> None:
        """
        Set the DPI (dot per inch) of the display. dpi = sqrt(hor_res^2 + ver_res^2) / diagonal" 
        
        :param dpi: the new DPI 
        :type dpi: int

        :returns: 
        :rtype: None
        """
        ...

    def get_horizontal_resolution(self) -> int:
        """
        Get the horizontal resolution of a display. the horizontal resolution of the display. 
        

        :returns: the horizontal resolution of the display. 
        :rtype: int
        """
        ...

    def get_vertical_resolution(self) -> int:
        """
        Get the vertical resolution of a display the vertical resolution of the display 
        

        :returns: the vertical resolution of the display 
        :rtype: int
        """
        ...

    def get_physical_horizontal_resolution(self) -> int:
        """
        Get the physical horizontal resolution of a display the physical horizontal resolution of the display 
        

        :returns: the physical horizontal resolution of the display 
        :rtype: int
        """
        ...

    def get_physical_vertical_resolution(self) -> int:
        """
        Get the physical vertical resolution of a display the physical vertical resolution of the display 
        

        :returns: the physical vertical resolution of the display 
        :rtype: int
        """
        ...

    def get_offset_x(self) -> int:
        """
        Get the horizontal offset from the full / physical display the horizontal offset from the physical display 
        

        :returns: the horizontal offset from the physical display 
        :rtype: int
        """
        ...

    def get_offset_y(self) -> int:
        """
        Get the vertical offset from the full / physical display the horizontal offset from the physical display 
        

        :returns: the horizontal offset from the physical display 
        :rtype: int
        """
        ...

    def get_rotation(self) -> "display_rotation_t":
        """
        Get the current rotation of this display. the current rotation 
        

        :returns: the current rotation 
        :rtype: "display_rotation_t"
        """
        ...

    def get_dpi(self) -> int:
        """
        Get the DPI of the display dpi of the display 
        

        :returns: dpi of the display 
        :rtype: int
        """
        ...

    def set_buffers(self, buf1: Any, buf2: Any, buf_size: int, render_mode: display_render_mode_t) -> None:
        """
        Set the buffers for a display, similarly to lv_display_set_draw_buffers , but accept the raw buffer pointers. For DIRECT/FULL rending modes, the buffer size must be at least hor_res * ver_res * lv_color_format_get_size(lv_display_get_color_format(disp)) 
        
        :param buf1: first buffer 
        :type buf1: Any
        :param buf2: second buffer (can be NULL ) 
        :type buf2: Any
        :param buf_size: buffer size in byte 
        :type buf_size: int
        :param render_mode: LV_DISPLAY_RENDER_MODE_PARTIAL/DIRECT/FULL 
        :type render_mode: display_render_mode_t

        :returns: 
        :rtype: None
        """
        ...

    def set_draw_buffers(self, buf1: "draw_buf_t", buf2: "draw_buf_t") -> None:
        """
        Set the buffers for a display, accept a draw buffer pointer. Normally use lv_display_set_buffers is enough for most cases. Use this function when an existing :ref:`lv_draw_buf_t` is available. 
        
        :param buf1: first buffer 
        :type buf1: "draw_buf_t"
        :param buf2: second buffer (can be NULL ) 
        :type buf2: "draw_buf_t"

        :returns: 
        :rtype: None
        """
        ...

    def set_render_mode(self, render_mode: display_render_mode_t) -> None:
        """
        Set display render mode 
        
        :param render_mode: LV_DISPLAY_RENDER_MODE_PARTIAL/DIRECT/FULL 
        :type render_mode: display_render_mode_t

        :returns: 
        :rtype: None
        """
        ...

    def set_flush_cb(self, flush_cb: Callable[["display_t", "area_t", Union[str, List[int]]], None]) -> None:
        """
        Set the flush callback which will be called to copy the rendered image to the display. 
        
        :param flush_cb: the flush callback ( px_map contains the rendered image as raw pixel map and it should be copied to area on the display) 
        :type flush_cb: Callable[["display_t", "area_t", Union[str, List[int]]], None]

        :returns: 
        :rtype: None
        """
        ...

    def set_flush_wait_cb(self, wait_cb: Callable[["display_t"], None]) -> None:
        """
        Set a callback to be used while LVGL is waiting flushing to be finished. It can do any complex logic to wait, including semaphores, mutexes, polling flags, etc. If not set the disp->flushing flag is used which can be cleared with lv_display_flush_ready() 
        
        :param wait_cb: a callback to call while LVGL is waiting for flush ready. If NULL lv_display_flush_ready() can be used to signal that flushing is ready. 
        :type wait_cb: Callable[["display_t"], None]

        :returns: 
        :rtype: None
        """
        ...

    def set_color_format(self, color_format: color_format_t) -> None:
        """
        Set the color format of the display. To change the endianness of the rendered image in case of RGB565 format (i.e. swap the 2 bytes) call lv_draw_sw_rgb565_swap in the flush_cb 
        
        :param color_format: Possible values are LV_COLOR_FORMAT_RGB565 LV_COLOR_FORMAT_RGB888 LV_COLOR_FORMAT_XRGB888 LV_COLOR_FORMAT_ARGB888 
        :type color_format: color_format_t

        :returns: 
        :rtype: None
        """
        ...

    def get_color_format(self) -> "color_format_t":
        """
        Get the color format of the display the color format 
        

        :returns: the color format 
        :rtype: "color_format_t"
        """
        ...

    def set_antialiasing(self, en: bool) -> None:
        """
        Enable anti-aliasing for the render engine 
        
        :param en: true/false 
        :type en: bool

        :returns: 
        :rtype: None
        """
        ...

    def get_antialiasing(self) -> bool:
        """
        Get if anti-aliasing is enabled for a display or not true/false 
        

        :returns: true/false 
        :rtype: bool
        """
        ...

    def flush_ready(self) -> None:
        """

        :returns: 
        :rtype: None
        """
        ...

    def flush_is_last(self) -> bool:
        """

        :returns: 
        :rtype: bool
        """
        ...

    def is_double_buffered(self) -> bool:
        """

        :returns: 
        :rtype: bool
        """
        ...

    def get_screen_active(self) -> "obj":
        """
        Return a pointer to the active screen on a display pointer to the active screen object (loaded by ' :ref:`lv_screen_load()` ') 
        

        :returns: pointer to the active screen object (loaded by ' :ref:`lv_screen_load()` ') 
        :rtype: "obj"
        """
        ...

    def get_screen_prev(self) -> "obj":
        """
        Return with a pointer to the previous screen. Only used during screen transitions. pointer to the previous screen object or NULL if not used now 
        

        :returns: pointer to the previous screen object or NULL if not used now 
        :rtype: "obj"
        """
        ...

    def get_layer_top(self) -> "obj":
        """
        Return the top layer. The top layer is the same on all screens and it is above the normal screen layer. pointer to the top layer object 
        

        :returns: pointer to the top layer object 
        :rtype: "obj"
        """
        ...

    def get_layer_sys(self) -> "obj":
        """
        Return the sys. layer. The system layer is the same on all screen and it is above the normal screen and the top layer. pointer to the sys layer object 
        

        :returns: pointer to the sys layer object 
        :rtype: "obj"
        """
        ...

    def get_layer_bottom(self) -> "obj":
        """
        Return the bottom layer. The bottom layer is the same on all screen and it is under the normal screen layer. It's visible only if the screen is transparent. pointer to the bottom layer object 
        

        :returns: pointer to the bottom layer object 
        :rtype: "obj"
        """
        ...

    def add_event_cb(self, event_cb: Callable[["event_t"], None], filter: "event_code_t", disp: "display_t") -> None:
        """
        Add an event handler to the display 
        
        :param event_cb: an event callback 
        :type event_cb: Callable[["event_t"], None]
        :param filter: event code to react or LV_EVENT_ALL 
        :type filter: "event_code_t"
        :param disp: optional user_data 
        :type disp: "display_t"

        :returns: 
        :rtype: None
        """
        ...

    def get_event_count(self) -> int:
        """
        Get the number of event attached to a display number of events 
        

        :returns: number of events 
        :rtype: int
        """
        ...

    def get_event_dsc(self, index: int) -> "event_dsc_t":
        """
        Get an event descriptor for an event the event descriptor 
        
        :param index: the index of the event 
        :type index: int

        :returns: the event descriptor 
        :rtype: "event_dsc_t"
        """
        ...

    def delete_event(self, index: int) -> bool:
        """
        Remove an event true: and event was removed; false: no event was removed 
        
        :param index: the index of the event to remove 
        :type index: int

        :returns: true: and event was removed; false: no event was removed 
        :rtype: bool
        """
        ...

    def remove_event_cb_with_user_data(self, event_cb: Callable[["event_t"], None], disp: "display_t") -> int:
        """
        Remove an event_cb with user_data the count of the event removed 
        
        :param event_cb: the event_cb of the event to remove 
        :type event_cb: Callable[["event_t"], None]
        :param disp: user_data 
        :type disp: "display_t"

        :returns: the count of the event removed 
        :rtype: int
        """
        ...

    def send_event(self, code: "event_code_t", param: Any) -> "result_t":
        """
        Send an event to a display LV_RESULT_OK: disp wasn't deleted in the event. 
        
        :param code: an event code. LV_EVENT_... 
        :type code: "event_code_t"
        :param param: optional param 
        :type param: Any

        :returns: LV_RESULT_OK: disp wasn't deleted in the event. 
        :rtype: "result_t"
        """
        ...

    def set_theme(self, th: "theme_t") -> None:
        """
        Set the theme of a display. If there are no user created widgets yet the screens' theme will be updated 
        
        :param th: pointer to a theme 
        :type th: "theme_t"

        :returns: 
        :rtype: None
        """
        ...

    def get_theme(self) -> "theme_t":
        """
        Get the theme of a display the display's theme (can be NULL) 
        

        :returns: the display's theme (can be NULL) 
        :rtype: "theme_t"
        """
        ...

    def get_inactive_time(self) -> int:
        """
        Get elapsed time since last user activity on a display (e.g. click) elapsed ticks (milliseconds) since the last activity 
        

        :returns: elapsed ticks (milliseconds) since the last activity 
        :rtype: int
        """
        ...

    def trigger_activity(self) -> None:
        """
        Manually trigger an activity on a display 
        

        :returns: 
        :rtype: None
        """
        ...

    def enable_invalidation(self, en: bool) -> None:
        """
        Temporarily enable and disable the invalidation of the display. 
        
        :param en: true: enable invalidation; false: invalidation 
        :type en: bool

        :returns: 
        :rtype: None
        """
        ...

    def is_invalidation_enabled(self) -> bool:
        """
        Get display invalidation is enabled. return true if invalidation is enabled 
        

        :returns: return true if invalidation is enabled 
        :rtype: bool
        """
        ...

    def get_refr_timer(self) -> "timer_t":
        """
        Get a pointer to the screen refresher timer to modify its parameters with lv_timer_... functions. pointer to the display refresher timer. (NULL on error) 
        

        :returns: pointer to the display refresher timer. (NULL on error) 
        :rtype: "timer_t"
        """
        ...

    def delete_refr_timer(self) -> None:
        """
        Delete screen refresher timer 
        

        :returns: 
        :rtype: None
        """
        ...

    def set_user_data(self, disp: "display_t") -> None:
        """
        :param disp: 
        :type disp: "display_t"

        :returns: 
        :rtype: None
        """
        ...

    def set_driver_data(self, disp: "display_t") -> None:
        """
        :param disp: 
        :type disp: "display_t"

        :returns: 
        :rtype: None
        """
        ...

    def get_user_data(self) -> Any:
        """

        :returns: 
        :rtype: Any
        """
        ...

    def get_driver_data(self) -> Any:
        """

        :returns: 
        :rtype: Any
        """
        ...

    def get_buf_active(self) -> "draw_buf_t":
        """

        :returns: 
        :rtype: "draw_buf_t"
        """
        ...

    def rotate_area(self, area: "area_t") -> None:
        """
        Rotate an area in-place according to the display's rotation 
        
        :param area: pointer to an area to rotate 
        :type area: "area_t"

        :returns: 
        :rtype: None
        """
        ...

    def dpx(self, n: int) -> int:
        """
        Scale the given number of pixels (a distance or size) relative to a 160 DPI display considering the DPI of the given display. It ensures that e.g. lv_dpx(100) will have the same physical size regardless to the DPI of the display. n x current_dpi/160 
        
        :param n: the number of pixels to scale 
        :type n: int

        :returns: n x current_dpi/160 
        :rtype: int
        """
        ...



class _type_area_t(TypedDict, total=False):
    x1: int
    y1: int
    x2: int
    y2: int


class area_t(Struct):

    __SIZE__: ClassVar[int] = ...
    
    def __init__(self, *, kwargs: _type_area_t = dict()):
        ...

    @property
    def x1(self) -> int:
        """
        :type value: int
        :rtype: int
        """
    
        ...    

    @x1.setter
    def x1(self, value: int):
        ...    

    @property
    def y1(self) -> int:
        """
        :type value: int
        :rtype: int
        """
    
        ...    

    @y1.setter
    def y1(self, value: int):
        ...    

    @property
    def x2(self) -> int:
        """
        :type value: int
        :rtype: int
        """
    
        ...    

    @x2.setter
    def x2(self, value: int):
        ...    

    @property
    def y2(self) -> int:
        """
        :type value: int
        :rtype: int
        """
    
        ...    

    @y2.setter
    def y2(self, value: int):
        ...    


    def copy(self, src: "area_t") -> None:
        """
        Copy an area 
        
        :param src: pointer to the source area 
        :type src: "area_t"

        :returns: 
        :rtype: None
        """
        ...

    def set(self, x1: int, y1: int, x2: int, y2: int) -> None:
        """
        Initialize an area 
        
        :param x1: left coordinate of the area 
        :type x1: int
        :param y1: top coordinate of the area 
        :type y1: int
        :param x2: right coordinate of the area 
        :type x2: int
        :param y2: bottom coordinate of the area 
        :type y2: int

        :returns: 
        :rtype: None
        """
        ...

    def get_width(self) -> int:
        """
        Get the width of an area the width of the area (if x1 == x2 -> width = 1) 
        

        :returns: the width of the area (if x1 == x2 -> width = 1) 
        :rtype: int
        """
        ...

    def get_height(self) -> int:
        """
        Get the height of an area the height of the area (if y1 == y2 -> height = 1) 
        

        :returns: the height of the area (if y1 == y2 -> height = 1) 
        :rtype: int
        """
        ...

    def set_width(self, w: int) -> None:
        """
        Set the width of an area 
        
        :param w: the new width of the area (w == 1 makes x1 == x2) 
        :type w: int

        :returns: 
        :rtype: None
        """
        ...

    def set_height(self, w: int) -> None:
        """
        Set the height of an area 
        
        :param w: the new height of the area (h == 1 makes y1 == y2) 
        :type w: int

        :returns: 
        :rtype: None
        """
        ...

    def get_size(self) -> int:
        """
        Return with area of an area (x * y) size of area 
        

        :returns: size of area 
        :rtype: int
        """
        ...

    def increase(self, w_extra: int, h_extra: int) -> None:
        """
        :param w_extra: 
        :type w_extra: int
        :param h_extra: 
        :type h_extra: int

        :returns: 
        :rtype: None
        """
        ...

    def move(self, w_extra: int, h_extra: int) -> None:
        """
        :param w_extra: 
        :type w_extra: int
        :param h_extra: 
        :type h_extra: int

        :returns: 
        :rtype: None
        """
        ...

    def align(self, to_align: "area_t", align: align_t, ofs_x: int, ofs_y: int) -> None:
        """
        Align an area to another 
        
        :param to_align: the area to align 
        :type to_align: "area_t"
        :param align: LV_ALIGN_... 
        :type align: align_t
        :param ofs_x: X offset 
        :type ofs_x: int
        :param ofs_y: Y offset 
        :type ofs_y: int

        :returns: 
        :rtype: None
        """
        ...



class _type_point_t(TypedDict, total=False):
    x: int
    y: int


class point_t(Struct):

    __SIZE__: ClassVar[int] = ...
    
    def __init__(self, *, kwargs: _type_point_t = dict()):
        ...

    @property
    def x(self) -> int:
        """
        :type value: int
        :rtype: int
        """
    
        ...    

    @x.setter
    def x(self, value: int):
        ...    

    @property
    def y(self) -> int:
        """
        :type value: int
        :rtype: int
        """
    
        ...    

    @y.setter
    def y(self, value: int):
        ...    


    def transform(self, angle: int, scale_x: int, scale_y: int, pivot: "point_t", zoom_first: bool) -> None:
        """
        Transform a point 
        
        :param angle: angle with 0.1 resolutions (123 means 12.3°) 
        :type angle: int
        :param scale_x: horizontal zoom, 256 means 100% 
        :type scale_x: int
        :param scale_y: vertical zoom, 256 means 100% 
        :type scale_y: int
        :param pivot: pointer to the pivot point of the transformation 
        :type pivot: "point_t"
        :param zoom_first: true: zoom first and rotate after that; else: opposite order 
        :type zoom_first: bool

        :returns: 
        :rtype: None
        """
        ...

    def array_transform(self, count: int, angle: int, scale_x: int, scale_y: int, pivot: "point_t", zoom_first: bool) -> None:
        """
        Transform an array of points 
        
        :param count: number of points in the array 
        :type count: int
        :param angle: angle with 0.1 resolutions (123 means 12.3°) 
        :type angle: int
        :param scale_x: horizontal zoom, 256 means 100% 
        :type scale_x: int
        :param scale_y: vertical zoom, 256 means 100% 
        :type scale_y: int
        :param pivot: pointer to the pivot point of the transformation 
        :type pivot: "point_t"
        :param zoom_first: true: zoom first and rotate after that; else: opposite order 
        :type zoom_first: bool

        :returns: 
        :rtype: None
        """
        ...

    def to_precise(self) -> "point_precise_t":
        """

        :returns: 
        :rtype: "point_precise_t"
        """
        ...

    def set(self, x: int, y: int) -> None:
        """
        :param x: 
        :type x: int
        :param y: 
        :type y: int

        :returns: 
        :rtype: None
        """
        ...

    def swap(self, p2: "point_t") -> None:
        """
        :param p2: 
        :type p2: "point_t"

        :returns: 
        :rtype: None
        """
        ...



class _type_style_t(TypedDict, total=False):
    values_and_props: Any
    has_group: int
    prop_cnt: int


class style_t(Struct):

    __SIZE__: ClassVar[int] = ...
    
    def __init__(self, *, kwargs: _type_style_t = dict()):
        ...

    @property
    def values_and_props(self) -> Any:
        """
        :type value: Any
        :rtype: Any
        """
    
        ...    

    @values_and_props.setter
    def values_and_props(self, value: Any):
        ...    

    @property
    def has_group(self) -> int:
        """
        :type value: int
        :rtype: int
        """
    
        ...    

    @has_group.setter
    def has_group(self, value: int):
        ...    

    @property
    def prop_cnt(self) -> int:
        """
        :type value: int
        :rtype: int
        """
    
        ...    

    @prop_cnt.setter
    def prop_cnt(self, value: int):
        ...    


    def is_const(self) -> bool:
        """
        Check if a style is constant true: the style is constant 
        

        :returns: true: the style is constant 
        :rtype: bool
        """
        ...

    def get_prop_inlined(self, prop: "style_prop_t", value: "style_value_t") -> "style_res_t":
        """
        Get the value of a property LV_RESULT_INVALID: the property wasn't found in the style ( value is unchanged) LV_RESULT_OK: the property was fond, and value is set accordingly  For performance reasons there are no sanity check on style  This function is the same as :ref:`lv_style_get_prop` but inlined. Use it only on performance critical places 
        
        :param prop: the ID of a property 
        :type prop: "style_prop_t"
        :param value: pointer to a :ref:`lv_style_value_t` variable to store the value 
        :type value: "style_value_t"

        :returns: LV_RESULT_INVALID: the property wasn't found in the style ( value is unchanged) LV_RESULT_OK: the property was fond, and value is set accordingly 
        :rtype: "style_res_t"
        """
        ...

    def set_size(self, width: int, height: int) -> None:
        """
        :param width: 
        :type width: int
        :param height: 
        :type height: int

        :returns: 
        :rtype: None
        """
        ...

    def set_pad_all(self, value: int) -> None:
        """
        :param value: 
        :type value: int

        :returns: 
        :rtype: None
        """
        ...

    def set_pad_hor(self, value: int) -> None:
        """
        :param value: 
        :type value: int

        :returns: 
        :rtype: None
        """
        ...

    def set_pad_ver(self, value: int) -> None:
        """
        :param value: 
        :type value: int

        :returns: 
        :rtype: None
        """
        ...

    def set_pad_gap(self, value: int) -> None:
        """
        :param value: 
        :type value: int

        :returns: 
        :rtype: None
        """
        ...

    def set_transform_scale(self, value: int) -> None:
        """
        :param value: 
        :type value: int

        :returns: 
        :rtype: None
        """
        ...

    def init(self) -> None:
        """
        Initialize a style Do not call lv_style_init on styles that already have some properties because this function won't free the used memory, just sets a default state for the style. In other words be sure to initialize styles only once! 
        

        :returns: 
        :rtype: None
        """
        ...

    def reset(self) -> None:
        """
        Clear all properties from a style and free all allocated memories. 
        

        :returns: 
        :rtype: None
        """
        ...

    def remove_prop(self, prop: "style_prop_t") -> bool:
        """
        Remove a property from a style true: the property was found and removed; false: the property wasn't found 
        
        :param prop: a style property ORed with a state. 
        :type prop: "style_prop_t"

        :returns: true: the property was found and removed; false: the property wasn't found 
        :rtype: bool
        """
        ...

    def set_prop(self, prop: "style_prop_t", value: "style_value_t") -> None:
        """
        Set the value of property in a style. This function shouldn't be used directly by the user. Instead use lv_style_set_<prop_name>() . E.g. lv_style_set_bg_color() 
        
        :param prop: the ID of a property (e.g. LV_STYLE_BG_COLOR ) 
        :type prop: "style_prop_t"
        :param value: :ref:`lv_style_value_t` variable in which a field is set according to the type of prop 
        :type value: "style_value_t"

        :returns: 
        :rtype: None
        """
        ...

    def get_prop(self, prop: "style_prop_t", value: "style_value_t") -> "style_res_t":
        """
        Get the value of a property LV_RESULT_INVALID: the property wasn't found in the style ( value is unchanged) LV_RESULT_OK: the property was fond, and value is set accordingly  For performance reasons there are no sanity check on style 
        
        :param prop: the ID of a property 
        :type prop: "style_prop_t"
        :param value: pointer to a :ref:`lv_style_value_t` variable to store the value 
        :type value: "style_value_t"

        :returns: LV_RESULT_INVALID: the property wasn't found in the style ( value is unchanged) LV_RESULT_OK: the property was fond, and value is set accordingly 
        :rtype: "style_res_t"
        """
        ...

    def is_empty(self) -> bool:
        """
        Checks if a style is empty (has no properties) true if the style is empty 
        

        :returns: true if the style is empty 
        :rtype: bool
        """
        ...

    def set_width(self, value: int) -> None:
        """
        :param value: 
        :type value: int

        :returns: 
        :rtype: None
        """
        ...

    def set_min_width(self, value: int) -> None:
        """
        :param value: 
        :type value: int

        :returns: 
        :rtype: None
        """
        ...

    def set_max_width(self, value: int) -> None:
        """
        :param value: 
        :type value: int

        :returns: 
        :rtype: None
        """
        ...

    def set_height(self, value: int) -> None:
        """
        :param value: 
        :type value: int

        :returns: 
        :rtype: None
        """
        ...

    def set_min_height(self, value: int) -> None:
        """
        :param value: 
        :type value: int

        :returns: 
        :rtype: None
        """
        ...

    def set_max_height(self, value: int) -> None:
        """
        :param value: 
        :type value: int

        :returns: 
        :rtype: None
        """
        ...

    def set_length(self, value: int) -> None:
        """
        :param value: 
        :type value: int

        :returns: 
        :rtype: None
        """
        ...

    def set_x(self, value: int) -> None:
        """
        :param value: 
        :type value: int

        :returns: 
        :rtype: None
        """
        ...

    def set_y(self, value: int) -> None:
        """
        :param value: 
        :type value: int

        :returns: 
        :rtype: None
        """
        ...

    def set_align(self, value: align_t) -> None:
        """
        :param value: 
        :type value: align_t

        :returns: 
        :rtype: None
        """
        ...

    def set_transform_width(self, value: int) -> None:
        """
        :param value: 
        :type value: int

        :returns: 
        :rtype: None
        """
        ...

    def set_transform_height(self, value: int) -> None:
        """
        :param value: 
        :type value: int

        :returns: 
        :rtype: None
        """
        ...

    def set_translate_x(self, value: int) -> None:
        """
        :param value: 
        :type value: int

        :returns: 
        :rtype: None
        """
        ...

    def set_translate_y(self, value: int) -> None:
        """
        :param value: 
        :type value: int

        :returns: 
        :rtype: None
        """
        ...

    def set_transform_scale_x(self, value: int) -> None:
        """
        :param value: 
        :type value: int

        :returns: 
        :rtype: None
        """
        ...

    def set_transform_scale_y(self, value: int) -> None:
        """
        :param value: 
        :type value: int

        :returns: 
        :rtype: None
        """
        ...

    def set_transform_rotation(self, value: int) -> None:
        """
        :param value: 
        :type value: int

        :returns: 
        :rtype: None
        """
        ...

    def set_transform_pivot_x(self, value: int) -> None:
        """
        :param value: 
        :type value: int

        :returns: 
        :rtype: None
        """
        ...

    def set_transform_pivot_y(self, value: int) -> None:
        """
        :param value: 
        :type value: int

        :returns: 
        :rtype: None
        """
        ...

    def set_transform_skew_x(self, value: int) -> None:
        """
        :param value: 
        :type value: int

        :returns: 
        :rtype: None
        """
        ...

    def set_transform_skew_y(self, value: int) -> None:
        """
        :param value: 
        :type value: int

        :returns: 
        :rtype: None
        """
        ...

    def set_pad_top(self, value: int) -> None:
        """
        :param value: 
        :type value: int

        :returns: 
        :rtype: None
        """
        ...

    def set_pad_bottom(self, value: int) -> None:
        """
        :param value: 
        :type value: int

        :returns: 
        :rtype: None
        """
        ...

    def set_pad_left(self, value: int) -> None:
        """
        :param value: 
        :type value: int

        :returns: 
        :rtype: None
        """
        ...

    def set_pad_right(self, value: int) -> None:
        """
        :param value: 
        :type value: int

        :returns: 
        :rtype: None
        """
        ...

    def set_pad_row(self, value: int) -> None:
        """
        :param value: 
        :type value: int

        :returns: 
        :rtype: None
        """
        ...

    def set_pad_column(self, value: int) -> None:
        """
        :param value: 
        :type value: int

        :returns: 
        :rtype: None
        """
        ...

    def set_margin_top(self, value: int) -> None:
        """
        :param value: 
        :type value: int

        :returns: 
        :rtype: None
        """
        ...

    def set_margin_bottom(self, value: int) -> None:
        """
        :param value: 
        :type value: int

        :returns: 
        :rtype: None
        """
        ...

    def set_margin_left(self, value: int) -> None:
        """
        :param value: 
        :type value: int

        :returns: 
        :rtype: None
        """
        ...

    def set_margin_right(self, value: int) -> None:
        """
        :param value: 
        :type value: int

        :returns: 
        :rtype: None
        """
        ...

    def set_bg_color(self, value: "color_t") -> None:
        """
        :param value: 
        :type value: "color_t"

        :returns: 
        :rtype: None
        """
        ...

    def set_bg_opa(self, value: opa_t) -> None:
        """
        :param value: 
        :type value: opa_t

        :returns: 
        :rtype: None
        """
        ...

    def set_bg_grad_color(self, value: "color_t") -> None:
        """
        :param value: 
        :type value: "color_t"

        :returns: 
        :rtype: None
        """
        ...

    def set_bg_grad_dir(self, value: grad_dir_t) -> None:
        """
        :param value: 
        :type value: grad_dir_t

        :returns: 
        :rtype: None
        """
        ...

    def set_bg_main_stop(self, value: int) -> None:
        """
        :param value: 
        :type value: int

        :returns: 
        :rtype: None
        """
        ...

    def set_bg_grad_stop(self, value: int) -> None:
        """
        :param value: 
        :type value: int

        :returns: 
        :rtype: None
        """
        ...

    def set_bg_main_opa(self, value: opa_t) -> None:
        """
        :param value: 
        :type value: opa_t

        :returns: 
        :rtype: None
        """
        ...

    def set_bg_grad_opa(self, value: opa_t) -> None:
        """
        :param value: 
        :type value: opa_t

        :returns: 
        :rtype: None
        """
        ...

    def set_bg_grad(self, value: "grad_dsc_t") -> None:
        """
        :param value: 
        :type value: "grad_dsc_t"

        :returns: 
        :rtype: None
        """
        ...

    def set_bg_image_src(self, value: Any) -> None:
        """
        :param value: 
        :type value: Any

        :returns: 
        :rtype: None
        """
        ...

    def set_bg_image_opa(self, value: opa_t) -> None:
        """
        :param value: 
        :type value: opa_t

        :returns: 
        :rtype: None
        """
        ...

    def set_bg_image_recolor(self, value: "color_t") -> None:
        """
        :param value: 
        :type value: "color_t"

        :returns: 
        :rtype: None
        """
        ...

    def set_bg_image_recolor_opa(self, value: opa_t) -> None:
        """
        :param value: 
        :type value: opa_t

        :returns: 
        :rtype: None
        """
        ...

    def set_bg_image_tiled(self, value: bool) -> None:
        """
        :param value: 
        :type value: bool

        :returns: 
        :rtype: None
        """
        ...

    def set_border_color(self, value: "color_t") -> None:
        """
        :param value: 
        :type value: "color_t"

        :returns: 
        :rtype: None
        """
        ...

    def set_border_opa(self, value: opa_t) -> None:
        """
        :param value: 
        :type value: opa_t

        :returns: 
        :rtype: None
        """
        ...

    def set_border_width(self, value: int) -> None:
        """
        :param value: 
        :type value: int

        :returns: 
        :rtype: None
        """
        ...

    def set_border_side(self, value: border_side_t) -> None:
        """
        :param value: 
        :type value: border_side_t

        :returns: 
        :rtype: None
        """
        ...

    def set_border_post(self, value: bool) -> None:
        """
        :param value: 
        :type value: bool

        :returns: 
        :rtype: None
        """
        ...

    def set_outline_width(self, value: int) -> None:
        """
        :param value: 
        :type value: int

        :returns: 
        :rtype: None
        """
        ...

    def set_outline_color(self, value: "color_t") -> None:
        """
        :param value: 
        :type value: "color_t"

        :returns: 
        :rtype: None
        """
        ...

    def set_outline_opa(self, value: opa_t) -> None:
        """
        :param value: 
        :type value: opa_t

        :returns: 
        :rtype: None
        """
        ...

    def set_outline_pad(self, value: int) -> None:
        """
        :param value: 
        :type value: int

        :returns: 
        :rtype: None
        """
        ...

    def set_shadow_width(self, value: int) -> None:
        """
        :param value: 
        :type value: int

        :returns: 
        :rtype: None
        """
        ...

    def set_shadow_offset_x(self, value: int) -> None:
        """
        :param value: 
        :type value: int

        :returns: 
        :rtype: None
        """
        ...

    def set_shadow_offset_y(self, value: int) -> None:
        """
        :param value: 
        :type value: int

        :returns: 
        :rtype: None
        """
        ...

    def set_shadow_spread(self, value: int) -> None:
        """
        :param value: 
        :type value: int

        :returns: 
        :rtype: None
        """
        ...

    def set_shadow_color(self, value: "color_t") -> None:
        """
        :param value: 
        :type value: "color_t"

        :returns: 
        :rtype: None
        """
        ...

    def set_shadow_opa(self, value: opa_t) -> None:
        """
        :param value: 
        :type value: opa_t

        :returns: 
        :rtype: None
        """
        ...

    def set_image_opa(self, value: opa_t) -> None:
        """
        :param value: 
        :type value: opa_t

        :returns: 
        :rtype: None
        """
        ...

    def set_image_recolor(self, value: "color_t") -> None:
        """
        :param value: 
        :type value: "color_t"

        :returns: 
        :rtype: None
        """
        ...

    def set_image_recolor_opa(self, value: opa_t) -> None:
        """
        :param value: 
        :type value: opa_t

        :returns: 
        :rtype: None
        """
        ...

    def set_line_width(self, value: int) -> None:
        """
        :param value: 
        :type value: int

        :returns: 
        :rtype: None
        """
        ...

    def set_line_dash_width(self, value: int) -> None:
        """
        :param value: 
        :type value: int

        :returns: 
        :rtype: None
        """
        ...

    def set_line_dash_gap(self, value: int) -> None:
        """
        :param value: 
        :type value: int

        :returns: 
        :rtype: None
        """
        ...

    def set_line_rounded(self, value: bool) -> None:
        """
        :param value: 
        :type value: bool

        :returns: 
        :rtype: None
        """
        ...

    def set_line_color(self, value: "color_t") -> None:
        """
        :param value: 
        :type value: "color_t"

        :returns: 
        :rtype: None
        """
        ...

    def set_line_opa(self, value: opa_t) -> None:
        """
        :param value: 
        :type value: opa_t

        :returns: 
        :rtype: None
        """
        ...

    def set_arc_width(self, value: int) -> None:
        """
        :param value: 
        :type value: int

        :returns: 
        :rtype: None
        """
        ...

    def set_arc_rounded(self, value: bool) -> None:
        """
        :param value: 
        :type value: bool

        :returns: 
        :rtype: None
        """
        ...

    def set_arc_color(self, value: "color_t") -> None:
        """
        :param value: 
        :type value: "color_t"

        :returns: 
        :rtype: None
        """
        ...

    def set_arc_opa(self, value: opa_t) -> None:
        """
        :param value: 
        :type value: opa_t

        :returns: 
        :rtype: None
        """
        ...

    def set_arc_image_src(self, value: Any) -> None:
        """
        :param value: 
        :type value: Any

        :returns: 
        :rtype: None
        """
        ...

    def set_text_color(self, value: "color_t") -> None:
        """
        :param value: 
        :type value: "color_t"

        :returns: 
        :rtype: None
        """
        ...

    def set_text_opa(self, value: opa_t) -> None:
        """
        :param value: 
        :type value: opa_t

        :returns: 
        :rtype: None
        """
        ...

    def set_text_font(self, value: "font_t") -> None:
        """
        :param value: 
        :type value: "font_t"

        :returns: 
        :rtype: None
        """
        ...

    def set_text_letter_space(self, value: int) -> None:
        """
        :param value: 
        :type value: int

        :returns: 
        :rtype: None
        """
        ...

    def set_text_line_space(self, value: int) -> None:
        """
        :param value: 
        :type value: int

        :returns: 
        :rtype: None
        """
        ...

    def set_text_decor(self, value: text_decor_t) -> None:
        """
        :param value: 
        :type value: text_decor_t

        :returns: 
        :rtype: None
        """
        ...

    def set_text_align(self, value: text_align_t) -> None:
        """
        :param value: 
        :type value: text_align_t

        :returns: 
        :rtype: None
        """
        ...

    def set_radius(self, value: int) -> None:
        """
        :param value: 
        :type value: int

        :returns: 
        :rtype: None
        """
        ...

    def set_clip_corner(self, value: bool) -> None:
        """
        :param value: 
        :type value: bool

        :returns: 
        :rtype: None
        """
        ...

    def set_opa(self, value: opa_t) -> None:
        """
        :param value: 
        :type value: opa_t

        :returns: 
        :rtype: None
        """
        ...

    def set_opa_layered(self, value: opa_t) -> None:
        """
        :param value: 
        :type value: opa_t

        :returns: 
        :rtype: None
        """
        ...

    def set_color_filter_dsc(self, value: "color_filter_dsc_t") -> None:
        """
        :param value: 
        :type value: "color_filter_dsc_t"

        :returns: 
        :rtype: None
        """
        ...

    def set_color_filter_opa(self, value: opa_t) -> None:
        """
        :param value: 
        :type value: opa_t

        :returns: 
        :rtype: None
        """
        ...

    def set_anim(self, value: anim_t) -> None:
        """
        :param value: 
        :type value: anim_t

        :returns: 
        :rtype: None
        """
        ...

    def set_anim_duration(self, value: int) -> None:
        """
        :param value: 
        :type value: int

        :returns: 
        :rtype: None
        """
        ...

    def set_transition(self, value: "style_transition_dsc_t") -> None:
        """
        :param value: 
        :type value: "style_transition_dsc_t"

        :returns: 
        :rtype: None
        """
        ...

    def set_blend_mode(self, value: blend_mode_t) -> None:
        """
        :param value: 
        :type value: blend_mode_t

        :returns: 
        :rtype: None
        """
        ...

    def set_layout(self, value: int) -> None:
        """
        :param value: 
        :type value: int

        :returns: 
        :rtype: None
        """
        ...

    def set_base_dir(self, value: base_dir_t) -> None:
        """
        :param value: 
        :type value: base_dir_t

        :returns: 
        :rtype: None
        """
        ...

    def set_bitmap_mask_src(self, value: Any) -> None:
        """
        :param value: 
        :type value: Any

        :returns: 
        :rtype: None
        """
        ...

    def set_rotary_sensitivity(self, value: int) -> None:
        """
        :param value: 
        :type value: int

        :returns: 
        :rtype: None
        """
        ...

    def set_flex_flow(self, value: flex_flow_t) -> None:
        """

        :returns: 
        :rtype: None
        """
        ...

    def set_flex_main_place(self, value: flex_align_t) -> None:
        """

        :returns: 
        :rtype: None
        """
        ...

    def set_flex_cross_place(self, value: flex_align_t) -> None:
        """

        :returns: 
        :rtype: None
        """
        ...

    def set_flex_track_place(self, value: flex_align_t) -> None:
        """

        :returns: 
        :rtype: None
        """
        ...

    def set_flex_grow(self, value: int) -> None:
        """

        :returns: 
        :rtype: None
        """
        ...

    def set_grid_column_dsc_array(self, value: List[int]) -> None:
        """

        :returns: 
        :rtype: None
        """
        ...

    def set_grid_column_align(self, value: grid_align_t) -> None:
        """

        :returns: 
        :rtype: None
        """
        ...

    def set_grid_row_dsc_array(self, value: List[int]) -> None:
        """

        :returns: 
        :rtype: None
        """
        ...

    def set_grid_row_align(self, value: grid_align_t) -> None:
        """

        :returns: 
        :rtype: None
        """
        ...

    def set_grid_cell_column_pos(self, value: int) -> None:
        """

        :returns: 
        :rtype: None
        """
        ...

    def set_grid_cell_x_align(self, value: grid_align_t) -> None:
        """

        :returns: 
        :rtype: None
        """
        ...

    def set_grid_cell_column_span(self, value: int) -> None:
        """

        :returns: 
        :rtype: None
        """
        ...

    def set_grid_cell_row_pos(self, value: int) -> None:
        """

        :returns: 
        :rtype: None
        """
        ...

    def set_grid_cell_y_align(self, value: grid_align_t) -> None:
        """

        :returns: 
        :rtype: None
        """
        ...

    def set_grid_cell_row_span(self, value: int) -> None:
        """

        :returns: 
        :rtype: None
        """
        ...



class _type_style_value_t(TypedDict, total=False):
    num: int
    ptr: Any
    color: "color_t"


class style_value_t(Struct):

    __SIZE__: ClassVar[int] = ...
    
    def __init__(self, *, kwargs: _type_style_value_t = dict()):
        ...

    @property
    def num(self) -> int:
        """
        :type value: int
        :rtype: int
        """
    
        ...    

    @num.setter
    def num(self, value: int):
        ...    

    @property
    def ptr(self) -> Any:
        """
        :type value: Any
        :rtype: Any
        """
    
        ...    

    @ptr.setter
    def ptr(self, value: Any):
        ...    

    @property
    def color(self) -> "color_t":
        """
        :type value: "color_t"
        :rtype: "color_t"
        """
    
        ...    

    @color.setter
    def color(self, value: "color_t"):
        ...    



class _type_draw_rect_dsc_t(TypedDict, total=False):
    base: "draw_dsc_base_t"
    radius: int
    bg_opa: "opa_t"
    bg_color: "color_t"
    bg_grad: "grad_dsc_t"
    bg_image_src: Any
    bg_image_symbol_font: Any
    bg_image_recolor: "color_t"
    bg_image_opa: "opa_t"
    bg_image_recolor_opa: "opa_t"
    bg_image_tiled: int
    border_color: "color_t"
    border_width: int
    border_opa: "opa_t"
    border_side: "border_side_t"
    border_post: int
    outline_color: "color_t"
    outline_width: int
    outline_pad: int
    outline_opa: "opa_t"
    shadow_color: "color_t"
    shadow_width: int
    shadow_offset_x: int
    shadow_offset_y: int
    shadow_spread: int
    shadow_opa: "opa_t"


class draw_rect_dsc_t(Struct):

    __SIZE__: ClassVar[int] = ...
    
    def __init__(self, *, kwargs: _type_draw_rect_dsc_t = dict()):
        ...

    @property
    def base(self) -> "draw_dsc_base_t":
        """
        :type value: "draw_dsc_base_t"
        :rtype: "draw_dsc_base_t"
        """
    
        ...    

    @base.setter
    def base(self, value: "draw_dsc_base_t"):
        ...    

    @property
    def radius(self) -> int:
        """
        :type value: int
        :rtype: int
        """
    
        ...    

    @radius.setter
    def radius(self, value: int):
        ...    

    @property
    def bg_opa(self) -> "opa_t":
        """
        :type value: "opa_t"
        :rtype: "opa_t"
        """
    
        ...    

    @bg_opa.setter
    def bg_opa(self, value: "opa_t"):
        ...    

    @property
    def bg_color(self) -> "color_t":
        """
        :type value: "color_t"
        :rtype: "color_t"
        """
    
        ...    

    @bg_color.setter
    def bg_color(self, value: "color_t"):
        ...    

    @property
    def bg_grad(self) -> "grad_dsc_t":
        """
        :type value: "grad_dsc_t"
        :rtype: "grad_dsc_t"
        """
    
        ...    

    @bg_grad.setter
    def bg_grad(self, value: "grad_dsc_t"):
        ...    

    @property
    def bg_image_src(self) -> Any:
        """
        :type value: Any
        :rtype: Any
        """
    
        ...    

    @bg_image_src.setter
    def bg_image_src(self, value: Any):
        ...    

    @property
    def bg_image_symbol_font(self) -> Any:
        """
        :type value: Any
        :rtype: Any
        """
    
        ...    

    @bg_image_symbol_font.setter
    def bg_image_symbol_font(self, value: Any):
        ...    

    @property
    def bg_image_recolor(self) -> "color_t":
        """
        :type value: "color_t"
        :rtype: "color_t"
        """
    
        ...    

    @bg_image_recolor.setter
    def bg_image_recolor(self, value: "color_t"):
        ...    

    @property
    def bg_image_opa(self) -> "opa_t":
        """
        :type value: "opa_t"
        :rtype: "opa_t"
        """
    
        ...    

    @bg_image_opa.setter
    def bg_image_opa(self, value: "opa_t"):
        ...    

    @property
    def bg_image_recolor_opa(self) -> "opa_t":
        """
        :type value: "opa_t"
        :rtype: "opa_t"
        """
    
        ...    

    @bg_image_recolor_opa.setter
    def bg_image_recolor_opa(self, value: "opa_t"):
        ...    

    @property
    def bg_image_tiled(self) -> int:
        """
        :type value: int
        :rtype: int
        """
    
        ...    

    @bg_image_tiled.setter
    def bg_image_tiled(self, value: int):
        ...    

    @property
    def border_color(self) -> "color_t":
        """
        :type value: "color_t"
        :rtype: "color_t"
        """
    
        ...    

    @border_color.setter
    def border_color(self, value: "color_t"):
        ...    

    @property
    def border_width(self) -> int:
        """
        :type value: int
        :rtype: int
        """
    
        ...    

    @border_width.setter
    def border_width(self, value: int):
        ...    

    @property
    def border_opa(self) -> "opa_t":
        """
        :type value: "opa_t"
        :rtype: "opa_t"
        """
    
        ...    

    @border_opa.setter
    def border_opa(self, value: "opa_t"):
        ...    

    @property
    def border_side(self) -> "border_side_t":
        """
        :type value: "border_side_t"
        :rtype: "border_side_t"
        """
    
        ...    

    @border_side.setter
    def border_side(self, value: "border_side_t"):
        ...    

    @property
    def border_post(self) -> int:
        """
        :type value: int
        :rtype: int
        """
    
        ...    

    @border_post.setter
    def border_post(self, value: int):
        ...    

    @property
    def outline_color(self) -> "color_t":
        """
        :type value: "color_t"
        :rtype: "color_t"
        """
    
        ...    

    @outline_color.setter
    def outline_color(self, value: "color_t"):
        ...    

    @property
    def outline_width(self) -> int:
        """
        :type value: int
        :rtype: int
        """
    
        ...    

    @outline_width.setter
    def outline_width(self, value: int):
        ...    

    @property
    def outline_pad(self) -> int:
        """
        :type value: int
        :rtype: int
        """
    
        ...    

    @outline_pad.setter
    def outline_pad(self, value: int):
        ...    

    @property
    def outline_opa(self) -> "opa_t":
        """
        :type value: "opa_t"
        :rtype: "opa_t"
        """
    
        ...    

    @outline_opa.setter
    def outline_opa(self, value: "opa_t"):
        ...    

    @property
    def shadow_color(self) -> "color_t":
        """
        :type value: "color_t"
        :rtype: "color_t"
        """
    
        ...    

    @shadow_color.setter
    def shadow_color(self, value: "color_t"):
        ...    

    @property
    def shadow_width(self) -> int:
        """
        :type value: int
        :rtype: int
        """
    
        ...    

    @shadow_width.setter
    def shadow_width(self, value: int):
        ...    

    @property
    def shadow_offset_x(self) -> int:
        """
        :type value: int
        :rtype: int
        """
    
        ...    

    @shadow_offset_x.setter
    def shadow_offset_x(self, value: int):
        ...    

    @property
    def shadow_offset_y(self) -> int:
        """
        :type value: int
        :rtype: int
        """
    
        ...    

    @shadow_offset_y.setter
    def shadow_offset_y(self, value: int):
        ...    

    @property
    def shadow_spread(self) -> int:
        """
        :type value: int
        :rtype: int
        """
    
        ...    

    @shadow_spread.setter
    def shadow_spread(self, value: int):
        ...    

    @property
    def shadow_opa(self) -> "opa_t":
        """
        :type value: "opa_t"
        :rtype: "opa_t"
        """
    
        ...    

    @shadow_opa.setter
    def shadow_opa(self, value: "opa_t"):
        ...    


    def init(self) -> None:
        """
        Initialize a rectangle draw descriptor. 
        

        :returns: 
        :rtype: None
        """
        ...



class _type_draw_dsc_base_t(TypedDict, total=False):
    obj: "obj"
    part: "part_t"
    id1: int
    id2: int
    layer: "layer_t"
    dsc_size: int
    user_data: Any


class draw_dsc_base_t(Struct):

    __SIZE__: ClassVar[int] = ...
    
    def __init__(self, *, kwargs: _type_draw_dsc_base_t = dict()):
        ...

    @property
    def obj(self) -> "obj":
        """
        :type value: "obj"
        :rtype: "obj"
        """
    
        ...    

    @obj.setter
    def obj(self, value: "obj"):
        ...    

    @property
    def part(self) -> "part_t":
        """
        :type value: "part_t"
        :rtype: "part_t"
        """
    
        ...    

    @part.setter
    def part(self, value: "part_t"):
        ...    

    @property
    def id1(self) -> int:
        """
        :type value: int
        :rtype: int
        """
    
        ...    

    @id1.setter
    def id1(self, value: int):
        ...    

    @property
    def id2(self) -> int:
        """
        :type value: int
        :rtype: int
        """
    
        ...    

    @id2.setter
    def id2(self, value: int):
        ...    

    @property
    def layer(self) -> "layer_t":
        """
        :type value: "layer_t"
        :rtype: "layer_t"
        """
    
        ...    

    @layer.setter
    def layer(self, value: "layer_t"):
        ...    

    @property
    def dsc_size(self) -> int:
        """
        :type value: int
        :rtype: int
        """
    
        ...    

    @dsc_size.setter
    def dsc_size(self, value: int):
        ...    

    @property
    def user_data(self) -> Any:
        """
        :type value: Any
        :rtype: Any
        """
    
        ...    

    @user_data.setter
    def user_data(self, value: Any):
        ...    



class _type_layer_t(TypedDict, total=False):
    draw_buf: "draw_buf_t"
    buf_area: "area_t"
    color_format: "color_format_t"
    _clip_area: "area_t"
    phy_clip_area: "area_t"
    draw_task_head: "draw_task_t"
    parent: "layer_t"
    next: "layer_t"
    all_tasks_added: bool
    user_data: Any


class layer_t(Struct):

    __SIZE__: ClassVar[int] = ...
    
    def __init__(self, *, kwargs: _type_layer_t = dict()):
        ...

    @property
    def draw_buf(self) -> "draw_buf_t":
        """
        :type value: "draw_buf_t"
        :rtype: "draw_buf_t"
        """
    
        ...    

    @draw_buf.setter
    def draw_buf(self, value: "draw_buf_t"):
        ...    

    @property
    def buf_area(self) -> "area_t":
        """
        :type value: "area_t"
        :rtype: "area_t"
        """
    
        ...    

    @buf_area.setter
    def buf_area(self, value: "area_t"):
        ...    

    @property
    def color_format(self) -> "color_format_t":
        """
        :type value: "color_format_t"
        :rtype: "color_format_t"
        """
    
        ...    

    @color_format.setter
    def color_format(self, value: "color_format_t"):
        ...    

    @property
    def _clip_area(self) -> "area_t":
        """
        :type value: "area_t"
        :rtype: "area_t"
        """
    
        ...    

    @_clip_area.setter
    def _clip_area(self, value: "area_t"):
        ...    

    @property
    def phy_clip_area(self) -> "area_t":
        """
        :type value: "area_t"
        :rtype: "area_t"
        """
    
        ...    

    @phy_clip_area.setter
    def phy_clip_area(self, value: "area_t"):
        ...    

    @property
    def draw_task_head(self) -> "draw_task_t":
        """
        :type value: "draw_task_t"
        :rtype: "draw_task_t"
        """
    
        ...    

    @draw_task_head.setter
    def draw_task_head(self, value: "draw_task_t"):
        ...    

    @property
    def parent(self) -> "layer_t":
        """
        :type value: "layer_t"
        :rtype: "layer_t"
        """
    
        ...    

    @parent.setter
    def parent(self, value: "layer_t"):
        ...    

    @property
    def next(self) -> "layer_t":
        """
        :type value: "layer_t"
        :rtype: "layer_t"
        """
    
        ...    

    @next.setter
    def next(self, value: "layer_t"):
        ...    

    @property
    def all_tasks_added(self) -> bool:
        """
        :type value: bool
        :rtype: bool
        """
    
        ...    

    @all_tasks_added.setter
    def all_tasks_added(self, value: bool):
        ...    

    @property
    def user_data(self) -> Any:
        """
        :type value: Any
        :rtype: Any
        """
    
        ...    

    @user_data.setter
    def user_data(self, value: Any):
        ...    



class _type_draw_task_t(TypedDict, total=False):
    pass


class draw_task_t(Struct):
    
    def __init__(self, *, kwargs: _type_draw_task_t = dict()):
        ...

    def get_dependent_count(self) -> int:
        """
        Tell how many draw task are waiting to be drawn on the area of t_check . It can be used to determine if a GPU shall combine many draw tasks into one or not. If a lot of tasks are waiting for the current ones it makes sense to draw them one-by-one to not block the dependent tasks' rendering number of tasks depending on t_check 
        

        :returns: number of tasks depending on t_check 
        :rtype: int
        """
        ...

    def get_type(self) -> "draw_task_type_t":
        """
        Get the type of a draw task the draw task type 
        

        :returns: the draw task type 
        :rtype: "draw_task_type_t"
        """
        ...

    def get_draw_dsc(self) -> Any:
        """
        Get the draw descriptor of a draw task a void pointer to the draw descriptor 
        

        :returns: a void pointer to the draw descriptor 
        :rtype: Any
        """
        ...

    def get_area(self, area: "area_t") -> None:
        """
        Get the draw area of a draw task 
        
        :param area: the destination where the draw area will be stored 
        :type area: "area_t"

        :returns: 
        :rtype: None
        """
        ...

    def get_fill_dsc(self) -> "draw_fill_dsc_t":
        """
        Try to get a fill draw descriptor from a draw task. the task's draw descriptor or NULL if the task is not of type LV_DRAW_TASK_TYPE_FILL 
        

        :returns: the task's draw descriptor or NULL if the task is not of type LV_DRAW_TASK_TYPE_FILL 
        :rtype: "draw_fill_dsc_t"
        """
        ...

    def get_border_dsc(self) -> "draw_border_dsc_t":
        """
        Try to get a border draw descriptor from a draw task. the task's draw descriptor or NULL if the task is not of type LV_DRAW_TASK_TYPE_BORDER 
        

        :returns: the task's draw descriptor or NULL if the task is not of type LV_DRAW_TASK_TYPE_BORDER 
        :rtype: "draw_border_dsc_t"
        """
        ...

    def get_box_shadow_dsc(self) -> "draw_box_shadow_dsc_t":
        """
        Try to get a box shadow draw descriptor from a draw task. the task's draw descriptor or NULL if the task is not of type LV_DRAW_TASK_TYPE_BOX_SHADOW 
        

        :returns: the task's draw descriptor or NULL if the task is not of type LV_DRAW_TASK_TYPE_BOX_SHADOW 
        :rtype: "draw_box_shadow_dsc_t"
        """
        ...

    def get_label_dsc(self) -> "draw_label_dsc_t":
        """
        Try to get a label draw descriptor from a draw task. the task's draw descriptor or NULL if the task is not of type LV_DRAW_TASK_TYPE_LABEL 
        

        :returns: the task's draw descriptor or NULL if the task is not of type LV_DRAW_TASK_TYPE_LABEL 
        :rtype: "draw_label_dsc_t"
        """
        ...

    def get_image_dsc(self) -> "draw_image_dsc_t":
        """
        Try to get an image draw descriptor from a draw task. the task's draw descriptor or NULL if the task is not of type LV_DRAW_TASK_TYPE_IMAGE 
        

        :returns: the task's draw descriptor or NULL if the task is not of type LV_DRAW_TASK_TYPE_IMAGE 
        :rtype: "draw_image_dsc_t"
        """
        ...

    def get_line_dsc(self) -> "draw_line_dsc_t":
        """
        Try to get a line draw descriptor from a draw task. the task's draw descriptor or NULL if the task is not of type LV_DRAW_TASK_TYPE_LINE 
        

        :returns: the task's draw descriptor or NULL if the task is not of type LV_DRAW_TASK_TYPE_LINE 
        :rtype: "draw_line_dsc_t"
        """
        ...

    def get_arc_dsc(self) -> "draw_arc_dsc_t":
        """
        Try to get an arc draw descriptor from a draw task. the task's draw descriptor or NULL if the task is not of type LV_DRAW_TASK_TYPE_ARC 
        

        :returns: the task's draw descriptor or NULL if the task is not of type LV_DRAW_TASK_TYPE_ARC 
        :rtype: "draw_arc_dsc_t"
        """
        ...

    def get_triangle_dsc(self) -> "draw_triangle_dsc_t":
        """
        Try to get a triangle draw descriptor from a draw task. the task's draw descriptor or NULL if the task is not of type LV_DRAW_TASK_TYPE_TRIANGLE 
        

        :returns: the task's draw descriptor or NULL if the task is not of type LV_DRAW_TASK_TYPE_TRIANGLE 
        :rtype: "draw_triangle_dsc_t"
        """
        ...



class _type_draw_label_dsc_t(TypedDict, total=False):
    base: "draw_dsc_base_t"
    text: str
    font: "font_t"
    sel_start: int
    sel_end: int
    color: "color_t"
    sel_color: "color_t"
    sel_bg_color: "color_t"
    line_space: int
    letter_space: int
    ofs_x: int
    ofs_y: int
    opa: "opa_t"
    bidi_dir: "base_dir_t"
    align: "text_align_t"
    flag: "text_flag_t"
    decor: "text_decor_t"
    blend_mode: "blend_mode_t"
    text_local: int
    hint: "draw_label_hint_t"


class draw_label_dsc_t(Struct):

    __SIZE__: ClassVar[int] = ...
    
    def __init__(self, *, kwargs: _type_draw_label_dsc_t = dict()):
        ...

    @property
    def base(self) -> "draw_dsc_base_t":
        """
        :type value: "draw_dsc_base_t"
        :rtype: "draw_dsc_base_t"
        """
    
        ...    

    @base.setter
    def base(self, value: "draw_dsc_base_t"):
        ...    

    @property
    def text(self) -> str:
        """
        :type value: str
        :rtype: str
        """
    
        ...    

    @text.setter
    def text(self, value: str):
        ...    

    @property
    def font(self) -> "font_t":
        """
        :type value: "font_t"
        :rtype: "font_t"
        """
    
        ...    

    @font.setter
    def font(self, value: "font_t"):
        ...    

    @property
    def sel_start(self) -> int:
        """
        :type value: int
        :rtype: int
        """
    
        ...    

    @sel_start.setter
    def sel_start(self, value: int):
        ...    

    @property
    def sel_end(self) -> int:
        """
        :type value: int
        :rtype: int
        """
    
        ...    

    @sel_end.setter
    def sel_end(self, value: int):
        ...    

    @property
    def color(self) -> "color_t":
        """
        :type value: "color_t"
        :rtype: "color_t"
        """
    
        ...    

    @color.setter
    def color(self, value: "color_t"):
        ...    

    @property
    def sel_color(self) -> "color_t":
        """
        :type value: "color_t"
        :rtype: "color_t"
        """
    
        ...    

    @sel_color.setter
    def sel_color(self, value: "color_t"):
        ...    

    @property
    def sel_bg_color(self) -> "color_t":
        """
        :type value: "color_t"
        :rtype: "color_t"
        """
    
        ...    

    @sel_bg_color.setter
    def sel_bg_color(self, value: "color_t"):
        ...    

    @property
    def line_space(self) -> int:
        """
        :type value: int
        :rtype: int
        """
    
        ...    

    @line_space.setter
    def line_space(self, value: int):
        ...    

    @property
    def letter_space(self) -> int:
        """
        :type value: int
        :rtype: int
        """
    
        ...    

    @letter_space.setter
    def letter_space(self, value: int):
        ...    

    @property
    def ofs_x(self) -> int:
        """
        :type value: int
        :rtype: int
        """
    
        ...    

    @ofs_x.setter
    def ofs_x(self, value: int):
        ...    

    @property
    def ofs_y(self) -> int:
        """
        :type value: int
        :rtype: int
        """
    
        ...    

    @ofs_y.setter
    def ofs_y(self, value: int):
        ...    

    @property
    def opa(self) -> "opa_t":
        """
        :type value: "opa_t"
        :rtype: "opa_t"
        """
    
        ...    

    @opa.setter
    def opa(self, value: "opa_t"):
        ...    

    @property
    def bidi_dir(self) -> "base_dir_t":
        """
        :type value: "base_dir_t"
        :rtype: "base_dir_t"
        """
    
        ...    

    @bidi_dir.setter
    def bidi_dir(self, value: "base_dir_t"):
        ...    

    @property
    def align(self) -> "text_align_t":
        """
        :type value: "text_align_t"
        :rtype: "text_align_t"
        """
    
        ...    

    @align.setter
    def align(self, value: "text_align_t"):
        ...    

    @property
    def flag(self) -> "text_flag_t":
        """
        :type value: "text_flag_t"
        :rtype: "text_flag_t"
        """
    
        ...    

    @flag.setter
    def flag(self, value: "text_flag_t"):
        ...    

    @property
    def decor(self) -> "text_decor_t":
        """
        :type value: "text_decor_t"
        :rtype: "text_decor_t"
        """
    
        ...    

    @decor.setter
    def decor(self, value: "text_decor_t"):
        ...    

    @property
    def blend_mode(self) -> "blend_mode_t":
        """
        :type value: "blend_mode_t"
        :rtype: "blend_mode_t"
        """
    
        ...    

    @blend_mode.setter
    def blend_mode(self, value: "blend_mode_t"):
        ...    

    @property
    def text_local(self) -> int:
        """
        :type value: int
        :rtype: int
        """
    
        ...    

    @text_local.setter
    def text_local(self, value: int):
        ...    

    @property
    def hint(self) -> "draw_label_hint_t":
        """
        :type value: "draw_label_hint_t"
        :rtype: "draw_label_hint_t"
        """
    
        ...    

    @hint.setter
    def hint(self, value: "draw_label_hint_t"):
        ...    


    def init(self) -> None:
        """
        Initialize a label draw descriptor 
        

        :returns: 
        :rtype: None
        """
        ...



class _type_draw_label_hint_t(TypedDict, total=False):
    pass


class draw_label_hint_t(Struct):
    
    def __init__(self, *, kwargs: _type_draw_label_hint_t = dict()):
        ...


class _type_draw_image_dsc_t(TypedDict, total=False):
    base: "draw_dsc_base_t"
    src: Any
    header: "image"
    rotation: int
    scale_x: int
    scale_y: int
    skew_x: int
    skew_y: int
    pivot: "point_t"
    recolor: "color_t"
    recolor_opa: "opa_t"
    opa: "opa_t"
    blend_mode: "blend_mode_t"
    antialias: int
    tile: int
    sup: "draw_image_sup_t"
    image_area: "area_t"
    clip_radius: int
    bitmap_mask_src: "image"


class draw_image_dsc_t(Struct):

    __SIZE__: ClassVar[int] = ...
    
    def __init__(self, *, kwargs: _type_draw_image_dsc_t = dict()):
        ...

    @property
    def base(self) -> "draw_dsc_base_t":
        """
        :type value: "draw_dsc_base_t"
        :rtype: "draw_dsc_base_t"
        """
    
        ...    

    @base.setter
    def base(self, value: "draw_dsc_base_t"):
        ...    

    @property
    def src(self) -> Any:
        """
        :type value: Any
        :rtype: Any
        """
    
        ...    

    @src.setter
    def src(self, value: Any):
        ...    

    @property
    def header(self) -> "image":
        """
        :type value: "image"
        :rtype: "image"
        """
    
        ...    

    @header.setter
    def header(self, value: "image"):
        ...    

    @property
    def rotation(self) -> int:
        """
        :type value: int
        :rtype: int
        """
    
        ...    

    @rotation.setter
    def rotation(self, value: int):
        ...    

    @property
    def scale_x(self) -> int:
        """
        :type value: int
        :rtype: int
        """
    
        ...    

    @scale_x.setter
    def scale_x(self, value: int):
        ...    

    @property
    def scale_y(self) -> int:
        """
        :type value: int
        :rtype: int
        """
    
        ...    

    @scale_y.setter
    def scale_y(self, value: int):
        ...    

    @property
    def skew_x(self) -> int:
        """
        :type value: int
        :rtype: int
        """
    
        ...    

    @skew_x.setter
    def skew_x(self, value: int):
        ...    

    @property
    def skew_y(self) -> int:
        """
        :type value: int
        :rtype: int
        """
    
        ...    

    @skew_y.setter
    def skew_y(self, value: int):
        ...    

    @property
    def pivot(self) -> "point_t":
        """
        :type value: "point_t"
        :rtype: "point_t"
        """
    
        ...    

    @pivot.setter
    def pivot(self, value: "point_t"):
        ...    

    @property
    def recolor(self) -> "color_t":
        """
        :type value: "color_t"
        :rtype: "color_t"
        """
    
        ...    

    @recolor.setter
    def recolor(self, value: "color_t"):
        ...    

    @property
    def recolor_opa(self) -> "opa_t":
        """
        :type value: "opa_t"
        :rtype: "opa_t"
        """
    
        ...    

    @recolor_opa.setter
    def recolor_opa(self, value: "opa_t"):
        ...    

    @property
    def opa(self) -> "opa_t":
        """
        :type value: "opa_t"
        :rtype: "opa_t"
        """
    
        ...    

    @opa.setter
    def opa(self, value: "opa_t"):
        ...    

    @property
    def blend_mode(self) -> "blend_mode_t":
        """
        :type value: "blend_mode_t"
        :rtype: "blend_mode_t"
        """
    
        ...    

    @blend_mode.setter
    def blend_mode(self, value: "blend_mode_t"):
        ...    

    @property
    def antialias(self) -> int:
        """
        :type value: int
        :rtype: int
        """
    
        ...    

    @antialias.setter
    def antialias(self, value: int):
        ...    

    @property
    def tile(self) -> int:
        """
        :type value: int
        :rtype: int
        """
    
        ...    

    @tile.setter
    def tile(self, value: int):
        ...    

    @property
    def sup(self) -> "draw_image_sup_t":
        """
        :type value: "draw_image_sup_t"
        :rtype: "draw_image_sup_t"
        """
    
        ...    

    @sup.setter
    def sup(self, value: "draw_image_sup_t"):
        ...    

    @property
    def image_area(self) -> "area_t":
        """
        :type value: "area_t"
        :rtype: "area_t"
        """
    
        ...    

    @image_area.setter
    def image_area(self, value: "area_t"):
        ...    

    @property
    def clip_radius(self) -> int:
        """
        :type value: int
        :rtype: int
        """
    
        ...    

    @clip_radius.setter
    def clip_radius(self, value: int):
        ...    

    @property
    def bitmap_mask_src(self) -> "image":
        """
        :type value: "image"
        :rtype: "image"
        """
    
        ...    

    @bitmap_mask_src.setter
    def bitmap_mask_src(self, value: "image"):
        ...    


    def init(self) -> None:
        """
        Initialize an image draw descriptor. 
        

        :returns: 
        :rtype: None
        """
        ...



class _type_draw_image_sup_t(TypedDict, total=False):
    pass


class draw_image_sup_t(Struct):
    
    def __init__(self, *, kwargs: _type_draw_image_sup_t = dict()):
        ...


class _type_draw_line_dsc_t(TypedDict, total=False):
    base: "draw_dsc_base_t"
    p1: "point_precise_t"
    p2: "point_precise_t"
    color: "color_t"
    width: int
    dash_width: int
    dash_gap: int
    opa: "opa_t"
    blend_mode: "blend_mode_t"
    round_start: int
    round_end: int
    raw_end: int


class draw_line_dsc_t(Struct):

    __SIZE__: ClassVar[int] = ...
    
    def __init__(self, *, kwargs: _type_draw_line_dsc_t = dict()):
        ...

    @property
    def base(self) -> "draw_dsc_base_t":
        """
        :type value: "draw_dsc_base_t"
        :rtype: "draw_dsc_base_t"
        """
    
        ...    

    @base.setter
    def base(self, value: "draw_dsc_base_t"):
        ...    

    @property
    def p1(self) -> "point_precise_t":
        """
        :type value: "point_precise_t"
        :rtype: "point_precise_t"
        """
    
        ...    

    @p1.setter
    def p1(self, value: "point_precise_t"):
        ...    

    @property
    def p2(self) -> "point_precise_t":
        """
        :type value: "point_precise_t"
        :rtype: "point_precise_t"
        """
    
        ...    

    @p2.setter
    def p2(self, value: "point_precise_t"):
        ...    

    @property
    def color(self) -> "color_t":
        """
        :type value: "color_t"
        :rtype: "color_t"
        """
    
        ...    

    @color.setter
    def color(self, value: "color_t"):
        ...    

    @property
    def width(self) -> int:
        """
        :type value: int
        :rtype: int
        """
    
        ...    

    @width.setter
    def width(self, value: int):
        ...    

    @property
    def dash_width(self) -> int:
        """
        :type value: int
        :rtype: int
        """
    
        ...    

    @dash_width.setter
    def dash_width(self, value: int):
        ...    

    @property
    def dash_gap(self) -> int:
        """
        :type value: int
        :rtype: int
        """
    
        ...    

    @dash_gap.setter
    def dash_gap(self, value: int):
        ...    

    @property
    def opa(self) -> "opa_t":
        """
        :type value: "opa_t"
        :rtype: "opa_t"
        """
    
        ...    

    @opa.setter
    def opa(self, value: "opa_t"):
        ...    

    @property
    def blend_mode(self) -> "blend_mode_t":
        """
        :type value: "blend_mode_t"
        :rtype: "blend_mode_t"
        """
    
        ...    

    @blend_mode.setter
    def blend_mode(self, value: "blend_mode_t"):
        ...    

    @property
    def round_start(self) -> int:
        """
        :type value: int
        :rtype: int
        """
    
        ...    

    @round_start.setter
    def round_start(self, value: int):
        ...    

    @property
    def round_end(self) -> int:
        """
        :type value: int
        :rtype: int
        """
    
        ...    

    @round_end.setter
    def round_end(self, value: int):
        ...    

    @property
    def raw_end(self) -> int:
        """
        :type value: int
        :rtype: int
        """
    
        ...    

    @raw_end.setter
    def raw_end(self, value: int):
        ...    


    def init(self) -> None:
        """
        Initialize a line draw descriptor 
        

        :returns: 
        :rtype: None
        """
        ...



class _type_point_precise_t(TypedDict, total=False):
    x: "value_precise_t"
    y: "value_precise_t"


class point_precise_t(Struct):

    __SIZE__: ClassVar[int] = ...
    
    def __init__(self, *, kwargs: _type_point_precise_t = dict()):
        ...

    @property
    def x(self) -> "value_precise_t":
        """
        :type value: "value_precise_t"
        :rtype: "value_precise_t"
        """
    
        ...    

    @x.setter
    def x(self, value: "value_precise_t"):
        ...    

    @property
    def y(self) -> "value_precise_t":
        """
        :type value: "value_precise_t"
        :rtype: "value_precise_t"
        """
    
        ...    

    @y.setter
    def y(self, value: "value_precise_t"):
        ...    


    def from_precise(self) -> "point_t":
        """

        :returns: 
        :rtype: "point_t"
        """
        ...

    def set(self, x: "value_precise_t", y: "value_precise_t") -> None:
        """
        :param x: 
        :type x: "value_precise_t"
        :param y: 
        :type y: "value_precise_t"

        :returns: 
        :rtype: None
        """
        ...

    def swap(self, p2: "point_precise_t") -> None:
        """
        :param p2: 
        :type p2: "point_precise_t"

        :returns: 
        :rtype: None
        """
        ...



class _type_draw_arc_dsc_t(TypedDict, total=False):
    base: "draw_dsc_base_t"
    color: "color_t"
    width: int
    start_angle: "value_precise_t"
    end_angle: "value_precise_t"
    center: "point_t"
    radius: int
    img_src: Any
    opa: "opa_t"
    rounded: int


class draw_arc_dsc_t(Struct):

    __SIZE__: ClassVar[int] = ...
    
    def __init__(self, *, kwargs: _type_draw_arc_dsc_t = dict()):
        ...

    @property
    def base(self) -> "draw_dsc_base_t":
        """
        :type value: "draw_dsc_base_t"
        :rtype: "draw_dsc_base_t"
        """
    
        ...    

    @base.setter
    def base(self, value: "draw_dsc_base_t"):
        ...    

    @property
    def color(self) -> "color_t":
        """
        :type value: "color_t"
        :rtype: "color_t"
        """
    
        ...    

    @color.setter
    def color(self, value: "color_t"):
        ...    

    @property
    def width(self) -> int:
        """
        :type value: int
        :rtype: int
        """
    
        ...    

    @width.setter
    def width(self, value: int):
        ...    

    @property
    def start_angle(self) -> "value_precise_t":
        """
        :type value: "value_precise_t"
        :rtype: "value_precise_t"
        """
    
        ...    

    @start_angle.setter
    def start_angle(self, value: "value_precise_t"):
        ...    

    @property
    def end_angle(self) -> "value_precise_t":
        """
        :type value: "value_precise_t"
        :rtype: "value_precise_t"
        """
    
        ...    

    @end_angle.setter
    def end_angle(self, value: "value_precise_t"):
        ...    

    @property
    def center(self) -> "point_t":
        """
        :type value: "point_t"
        :rtype: "point_t"
        """
    
        ...    

    @center.setter
    def center(self, value: "point_t"):
        ...    

    @property
    def radius(self) -> int:
        """
        :type value: int
        :rtype: int
        """
    
        ...    

    @radius.setter
    def radius(self, value: int):
        ...    

    @property
    def img_src(self) -> Any:
        """
        :type value: Any
        :rtype: Any
        """
    
        ...    

    @img_src.setter
    def img_src(self, value: Any):
        ...    

    @property
    def opa(self) -> "opa_t":
        """
        :type value: "opa_t"
        :rtype: "opa_t"
        """
    
        ...    

    @opa.setter
    def opa(self, value: "opa_t"):
        ...    

    @property
    def rounded(self) -> int:
        """
        :type value: int
        :rtype: int
        """
    
        ...    

    @rounded.setter
    def rounded(self, value: int):
        ...    


    def init(self) -> None:
        """
        Initialize an arc draw descriptor. 
        

        :returns: 
        :rtype: None
        """
        ...



class _type_event_t(TypedDict, total=False):
    pass


class event_t(Struct):
    
    def __init__(self, *, kwargs: _type_event_t = dict()):
        ...

    def get_target(self) -> Any:
        """
        Get the object originally targeted by the event. It's the same even if the event is bubbled. the target of the event_code 
        

        :returns: the target of the event_code 
        :rtype: Any
        """
        ...

    def get_current_target(self) -> Any:
        """
        Get the current target of the event. It's the object which event handler being called. If the event is not bubbled it's the same as "normal" target. pointer to the current target of the event_code 
        

        :returns: pointer to the current target of the event_code 
        :rtype: Any
        """
        ...

    def get_code(self) -> "event_code_t":
        """
        Get the event code of an event the event code. (E.g. LV_EVENT_CLICKED , LV_EVENT_FOCUSED , etc) 
        

        :returns: the event code. (E.g. LV_EVENT_CLICKED , LV_EVENT_FOCUSED , etc) 
        :rtype: "event_code_t"
        """
        ...

    def get_param(self) -> Any:
        """
        Get the parameter passed when the event was sent pointer to the parameter 
        

        :returns: pointer to the parameter 
        :rtype: Any
        """
        ...

    def get_user_data(self) -> Any:
        """
        Get the user_data passed when the event was registered on the object pointer to the user_data 
        

        :returns: pointer to the user_data 
        :rtype: Any
        """
        ...

    def stop_bubbling(self) -> None:
        """
        Stop the event from bubbling. This is only valid when called in the middle of an event processing chain. 
        

        :returns: 
        :rtype: None
        """
        ...

    def stop_processing(self) -> None:
        """
        Stop processing this event. This is only valid when called in the middle of an event processing chain. 
        

        :returns: 
        :rtype: None
        """
        ...

    def get_current_target_obj(self) -> "obj":
        """
        Get the current target of the event. It's the object which event handler being called. If the event is not bubbled it's the same as "original" target. the target of the event_code 
        

        :returns: the target of the event_code 
        :rtype: "obj"
        """
        ...

    def get_target_obj(self) -> "obj":
        """
        Get the object originally targeted by the event. It's the same even if the event is bubbled. pointer to the original target of the event_code 
        

        :returns: pointer to the original target of the event_code 
        :rtype: "obj"
        """
        ...

    def get_indev(self) -> "indev_t":
        """
        Get the input device passed as parameter to indev related events. the indev that triggered the event or NULL if called on a not indev related event 
        

        :returns: the indev that triggered the event or NULL if called on a not indev related event 
        :rtype: "indev_t"
        """
        ...

    def get_layer(self) -> "layer_t":
        """
        Get the draw context which should be the first parameter of the draw functions. Namely: LV_EVENT_DRAW_MAIN/POST , LV_EVENT_DRAW_MAIN/POST_BEGIN , LV_EVENT_DRAW_MAIN/POST_END  pointer to a draw context or NULL if called on an unrelated event 
        

        :returns: pointer to a draw context or NULL if called on an unrelated event 
        :rtype: "layer_t"
        """
        ...

    def get_old_size(self) -> "area_t":
        """
        Get the old area of the object before its size was changed. Can be used in LV_EVENT_SIZE_CHANGED  the old absolute area of the object or NULL if called on an unrelated event 
        

        :returns: the old absolute area of the object or NULL if called on an unrelated event 
        :rtype: "area_t"
        """
        ...

    def get_key(self) -> int:
        """
        Get the key passed as parameter to an event. Can be used in LV_EVENT_KEY  the triggering key or NULL if called on an unrelated event 
        

        :returns: the triggering key or NULL if called on an unrelated event 
        :rtype: int
        """
        ...

    def get_rotary_diff(self) -> int:
        """
        Get the signed rotary encoder diff. passed as parameter to an event. Can be used in LV_EVENT_ROTARY  the triggering key or NULL if called on an unrelated event 
        

        :returns: the triggering key or NULL if called on an unrelated event 
        :rtype: int
        """
        ...

    def get_scroll_anim(self) -> "anim_t":
        """
        Get the animation descriptor of a scrolling. Can be used in LV_EVENT_SCROLL_BEGIN  the animation that will scroll the object. (can be modified as required) 
        

        :returns: the animation that will scroll the object. (can be modified as required) 
        :rtype: "anim_t"
        """
        ...

    def set_ext_draw_size(self, size: int) -> None:
        """
        Set the new extra draw size. Can be used in LV_EVENT_REFR_EXT_DRAW_SIZE 
        
        :param size: The new extra draw size 
        :type size: int

        :returns: 
        :rtype: None
        """
        ...

    def get_self_size_info(self) -> "point_t":
        """
        Get a pointer to an :ref:`lv_point_t` variable in which the self size should be saved (width in point->x and height point->y ). Can be used in LV_EVENT_GET_SELF_SIZE  pointer to :ref:`lv_point_t` or NULL if called on an unrelated event 
        

        :returns: pointer to :ref:`lv_point_t` or NULL if called on an unrelated event 
        :rtype: "point_t"
        """
        ...

    def get_hit_test_info(self) -> "hit_test_info_t":
        """
        Get a pointer to an :ref:`lv_hit_test_info_t` variable in which the hit test result should be saved. Can be used in LV_EVENT_HIT_TEST  pointer to :ref:`lv_hit_test_info_t` or NULL if called on an unrelated event 
        

        :returns: pointer to :ref:`lv_hit_test_info_t` or NULL if called on an unrelated event 
        :rtype: "hit_test_info_t"
        """
        ...

    def get_cover_area(self) -> "area_t":
        """
        Get a pointer to an area which should be examined whether the object fully covers it or not. Can be used in LV_EVENT_HIT_TEST  an area with absolute coordinates to check 
        

        :returns: an area with absolute coordinates to check 
        :rtype: "area_t"
        """
        ...

    def set_cover_res(self, res: cover_res_t) -> None:
        """
        Set the result of cover checking. Can be used in LV_EVENT_COVER_CHECK 
        
        :param res: an element of :ref:`lv_cover_check_info_t` 
        :type res: cover_res_t

        :returns: 
        :rtype: None
        """
        ...

    def get_draw_task(self) -> "draw_task_t":
        """
        Get the draw task which was just added. Can be used in LV_EVENT_DRAW_TASK_ADDED event  the added draw task 
        

        :returns: the added draw task 
        :rtype: "draw_task_t"
        """
        ...



class _type_event_dsc_t(TypedDict, total=False):
    pass


class event_dsc_t(Struct):
    
    def __init__(self, *, kwargs: _type_event_dsc_t = dict()):
        ...

    def get_cb(self) -> "event_cb_t":
        """

        :returns: 
        :rtype: "event_cb_t"
        """
        ...

    def get_user_data(self) -> Any:
        """

        :returns: 
        :rtype: Any
        """
        ...



class _type_group_t(TypedDict, total=False):
    pass


class group_t(Struct):
    
    def __init__(self, *, kwargs: _type_group_t = dict()):
        ...

    def delete(self) -> None:
        """
        Delete a group object 
        

        :returns: 
        :rtype: None
        """
        ...

    def set_default(self) -> None:
        """
        Set a default group. New object are added to this group if it's enabled in their class with add_to_def_group = true 
        

        :returns: 
        :rtype: None
        """
        ...

    def add_obj(self, obj: "obj") -> None:
        """
        Add an object to a group 
        
        :param obj: pointer to an object to add 
        :type obj: "obj"

        :returns: 
        :rtype: None
        """
        ...

    def remove_all_objs(self) -> None:
        """
        Remove all objects from a group 
        

        :returns: 
        :rtype: None
        """
        ...

    def focus_next(self) -> None:
        """
        Focus the next object in a group (defocus the current) 
        

        :returns: 
        :rtype: None
        """
        ...

    def focus_prev(self) -> None:
        """
        Focus the previous object in a group (defocus the current) 
        

        :returns: 
        :rtype: None
        """
        ...

    def focus_freeze(self, en: bool) -> None:
        """
        Do not let to change the focus from the current object 
        
        :param en: true: freeze, false: release freezing (normal mode) 
        :type en: bool

        :returns: 
        :rtype: None
        """
        ...

    def send_data(self, c: int) -> "result_t":
        """
        Send a control character to the focuses object of a group result of focused object in group. 
        
        :param c: a character (use LV_KEY_.. to navigate) 
        :type c: int

        :returns: result of focused object in group. 
        :rtype: "result_t"
        """
        ...

    def set_focus_cb(self, focus_cb: Callable[["group_t"], None]) -> None:
        """
        Set a function for a group which will be called when a new object is focused 
        
        :param focus_cb: the call back function or NULL if unused 
        :type focus_cb: Callable[["group_t"], None]

        :returns: 
        :rtype: None
        """
        ...

    def set_edge_cb(self, edge_cb: Callable[["group_t", bool], None]) -> None:
        """
        Set a function for a group which will be called when a focus edge is reached 
        
        :param edge_cb: the call back function or NULL if unused 
        :type edge_cb: Callable[["group_t", bool], None]

        :returns: 
        :rtype: None
        """
        ...

    def set_refocus_policy(self, policy: group_refocus_policy_t) -> None:
        """
        Set whether the next or previous item in a group is focused if the currently focused obj is deleted. 
        
        :param policy: new refocus policy enum 
        :type policy: group_refocus_policy_t

        :returns: 
        :rtype: None
        """
        ...

    def set_editing(self, en: bool) -> None:
        """
        Manually set the current mode (edit or navigate). 
        
        :param en: true: edit mode; false: navigate mode 
        :type en: bool

        :returns: 
        :rtype: None
        """
        ...

    def set_wrap(self, en: bool) -> None:
        """
        Set whether focus next/prev will allow wrapping from first->last or last->first object. 
        
        :param en: true: wrapping enabled; false: wrapping disabled 
        :type en: bool

        :returns: 
        :rtype: None
        """
        ...

    def get_focused(self) -> "obj":
        """
        Get the focused object or NULL if there isn't one pointer to the focused object 
        

        :returns: pointer to the focused object 
        :rtype: "obj"
        """
        ...

    def get_focus_cb(self) -> "group_focus_cb_t":
        """
        Get the focus callback function of a group the call back function or NULL if not set 
        

        :returns: the call back function or NULL if not set 
        :rtype: "group_focus_cb_t"
        """
        ...

    def get_edge_cb(self) -> "group_edge_cb_t":
        """
        Get the edge callback function of a group the call back function or NULL if not set 
        

        :returns: the call back function or NULL if not set 
        :rtype: "group_edge_cb_t"
        """
        ...

    def get_editing(self) -> bool:
        """
        Get the current mode (edit or navigate). true: edit mode; false: navigate mode 
        

        :returns: true: edit mode; false: navigate mode 
        :rtype: bool
        """
        ...

    def get_wrap(self) -> bool:
        """
        Get whether focus next/prev will allow wrapping from first->last or last->first object. 
        

        :returns: 
        :rtype: bool
        """
        ...

    def get_obj_count(self) -> int:
        """
        Get the number of object in the group number of objects in the group 
        

        :returns: number of objects in the group 
        :rtype: int
        """
        ...

    def get_obj_by_index(self, index: int) -> "obj":
        """
        Get the nth object within a group pointer to the object 
        
        :param index: index of object within the group 
        :type index: int

        :returns: pointer to the object 
        :rtype: "obj"
        """
        ...



class _type_subject_t(TypedDict, total=False):
    subs_ll: "ll_t"
    type: int
    size: int
    value: "subject_value_t"
    prev_value: "subject_value_t"
    notify_restart_query: int
    user_data: Any


class subject_t(Struct):

    __SIZE__: ClassVar[int] = ...
    
    def __init__(self, *, kwargs: _type_subject_t = dict()):
        ...

    @property
    def subs_ll(self) -> "ll_t":
        """
        :type value: "ll_t"
        :rtype: "ll_t"
        """
    
        ...    

    @subs_ll.setter
    def subs_ll(self, value: "ll_t"):
        ...    

    @property
    def type(self) -> int:
        """
        :type value: int
        :rtype: int
        """
    
        ...    

    @type.setter
    def type(self, value: int):
        ...    

    @property
    def size(self) -> int:
        """
        :type value: int
        :rtype: int
        """
    
        ...    

    @size.setter
    def size(self, value: int):
        ...    

    @property
    def value(self) -> "subject_value_t":
        """
        :type value: "subject_value_t"
        :rtype: "subject_value_t"
        """
    
        ...    

    @value.setter
    def value(self, value: "subject_value_t"):
        ...    

    @property
    def prev_value(self) -> "subject_value_t":
        """
        :type value: "subject_value_t"
        :rtype: "subject_value_t"
        """
    
        ...    

    @prev_value.setter
    def prev_value(self, value: "subject_value_t"):
        ...    

    @property
    def notify_restart_query(self) -> int:
        """
        :type value: int
        :rtype: int
        """
    
        ...    

    @notify_restart_query.setter
    def notify_restart_query(self, value: int):
        ...    

    @property
    def user_data(self) -> Any:
        """
        :type value: Any
        :rtype: Any
        """
    
        ...    

    @user_data.setter
    def user_data(self, value: Any):
        ...    


    def init_int(self, value: int) -> None:
        """
        Initialize an integer type subject 
        
        :param value: initial value 
        :type value: int

        :returns: 
        :rtype: None
        """
        ...

    def set_int(self, value: int) -> None:
        """
        Set the value of an integer subject. It will notify all the observers as well. 
        
        :param value: the new value 
        :type value: int

        :returns: 
        :rtype: None
        """
        ...

    def get_int(self) -> int:
        """
        Get the current value of an integer subject the current value 
        

        :returns: the current value 
        :rtype: int
        """
        ...

    def get_previous_int(self) -> int:
        """
        Get the previous value of an integer subject the current value 
        

        :returns: the current value 
        :rtype: int
        """
        ...

    def init_string(self, buf: str, prev_buf: str, size: int, value: str) -> None:
        """
        Initialize a string type subject the string subject stores the whole string, not only a pointer 
        
        :param buf: pointer to a buffer to store the string 
        :type buf: str
        :param prev_buf: pointer to a buffer to store the previous string, can be NULL if not used 
        :type prev_buf: str
        :param size: size of the buffer 
        :type size: int
        :param value: initial value as a string, e.g. "hello" 
        :type value: str

        :returns: 
        :rtype: None
        """
        ...

    def copy_string(self, buf: str) -> None:
        """
        Copy a string to a subject. It will notify all the observers as well. 
        
        :param buf: the new string 
        :type buf: str

        :returns: 
        :rtype: None
        """
        ...

    def get_string(self) -> str:
        """
        Get the current value of an string subject pointer to the buffer containing the current value 
        

        :returns: pointer to the buffer containing the current value 
        :rtype: str
        """
        ...

    def get_previous_string(self) -> str:
        """
        Get the previous value of an string subject pointer to the buffer containing the current value  NULL will be returned if NULL was passed in :ref:`lv_subject_init_string()` as prev_buf 
        

        :returns: pointer to the buffer containing the current value 
        :rtype: str
        """
        ...

    def init_pointer(self, value: Any) -> None:
        """
        Initialize an pointer type subject 
        
        :param value: initial value 
        :type value: Any

        :returns: 
        :rtype: None
        """
        ...

    def set_pointer(self, value: Any) -> None:
        """
        Set the value of a pointer subject. It will notify all the observers as well. 
        
        :param value: new value 
        :type value: Any

        :returns: 
        :rtype: None
        """
        ...

    def get_pointer(self) -> Any:
        """
        Get the current value of a pointer subject current value 
        

        :returns: current value 
        :rtype: Any
        """
        ...

    def get_previous_pointer(self) -> Any:
        """
        Get the previous value of a pointer subject current value 
        

        :returns: current value 
        :rtype: Any
        """
        ...

    def init_color(self, color: "color_t") -> None:
        """
        Initialize an color type subject 
        
        :param color: initial value 
        :type color: "color_t"

        :returns: 
        :rtype: None
        """
        ...

    def set_color(self, color: "color_t") -> None:
        """
        Set the value of a color subject. It will notify all the observers as well. 
        
        :param color: new value 
        :type color: "color_t"

        :returns: 
        :rtype: None
        """
        ...

    def get_color(self) -> "color_t":
        """
        Get the current value of a color subject current value 
        

        :returns: current value 
        :rtype: "color_t"
        """
        ...

    def get_previous_color(self) -> "color_t":
        """
        Get the previous value of a color subject current value 
        

        :returns: current value 
        :rtype: "color_t"
        """
        ...

    def init_group(self, list: "subject_t", list_len: int) -> None:
        """
        Initialize a subject group 
        
        :param list: list of other subject addresses, any of these changes subject will be notified 
        :type list: "subject_t"
        :param list_len: number of elements in list 
        :type list_len: int

        :returns: 
        :rtype: None
        """
        ...

    def deinit(self) -> None:
        """
        Remove all the observers from a subject and free all allocated memories in it objects added with lv_subject_add_observer_obj should be already deleted or removed manually. 
        

        :returns: 
        :rtype: None
        """
        ...

    def get_group_element(self, index: int) -> "subject_t":
        """
        Get an element from the subject group's list pointer a subject from the list, or NULL if the index is out of bounds 
        
        :param index: index of the element to get 
        :type index: int

        :returns: pointer a subject from the list, or NULL if the index is out of bounds 
        :rtype: "subject_t"
        """
        ...

    def add_observer(self, observer_cb: Callable[["observer_t", "subject_t"], None], subject: "subject_t") -> "observer_t":
        """
        Add an observer to a subject. When the subject changes observer_cb will be called. pointer to the created observer 
        
        :param observer_cb: callback to call 
        :type observer_cb: Callable[["observer_t", "subject_t"], None]
        :param subject: optional user data 
        :type subject: "subject_t"

        :returns: pointer to the created observer 
        :rtype: "observer_t"
        """
        ...

    def add_observer_obj(self, observer_cb: Callable[["observer_t", "subject_t"], None], obj: "obj", subject: "subject_t") -> "observer_t":
        """
        Add an observer to a subject for an object. When the object is deleted, it will be removed from the subject automatically. pointer to the created observer 
        
        :param observer_cb: callback to call 
        :type observer_cb: Callable[["observer_t", "subject_t"], None]
        :param obj: pointer to an object 
        :type obj: "obj"
        :param subject: optional user data 
        :type subject: "subject_t"

        :returns: pointer to the created observer 
        :rtype: "observer_t"
        """
        ...

    def add_observer_with_target(self, observer_cb: Callable[["observer_t", "subject_t"], None], target: Any, subject: "subject_t") -> "observer_t":
        """
        Add an observer to a subject and also save a target. pointer to the created observer 
        
        :param observer_cb: callback to call 
        :type observer_cb: Callable[["observer_t", "subject_t"], None]
        :param target: pointer to any data 
        :type target: Any
        :param subject: optional user data 
        :type subject: "subject_t"

        :returns: pointer to the created observer 
        :rtype: "observer_t"
        """
        ...

    def notify(self) -> None:
        """
        Notify all observers of subject 
        

        :returns: 
        :rtype: None
        """
        ...



class _type_ll_t(TypedDict, total=False):
    n_size: int
    head: "ll_node_t"
    tail: "ll_node_t"


class ll_t(Struct):

    __SIZE__: ClassVar[int] = ...
    
    def __init__(self, *, kwargs: _type_ll_t = dict()):
        ...

    @property
    def n_size(self) -> int:
        """
        :type value: int
        :rtype: int
        """
    
        ...    

    @n_size.setter
    def n_size(self, value: int):
        ...    

    @property
    def head(self) -> "ll_node_t":
        """
        :type value: "ll_node_t"
        :rtype: "ll_node_t"
        """
    
        ...    

    @head.setter
    def head(self, value: "ll_node_t"):
        ...    

    @property
    def tail(self) -> "ll_node_t":
        """
        :type value: "ll_node_t"
        :rtype: "ll_node_t"
        """
    
        ...    

    @tail.setter
    def tail(self, value: "ll_node_t"):
        ...    


    def init(self, node_size: int) -> None:
        """
        Initialize linked list 
        
        :param node_size: the size of 1 node in bytes 
        :type node_size: int

        :returns: 
        :rtype: None
        """
        ...

    def ins_head(self) -> Any:
        """
        Add a new head to a linked list pointer to the new head 
        

        :returns: pointer to the new head 
        :rtype: Any
        """
        ...

    def ins_prev(self, n_act: Any) -> Any:
        """
        Insert a new node in front of the n_act node pointer to the new node 
        
        :param n_act: pointer a node 
        :type n_act: Any

        :returns: pointer to the new node 
        :rtype: Any
        """
        ...

    def ins_tail(self) -> Any:
        """
        Add a new tail to a linked list pointer to the new tail 
        

        :returns: pointer to the new tail 
        :rtype: Any
        """
        ...

    def remove(self, node_p: Any) -> None:
        """
        Remove the node 'node_p' from 'll_p' linked list. It does not free the memory of node. 
        
        :param node_p: pointer to node in 'll_p' linked list 
        :type node_p: Any

        :returns: 
        :rtype: None
        """
        ...

    def clear(self) -> None:
        """
        Remove and free all elements from a linked list. The list remain valid but become empty. 
        

        :returns: 
        :rtype: None
        """
        ...

    def chg_list(self, ll_new_p: "ll_t", node: Any, head: bool) -> None:
        """
        Move a node to a new linked list 
        
        :param ll_new_p: pointer to the new linked list 
        :type ll_new_p: "ll_t"
        :param node: pointer to a node 
        :type node: Any
        :param head: true: be the head in the new list false be the tail in the new list 
        :type head: bool

        :returns: 
        :rtype: None
        """
        ...

    def get_head(self) -> Any:
        """
        Return with head node of the linked list pointer to the head of 'll_p' 
        

        :returns: pointer to the head of 'll_p' 
        :rtype: Any
        """
        ...

    def get_tail(self) -> Any:
        """
        Return with tail node of the linked list pointer to the tail of 'll_p' 
        

        :returns: pointer to the tail of 'll_p' 
        :rtype: Any
        """
        ...

    def get_next(self, n_act: Any) -> Any:
        """
        Return with the pointer of the next node after 'n_act' pointer to the next node 
        
        :param n_act: pointer a node 
        :type n_act: Any

        :returns: pointer to the next node 
        :rtype: Any
        """
        ...

    def get_prev(self, n_act: Any) -> Any:
        """
        Return with the pointer of the previous node after 'n_act' pointer to the previous node 
        
        :param n_act: pointer a node 
        :type n_act: Any

        :returns: pointer to the previous node 
        :rtype: Any
        """
        ...

    def get_len(self) -> int:
        """
        Return the length of the linked list. length of the linked list 
        

        :returns: length of the linked list 
        :rtype: int
        """
        ...

    def move_before(self, n_act: Any, n_after: Any) -> None:
        """
        Move a node before another node in the same linked list 
        
        :param n_act: pointer to node to move 
        :type n_act: Any
        :param n_after: pointer to a node which should be after n_act 
        :type n_after: Any

        :returns: 
        :rtype: None
        """
        ...

    def is_empty(self) -> bool:
        """
        Check if a linked list is empty true: the linked list is empty; false: not empty 
        

        :returns: true: the linked list is empty; false: not empty 
        :rtype: bool
        """
        ...



class _type_subject_value_t(TypedDict, total=False):
    num: int
    pointer: Any
    color: "color_t"


class subject_value_t(Struct):

    __SIZE__: ClassVar[int] = ...
    
    def __init__(self, *, kwargs: _type_subject_value_t = dict()):
        ...

    @property
    def num(self) -> int:
        """
        :type value: int
        :rtype: int
        """
    
        ...    

    @num.setter
    def num(self, value: int):
        ...    

    @property
    def pointer(self) -> Any:
        """
        :type value: Any
        :rtype: Any
        """
    
        ...    

    @pointer.setter
    def pointer(self, value: Any):
        ...    

    @property
    def color(self) -> "color_t":
        """
        :type value: "color_t"
        :rtype: "color_t"
        """
    
        ...    

    @color.setter
    def color(self, value: "color_t"):
        ...    



class _type_observer_t(TypedDict, total=False):
    pass


class observer_t(Struct):
    
    def __init__(self, *, kwargs: _type_observer_t = dict()):
        ...

    def remove(self) -> None:
        """
        Remove an observer from its subject 
        

        :returns: 
        :rtype: None
        """
        ...

    def get_target(self) -> Any:
        """
        Get the target of an observer pointer to the saved target 
        

        :returns: pointer to the saved target 
        :rtype: Any
        """
        ...

    def get_target_obj(self) -> "obj":
        """
        Get the target object of the observer. It's the same as lv_observer_get_target and added only for semantic reasons pointer to the saved object target 
        

        :returns: pointer to the saved object target 
        :rtype: "obj"
        """
        ...

    def get_user_data(self) -> Any:
        """
        Get the user data of the observer. void pointer to the saved user data 
        

        :returns: void pointer to the saved user data 
        :rtype: Any
        """
        ...



class _type_color32_t(TypedDict, total=False):
    blue: int
    green: int
    red: int
    alpha: int


class color32_t(Struct):

    __SIZE__: ClassVar[int] = ...
    
    def __init__(self, *, kwargs: _type_color32_t = dict()):
        ...

    @property
    def blue(self) -> int:
        """
        :type value: int
        :rtype: int
        """
    
        ...    

    @blue.setter
    def blue(self, value: int):
        ...    

    @property
    def green(self) -> int:
        """
        :type value: int
        :rtype: int
        """
    
        ...    

    @green.setter
    def green(self, value: int):
        ...    

    @property
    def red(self) -> int:
        """
        :type value: int
        :rtype: int
        """
    
        ...    

    @red.setter
    def red(self, value: int):
        ...    

    @property
    def alpha(self) -> int:
        """
        :type value: int
        :rtype: int
        """
    
        ...    

    @alpha.setter
    def alpha(self, value: int):
        ...    


    def eq(self, c2: "color32_t") -> bool:
        """
        Check if two ARGB8888 color are equal true: equal 
        
        :param c2: the second color 
        :type c2: "color32_t"

        :returns: true: equal 
        :rtype: bool
        """
        ...

    def color_premultiply(self) -> None:
        """

        :returns: 
        :rtype: None
        """
        ...

    def luminance(self) -> int:
        """
        Get the luminance of a color32: luminance = 0.3 R + 0.59 G + 0.11 B the brightness [0..255] 
        

        :returns: the brightness [0..255] 
        :rtype: int
        """
        ...

    def color_mix32(self, bg: "color32_t") -> "color32_t":
        """
        Use bg.alpha in the return value Use fg.alpha as mix ratio 
        
        :param bg: 
        :type bg: "color32_t"

        :returns: 
        :rtype: "color32_t"
        """
        ...



class _type_span_t(TypedDict, total=False):
    pass


class span_t(Struct):
    
    def __init__(self, *, kwargs: _type_span_t = dict()):
        ...

    def set_text(self, text: str) -> None:
        """
        Set a new text for a span. Memory will be allocated to store the text by the span. 
        
        :param text: pointer to a text. 
        :type text: str

        :returns: 
        :rtype: None
        """
        ...

    def set_text_static(self, text: str) -> None:
        """
        Set a static text. It will not be saved by the span so the 'text' variable has to be 'alive' while the span exist. 
        
        :param text: pointer to a text. 
        :type text: str

        :returns: 
        :rtype: None
        """
        ...

    def get_style(self) -> "style_t":
        """
        Get a pointer to the style of a span pointer to the style. valid as long as the span is valid 
        

        :returns: pointer to the style. valid as long as the span is valid 
        :rtype: "style_t"
        """
        ...



class _type_pinyin_dict_t(TypedDict, total=False):
    pass


class pinyin_dict_t(Struct):

    __SIZE__: ClassVar[int] = ...
    
    def __init__(self, *, kwargs: _type_pinyin_dict_t = dict()):
        ...

    @property
    def py(self) -> str:
        ...    

    @property
    def py_mb(self) -> str:
        ...    



class _type_cache_class_t(TypedDict, total=False):
    pass


class cache_class_t(Struct):

    __SIZE__: ClassVar[int] = ...
    
    def __init__(self, *, kwargs: _type_cache_class_t = dict()):
        ...

    def create(self, node_size: int, max_size: int, ops: "cache_ops_t") -> "cache_t":
        """
        Create a cache object with the given parameters. Returns a pointer to the created cache object on success, NULL on error. 
        
        :param node_size: The node size is the size of the data stored in the cache.. 
        :type node_size: int
        :param max_size: The max size is the maximum amount of memory or count that the cache can hold. lv_cache_class_lru_rb_count: max_size is the maximum count of nodes in the cache. lv_cache_class_lru_rb_size: max_size is the maximum size of the cache in bytes. 
        :type max_size: int
        :param ops: A set of operations that can be performed on the cache. See :ref:`lv_cache_ops_t` for details. 
        :type ops: "cache_ops_t"

        :returns: Returns a pointer to the created cache object on success, NULL on error. 
        :rtype: "cache_t"
        """
        ...



class _type_cache_t(TypedDict, total=False):
    clz: "cache_class_t"
    node_size: int
    max_size: int
    size: int
    ops: "cache_ops_t"
    lock: "mutex_t"
    name: str


class cache_t(Struct):

    __SIZE__: ClassVar[int] = ...
    
    def __init__(self, *, kwargs: _type_cache_t = dict()):
        ...

    @property
    def clz(self) -> "cache_class_t":
        """
        :type value: "cache_class_t"
        :rtype: "cache_class_t"
        """
    
        ...    

    @clz.setter
    def clz(self, value: "cache_class_t"):
        ...    

    @property
    def node_size(self) -> int:
        """
        :type value: int
        :rtype: int
        """
    
        ...    

    @node_size.setter
    def node_size(self, value: int):
        ...    

    @property
    def max_size(self) -> int:
        """
        :type value: int
        :rtype: int
        """
    
        ...    

    @max_size.setter
    def max_size(self, value: int):
        ...    

    @property
    def size(self) -> int:
        """
        :type value: int
        :rtype: int
        """
    
        ...    

    @size.setter
    def size(self, value: int):
        ...    

    @property
    def ops(self) -> "cache_ops_t":
        """
        :type value: "cache_ops_t"
        :rtype: "cache_ops_t"
        """
    
        ...    

    @ops.setter
    def ops(self, value: "cache_ops_t"):
        ...    

    @property
    def lock(self) -> "mutex_t":
        """
        :type value: "mutex_t"
        :rtype: "mutex_t"
        """
    
        ...    

    @lock.setter
    def lock(self, value: "mutex_t"):
        ...    

    @property
    def name(self) -> str:
        """
        :type value: str
        :rtype: str
        """
    
        ...    

    @name.setter
    def name(self, value: str):
        ...    


    def destroy(self, cache: "cache_t") -> None:
        """
        Destroy a cache object. 
        
        :param cache: A user data pointer that will be passed to the free callback. 
        :type cache: "cache_t"

        :returns: 
        :rtype: None
        """
        ...

    def acquire(self, key: Any, cache: "cache_t") -> "cache_entry_t":
        """
        Acquire a cache entry with the given key. If entry not in cache, it will return NULL (not found). If the entry is found, it's priority will be changed by the cache's policy. And the lv_cache_entry_t::ref_cnt will be incremented. Returns a pointer to the acquired cache entry on success with lv_cache_entry_t::ref_cnt incremented, NULL on error. 
        
        :param key: The key of the entry to acquire. 
        :type key: Any
        :param cache: A user data pointer that will be passed to the create callback. 
        :type cache: "cache_t"

        :returns: Returns a pointer to the acquired cache entry on success with lv_cache_entry_t::ref_cnt incremented, NULL on error. 
        :rtype: "cache_entry_t"
        """
        ...

    def acquire_or_create(self, key: Any, cache: "cache_t") -> "cache_entry_t":
        """
        Acquire a cache entry with the given key. If the entry is not in the cache, it will create a new entry with the given key. If the entry is found, it's priority will be changed by the cache's policy. And the lv_cache_entry_t::ref_cnt will be incremented. If you want to use this API to simplify the code, you should provide a :ref:`lv_cache_ops_t::create_cb` that creates a new entry with the given key. This API is a combination of :ref:`lv_cache_acquire()` and :ref:`lv_cache_add()` . The effect is the same as calling :ref:`lv_cache_acquire()` and :ref:`lv_cache_add()` separately. And the internal impact on cache is also consistent with these two APIs. Returns a pointer to the acquired or created cache entry on success with lv_cache_entry_t::ref_cnt incremented, NULL on error. 
        
        :param key: The key of the entry to acquire or create. 
        :type key: Any
        :param cache: A user data pointer that will be passed to the create callback. 
        :type cache: "cache_t"

        :returns: Returns a pointer to the acquired or created cache entry on success with lv_cache_entry_t::ref_cnt incremented, NULL on error. 
        :rtype: "cache_entry_t"
        """
        ...

    def add(self, key: Any, cache: "cache_t") -> "cache_entry_t":
        """
        Add a new cache entry with the given key and data. If the cache is full, the cache's policy will be used to evict an entry. Returns a pointer to the added cache entry on success with lv_cache_entry_t::ref_cnt incremented, NULL on error. 
        
        :param key: The key of the entry to add. 
        :type key: Any
        :param cache: A user data pointer that will be passed to the create callback. 
        :type cache: "cache_t"

        :returns: Returns a pointer to the added cache entry on success with lv_cache_entry_t::ref_cnt incremented, NULL on error. 
        :rtype: "cache_entry_t"
        """
        ...

    def release(self, entry: "cache_entry_t", cache: "cache_t") -> None:
        """
        Release a cache entry. The lv_cache_entry_t::ref_cnt will be decremented. If the lv_cache_entry_t::ref_cnt is zero, it will issue an error. If the entry passed to this function is the last reference to the data and the entry is marked as invalid, the cache's policy will be used to evict the entry. 
        
        :param entry: The cache entry pointer to release. 
        :type entry: "cache_entry_t"
        :param cache: A user data pointer that will be passed to the free callback. 
        :type cache: "cache_t"

        :returns: 
        :rtype: None
        """
        ...

    def reserve(self, reserved_size: int, cache: "cache_t") -> None:
        """
        Reserve a certain amount of memory/count in the cache. This function is useful when you want to reserve a certain amount of memory/count in advance, for example, when you know that you will need it later. When the current cache size is max than the reserved size, the function will evict entries until the reserved size is reached. 
        
        :param reserved_size: The amount of memory/count to reserve. 
        :type reserved_size: int
        :param cache: A user data pointer that will be passed to the free callback. 
        :type cache: "cache_t"

        :returns: 
        :rtype: None
        """
        ...

    def drop(self, key: Any, cache: "cache_t") -> None:
        """
        Drop a cache entry with the given key. If the entry is not in the cache, nothing will happen to it. If the entry is found, it will be removed from the cache and its data will be freed when the last reference to it is released. The data will not be freed immediately but when the last reference to it is released. But this entry will not be found by :ref:`lv_cache_acquire()` . If you want cache a same key again, you should use :ref:`lv_cache_add()` or :ref:`lv_cache_acquire_or_create()` . 
        
        :param key: The key of the entry to drop. 
        :type key: Any
        :param cache: A user data pointer that will be passed to the free callback. 
        :type cache: "cache_t"

        :returns: 
        :rtype: None
        """
        ...

    def drop_all(self, cache: "cache_t") -> None:
        """
        Drop all cache entries. All entries will be removed from the cache and their data will be freed when the last reference to them is released. If some entries are still referenced by other objects, it will issue an error. And this case shouldn't happen in normal cases.. 
        
        :param cache: A user data pointer that will be passed to the free callback. 
        :type cache: "cache_t"

        :returns: 
        :rtype: None
        """
        ...

    def evict_one(self, cache: "cache_t") -> bool:
        """
        Evict one entry from the cache. The eviction policy will be used to select the entry to evict. Returns true if an entry is evicted, false if no entry is evicted. 
        
        :param cache: A user data pointer that will be passed to the free callback. 
        :type cache: "cache_t"

        :returns: Returns true if an entry is evicted, false if no entry is evicted. 
        :rtype: bool
        """
        ...

    def set_max_size(self, max_size: int, cache: "cache_t") -> None:
        """
        Set the maximum size of the cache. If the current cache size is greater than the new maximum size, the cache's policy will be used to evict entries until the new maximum size is reached. If set to 0, the cache will be disabled. But this behavior will happen only new entries are added to the cache. 
        
        :param max_size: The new maximum size of the cache. 
        :type max_size: int
        :param cache: A user data pointer that will be passed to the free callback. 
        :type cache: "cache_t"

        :returns: 
        :rtype: None
        """
        ...

    def get_max_size(self, cache: "cache_t") -> int:
        """
        Get the maximum size of the cache. Returns the maximum size of the cache. 
        
        :param cache: A user data pointer that will be passed to the free callback. 
        :type cache: "cache_t"

        :returns: Returns the maximum size of the cache. 
        :rtype: int
        """
        ...

    def get_size(self, cache: "cache_t") -> int:
        """
        Get the current size of the cache. Returns the current size of the cache. 
        
        :param cache: A user data pointer that will be passed to the free callback. 
        :type cache: "cache_t"

        :returns: Returns the current size of the cache. 
        :rtype: int
        """
        ...

    def get_free_size(self, cache: "cache_t") -> int:
        """
        Get the free size of the cache. Returns the free size of the cache. 
        
        :param cache: A user data pointer that will be passed to the free callback. 
        :type cache: "cache_t"

        :returns: Returns the free size of the cache. 
        :rtype: int
        """
        ...

    def is_enabled(self) -> bool:
        """
        Return true if the cache is enabled. Disabled cache means that when the max_size of the cache is 0. In this case, all cache operations will be no-op. Returns true if the cache is enabled, false otherwise. 
        

        :returns: Returns true if the cache is enabled, false otherwise. 
        :rtype: bool
        """
        ...

    def set_compare_cb(self, compare_cb: "cache_compare_cb_t", cache: "cache_t") -> None:
        """
        Set the compare callback of the cache. 
        
        :param compare_cb: The compare callback to set. 
        :type compare_cb: "cache_compare_cb_t"
        :param cache: A user data pointer. 
        :type cache: "cache_t"

        :returns: 
        :rtype: None
        """
        ...

    def set_create_cb(self, alloc_cb: Callable[[Any, Any], bool], cache: "cache_t") -> None:
        """
        Set the create callback of the cache. 
        
        :param alloc_cb: The create callback to set. 
        :type alloc_cb: Callable[[Any, Any], bool]
        :param cache: A user data pointer. 
        :type cache: "cache_t"

        :returns: 
        :rtype: None
        """
        ...

    def set_free_cb(self, free_cb: Callable[[Any, Any], None], cache: "cache_t") -> None:
        """
        Set the free callback of the cache. 
        
        :param free_cb: The free callback to set. 
        :type free_cb: Callable[[Any, Any], None]
        :param cache: A user data pointer. 
        :type cache: "cache_t"

        :returns: 
        :rtype: None
        """
        ...

    def set_name(self, name: str) -> None:
        """
        Give a name for a cache object. Only the pointer of the string is saved. 
        
        :param name: The name of the cache. 
        :type name: str

        :returns: 
        :rtype: None
        """
        ...

    def get_name(self) -> str:
        """
        Get the name of a cache object. Returns the name of the cache. 
        

        :returns: Returns the name of the cache. 
        :rtype: str
        """
        ...



class _type_cache_ops_t(TypedDict, total=False):
    pass


class cache_ops_t(Struct):

    __SIZE__: ClassVar[int] = ...
    
    def __init__(self, *, kwargs: _type_cache_ops_t = dict()):
        ...


class _type_mem_monitor_t(TypedDict, total=False):
    total_size: int
    free_cnt: int
    free_size: int
    free_biggest_size: int
    used_cnt: int
    max_used: int
    used_pct: int
    frag_pct: int


class mem_monitor_t(Struct):

    __SIZE__: ClassVar[int] = ...
    
    def __init__(self, *, kwargs: _type_mem_monitor_t = dict()):
        ...

    @property
    def total_size(self) -> int:
        """
        :type value: int
        :rtype: int
        """
    
        ...    

    @total_size.setter
    def total_size(self, value: int):
        ...    

    @property
    def free_cnt(self) -> int:
        """
        :type value: int
        :rtype: int
        """
    
        ...    

    @free_cnt.setter
    def free_cnt(self, value: int):
        ...    

    @property
    def free_size(self) -> int:
        """
        :type value: int
        :rtype: int
        """
    
        ...    

    @free_size.setter
    def free_size(self, value: int):
        ...    

    @property
    def free_biggest_size(self) -> int:
        """
        :type value: int
        :rtype: int
        """
    
        ...    

    @free_biggest_size.setter
    def free_biggest_size(self, value: int):
        ...    

    @property
    def used_cnt(self) -> int:
        """
        :type value: int
        :rtype: int
        """
    
        ...    

    @used_cnt.setter
    def used_cnt(self, value: int):
        ...    

    @property
    def max_used(self) -> int:
        """
        :type value: int
        :rtype: int
        """
    
        ...    

    @max_used.setter
    def max_used(self, value: int):
        ...    

    @property
    def used_pct(self) -> int:
        """
        :type value: int
        :rtype: int
        """
    
        ...    

    @used_pct.setter
    def used_pct(self, value: int):
        ...    

    @property
    def frag_pct(self) -> int:
        """
        :type value: int
        :rtype: int
        """
    
        ...    

    @frag_pct.setter
    def frag_pct(self, value: int):
        ...    


    def core(self) -> None:
        """
        Used internally by :ref:`lv_mem_monitor()` to gather LVGL heap state information. 
        

        :returns: 
        :rtype: None
        """
        ...

    def monitor(self) -> None:
        """
        Give information about the work memory of dynamic allocation 
        

        :returns: 
        :rtype: None
        """
        ...



class _type_timer_t(TypedDict, total=False):
    pass


class timer_t(Struct):
    
    def __init__(self, *, kwargs: _type_timer_t = dict()):
        ...

    def delete(self) -> None:
        """
        Delete a lv_timer 
        

        :returns: 
        :rtype: None
        """
        ...

    def pause(self) -> None:
        """
        Pause a timer. 
        

        :returns: 
        :rtype: None
        """
        ...

    def resume(self) -> None:
        """
        Resume a timer. 
        

        :returns: 
        :rtype: None
        """
        ...

    def set_cb(self, timer_cb: Callable[["timer_t"], None]) -> None:
        """
        Set the callback to the timer (the function to call periodically) 
        
        :param timer_cb: the function to call periodically 
        :type timer_cb: Callable[["timer_t"], None]

        :returns: 
        :rtype: None
        """
        ...

    def set_period(self, period: int) -> None:
        """
        Set new period for a lv_timer 
        
        :param period: the new period 
        :type period: int

        :returns: 
        :rtype: None
        """
        ...

    def ready(self) -> None:
        """
        Make a lv_timer ready. It will not wait its period. 
        

        :returns: 
        :rtype: None
        """
        ...

    def set_repeat_count(self, repeat_count: int) -> None:
        """
        Set the number of times a timer will repeat. 
        
        :param repeat_count: -1 : infinity; 0 : stop ; n>0: residual times 
        :type repeat_count: int

        :returns: 
        :rtype: None
        """
        ...

    def set_auto_delete(self, auto_delete: bool) -> None:
        """
        Set whether a lv_timer will be deleted automatically when it is called repeat_count times. 
        
        :param auto_delete: true: auto delete; false: timer will be paused when it is called repeat_count times. 
        :type auto_delete: bool

        :returns: 
        :rtype: None
        """
        ...

    def set_user_data(self, timer: "timer_t") -> None:
        """
        Set custom parameter to the lv_timer. 
        
        :param timer: custom parameter 
        :type timer: "timer_t"

        :returns: 
        :rtype: None
        """
        ...

    def reset(self) -> None:
        """
        Reset a lv_timer. It will be called the previously set period milliseconds later. 
        

        :returns: 
        :rtype: None
        """
        ...

    def get_next(self) -> "timer_t":
        """
        Iterate through the timers the next timer or NULL if there is no more timer 
        

        :returns: the next timer or NULL if there is no more timer 
        :rtype: "timer_t"
        """
        ...

    def get_user_data(self) -> Any:
        """
        Get the user_data passed when the timer was created pointer to the user_data 
        

        :returns: pointer to the user_data 
        :rtype: Any
        """
        ...

    def get_paused(self) -> bool:
        """
        Get the pause state of a timer true: timer is paused; false: timer is running 
        

        :returns: true: timer is paused; false: timer is running 
        :rtype: bool
        """
        ...



class _type_array_t(TypedDict, total=False):
    data: Union[str, List[int]]
    size: int
    capacity: int
    element_size: int


class array_t(Struct):

    __SIZE__: ClassVar[int] = ...
    
    def __init__(self, *, kwargs: _type_array_t = dict()):
        ...

    @property
    def data(self) -> Union[str, List[int]]:
        """
        :type value: Union[str, List[int]]
        :rtype: Union[str, List[int]]
        """
    
        ...    

    @data.setter
    def data(self, value: Union[str, List[int]]):
        ...    

    @property
    def size(self) -> int:
        """
        :type value: int
        :rtype: int
        """
    
        ...    

    @size.setter
    def size(self, value: int):
        ...    

    @property
    def capacity(self) -> int:
        """
        :type value: int
        :rtype: int
        """
    
        ...    

    @capacity.setter
    def capacity(self, value: int):
        ...    

    @property
    def element_size(self) -> int:
        """
        :type value: int
        :rtype: int
        """
    
        ...    

    @element_size.setter
    def element_size(self, value: int):
        ...    


    def init(self, capacity: int, element_size: int) -> None:
        """
        Init an array. 
        
        :param capacity: the initial capacity of the array 
        :type capacity: int
        :param element_size: the size of an element in bytes 
        :type element_size: int

        :returns: 
        :rtype: None
        """
        ...

    def resize(self, new_capacity: int) -> None:
        """
        Resize the array to the given capacity. if the new capacity is smaller than the current size, the array will be truncated. 
        
        :param new_capacity: the new capacity of the array 
        :type new_capacity: int

        :returns: 
        :rtype: None
        """
        ...

    def deinit(self) -> None:
        """
        Deinit the array, and free the allocated memory 
        

        :returns: 
        :rtype: None
        """
        ...

    def size(self) -> int:
        """
        Return how many elements are stored in the array. the number of elements stored in the array 
        

        :returns: the number of elements stored in the array 
        :rtype: int
        """
        ...

    def capacity(self) -> int:
        """
        Return the capacity of the array, i.e. how many elements can be stored. the capacity of the array 
        

        :returns: the capacity of the array 
        :rtype: int
        """
        ...

    def is_empty(self) -> bool:
        """
        Return if the array is empty true: array is empty; false: array is not empty 
        

        :returns: true: array is empty; false: array is not empty 
        :rtype: bool
        """
        ...

    def is_full(self) -> bool:
        """
        Return if the array is full true: array is full; false: array is not full 
        

        :returns: true: array is full; false: array is not full 
        :rtype: bool
        """
        ...

    def copy(self, source: "array_t") -> None:
        """
        Copy an array to another. this will create a new array with the same capacity and size as the source array. 
        
        :param source: pointer to an :ref:`lv_array_t` variable to copy from 
        :type source: "array_t"

        :returns: 
        :rtype: None
        """
        ...

    def clear(self) -> None:
        """
        Remove all elements in array. 
        

        :returns: 
        :rtype: None
        """
        ...

    def shrink(self) -> None:
        """
        Shrink the memory capacity of array if necessary. 
        

        :returns: 
        :rtype: None
        """
        ...

    def remove(self, index: int) -> "result_t":
        """
        Remove the element at the specified position in the array. LV_RESULT_OK: success, otherwise: error 
        
        :param index: the index of the element to remove 
        :type index: int

        :returns: LV_RESULT_OK: success, otherwise: error 
        :rtype: "result_t"
        """
        ...

    def erase(self, start: int, end: int) -> "result_t":
        """
        Remove from the array either a single element or a range of elements ([start, end)). This effectively reduces the container size by the number of elements removed.  When start equals to end, the function has no effect.  LV_RESULT_OK: success, otherwise: error 
        
        :param start: the index of the first element to be removed 
        :type start: int
        :param end: the index of the first element that is not to be removed 
        :type end: int

        :returns: LV_RESULT_OK: success, otherwise: error 
        :rtype: "result_t"
        """
        ...

    def concat(self, other: "array_t") -> "result_t":
        """
        Concatenate two arrays. Adds new elements to the end of the array. The destination array is automatically expanded as necessary.  LV_RESULT_OK: success, otherwise: error 
        
        :param other: pointer to the array to concatenate 
        :type other: "array_t"

        :returns: LV_RESULT_OK: success, otherwise: error 
        :rtype: "result_t"
        """
        ...

    def push_back(self, element: Any) -> "result_t":
        """
        Push back element. Adds a new element to the end of the array. If the array capacity is not enough for the new element, the array will be resized automatically. LV_RESULT_OK: success, otherwise: error 
        
        :param element: pointer to the element to add 
        :type element: Any

        :returns: LV_RESULT_OK: success, otherwise: error 
        :rtype: "result_t"
        """
        ...

    def assign(self, index: int, value: Any) -> "result_t":
        """
        Assigns one content to the array, replacing its current content. true: success; false: error 
        
        :param index: the index of the element to replace 
        :type index: int
        :param value: pointer to the elements to add 
        :type value: Any

        :returns: true: success; false: error 
        :rtype: "result_t"
        """
        ...

    def at(self, index: int) -> Any:
        """
        Returns a pointer to the element at position n in the array. a pointer to the requested element, NULL if index is out of range 
        
        :param index: the index of the element to return 
        :type index: int

        :returns: a pointer to the requested element, NULL if index is out of range 
        :rtype: Any
        """
        ...

    def front(self) -> Any:
        """
        Returns a pointer to the first element in the array. a pointer to the first element in the array 
        

        :returns: a pointer to the first element in the array 
        :rtype: Any
        """
        ...

    def back(self) -> Any:
        """
        Returns a pointer to the last element in the array. 
        

        :returns: 
        :rtype: Any
        """
        ...



class _type_anim_timeline_t(TypedDict, total=False):
    pass


class anim_timeline_t(Struct):
    
    def __init__(self, *, kwargs: _type_anim_timeline_t = dict()):
        ...

    def delete(self) -> None:
        """
        Delete animation timeline. 
        

        :returns: 
        :rtype: None
        """
        ...

    def add(self, start_time: int, a: anim_t) -> None:
        """
        Add animation to the animation timeline. 
        
        :param start_time: the time the animation started on the timeline, note that start_time will override the value of delay. 
        :type start_time: int
        :param a: pointer to an animation. 
        :type a: anim_t

        :returns: 
        :rtype: None
        """
        ...

    def start(self) -> int:
        """
        Start the animation timeline. total time spent in animation timeline. 
        

        :returns: total time spent in animation timeline. 
        :rtype: int
        """
        ...

    def pause(self) -> None:
        """
        Pause the animation timeline. 
        

        :returns: 
        :rtype: None
        """
        ...

    def set_reverse(self, reverse: bool) -> None:
        """
        Set the playback direction of the animation timeline. 
        
        :param reverse: whether to play in reverse. 
        :type reverse: bool

        :returns: 
        :rtype: None
        """
        ...

    def set_repeat_count(self, cnt: int) -> None:
        """
        Make the animation timeline repeat itself. 
        
        :param cnt: repeat count or LV_ANIM_REPEAT_INFINITE for infinite repetition. 0: to disable repetition. 
        :type cnt: int

        :returns: 
        :rtype: None
        """
        ...

    def set_repeat_delay(self, cnt: int) -> None:
        """
        Set a delay before repeating the animation timeline. 
        
        :param cnt: delay in milliseconds before repeating the animation timeline. 
        :type cnt: int

        :returns: 
        :rtype: None
        """
        ...

    def set_progress(self, progress: int) -> None:
        """
        Set the progress of the animation timeline. 
        
        :param progress: set value 0~65535 to map 0~100% animation progress. 
        :type progress: int

        :returns: 
        :rtype: None
        """
        ...

    def get_playtime(self) -> int:
        """
        Get the time used to play the animation timeline. total time spent in animation timeline. 
        

        :returns: total time spent in animation timeline. 
        :rtype: int
        """
        ...

    def get_reverse(self) -> bool:
        """
        Get whether the animation timeline is played in reverse. return true if it is reverse playback. 
        

        :returns: return true if it is reverse playback. 
        :rtype: bool
        """
        ...

    def get_progress(self) -> int:
        """
        Get the progress of the animation timeline. return value 0~65535 to map 0~100% animation progress. 
        

        :returns: return value 0~65535 to map 0~100% animation progress. 
        :rtype: int
        """
        ...

    def get_repeat_count(self) -> int:
        """
        Get repeat count of the animation timeline. 
        

        :returns: 
        :rtype: int
        """
        ...

    def get_repeat_delay(self) -> int:
        """
        Get repeat delay of the animation timeline. 
        

        :returns: 
        :rtype: int
        """
        ...



class _type_rb_t(TypedDict, total=False):
    pass


class rb_t(Struct):
    
    def __init__(self, *, kwargs: _type_rb_t = dict()):
        ...

    def init(self, compare: "rb_compare_t", node_size: int) -> bool:
        """
        :param compare: 
        :type compare: "rb_compare_t"
        :param node_size: 
        :type node_size: int

        :returns: 
        :rtype: bool
        """
        ...

    def insert(self, key: Any) -> "rb_node_t":
        """
        :param key: 
        :type key: Any

        :returns: 
        :rtype: "rb_node_t"
        """
        ...

    def find(self, key: Any) -> "rb_node_t":
        """
        :param key: 
        :type key: Any

        :returns: 
        :rtype: "rb_node_t"
        """
        ...

    def remove_node(self, node: "rb_node_t") -> Any:
        """
        :param node: 
        :type node: "rb_node_t"

        :returns: 
        :rtype: Any
        """
        ...

    def remove(self, key: Any) -> Any:
        """
        :param key: 
        :type key: Any

        :returns: 
        :rtype: Any
        """
        ...

    def drop_node(self, node: "rb_node_t") -> bool:
        """
        :param node: 
        :type node: "rb_node_t"

        :returns: 
        :rtype: bool
        """
        ...

    def drop(self, key: Any) -> bool:
        """
        :param key: 
        :type key: Any

        :returns: 
        :rtype: bool
        """
        ...

    def minimum(self) -> "rb_node_t":
        """

        :returns: 
        :rtype: "rb_node_t"
        """
        ...

    def maximum(self) -> "rb_node_t":
        """

        :returns: 
        :rtype: "rb_node_t"
        """
        ...

    def destroy(self) -> None:
        """

        :returns: 
        :rtype: None
        """
        ...



class _type_rb_node_t(TypedDict, total=False):
    pass


class rb_node_t(Struct):
    
    def __init__(self, *, kwargs: _type_rb_node_t = dict()):
        ...

    def minimum_from(self) -> "rb_node_t":
        """

        :returns: 
        :rtype: "rb_node_t"
        """
        ...

    def maximum_from(self) -> "rb_node_t":
        """

        :returns: 
        :rtype: "rb_node_t"
        """
        ...



class _type_color16_t(TypedDict, total=False):
    blue: int
    green: int
    red: int


class color16_t(Struct):

    __SIZE__: ClassVar[int] = ...
    
    def __init__(self, *, kwargs: _type_color16_t = dict()):
        ...

    @property
    def blue(self) -> int:
        """
        :type value: int
        :rtype: int
        """
    
        ...    

    @blue.setter
    def blue(self, value: int):
        ...    

    @property
    def green(self) -> int:
        """
        :type value: int
        :rtype: int
        """
    
        ...    

    @green.setter
    def green(self, value: int):
        ...    

    @property
    def red(self) -> int:
        """
        :type value: int
        :rtype: int
        """
    
        ...    

    @red.setter
    def red(self, value: int):
        ...    


    def premultiply(self, a: opa_t) -> None:
        """
        :param a: 
        :type a: opa_t

        :returns: 
        :rtype: None
        """
        ...

    def luminance(self) -> int:
        """
        Get the luminance of a color16: luminance = 0.3 R + 0.59 G + 0.11 B the brightness [0..255] 
        

        :returns: the brightness [0..255] 
        :rtype: int
        """
        ...



class _type_fs_drv_t(TypedDict, total=False):
    letter: str
    cache_size: int
    user_data: Any


class fs_drv_t(Struct):

    __SIZE__: ClassVar[int] = ...
    
    def __init__(self, *, kwargs: _type_fs_drv_t = dict()):
        ...

    @property
    def letter(self) -> str:
        """
        :type value: str
        :rtype: str
        """
    
        ...    

    @letter.setter
    def letter(self, value: str):
        ...    

    @property
    def cache_size(self) -> int:
        """
        :type value: int
        :rtype: int
        """
    
        ...    

    @cache_size.setter
    def cache_size(self, value: int):
        ...    

    @property
    def user_data(self) -> Any:
        """
        :type value: Any
        :rtype: Any
        """
    
        ...    

    @user_data.setter
    def user_data(self, value: Any):
        ...    


    def init(self) -> None:
        """
        Initialize a file system driver with default values. It is used to ensure all fields have known values and not memory junk. After it you can set the fields. 
        

        :returns: 
        :rtype: None
        """
        ...

    def register(self) -> None:
        """
        Add a new drive 
        

        :returns: 
        :rtype: None
        """
        ...



class _type_fs_file_t(TypedDict, total=False):
    file_d: Any
    drv: "fs_drv_t"
    cache: "fs_file_cache_t"


class fs_file_t(Struct):

    __SIZE__: ClassVar[int] = ...
    
    def __init__(self, *, kwargs: _type_fs_file_t = dict()):
        ...

    @property
    def file_d(self) -> Any:
        """
        :type value: Any
        :rtype: Any
        """
    
        ...    

    @file_d.setter
    def file_d(self, value: Any):
        ...    

    @property
    def drv(self) -> "fs_drv_t":
        """
        :type value: "fs_drv_t"
        :rtype: "fs_drv_t"
        """
    
        ...    

    @drv.setter
    def drv(self, value: "fs_drv_t"):
        ...    

    @property
    def cache(self) -> "fs_file_cache_t":
        """
        :type value: "fs_file_cache_t"
        :rtype: "fs_file_cache_t"
        """
    
        ...    

    @cache.setter
    def cache(self, value: "fs_file_cache_t"):
        ...    


    def open(self, path: str, mode: fs_mode_t) -> "fs_res_t":
        """
        Open a file LV_FS_RES_OK or any error from lv_fs_res_t enum 
        
        :param path: path to the file beginning with the driver letter (e.g. S:/folder/file.txt) 
        :type path: str
        :param mode: read: FS_MODE_RD, write: FS_MODE_WR, both: FS_MODE_RD | FS_MODE_WR 
        :type mode: fs_mode_t

        :returns: LV_FS_RES_OK or any error from lv_fs_res_t enum 
        :rtype: "fs_res_t"
        """
        ...

    def close(self) -> "fs_res_t":
        """
        Close an already opened file LV_FS_RES_OK or any error from lv_fs_res_t enum 
        

        :returns: LV_FS_RES_OK or any error from lv_fs_res_t enum 
        :rtype: "fs_res_t"
        """
        ...

    def read(self, buf: Any, btr: int, br: List[int]) -> "fs_res_t":
        """
        Read from a file LV_FS_RES_OK or any error from lv_fs_res_t enum 
        
        :param buf: pointer to a buffer where the read bytes are stored 
        :type buf: Any
        :param btr: Bytes To Read 
        :type btr: int
        :param br: the number of real read bytes (Bytes Read). NULL if unused. 
        :type br: List[int]

        :returns: LV_FS_RES_OK or any error from lv_fs_res_t enum 
        :rtype: "fs_res_t"
        """
        ...

    def write(self, buf: Any, btw: int, bw: List[int]) -> "fs_res_t":
        """
        Write into a file LV_FS_RES_OK or any error from lv_fs_res_t enum 
        
        :param buf: pointer to a buffer with the bytes to write 
        :type buf: Any
        :param btw: Bytes To Write 
        :type btw: int
        :param bw: the number of real written bytes (Bytes Written). NULL if unused. 
        :type bw: List[int]

        :returns: LV_FS_RES_OK or any error from lv_fs_res_t enum 
        :rtype: "fs_res_t"
        """
        ...

    def seek(self, pos: int, whence: "fs_whence_t") -> "fs_res_t":
        """
        Set the position of the 'cursor' (read write pointer) in a file LV_FS_RES_OK or any error from lv_fs_res_t enum 
        
        :param pos: the new position expressed in bytes index (0: start of file) 
        :type pos: int
        :param whence: tells from where to set position. See lv_fs_whence_t 
        :type whence: "fs_whence_t"

        :returns: LV_FS_RES_OK or any error from lv_fs_res_t enum 
        :rtype: "fs_res_t"
        """
        ...

    def tell(self, pos: List[int]) -> "fs_res_t":
        """
        Give the position of the read write pointer LV_FS_RES_OK or any error from 'fs_res_t' 
        
        :param pos: pointer to store the position of the read write pointer 
        :type pos: List[int]

        :returns: LV_FS_RES_OK or any error from 'fs_res_t' 
        :rtype: "fs_res_t"
        """
        ...



class _type_fs_file_cache_t(TypedDict, total=False):
    pass


class fs_file_cache_t(Struct):
    
    def __init__(self, *, kwargs: _type_fs_file_cache_t = dict()):
        ...


class _type_fs_path_ex_t(TypedDict, total=False):
    pass


class fs_path_ex_t(Struct):
    
    def __init__(self, *, kwargs: _type_fs_path_ex_t = dict()):
        ...

    def make_path_from_buffer(self, letter: str, buf: Any, size: int) -> None:
        """
        Make a path object for the memory-mapped file compatible with the file system interface 
        
        :param letter: the letter of the driver. E.g. LV_FS_MEMFS_LETTER 
        :type letter: str
        :param buf: address of the memory buffer 
        :type buf: Any
        :param size: size of the memory buffer in bytes 
        :type size: int

        :returns: 
        :rtype: None
        """
        ...



class _type_fs_dir_t(TypedDict, total=False):
    dir_d: Any
    drv: "fs_drv_t"


class fs_dir_t(Struct):

    __SIZE__: ClassVar[int] = ...
    
    def __init__(self, *, kwargs: _type_fs_dir_t = dict()):
        ...

    @property
    def dir_d(self) -> Any:
        """
        :type value: Any
        :rtype: Any
        """
    
        ...    

    @dir_d.setter
    def dir_d(self, value: Any):
        ...    

    @property
    def drv(self) -> "fs_drv_t":
        """
        :type value: "fs_drv_t"
        :rtype: "fs_drv_t"
        """
    
        ...    

    @drv.setter
    def drv(self, value: "fs_drv_t"):
        ...    


    def open(self, path: str) -> "fs_res_t":
        """
        Initialize a 'fs_dir_t' variable for directory reading LV_FS_RES_OK or any error from lv_fs_res_t enum 
        
        :param path: path to a directory 
        :type path: str

        :returns: LV_FS_RES_OK or any error from lv_fs_res_t enum 
        :rtype: "fs_res_t"
        """
        ...

    def read(self, fn: str, fn_len: int) -> "fs_res_t":
        """
        Read the next filename form a directory. The name of the directories will begin with '/' LV_FS_RES_OK or any error from lv_fs_res_t enum 
        
        :param fn: pointer to a buffer to store the filename 
        :type fn: str
        :param fn_len: length of the buffer to store the filename 
        :type fn_len: int

        :returns: LV_FS_RES_OK or any error from lv_fs_res_t enum 
        :rtype: "fs_res_t"
        """
        ...

    def close(self) -> "fs_res_t":
        """
        Close the directory reading LV_FS_RES_OK or any error from lv_fs_res_t enum 
        

        :returns: LV_FS_RES_OK or any error from lv_fs_res_t enum 
        :rtype: "fs_res_t"
        """
        ...



class _type_grad_t(TypedDict, total=False):
    pass


class grad_t(Struct):
    
    def __init__(self, *, kwargs: _type_grad_t = dict()):
        ...

    def gradient_cleanup(self) -> None:
        """
        Clean up the gradient item after it was get with lv_grad_get_from_cache . 
        

        :returns: 
        :rtype: None
        """
        ...



class _type_draw_fill_dsc_t(TypedDict, total=False):
    base: "draw_dsc_base_t"
    radius: int
    opa: "opa_t"
    color: "color_t"
    grad: "grad_dsc_t"


class draw_fill_dsc_t(Struct):

    __SIZE__: ClassVar[int] = ...
    
    def __init__(self, *, kwargs: _type_draw_fill_dsc_t = dict()):
        ...

    @property
    def base(self) -> "draw_dsc_base_t":
        """
        :type value: "draw_dsc_base_t"
        :rtype: "draw_dsc_base_t"
        """
    
        ...    

    @base.setter
    def base(self, value: "draw_dsc_base_t"):
        ...    

    @property
    def radius(self) -> int:
        """
        :type value: int
        :rtype: int
        """
    
        ...    

    @radius.setter
    def radius(self, value: int):
        ...    

    @property
    def opa(self) -> "opa_t":
        """
        :type value: "opa_t"
        :rtype: "opa_t"
        """
    
        ...    

    @opa.setter
    def opa(self, value: "opa_t"):
        ...    

    @property
    def color(self) -> "color_t":
        """
        :type value: "color_t"
        :rtype: "color_t"
        """
    
        ...    

    @color.setter
    def color(self, value: "color_t"):
        ...    

    @property
    def grad(self) -> "grad_dsc_t":
        """
        :type value: "grad_dsc_t"
        :rtype: "grad_dsc_t"
        """
    
        ...    

    @grad.setter
    def grad(self, value: "grad_dsc_t"):
        ...    


    def init(self) -> None:
        """
        Initialize a fill draw descriptor. 
        

        :returns: 
        :rtype: None
        """
        ...



class _type_draw_border_dsc_t(TypedDict, total=False):
    base: "draw_dsc_base_t"
    radius: int
    color: "color_t"
    width: int
    opa: "opa_t"
    side: "border_side_t"


class draw_border_dsc_t(Struct):

    __SIZE__: ClassVar[int] = ...
    
    def __init__(self, *, kwargs: _type_draw_border_dsc_t = dict()):
        ...

    @property
    def base(self) -> "draw_dsc_base_t":
        """
        :type value: "draw_dsc_base_t"
        :rtype: "draw_dsc_base_t"
        """
    
        ...    

    @base.setter
    def base(self, value: "draw_dsc_base_t"):
        ...    

    @property
    def radius(self) -> int:
        """
        :type value: int
        :rtype: int
        """
    
        ...    

    @radius.setter
    def radius(self, value: int):
        ...    

    @property
    def color(self) -> "color_t":
        """
        :type value: "color_t"
        :rtype: "color_t"
        """
    
        ...    

    @color.setter
    def color(self, value: "color_t"):
        ...    

    @property
    def width(self) -> int:
        """
        :type value: int
        :rtype: int
        """
    
        ...    

    @width.setter
    def width(self, value: int):
        ...    

    @property
    def opa(self) -> "opa_t":
        """
        :type value: "opa_t"
        :rtype: "opa_t"
        """
    
        ...    

    @opa.setter
    def opa(self, value: "opa_t"):
        ...    

    @property
    def side(self) -> "border_side_t":
        """
        :type value: "border_side_t"
        :rtype: "border_side_t"
        """
    
        ...    

    @side.setter
    def side(self, value: "border_side_t"):
        ...    


    def init(self) -> None:
        """
        Initialize a border draw descriptor. 
        

        :returns: 
        :rtype: None
        """
        ...



class _type_draw_box_shadow_dsc_t(TypedDict, total=False):
    base: "draw_dsc_base_t"
    radius: int
    color: "color_t"
    width: int
    spread: int
    ofs_x: int
    ofs_y: int
    opa: "opa_t"
    bg_cover: int


class draw_box_shadow_dsc_t(Struct):

    __SIZE__: ClassVar[int] = ...
    
    def __init__(self, *, kwargs: _type_draw_box_shadow_dsc_t = dict()):
        ...

    @property
    def base(self) -> "draw_dsc_base_t":
        """
        :type value: "draw_dsc_base_t"
        :rtype: "draw_dsc_base_t"
        """
    
        ...    

    @base.setter
    def base(self, value: "draw_dsc_base_t"):
        ...    

    @property
    def radius(self) -> int:
        """
        :type value: int
        :rtype: int
        """
    
        ...    

    @radius.setter
    def radius(self, value: int):
        ...    

    @property
    def color(self) -> "color_t":
        """
        :type value: "color_t"
        :rtype: "color_t"
        """
    
        ...    

    @color.setter
    def color(self, value: "color_t"):
        ...    

    @property
    def width(self) -> int:
        """
        :type value: int
        :rtype: int
        """
    
        ...    

    @width.setter
    def width(self, value: int):
        ...    

    @property
    def spread(self) -> int:
        """
        :type value: int
        :rtype: int
        """
    
        ...    

    @spread.setter
    def spread(self, value: int):
        ...    

    @property
    def ofs_x(self) -> int:
        """
        :type value: int
        :rtype: int
        """
    
        ...    

    @ofs_x.setter
    def ofs_x(self, value: int):
        ...    

    @property
    def ofs_y(self) -> int:
        """
        :type value: int
        :rtype: int
        """
    
        ...    

    @ofs_y.setter
    def ofs_y(self, value: int):
        ...    

    @property
    def opa(self) -> "opa_t":
        """
        :type value: "opa_t"
        :rtype: "opa_t"
        """
    
        ...    

    @opa.setter
    def opa(self, value: "opa_t"):
        ...    

    @property
    def bg_cover(self) -> int:
        """
        :type value: int
        :rtype: int
        """
    
        ...    

    @bg_cover.setter
    def bg_cover(self, value: int):
        ...    


    def init(self) -> None:
        """
        Initialize a box shadow draw descriptor. 
        

        :returns: 
        :rtype: None
        """
        ...



class _type_draw_glyph_dsc_t(TypedDict, total=False):
    pass


class draw_glyph_dsc_t(Struct):
    
    def __init__(self, *, kwargs: _type_draw_glyph_dsc_t = dict()):
        ...

    def init(self) -> None:
        """
        Initialize a glyph draw descriptor. Used internally. 
        

        :returns: 
        :rtype: None
        """
        ...



class _type_draw_unit_t(TypedDict, total=False):
    pass


class draw_unit_t(Struct):
    
    def __init__(self, *, kwargs: _type_draw_unit_t = dict()):
        ...

    def label_iterate_characters(self, dsc: "draw_label_dsc_t", coords: "area_t", cb: "draw_glyph_cb_t") -> None:
        """
        Should be used during rendering the characters to get the position and other parameters of the characters 
        
        :param dsc: pointer to draw descriptor 
        :type dsc: "draw_label_dsc_t"
        :param coords: coordinates of the label 
        :type coords: "area_t"
        :param cb: a callback to call to draw each glyphs one by one 
        :type cb: "draw_glyph_cb_t"

        :returns: 
        :rtype: None
        """
        ...

    def sw_fill(self, dsc: "draw_fill_dsc_t", coords: "area_t") -> None:
        """
        Fill an area using SW render. Handle gradient and radius. 
        
        :param dsc: the draw descriptor 
        :type dsc: "draw_fill_dsc_t"
        :param coords: the coordinates of the rectangle 
        :type coords: "area_t"

        :returns: 
        :rtype: None
        """
        ...

    def sw_border(self, dsc: "draw_border_dsc_t", coords: "area_t") -> None:
        """
        Draw border with SW render. 
        
        :param dsc: the draw descriptor 
        :type dsc: "draw_border_dsc_t"
        :param coords: the coordinates of the rectangle 
        :type coords: "area_t"

        :returns: 
        :rtype: None
        """
        ...

    def sw_box_shadow(self, dsc: "draw_box_shadow_dsc_t", coords: "area_t") -> None:
        """
        Draw box shadow with SW render. 
        
        :param dsc: the draw descriptor 
        :type dsc: "draw_box_shadow_dsc_t"
        :param coords: the coordinates of the rectangle for which the box shadow should be drawn 
        :type coords: "area_t"

        :returns: 
        :rtype: None
        """
        ...

    def sw_image(self, draw_dsc: "draw_image_dsc_t", coords: "area_t") -> None:
        """
        Draw an image with SW render. It handles image decoding, tiling, transformations, and recoloring. 
        
        :param draw_dsc: the draw descriptor 
        :type draw_dsc: "draw_image_dsc_t"
        :param coords: the coordinates of the image 
        :type coords: "area_t"

        :returns: 
        :rtype: None
        """
        ...

    def sw_label(self, dsc: "draw_label_dsc_t", coords: "area_t") -> None:
        """
        Draw a label with SW render. 
        
        :param dsc: the draw descriptor 
        :type dsc: "draw_label_dsc_t"
        :param coords: the coordinates of the label 
        :type coords: "area_t"

        :returns: 
        :rtype: None
        """
        ...

    def sw_arc(self, dsc: "draw_arc_dsc_t", coords: "area_t") -> None:
        """
        Draw an arc with SW render. 
        
        :param dsc: the draw descriptor 
        :type dsc: "draw_arc_dsc_t"
        :param coords: the coordinates of the arc 
        :type coords: "area_t"

        :returns: 
        :rtype: None
        """
        ...

    def sw_line(self, dsc: "draw_line_dsc_t") -> None:
        """
        Draw a line with SW render. 
        
        :param dsc: the draw descriptor 
        :type dsc: "draw_line_dsc_t"

        :returns: 
        :rtype: None
        """
        ...

    def sw_layer(self, draw_dsc: "draw_image_dsc_t", coords: "area_t") -> None:
        """
        Blend a layer with SW render 
        
        :param draw_dsc: the draw descriptor 
        :type draw_dsc: "draw_image_dsc_t"
        :param coords: the coordinates of the layer 
        :type coords: "area_t"

        :returns: 
        :rtype: None
        """
        ...

    def sw_triangle(self, dsc: "draw_triangle_dsc_t") -> None:
        """
        Draw a triangle with SW render. 
        
        :param dsc: the draw descriptor 
        :type dsc: "draw_triangle_dsc_t"

        :returns: 
        :rtype: None
        """
        ...

    def sw_mask_rect(self, dsc: "draw_mask_rect_dsc_t", coords: "area_t") -> None:
        """
        Mask out a rectangle with radius from a current layer 
        
        :param dsc: the draw descriptor 
        :type dsc: "draw_mask_rect_dsc_t"
        :param coords: the coordinates of the mask 
        :type coords: "area_t"

        :returns: 
        :rtype: None
        """
        ...

    def sw_transform(self, dest_area: "area_t", src_buf: Any, src_w: int, src_h: int, src_stride: int, draw_dsc: "draw_image_dsc_t", sup: "draw_image_sup_t", cf: color_format_t, dest_buf: Any) -> None:
        """
        Used internally to get a transformed are of an image 
        
        :param dest_area: area to calculate, i.e. get this area from the transformed image 
        :type dest_area: "area_t"
        :param src_buf: source buffer 
        :type src_buf: Any
        :param src_w: source buffer width in pixels 
        :type src_w: int
        :param src_h: source buffer height in pixels 
        :type src_h: int
        :param src_stride: source buffer stride in bytes 
        :type src_stride: int
        :param draw_dsc: draw descriptor 
        :type draw_dsc: "draw_image_dsc_t"
        :param sup: supplementary data 
        :type sup: "draw_image_sup_t"
        :param cf: color format of the source buffer 
        :type cf: color_format_t
        :param dest_buf: the destination buffer 
        :type dest_buf: Any

        :returns: 
        :rtype: None
        """
        ...

    def sw_blend(self, dsc: "draw_sw_blend_dsc_t") -> None:
        """
        Call the blend function of the layer . 
        
        :param dsc: pointer to an initialized blend descriptor 
        :type dsc: "draw_sw_blend_dsc_t"

        :returns: 
        :rtype: None
        """
        ...



class _type_indev_t(TypedDict, total=False):
    pass


class indev_t(Struct):
    
    def __init__(self, *, kwargs: _type_indev_t = dict()):
        ...

    def delete(self) -> None:
        """
        Remove the provided input device. Make sure not to use the provided input device afterwards anymore. 
        

        :returns: 
        :rtype: None
        """
        ...

    def get_next(self) -> "indev_t":
        """
        Get the next input device. the next input device or NULL if there are no more. Provide the first input device when the parameter is NULL 
        

        :returns: the next input device or NULL if there are no more. Provide the first input device when the parameter is NULL 
        :rtype: "indev_t"
        """
        ...

    def read(self) -> None:
        """
        Read data from an input device. 
        

        :returns: 
        :rtype: None
        """
        ...

    def enable(self, enable: bool) -> None:
        """
        Enable or disable one or all input devices (default enabled) 
        
        :param enable: true to enable, false to disable 
        :type enable: bool

        :returns: 
        :rtype: None
        """
        ...

    def set_type(self, indev_type: indev_type_t) -> None:
        """
        Set the type of an input device 
        
        :param indev_type: the type of the input device from lv_indev_type_t ( LV_INDEV_TYPE_... ) 
        :type indev_type: indev_type_t

        :returns: 
        :rtype: None
        """
        ...

    def set_read_cb(self, read_cb: Callable[["indev_t", "indev_data_t"], None]) -> None:
        """
        Set a callback function to read input device data to the indev 
        
        :param read_cb: pointer to callback function to read input device data 
        :type read_cb: Callable[["indev_t", "indev_data_t"], None]

        :returns: 
        :rtype: None
        """
        ...

    def set_user_data(self, indev: "indev_t") -> None:
        """
        Set user data to the indev 
        
        :param indev: pointer to user data 
        :type indev: "indev_t"

        :returns: 
        :rtype: None
        """
        ...

    def set_driver_data(self, indev: "indev_t") -> None:
        """
        Set driver data to the indev 
        
        :param indev: pointer to driver data 
        :type indev: "indev_t"

        :returns: 
        :rtype: None
        """
        ...

    def set_display(self, disp: "display_t") -> None:
        """
        Assign a display to the indev 
        
        :param disp: pointer to an display 
        :type disp: "display_t"

        :returns: 
        :rtype: None
        """
        ...

    def set_long_press_time(self, long_press_time: int) -> None:
        """
        Set long press time to indev 
        
        :param long_press_time: time long press time in ms 
        :type long_press_time: int

        :returns: 
        :rtype: None
        """
        ...

    def set_scroll_limit(self, scroll_limit: int) -> None:
        """
        Set scroll limit to the input device 
        
        :param scroll_limit: the number of pixels to slide before actually drag the object 
        :type scroll_limit: int

        :returns: 
        :rtype: None
        """
        ...

    def set_scroll_throw(self, scroll_limit: int) -> None:
        """
        Set scroll throw slow-down to the indev. Greater value means faster slow-down 
        
        :param scroll_limit: the slow-down in [%] 
        :type scroll_limit: int

        :returns: 
        :rtype: None
        """
        ...

    def get_type(self) -> "indev_type_t":
        """
        Get the type of an input device the type of the input device from lv_hal_indev_type_t ( LV_INDEV_TYPE_... ) 
        

        :returns: the type of the input device from lv_hal_indev_type_t ( LV_INDEV_TYPE_... ) 
        :rtype: "indev_type_t"
        """
        ...

    def get_read_cb(self) -> "indev_read_cb_t":
        """
        Get the callback function to read input device data to the indev Pointer to callback function to read input device data or NULL if indev is NULL 
        

        :returns: Pointer to callback function to read input device data or NULL if indev is NULL 
        :rtype: "indev_read_cb_t"
        """
        ...

    def get_state(self) -> "indev_state_t":
        """
        Get the indev state Indev state or LV_INDEV_STATE_RELEASED if indev is NULL 
        

        :returns: Indev state or LV_INDEV_STATE_RELEASED if indev is NULL 
        :rtype: "indev_state_t"
        """
        ...

    def get_group(self) -> "group_t":
        """
        Get the indev assigned group Pointer to indev assigned group or NULL if indev is NULL 
        

        :returns: Pointer to indev assigned group or NULL if indev is NULL 
        :rtype: "group_t"
        """
        ...

    def get_display(self) -> "display_t":
        """
        Get a pointer to the assigned display of the indev pointer to the assigned display or NULL if indev is NULL 
        

        :returns: pointer to the assigned display or NULL if indev is NULL 
        :rtype: "display_t"
        """
        ...

    def get_user_data(self) -> Any:
        """
        Get a pointer to the user data of the indev pointer to the user data or NULL if indev is NULL 
        

        :returns: pointer to the user data or NULL if indev is NULL 
        :rtype: Any
        """
        ...

    def get_driver_data(self) -> Any:
        """
        Get a pointer to the driver data of the indev pointer to the driver data or NULL if indev is NULL 
        

        :returns: pointer to the driver data or NULL if indev is NULL 
        :rtype: Any
        """
        ...

    def get_press_moved(self) -> bool:
        """
        Get whether indev is moved while pressed true: indev is moved while pressed; false: indev is not moved while pressed 
        

        :returns: true: indev is moved while pressed; false: indev is not moved while pressed 
        :rtype: bool
        """
        ...

    def reset(self, obj: "obj") -> None:
        """
        Reset one or all input devices 
        
        :param obj: pointer to an object which triggers the reset. 
        :type obj: "obj"

        :returns: 
        :rtype: None
        """
        ...

    def stop_processing(self) -> None:
        """
        Touch and key related events are sent to the input device first and to the widget after that. If this functions called in an indev event, the event won't be sent to the widget. 
        

        :returns: 
        :rtype: None
        """
        ...

    def reset_long_press(self) -> None:
        """
        Reset the long press state of an input device 
        

        :returns: 
        :rtype: None
        """
        ...

    def set_cursor(self, obj: "obj") -> None:
        """
        Set a cursor for a pointer input device (for LV_INPUT_TYPE_POINTER and LV_INPUT_TYPE_BUTTON) 
        
        :param obj: pointer to an object to be used as cursor 
        :type obj: "obj"

        :returns: 
        :rtype: None
        """
        ...

    def set_group(self, group: "group_t") -> None:
        """
        Set a destination group for a keypad input device (for LV_INDEV_TYPE_KEYPAD) 
        
        :param group: pointer to a group 
        :type group: "group_t"

        :returns: 
        :rtype: None
        """
        ...

    def set_button_points(self, points: List["point_t"]) -> None:
        """
        Set the an array of points for LV_INDEV_TYPE_BUTTON. These points will be assigned to the buttons to press a specific point on the screen 
        
        :param points: array of points 
        :type points: List["point_t"]

        :returns: 
        :rtype: None
        """
        ...

    def get_point(self, point: "point_t") -> None:
        """
        Get the last point of an input device (for LV_INDEV_TYPE_POINTER and LV_INDEV_TYPE_BUTTON) 
        
        :param point: pointer to a point to store the result 
        :type point: "point_t"

        :returns: 
        :rtype: None
        """
        ...

    def get_gesture_dir(self) -> "dir_t":
        """
        Get the current gesture direct current gesture direct 
        

        :returns: current gesture direct 
        :rtype: "dir_t"
        """
        ...

    def get_key(self) -> int:
        """
        Get the last pressed key of an input device (for LV_INDEV_TYPE_KEYPAD) the last pressed key (0 on error) 
        

        :returns: the last pressed key (0 on error) 
        :rtype: int
        """
        ...

    def get_scroll_dir(self) -> "dir_t":
        """
        Check the current scroll direction of an input device (for LV_INDEV_TYPE_POINTER and LV_INDEV_TYPE_BUTTON) LV_DIR_NONE: no scrolling now LV_DIR_HOR/VER 
        

        :returns: LV_DIR_NONE: no scrolling now LV_DIR_HOR/VER 
        :rtype: "dir_t"
        """
        ...

    def get_scroll_obj(self) -> "obj":
        """
        Get the currently scrolled object (for LV_INDEV_TYPE_POINTER and LV_INDEV_TYPE_BUTTON) pointer to the currently scrolled object or NULL if no scrolling by this indev 
        

        :returns: pointer to the currently scrolled object or NULL if no scrolling by this indev 
        :rtype: "obj"
        """
        ...

    def get_vect(self, point: "point_t") -> None:
        """
        Get the movement vector of an input device (for LV_INDEV_TYPE_POINTER and LV_INDEV_TYPE_BUTTON) 
        
        :param point: pointer to a point to store the types.pointer.vector 
        :type point: "point_t"

        :returns: 
        :rtype: None
        """
        ...

    def wait_release(self) -> None:
        """
        Do nothing until the next release 
        

        :returns: 
        :rtype: None
        """
        ...

    def get_read_timer(self) -> "timer_t":
        """
        Get a pointer to the indev read timer to modify its parameters with lv_timer_... functions. pointer to the indev read refresher timer. (NULL on error) 
        

        :returns: pointer to the indev read refresher timer. (NULL on error) 
        :rtype: "timer_t"
        """
        ...

    def set_mode(self, mode: indev_mode_t) -> None:
        """
        Set the input device's event model: event-driven mode or timer mode. 
        
        :param mode: the mode of input device 
        :type mode: indev_mode_t

        :returns: 
        :rtype: None
        """
        ...

    def get_mode(self) -> "indev_mode_t":
        """
        Get the input device's running mode. the running mode for the specified input device. 
        

        :returns: the running mode for the specified input device. 
        :rtype: "indev_mode_t"
        """
        ...

    def add_event_cb(self, event_cb: Callable[["event_t"], None], filter: "event_code_t", indev: "indev_t") -> None:
        """
        Add an event handler to the indev 
        
        :param event_cb: an event callback 
        :type event_cb: Callable[["event_t"], None]
        :param filter: event code to react or LV_EVENT_ALL 
        :type filter: "event_code_t"
        :param indev: optional user_data 
        :type indev: "indev_t"

        :returns: 
        :rtype: None
        """
        ...

    def get_event_count(self) -> int:
        """
        Get the number of event attached to an indev number of events 
        

        :returns: number of events 
        :rtype: int
        """
        ...

    def get_event_dsc(self, index: int) -> "event_dsc_t":
        """
        Get an event descriptor for an event the event descriptor 
        
        :param index: the index of the event 
        :type index: int

        :returns: the event descriptor 
        :rtype: "event_dsc_t"
        """
        ...

    def remove_event(self, index: int) -> bool:
        """
        Remove an event true: and event was removed; false: no event was removed 
        
        :param index: the index of the event to remove 
        :type index: int

        :returns: true: and event was removed; false: no event was removed 
        :rtype: bool
        """
        ...

    def remove_event_cb_with_user_data(self, event_cb: Callable[["event_t"], None], indev: "indev_t") -> int:
        """
        Remove an event_cb with user_data the count of the event removed 
        
        :param event_cb: the event_cb of the event to remove 
        :type event_cb: Callable[["event_t"], None]
        :param indev: user_data 
        :type indev: "indev_t"

        :returns: the count of the event removed 
        :rtype: int
        """
        ...

    def send_event(self, code: "event_code_t", param: Any) -> "result_t":
        """
        Send an event to an indev LV_RESULT_OK: indev wasn't deleted in the event. 
        
        :param code: an event code. LV_EVENT_... 
        :type code: "event_code_t"
        :param param: optional param 
        :type param: Any

        :returns: LV_RESULT_OK: indev wasn't deleted in the event. 
        :rtype: "result_t"
        """
        ...



class _type_draw_triangle_dsc_t(TypedDict, total=False):
    base: "draw_dsc_base_t"
    bg_opa: "opa_t"
    bg_color: "color_t"
    bg_grad: "grad_dsc_t"
    p: List["point_precise_t"]


class draw_triangle_dsc_t(Struct):

    __SIZE__: ClassVar[int] = ...
    
    def __init__(self, *, kwargs: _type_draw_triangle_dsc_t = dict()):
        ...

    @property
    def base(self) -> "draw_dsc_base_t":
        """
        :type value: "draw_dsc_base_t"
        :rtype: "draw_dsc_base_t"
        """
    
        ...    

    @base.setter
    def base(self, value: "draw_dsc_base_t"):
        ...    

    @property
    def bg_opa(self) -> "opa_t":
        """
        :type value: "opa_t"
        :rtype: "opa_t"
        """
    
        ...    

    @bg_opa.setter
    def bg_opa(self, value: "opa_t"):
        ...    

    @property
    def bg_color(self) -> "color_t":
        """
        :type value: "color_t"
        :rtype: "color_t"
        """
    
        ...    

    @bg_color.setter
    def bg_color(self, value: "color_t"):
        ...    

    @property
    def bg_grad(self) -> "grad_dsc_t":
        """
        :type value: "grad_dsc_t"
        :rtype: "grad_dsc_t"
        """
    
        ...    

    @bg_grad.setter
    def bg_grad(self, value: "grad_dsc_t"):
        ...    

    @property
    def p(self) -> List["point_precise_t"]:
        """
        :type value: List["point_precise_t"]
        :rtype: List["point_precise_t"]
        """
    
        ...    

    @p.setter
    def p(self, value: List["point_precise_t"]):
        ...    


    def init(self) -> None:
        """
        Initialize a triangle draw descriptor 
        

        :returns: 
        :rtype: None
        """
        ...



class _type_draw_sw_mask_line_param_t(TypedDict, total=False):
    pass


class draw_sw_mask_line_param_t(Struct):
    
    def __init__(self, *, kwargs: _type_draw_sw_mask_line_param_t = dict()):
        ...

    def points_init(self, p1x: int, p1y: int, p2x: int, p2y: int, side: draw_sw_mask_line_side_t) -> None:
        """
        Initialize a line mask from two points. 
        
        :param p1x: X coordinate of the first point of the line 
        :type p1x: int
        :param p1y: Y coordinate of the first point of the line 
        :type p1y: int
        :param p2x: X coordinate of the second point of the line 
        :type p2x: int
        :param p2y: y coordinate of the second point of the line 
        :type p2y: int
        :param side: and element of lv_draw_mask_line_side_t to describe which side to keep. With LV_DRAW_MASK_LINE_SIDE_LEFT/RIGHT and horizontal line all pixels are kept With LV_DRAW_MASK_LINE_SIDE_TOP/BOTTOM and vertical line all pixels are kept 
        :type side: draw_sw_mask_line_side_t

        :returns: 
        :rtype: None
        """
        ...

    def angle_init(self, px: int, py: int, angle: int, side: draw_sw_mask_line_side_t) -> None:
        """
        Initialize a line mask from a point and an angle. 
        
        :param px: X coordinate of a point of the line 
        :type px: int
        :param py: X coordinate of a point of the line 
        :type py: int
        :param angle: right 0 deg, bottom: 90 
        :type angle: int
        :param side: an element of lv_draw_mask_line_side_t to describe which side to keep. With LV_DRAW_MASK_LINE_SIDE_LEFT/RIGHT and horizontal line all pixels are kept With LV_DRAW_MASK_LINE_SIDE_TOP/BOTTOM and vertical line all pixels are kept 
        :type side: draw_sw_mask_line_side_t

        :returns: 
        :rtype: None
        """
        ...



class _type_draw_sw_mask_angle_param_t(TypedDict, total=False):
    pass


class draw_sw_mask_angle_param_t(Struct):
    
    def __init__(self, *, kwargs: _type_draw_sw_mask_angle_param_t = dict()):
        ...

    def init(self, vertex_x: int, vertex_y: int, start_angle: int, end_angle: int) -> None:
        """
        Initialize an angle mask. 
        
        :param vertex_x: X coordinate of the angle vertex (absolute coordinates) 
        :type vertex_x: int
        :param vertex_y: Y coordinate of the angle vertex (absolute coordinates) 
        :type vertex_y: int
        :param start_angle: start angle in degrees. 0 deg on the right, 90 deg, on the bottom 
        :type start_angle: int
        :param end_angle: end angle 
        :type end_angle: int

        :returns: 
        :rtype: None
        """
        ...



class _type_draw_sw_mask_radius_param_t(TypedDict, total=False):
    pass


class draw_sw_mask_radius_param_t(Struct):
    
    def __init__(self, *, kwargs: _type_draw_sw_mask_radius_param_t = dict()):
        ...

    def init(self, rect: "area_t", radius: int, inv: bool) -> None:
        """
        Initialize a fade mask. 
        
        :param rect: coordinates of the rectangle to affect (absolute coordinates) 
        :type rect: "area_t"
        :param radius: radius of the rectangle 
        :type radius: int
        :param inv: true: keep the pixels inside the rectangle; keep the pixels outside of the rectangle 
        :type inv: bool

        :returns: 
        :rtype: None
        """
        ...



class _type_draw_sw_mask_fade_param_t(TypedDict, total=False):
    pass


class draw_sw_mask_fade_param_t(Struct):
    
    def __init__(self, *, kwargs: _type_draw_sw_mask_fade_param_t = dict()):
        ...

    def init(self, coords: "area_t", opa_top: opa_t, y_top: int, opa_bottom: opa_t, y_bottom: int) -> None:
        """
        Initialize a fade mask. 
        
        :param coords: coordinates of the area to affect (absolute coordinates) 
        :type coords: "area_t"
        :param opa_top: opacity on the top 
        :type opa_top: opa_t
        :param y_top: at which coordinate start to change to opacity to opa_bottom 
        :type y_top: int
        :param opa_bottom: opacity at the bottom 
        :type opa_bottom: opa_t
        :param y_bottom: at which coordinate reach opa_bottom . 
        :type y_bottom: int

        :returns: 
        :rtype: None
        """
        ...



class _type_draw_sw_mask_map_param_t(TypedDict, total=False):
    pass


class draw_sw_mask_map_param_t(Struct):
    
    def __init__(self, *, kwargs: _type_draw_sw_mask_map_param_t = dict()):
        ...

    def init(self, coords: "area_t", map: opa_t) -> None:
        """
        Initialize a map mask. 
        
        :param coords: coordinates of the map (absolute coordinates) 
        :type coords: "area_t"
        :param map: array of bytes with the mask values 
        :type map: opa_t

        :returns: 
        :rtype: None
        """
        ...



class _type_theme_t(TypedDict, total=False):
    pass


class theme_t(Struct):
    
    def __init__(self, *, kwargs: _type_theme_t = dict()):
        ...

    def set_parent(self, parent: "theme_t") -> None:
        """
        Set a base theme for a theme. The styles from the base them will be added before the styles of the current theme. Arbitrary long chain of themes can be created by setting base themes. 
        
        :param parent: pointer to the base theme 
        :type parent: "theme_t"

        :returns: 
        :rtype: None
        """
        ...

    def set_apply_cb(self, apply_cb: Callable[["theme_t", "obj"], None]) -> None:
        """
        Set an apply callback for a theme. The apply callback is used to add styles to different objects 
        
        :param apply_cb: pointer to the callback 
        :type apply_cb: Callable[["theme_t", "obj"], None]

        :returns: 
        :rtype: None
        """
        ...



class _type_color_hsv_t(TypedDict, total=False):
    h: int
    s: int
    v: int


class color_hsv_t(Struct):

    __SIZE__: ClassVar[int] = ...
    
    def __init__(self, *, kwargs: _type_color_hsv_t = dict()):
        ...

    @property
    def h(self) -> int:
        """
        :type value: int
        :rtype: int
        """
    
        ...    

    @h.setter
    def h(self, value: int):
        ...    

    @property
    def s(self) -> int:
        """
        :type value: int
        :rtype: int
        """
    
        ...    

    @s.setter
    def s(self, value: int):
        ...    

    @property
    def v(self) -> int:
        """
        :type value: int
        :rtype: int
        """
    
        ...    

    @v.setter
    def v(self, value: int):
        ...    



class _type_hit_test_info_t(TypedDict, total=False):
    pass


class hit_test_info_t(Struct):
    
    def __init__(self, *, kwargs: _type_hit_test_info_t = dict()):
        ...


class _type_draw_mask_rect_dsc_t(TypedDict, total=False):
    pass


class draw_mask_rect_dsc_t(Struct):
    
    def __init__(self, *, kwargs: _type_draw_mask_rect_dsc_t = dict()):
        ...


class _type_draw_sw_blend_dsc_t(TypedDict, total=False):
    pass


class draw_sw_blend_dsc_t(Struct):
    
    def __init__(self, *, kwargs: _type_draw_sw_blend_dsc_t = dict()):
        ...


class _type_indev_data_t(TypedDict, total=False):
    point: "point_t"
    key: int
    btn_id: int
    enc_diff: int
    state: "indev_state_t"
    continue_reading: bool


class indev_data_t(Struct):

    __SIZE__: ClassVar[int] = ...
    
    def __init__(self, *, kwargs: _type_indev_data_t = dict()):
        ...

    @property
    def point(self) -> "point_t":
        """
        :type value: "point_t"
        :rtype: "point_t"
        """
    
        ...    

    @point.setter
    def point(self, value: "point_t"):
        ...    

    @property
    def key(self) -> int:
        """
        :type value: int
        :rtype: int
        """
    
        ...    

    @key.setter
    def key(self, value: int):
        ...    

    @property
    def btn_id(self) -> int:
        """
        :type value: int
        :rtype: int
        """
    
        ...    

    @btn_id.setter
    def btn_id(self, value: int):
        ...    

    @property
    def enc_diff(self) -> int:
        """
        :type value: int
        :rtype: int
        """
    
        ...    

    @enc_diff.setter
    def enc_diff(self, value: int):
        ...    

    @property
    def state(self) -> "indev_state_t":
        """
        :type value: "indev_state_t"
        :rtype: "indev_state_t"
        """
    
        ...    

    @state.setter
    def state(self, value: "indev_state_t"):
        ...    

    @property
    def continue_reading(self) -> bool:
        """
        :type value: bool
        :rtype: bool
        """
    
        ...    

    @continue_reading.setter
    def continue_reading(self, value: bool):
        ...    



class _type_sqrt_res_t(TypedDict, total=False):
    i: int
    f: int


class sqrt_res_t(Struct):

    __SIZE__: ClassVar[int] = ...
    
    def __init__(self, *, kwargs: _type_sqrt_res_t = dict()):
        ...

    @property
    def i(self) -> int:
        """
        :type value: int
        :rtype: int
        """
    
        ...    

    @i.setter
    def i(self, value: int):
        ...    

    @property
    def f(self) -> int:
        """
        :type value: int
        :rtype: int
        """
    
        ...    

    @f.setter
    def f(self, value: int):
        ...    



class obj(Struct):

    class TREE_WALK(object):

        NEXT: ClassVar[int] = ...
        SKIP_CHILDREN: ClassVar[int] = ...
        END: ClassVar[int] = ...
        
        def __init__(self, *, parent: "obj"):
            ...

    class POINT_TRANSFORM_FLAG(object):

        NONE: ClassVar[int] = ...
        RECURSIVE: ClassVar[int] = ...
        INVERSE: ClassVar[int] = ...
        INVERSE_RECURSIVE: ClassVar[int] = ...
        
        def __init__(self, *, parent: "obj"):
            ...

    class CLASS_EDITABLE(object):

        INHERIT: ClassVar[int] = ...
        TRUE: ClassVar[int] = ...
        FALSE: ClassVar[int] = ...
        
        def __init__(self, *, parent: "obj"):
            ...

    class CLASS_GROUP_DEF(object):

        INHERIT: ClassVar[int] = ...
        TRUE: ClassVar[int] = ...
        FALSE: ClassVar[int] = ...
        
        def __init__(self, *, parent: "obj"):
            ...

    class CLASS_THEME_INHERITABLE(object):

        FALSE: ClassVar[int] = ...
        TRUE: ClassVar[int] = ...
        
        def __init__(self, *, parent: "obj"):
            ...

    class FLAG(object):

        HIDDEN: ClassVar[int] = ...
        CLICKABLE: ClassVar[int] = ...
        CLICK_FOCUSABLE: ClassVar[int] = ...
        CHECKABLE: ClassVar[int] = ...
        SCROLLABLE: ClassVar[int] = ...
        SCROLL_ELASTIC: ClassVar[int] = ...
        SCROLL_MOMENTUM: ClassVar[int] = ...
        SCROLL_ONE: ClassVar[int] = ...
        SCROLL_CHAIN_HOR: ClassVar[int] = ...
        SCROLL_CHAIN_VER: ClassVar[int] = ...
        SCROLL_CHAIN: ClassVar[int] = ...
        SCROLL_ON_FOCUS: ClassVar[int] = ...
        SCROLL_WITH_ARROW: ClassVar[int] = ...
        SNAPPABLE: ClassVar[int] = ...
        PRESS_LOCK: ClassVar[int] = ...
        EVENT_BUBBLE: ClassVar[int] = ...
        GESTURE_BUBBLE: ClassVar[int] = ...
        ADV_HITTEST: ClassVar[int] = ...
        IGNORE_LAYOUT: ClassVar[int] = ...
        FLOATING: ClassVar[int] = ...
        SEND_DRAW_TASK_EVENTS: ClassVar[int] = ...
        OVERFLOW_VISIBLE: ClassVar[int] = ...
        FLEX_IN_NEW_TRACK: ClassVar[int] = ...
        LAYOUT_1: ClassVar[int] = ...
        LAYOUT_2: ClassVar[int] = ...
        WIDGET_1: ClassVar[int] = ...
        WIDGET_2: ClassVar[int] = ...
        USER_1: ClassVar[int] = ...
        USER_2: ClassVar[int] = ...
        USER_3: ClassVar[int] = ...
        USER_4: ClassVar[int] = ...
        
        def __init__(self, *, parent: "obj"):
            ...

    
    def __init__(self, *, parent: "obj"):
        """
        Create a base object (a rectangle) pointer to the new object 
        """
        ...

    def style_get_selector_state(self) -> "state_t":
        """

        :returns: 
        :rtype: "state_t"
        """
        ...

    def style_get_selector_part(self) -> "part_t":
        """

        :returns: 
        :rtype: "part_t"
        """
        ...

    def get_style_width(self, part: part_t) -> int:
        """
        :param part: 
        :type part: part_t

        :returns: 
        :rtype: int
        """
        ...

    def get_style_min_width(self, part: part_t) -> int:
        """
        :param part: 
        :type part: part_t

        :returns: 
        :rtype: int
        """
        ...

    def get_style_max_width(self, part: part_t) -> int:
        """
        :param part: 
        :type part: part_t

        :returns: 
        :rtype: int
        """
        ...

    def get_style_height(self, part: part_t) -> int:
        """
        :param part: 
        :type part: part_t

        :returns: 
        :rtype: int
        """
        ...

    def get_style_min_height(self, part: part_t) -> int:
        """
        :param part: 
        :type part: part_t

        :returns: 
        :rtype: int
        """
        ...

    def get_style_max_height(self, part: part_t) -> int:
        """
        :param part: 
        :type part: part_t

        :returns: 
        :rtype: int
        """
        ...

    def get_style_length(self, part: part_t) -> int:
        """
        :param part: 
        :type part: part_t

        :returns: 
        :rtype: int
        """
        ...

    def get_style_x(self, part: part_t) -> int:
        """
        :param part: 
        :type part: part_t

        :returns: 
        :rtype: int
        """
        ...

    def get_style_y(self, part: part_t) -> int:
        """
        :param part: 
        :type part: part_t

        :returns: 
        :rtype: int
        """
        ...

    def get_style_align(self, part: part_t) -> "align_t":
        """
        :param part: 
        :type part: part_t

        :returns: 
        :rtype: "align_t"
        """
        ...

    def get_style_transform_width(self, part: part_t) -> int:
        """
        :param part: 
        :type part: part_t

        :returns: 
        :rtype: int
        """
        ...

    def get_style_transform_height(self, part: part_t) -> int:
        """
        :param part: 
        :type part: part_t

        :returns: 
        :rtype: int
        """
        ...

    def get_style_translate_x(self, part: part_t) -> int:
        """
        :param part: 
        :type part: part_t

        :returns: 
        :rtype: int
        """
        ...

    def get_style_translate_y(self, part: part_t) -> int:
        """
        :param part: 
        :type part: part_t

        :returns: 
        :rtype: int
        """
        ...

    def get_style_transform_scale_x(self, part: part_t) -> int:
        """
        :param part: 
        :type part: part_t

        :returns: 
        :rtype: int
        """
        ...

    def get_style_transform_scale_y(self, part: part_t) -> int:
        """
        :param part: 
        :type part: part_t

        :returns: 
        :rtype: int
        """
        ...

    def get_style_transform_rotation(self, part: part_t) -> int:
        """
        :param part: 
        :type part: part_t

        :returns: 
        :rtype: int
        """
        ...

    def get_style_transform_pivot_x(self, part: part_t) -> int:
        """
        :param part: 
        :type part: part_t

        :returns: 
        :rtype: int
        """
        ...

    def get_style_transform_pivot_y(self, part: part_t) -> int:
        """
        :param part: 
        :type part: part_t

        :returns: 
        :rtype: int
        """
        ...

    def get_style_transform_skew_x(self, part: part_t) -> int:
        """
        :param part: 
        :type part: part_t

        :returns: 
        :rtype: int
        """
        ...

    def get_style_transform_skew_y(self, part: part_t) -> int:
        """
        :param part: 
        :type part: part_t

        :returns: 
        :rtype: int
        """
        ...

    def get_style_pad_top(self, part: part_t) -> int:
        """
        :param part: 
        :type part: part_t

        :returns: 
        :rtype: int
        """
        ...

    def get_style_pad_bottom(self, part: part_t) -> int:
        """
        :param part: 
        :type part: part_t

        :returns: 
        :rtype: int
        """
        ...

    def get_style_pad_left(self, part: part_t) -> int:
        """
        :param part: 
        :type part: part_t

        :returns: 
        :rtype: int
        """
        ...

    def get_style_pad_right(self, part: part_t) -> int:
        """
        :param part: 
        :type part: part_t

        :returns: 
        :rtype: int
        """
        ...

    def get_style_pad_row(self, part: part_t) -> int:
        """
        :param part: 
        :type part: part_t

        :returns: 
        :rtype: int
        """
        ...

    def get_style_pad_column(self, part: part_t) -> int:
        """
        :param part: 
        :type part: part_t

        :returns: 
        :rtype: int
        """
        ...

    def get_style_margin_top(self, part: part_t) -> int:
        """
        :param part: 
        :type part: part_t

        :returns: 
        :rtype: int
        """
        ...

    def get_style_margin_bottom(self, part: part_t) -> int:
        """
        :param part: 
        :type part: part_t

        :returns: 
        :rtype: int
        """
        ...

    def get_style_margin_left(self, part: part_t) -> int:
        """
        :param part: 
        :type part: part_t

        :returns: 
        :rtype: int
        """
        ...

    def get_style_margin_right(self, part: part_t) -> int:
        """
        :param part: 
        :type part: part_t

        :returns: 
        :rtype: int
        """
        ...

    def get_style_bg_color(self, part: part_t) -> "color_t":
        """
        :param part: 
        :type part: part_t

        :returns: 
        :rtype: "color_t"
        """
        ...

    def get_style_bg_color_filtered(self, part: part_t) -> "color_t":
        """
        :param part: 
        :type part: part_t

        :returns: 
        :rtype: "color_t"
        """
        ...

    def get_style_bg_opa(self, part: part_t) -> "opa_t":
        """
        :param part: 
        :type part: part_t

        :returns: 
        :rtype: "opa_t"
        """
        ...

    def get_style_bg_grad_color(self, part: part_t) -> "color_t":
        """
        :param part: 
        :type part: part_t

        :returns: 
        :rtype: "color_t"
        """
        ...

    def get_style_bg_grad_color_filtered(self, part: part_t) -> "color_t":
        """
        :param part: 
        :type part: part_t

        :returns: 
        :rtype: "color_t"
        """
        ...

    def get_style_bg_grad_dir(self, part: part_t) -> "grad_dir_t":
        """
        :param part: 
        :type part: part_t

        :returns: 
        :rtype: "grad_dir_t"
        """
        ...

    def get_style_bg_main_stop(self, part: part_t) -> int:
        """
        :param part: 
        :type part: part_t

        :returns: 
        :rtype: int
        """
        ...

    def get_style_bg_grad_stop(self, part: part_t) -> int:
        """
        :param part: 
        :type part: part_t

        :returns: 
        :rtype: int
        """
        ...

    def get_style_bg_main_opa(self, part: part_t) -> "opa_t":
        """
        :param part: 
        :type part: part_t

        :returns: 
        :rtype: "opa_t"
        """
        ...

    def get_style_bg_grad_opa(self, part: part_t) -> "opa_t":
        """
        :param part: 
        :type part: part_t

        :returns: 
        :rtype: "opa_t"
        """
        ...

    def get_style_bg_grad(self, part: part_t) -> "grad_dsc_t":
        """
        :param part: 
        :type part: part_t

        :returns: 
        :rtype: "grad_dsc_t"
        """
        ...

    def get_style_bg_image_src(self, part: part_t) -> Any:
        """
        :param part: 
        :type part: part_t

        :returns: 
        :rtype: Any
        """
        ...

    def get_style_bg_image_opa(self, part: part_t) -> "opa_t":
        """
        :param part: 
        :type part: part_t

        :returns: 
        :rtype: "opa_t"
        """
        ...

    def get_style_bg_image_recolor(self, part: part_t) -> "color_t":
        """
        :param part: 
        :type part: part_t

        :returns: 
        :rtype: "color_t"
        """
        ...

    def get_style_bg_image_recolor_filtered(self, part: part_t) -> "color_t":
        """
        :param part: 
        :type part: part_t

        :returns: 
        :rtype: "color_t"
        """
        ...

    def get_style_bg_image_recolor_opa(self, part: part_t) -> "opa_t":
        """
        :param part: 
        :type part: part_t

        :returns: 
        :rtype: "opa_t"
        """
        ...

    def get_style_bg_image_tiled(self, part: part_t) -> bool:
        """
        :param part: 
        :type part: part_t

        :returns: 
        :rtype: bool
        """
        ...

    def get_style_border_color(self, part: part_t) -> "color_t":
        """
        :param part: 
        :type part: part_t

        :returns: 
        :rtype: "color_t"
        """
        ...

    def get_style_border_color_filtered(self, part: part_t) -> "color_t":
        """
        :param part: 
        :type part: part_t

        :returns: 
        :rtype: "color_t"
        """
        ...

    def get_style_border_opa(self, part: part_t) -> "opa_t":
        """
        :param part: 
        :type part: part_t

        :returns: 
        :rtype: "opa_t"
        """
        ...

    def get_style_border_width(self, part: part_t) -> int:
        """
        :param part: 
        :type part: part_t

        :returns: 
        :rtype: int
        """
        ...

    def get_style_border_side(self, part: part_t) -> "border_side_t":
        """
        :param part: 
        :type part: part_t

        :returns: 
        :rtype: "border_side_t"
        """
        ...

    def get_style_border_post(self, part: part_t) -> bool:
        """
        :param part: 
        :type part: part_t

        :returns: 
        :rtype: bool
        """
        ...

    def get_style_outline_width(self, part: part_t) -> int:
        """
        :param part: 
        :type part: part_t

        :returns: 
        :rtype: int
        """
        ...

    def get_style_outline_color(self, part: part_t) -> "color_t":
        """
        :param part: 
        :type part: part_t

        :returns: 
        :rtype: "color_t"
        """
        ...

    def get_style_outline_color_filtered(self, part: part_t) -> "color_t":
        """
        :param part: 
        :type part: part_t

        :returns: 
        :rtype: "color_t"
        """
        ...

    def get_style_outline_opa(self, part: part_t) -> "opa_t":
        """
        :param part: 
        :type part: part_t

        :returns: 
        :rtype: "opa_t"
        """
        ...

    def get_style_outline_pad(self, part: part_t) -> int:
        """
        :param part: 
        :type part: part_t

        :returns: 
        :rtype: int
        """
        ...

    def get_style_shadow_width(self, part: part_t) -> int:
        """
        :param part: 
        :type part: part_t

        :returns: 
        :rtype: int
        """
        ...

    def get_style_shadow_offset_x(self, part: part_t) -> int:
        """
        :param part: 
        :type part: part_t

        :returns: 
        :rtype: int
        """
        ...

    def get_style_shadow_offset_y(self, part: part_t) -> int:
        """
        :param part: 
        :type part: part_t

        :returns: 
        :rtype: int
        """
        ...

    def get_style_shadow_spread(self, part: part_t) -> int:
        """
        :param part: 
        :type part: part_t

        :returns: 
        :rtype: int
        """
        ...

    def get_style_shadow_color(self, part: part_t) -> "color_t":
        """
        :param part: 
        :type part: part_t

        :returns: 
        :rtype: "color_t"
        """
        ...

    def get_style_shadow_color_filtered(self, part: part_t) -> "color_t":
        """
        :param part: 
        :type part: part_t

        :returns: 
        :rtype: "color_t"
        """
        ...

    def get_style_shadow_opa(self, part: part_t) -> "opa_t":
        """
        :param part: 
        :type part: part_t

        :returns: 
        :rtype: "opa_t"
        """
        ...

    def get_style_image_opa(self, part: part_t) -> "opa_t":
        """
        :param part: 
        :type part: part_t

        :returns: 
        :rtype: "opa_t"
        """
        ...

    def get_style_image_recolor(self, part: part_t) -> "color_t":
        """
        :param part: 
        :type part: part_t

        :returns: 
        :rtype: "color_t"
        """
        ...

    def get_style_image_recolor_filtered(self, part: part_t) -> "color_t":
        """
        :param part: 
        :type part: part_t

        :returns: 
        :rtype: "color_t"
        """
        ...

    def get_style_image_recolor_opa(self, part: part_t) -> "opa_t":
        """
        :param part: 
        :type part: part_t

        :returns: 
        :rtype: "opa_t"
        """
        ...

    def get_style_line_width(self, part: part_t) -> int:
        """
        :param part: 
        :type part: part_t

        :returns: 
        :rtype: int
        """
        ...

    def get_style_line_dash_width(self, part: part_t) -> int:
        """
        :param part: 
        :type part: part_t

        :returns: 
        :rtype: int
        """
        ...

    def get_style_line_dash_gap(self, part: part_t) -> int:
        """
        :param part: 
        :type part: part_t

        :returns: 
        :rtype: int
        """
        ...

    def get_style_line_rounded(self, part: part_t) -> bool:
        """
        :param part: 
        :type part: part_t

        :returns: 
        :rtype: bool
        """
        ...

    def get_style_line_color(self, part: part_t) -> "color_t":
        """
        :param part: 
        :type part: part_t

        :returns: 
        :rtype: "color_t"
        """
        ...

    def get_style_line_color_filtered(self, part: part_t) -> "color_t":
        """
        :param part: 
        :type part: part_t

        :returns: 
        :rtype: "color_t"
        """
        ...

    def get_style_line_opa(self, part: part_t) -> "opa_t":
        """
        :param part: 
        :type part: part_t

        :returns: 
        :rtype: "opa_t"
        """
        ...

    def get_style_arc_width(self, part: part_t) -> int:
        """
        :param part: 
        :type part: part_t

        :returns: 
        :rtype: int
        """
        ...

    def get_style_arc_rounded(self, part: part_t) -> bool:
        """
        :param part: 
        :type part: part_t

        :returns: 
        :rtype: bool
        """
        ...

    def get_style_arc_color(self, part: part_t) -> "color_t":
        """
        :param part: 
        :type part: part_t

        :returns: 
        :rtype: "color_t"
        """
        ...

    def get_style_arc_color_filtered(self, part: part_t) -> "color_t":
        """
        :param part: 
        :type part: part_t

        :returns: 
        :rtype: "color_t"
        """
        ...

    def get_style_arc_opa(self, part: part_t) -> "opa_t":
        """
        :param part: 
        :type part: part_t

        :returns: 
        :rtype: "opa_t"
        """
        ...

    def get_style_arc_image_src(self, part: part_t) -> Any:
        """
        :param part: 
        :type part: part_t

        :returns: 
        :rtype: Any
        """
        ...

    def get_style_text_color(self, part: part_t) -> "color_t":
        """
        :param part: 
        :type part: part_t

        :returns: 
        :rtype: "color_t"
        """
        ...

    def get_style_text_color_filtered(self, part: part_t) -> "color_t":
        """
        :param part: 
        :type part: part_t

        :returns: 
        :rtype: "color_t"
        """
        ...

    def get_style_text_opa(self, part: part_t) -> "opa_t":
        """
        :param part: 
        :type part: part_t

        :returns: 
        :rtype: "opa_t"
        """
        ...

    def get_style_text_font(self, part: part_t) -> "font_t":
        """
        :param part: 
        :type part: part_t

        :returns: 
        :rtype: "font_t"
        """
        ...

    def get_style_text_letter_space(self, part: part_t) -> int:
        """
        :param part: 
        :type part: part_t

        :returns: 
        :rtype: int
        """
        ...

    def get_style_text_line_space(self, part: part_t) -> int:
        """
        :param part: 
        :type part: part_t

        :returns: 
        :rtype: int
        """
        ...

    def get_style_text_decor(self, part: part_t) -> "text_decor_t":
        """
        :param part: 
        :type part: part_t

        :returns: 
        :rtype: "text_decor_t"
        """
        ...

    def get_style_text_align(self, part: part_t) -> "text_align_t":
        """
        :param part: 
        :type part: part_t

        :returns: 
        :rtype: "text_align_t"
        """
        ...

    def get_style_radius(self, part: part_t) -> int:
        """
        :param part: 
        :type part: part_t

        :returns: 
        :rtype: int
        """
        ...

    def get_style_clip_corner(self, part: part_t) -> bool:
        """
        :param part: 
        :type part: part_t

        :returns: 
        :rtype: bool
        """
        ...

    def get_style_opa(self, part: part_t) -> "opa_t":
        """
        :param part: 
        :type part: part_t

        :returns: 
        :rtype: "opa_t"
        """
        ...

    def get_style_opa_layered(self, part: part_t) -> "opa_t":
        """
        :param part: 
        :type part: part_t

        :returns: 
        :rtype: "opa_t"
        """
        ...

    def get_style_color_filter_dsc(self, part: part_t) -> "color_filter_dsc_t":
        """
        :param part: 
        :type part: part_t

        :returns: 
        :rtype: "color_filter_dsc_t"
        """
        ...

    def get_style_color_filter_opa(self, part: part_t) -> "opa_t":
        """
        :param part: 
        :type part: part_t

        :returns: 
        :rtype: "opa_t"
        """
        ...

    def get_style_anim(self, part: part_t) -> "anim_t":
        """
        :param part: 
        :type part: part_t

        :returns: 
        :rtype: "anim_t"
        """
        ...

    def get_style_anim_duration(self, part: part_t) -> int:
        """
        :param part: 
        :type part: part_t

        :returns: 
        :rtype: int
        """
        ...

    def get_style_transition(self, part: part_t) -> "style_transition_dsc_t":
        """
        :param part: 
        :type part: part_t

        :returns: 
        :rtype: "style_transition_dsc_t"
        """
        ...

    def get_style_blend_mode(self, part: part_t) -> "blend_mode_t":
        """
        :param part: 
        :type part: part_t

        :returns: 
        :rtype: "blend_mode_t"
        """
        ...

    def get_style_layout(self, part: part_t) -> int:
        """
        :param part: 
        :type part: part_t

        :returns: 
        :rtype: int
        """
        ...

    def get_style_base_dir(self, part: part_t) -> "base_dir_t":
        """
        :param part: 
        :type part: part_t

        :returns: 
        :rtype: "base_dir_t"
        """
        ...

    def get_style_bitmap_mask_src(self, part: part_t) -> Any:
        """
        :param part: 
        :type part: part_t

        :returns: 
        :rtype: Any
        """
        ...

    def get_style_rotary_sensitivity(self, part: part_t) -> int:
        """
        :param part: 
        :type part: part_t

        :returns: 
        :rtype: int
        """
        ...

    def get_style_flex_flow(self, part: part_t) -> "flex_flow_t":
        """
        :param part: 
        :type part: part_t

        :returns: 
        :rtype: "flex_flow_t"
        """
        ...

    def get_style_flex_main_place(self, part: part_t) -> "flex_align_t":
        """
        :param part: 
        :type part: part_t

        :returns: 
        :rtype: "flex_align_t"
        """
        ...

    def get_style_flex_cross_place(self, part: part_t) -> "flex_align_t":
        """
        :param part: 
        :type part: part_t

        :returns: 
        :rtype: "flex_align_t"
        """
        ...

    def get_style_flex_track_place(self, part: part_t) -> "flex_align_t":
        """
        :param part: 
        :type part: part_t

        :returns: 
        :rtype: "flex_align_t"
        """
        ...

    def get_style_flex_grow(self, part: part_t) -> int:
        """
        :param part: 
        :type part: part_t

        :returns: 
        :rtype: int
        """
        ...

    def get_style_grid_column_dsc_array(self, part: part_t) -> List[int]:
        """
        :param part: 
        :type part: part_t

        :returns: 
        :rtype: List[int]
        """
        ...

    def get_style_grid_column_align(self, part: part_t) -> "grid_align_t":
        """
        :param part: 
        :type part: part_t

        :returns: 
        :rtype: "grid_align_t"
        """
        ...

    def get_style_grid_row_dsc_array(self, part: part_t) -> List[int]:
        """
        :param part: 
        :type part: part_t

        :returns: 
        :rtype: List[int]
        """
        ...

    def get_style_grid_row_align(self, part: part_t) -> "grid_align_t":
        """
        :param part: 
        :type part: part_t

        :returns: 
        :rtype: "grid_align_t"
        """
        ...

    def get_style_grid_cell_column_pos(self, part: part_t) -> int:
        """
        :param part: 
        :type part: part_t

        :returns: 
        :rtype: int
        """
        ...

    def get_style_grid_cell_x_align(self, part: part_t) -> "grid_align_t":
        """
        :param part: 
        :type part: part_t

        :returns: 
        :rtype: "grid_align_t"
        """
        ...

    def get_style_grid_cell_column_span(self, part: part_t) -> int:
        """
        :param part: 
        :type part: part_t

        :returns: 
        :rtype: int
        """
        ...

    def get_style_grid_cell_row_pos(self, part: part_t) -> int:
        """
        :param part: 
        :type part: part_t

        :returns: 
        :rtype: int
        """
        ...

    def get_style_grid_cell_y_align(self, part: part_t) -> "grid_align_t":
        """
        :param part: 
        :type part: part_t

        :returns: 
        :rtype: "grid_align_t"
        """
        ...

    def get_style_grid_cell_row_span(self, part: part_t) -> int:
        """
        :param part: 
        :type part: part_t

        :returns: 
        :rtype: int
        """
        ...

    def set_style_pad_all(self, value: int, selector: "style_selector_t") -> None:
        """
        :param value: 
        :type value: int
        :param selector: 
        :type selector: "style_selector_t"

        :returns: 
        :rtype: None
        """
        ...

    def set_style_pad_hor(self, value: int, selector: "style_selector_t") -> None:
        """
        :param value: 
        :type value: int
        :param selector: 
        :type selector: "style_selector_t"

        :returns: 
        :rtype: None
        """
        ...

    def set_style_pad_ver(self, value: int, selector: "style_selector_t") -> None:
        """
        :param value: 
        :type value: int
        :param selector: 
        :type selector: "style_selector_t"

        :returns: 
        :rtype: None
        """
        ...

    def set_style_margin_all(self, value: int, selector: "style_selector_t") -> None:
        """
        :param value: 
        :type value: int
        :param selector: 
        :type selector: "style_selector_t"

        :returns: 
        :rtype: None
        """
        ...

    def set_style_margin_hor(self, value: int, selector: "style_selector_t") -> None:
        """
        :param value: 
        :type value: int
        :param selector: 
        :type selector: "style_selector_t"

        :returns: 
        :rtype: None
        """
        ...

    def set_style_margin_ver(self, value: int, selector: "style_selector_t") -> None:
        """
        :param value: 
        :type value: int
        :param selector: 
        :type selector: "style_selector_t"

        :returns: 
        :rtype: None
        """
        ...

    def set_style_pad_gap(self, value: int, selector: "style_selector_t") -> None:
        """
        :param value: 
        :type value: int
        :param selector: 
        :type selector: "style_selector_t"

        :returns: 
        :rtype: None
        """
        ...

    def set_style_size(self, width: int, height: int, selector: "style_selector_t") -> None:
        """
        :param width: 
        :type width: int
        :param height: 
        :type height: int
        :param selector: 
        :type selector: "style_selector_t"

        :returns: 
        :rtype: None
        """
        ...

    def set_style_transform_scale(self, value: int, selector: "style_selector_t") -> None:
        """
        :param value: 
        :type value: int
        :param selector: 
        :type selector: "style_selector_t"

        :returns: 
        :rtype: None
        """
        ...

    def get_style_space_left(self, part: part_t) -> int:
        """
        :param part: 
        :type part: part_t

        :returns: 
        :rtype: int
        """
        ...

    def get_style_space_right(self, part: part_t) -> int:
        """
        :param part: 
        :type part: part_t

        :returns: 
        :rtype: int
        """
        ...

    def get_style_space_top(self, part: part_t) -> int:
        """
        :param part: 
        :type part: part_t

        :returns: 
        :rtype: int
        """
        ...

    def get_style_space_bottom(self, part: part_t) -> int:
        """
        :param part: 
        :type part: part_t

        :returns: 
        :rtype: int
        """
        ...

    def get_style_transform_scale_x_safe(self, part: part_t) -> int:
        """
        :param part: 
        :type part: part_t

        :returns: 
        :rtype: int
        """
        ...

    def get_style_transform_scale_y_safe(self, part: part_t) -> int:
        """
        :param part: 
        :type part: part_t

        :returns: 
        :rtype: int
        """
        ...

    def move_foreground(self) -> None:
        """
        Move the object to the foreground. It will look like if it was created as the last child of its parent. It also means it can cover any of the siblings. 
        

        :returns: 
        :rtype: None
        """
        ...

    def move_background(self) -> None:
        """
        Move the object to the background. It will look like if it was created as the first child of its parent. It also means any of the siblings can cover the object. 
        

        :returns: 
        :rtype: None
        """
        ...

    def set_flex_flow(self, flow: flex_flow_t) -> None:
        """
        Set how the item should flow 
        
        :param flow: an element of lv_flex_flow_t . 
        :type flow: flex_flow_t

        :returns: 
        :rtype: None
        """
        ...

    def set_flex_align(self, main_place: flex_align_t, cross_place: flex_align_t, track_cross_place: flex_align_t) -> None:
        """
        Set how to place (where to align) the items and tracks 
        
        :param main_place: where to place the items on main axis (in their track). Any value of lv_flex_align_t . 
        :type main_place: flex_align_t
        :param cross_place: where to place the item in their track on the cross axis. LV_FLEX_ALIGN_START/END/CENTER 
        :type cross_place: flex_align_t
        :param track_cross_place: where to place the tracks in the cross direction. Any value of lv_flex_align_t . 
        :type track_cross_place: flex_align_t

        :returns: 
        :rtype: None
        """
        ...

    def set_flex_grow(self, grow: int) -> None:
        """
        Sets the width or height (on main axis) to grow the object in order fill the free space 
        
        :param grow: a value to set how much free space to take proportionally to other growing items. 
        :type grow: int

        :returns: 
        :rtype: None
        """
        ...

    def set_grid_dsc_array(self, col_dsc: List[int], row_dsc: List[int]) -> None:
        """
        :param col_dsc: 
        :type col_dsc: List[int]
        :param row_dsc: 
        :type row_dsc: List[int]

        :returns: 
        :rtype: None
        """
        ...

    def set_grid_align(self, column_align: grid_align_t, row_align: grid_align_t) -> None:
        """
        :param column_align: 
        :type column_align: grid_align_t
        :param row_align: 
        :type row_align: grid_align_t

        :returns: 
        :rtype: None
        """
        ...

    def set_grid_cell(self, column_align: grid_align_t, col_pos: int, col_span: int, row_align: grid_align_t, row_pos: int, row_span: int) -> None:
        """
        Set the cell of an object. The object's parent needs to have grid layout, else nothing will happen 
        
        :param column_align: the vertical alignment in the cell. LV_GRID_START/END/CENTER/STRETCH 
        :type column_align: grid_align_t
        :param col_pos: column ID 
        :type col_pos: int
        :param col_span: number of columns to take (>= 1) 
        :type col_span: int
        :param row_align: the horizontal alignment in the cell. LV_GRID_START/END/CENTER/STRETCH 
        :type row_align: grid_align_t
        :param row_pos: row ID 
        :type row_pos: int
        :param row_span: number of rows to take (>= 1) 
        :type row_span: int

        :returns: 
        :rtype: None
        """
        ...

    def delete(self) -> None:
        """
        Delete an object and all of its children. Also remove the objects from their group and remove all animations (if any). Send LV_EVENT_DELETED to deleted objects. 
        

        :returns: 
        :rtype: None
        """
        ...

    def clean(self) -> None:
        """
        Delete all children of an object. Also remove the objects from their group and remove all animations (if any). Send LV_EVENT_DELETED to deleted objects. 
        

        :returns: 
        :rtype: None
        """
        ...

    def delete_delayed(self, delay_ms: int) -> None:
        """
        Delete an object after some delay 
        
        :param delay_ms: time to wait before delete in milliseconds 
        :type delay_ms: int

        :returns: 
        :rtype: None
        """
        ...

    def delete_async(self) -> None:
        """
        Helper function for asynchronously deleting objects. Useful for cases where you can't delete an object directly in an LV_EVENT_DELETE handler (i.e. parent). :ref:`lv_async_call` 
        

        :returns: 
        :rtype: None
        """
        ...

    def set_parent(self, parent: "obj") -> None:
        """
        Move the parent of an object. The relative coordinates will be kept. 
        
        :param parent: pointer to the new parent 
        :type parent: "obj"

        :returns: 
        :rtype: None
        """
        ...

    def swap(self, parent: "obj") -> None:
        """
        Swap the positions of two objects. When used in listboxes, it can be used to sort the listbox items. 
        
        :param parent: pointer to the second object 
        :type parent: "obj"

        :returns: 
        :rtype: None
        """
        ...

    def move_to_index(self, index: int) -> None:
        """
        moves the object to the given index in its parent. When used in listboxes, it can be used to sort the listbox items. to move to the background: lv_obj_move_to_index(obj, 0)  to move forward (up): lv_obj_move_to_index(obj, lv_obj_get_index(obj) - 1) 
        
        :param index: new index in parent. -1 to count from the back 
        :type index: int

        :returns: 
        :rtype: None
        """
        ...

    def get_screen(self) -> "obj":
        """
        Get the screen of an object pointer to the object's screen 
        

        :returns: pointer to the object's screen 
        :rtype: "obj"
        """
        ...

    def get_display(self) -> "display_t":
        """
        Get the display of the object pointer to the object's display 
        

        :returns: pointer to the object's display 
        :rtype: "display_t"
        """
        ...

    def get_parent(self) -> "obj":
        """
        Get the parent of an object the parent of the object. (NULL if obj was a screen) 
        

        :returns: the parent of the object. (NULL if obj was a screen) 
        :rtype: "obj"
        """
        ...

    def get_child(self, idx: int) -> "obj":
        """
        Get the child of an object by the child's index. pointer to the child or NULL if the index was invalid 
        
        :param idx: the index of the child. 0: the oldest (firstly created) child 1: the second oldest child count-1: the youngest -1: the youngest -2: the second youngest 
        :type idx: int

        :returns: pointer to the child or NULL if the index was invalid 
        :rtype: "obj"
        """
        ...

    def get_child_by_type(self, idx: int, class_p: "obj") -> "obj":
        """
        Get the child of an object by the child's index. Consider the children only with a given type. pointer to the child or NULL if the index was invalid 
        
        :param idx: the index of the child. 0: the oldest (firstly created) child 1: the second oldest child count-1: the youngest -1: the youngest -2: the second youngest 
        :type idx: int
        :param class_p: the type of the children to check 
        :type class_p: "obj"

        :returns: pointer to the child or NULL if the index was invalid 
        :rtype: "obj"
        """
        ...

    def get_sibling(self, idx: int) -> "obj":
        """
        Return a sibling of an object pointer to the requested sibling or NULL if there is no such sibling 
        
        :param idx: 0: obj itself -1: the first older sibling -2: the next older sibling 1: the first younger sibling 2: the next younger sibling etc 
        :type idx: int

        :returns: pointer to the requested sibling or NULL if there is no such sibling 
        :rtype: "obj"
        """
        ...

    def get_sibling_by_type(self, idx: int, class_p: "obj") -> "obj":
        """
        Return a sibling of an object. Consider the siblings only with a given type. pointer to the requested sibling or NULL if there is no such sibling 
        
        :param idx: 0: obj itself -1: the first older sibling -2: the next older sibling 1: the first younger sibling 2: the next younger sibling etc 
        :type idx: int
        :param class_p: the type of the children to check 
        :type class_p: "obj"

        :returns: pointer to the requested sibling or NULL if there is no such sibling 
        :rtype: "obj"
        """
        ...

    def get_child_count(self) -> int:
        """
        Get the number of children the number of children 
        

        :returns: the number of children 
        :rtype: int
        """
        ...

    def get_child_count_by_type(self, class_p: "obj") -> int:
        """
        Get the number of children having a given type. the number of children 
        
        :param class_p: the type of the children to check 
        :type class_p: "obj"

        :returns: the number of children 
        :rtype: int
        """
        ...

    def get_index(self) -> int:
        """
        Get the index of a child. the child index of the object. E.g. 0: the oldest (firstly created child). (-1 if child could not be found or no parent exists) 
        

        :returns: the child index of the object. E.g. 0: the oldest (firstly created child). (-1 if child could not be found or no parent exists) 
        :rtype: int
        """
        ...

    def get_index_by_type(self, class_p: "obj") -> int:
        """
        Get the index of a child. Consider the children only with a given type. the child index of the object. E.g. 0: the oldest (firstly created child with the given class). (-1 if child could not be found or no parent exists) 
        
        :param class_p: the type of the children to check 
        :type class_p: "obj"

        :returns: the child index of the object. E.g. 0: the oldest (firstly created child with the given class). (-1 if child could not be found or no parent exists) 
        :rtype: int
        """
        ...

    def tree_walk(self, cb: Callable[["obj", Any], "obj"], start_obj: "obj") -> None:
        """
        Iterate through all children of any object. 
        
        :param cb: call this callback on the objects 
        :type cb: Callable[["obj", Any], "obj"]
        :param start_obj: pointer to any user related data (will be passed to cb ) 
        :type start_obj: "obj"

        :returns: 
        :rtype: None
        """
        ...

    def dump_tree(self) -> None:
        """
        Iterate through all children of any object and print their ID. 
        

        :returns: 
        :rtype: None
        """
        ...

    def set_pos(self, x: int, y: int) -> None:
        """
        Set the position of an object relative to the set alignment. With default alignment it's the distance from the top left corner  E.g. LV_ALIGN_CENTER alignment it's the offset from the center of the parent  The position is interpreted on the content area of the parent  The values can be set in pixel or in percentage of parent size with lv_pct(v) 
        
        :param x: new x coordinate 
        :type x: int
        :param y: new y coordinate 
        :type y: int

        :returns: 
        :rtype: None
        """
        ...

    def set_x(self, index: int) -> None:
        """
        Set the x coordinate of an object With default alignment it's the distance from the top left corner  E.g. LV_ALIGN_CENTER alignment it's the offset from the center of the parent  The position is interpreted on the content area of the parent  The values can be set in pixel or in percentage of parent size with lv_pct(v) 
        
        :param index: new x coordinate 
        :type index: int

        :returns: 
        :rtype: None
        """
        ...

    def set_y(self, index: int) -> None:
        """
        Set the y coordinate of an object With default alignment it's the distance from the top left corner  E.g. LV_ALIGN_CENTER alignment it's the offset from the center of the parent  The position is interpreted on the content area of the parent  The values can be set in pixel or in percentage of parent size with lv_pct(v) 
        
        :param index: new y coordinate 
        :type index: int

        :returns: 
        :rtype: None
        """
        ...

    def set_size(self, x: int, y: int) -> None:
        """
        Set the size of an object. possible values are: pixel simple set the size accordingly LV_SIZE_CONTENT set the size to involve all children in the given direction lv_pct(x) to set size in percentage of the parent's content area size (the size without paddings). x should be in [0..1000]% range 
        
        :param x: the new width 
        :type x: int
        :param y: the new height 
        :type y: int

        :returns: 
        :rtype: None
        """
        ...

    def refr_size(self) -> bool:
        """
        Recalculate the size of the object true: the size has been changed 
        

        :returns: true: the size has been changed 
        :rtype: bool
        """
        ...

    def set_width(self, index: int) -> None:
        """
        Set the width of an object possible values are: pixel simple set the size accordingly LV_SIZE_CONTENT set the size to involve all children in the given direction lv_pct(x) to set size in percentage of the parent's content area size (the size without paddings). x should be in [0..1000]% range 
        
        :param index: the new width 
        :type index: int

        :returns: 
        :rtype: None
        """
        ...

    def set_height(self, index: int) -> None:
        """
        Set the height of an object possible values are: pixel simple set the size accordingly LV_SIZE_CONTENT set the size to involve all children in the given direction lv_pct(x) to set size in percentage of the parent's content area size (the size without paddings). x should be in [0..1000]% range 
        
        :param index: the new height 
        :type index: int

        :returns: 
        :rtype: None
        """
        ...

    def set_content_width(self, index: int) -> None:
        """
        Set the width reduced by the left and right padding and the border width. 
        
        :param index: the width without paddings in pixels 
        :type index: int

        :returns: 
        :rtype: None
        """
        ...

    def set_content_height(self, index: int) -> None:
        """
        Set the height reduced by the top and bottom padding and the border width. 
        
        :param index: the height without paddings in pixels 
        :type index: int

        :returns: 
        :rtype: None
        """
        ...

    def set_layout(self, delay_ms: int) -> None:
        """
        Set a layout for an object 
        
        :param delay_ms: pointer to a layout descriptor to set 
        :type delay_ms: int

        :returns: 
        :rtype: None
        """
        ...

    def is_layout_positioned(self) -> bool:
        """
        Test whether the and object is positioned by a layout or not true: positioned by a layout; false: not positioned by a layout 
        

        :returns: true: positioned by a layout; false: not positioned by a layout 
        :rtype: bool
        """
        ...

    def mark_layout_as_dirty(self) -> None:
        """
        Mark the object for layout update. 
        

        :returns: 
        :rtype: None
        """
        ...

    def update_layout(self) -> None:
        """
        Update the layout of an object. 
        

        :returns: 
        :rtype: None
        """
        ...

    def set_align(self, align: align_t) -> None:
        """
        Change the alignment of an object. 
        
        :param align: type of alignment (see 'lv_align_t' enum) LV_ALIGN_OUT_... can't be used. 
        :type align: align_t

        :returns: 
        :rtype: None
        """
        ...

    def align(self, align: align_t, x_ofs: int, y_ofs: int) -> None:
        """
        Change the alignment of an object and set new coordinates. Equivalent to: lv_obj_set_align(obj, align); lv_obj_set_pos(obj, x_ofs, y_ofs); 
        
        :param align: type of alignment (see 'lv_align_t' enum) LV_ALIGN_OUT_... can't be used. 
        :type align: align_t
        :param x_ofs: x coordinate offset after alignment 
        :type x_ofs: int
        :param y_ofs: y coordinate offset after alignment 
        :type y_ofs: int

        :returns: 
        :rtype: None
        """
        ...

    def align_to(self, base: "obj", align: align_t, x_ofs: int, y_ofs: int) -> None:
        """
        Align an object to another object. if the position or size of base changes obj needs to be aligned manually again 
        
        :param base: pointer to another object (if NULL obj s parent is used). 'obj' will be aligned to it. 
        :type base: "obj"
        :param align: type of alignment (see 'lv_align_t' enum) 
        :type align: align_t
        :param x_ofs: x coordinate offset after alignment 
        :type x_ofs: int
        :param y_ofs: y coordinate offset after alignment 
        :type y_ofs: int

        :returns: 
        :rtype: None
        """
        ...

    def center(self) -> None:
        """
        Align an object to the center on its parent. if the parent size changes obj needs to be aligned manually again 
        

        :returns: 
        :rtype: None
        """
        ...

    def get_coords(self, coords: "area_t") -> None:
        """
        Copy the coordinates of an object to an area 
        
        :param coords: pointer to an area to store the coordinates 
        :type coords: "area_t"

        :returns: 
        :rtype: None
        """
        ...

    def get_x(self) -> int:
        """
        Get the x coordinate of object. distance of obj from the left side of its parent plus the parent's left padding  The position of the object is recalculated only on the next redraw. To force coordinate recalculation call lv_obj_update_layout(obj) .  Zero return value means the object is on the left padding of the parent, and not on the left edge.  Scrolling of the parent doesn't change the returned value.  The returned value is always the distance from the parent even if obj is positioned by a layout. 
        

        :returns: distance of obj from the left side of its parent plus the parent's left padding 
        :rtype: int
        """
        ...

    def get_x2(self) -> int:
        """
        Get the x2 coordinate of object. distance of obj from the right side of its parent plus the parent's right padding  The position of the object is recalculated only on the next redraw. To force coordinate recalculation call lv_obj_update_layout(obj) .  Zero return value means the object is on the right padding of the parent, and not on the right edge.  Scrolling of the parent doesn't change the returned value.  The returned value is always the distance from the parent even if obj is positioned by a layout. 
        

        :returns: distance of obj from the right side of its parent plus the parent's right padding 
        :rtype: int
        """
        ...

    def get_y(self) -> int:
        """
        Get the y coordinate of object. distance of obj from the top side of its parent plus the parent's top padding  The position of the object is recalculated only on the next redraw. To force coordinate recalculation call lv_obj_update_layout(obj) .  Zero return value means the object is on the top padding of the parent, and not on the top edge.  Scrolling of the parent doesn't change the returned value.  The returned value is always the distance from the parent even if obj is positioned by a layout. 
        

        :returns: distance of obj from the top side of its parent plus the parent's top padding 
        :rtype: int
        """
        ...

    def get_y2(self) -> int:
        """
        Get the y2 coordinate of object. distance of obj from the bottom side of its parent plus the parent's bottom padding  The position of the object is recalculated only on the next redraw. To force coordinate recalculation call lv_obj_update_layout(obj) .  Zero return value means the object is on the bottom padding of the parent, and not on the bottom edge.  Scrolling of the parent doesn't change the returned value.  The returned value is always the distance from the parent even if obj is positioned by a layout. 
        

        :returns: distance of obj from the bottom side of its parent plus the parent's bottom padding 
        :rtype: int
        """
        ...

    def get_x_aligned(self) -> int:
        """
        Get the actually set x coordinate of object, i.e. the offset from the set alignment the set x coordinate 
        

        :returns: the set x coordinate 
        :rtype: int
        """
        ...

    def get_y_aligned(self) -> int:
        """
        Get the actually set y coordinate of object, i.e. the offset from the set alignment the set y coordinate 
        

        :returns: the set y coordinate 
        :rtype: int
        """
        ...

    def get_width(self) -> int:
        """
        Get the width of an object The position of the object is recalculated only on the next redraw. To force coordinate recalculation call lv_obj_update_layout(obj) .  the width in pixels 
        

        :returns: the width in pixels 
        :rtype: int
        """
        ...

    def get_height(self) -> int:
        """
        Get the height of an object The position of the object is recalculated only on the next redraw. To force coordinate recalculation call lv_obj_update_layout(obj) .  the height in pixels 
        

        :returns: the height in pixels 
        :rtype: int
        """
        ...

    def get_content_width(self) -> int:
        """
        Get the width reduced by the left and right padding and the border width. The position of the object is recalculated only on the next redraw. To force coordinate recalculation call lv_obj_update_layout(obj) .  the width which still fits into its parent without causing overflow (making the parent scrollable) 
        

        :returns: the width which still fits into its parent without causing overflow (making the parent scrollable) 
        :rtype: int
        """
        ...

    def get_content_height(self) -> int:
        """
        Get the height reduced by the top and bottom padding and the border width. The position of the object is recalculated only on the next redraw. To force coordinate recalculation call lv_obj_update_layout(obj) .  the height which still fits into the parent without causing overflow (making the parent scrollable) 
        

        :returns: the height which still fits into the parent without causing overflow (making the parent scrollable) 
        :rtype: int
        """
        ...

    def get_content_coords(self, coords: "area_t") -> None:
        """
        Get the area reduced by the paddings and the border width. The position of the object is recalculated only on the next redraw. To force coordinate recalculation call lv_obj_update_layout(obj) . 
        
        :param coords: the area which still fits into the parent without causing overflow (making the parent scrollable) 
        :type coords: "area_t"

        :returns: 
        :rtype: None
        """
        ...

    def get_self_width(self) -> int:
        """
        Get the width occupied by the "parts" of the widget. E.g. the width of all columns of a table. the width of the virtually drawn content  This size independent from the real size of the widget. It just tells how large the internal ("virtual") content is. 
        

        :returns: the width of the virtually drawn content 
        :rtype: int
        """
        ...

    def get_self_height(self) -> int:
        """
        Get the height occupied by the "parts" of the widget. E.g. the height of all rows of a table. the width of the virtually drawn content  This size independent from the real size of the widget. It just tells how large the internal ("virtual") content is. 
        

        :returns: the width of the virtually drawn content 
        :rtype: int
        """
        ...

    def refresh_self_size(self) -> bool:
        """
        Handle if the size of the internal ("virtual") content of an object has changed. false: nothing happened; true: refresh happened 
        

        :returns: false: nothing happened; true: refresh happened 
        :rtype: bool
        """
        ...

    def refr_pos(self) -> None:
        """

        :returns: 
        :rtype: None
        """
        ...

    def move_to(self, x: int, y: int) -> None:
        """
        :param x: 
        :type x: int
        :param y: 
        :type y: int

        :returns: 
        :rtype: None
        """
        ...

    def move_children_by(self, x_diff: int, y_diff: int, ignore_floating: bool) -> None:
        """
        :param x_diff: 
        :type x_diff: int
        :param y_diff: 
        :type y_diff: int
        :param ignore_floating: 
        :type ignore_floating: bool

        :returns: 
        :rtype: None
        """
        ...

    def transform_point(self, p: "point_t", flags: "obj") -> None:
        """
        Transform a point using the angle and zoom style properties of an object 
        
        :param p: a point to transform, the result will be written back here too 
        :type p: "point_t"
        :param flags: OR-ed valued of :cpp:enum: lv_obj_point_transform_flag_t 
        :type flags: "obj"

        :returns: 
        :rtype: None
        """
        ...

    def transform_point_array(self, points: List["point_t"], count: int, flags: "obj") -> None:
        """
        Transform an array of points using the angle and zoom style properties of an object 
        
        :param points: the array of points to transform, the result will be written back here too 
        :type points: List["point_t"]
        :param count: number of points in the array 
        :type count: int
        :param flags: OR-ed valued of :cpp:enum: lv_obj_point_transform_flag_t 
        :type flags: "obj"

        :returns: 
        :rtype: None
        """
        ...

    def get_transformed_area(self, area: "area_t", flags: "obj") -> None:
        """
        Transform an area using the angle and zoom style properties of an object 
        
        :param area: an area to transform, the result will be written back here too 
        :type area: "area_t"
        :param flags: OR-ed valued of :cpp:enum: lv_obj_point_transform_flag_t 
        :type flags: "obj"

        :returns: 
        :rtype: None
        """
        ...

    def invalidate_area(self, area: "area_t") -> None:
        """
        Mark an area of an object as invalid. The area will be truncated to the object's area and marked for redraw. 
        
        :param area: the area to redraw 
        :type area: "area_t"

        :returns: 
        :rtype: None
        """
        ...

    def invalidate(self) -> None:
        """
        Mark the object as invalid to redrawn its area 
        

        :returns: 
        :rtype: None
        """
        ...

    def area_is_visible(self, area: "area_t") -> bool:
        """
        Tell whether an area of an object is visible (even partially) now or not true visible; false not visible (hidden, out of parent, on other screen, etc) 
        
        :param area: the are to check. The visible part of the area will be written back here. 
        :type area: "area_t"

        :returns: true visible; false not visible (hidden, out of parent, on other screen, etc) 
        :rtype: bool
        """
        ...

    def is_visible(self) -> bool:
        """
        Tell whether an object is visible (even partially) now or not true: visible; false not visible (hidden, out of parent, on other screen, etc) 
        

        :returns: true: visible; false not visible (hidden, out of parent, on other screen, etc) 
        :rtype: bool
        """
        ...

    def set_ext_click_area(self, index: int) -> None:
        """
        Set the size of an extended clickable area 
        
        :param index: extended clickable area in all 4 directions [px] 
        :type index: int

        :returns: 
        :rtype: None
        """
        ...

    def get_click_area(self, coords: "area_t") -> None:
        """
        Get the an area where to object can be clicked. It's the object's normal area plus the extended click area. 
        
        :param coords: store the result area here 
        :type coords: "area_t"

        :returns: 
        :rtype: None
        """
        ...

    def hit_test(self, point: "point_t") -> bool:
        """
        Hit-test an object given a particular point in screen space. true: if the object is considered under the point 
        
        :param point: screen-space point (absolute coordinate) 
        :type point: "point_t"

        :returns: true: if the object is considered under the point 
        :rtype: bool
        """
        ...

    def set_scrollbar_mode(self, mode: scrollbar_mode_t) -> None:
        """
        Set how the scrollbars should behave. 
        
        :param mode: LV_SCROLL_MODE_ON/OFF/AUTO/ACTIVE 
        :type mode: scrollbar_mode_t

        :returns: 
        :rtype: None
        """
        ...

    def set_scroll_dir(self, dir: dir_t) -> None:
        """
        Set the object in which directions can be scrolled 
        
        :param dir: the allow scroll directions. An element or OR-ed values of lv_dir_t 
        :type dir: dir_t

        :returns: 
        :rtype: None
        """
        ...

    def set_scroll_snap_x(self, align: scroll_snap_t) -> None:
        """
        Set where to snap the children when scrolling ends horizontally 
        
        :param align: the snap align to set from lv_scroll_snap_t 
        :type align: scroll_snap_t

        :returns: 
        :rtype: None
        """
        ...

    def set_scroll_snap_y(self, align: scroll_snap_t) -> None:
        """
        Set where to snap the children when scrolling ends vertically 
        
        :param align: the snap align to set from lv_scroll_snap_t 
        :type align: scroll_snap_t

        :returns: 
        :rtype: None
        """
        ...

    def get_scrollbar_mode(self) -> "scrollbar_mode_t":
        """
        Get the current scroll mode (when to hide the scrollbars) the current scroll mode from lv_scrollbar_mode_t 
        

        :returns: the current scroll mode from lv_scrollbar_mode_t 
        :rtype: "scrollbar_mode_t"
        """
        ...

    def get_scroll_dir(self) -> "dir_t":
        """
        Get the object in which directions can be scrolled 
        

        :returns: 
        :rtype: "dir_t"
        """
        ...

    def get_scroll_snap_x(self) -> "scroll_snap_t":
        """
        Get where to snap the children when scrolling ends horizontally the current snap align from lv_scroll_snap_t 
        

        :returns: the current snap align from lv_scroll_snap_t 
        :rtype: "scroll_snap_t"
        """
        ...

    def get_scroll_snap_y(self) -> "scroll_snap_t":
        """
        Get where to snap the children when scrolling ends vertically the current snap align from lv_scroll_snap_t 
        

        :returns: the current snap align from lv_scroll_snap_t 
        :rtype: "scroll_snap_t"
        """
        ...

    def get_scroll_x(self) -> int:
        """
        Get current X scroll position. the current scroll position from the left edge. If the object is not scrolled return 0 If scrolled return > 0 If scrolled in (elastic scroll) return < 0 
        

        :returns: the current scroll position from the left edge. If the object is not scrolled return 0 If scrolled return > 0 If scrolled in (elastic scroll) return < 0 
        :rtype: int
        """
        ...

    def get_scroll_y(self) -> int:
        """
        Get current Y scroll position. the current scroll position from the top edge. If the object is not scrolled return 0 If scrolled return > 0 If scrolled inside return < 0 
        

        :returns: the current scroll position from the top edge. If the object is not scrolled return 0 If scrolled return > 0 If scrolled inside return < 0 
        :rtype: int
        """
        ...

    def get_scroll_top(self) -> int:
        """
        Return the height of the area above the object. That is the number of pixels the object can be scrolled down. Normally positive but can be negative when scrolled inside. the scrollable area above the object in pixels 
        

        :returns: the scrollable area above the object in pixels 
        :rtype: int
        """
        ...

    def get_scroll_bottom(self) -> int:
        """
        Return the height of the area below the object. That is the number of pixels the object can be scrolled down. Normally positive but can be negative when scrolled inside. the scrollable area below the object in pixels 
        

        :returns: the scrollable area below the object in pixels 
        :rtype: int
        """
        ...

    def get_scroll_left(self) -> int:
        """
        Return the width of the area on the left the object. That is the number of pixels the object can be scrolled down. Normally positive but can be negative when scrolled inside. the scrollable area on the left the object in pixels 
        

        :returns: the scrollable area on the left the object in pixels 
        :rtype: int
        """
        ...

    def get_scroll_right(self) -> int:
        """
        Return the width of the area on the right the object. That is the number of pixels the object can be scrolled down. Normally positive but can be negative when scrolled inside. the scrollable area on the right the object in pixels 
        

        :returns: the scrollable area on the right the object in pixels 
        :rtype: int
        """
        ...

    def get_scroll_end(self, end: "point_t") -> None:
        """
        Get the X and Y coordinates where the scrolling will end for this object if a scrolling animation is in progress. If no scrolling animation, give the current x or y scroll position. 
        
        :param end: pointer to store the result 
        :type end: "point_t"

        :returns: 
        :rtype: None
        """
        ...

    def scroll_by(self, x: int, y: int, anim_en: "anim_enable_t") -> None:
        """
        Scroll by a given amount of pixels > 0 value means scroll right/bottom (show the more content on the right/bottom)  e.g. dy = -20 means scroll down 20 px 
        
        :param x: pixels to scroll horizontally 
        :type x: int
        :param y: pixels to scroll vertically 
        :type y: int
        :param anim_en: LV_ANIM_ON: scroll with animation; LV_ANIM_OFF: scroll immediately 
        :type anim_en: "anim_enable_t"

        :returns: 
        :rtype: None
        """
        ...

    def scroll_by_bounded(self, x: int, y: int, anim_en: "anim_enable_t") -> None:
        """
        Scroll by a given amount of pixels. dx and dy will be limited internally to allow scrolling only on the content area. e.g. dy = -20 means scroll down 20 px 
        
        :param x: pixels to scroll horizontally 
        :type x: int
        :param y: pixels to scroll vertically 
        :type y: int
        :param anim_en: LV_ANIM_ON: scroll with animation; LV_ANIM_OFF: scroll immediately 
        :type anim_en: "anim_enable_t"

        :returns: 
        :rtype: None
        """
        ...

    def scroll_to(self, x: int, y: int, anim_en: "anim_enable_t") -> None:
        """
        Scroll to a given coordinate on an object. x and y will be limited internally to allow scrolling only on the content area. 
        
        :param x: pixels to scroll horizontally 
        :type x: int
        :param y: pixels to scroll vertically 
        :type y: int
        :param anim_en: LV_ANIM_ON: scroll with animation; LV_ANIM_OFF: scroll immediately 
        :type anim_en: "anim_enable_t"

        :returns: 
        :rtype: None
        """
        ...

    def scroll_to_x(self, x: int, anim_en: "anim_enable_t") -> None:
        """
        Scroll to a given X coordinate on an object. x will be limited internally to allow scrolling only on the content area. 
        
        :param x: pixels to scroll horizontally 
        :type x: int
        :param anim_en: LV_ANIM_ON: scroll with animation; LV_ANIM_OFF: scroll immediately 
        :type anim_en: "anim_enable_t"

        :returns: 
        :rtype: None
        """
        ...

    def scroll_to_y(self, x: int, anim_en: "anim_enable_t") -> None:
        """
        Scroll to a given Y coordinate on an object y will be limited internally to allow scrolling only on the content area. 
        
        :param x: pixels to scroll vertically 
        :type x: int
        :param anim_en: LV_ANIM_ON: scroll with animation; LV_ANIM_OFF: scroll immediately 
        :type anim_en: "anim_enable_t"

        :returns: 
        :rtype: None
        """
        ...

    def scroll_to_view(self, anim_en: "anim_enable_t") -> None:
        """
        Scroll to an object until it becomes visible on its parent 
        
        :param anim_en: LV_ANIM_ON: scroll with animation; LV_ANIM_OFF: scroll immediately 
        :type anim_en: "anim_enable_t"

        :returns: 
        :rtype: None
        """
        ...

    def scroll_to_view_recursive(self, anim_en: "anim_enable_t") -> None:
        """
        Scroll to an object until it becomes visible on its parent. Do the same on the parent's parent, and so on. Therefore the object will be scrolled into view even it has nested scrollable parents 
        
        :param anim_en: LV_ANIM_ON: scroll with animation; LV_ANIM_OFF: scroll immediately 
        :type anim_en: "anim_enable_t"

        :returns: 
        :rtype: None
        """
        ...

    def is_scrolling(self) -> bool:
        """
        Tell whether an object is being scrolled or not at this moment true: obj is being scrolled 
        

        :returns: true: obj is being scrolled 
        :rtype: bool
        """
        ...

    def update_snap(self, anim_en: "anim_enable_t") -> None:
        """
        Check the children of obj and scroll obj to fulfill the scroll_snap settings 
        
        :param anim_en: LV_ANIM_ON/OFF 
        :type anim_en: "anim_enable_t"

        :returns: 
        :rtype: None
        """
        ...

    def get_scrollbar_area(self, hor: "area_t", ver: "area_t") -> None:
        """
        Get the area of the scrollbars 
        
        :param hor: pointer to store the area of the horizontal scrollbar 
        :type hor: "area_t"
        :param ver: pointer to store the area of the vertical scrollbar 
        :type ver: "area_t"

        :returns: 
        :rtype: None
        """
        ...

    def scrollbar_invalidate(self) -> None:
        """
        Invalidate the area of the scrollbars 
        

        :returns: 
        :rtype: None
        """
        ...

    def readjust_scroll(self, anim_en: "anim_enable_t") -> None:
        """
        Checks if the content is scrolled "in" and adjusts it to a normal position. 
        
        :param anim_en: LV_ANIM_ON/OFF 
        :type anim_en: "anim_enable_t"

        :returns: 
        :rtype: None
        """
        ...

    def add_style(self, style: "style_t", selector: "style_selector_t") -> None:
        """
        Add a style to an object. lv_obj_add_style(btn, &style_btn, 0); //Default button style lv_obj_add_style(btn, &btn_red, LV_STATE_PRESSED); //Overwrite only some colors to red when pressed 
        
        :param style: pointer to a style to add 
        :type style: "style_t"
        :param selector: OR-ed value of parts and state to which the style should be added 
        :type selector: "style_selector_t"

        :returns: 
        :rtype: None
        """
        ...

    def replace_style(self, old_style: "style_t", new_style: "style_t", selector: "style_selector_t") -> bool:
        """
        Replaces a style of an object, preserving the order of the style stack (local styles and transitions are ignored). lv_obj_replace_style(obj, &yellow_style, &blue_style, LV_PART_ANY | LV_STATE_ANY); //Replace a specific style lv_obj_replace_style(obj, &yellow_style, &blue_style, LV_PART_MAIN | LV_STATE_PRESSED); //Replace a specific style assigned to the main part when it is pressed 
        
        :param old_style: pointer to a style to replace. 
        :type old_style: "style_t"
        :param new_style: pointer to a style to replace the old style with. 
        :type new_style: "style_t"
        :param selector: OR-ed values of states and a part to replace only styles with matching selectors. LV_STATE_ANY and LV_PART_ANY can be used 
        :type selector: "style_selector_t"

        :returns: 
        :rtype: bool
        """
        ...

    def remove_style(self, style: "style_t", selector: "style_selector_t") -> None:
        """
        Remove a style from an object. lv_obj_remove_style(obj, &style, LV_PART_ANY | LV_STATE_ANY); //Remove a specific style lv_obj_remove_style(obj, NULL, LV_PART_MAIN | LV_STATE_ANY); //Remove all styles from the main part  lv_obj_remove_style(obj, NULL, LV_PART_ANY | LV_STATE_ANY); //Remove all styles 
        
        :param style: pointer to a style to remove. Can be NULL to check only the selector 
        :type style: "style_t"
        :param selector: OR-ed values of states and a part to remove only styles with matching selectors. LV_STATE_ANY and LV_PART_ANY can be used 
        :type selector: "style_selector_t"

        :returns: 
        :rtype: None
        """
        ...

    def remove_style_all(self) -> None:
        """
        Remove all styles from an object 
        

        :returns: 
        :rtype: None
        """
        ...

    def report_style_change(self) -> None:
        """
        Notify all object if a style is modified 
        

        :returns: 
        :rtype: None
        """
        ...

    def refresh_style(self, part: part_t, prop: "style_prop_t") -> None:
        """
        Notify an object and its children about its style is modified. 
        
        :param part: the part whose style was changed. E.g. LV_PART_ANY , LV_PART_MAIN 
        :type part: part_t
        :param prop: LV_STYLE_PROP_ANY or an LV_STYLE_... property. It is used to optimize what needs to be refreshed. LV_STYLE_PROP_INV to perform only a style cache update 
        :type prop: "style_prop_t"

        :returns: 
        :rtype: None
        """
        ...

    def enable_style_refresh(self) -> None:
        """
        Enable or disable automatic style refreshing when a new style is added/removed to/from an object or any other style change happens. 
        

        :returns: 
        :rtype: None
        """
        ...

    def get_style_prop(self, part: part_t, prop: "style_prop_t") -> "style_value_t":
        """
        Get the value of a style property. The current state of the object will be considered. Inherited properties will be inherited. If a property is not set a default value will be returned. the value of the property. Should be read from the correct field of the :ref:`lv_style_value_t` according to the type of the property. 
        
        :param part: a part from which the property should be get 
        :type part: part_t
        :param prop: the property to get 
        :type prop: "style_prop_t"

        :returns: the value of the property. Should be read from the correct field of the :ref:`lv_style_value_t` according to the type of the property. 
        :rtype: "style_value_t"
        """
        ...

    def has_style_prop(self, selector: "style_selector_t", prop: "style_prop_t") -> bool:
        """
        Check if an object has a specified style property for a given style selector. true if the object has the specified selector and property, false otherwise. 
        
        :param selector: the style selector to be checked, defining the scope of the style to be examined. 
        :type selector: "style_selector_t"
        :param prop: the property to be checked. 
        :type prop: "style_prop_t"

        :returns: true if the object has the specified selector and property, false otherwise. 
        :rtype: bool
        """
        ...

    def set_local_style_prop(self, prop: "style_prop_t", value: "style_value_t", selector: "style_selector_t") -> None:
        """
        Set local style property on an object's part and state. 
        
        :param prop: the property 
        :type prop: "style_prop_t"
        :param value: value of the property. The correct element should be set according to the type of the property 
        :type value: "style_value_t"
        :param selector: OR-ed value of parts and state for which the style should be set 
        :type selector: "style_selector_t"

        :returns: 
        :rtype: None
        """
        ...

    def get_local_style_prop(self, prop: "style_prop_t", value: "style_value_t", selector: "style_selector_t") -> "style_res_t":
        """
        :param prop: 
        :type prop: "style_prop_t"
        :param value: 
        :type value: "style_value_t"
        :param selector: 
        :type selector: "style_selector_t"

        :returns: 
        :rtype: "style_res_t"
        """
        ...

    def remove_local_style_prop(self, prop: "style_prop_t", selector: "style_selector_t") -> bool:
        """
        Remove a local style property from a part of an object with a given state. true the property was found and removed; false: the property was not found 
        
        :param prop: a style property to remove. 
        :type prop: "style_prop_t"
        :param selector: OR-ed value of parts and state for which the style should be removed 
        :type selector: "style_selector_t"

        :returns: true the property was found and removed; false: the property was not found 
        :rtype: bool
        """
        ...

    def style_apply_color_filter(self, part: part_t, v: "style_value_t") -> "style_value_t":
        """
        Used internally for color filtering 
        
        :param part: 
        :type part: part_t
        :param v: 
        :type v: "style_value_t"

        :returns: 
        :rtype: "style_value_t"
        """
        ...

    def fade_in(self, time: int, delay: int) -> None:
        """
        Fade in an an object and all its children. 
        
        :param time: time of fade 
        :type time: int
        :param delay: delay to start the animation 
        :type delay: int

        :returns: 
        :rtype: None
        """
        ...

    def fade_out(self, time: int, delay: int) -> None:
        """
        Fade out an an object and all its children. 
        
        :param time: time of fade 
        :type time: int
        :param delay: delay to start the animation 
        :type delay: int

        :returns: 
        :rtype: None
        """
        ...

    def set_style_width(self, value: int, selector: "style_selector_t") -> None:
        """
        :param value: 
        :type value: int
        :param selector: 
        :type selector: "style_selector_t"

        :returns: 
        :rtype: None
        """
        ...

    def set_style_min_width(self, value: int, selector: "style_selector_t") -> None:
        """
        :param value: 
        :type value: int
        :param selector: 
        :type selector: "style_selector_t"

        :returns: 
        :rtype: None
        """
        ...

    def set_style_max_width(self, value: int, selector: "style_selector_t") -> None:
        """
        :param value: 
        :type value: int
        :param selector: 
        :type selector: "style_selector_t"

        :returns: 
        :rtype: None
        """
        ...

    def set_style_height(self, value: int, selector: "style_selector_t") -> None:
        """
        :param value: 
        :type value: int
        :param selector: 
        :type selector: "style_selector_t"

        :returns: 
        :rtype: None
        """
        ...

    def set_style_min_height(self, value: int, selector: "style_selector_t") -> None:
        """
        :param value: 
        :type value: int
        :param selector: 
        :type selector: "style_selector_t"

        :returns: 
        :rtype: None
        """
        ...

    def set_style_max_height(self, value: int, selector: "style_selector_t") -> None:
        """
        :param value: 
        :type value: int
        :param selector: 
        :type selector: "style_selector_t"

        :returns: 
        :rtype: None
        """
        ...

    def set_style_length(self, value: int, selector: "style_selector_t") -> None:
        """
        :param value: 
        :type value: int
        :param selector: 
        :type selector: "style_selector_t"

        :returns: 
        :rtype: None
        """
        ...

    def set_style_x(self, value: int, selector: "style_selector_t") -> None:
        """
        :param value: 
        :type value: int
        :param selector: 
        :type selector: "style_selector_t"

        :returns: 
        :rtype: None
        """
        ...

    def set_style_y(self, value: int, selector: "style_selector_t") -> None:
        """
        :param value: 
        :type value: int
        :param selector: 
        :type selector: "style_selector_t"

        :returns: 
        :rtype: None
        """
        ...

    def set_style_align(self, value: align_t, selector: "style_selector_t") -> None:
        """
        :param value: 
        :type value: align_t
        :param selector: 
        :type selector: "style_selector_t"

        :returns: 
        :rtype: None
        """
        ...

    def set_style_transform_width(self, value: int, selector: "style_selector_t") -> None:
        """
        :param value: 
        :type value: int
        :param selector: 
        :type selector: "style_selector_t"

        :returns: 
        :rtype: None
        """
        ...

    def set_style_transform_height(self, value: int, selector: "style_selector_t") -> None:
        """
        :param value: 
        :type value: int
        :param selector: 
        :type selector: "style_selector_t"

        :returns: 
        :rtype: None
        """
        ...

    def set_style_translate_x(self, value: int, selector: "style_selector_t") -> None:
        """
        :param value: 
        :type value: int
        :param selector: 
        :type selector: "style_selector_t"

        :returns: 
        :rtype: None
        """
        ...

    def set_style_translate_y(self, value: int, selector: "style_selector_t") -> None:
        """
        :param value: 
        :type value: int
        :param selector: 
        :type selector: "style_selector_t"

        :returns: 
        :rtype: None
        """
        ...

    def set_style_transform_scale_x(self, value: int, selector: "style_selector_t") -> None:
        """
        :param value: 
        :type value: int
        :param selector: 
        :type selector: "style_selector_t"

        :returns: 
        :rtype: None
        """
        ...

    def set_style_transform_scale_y(self, value: int, selector: "style_selector_t") -> None:
        """
        :param value: 
        :type value: int
        :param selector: 
        :type selector: "style_selector_t"

        :returns: 
        :rtype: None
        """
        ...

    def set_style_transform_rotation(self, value: int, selector: "style_selector_t") -> None:
        """
        :param value: 
        :type value: int
        :param selector: 
        :type selector: "style_selector_t"

        :returns: 
        :rtype: None
        """
        ...

    def set_style_transform_pivot_x(self, value: int, selector: "style_selector_t") -> None:
        """
        :param value: 
        :type value: int
        :param selector: 
        :type selector: "style_selector_t"

        :returns: 
        :rtype: None
        """
        ...

    def set_style_transform_pivot_y(self, value: int, selector: "style_selector_t") -> None:
        """
        :param value: 
        :type value: int
        :param selector: 
        :type selector: "style_selector_t"

        :returns: 
        :rtype: None
        """
        ...

    def set_style_transform_skew_x(self, value: int, selector: "style_selector_t") -> None:
        """
        :param value: 
        :type value: int
        :param selector: 
        :type selector: "style_selector_t"

        :returns: 
        :rtype: None
        """
        ...

    def set_style_transform_skew_y(self, value: int, selector: "style_selector_t") -> None:
        """
        :param value: 
        :type value: int
        :param selector: 
        :type selector: "style_selector_t"

        :returns: 
        :rtype: None
        """
        ...

    def set_style_pad_top(self, value: int, selector: "style_selector_t") -> None:
        """
        :param value: 
        :type value: int
        :param selector: 
        :type selector: "style_selector_t"

        :returns: 
        :rtype: None
        """
        ...

    def set_style_pad_bottom(self, value: int, selector: "style_selector_t") -> None:
        """
        :param value: 
        :type value: int
        :param selector: 
        :type selector: "style_selector_t"

        :returns: 
        :rtype: None
        """
        ...

    def set_style_pad_left(self, value: int, selector: "style_selector_t") -> None:
        """
        :param value: 
        :type value: int
        :param selector: 
        :type selector: "style_selector_t"

        :returns: 
        :rtype: None
        """
        ...

    def set_style_pad_right(self, value: int, selector: "style_selector_t") -> None:
        """
        :param value: 
        :type value: int
        :param selector: 
        :type selector: "style_selector_t"

        :returns: 
        :rtype: None
        """
        ...

    def set_style_pad_row(self, value: int, selector: "style_selector_t") -> None:
        """
        :param value: 
        :type value: int
        :param selector: 
        :type selector: "style_selector_t"

        :returns: 
        :rtype: None
        """
        ...

    def set_style_pad_column(self, value: int, selector: "style_selector_t") -> None:
        """
        :param value: 
        :type value: int
        :param selector: 
        :type selector: "style_selector_t"

        :returns: 
        :rtype: None
        """
        ...

    def set_style_margin_top(self, value: int, selector: "style_selector_t") -> None:
        """
        :param value: 
        :type value: int
        :param selector: 
        :type selector: "style_selector_t"

        :returns: 
        :rtype: None
        """
        ...

    def set_style_margin_bottom(self, value: int, selector: "style_selector_t") -> None:
        """
        :param value: 
        :type value: int
        :param selector: 
        :type selector: "style_selector_t"

        :returns: 
        :rtype: None
        """
        ...

    def set_style_margin_left(self, value: int, selector: "style_selector_t") -> None:
        """
        :param value: 
        :type value: int
        :param selector: 
        :type selector: "style_selector_t"

        :returns: 
        :rtype: None
        """
        ...

    def set_style_margin_right(self, value: int, selector: "style_selector_t") -> None:
        """
        :param value: 
        :type value: int
        :param selector: 
        :type selector: "style_selector_t"

        :returns: 
        :rtype: None
        """
        ...

    def set_style_bg_color(self, value: "color_t", selector: "style_selector_t") -> None:
        """
        :param value: 
        :type value: "color_t"
        :param selector: 
        :type selector: "style_selector_t"

        :returns: 
        :rtype: None
        """
        ...

    def set_style_bg_opa(self, value: opa_t, selector: "style_selector_t") -> None:
        """
        :param value: 
        :type value: opa_t
        :param selector: 
        :type selector: "style_selector_t"

        :returns: 
        :rtype: None
        """
        ...

    def set_style_bg_grad_color(self, value: "color_t", selector: "style_selector_t") -> None:
        """
        :param value: 
        :type value: "color_t"
        :param selector: 
        :type selector: "style_selector_t"

        :returns: 
        :rtype: None
        """
        ...

    def set_style_bg_grad_dir(self, value: grad_dir_t, selector: "style_selector_t") -> None:
        """
        :param value: 
        :type value: grad_dir_t
        :param selector: 
        :type selector: "style_selector_t"

        :returns: 
        :rtype: None
        """
        ...

    def set_style_bg_main_stop(self, value: int, selector: "style_selector_t") -> None:
        """
        :param value: 
        :type value: int
        :param selector: 
        :type selector: "style_selector_t"

        :returns: 
        :rtype: None
        """
        ...

    def set_style_bg_grad_stop(self, value: int, selector: "style_selector_t") -> None:
        """
        :param value: 
        :type value: int
        :param selector: 
        :type selector: "style_selector_t"

        :returns: 
        :rtype: None
        """
        ...

    def set_style_bg_main_opa(self, value: opa_t, selector: "style_selector_t") -> None:
        """
        :param value: 
        :type value: opa_t
        :param selector: 
        :type selector: "style_selector_t"

        :returns: 
        :rtype: None
        """
        ...

    def set_style_bg_grad_opa(self, value: opa_t, selector: "style_selector_t") -> None:
        """
        :param value: 
        :type value: opa_t
        :param selector: 
        :type selector: "style_selector_t"

        :returns: 
        :rtype: None
        """
        ...

    def set_style_bg_grad(self, value: "grad_dsc_t", selector: "style_selector_t") -> None:
        """
        :param value: 
        :type value: "grad_dsc_t"
        :param selector: 
        :type selector: "style_selector_t"

        :returns: 
        :rtype: None
        """
        ...

    def set_style_bg_image_src(self, value: Any, selector: "style_selector_t") -> None:
        """
        :param value: 
        :type value: Any
        :param selector: 
        :type selector: "style_selector_t"

        :returns: 
        :rtype: None
        """
        ...

    def set_style_bg_image_opa(self, value: opa_t, selector: "style_selector_t") -> None:
        """
        :param value: 
        :type value: opa_t
        :param selector: 
        :type selector: "style_selector_t"

        :returns: 
        :rtype: None
        """
        ...

    def set_style_bg_image_recolor(self, value: "color_t", selector: "style_selector_t") -> None:
        """
        :param value: 
        :type value: "color_t"
        :param selector: 
        :type selector: "style_selector_t"

        :returns: 
        :rtype: None
        """
        ...

    def set_style_bg_image_recolor_opa(self, value: opa_t, selector: "style_selector_t") -> None:
        """
        :param value: 
        :type value: opa_t
        :param selector: 
        :type selector: "style_selector_t"

        :returns: 
        :rtype: None
        """
        ...

    def set_style_bg_image_tiled(self, value: bool, selector: "style_selector_t") -> None:
        """
        :param value: 
        :type value: bool
        :param selector: 
        :type selector: "style_selector_t"

        :returns: 
        :rtype: None
        """
        ...

    def set_style_border_color(self, value: "color_t", selector: "style_selector_t") -> None:
        """
        :param value: 
        :type value: "color_t"
        :param selector: 
        :type selector: "style_selector_t"

        :returns: 
        :rtype: None
        """
        ...

    def set_style_border_opa(self, value: opa_t, selector: "style_selector_t") -> None:
        """
        :param value: 
        :type value: opa_t
        :param selector: 
        :type selector: "style_selector_t"

        :returns: 
        :rtype: None
        """
        ...

    def set_style_border_width(self, value: int, selector: "style_selector_t") -> None:
        """
        :param value: 
        :type value: int
        :param selector: 
        :type selector: "style_selector_t"

        :returns: 
        :rtype: None
        """
        ...

    def set_style_border_side(self, value: border_side_t, selector: "style_selector_t") -> None:
        """
        :param value: 
        :type value: border_side_t
        :param selector: 
        :type selector: "style_selector_t"

        :returns: 
        :rtype: None
        """
        ...

    def set_style_border_post(self, value: bool, selector: "style_selector_t") -> None:
        """
        :param value: 
        :type value: bool
        :param selector: 
        :type selector: "style_selector_t"

        :returns: 
        :rtype: None
        """
        ...

    def set_style_outline_width(self, value: int, selector: "style_selector_t") -> None:
        """
        :param value: 
        :type value: int
        :param selector: 
        :type selector: "style_selector_t"

        :returns: 
        :rtype: None
        """
        ...

    def set_style_outline_color(self, value: "color_t", selector: "style_selector_t") -> None:
        """
        :param value: 
        :type value: "color_t"
        :param selector: 
        :type selector: "style_selector_t"

        :returns: 
        :rtype: None
        """
        ...

    def set_style_outline_opa(self, value: opa_t, selector: "style_selector_t") -> None:
        """
        :param value: 
        :type value: opa_t
        :param selector: 
        :type selector: "style_selector_t"

        :returns: 
        :rtype: None
        """
        ...

    def set_style_outline_pad(self, value: int, selector: "style_selector_t") -> None:
        """
        :param value: 
        :type value: int
        :param selector: 
        :type selector: "style_selector_t"

        :returns: 
        :rtype: None
        """
        ...

    def set_style_shadow_width(self, value: int, selector: "style_selector_t") -> None:
        """
        :param value: 
        :type value: int
        :param selector: 
        :type selector: "style_selector_t"

        :returns: 
        :rtype: None
        """
        ...

    def set_style_shadow_offset_x(self, value: int, selector: "style_selector_t") -> None:
        """
        :param value: 
        :type value: int
        :param selector: 
        :type selector: "style_selector_t"

        :returns: 
        :rtype: None
        """
        ...

    def set_style_shadow_offset_y(self, value: int, selector: "style_selector_t") -> None:
        """
        :param value: 
        :type value: int
        :param selector: 
        :type selector: "style_selector_t"

        :returns: 
        :rtype: None
        """
        ...

    def set_style_shadow_spread(self, value: int, selector: "style_selector_t") -> None:
        """
        :param value: 
        :type value: int
        :param selector: 
        :type selector: "style_selector_t"

        :returns: 
        :rtype: None
        """
        ...

    def set_style_shadow_color(self, value: "color_t", selector: "style_selector_t") -> None:
        """
        :param value: 
        :type value: "color_t"
        :param selector: 
        :type selector: "style_selector_t"

        :returns: 
        :rtype: None
        """
        ...

    def set_style_shadow_opa(self, value: opa_t, selector: "style_selector_t") -> None:
        """
        :param value: 
        :type value: opa_t
        :param selector: 
        :type selector: "style_selector_t"

        :returns: 
        :rtype: None
        """
        ...

    def set_style_image_opa(self, value: opa_t, selector: "style_selector_t") -> None:
        """
        :param value: 
        :type value: opa_t
        :param selector: 
        :type selector: "style_selector_t"

        :returns: 
        :rtype: None
        """
        ...

    def set_style_image_recolor(self, value: "color_t", selector: "style_selector_t") -> None:
        """
        :param value: 
        :type value: "color_t"
        :param selector: 
        :type selector: "style_selector_t"

        :returns: 
        :rtype: None
        """
        ...

    def set_style_image_recolor_opa(self, value: opa_t, selector: "style_selector_t") -> None:
        """
        :param value: 
        :type value: opa_t
        :param selector: 
        :type selector: "style_selector_t"

        :returns: 
        :rtype: None
        """
        ...

    def set_style_line_width(self, value: int, selector: "style_selector_t") -> None:
        """
        :param value: 
        :type value: int
        :param selector: 
        :type selector: "style_selector_t"

        :returns: 
        :rtype: None
        """
        ...

    def set_style_line_dash_width(self, value: int, selector: "style_selector_t") -> None:
        """
        :param value: 
        :type value: int
        :param selector: 
        :type selector: "style_selector_t"

        :returns: 
        :rtype: None
        """
        ...

    def set_style_line_dash_gap(self, value: int, selector: "style_selector_t") -> None:
        """
        :param value: 
        :type value: int
        :param selector: 
        :type selector: "style_selector_t"

        :returns: 
        :rtype: None
        """
        ...

    def set_style_line_rounded(self, value: bool, selector: "style_selector_t") -> None:
        """
        :param value: 
        :type value: bool
        :param selector: 
        :type selector: "style_selector_t"

        :returns: 
        :rtype: None
        """
        ...

    def set_style_line_color(self, value: "color_t", selector: "style_selector_t") -> None:
        """
        :param value: 
        :type value: "color_t"
        :param selector: 
        :type selector: "style_selector_t"

        :returns: 
        :rtype: None
        """
        ...

    def set_style_line_opa(self, value: opa_t, selector: "style_selector_t") -> None:
        """
        :param value: 
        :type value: opa_t
        :param selector: 
        :type selector: "style_selector_t"

        :returns: 
        :rtype: None
        """
        ...

    def set_style_arc_width(self, value: int, selector: "style_selector_t") -> None:
        """
        :param value: 
        :type value: int
        :param selector: 
        :type selector: "style_selector_t"

        :returns: 
        :rtype: None
        """
        ...

    def set_style_arc_rounded(self, value: bool, selector: "style_selector_t") -> None:
        """
        :param value: 
        :type value: bool
        :param selector: 
        :type selector: "style_selector_t"

        :returns: 
        :rtype: None
        """
        ...

    def set_style_arc_color(self, value: "color_t", selector: "style_selector_t") -> None:
        """
        :param value: 
        :type value: "color_t"
        :param selector: 
        :type selector: "style_selector_t"

        :returns: 
        :rtype: None
        """
        ...

    def set_style_arc_opa(self, value: opa_t, selector: "style_selector_t") -> None:
        """
        :param value: 
        :type value: opa_t
        :param selector: 
        :type selector: "style_selector_t"

        :returns: 
        :rtype: None
        """
        ...

    def set_style_arc_image_src(self, value: Any, selector: "style_selector_t") -> None:
        """
        :param value: 
        :type value: Any
        :param selector: 
        :type selector: "style_selector_t"

        :returns: 
        :rtype: None
        """
        ...

    def set_style_text_color(self, value: "color_t", selector: "style_selector_t") -> None:
        """
        :param value: 
        :type value: "color_t"
        :param selector: 
        :type selector: "style_selector_t"

        :returns: 
        :rtype: None
        """
        ...

    def set_style_text_opa(self, value: opa_t, selector: "style_selector_t") -> None:
        """
        :param value: 
        :type value: opa_t
        :param selector: 
        :type selector: "style_selector_t"

        :returns: 
        :rtype: None
        """
        ...

    def set_style_text_font(self, value: "font_t", selector: "style_selector_t") -> None:
        """
        :param value: 
        :type value: "font_t"
        :param selector: 
        :type selector: "style_selector_t"

        :returns: 
        :rtype: None
        """
        ...

    def set_style_text_letter_space(self, value: int, selector: "style_selector_t") -> None:
        """
        :param value: 
        :type value: int
        :param selector: 
        :type selector: "style_selector_t"

        :returns: 
        :rtype: None
        """
        ...

    def set_style_text_line_space(self, value: int, selector: "style_selector_t") -> None:
        """
        :param value: 
        :type value: int
        :param selector: 
        :type selector: "style_selector_t"

        :returns: 
        :rtype: None
        """
        ...

    def set_style_text_decor(self, value: text_decor_t, selector: "style_selector_t") -> None:
        """
        :param value: 
        :type value: text_decor_t
        :param selector: 
        :type selector: "style_selector_t"

        :returns: 
        :rtype: None
        """
        ...

    def set_style_text_align(self, value: text_align_t, selector: "style_selector_t") -> None:
        """
        :param value: 
        :type value: text_align_t
        :param selector: 
        :type selector: "style_selector_t"

        :returns: 
        :rtype: None
        """
        ...

    def set_style_radius(self, value: int, selector: "style_selector_t") -> None:
        """
        :param value: 
        :type value: int
        :param selector: 
        :type selector: "style_selector_t"

        :returns: 
        :rtype: None
        """
        ...

    def set_style_clip_corner(self, value: bool, selector: "style_selector_t") -> None:
        """
        :param value: 
        :type value: bool
        :param selector: 
        :type selector: "style_selector_t"

        :returns: 
        :rtype: None
        """
        ...

    def set_style_opa(self, value: opa_t, selector: "style_selector_t") -> None:
        """
        :param value: 
        :type value: opa_t
        :param selector: 
        :type selector: "style_selector_t"

        :returns: 
        :rtype: None
        """
        ...

    def set_style_opa_layered(self, value: opa_t, selector: "style_selector_t") -> None:
        """
        :param value: 
        :type value: opa_t
        :param selector: 
        :type selector: "style_selector_t"

        :returns: 
        :rtype: None
        """
        ...

    def set_style_color_filter_dsc(self, value: "color_filter_dsc_t", selector: "style_selector_t") -> None:
        """
        :param value: 
        :type value: "color_filter_dsc_t"
        :param selector: 
        :type selector: "style_selector_t"

        :returns: 
        :rtype: None
        """
        ...

    def set_style_color_filter_opa(self, value: opa_t, selector: "style_selector_t") -> None:
        """
        :param value: 
        :type value: opa_t
        :param selector: 
        :type selector: "style_selector_t"

        :returns: 
        :rtype: None
        """
        ...

    def set_style_anim(self, value: anim_t, selector: "style_selector_t") -> None:
        """
        :param value: 
        :type value: anim_t
        :param selector: 
        :type selector: "style_selector_t"

        :returns: 
        :rtype: None
        """
        ...

    def set_style_anim_duration(self, value: int, selector: "style_selector_t") -> None:
        """
        :param value: 
        :type value: int
        :param selector: 
        :type selector: "style_selector_t"

        :returns: 
        :rtype: None
        """
        ...

    def set_style_transition(self, value: "style_transition_dsc_t", selector: "style_selector_t") -> None:
        """
        :param value: 
        :type value: "style_transition_dsc_t"
        :param selector: 
        :type selector: "style_selector_t"

        :returns: 
        :rtype: None
        """
        ...

    def set_style_blend_mode(self, value: blend_mode_t, selector: "style_selector_t") -> None:
        """
        :param value: 
        :type value: blend_mode_t
        :param selector: 
        :type selector: "style_selector_t"

        :returns: 
        :rtype: None
        """
        ...

    def set_style_layout(self, value: int, selector: "style_selector_t") -> None:
        """
        :param value: 
        :type value: int
        :param selector: 
        :type selector: "style_selector_t"

        :returns: 
        :rtype: None
        """
        ...

    def set_style_base_dir(self, value: base_dir_t, selector: "style_selector_t") -> None:
        """
        :param value: 
        :type value: base_dir_t
        :param selector: 
        :type selector: "style_selector_t"

        :returns: 
        :rtype: None
        """
        ...

    def set_style_bitmap_mask_src(self, value: Any, selector: "style_selector_t") -> None:
        """
        :param value: 
        :type value: Any
        :param selector: 
        :type selector: "style_selector_t"

        :returns: 
        :rtype: None
        """
        ...

    def set_style_rotary_sensitivity(self, value: int, selector: "style_selector_t") -> None:
        """
        :param value: 
        :type value: int
        :param selector: 
        :type selector: "style_selector_t"

        :returns: 
        :rtype: None
        """
        ...

    def set_style_flex_flow(self, value: flex_flow_t, selector: "style_selector_t") -> None:
        """
        :param value: 
        :type value: flex_flow_t
        :param selector: 
        :type selector: "style_selector_t"

        :returns: 
        :rtype: None
        """
        ...

    def set_style_flex_main_place(self, value: flex_align_t, selector: "style_selector_t") -> None:
        """
        :param value: 
        :type value: flex_align_t
        :param selector: 
        :type selector: "style_selector_t"

        :returns: 
        :rtype: None
        """
        ...

    def set_style_flex_cross_place(self, value: flex_align_t, selector: "style_selector_t") -> None:
        """
        :param value: 
        :type value: flex_align_t
        :param selector: 
        :type selector: "style_selector_t"

        :returns: 
        :rtype: None
        """
        ...

    def set_style_flex_track_place(self, value: flex_align_t, selector: "style_selector_t") -> None:
        """
        :param value: 
        :type value: flex_align_t
        :param selector: 
        :type selector: "style_selector_t"

        :returns: 
        :rtype: None
        """
        ...

    def set_style_flex_grow(self, value: int, selector: "style_selector_t") -> None:
        """
        :param value: 
        :type value: int
        :param selector: 
        :type selector: "style_selector_t"

        :returns: 
        :rtype: None
        """
        ...

    def set_style_grid_column_dsc_array(self, value: List[int], selector: "style_selector_t") -> None:
        """
        :param value: 
        :type value: List[int]
        :param selector: 
        :type selector: "style_selector_t"

        :returns: 
        :rtype: None
        """
        ...

    def set_style_grid_column_align(self, value: grid_align_t, selector: "style_selector_t") -> None:
        """
        :param value: 
        :type value: grid_align_t
        :param selector: 
        :type selector: "style_selector_t"

        :returns: 
        :rtype: None
        """
        ...

    def set_style_grid_row_dsc_array(self, value: List[int], selector: "style_selector_t") -> None:
        """
        :param value: 
        :type value: List[int]
        :param selector: 
        :type selector: "style_selector_t"

        :returns: 
        :rtype: None
        """
        ...

    def set_style_grid_row_align(self, value: grid_align_t, selector: "style_selector_t") -> None:
        """
        :param value: 
        :type value: grid_align_t
        :param selector: 
        :type selector: "style_selector_t"

        :returns: 
        :rtype: None
        """
        ...

    def set_style_grid_cell_column_pos(self, value: int, selector: "style_selector_t") -> None:
        """
        :param value: 
        :type value: int
        :param selector: 
        :type selector: "style_selector_t"

        :returns: 
        :rtype: None
        """
        ...

    def set_style_grid_cell_x_align(self, value: grid_align_t, selector: "style_selector_t") -> None:
        """
        :param value: 
        :type value: grid_align_t
        :param selector: 
        :type selector: "style_selector_t"

        :returns: 
        :rtype: None
        """
        ...

    def set_style_grid_cell_column_span(self, value: int, selector: "style_selector_t") -> None:
        """
        :param value: 
        :type value: int
        :param selector: 
        :type selector: "style_selector_t"

        :returns: 
        :rtype: None
        """
        ...

    def set_style_grid_cell_row_pos(self, value: int, selector: "style_selector_t") -> None:
        """
        :param value: 
        :type value: int
        :param selector: 
        :type selector: "style_selector_t"

        :returns: 
        :rtype: None
        """
        ...

    def set_style_grid_cell_y_align(self, value: grid_align_t, selector: "style_selector_t") -> None:
        """
        :param value: 
        :type value: grid_align_t
        :param selector: 
        :type selector: "style_selector_t"

        :returns: 
        :rtype: None
        """
        ...

    def set_style_grid_cell_row_span(self, value: int, selector: "style_selector_t") -> None:
        """
        :param value: 
        :type value: int
        :param selector: 
        :type selector: "style_selector_t"

        :returns: 
        :rtype: None
        """
        ...

    def calculate_style_text_align(self, part: part_t, txt: str) -> "text_align_t":
        """
        :param part: 
        :type part: part_t
        :param txt: 
        :type txt: str

        :returns: 
        :rtype: "text_align_t"
        """
        ...

    def get_style_opa_recursive(self, part: part_t) -> "opa_t":
        """
        Get the opa style property from all parents and multiply and >> 8 them. the final opacity considering the parents' opacity too 
        
        :param part: the part whose opacity should be get. Non-MAIN parts will consider the opa of the MAIN part too 
        :type part: part_t

        :returns: the final opacity considering the parents' opacity too 
        :rtype: "opa_t"
        """
        ...

    def init_draw_rect_dsc(self, part: part_t, draw_dsc: "draw_rect_dsc_t") -> None:
        """
        Initialize a rectangle draw descriptor from an object's styles in its current state Only the relevant fields will be set. E.g. if border width == 0 the other border properties won't be evaluated. 
        
        :param part: part of the object, e.g. LV_PART_MAIN , LV_PART_SCROLLBAR , LV_PART_KNOB , etc 
        :type part: part_t
        :param draw_dsc: the descriptor to initialize. If an ..._opa field is set to LV_OPA_TRANSP the related properties won't be initialized. Should be initialized with lv_draw_rect_dsc_init(draw_dsc) . 
        :type draw_dsc: "draw_rect_dsc_t"

        :returns: 
        :rtype: None
        """
        ...

    def init_draw_label_dsc(self, part: part_t, draw_dsc: "draw_label_dsc_t") -> None:
        """
        Initialize a label draw descriptor from an object's styles in its current state 
        
        :param part: part of the object, e.g. LV_PART_MAIN , LV_PART_SCROLLBAR , LV_PART_KNOB , etc 
        :type part: part_t
        :param draw_dsc: the descriptor to initialize. If the opa field is set to or the property is equal to LV_OPA_TRANSP the rest won't be initialized. Should be initialized with lv_draw_label_dsc_init(draw_dsc) . 
        :type draw_dsc: "draw_label_dsc_t"

        :returns: 
        :rtype: None
        """
        ...

    def init_draw_image_dsc(self, part: part_t, draw_dsc: "draw_image_dsc_t") -> None:
        """
        Initialize an image draw descriptor from an object's styles in its current state 
        
        :param part: part of the object, e.g. LV_PART_MAIN , LV_PART_SCROLLBAR , LV_PART_KNOB , etc 
        :type part: part_t
        :param draw_dsc: the descriptor to initialize. Should be initialized with lv_draw_image_dsc_init(draw_dsc) . 
        :type draw_dsc: "draw_image_dsc_t"

        :returns: 
        :rtype: None
        """
        ...

    def init_draw_line_dsc(self, part: part_t, draw_dsc: "draw_line_dsc_t") -> None:
        """
        Initialize a line draw descriptor from an object's styles in its current state 
        
        :param part: part of the object, e.g. LV_PART_MAIN , LV_PART_SCROLLBAR , LV_PART_KNOB , etc 
        :type part: part_t
        :param draw_dsc: the descriptor to initialize. Should be initialized with lv_draw_line_dsc_init(draw_dsc) . 
        :type draw_dsc: "draw_line_dsc_t"

        :returns: 
        :rtype: None
        """
        ...

    def init_draw_arc_dsc(self, part: part_t, draw_dsc: "draw_arc_dsc_t") -> None:
        """
        Initialize an arc draw descriptor from an object's styles in its current state 
        
        :param part: part of the object, e.g. LV_PART_MAIN , LV_PART_SCROLLBAR , LV_PART_KNOB , etc 
        :type part: part_t
        :param draw_dsc: the descriptor to initialize. Should be initialized with lv_draw_arc_dsc_init(draw_dsc) . 
        :type draw_dsc: "draw_arc_dsc_t"

        :returns: 
        :rtype: None
        """
        ...

    def calculate_ext_draw_size(self, part: part_t) -> int:
        """
        Get the required extra size (around the object's part) to draw shadow, outline, value etc. the extra size required around the object 
        
        :param part: part of the object 
        :type part: part_t

        :returns: the extra size required around the object 
        :rtype: int
        """
        ...

    def refresh_ext_draw_size(self) -> None:
        """
        Send a 'LV_EVENT_REFR_EXT_DRAW_SIZE' Call the ancestor's event handler to the object to refresh the value of the extended draw size. The result will be saved in obj . 
        

        :returns: 
        :rtype: None
        """
        ...

    def class_create_obj(self, parent: "obj") -> "obj":
        """
        Create an object form a class descriptor pointer to the created object 
        
        :param parent: pointer to an object where the new object should be created 
        :type parent: "obj"

        :returns: pointer to the created object 
        :rtype: "obj"
        """
        ...

    def class_init_obj(self) -> None:
        """

        :returns: 
        :rtype: None
        """
        ...

    def is_editable(self) -> bool:
        """

        :returns: 
        :rtype: bool
        """
        ...

    def is_group_def(self) -> bool:
        """

        :returns: 
        :rtype: bool
        """
        ...

    def send_event(self, event_code: "event_code_t", param: Any) -> "result_t":
        """
        Send an event to the object LV_RESULT_OK: obj was not deleted in the event; LV_RESULT_INVALID: obj was deleted in the event_code 
        
        :param event_code: the type of the event from :ref:`lv_event_t` 
        :type event_code: "event_code_t"
        :param param: arbitrary data depending on the widget type and the event. (Usually NULL ) 
        :type param: Any

        :returns: LV_RESULT_OK: obj was not deleted in the event; LV_RESULT_INVALID: obj was deleted in the event_code 
        :rtype: "result_t"
        """
        ...

    def event_base(self, e: event_t) -> "result_t":
        """
        Used by the widgets internally to call the ancestor widget types's event handler LV_RESULT_OK: the target object was not deleted in the event; LV_RESULT_INVALID: it was deleted in the event_code 
        
        :param e: pointer to the event descriptor 
        :type e: event_t

        :returns: LV_RESULT_OK: the target object was not deleted in the event; LV_RESULT_INVALID: it was deleted in the event_code 
        :rtype: "result_t"
        """
        ...

    def add_event_cb(self, event_cb: Callable[["event_t"], None], filter: "event_code_t", obj: "obj") -> "event_dsc_t":
        """
        Add an event handler function for an object. Used by the user to react on event which happens with the object. An object can have multiple event handler. They will be called in the same order as they were added. handler to the event. It can be used in lv_obj_remove_event_dsc . 
        
        :param event_cb: the new event function 
        :type event_cb: Callable[["event_t"], None]
        :param filter: an event code (e.g. LV_EVENT_CLICKED ) on which the event should be called. LV_EVENT_ALL can be used to receive all the events. 
        :type filter: "event_code_t"
        :param obj: custom data will be available in event_cb 
        :type obj: "obj"

        :returns: handler to the event. It can be used in lv_obj_remove_event_dsc . 
        :rtype: "event_dsc_t"
        """
        ...

    def get_event_count(self) -> int:
        """

        :returns: 
        :rtype: int
        """
        ...

    def get_event_dsc(self, index: int) -> "event_dsc_t":
        """
        :param index: 
        :type index: int

        :returns: 
        :rtype: "event_dsc_t"
        """
        ...

    def remove_event(self, index: int) -> bool:
        """
        :param index: 
        :type index: int

        :returns: 
        :rtype: bool
        """
        ...

    def remove_event_cb(self, event_cb: Callable[["event_t"], None]) -> bool:
        """
        :param event_cb: 
        :type event_cb: Callable[["event_t"], None]

        :returns: 
        :rtype: bool
        """
        ...

    def remove_event_dsc(self, dsc: "event_dsc_t") -> bool:
        """
        :param dsc: 
        :type dsc: "event_dsc_t"

        :returns: 
        :rtype: bool
        """
        ...

    def remove_event_cb_with_user_data(self, event_cb: Callable[["event_t"], None], obj: "obj") -> int:
        """
        Remove an event_cb with user_data the count of the event removed 
        
        :param event_cb: the event_cb of the event to remove 
        :type event_cb: Callable[["event_t"], None]
        :param obj: user_data 
        :type obj: "obj"

        :returns: the count of the event removed 
        :rtype: int
        """
        ...

    def add_flag(self, f: "obj") -> None:
        """
        Set one or more flags 
        
        :param f: OR-ed values from lv_obj_flag_t to set. 
        :type f: "obj"

        :returns: 
        :rtype: None
        """
        ...

    def remove_flag(self, f: "obj") -> None:
        """
        Remove one or more flags 
        
        :param f: OR-ed values from lv_obj_flag_t to clear. 
        :type f: "obj"

        :returns: 
        :rtype: None
        """
        ...

    def update_flag(self, f: "obj", v: bool) -> None:
        """
        Set add or remove one or more flags. 
        
        :param f: OR-ed values from lv_obj_flag_t to update. 
        :type f: "obj"
        :param v: true: add the flags; false: remove the flags 
        :type v: bool

        :returns: 
        :rtype: None
        """
        ...

    def add_state(self, state: state_t) -> None:
        """
        Add one or more states to the object. The other state bits will remain unchanged. If specified in the styles, transition animation will be started from the previous state to the current. 
        
        :param state: the states to add. E.g LV_STATE_PRESSED | LV_STATE_FOCUSED 
        :type state: state_t

        :returns: 
        :rtype: None
        """
        ...

    def remove_state(self, state: state_t) -> None:
        """
        Remove one or more states to the object. The other state bits will remain unchanged. If specified in the styles, transition animation will be started from the previous state to the current. 
        
        :param state: the states to add. E.g LV_STATE_PRESSED | LV_STATE_FOCUSED 
        :type state: state_t

        :returns: 
        :rtype: None
        """
        ...

    def set_state(self, state: state_t, v: bool) -> None:
        """
        Add or remove one or more states to the object. The other state bits will remain unchanged. 
        
        :param state: the states to add. E.g LV_STATE_PRESSED | LV_STATE_FOCUSED 
        :type state: state_t
        :param v: true: add the states; false: remove the states 
        :type v: bool

        :returns: 
        :rtype: None
        """
        ...

    def set_user_data(self, obj: "obj") -> None:
        """
        Set the user_data field of the object 
        
        :param obj: pointer to the new user_data. 
        :type obj: "obj"

        :returns: 
        :rtype: None
        """
        ...

    def has_flag(self, f: "obj") -> bool:
        """
        Check if a given flag or all the given flags are set on an object. true: all flags are set; false: not all flags are set 
        
        :param f: the flag(s) to check (OR-ed values can be used) 
        :type f: "obj"

        :returns: true: all flags are set; false: not all flags are set 
        :rtype: bool
        """
        ...

    def has_flag_any(self, f: "obj") -> bool:
        """
        Check if a given flag or any of the flags are set on an object. true: at least one flag is set; false: none of the flags are set 
        
        :param f: the flag(s) to check (OR-ed values can be used) 
        :type f: "obj"

        :returns: true: at least one flag is set; false: none of the flags are set 
        :rtype: bool
        """
        ...

    def get_state(self) -> "state_t":
        """
        Get the state of an object the state (OR-ed values from lv_state_t ) 
        

        :returns: the state (OR-ed values from lv_state_t ) 
        :rtype: "state_t"
        """
        ...

    def has_state(self, state: state_t) -> bool:
        """
        Check if the object is in a given state or not. true: obj is in state ; false: obj is not in state 
        
        :param state: a state or combination of states to check 
        :type state: state_t

        :returns: true: obj is in state ; false: obj is not in state 
        :rtype: bool
        """
        ...

    def get_group(self) -> "group_t":
        """
        Get the group of the object the pointer to group of the object 
        

        :returns: the pointer to group of the object 
        :rtype: "group_t"
        """
        ...

    def get_user_data(self) -> Any:
        """
        Get the user_data field of the object the pointer to the user_data of the object 
        

        :returns: the pointer to the user_data of the object 
        :rtype: Any
        """
        ...

    def allocate_spec_attr(self) -> None:
        """
        Allocate special data for an object if not allocated yet. 
        

        :returns: 
        :rtype: None
        """
        ...

    def check_type(self, class_p: "obj") -> bool:
        """
        Check the type of obj. true: class_p is the obj class. 
        
        :param class_p: a class to check (e.g. lv_slider_class ) 
        :type class_p: "obj"

        :returns: true: class_p is the obj class. 
        :rtype: bool
        """
        ...

    def has_class(self, class_p: "obj") -> bool:
        """
        Check if any object has a given class (type). It checks the ancestor classes too. true: obj has the given class 
        
        :param class_p: a class to check (e.g. lv_slider_class ) 
        :type class_p: "obj"

        :returns: true: obj has the given class 
        :rtype: bool
        """
        ...

    def get_class(self) -> "obj":
        """
        Get the class (type) of the object the class (type) of the object 
        

        :returns: the class (type) of the object 
        :rtype: "obj"
        """
        ...

    def is_valid(self) -> bool:
        """
        Check if any object is still "alive". true: valid 
        

        :returns: true: valid 
        :rtype: bool
        """
        ...

    def null_on_delete(self) -> None:
        """
        Utility to set an object reference to NULL when it gets deleted. The reference should be in a location that will not become invalid during the object's lifetime, i.e. static or allocated. 
        

        :returns: 
        :rtype: None
        """
        ...

    def set_id(self, obj: "obj") -> None:
        """

        :returns: 
        :rtype: None
        """
        ...

    def get_id(self) -> Any:
        """

        :returns: 
        :rtype: Any
        """
        ...

    def get_child_by_id(self, id: Any) -> "obj":
        """

        :returns: 
        :rtype: "obj"
        """
        ...

    def assign_id(self, obj: "obj") -> None:
        """

        :returns: 
        :rtype: None
        """
        ...

    def free_id(self) -> None:
        """

        :returns: 
        :rtype: None
        """
        ...

    def id_compare(self, id2: Any) -> int:
        """

        :returns: 
        :rtype: int
        """
        ...

    def stringify_id(self, buf: str, len: int) -> str:
        """

        :returns: 
        :rtype: str
        """
        ...

    def redraw(self, obj: "obj") -> None:
        """
        Redrawn on object and all its children using the passed draw context 
        
        :param obj: the start object from the redraw should start 
        :type obj: "obj"

        :returns: 
        :rtype: None
        """
        ...

    def remove_from_subject(self, subject: "subject_t") -> None:
        """
        Remove the observers of an object from a subject or all subjects This function can be used e.g. when an object's subject(s) needs to be replaced by other subject(s) 
        
        :param subject: the subject to remove the object from, or NULL to remove from all subjects 
        :type subject: "subject_t"

        :returns: 
        :rtype: None
        """
        ...

    def bind_flag_if_eq(self, subject: "subject_t", flag: "obj", ref_value: int) -> "observer_t":
        """
        Set an object flag if an integer subject's value is equal to a reference value, clear the flag otherwise pointer to the created observer 
        
        :param subject: pointer to a subject 
        :type subject: "subject_t"
        :param flag: flag to set or clear (e.g. LV_OBJ_FLAG_HIDDEN ) 
        :type flag: "obj"
        :param ref_value: reference value to compare the subject's value with 
        :type ref_value: int

        :returns: pointer to the created observer 
        :rtype: "observer_t"
        """
        ...

    def bind_flag_if_not_eq(self, subject: "subject_t", flag: "obj", ref_value: int) -> "observer_t":
        """
        Set an object flag if an integer subject's value is not equal to a reference value, clear the flag otherwise pointer to the created observer 
        
        :param subject: pointer to a subject 
        :type subject: "subject_t"
        :param flag: flag to set or clear (e.g. LV_OBJ_FLAG_HIDDEN ) 
        :type flag: "obj"
        :param ref_value: reference value to compare the subject's value with 
        :type ref_value: int

        :returns: pointer to the created observer 
        :rtype: "observer_t"
        """
        ...

    def bind_state_if_eq(self, subject: "subject_t", state: state_t, ref_value: int) -> "observer_t":
        """
        Set an object state if an integer subject's value is equal to a reference value, clear the flag otherwise pointer to the created observer 
        
        :param subject: pointer to a subject 
        :type subject: "subject_t"
        :param state: state to set or clear (e.g. LV_STATE_CHECKED ) 
        :type state: state_t
        :param ref_value: reference value to compare the subject's value with 
        :type ref_value: int

        :returns: pointer to the created observer 
        :rtype: "observer_t"
        """
        ...

    def bind_state_if_not_eq(self, subject: "subject_t", state: state_t, ref_value: int) -> "observer_t":
        """
        Set an object state if an integer subject's value is not equal to a reference value, clear the flag otherwise pointer to the created observer 
        
        :param subject: pointer to a subject 
        :type subject: "subject_t"
        :param state: state to set or clear (e.g. LV_STATE_CHECKED ) 
        :type state: state_t
        :param ref_value: reference value to compare the subject's value with 
        :type ref_value: int

        :returns: pointer to the created observer 
        :rtype: "observer_t"
        """
        ...

    def bind_checked(self, subject: "subject_t") -> "observer_t":
        """
        Set an integer subject to 1 when an object is checked and set it 0 when unchecked. pointer to the created observer  Ensure the object's LV_OBJ_FLAG_CHECKABLE flag is set 
        
        :param subject: pointer to a subject 
        :type subject: "subject_t"

        :returns: pointer to the created observer 
        :rtype: "observer_t"
        """
        ...



class image(obj):

    class FLAGS(object):

        PREMULTIPLIED: ClassVar[int] = ...
        COMPRESSED: ClassVar[int] = ...
        ALLOCATED: ClassVar[int] = ...
        MODIFIABLE: ClassVar[int] = ...
        USER1: ClassVar[int] = ...
        USER2: ClassVar[int] = ...
        USER3: ClassVar[int] = ...
        USER4: ClassVar[int] = ...
        USER5: ClassVar[int] = ...
        USER6: ClassVar[int] = ...
        USER7: ClassVar[int] = ...
        USER8: ClassVar[int] = ...
        
        def __init__(self, *, parent: "obj"):
            ...

    class COMPRESS(object):

        NONE: ClassVar[int] = ...
        RLE: ClassVar[int] = ...
        LZ4: ClassVar[int] = ...
        
        def __init__(self, *, parent: "obj"):
            ...

    class SRC(object):

        VARIABLE: ClassVar[int] = ...
        FILE: ClassVar[int] = ...
        SYMBOL: ClassVar[int] = ...
        UNKNOWN: ClassVar[int] = ...
        
        def __init__(self, *, parent: "obj"):
            ...

    class ALIGN(object):

        DEFAULT: ClassVar[int] = ...
        TOP_LEFT: ClassVar[int] = ...
        TOP_MID: ClassVar[int] = ...
        TOP_RIGHT: ClassVar[int] = ...
        BOTTOM_LEFT: ClassVar[int] = ...
        BOTTOM_MID: ClassVar[int] = ...
        BOTTOM_RIGHT: ClassVar[int] = ...
        LEFT_MID: ClassVar[int] = ...
        RIGHT_MID: ClassVar[int] = ...
        CENTER: ClassVar[int] = ...
        AUTO_TRANSFORM: ClassVar[int] = ...
        STRETCH: ClassVar[int] = ...
        TILE: ClassVar[int] = ...
        
        def __init__(self, *, parent: "obj"):
            ...

    
    def __init__(self, *, parent: "obj"):
        """
        Create an image object pointer to the created image 
        """
        ...

    def buf_set_palette(self, id: int, c: "color32_t") -> None:
        """
        Deprecated Use lv_draw_buf_set_palette instead. 
        
        :param id: 
        :type id: int
        :param c: 
        :type c: "color32_t"

        :returns: 
        :rtype: None
        """
        ...

    def buf_free(self) -> None:
        """
        Deprecated Use lv_draw_buffer_create/destroy instead. Free the data pointer and dsc struct of an image. 
        

        :returns: 
        :rtype: None
        """
        ...

    def cache_init(self) -> "result_t":
        """
        Initialize image cache. LV_RESULT_OK: initialization succeeded, LV_RESULT_INVALID: failed. 
        

        :returns: LV_RESULT_OK: initialization succeeded, LV_RESULT_INVALID: failed. 
        :rtype: "result_t"
        """
        ...

    def cache_resize(self, evict_now: bool) -> None:
        """
        Resize image cache. If set to 0, the cache will be disabled. 
        
        :param evict_now: true: evict the images should be removed by the eviction policy, false: wait for the next cache cleanup. 
        :type evict_now: bool

        :returns: 
        :rtype: None
        """
        ...

    def cache_drop(self) -> None:
        """
        Invalidate image cache. Use NULL to invalidate all images. 
        

        :returns: 
        :rtype: None
        """
        ...

    def cache_is_enabled(self) -> bool:
        """
        Return true if the image cache is enabled. true: enabled, false: disabled. 
        

        :returns: true: enabled, false: disabled. 
        :rtype: bool
        """
        ...

    def header_cache_init(self) -> "result_t":
        """
        Initialize image header cache. LV_RESULT_OK: initialization succeeded, LV_RESULT_INVALID: failed. 
        

        :returns: LV_RESULT_OK: initialization succeeded, LV_RESULT_INVALID: failed. 
        :rtype: "result_t"
        """
        ...

    def header_cache_resize(self, evict_now: bool) -> None:
        """
        Resize image header cache. If set to 0, the cache is disabled. 
        
        :param evict_now: true: evict the image headers should be removed by the eviction policy, false: wait for the next cache cleanup. 
        :type evict_now: bool

        :returns: 
        :rtype: None
        """
        ...

    def header_cache_drop(self) -> None:
        """
        Invalidate image header cache. Use NULL to invalidate all image headers. It's also automatically called when an image is invalidated. 
        

        :returns: 
        :rtype: None
        """
        ...

    def header_cache_is_enabled(self) -> bool:
        """
        Return true if the image header cache is enabled. true: enabled, false: disabled. 
        

        :returns: true: enabled, false: disabled. 
        :rtype: bool
        """
        ...

    def decoder_get_info(self, header: "image") -> "result_t":
        """
        Get information about an image. Try the created image decoder one by one. Once one is able to get info that info will be used. LV_RESULT_OK: success; LV_RESULT_INVALID: wasn't able to get info about the image 
        
        :param header: the image info will be stored here 
        :type header: "image"

        :returns: LV_RESULT_OK: success; LV_RESULT_INVALID: wasn't able to get info about the image 
        :rtype: "result_t"
        """
        ...

    def decoder_open(self, src: Any, args: "image") -> "result_t":
        """
        Open an image. Try the created image decoders one by one. Once one is able to open the image that decoder is saved in dsc  LV_RESULT_OK: opened the image. dsc->decoded and dsc->header are set. LV_RESULT_INVALID: none of the registered image decoders were able to open the image. 
        
        :param src: the image source. Can be 1) File name: E.g. "S:folder/img1.png" (The drivers needs to registered via :ref:`lv_fs_drv_register()` ) ) 2) Variable: Pointer to an :ref:`lv_image_dsc_t` variable 3) Symbol: E.g. LV_SYMBOL_OK 
        :type src: Any
        :param args: args about how the image should be opened. 
        :type args: "image"

        :returns: LV_RESULT_OK: opened the image. dsc->decoded and dsc->header are set. LV_RESULT_INVALID: none of the registered image decoders were able to open the image. 
        :rtype: "result_t"
        """
        ...

    def decoder_get_area(self, full_area: "area_t", decoded_area: "area_t") -> "result_t":
        """
        Decode full_area pixels incrementally by calling in a loop. Set decoded_area to LV_COORD_MIN on first call. LV_RESULT_OK: success; LV_RESULT_INVALID: an error occurred or there is nothing left to decode 
        
        :param full_area: input parameter. the full area to decode after enough subsequent calls 
        :type full_area: "area_t"
        :param decoded_area: input+output parameter. set the values to LV_COORD_MIN for the first call and to reset decoding. the decoded area is stored here after each call. 
        :type decoded_area: "area_t"

        :returns: LV_RESULT_OK: success; LV_RESULT_INVALID: an error occurred or there is nothing left to decode 
        :rtype: "result_t"
        """
        ...

    def decoder_close(self) -> None:
        """
        Close a decoding session 
        

        :returns: 
        :rtype: None
        """
        ...

    def decoder_create(self) -> "image":
        """
        Create a new image decoder pointer to the new image decoder 
        

        :returns: pointer to the new image decoder 
        :rtype: "image"
        """
        ...

    def decoder_delete(self) -> None:
        """
        Delete an image decoder 
        

        :returns: 
        :rtype: None
        """
        ...

    def decoder_get_next(self) -> "image":
        """
        Get the next image decoder in the linked list of image decoders the next image decoder or NULL if no more image decoder exists 
        

        :returns: the next image decoder or NULL if no more image decoder exists 
        :rtype: "image"
        """
        ...

    def decoder_set_info_cb(self, info_cb: Callable[["image", "image", "image"], "result_t"]) -> None:
        """
        Set a callback to get information about the image 
        
        :param info_cb: a function to collect info about an image (fill an :ref:`lv_image_header_t` struct) 
        :type info_cb: Callable[["image", "image", "image"], "result_t"]

        :returns: 
        :rtype: None
        """
        ...

    def decoder_set_open_cb(self, open_cb: Callable[["image", "image"], "result_t"]) -> None:
        """
        Set a callback to open an image 
        
        :param open_cb: a function to open an image 
        :type open_cb: Callable[["image", "image"], "result_t"]

        :returns: 
        :rtype: None
        """
        ...

    def decoder_set_get_area_cb(self, read_line_cb: Callable[["image", "image", "area_t", "area_t"], "result_t"]) -> None:
        """
        Set a callback to a decoded line of an image 
        
        :param read_line_cb: a function to read a line of an image 
        :type read_line_cb: Callable[["image", "image", "area_t", "area_t"], "result_t"]

        :returns: 
        :rtype: None
        """
        ...

    def decoder_set_close_cb(self, close_cb: Callable[["image", "image"], None]) -> None:
        """
        Set a callback to close a decoding session. E.g. close files and free other resources. 
        
        :param close_cb: a function to close a decoding session 
        :type close_cb: Callable[["image", "image"], None]

        :returns: 
        :rtype: None
        """
        ...

    def decoder_add_to_cache(self, search_key: "image", decoded: "draw_buf_t", decoder: "image") -> "cache_entry_t":
        """
        :param search_key: 
        :type search_key: "image"
        :param decoded: 
        :type decoded: "draw_buf_t"
        :param decoder: 
        :type decoder: "image"

        :returns: 
        :rtype: "cache_entry_t"
        """
        ...

    def decoder_post_process(self, decoded: "draw_buf_t") -> "draw_buf_t":
        """
        Check the decoded image, make any modification if decoder args requires. A new draw buf will be allocated if provided decoded is not modifiable or stride mismatch etc.  post processed draw buffer, when it differs with decoded , it's newly allocated. 
        
        :param decoded: pointer to a decoded image to post process to meet dsc->args requirement. 
        :type decoded: "draw_buf_t"

        :returns: post processed draw buffer, when it differs with decoded , it's newly allocated. 
        :rtype: "draw_buf_t"
        """
        ...

    def src_get_type(self) -> "image":
        """
        Get the type of an image source type of the image source LV_IMAGE_SRC_VARIABLE/FILE/SYMBOL/UNKNOWN 
        

        :returns: type of the image source LV_IMAGE_SRC_VARIABLE/FILE/SYMBOL/UNKNOWN 
        :rtype: "image"
        """
        ...

    def set_src(self, src: Any) -> None:
        """
        Set the image data to display on the object 
        
        :param src: 1) pointer to an :ref:`lv_image_dsc_t` descriptor (converted by LVGL's image converter) (e.g. &my_img) or 2) path to an image file (e.g. "S:/dir/img.bin")or 3) a SYMBOL (e.g. LV_SYMBOL_OK) 
        :type src: Any

        :returns: 
        :rtype: None
        """
        ...

    def set_offset_x(self, index: int) -> None:
        """
        Set an offset for the source of an image so the image will be displayed from the new origin. 
        
        :param index: the new offset along x axis. 
        :type index: int

        :returns: 
        :rtype: None
        """
        ...

    def set_offset_y(self, index: int) -> None:
        """
        Set an offset for the source of an image. so the image will be displayed from the new origin. 
        
        :param index: the new offset along y axis. 
        :type index: int

        :returns: 
        :rtype: None
        """
        ...

    def set_rotation(self, index: int) -> None:
        """
        Set the rotation angle of the image. The image will be rotated around the set pivot set by :ref:`lv_image_set_pivot()` Note that indexed and alpha only images can't be transformed. if image_align is LV_IMAGE_ALIGN_STRETCH or LV_IMAGE_ALIGN_FIT rotation will be set to 0 automatically. 
        
        :param index: rotation in degree with 0.1 degree resolution (0..3600: clock wise) 
        :type index: int

        :returns: 
        :rtype: None
        """
        ...

    def set_pivot(self, x: int, y: int) -> None:
        """
        Set the rotation center of the image. The image will be rotated around this point. x, y can be set with value of LV_PCT, lv_image_get_pivot will return the true pixel coordinate of pivot in this case. 
        
        :param x: rotation center x of the image 
        :type x: int
        :param y: rotation center y of the image 
        :type y: int

        :returns: 
        :rtype: None
        """
        ...

    def set_scale(self, delay_ms: int) -> None:
        """
        Set the zoom factor of the image. Note that indexed and alpha only images can't be transformed. 
        
        :param delay_ms: the zoom factor. Example values: 256 or LV_ZOOM_IMAGE_NONE: no zoom <256: scale down >256: scale up 128: half size 512: double size 
        :type delay_ms: int

        :returns: 
        :rtype: None
        """
        ...

    def set_scale_x(self, delay_ms: int) -> None:
        """
        Set the horizontal zoom factor of the image. Note that indexed and alpha only images can't be transformed. 
        
        :param delay_ms: the zoom factor. Example values: 256 or LV_ZOOM_IMAGE_NONE: no zoom <256: scale down >256: scale up 128: half size 512: double size 
        :type delay_ms: int

        :returns: 
        :rtype: None
        """
        ...

    def set_scale_y(self, delay_ms: int) -> None:
        """
        Set the vertical zoom factor of the image. Note that indexed and alpha only images can't be transformed. 
        
        :param delay_ms: the zoom factor. Example values: 256 or LV_ZOOM_IMAGE_NONE: no zoom <256: scale down >256: scale up 128: half size 512: double size 
        :type delay_ms: int

        :returns: 
        :rtype: None
        """
        ...

    def set_blend_mode(self, blend_mode: blend_mode_t) -> None:
        """
        Set the blend mode of an image. 
        
        :param blend_mode: the new blend mode 
        :type blend_mode: blend_mode_t

        :returns: 
        :rtype: None
        """
        ...

    def set_antialias(self, antialias: bool) -> None:
        """
        Enable/disable anti-aliasing for the transformations (rotate, zoom) or not. The quality is better with anti-aliasing looks better but slower. 
        
        :param antialias: true: anti-aliased; false: not anti-aliased 
        :type antialias: bool

        :returns: 
        :rtype: None
        """
        ...

    def set_inner_align(self, align: "image") -> None:
        """
        Set the image object size mode. if image_align is LV_IMAGE_ALIGN_STRETCH or LV_IMAGE_ALIGN_FIT rotation, scale and pivot will be overwritten and controlled internally. 
        
        :param align: the new align mode. 
        :type align: "image"

        :returns: 
        :rtype: None
        """
        ...

    def set_bitmap_map_src(self, src: "image") -> None:
        """
        Set an A8 bitmap mask for the image. 
        
        :param src: an :ref:`lv_image_dsc_t` bitmap mask source. 
        :type src: "image"

        :returns: 
        :rtype: None
        """
        ...

    def get_src(self) -> Any:
        """
        Get the source of the image the image source (symbol, file name or ::lv-img_dsc_t for C arrays) 
        

        :returns: the image source (symbol, file name or ::lv-img_dsc_t for C arrays) 
        :rtype: Any
        """
        ...

    def get_offset_x(self) -> int:
        """
        Get the offset's x attribute of the image object. offset X value. 
        

        :returns: offset X value. 
        :rtype: int
        """
        ...

    def get_offset_y(self) -> int:
        """
        Get the offset's y attribute of the image object. offset Y value. 
        

        :returns: offset Y value. 
        :rtype: int
        """
        ...

    def get_rotation(self) -> int:
        """
        Get the rotation of the image. rotation in 0.1 degrees (0..3600)  if image_align is LV_IMAGE_ALIGN_STRETCH or LV_IMAGE_ALIGN_FIT rotation will be set to 0 automatically. 
        

        :returns: rotation in 0.1 degrees (0..3600) 
        :rtype: int
        """
        ...

    def get_pivot(self, end: "point_t") -> None:
        """
        Get the pivot (rotation center) of the image. If pivot is set with LV_PCT, convert it to px before return. 
        
        :param end: store the rotation center here 
        :type end: "point_t"

        :returns: 
        :rtype: None
        """
        ...

    def get_scale(self) -> int:
        """
        Get the zoom factor of the image. zoom factor (256: no zoom) 
        

        :returns: zoom factor (256: no zoom) 
        :rtype: int
        """
        ...

    def get_scale_x(self) -> int:
        """
        Get the horizontal zoom factor of the image. zoom factor (256: no zoom) 
        

        :returns: zoom factor (256: no zoom) 
        :rtype: int
        """
        ...

    def get_scale_y(self) -> int:
        """
        Get the vertical zoom factor of the image. zoom factor (256: no zoom) 
        

        :returns: zoom factor (256: no zoom) 
        :rtype: int
        """
        ...

    def get_blend_mode(self) -> "blend_mode_t":
        """
        Get the current blend mode of the image the current blend mode 
        

        :returns: the current blend mode 
        :rtype: "blend_mode_t"
        """
        ...

    def get_antialias(self) -> bool:
        """
        Get whether the transformations (rotate, zoom) are anti-aliased or not true: anti-aliased; false: not anti-aliased 
        

        :returns: true: anti-aliased; false: not anti-aliased 
        :rtype: bool
        """
        ...

    def get_inner_align(self) -> "image":
        """
        Get the size mode of the image element of lv_image_align_t 
        

        :returns: element of lv_image_align_t 
        :rtype: "image"
        """
        ...

    def get_bitmap_map_src(self) -> "image":
        """
        Get the bitmap mask source. an :ref:`lv_image_dsc_t` bitmap mask source. 
        

        :returns: an :ref:`lv_image_dsc_t` bitmap mask source. 
        :rtype: "image"
        """
        ...



class animimg(obj):
    
    def __init__(self, *, parent: "obj"):
        """
        Create an animation image objects pointer to the created animation image object 
        """
        ...

    def set_src(self, dsc: Any, num: int) -> None:
        """
        Set the image animation images source. 
        
        :param dsc: pointer to a series images 
        :type dsc: Any
        :param num: images' number 
        :type num: int

        :returns: 
        :rtype: None
        """
        ...

    def start(self) -> None:
        """
        Startup the image animation. 
        

        :returns: 
        :rtype: None
        """
        ...

    def set_duration(self, delay_ms: int) -> None:
        """
        Set the image animation duration time. unit:ms 
        
        :param delay_ms: the duration in milliseconds 
        :type delay_ms: int

        :returns: 
        :rtype: None
        """
        ...

    def set_repeat_count(self, delay_ms: int) -> None:
        """
        Set the image animation repeatedly play times. 
        
        :param delay_ms: the number of times to repeat the animation 
        :type delay_ms: int

        :returns: 
        :rtype: None
        """
        ...

    def get_src_count(self) -> int:
        """
        Get the image animation images source. the number of source images 
        

        :returns: the number of source images 
        :rtype: int
        """
        ...

    def get_duration(self) -> int:
        """
        Get the image animation duration time. unit:ms the animation duration time 
        

        :returns: the animation duration time 
        :rtype: int
        """
        ...

    def get_repeat_count(self) -> int:
        """
        Get the image animation repeat play times. the repeat count 
        

        :returns: the repeat count 
        :rtype: int
        """
        ...

    def get_anim(self) -> "anim_t":
        """
        Get the image animation underlying animation. the animation reference 
        

        :returns: the animation reference 
        :rtype: "anim_t"
        """
        ...



class arc(obj):

    class MODE(object):

        NORMAL: ClassVar[int] = ...
        SYMMETRICAL: ClassVar[int] = ...
        REVERSE: ClassVar[int] = ...
        
        def __init__(self, *, parent: "obj"):
            ...

    
    def __init__(self, *, parent: "obj"):
        """
        Create an arc object pointer to the created arc 
        """
        ...

    def set_start_angle(self, start: "value_precise_t") -> None:
        """
        Set the start angle of an arc. 0 deg: right, 90 bottom, etc. 
        
        :param start: the start angle. (if LV_USE_FLOAT is enabled it can be fractional too.) 
        :type start: "value_precise_t"

        :returns: 
        :rtype: None
        """
        ...

    def set_end_angle(self, start: "value_precise_t") -> None:
        """
        Set the end angle of an arc. 0 deg: right, 90 bottom, etc. 
        
        :param start: the end angle (if LV_USE_FLOAT is enabled it can be fractional too.) 
        :type start: "value_precise_t"

        :returns: 
        :rtype: None
        """
        ...

    def set_angles(self, start: "value_precise_t", end: "value_precise_t") -> None:
        """
        Set the start and end angles 
        
        :param start: the start angle (if LV_USE_FLOAT is enabled it can be fractional too.) 
        :type start: "value_precise_t"
        :param end: the end angle (if LV_USE_FLOAT is enabled it can be fractional too.) 
        :type end: "value_precise_t"

        :returns: 
        :rtype: None
        """
        ...

    def set_bg_start_angle(self, start: "value_precise_t") -> None:
        """
        Set the start angle of an arc background. 0 deg: right, 90 bottom, etc. 
        
        :param start: the start angle (if LV_USE_FLOAT is enabled it can be fractional too.) 
        :type start: "value_precise_t"

        :returns: 
        :rtype: None
        """
        ...

    def set_bg_end_angle(self, start: "value_precise_t") -> None:
        """
        Set the start angle of an arc background. 0 deg: right, 90 bottom etc. 
        
        :param start: the end angle (if LV_USE_FLOAT is enabled it can be fractional too.) 
        :type start: "value_precise_t"

        :returns: 
        :rtype: None
        """
        ...

    def set_bg_angles(self, start: "value_precise_t", end: "value_precise_t") -> None:
        """
        Set the start and end angles of the arc background 
        
        :param start: the start angle (if LV_USE_FLOAT is enabled it can be fractional too.) 
        :type start: "value_precise_t"
        :param end: the end angle (if LV_USE_FLOAT is enabled it can be fractional too.) 
        :type end: "value_precise_t"

        :returns: 
        :rtype: None
        """
        ...

    def set_rotation(self, index: int) -> None:
        """
        Set the rotation for the whole arc 
        
        :param index: rotation angle 
        :type index: int

        :returns: 
        :rtype: None
        """
        ...

    def set_mode(self, type: "arc") -> None:
        """
        Set the type of arc. 
        
        :param type: arc's mode 
        :type type: "arc"

        :returns: 
        :rtype: None
        """
        ...

    def set_value(self, index: int) -> None:
        """
        Set a new value on the arc 
        
        :param index: new value 
        :type index: int

        :returns: 
        :rtype: None
        """
        ...

    def set_range(self, x: int, y: int) -> None:
        """
        Set minimum and the maximum values of an arc 
        
        :param x: minimum value 
        :type x: int
        :param y: maximum value 
        :type y: int

        :returns: 
        :rtype: None
        """
        ...

    def set_change_rate(self, delay_ms: int) -> None:
        """
        Set a change rate to limit the speed how fast the arc should reach the pressed point. 
        
        :param delay_ms: the change rate 
        :type delay_ms: int

        :returns: 
        :rtype: None
        """
        ...

    def set_knob_offset(self, index: int) -> None:
        """
        Set an offset angle for the knob 
        
        :param index: knob offset from main arc in degrees 
        :type index: int

        :returns: 
        :rtype: None
        """
        ...

    def get_angle_start(self) -> "value_precise_t":
        """
        Get the start angle of an arc. the start angle 0..360 
        

        :returns: the start angle 0..360 
        :rtype: "value_precise_t"
        """
        ...

    def get_angle_end(self) -> "value_precise_t":
        """
        Get the end angle of an arc. the end angle 0..360 
        

        :returns: the end angle 0..360 
        :rtype: "value_precise_t"
        """
        ...

    def get_bg_angle_start(self) -> "value_precise_t":
        """
        Get the start angle of an arc background. the start angle 0..360 
        

        :returns: the start angle 0..360 
        :rtype: "value_precise_t"
        """
        ...

    def get_bg_angle_end(self) -> "value_precise_t":
        """
        Get the end angle of an arc background. the end angle 0..360 
        

        :returns: the end angle 0..360 
        :rtype: "value_precise_t"
        """
        ...

    def get_value(self) -> int:
        """
        Get the value of an arc the value of the arc 
        

        :returns: the value of the arc 
        :rtype: int
        """
        ...

    def get_min_value(self) -> int:
        """
        Get the minimum value of an arc the minimum value of the arc 
        

        :returns: the minimum value of the arc 
        :rtype: int
        """
        ...

    def get_max_value(self) -> int:
        """
        Get the maximum value of an arc the maximum value of the arc 
        

        :returns: the maximum value of the arc 
        :rtype: int
        """
        ...

    def get_mode(self) -> "arc":
        """
        Get whether the arc is type or not. arc's mode 
        

        :returns: arc's mode 
        :rtype: "arc"
        """
        ...

    def get_rotation(self) -> int:
        """
        Get the rotation for the whole arc arc's current rotation 
        

        :returns: arc's current rotation 
        :rtype: int
        """
        ...

    def get_knob_offset(self) -> int:
        """
        Get the current knob angle offset arc's current knob offset 
        

        :returns: arc's current knob offset 
        :rtype: int
        """
        ...

    def align_obj_to_angle(self, obj_to_align: "obj", r_offset: int) -> None:
        """
        Align an object to the current position of the arc (knob) 
        
        :param obj_to_align: pointer to an object to align 
        :type obj_to_align: "obj"
        :param r_offset: consider the radius larger with this value (< 0: for smaller radius) 
        :type r_offset: int

        :returns: 
        :rtype: None
        """
        ...

    def rotate_obj_to_angle(self, obj_to_align: "obj", r_offset: int) -> None:
        """
        Rotate an object to the current position of the arc (knob) 
        
        :param obj_to_align: pointer to an object to rotate 
        :type obj_to_align: "obj"
        :param r_offset: consider the radius larger with this value (< 0: for smaller radius) 
        :type r_offset: int

        :returns: 
        :rtype: None
        """
        ...

    def bind_value(self, subject: "subject_t") -> "observer_t":
        """
        Bind an integer subject to an arc's value pointer to the created observer 
        
        :param subject: pointer to a subject 
        :type subject: "subject_t"

        :returns: pointer to the created observer 
        :rtype: "observer_t"
        """
        ...



class label(obj):

    class LONG(object):

        WRAP: ClassVar[int] = ...
        DOT: ClassVar[int] = ...
        SCROLL: ClassVar[int] = ...
        SCROLL_CIRCULAR: ClassVar[int] = ...
        CLIP: ClassVar[int] = ...
        
        def __init__(self, *, parent: "obj"):
            ...

    
    def __init__(self, *, parent: "obj"):
        """
        Create a label object pointer to the created button 
        """
        ...

    def set_text(self, text: str) -> None:
        """
        Set a new text for a label. Memory will be allocated to store the text by the label. 
        
        :param text: '\0' terminated character string. NULL to refresh with the current text. 
        :type text: str

        :returns: 
        :rtype: None
        """
        ...

    def set_text_static(self, text: str) -> None:
        """
        Set a static text. It will not be saved by the label so the 'text' variable has to be 'alive' while the label exists. 
        
        :param text: pointer to a text. NULL to refresh with the current text. 
        :type text: str

        :returns: 
        :rtype: None
        """
        ...

    def set_long_mode(self, long_mode: "label") -> None:
        """
        Set the behavior of the label with text longer than the object size 
        
        :param long_mode: the new mode from 'lv_label_long_mode' enum. In LV_LONG_WRAP/DOT/SCROLL/SCROLL_CIRC the size of the label should be set AFTER this function 
        :type long_mode: "label"

        :returns: 
        :rtype: None
        """
        ...

    def set_text_selection_start(self, delay_ms: int) -> None:
        """
        Set where text selection should start 
        
        :param delay_ms: character index from where selection should start. LV_LABEL_TEXT_SELECTION_OFF for no selection 
        :type delay_ms: int

        :returns: 
        :rtype: None
        """
        ...

    def set_text_selection_end(self, delay_ms: int) -> None:
        """
        Set where text selection should end 
        
        :param delay_ms: character index where selection should end. LV_LABEL_TEXT_SELECTION_OFF for no selection 
        :type delay_ms: int

        :returns: 
        :rtype: None
        """
        ...

    def get_text(self) -> str:
        """
        Get the text of a label the text of the label 
        

        :returns: the text of the label 
        :rtype: str
        """
        ...

    def get_long_mode(self) -> "label":
        """
        Get the long mode of a label the current long mode 
        

        :returns: the current long mode 
        :rtype: "label"
        """
        ...

    def get_letter_pos(self, char_id: int, pos: "point_t") -> None:
        """
        Get the relative x and y coordinates of a letter 
        
        :param char_id: index of the character [0 ... text length - 1]. Expressed in character index, not byte index (different in UTF-8) 
        :type char_id: int
        :param pos: store the result here (E.g. index = 0 gives 0;0 coordinates if the text if aligned to the left) 
        :type pos: "point_t"

        :returns: 
        :rtype: None
        """
        ...

    def get_letter_on(self, pos_in: "point_t", bidi: bool) -> int:
        """
        Get the index of letter on a relative point of a label. The index of the letter on the 'pos_p' point (E.g. on 0;0 is the 0. letter if aligned to the left) Expressed in character index and not byte index (different in UTF-8) 
        
        :param pos_in: pointer to point with coordinates on a the label 
        :type pos_in: "point_t"
        :param bidi: whether to use bidi processed 
        :type bidi: bool

        :returns: The index of the letter on the 'pos_p' point (E.g. on 0;0 is the 0. letter if aligned to the left) Expressed in character index and not byte index (different in UTF-8) 
        :rtype: int
        """
        ...

    def is_char_under_pos(self, pos: "point_t") -> bool:
        """
        Check if a character is drawn under a point. whether a character is drawn under the point 
        
        :param pos: Point to check for character under 
        :type pos: "point_t"

        :returns: whether a character is drawn under the point 
        :rtype: bool
        """
        ...

    def get_text_selection_start(self) -> int:
        """
        selection start index. LV_LABEL_TEXT_SELECTION_OFF if nothing is selected. 
        

        :returns: selection start index. LV_LABEL_TEXT_SELECTION_OFF if nothing is selected. 
        :rtype: int
        """
        ...

    def get_text_selection_end(self) -> int:
        """
        selection end index. LV_LABEL_TXT_SEL_OFF if nothing is selected. 
        

        :returns: selection end index. LV_LABEL_TXT_SEL_OFF if nothing is selected. 
        :rtype: int
        """
        ...

    def ins_text(self, pos: int, txt: str) -> None:
        """
        Insert a text to a label. The label text cannot be static. 
        
        :param pos: character index to insert. Expressed in character index and not byte index. 0: before first char. LV_LABEL_POS_LAST: after last char. 
        :type pos: int
        :param txt: pointer to the text to insert 
        :type txt: str

        :returns: 
        :rtype: None
        """
        ...

    def cut_text(self, time: int, delay: int) -> None:
        """
        Delete characters from a label. The label text cannot be static. 
        
        :param time: character index from where to cut. Expressed in character index and not byte index. 0: start in front of the first character 
        :type time: int
        :param delay: number of characters to cut 
        :type delay: int

        :returns: 
        :rtype: None
        """
        ...

    def bind_text(self, subject: "subject_t", fmt: str) -> "observer_t":
        """
        Bind an integer, string, or pointer subject to a label. pointer to the created observer  fmt == NULL can be used only with string and pointer subjects.  if the subject is a pointer must point to a \0 terminated string. 
        
        :param subject: pointer to a subject 
        :type subject: "subject_t"
        :param fmt: optional format string with 1 format specifier (e.g. "%d °C") or NULL to bind the value directly. 
        :type fmt: str

        :returns: pointer to the created observer 
        :rtype: "observer_t"
        """
        ...



class bar(obj):

    class MODE(object):

        NORMAL: ClassVar[int] = ...
        SYMMETRICAL: ClassVar[int] = ...
        RANGE: ClassVar[int] = ...
        
        def __init__(self, *, parent: "obj"):
            ...

    class ORIENTATION(object):

        AUTO: ClassVar[int] = ...
        HORIZONTAL: ClassVar[int] = ...
        VERTICAL: ClassVar[int] = ...
        
        def __init__(self, *, parent: "obj"):
            ...

    
    def __init__(self, *, parent: "obj"):
        """
        Create a bar object pointer to the created bar 
        """
        ...

    def set_value(self, x: int, anim_en: "anim_enable_t") -> None:
        """
        Set a new value on the bar 
        
        :param x: new value 
        :type x: int
        :param anim_en: LV_ANIM_ON: set the value with an animation; LV_ANIM_OFF: change the value immediately 
        :type anim_en: "anim_enable_t"

        :returns: 
        :rtype: None
        """
        ...

    def set_start_value(self, x: int, anim_en: "anim_enable_t") -> None:
        """
        Set a new start value on the bar 
        
        :param x: new start value 
        :type x: int
        :param anim_en: LV_ANIM_ON: set the value with an animation; LV_ANIM_OFF: change the value immediately 
        :type anim_en: "anim_enable_t"

        :returns: 
        :rtype: None
        """
        ...

    def set_range(self, x: int, y: int) -> None:
        """
        Set minimum and the maximum values of a bar If min is greater than max, the drawing direction becomes to the opposite direction. 
        
        :param x: minimum value 
        :type x: int
        :param y: maximum value 
        :type y: int

        :returns: 
        :rtype: None
        """
        ...

    def set_mode(self, mode: "bar") -> None:
        """
        Set the type of bar. 
        
        :param mode: bar type from ::lv_bar_mode_t 
        :type mode: "bar"

        :returns: 
        :rtype: None
        """
        ...

    def set_orientation(self, orientation: "bar") -> None:
        """
        Set the orientation of bar. 
        
        :param orientation: bar orientation from lv_bar_orientation_t 
        :type orientation: "bar"

        :returns: 
        :rtype: None
        """
        ...

    def get_value(self) -> int:
        """
        Get the value of a bar the value of the bar 
        

        :returns: the value of the bar 
        :rtype: int
        """
        ...

    def get_start_value(self) -> int:
        """
        Get the start value of a bar the start value of the bar 
        

        :returns: the start value of the bar 
        :rtype: int
        """
        ...

    def get_min_value(self) -> int:
        """
        Get the minimum value of a bar the minimum value of the bar 
        

        :returns: the minimum value of the bar 
        :rtype: int
        """
        ...

    def get_max_value(self) -> int:
        """
        Get the maximum value of a bar the maximum value of the bar 
        

        :returns: the maximum value of the bar 
        :rtype: int
        """
        ...

    def get_mode(self) -> "bar":
        """
        Get the type of bar. bar type from ::lv_bar_mode_t 
        

        :returns: bar type from ::lv_bar_mode_t 
        :rtype: "bar"
        """
        ...

    def get_orientation(self) -> "bar":
        """
        Get the orientation of bar. bar orientation from ::lv_bar_orientation_t 
        

        :returns: bar orientation from ::lv_bar_orientation_t 
        :rtype: "bar"
        """
        ...

    def is_symmetrical(self) -> bool:
        """
        Give the bar is in symmetrical mode or not true: in symmetrical mode false : not in 
        

        :returns: true: in symmetrical mode false : not in 
        :rtype: bool
        """
        ...



class button(obj):
    
    def __init__(self, *, parent: "obj"):
        """
        Create a button object pointer to the created button 
        """
        ...


class buttonmatrix(obj):

    class CTRL(object):

        HIDDEN: ClassVar[int] = ...
        NO_REPEAT: ClassVar[int] = ...
        DISABLED: ClassVar[int] = ...
        CHECKABLE: ClassVar[int] = ...
        CHECKED: ClassVar[int] = ...
        CLICK_TRIG: ClassVar[int] = ...
        POPOVER: ClassVar[int] = ...
        RESERVED_1: ClassVar[int] = ...
        RESERVED_2: ClassVar[int] = ...
        RESERVED_3: ClassVar[int] = ...
        CUSTOM_1: ClassVar[int] = ...
        CUSTOM_2: ClassVar[int] = ...
        
        def __init__(self, *, parent: "obj"):
            ...

    
    def __init__(self, *, parent: "obj"):
        """
        Create a button matrix object pointer to the created button matrix 
        """
        ...

    def set_map(self, map: List[str]) -> None:
        """
        Set a new map. Buttons will be created/deleted according to the map. The button matrix keeps a reference to the map and so the string array must not be deallocated during the life of the matrix. 
        
        :param map: pointer a string array. The last string has to be: "". Use "\n" to make a line break. 
        :type map: List[str]

        :returns: 
        :rtype: None
        """
        ...

    def set_ctrl_map(self, ctrl_map: List["buttonmatrix"]) -> None:
        """
        Set the button control map (hidden, disabled etc.) for a button matrix. The control map array will be copied and so may be deallocated after this function returns. 
        
        :param ctrl_map: pointer to an array of lv_button_ctrl_t control bytes. The length of the array and position of the elements must match the number and order of the individual buttons (i.e. excludes newline entries). An element of the map should look like e.g.: ctrl_map[0] = width | LV_BUTTONMATRIX_CTRL_NO_REPEAT | LV_BUTTONMATRIX_CTRL_TGL_ENABLE 
        :type ctrl_map: List["buttonmatrix"]

        :returns: 
        :rtype: None
        """
        ...

    def set_selected_button(self, delay_ms: int) -> None:
        """
        Set the selected buttons 
        
        :param delay_ms: 0 based index of the button to modify. (Not counting new lines) 
        :type delay_ms: int

        :returns: 
        :rtype: None
        """
        ...

    def set_button_ctrl(self, btn_id: int, ctrl: "buttonmatrix") -> None:
        """
        Set the attributes of a button of the button matrix 
        
        :param btn_id: 0 based index of the button to modify. (Not counting new lines) 
        :type btn_id: int
        :param ctrl: OR-ed attributes. E.g. LV_BUTTONMATRIX_CTRL_NO_REPEAT | LV_BUTTONMATRIX_CTRL_CHECKABLE 
        :type ctrl: "buttonmatrix"

        :returns: 
        :rtype: None
        """
        ...

    def clear_button_ctrl(self, btn_id: int, ctrl: "buttonmatrix") -> None:
        """
        Clear the attributes of a button of the button matrix 
        
        :param btn_id: 0 based index of the button to modify. (Not counting new lines) 
        :type btn_id: int
        :param ctrl: OR-ed attributes. E.g. LV_BUTTONMATRIX_CTRL_NO_REPEAT | LV_BUTTONMATRIX_CTRL_CHECKABLE 
        :type ctrl: "buttonmatrix"

        :returns: 
        :rtype: None
        """
        ...

    def set_button_ctrl_all(self, ctrl: "buttonmatrix") -> None:
        """
        Set attributes of all buttons of a button matrix 
        
        :param ctrl: attribute(s) to set from lv_buttonmatrix_ctrl_t . Values can be ORed. 
        :type ctrl: "buttonmatrix"

        :returns: 
        :rtype: None
        """
        ...

    def clear_button_ctrl_all(self, ctrl: "buttonmatrix") -> None:
        """
        Clear the attributes of all buttons of a button matrix 
        
        :param ctrl: attribute(s) to set from lv_buttonmatrix_ctrl_t . Values can be ORed. 
        :type ctrl: "buttonmatrix"

        :returns: 
        :rtype: None
        """
        ...

    def set_button_width(self, time: int, delay: int) -> None:
        """
        Set a single button's relative width. This method will cause the matrix be regenerated and is a relatively expensive operation. It is recommended that initial width be specified using lv_buttonmatrix_set_ctrl_map and this method only be used for dynamic changes. 
        
        :param time: 0 based index of the button to modify. 
        :type time: int
        :param delay: relative width compared to the buttons in the same row. [1..15] 
        :type delay: int

        :returns: 
        :rtype: None
        """
        ...

    def set_one_checked(self, antialias: bool) -> None:
        """
        Make the button matrix like a selector widget (only one button may be checked at a time). LV_BUTTONMATRIX_CTRL_CHECKABLE must be enabled on the buttons to be selected using lv_buttonmatrix_set_ctrl() or :ref:`lv_buttonmatrix_set_button_ctrl_all()` . 
        
        :param antialias: whether "one check" mode is enabled 
        :type antialias: bool

        :returns: 
        :rtype: None
        """
        ...

    def get_selected_button(self) -> int:
        """
        Get the index of the lastly "activated" button by the user (pressed, released, focused etc) Useful in the event_cb to get the text of the button, check if hidden etc. index of the last released button (LV_BUTTONMATRIX_BUTTON_NONE: if unset) 
        

        :returns: index of the last released button (LV_BUTTONMATRIX_BUTTON_NONE: if unset) 
        :rtype: int
        """
        ...

    def get_button_text(self, btn_id: int) -> str:
        """
        Get the button's text text of btn_index` button 
        
        :param btn_id: the index a button not counting new line characters. 
        :type btn_id: int

        :returns: text of btn_index` button 
        :rtype: str
        """
        ...

    def has_button_ctrl(self, btn_id: int, ctrl: "buttonmatrix") -> bool:
        """
        Get the whether a control value is enabled or disabled for button of a button matrix true: the control attribute is enabled false: disabled 
        
        :param btn_id: the index of a button not counting new line characters. 
        :type btn_id: int
        :param ctrl: control values to check (ORed value can be used) 
        :type ctrl: "buttonmatrix"

        :returns: true: the control attribute is enabled false: disabled 
        :rtype: bool
        """
        ...

    def get_one_checked(self) -> bool:
        """
        Tell whether "one check" mode is enabled or not. true: "one check" mode is enabled; false: disabled 
        

        :returns: true: "one check" mode is enabled; false: disabled 
        :rtype: bool
        """
        ...



class calendar(obj):
    
    def __init__(self, *, parent: "obj"):
        """
        Create a calendar widget pointer the created calendar 
        """
        ...

    def set_today_date(self, year: int, month: int, day: int) -> None:
        """
        Set the today's date 
        
        :param year: today's year 
        :type year: int
        :param month: today's month [1..12] 
        :type month: int
        :param day: today's day [1..31] 
        :type day: int

        :returns: 
        :rtype: None
        """
        ...

    def set_showed_date(self, time: int, delay: int) -> None:
        """
        Set the currently showed 
        
        :param time: today's year 
        :type time: int
        :param delay: today's month [1..12] 
        :type delay: int

        :returns: 
        :rtype: None
        """
        ...

    def set_highlighted_dates(self, highlighted: List["calendar"], date_num: int) -> None:
        """
        Set the highlighted dates 
        
        :param highlighted: pointer to an :ref:`lv_calendar_date_t` array containing the dates. Only the pointer will be saved so this variable can't be local which will be destroyed later. 
        :type highlighted: List["calendar"]
        :param date_num: number of dates in the array 
        :type date_num: int

        :returns: 
        :rtype: None
        """
        ...

    def set_day_names(self, day_names: List[str]) -> None:
        """
        Set the name of the days 
        
        :param day_names: pointer to an array with the names. E.g. const char * days[7] = {"Sun", "Mon", ...} Only the pointer will be saved so this variable can't be local which will be destroyed later. 
        :type day_names: List[str]

        :returns: 
        :rtype: None
        """
        ...

    def get_btnmatrix(self) -> "obj":
        """
        Get the button matrix object of the calendar. It shows the dates and day names. pointer to a the button matrix 
        

        :returns: pointer to a the button matrix 
        :rtype: "obj"
        """
        ...

    def get_today_date(self) -> "calendar":
        """
        Get the today's date return pointer to an :ref:`lv_calendar_date_t` variable containing the date of today. 
        

        :returns: return pointer to an :ref:`lv_calendar_date_t` variable containing the date of today. 
        :rtype: "calendar"
        """
        ...

    def get_showed_date(self) -> "calendar":
        """
        Get the currently showed pointer to an :ref:`lv_calendar_date_t` variable containing the date is being shown. 
        

        :returns: pointer to an :ref:`lv_calendar_date_t` variable containing the date is being shown. 
        :rtype: "calendar"
        """
        ...

    def get_highlighted_dates(self) -> "calendar":
        """
        Get the highlighted dates pointer to an :ref:`lv_calendar_date_t` array containing the dates. 
        

        :returns: pointer to an :ref:`lv_calendar_date_t` array containing the dates. 
        :rtype: "calendar"
        """
        ...

    def get_highlighted_dates_num(self) -> int:
        """
        Get the number of the highlighted dates number of highlighted days 
        

        :returns: number of highlighted days 
        :rtype: int
        """
        ...

    def get_pressed_date(self, date: "calendar") -> "result_t":
        """
        Get the currently pressed day LV_RESULT_OK: there is a valid pressed date LV_RESULT_INVALID: there is no pressed data 
        
        :param date: store the pressed date here 
        :type date: "calendar"

        :returns: LV_RESULT_OK: there is a valid pressed date LV_RESULT_INVALID: there is no pressed data 
        :rtype: "result_t"
        """
        ...

    def header_dropdown_set_year_list(self, text: str) -> None:
        """
        Sets a custom calendar year list 
        
        :param text: pointer to an const char array with the years list, see lv_dropdown set_options for more information. E.g. `const char * years = "2023\n2022\n2021\n2020\n2019" Only the pointer will be saved so this variable can't be local which will be destroyed later. 
        :type text: str

        :returns: 
        :rtype: None
        """
        ...



class calendar_header_arrow(obj):
    
    def __init__(self, *, parent: "obj"):
        """
        Create a calendar header with drop-drowns to select the year and month the created header 
        """
        ...


class calendar_header_dropdown(obj):
    
    def __init__(self, *, parent: "obj"):
        """
        Create a calendar header with drop-drowns to select the year and month the created header 
        """
        ...

    def header_dropdown_set_year_list(self, text: str) -> None:
        """
        Sets a custom calendar year list 
        
        :param text: pointer to an const char array with the years list, see lv_dropdown set_options for more information. E.g. `const char * years = "2023\n2022\n2021\n2020\n2019" Only the pointer will be saved so this variable can't be local which will be destroyed later. 
        :type text: str

        :returns: 
        :rtype: None
        """
        ...



class canvas(obj):
    
    def __init__(self, *, parent: "obj"):
        """
        Create a canvas object pointer to the created canvas 
        """
        ...

    def set_buffer(self, buf: Any, w: int, h: int, cf: color_format_t) -> None:
        """
        Set a buffer for the canvas. 
        
        Use :ref:`lv_canvas_set_draw_buf()` instead if you need to set a buffer with alignment requirement.  
        
        :param buf: buffer where content of canvas will be. The required size is (lv_image_color_format_get_px_size(cf) * w) / 8 * h) It can be allocated with :ref:`lv_malloc()` or it can be statically allocated array (e.g. static :ref:`lv_color_t` buf[100*50]) or it can be an address in RAM or external SRAM 
        :type buf: Any
        :param w: width of canvas 
        :type w: int
        :param h: height of canvas 
        :type h: int
        :param cf: color format. LV_COLOR_FORMAT... 
        :type cf: color_format_t

        :returns: 
        :rtype: None
        """
        ...

    def set_draw_buf(self, draw_buf: "draw_buf_t") -> None:
        """
        Set a draw buffer for the canvas. A draw buffer either can be allocated by :ref:`lv_draw_buf_create()` or defined statically by LV_DRAW_BUF_DEFINE_STATIC . When buffer start address and stride has alignment requirement, it's recommended to use lv_draw_buf_create . 
        
        :param draw_buf: pointer to a draw buffer 
        :type draw_buf: "draw_buf_t"

        :returns: 
        :rtype: None
        """
        ...

    def set_px(self, x: int, y: int, color: "color_t", opa: opa_t) -> None:
        """
        Set a pixel's color and opacity The following color formats are supported LV_COLOR_FORMAT_I1/2/4/8, LV_COLOR_FORMAT_A8, LV_COLOR_FORMAT_RGB565, LV_COLOR_FORMAT_RGB888, LV_COLOR_FORMAT_XRGB8888, LV_COLOR_FORMAT_ARGB8888 
        
        :param x: X coordinate of the pixel 
        :type x: int
        :param y: Y coordinate of the pixel 
        :type y: int
        :param color: the color 
        :type color: "color_t"
        :param opa: the opacity 
        :type opa: opa_t

        :returns: 
        :rtype: None
        """
        ...

    def set_palette(self, index: int, color: "color32_t") -> None:
        """
        Set the palette color of a canvas for index format. Valid only for LV_COLOR_FORMAT_I1/2/4/8 
        
        :param index: the palette color to set: for LV_COLOR_FORMAT_I1 : 0..1 for LV_COLOR_FORMAT_I2 : 0..3 for LV_COLOR_FORMAT_I4 : 0..15 for LV_COLOR_FORMAT_I8 : 0..255 
        :type index: int
        :param color: the color to set 
        :type color: "color32_t"

        :returns: 
        :rtype: None
        """
        ...

    def get_draw_buf(self) -> "draw_buf_t":
        """

        :returns: 
        :rtype: "draw_buf_t"
        """
        ...

    def get_px(self, x: int, y: int) -> "color32_t":
        """
        Get a pixel's color and opacity ARGB8888 color of the pixel 
        
        :param x: X coordinate of the pixel 
        :type x: int
        :param y: Y coordinate of the pixel 
        :type y: int

        :returns: ARGB8888 color of the pixel 
        :rtype: "color32_t"
        """
        ...

    def get_image(self) -> "image":
        """
        Get the image of the canvas as a pointer to an :ref:`lv_image_dsc_t` variable. pointer to the image descriptor. 
        

        :returns: pointer to the image descriptor. 
        :rtype: "image"
        """
        ...

    def get_buf(self) -> Any:
        """
        Return the pointer for the buffer. It's recommended to use this function instead of the buffer form the return value of :ref:`lv_canvas_get_image()` as is can be aligned pointer to the buffer 
        

        :returns: pointer to the buffer 
        :rtype: Any
        """
        ...

    def copy_buf(self, canvas_area: "area_t", dest_buf: "draw_buf_t", dest_area: "area_t") -> None:
        """
        Copy a buffer to the canvas 
        
        :param canvas_area: the area of the canvas to copy 
        :type canvas_area: "area_t"
        :param dest_buf: pointer to a buffer to store the copied data 
        :type dest_buf: "draw_buf_t"
        :param dest_area: the area of the destination buffer to copy to. If omitted NULL, copy to the whole dest_buf 
        :type dest_area: "area_t"

        :returns: 
        :rtype: None
        """
        ...

    def fill_bg(self, color: "color_t", opa: opa_t) -> None:
        """
        Fill the canvas with color 
        
        :param color: the background color 
        :type color: "color_t"
        :param opa: the desired opacity 
        :type opa: opa_t

        :returns: 
        :rtype: None
        """
        ...

    def init_layer(self, layer: "layer_t") -> None:
        """
        Initialize a layer to use LVGL's generic draw functions (lv_draw_rect/label/...) on the canvas. Needs to be usd in pair with lv_canvas_finish_layer . 
        
        :param layer: pointer to a layer variable to initialize 
        :type layer: "layer_t"

        :returns: 
        :rtype: None
        """
        ...

    def finish_layer(self, layer: "layer_t") -> None:
        """
        Wait until all the drawings are finished on layer. Needs to be usd in pair with lv_canvas_init_layer . 
        
        :param layer: pointer to a layer to finalize 
        :type layer: "layer_t"

        :returns: 
        :rtype: None
        """
        ...

    def buf_size(self, h: int, bpp: int, stride: int) -> int:
        """
        Just a wrapper to LV_CANVAS_BUF_SIZE for bindings. 
        
        :param h: 
        :type h: int
        :param bpp: 
        :type bpp: int
        :param stride: 
        :type stride: int

        :returns: 
        :rtype: int
        """
        ...



class chart(obj):

    class TYPE(object):

        NONE: ClassVar[int] = ...
        LINE: ClassVar[int] = ...
        BAR: ClassVar[int] = ...
        SCATTER: ClassVar[int] = ...
        
        def __init__(self, *, parent: "obj"):
            ...

    class UPDATE_MODE(object):

        SHIFT: ClassVar[int] = ...
        CIRCULAR: ClassVar[int] = ...
        
        def __init__(self, *, parent: "obj"):
            ...

    class AXIS(object):

        PRIMARY_Y: ClassVar[int] = ...
        SECONDARY_Y: ClassVar[int] = ...
        PRIMARY_X: ClassVar[int] = ...
        SECONDARY_X: ClassVar[int] = ...
        LAST: ClassVar[int] = ...
        
        def __init__(self, *, parent: "obj"):
            ...

    
    def __init__(self, *, parent: "obj"):
        """
        Create a chart object pointer to the created chart 
        """
        ...

    def set_type(self, type: "chart") -> None:
        """
        Set a new type for a chart 
        
        :param type: new type of the chart (from 'lv_chart_type_t' enum) 
        :type type: "chart"

        :returns: 
        :rtype: None
        """
        ...

    def set_point_count(self, delay_ms: int) -> None:
        """
        Set the number of points on a data line on a chart 
        
        :param delay_ms: new number of points on the data lines 
        :type delay_ms: int

        :returns: 
        :rtype: None
        """
        ...

    def set_range(self, axis: "chart", min: int, max: int) -> None:
        """
        Set the minimal and maximal y values on an axis 
        
        :param axis: LV_CHART_AXIS_PRIMARY_Y or LV_CHART_AXIS_SECONDARY_Y 
        :type axis: "chart"
        :param min: minimum value of the y axis 
        :type min: int
        :param max: maximum value of the y axis 
        :type max: int

        :returns: 
        :rtype: None
        """
        ...

    def set_update_mode(self, update_mode: "chart") -> None:
        """
        Set update mode of the chart object. Affects 
        
        :param update_mode: the update mode 
        :type update_mode: "chart"

        :returns: 
        :rtype: None
        """
        ...

    def set_div_line_count(self, hdiv: int, vdiv: int) -> None:
        """
        Set the number of horizontal and vertical division lines 
        
        :param hdiv: number of horizontal division lines 
        :type hdiv: int
        :param vdiv: number of vertical division lines 
        :type vdiv: int

        :returns: 
        :rtype: None
        """
        ...

    def get_type(self) -> "chart":
        """
        Get the type of a chart type of the chart (from ' :ref:`lv_chart_t` ' enum) 
        

        :returns: type of the chart (from ' :ref:`lv_chart_t` ' enum) 
        :rtype: "chart"
        """
        ...

    def get_point_count(self) -> int:
        """
        Get the data point number per data line on chart point number on each data line 
        

        :returns: point number on each data line 
        :rtype: int
        """
        ...

    def get_x_start_point(self, ser: "chart") -> int:
        """
        Get the current index of the x-axis start point in the data array the index of the current x start point in the data array 
        
        :param ser: pointer to a data series on 'chart' 
        :type ser: "chart"

        :returns: the index of the current x start point in the data array 
        :rtype: int
        """
        ...

    def get_point_pos_by_id(self, ser: "chart", id: int, p_out: "point_t") -> None:
        """
        Get the position of a point to the chart. 
        
        :param ser: pointer to series 
        :type ser: "chart"
        :param id: the index. 
        :type id: int
        :param p_out: store the result position here 
        :type p_out: "point_t"

        :returns: 
        :rtype: None
        """
        ...

    def refresh(self) -> None:
        """
        Refresh a chart if its data line has changed 
        

        :returns: 
        :rtype: None
        """
        ...

    def add_series(self, color: "color_t", axis: "chart") -> "chart":
        """
        Allocate and add a data series to the chart pointer to the allocated data series or NULL on failure 
        
        :param color: color of the data series 
        :type color: "color_t"
        :param axis: the y axis to which the series should be attached (::LV_CHART_AXIS_PRIMARY_Y or ::LV_CHART_AXIS_SECONDARY_Y) 
        :type axis: "chart"

        :returns: pointer to the allocated data series or NULL on failure 
        :rtype: "chart"
        """
        ...

    def remove_series(self, series: "chart") -> None:
        """
        Deallocate and remove a data series from a chart 
        
        :param series: pointer to a data series on 'chart' 
        :type series: "chart"

        :returns: 
        :rtype: None
        """
        ...

    def hide_series(self, series: "chart", hide: bool) -> None:
        """
        Hide/Unhide a single series of a chart. 
        
        :param series: pointer to a series object 
        :type series: "chart"
        :param hide: true: hide the series 
        :type hide: bool

        :returns: 
        :rtype: None
        """
        ...

    def set_series_color(self, series: "chart", color: "color_t") -> None:
        """
        Change the color of a series 
        
        :param series: pointer to a series object 
        :type series: "chart"
        :param color: the new color of the series 
        :type color: "color_t"

        :returns: 
        :rtype: None
        """
        ...

    def get_series_color(self, series: "chart") -> "color_t":
        """
        Get the color of a series the color of the series 
        
        :param series: pointer to a series object 
        :type series: "chart"

        :returns: the color of the series 
        :rtype: "color_t"
        """
        ...

    def set_x_start_point(self, ser: "chart", id: int) -> None:
        """
        Set the index of the x-axis start point in the data array. This point will be considers the first (left) point and the other points will be drawn after it. 
        
        :param ser: pointer to a data series on 'chart' 
        :type ser: "chart"
        :param id: the index of the x point in the data array 
        :type id: int

        :returns: 
        :rtype: None
        """
        ...

    def get_series_next(self, ser: "chart") -> "chart":
        """
        Get the next series. the next series or NULL if there is no more. 
        
        :param ser: the previous series or NULL to get the first 
        :type ser: "chart"

        :returns: the next series or NULL if there is no more. 
        :rtype: "chart"
        """
        ...

    def add_cursor(self, color: "color_t", dir: dir_t) -> "chart":
        """
        Add a cursor with a given color pointer to the created cursor 
        
        :param color: color of the cursor 
        :type color: "color_t"
        :param dir: direction of the cursor. LV_DIR_RIGHT/LEFT/TOP/DOWN/HOR/VER/ALL . OR-ed values are possible 
        :type dir: dir_t

        :returns: pointer to the created cursor 
        :rtype: "chart"
        """
        ...

    def set_cursor_pos(self, cursor: "chart", pos: "point_t") -> None:
        """
        Set the coordinate of the cursor with respect to the paddings 
        
        :param cursor: pointer to the cursor 
        :type cursor: "chart"
        :param pos: the new coordinate of cursor relative to the chart 
        :type pos: "point_t"

        :returns: 
        :rtype: None
        """
        ...

    def set_cursor_point(self, cursor: "chart", ser: "chart", point_id: int) -> None:
        """
        Stick the cursor to a point 
        
        :param cursor: pointer to the cursor 
        :type cursor: "chart"
        :param ser: pointer to a series 
        :type ser: "chart"
        :param point_id: the point's index or LV_CHART_POINT_NONE to not assign to any points. 
        :type point_id: int

        :returns: 
        :rtype: None
        """
        ...

    def get_cursor_point(self, cursor: "chart") -> "point_t":
        """
        Get the coordinate of the cursor with respect to the paddings coordinate of the cursor as :ref:`lv_point_t` 
        
        :param cursor: pointer to cursor 
        :type cursor: "chart"

        :returns: coordinate of the cursor as :ref:`lv_point_t` 
        :rtype: "point_t"
        """
        ...

    def set_all_value(self, ser: "chart", value: int) -> None:
        """
        Initialize all data points of a series with a value 
        
        :param ser: pointer to a data series on 'chart' 
        :type ser: "chart"
        :param value: the new value for all points. LV_CHART_POINT_NONE can be used to hide the points. 
        :type value: int

        :returns: 
        :rtype: None
        """
        ...

    def set_next_value(self, ser: "chart", value: int) -> None:
        """
        Set the next point's Y value according to the update mode policy. 
        
        :param ser: pointer to a data series on 'chart' 
        :type ser: "chart"
        :param value: the new value of the next data 
        :type value: int

        :returns: 
        :rtype: None
        """
        ...

    def set_next_value2(self, ser: "chart", x_value: int, y_value: int) -> None:
        """
        Set the next point's X and Y value according to the update mode policy. 
        
        :param ser: pointer to a data series on 'chart' 
        :type ser: "chart"
        :param x_value: the new X value of the next data 
        :type x_value: int
        :param y_value: the new Y value of the next data 
        :type y_value: int

        :returns: 
        :rtype: None
        """
        ...

    def set_value_by_id(self, ser: "chart", id: int, value: int) -> None:
        """
        Set an individual point's y value of a chart's series directly based on its index 
        
        :param ser: pointer to a data series on 'chart' 
        :type ser: "chart"
        :param id: the index of the x point in the array 
        :type id: int
        :param value: value to assign to array point 
        :type value: int

        :returns: 
        :rtype: None
        """
        ...

    def set_value_by_id2(self, ser: "chart", id: int, x_value: int, y_value: int) -> None:
        """
        Set an individual point's x and y value of a chart's series directly based on its index Can be used only with LV_CHART_TYPE_SCATTER . 
        
        :param ser: pointer to a data series on 'chart' 
        :type ser: "chart"
        :param id: the index of the x point in the array 
        :type id: int
        :param x_value: the new X value of the next data 
        :type x_value: int
        :param y_value: the new Y value of the next data 
        :type y_value: int

        :returns: 
        :rtype: None
        """
        ...

    def set_series_ext_y_array(self, ser: "chart", array: List[int]) -> None:
        """
        Set an external array for the y data points to use for the chart NOTE: It is the users responsibility to make sure the point_cnt matches the external array size. 
        
        :param ser: pointer to a data series on 'chart' 
        :type ser: "chart"
        :param array: external array of points for chart 
        :type array: List[int]

        :returns: 
        :rtype: None
        """
        ...

    def set_series_ext_x_array(self, ser: "chart", array: List[int]) -> None:
        """
        Set an external array for the x data points to use for the chart NOTE: It is the users responsibility to make sure the point_cnt matches the external array size. 
        
        :param ser: pointer to a data series on 'chart' 
        :type ser: "chart"
        :param array: external array of points for chart 
        :type array: List[int]

        :returns: 
        :rtype: None
        """
        ...

    def get_y_array(self, ser: "chart") -> List[int]:
        """
        Get the array of y values of a series the array of values with 'point_count' elements 
        
        :param ser: pointer to a data series on 'chart' 
        :type ser: "chart"

        :returns: the array of values with 'point_count' elements 
        :rtype: List[int]
        """
        ...

    def get_x_array(self, ser: "chart") -> List[int]:
        """
        Get the array of x values of a series the array of values with 'point_count' elements 
        
        :param ser: pointer to a data series on 'chart' 
        :type ser: "chart"

        :returns: the array of values with 'point_count' elements 
        :rtype: List[int]
        """
        ...

    def get_pressed_point(self) -> int:
        """
        Get the index of the currently pressed point. It's the same for every series. the index of the point [0 .. point count] or LV_CHART_POINT_ID_NONE if no point is being pressed 
        

        :returns: the index of the point [0 .. point count] or LV_CHART_POINT_ID_NONE if no point is being pressed 
        :rtype: int
        """
        ...

    def get_first_point_center_offset(self) -> int:
        """
        Get the overall offset from the chart's side to the center of the first point. In case of a bar chart it will be the center of the first column group the offset of the center 
        

        :returns: the offset of the center 
        :rtype: int
        """
        ...



class checkbox(obj):
    
    def __init__(self, *, parent: "obj"):
        """
        Create a check box object pointer to the created check box 
        """
        ...

    def set_text(self, text: str) -> None:
        """
        Set the text of a check box. txt will be copied and may be deallocated after this function returns. 
        
        :param text: the text of the check box. NULL to refresh with the current text. 
        :type text: str

        :returns: 
        :rtype: None
        """
        ...

    def set_text_static(self, text: str) -> None:
        """
        Set the text of a check box. txt must not be deallocated during the life of this checkbox. 
        
        :param text: the text of the check box. 
        :type text: str

        :returns: 
        :rtype: None
        """
        ...

    def get_text(self) -> str:
        """
        Get the text of a check box pointer to the text of the check box 
        

        :returns: pointer to the text of the check box 
        :rtype: str
        """
        ...



class dropdown(obj):
    
    def __init__(self, *, parent: "obj"):
        """
        Create a drop-down list object pointer to the created drop-down list 
        """
        ...

    def set_text(self, text: str) -> None:
        """
        Set text of the drop-down list's button. If set to NULL the selected option's text will be displayed on the button. If set to a specific text then that text will be shown regardless of the selected option. 
        
        :param text: the text as a string (Only its pointer is saved) 
        :type text: str

        :returns: 
        :rtype: None
        """
        ...

    def set_options(self, text: str) -> None:
        """
        Set the options in a drop-down list from a string. The options will be copied and saved in the object so the options can be destroyed after calling this function 
        
        :param text: a string with ' ' separated options. E.g. "One\nTwo\nThree" 
        :type text: str

        :returns: 
        :rtype: None
        """
        ...

    def set_options_static(self, text: str) -> None:
        """
        Set the options in a drop-down list from a static string (global, static or dynamically allocated). Only the pointer of the option string will be saved. 
        
        :param text: a static string with ' ' separated options. E.g. "One\nTwo\nThree" 
        :type text: str

        :returns: 
        :rtype: None
        """
        ...

    def add_option(self, option: str, pos: int) -> None:
        """
        Add an options to a drop-down list from a string. Only works for non-static options. 
        
        :param option: a string without ' '. E.g. "Four" 
        :type option: str
        :param pos: the insert position, indexed from 0, LV_DROPDOWN_POS_LAST = end of string 
        :type pos: int

        :returns: 
        :rtype: None
        """
        ...

    def clear_options(self) -> None:
        """
        Clear all options in a drop-down list. Works with both static and dynamic options. 
        

        :returns: 
        :rtype: None
        """
        ...

    def set_selected(self, delay_ms: int) -> None:
        """
        Set the selected option 
        
        :param delay_ms: id of the selected option (0 ... number of option - 1); 
        :type delay_ms: int

        :returns: 
        :rtype: None
        """
        ...

    def set_dir(self, dir: dir_t) -> None:
        """
        Set the direction of the a drop-down list 
        
        :param dir: LV_DIR_LEFT/RIGHT/TOP/BOTTOM 
        :type dir: dir_t

        :returns: 
        :rtype: None
        """
        ...

    def set_symbol(self, src: Any) -> None:
        """
        Set an arrow or other symbol to display when on drop-down list's button. Typically a down caret or arrow. angle and zoom transformation can be applied if the symbol is an image. E.g. when drop down is checked (opened) rotate the symbol by 180 degree 
        
        :param src: a text like LV_SYMBOL_DOWN , an image (pointer or path) or NULL to not draw symbol icon 
        :type src: Any

        :returns: 
        :rtype: None
        """
        ...

    def set_selected_highlight(self, antialias: bool) -> None:
        """
        Set whether the selected option in the list should be highlighted or not 
        
        :param antialias: true: highlight enabled; false: disabled 
        :type antialias: bool

        :returns: 
        :rtype: None
        """
        ...

    def get_list(self) -> "obj":
        """
        Get the list of a drop-down to allow styling or other modifications pointer to the list of the drop-down 
        

        :returns: pointer to the list of the drop-down 
        :rtype: "obj"
        """
        ...

    def get_text(self) -> str:
        """
        Get text of the drop-down list's button. the text as string, NULL if no text 
        

        :returns: the text as string, NULL if no text 
        :rtype: str
        """
        ...

    def get_options(self) -> str:
        """
        Get the options of a drop-down list the options separated by ' '-s (E.g. "Option1\nOption2\nOption3") 
        

        :returns: the options separated by ' '-s (E.g. "Option1\nOption2\nOption3") 
        :rtype: str
        """
        ...

    def get_selected(self) -> int:
        """
        Get the index of the selected option index of the selected option (0 ... number of option - 1); 
        

        :returns: index of the selected option (0 ... number of option - 1); 
        :rtype: int
        """
        ...

    def get_option_count(self) -> int:
        """
        Get the total number of options the total number of options in the list 
        

        :returns: the total number of options in the list 
        :rtype: int
        """
        ...

    def get_selected_str(self, buf: str, buf_size: int) -> None:
        """
        Get the current selected option as a string 
        
        :param buf: pointer to an array to store the string 
        :type buf: str
        :param buf_size: size of buf in bytes. 0: to ignore it. 
        :type buf_size: int

        :returns: 
        :rtype: None
        """
        ...

    def get_option_index(self, option: str) -> int:
        """
        Get the index of an option. index of option in the list of all options. -1 if not found. 
        
        :param option: an option as string 
        :type option: str

        :returns: index of option in the list of all options. -1 if not found. 
        :rtype: int
        """
        ...

    def get_symbol(self) -> str:
        """
        Get the symbol on the drop-down list. Typically a down caret or arrow. the symbol or NULL if not enabled 
        

        :returns: the symbol or NULL if not enabled 
        :rtype: str
        """
        ...

    def get_selected_highlight(self) -> bool:
        """
        Get whether the selected option in the list should be highlighted or not true: highlight enabled; false: disabled 
        

        :returns: true: highlight enabled; false: disabled 
        :rtype: bool
        """
        ...

    def get_dir(self) -> "dir_t":
        """
        Get the direction of the drop-down list LV_DIR_LEF/RIGHT/TOP/BOTTOM 
        

        :returns: LV_DIR_LEF/RIGHT/TOP/BOTTOM 
        :rtype: "dir_t"
        """
        ...

    def open(self) -> None:
        """
        Open the drop.down list 
        

        :returns: 
        :rtype: None
        """
        ...

    def close(self) -> None:
        """
        Close (Collapse) the drop-down list 
        

        :returns: 
        :rtype: None
        """
        ...

    def is_open(self) -> bool:
        """
        Tells whether the list is opened or not true if the list os opened 
        

        :returns: true if the list os opened 
        :rtype: bool
        """
        ...

    def bind_value(self, subject: "subject_t") -> "observer_t":
        """
        Bind an integer subject to a dropdown's value pointer to the created observer 
        
        :param subject: pointer to a subject 
        :type subject: "subject_t"

        :returns: pointer to the created observer 
        :rtype: "observer_t"
        """
        ...



class imagebutton(obj):

    class STATE(object):

        RELEASED: ClassVar[int] = ...
        PRESSED: ClassVar[int] = ...
        DISABLED: ClassVar[int] = ...
        CHECKED_RELEASED: ClassVar[int] = ...
        CHECKED_PRESSED: ClassVar[int] = ...
        CHECKED_DISABLED: ClassVar[int] = ...
        NUM: ClassVar[int] = ...
        
        def __init__(self, *, parent: "obj"):
            ...

    
    def __init__(self, *, parent: "obj"):
        """
        Create an image button object pointer to the created image button 
        """
        ...

    def set_src(self, state: "imagebutton", src_left: Any, src_mid: Any, src_right: Any) -> None:
        """
        Set images for a state of the image button 
        
        :param state: for which state set the new image 
        :type state: "imagebutton"
        :param src_left: pointer to an image source for the left side of the button (a C array or path to a file) 
        :type src_left: Any
        :param src_mid: pointer to an image source for the middle of the button (ideally 1px wide) (a C array or path to a file) 
        :type src_mid: Any
        :param src_right: pointer to an image source for the right side of the button (a C array or path to a file) 
        :type src_right: Any

        :returns: 
        :rtype: None
        """
        ...

    def get_src_left(self, state: "imagebutton") -> Any:
        """
        Get the left image in a given state pointer to the left image source (a C array or path to a file) 
        
        :param state: the state where to get the image (from lv_button_state_t ) ` 
        :type state: "imagebutton"

        :returns: pointer to the left image source (a C array or path to a file) 
        :rtype: Any
        """
        ...

    def get_src_middle(self, state: "imagebutton") -> Any:
        """
        Get the middle image in a given state pointer to the middle image source (a C array or path to a file) 
        
        :param state: the state where to get the image (from lv_button_state_t ) ` 
        :type state: "imagebutton"

        :returns: pointer to the middle image source (a C array or path to a file) 
        :rtype: Any
        """
        ...

    def get_src_right(self, state: "imagebutton") -> Any:
        """
        Get the right image in a given state pointer to the left image source (a C array or path to a file) 
        
        :param state: the state where to get the image (from lv_button_state_t ) ` 
        :type state: "imagebutton"

        :returns: pointer to the left image source (a C array or path to a file) 
        :rtype: Any
        """
        ...



class keyboard(obj):

    class MODE(object):

        TEXT_LOWER: ClassVar[int] = ...
        TEXT_UPPER: ClassVar[int] = ...
        SPECIAL: ClassVar[int] = ...
        NUMBER: ClassVar[int] = ...
        USER_1: ClassVar[int] = ...
        USER_2: ClassVar[int] = ...
        USER_3: ClassVar[int] = ...
        USER_4: ClassVar[int] = ...
        
        def __init__(self, *, parent: "obj"):
            ...

    
    def __init__(self, *, parent: "obj"):
        """
        Create a Keyboard object pointer to the created keyboard 
        """
        ...

    def set_textarea(self, parent: "obj") -> None:
        """
        Assign a Text Area to the Keyboard. The pressed characters will be put there. 
        
        :param parent: pointer to a Text Area object to write there 
        :type parent: "obj"

        :returns: 
        :rtype: None
        """
        ...

    def set_mode(self, mode: "keyboard") -> None:
        """
        Set a new a mode (text or number map) 
        
        :param mode: the mode from 'lv_keyboard_mode_t' 
        :type mode: "keyboard"

        :returns: 
        :rtype: None
        """
        ...

    def set_popovers(self, antialias: bool) -> None:
        """
        Show the button title in a popover when pressed. 
        
        :param antialias: whether "popovers" mode is enabled 
        :type antialias: bool

        :returns: 
        :rtype: None
        """
        ...

    def set_map(self, mode: "keyboard", map: List[str], ctrl_map: List["buttonmatrix"]) -> None:
        """
        Set a new map for the keyboard 
        
        :param mode: keyboard map to alter 'lv_keyboard_mode_t' 
        :type mode: "keyboard"
        :param map: pointer to a string array to describe the map. See ' :ref:`lv_buttonmatrix_set_map()` ' for more info. 
        :type map: List[str]
        :param ctrl_map: See ' :ref:`lv_buttonmatrix_set_ctrl_map()` ' for more info. 
        :type ctrl_map: List["buttonmatrix"]

        :returns: 
        :rtype: None
        """
        ...

    def get_textarea(self) -> "obj":
        """
        Assign a Text Area to the Keyboard. The pressed characters will be put there. pointer to the assigned Text Area object 
        

        :returns: pointer to the assigned Text Area object 
        :rtype: "obj"
        """
        ...

    def get_mode(self) -> "keyboard":
        """
        Set a new a mode (text or number map) the current mode from 'lv_keyboard_mode_t' 
        

        :returns: the current mode from 'lv_keyboard_mode_t' 
        :rtype: "keyboard"
        """
        ...

    def get_popovers(self) -> bool:
        """
        Tell whether "popovers" mode is enabled or not. true: "popovers" mode is enabled; false: disabled 
        

        :returns: true: "popovers" mode is enabled; false: disabled 
        :rtype: bool
        """
        ...

    def get_selected_button(self) -> int:
        """
        Get the index of the lastly "activated" button by the user (pressed, released, focused etc) Useful in the event_cb to get the text of the button, check if hidden etc. index of the last released button (LV_BUTTONMATRIX_BUTTON_NONE: if unset) 
        

        :returns: index of the last released button (LV_BUTTONMATRIX_BUTTON_NONE: if unset) 
        :rtype: int
        """
        ...

    def get_button_text(self, btn_id: int) -> str:
        """
        Get the button's text text of btn_index` button 
        
        :param btn_id: the index a button not counting new line characters. 
        :type btn_id: int

        :returns: text of btn_index` button 
        :rtype: str
        """
        ...

    def def_event_cb(self) -> None:
        """
        Default keyboard event to add characters to the Text area and change the map. If a custom event_cb is added to the keyboard this function can be called from it to handle the button clicks 
        

        :returns: 
        :rtype: None
        """
        ...



class led(obj):
    
    def __init__(self, *, parent: "obj"):
        """
        Create a led object pointer to the created led 
        """
        ...

    def set_color(self, color: "color_t") -> None:
        """
        Set the color of the LED 
        
        :param color: the color of the LED 
        :type color: "color_t"

        :returns: 
        :rtype: None
        """
        ...

    def set_brightness(self, grow: int) -> None:
        """
        Set the brightness of a LED object 
        
        :param grow: LV_LED_BRIGHT_MIN (max. dark) ... LV_LED_BRIGHT_MAX (max. light) 
        :type grow: int

        :returns: 
        :rtype: None
        """
        ...

    def on(self) -> None:
        """
        Light on a LED 
        

        :returns: 
        :rtype: None
        """
        ...

    def off(self) -> None:
        """
        Light off a LED 
        

        :returns: 
        :rtype: None
        """
        ...

    def toggle(self) -> None:
        """
        Toggle the state of a LED 
        

        :returns: 
        :rtype: None
        """
        ...

    def get_brightness(self) -> int:
        """
        Get the brightness of a LED object bright 0 (max. dark) ... 255 (max. light) 
        

        :returns: bright 0 (max. dark) ... 255 (max. light) 
        :rtype: int
        """
        ...



class line(obj):
    
    def __init__(self, *, parent: "obj"):
        """
        Create a line object pointer to the created line 
        """
        ...

    def set_points(self, points: List["point_precise_t"], point_num: int) -> None:
        """
        Set an array of points. The line object will connect these points. 
        
        :param points: an array of points. Only the address is saved, so the array needs to be alive while the line exists 
        :type points: List["point_precise_t"]
        :param point_num: number of points in 'point_a' 
        :type point_num: int

        :returns: 
        :rtype: None
        """
        ...

    def set_points_mutable(self, points: List["point_precise_t"], point_num: int) -> None:
        """
        Set a non-const array of points. Identical to lv_line_set_points except the array may be retrieved by lv_line_get_points_mutable . 
        
        :param points: a non-const array of points. Only the address is saved, so the array needs to be alive while the line exists. 
        :type points: List["point_precise_t"]
        :param point_num: number of points in 'point_a' 
        :type point_num: int

        :returns: 
        :rtype: None
        """
        ...

    def set_y_invert(self, antialias: bool) -> None:
        """
        Enable (or disable) the y coordinate inversion. If enabled then y will be subtracted from the height of the object, therefore the y = 0 coordinate will be on the bottom. 
        
        :param antialias: true: enable the y inversion, false:disable the y inversion 
        :type antialias: bool

        :returns: 
        :rtype: None
        """
        ...

    def get_points(self) -> "point_precise_t":
        """
        Get the pointer to the array of points. const pointer to the array of points 
        

        :returns: const pointer to the array of points 
        :rtype: "point_precise_t"
        """
        ...

    def get_point_count(self) -> int:
        """
        Get the number of points in the array of points. number of points in array of points 
        

        :returns: number of points in array of points 
        :rtype: int
        """
        ...

    def is_point_array_mutable(self) -> bool:
        """
        Check the mutability of the stored point array pointer. true: the point array pointer is mutable, false: constant 
        

        :returns: true: the point array pointer is mutable, false: constant 
        :rtype: bool
        """
        ...

    def get_points_mutable(self) -> "point_precise_t":
        """
        Get a pointer to the mutable array of points or NULL if it is not mutable pointer to the array of points. NULL if not mutable. 
        

        :returns: pointer to the array of points. NULL if not mutable. 
        :rtype: "point_precise_t"
        """
        ...

    def get_y_invert(self) -> bool:
        """
        Get the y inversion attribute true: y inversion is enabled, false: disabled 
        

        :returns: true: y inversion is enabled, false: disabled 
        :rtype: bool
        """
        ...



class list(obj):
    
    def __init__(self, *, parent: "obj"):
        """
        Create a list object pointer to the created list 
        """
        ...

    def add_text(self, txt: str) -> "obj":
        """
        Add text to a list pointer to the created label 
        
        :param txt: text of the new label 
        :type txt: str

        :returns: pointer to the created label 
        :rtype: "obj"
        """
        ...

    def add_button(self, icon: Any, txt: str) -> "obj":
        """
        Add button to a list pointer to the created button 
        
        :param icon: icon for the button, when NULL it will have no icon 
        :type icon: Any
        :param txt: text of the new button, when NULL no text will be added 
        :type txt: str

        :returns: pointer to the created button 
        :rtype: "obj"
        """
        ...

    def get_button_text(self, btn: "obj") -> str:
        """
        Get text of a given list button text of btn, if btn doesn't have text "" will be returned 
        
        :param btn: pointer to the button 
        :type btn: "obj"

        :returns: text of btn, if btn doesn't have text "" will be returned 
        :rtype: str
        """
        ...

    def set_button_text(self, btn: "obj", txt: str) -> None:
        """
        Set text of a given list button 
        
        :param btn: pointer to the button 
        :type btn: "obj"
        :param txt: pointer to the text 
        :type txt: str

        :returns: 
        :rtype: None
        """
        ...



class menu(obj):

    class HEADER(object):

        TOP_FIXED: ClassVar[int] = ...
        TOP_UNFIXED: ClassVar[int] = ...
        BOTTOM_FIXED: ClassVar[int] = ...
        
        def __init__(self, *, parent: "obj"):
            ...

    class ROOT_BACK_BUTTON(object):

        DISABLED: ClassVar[int] = ...
        ENABLED: ClassVar[int] = ...
        
        def __init__(self, *, parent: "obj"):
            ...

    
    def __init__(self, *, parent: "obj"):
        """
        Create a menu object pointer to the created menu 
        """
        ...

    def set_page(self, parent: "obj") -> None:
        """
        Set menu page to display in main 
        
        :param parent: pointer to the menu page to set (NULL to clear main and clear menu history) 
        :type parent: "obj"

        :returns: 
        :rtype: None
        """
        ...

    def set_page_title(self, title: str) -> None:
        """
        Set menu page title 
        
        :param title: pointer to text for title in header (NULL to not display title) 
        :type title: str

        :returns: 
        :rtype: None
        """
        ...

    def set_page_title_static(self, title: str) -> None:
        """
        Set menu page title with a static text. It will not be saved by the label so the 'text' variable has to be 'alive' while the page exists. 
        
        :param title: pointer to text for title in header (NULL to not display title) 
        :type title: str

        :returns: 
        :rtype: None
        """
        ...

    def set_sidebar_page(self, parent: "obj") -> None:
        """
        Set menu page to display in sidebar 
        
        :param parent: pointer to the menu page to set (NULL to clear sidebar) 
        :type parent: "obj"

        :returns: 
        :rtype: None
        """
        ...

    def set_mode_header(self, mode: "menu") -> None:
        """
        Set the how the header should behave and its position 
        
        :param mode: LV_MENU_HEADER_TOP_FIXED/TOP_UNFIXED/BOTTOM_FIXED 
        :type mode: "menu"

        :returns: 
        :rtype: None
        """
        ...

    def set_mode_root_back_button(self, mode: "menu") -> None:
        """
        Set whether back button should appear at root 
        
        :param mode: LV_MENU_ROOT_BACK_BUTTON_DISABLED/ENABLED 
        :type mode: "menu"

        :returns: 
        :rtype: None
        """
        ...

    def set_load_page_event(self, obj: "obj", page: "obj") -> None:
        """
        Add menu to the menu item 
        
        :param obj: pointer to the obj 
        :type obj: "obj"
        :param page: pointer to the page to load when obj is clicked 
        :type page: "obj"

        :returns: 
        :rtype: None
        """
        ...

    def get_cur_main_page(self) -> "obj":
        """
        Get a pointer to menu page that is currently displayed in main pointer to current page 
        

        :returns: pointer to current page 
        :rtype: "obj"
        """
        ...

    def get_cur_sidebar_page(self) -> "obj":
        """
        Get a pointer to menu page that is currently displayed in sidebar pointer to current page 
        

        :returns: pointer to current page 
        :rtype: "obj"
        """
        ...

    def get_main_header(self) -> "obj":
        """
        Get a pointer to main header obj pointer to main header obj 
        

        :returns: pointer to main header obj 
        :rtype: "obj"
        """
        ...

    def get_main_header_back_button(self) -> "obj":
        """
        Get a pointer to main header back btn obj pointer to main header back btn obj 
        

        :returns: pointer to main header back btn obj 
        :rtype: "obj"
        """
        ...

    def get_sidebar_header(self) -> "obj":
        """
        Get a pointer to sidebar header obj pointer to sidebar header obj 
        

        :returns: pointer to sidebar header obj 
        :rtype: "obj"
        """
        ...

    def get_sidebar_header_back_button(self) -> "obj":
        """
        Get a pointer to sidebar header obj pointer to sidebar header back btn obj 
        

        :returns: pointer to sidebar header back btn obj 
        :rtype: "obj"
        """
        ...

    def back_button_is_root(self, obj: "obj") -> bool:
        """
        Check if an obj is a root back btn true if it is a root back btn 
        
        :param obj: pointer to the back button 
        :type obj: "obj"

        :returns: true if it is a root back btn 
        :rtype: bool
        """
        ...

    def clear_history(self) -> None:
        """
        Clear menu history 
        

        :returns: 
        :rtype: None
        """
        ...



class menu_page(obj):
    
    def __init__(self, *, parent: "obj"):
        """
        Create a menu page object pointer to the created menu page 
        """
        ...


class menu_cont(obj):
    
    def __init__(self, *, parent: "obj"):
        """
        Create a menu cont object pointer to the created menu cont 
        """
        ...


class menu_section(obj):
    
    def __init__(self, *, parent: "obj"):
        """
        Create a menu section object pointer to the created menu section 
        """
        ...


class menu_separator(obj):
    
    def __init__(self, *, parent: "obj"):
        """
        Create a menu separator object pointer to the created menu separator 
        """
        ...


class msgbox(obj):
    
    def __init__(self, *, parent: "obj"):
        """
        Create an empty message box the created message box 
        """
        ...

    def add_title(self, txt: str) -> "obj":
        """
        Add title to the message box. It also creates a header for the title. the created title label 
        
        :param txt: the text of the tile 
        :type txt: str

        :returns: the created title label 
        :rtype: "obj"
        """
        ...

    def add_header_button(self, icon: Any) -> "obj":
        """
        Add a button to the header of to the message box. It also creates a header. the created button 
        
        :param icon: the icon of the button 
        :type icon: Any

        :returns: the created button 
        :rtype: "obj"
        """
        ...

    def add_text(self, txt: str) -> "obj":
        """
        Add a text to the content area of message box. Multiple texts will be created below each other. the created button 
        
        :param txt: text to add 
        :type txt: str

        :returns: the created button 
        :rtype: "obj"
        """
        ...

    def add_footer_button(self, txt: str) -> "obj":
        """
        Add a button to the footer of to the message box. It also creates a footer. the created button 
        
        :param txt: the text of the button 
        :type txt: str

        :returns: the created button 
        :rtype: "obj"
        """
        ...

    def add_close_button(self) -> "obj":
        """
        Add a close button to the message box. It also creates a header. the created close button 
        

        :returns: the created close button 
        :rtype: "obj"
        """
        ...

    def get_header(self) -> "obj":
        """
        Get the header widget the header, or NULL if not exists 
        

        :returns: the header, or NULL if not exists 
        :rtype: "obj"
        """
        ...

    def get_footer(self) -> "obj":
        """
        Get the footer widget the footer, or NULL if not exists 
        

        :returns: the footer, or NULL if not exists 
        :rtype: "obj"
        """
        ...

    def get_content(self) -> "obj":
        """
        Get the content widget the content 
        

        :returns: the content 
        :rtype: "obj"
        """
        ...

    def get_title(self) -> "obj":
        """
        Get the title label the title, or NULL if it does not exist 
        

        :returns: the title, or NULL if it does not exist 
        :rtype: "obj"
        """
        ...

    def close(self) -> None:
        """
        Close a message box 
        

        :returns: 
        :rtype: None
        """
        ...

    def close_async(self) -> None:
        """
        Close a message box in the next call of the message box 
        

        :returns: 
        :rtype: None
        """
        ...



class roller(obj):

    class MODE(object):

        NORMAL: ClassVar[int] = ...
        INFINITE: ClassVar[int] = ...
        
        def __init__(self, *, parent: "obj"):
            ...

    
    def __init__(self, *, parent: "obj"):
        """
        Create a roller object pointer to the created roller 
        """
        ...

    def set_options(self, options: str, mode: "roller") -> None:
        """
        Set the options on a roller 
        
        :param options: a string with ' ' separated options. E.g. "One\nTwo\nThree" 
        :type options: str
        :param mode: LV_ROLLER_MODE_NORMAL or LV_ROLLER_MODE_INFINITE 
        :type mode: "roller"

        :returns: 
        :rtype: None
        """
        ...

    def set_selected(self, sel_opt: int, anim: "anim_enable_t") -> None:
        """
        Set the selected option 
        
        :param sel_opt: index of the selected option (0 ... number of option - 1); 
        :type sel_opt: int
        :param anim: LV_ANIM_ON: set with animation; LV_ANOM_OFF set immediately 
        :type anim: "anim_enable_t"

        :returns: 
        :rtype: None
        """
        ...

    def set_visible_row_count(self, delay_ms: int) -> None:
        """
        Set the height to show the given number of rows (options) 
        
        :param delay_ms: number of desired visible rows 
        :type delay_ms: int

        :returns: 
        :rtype: None
        """
        ...

    def get_selected(self) -> int:
        """
        Get the index of the selected option index of the selected option (0 ... number of option - 1); 
        

        :returns: index of the selected option (0 ... number of option - 1); 
        :rtype: int
        """
        ...

    def get_selected_str(self, buf: str, buf_size: int) -> None:
        """
        Get the current selected option as a string. 
        
        :param buf: pointer to an array to store the string 
        :type buf: str
        :param buf_size: size of buf in bytes. 0: to ignore it. 
        :type buf_size: int

        :returns: 
        :rtype: None
        """
        ...

    def get_options(self) -> str:
        """
        Get the options of a roller the options separated by ' '-s (E.g. "Option1\nOption2\nOption3") 
        

        :returns: the options separated by ' '-s (E.g. "Option1\nOption2\nOption3") 
        :rtype: str
        """
        ...

    def get_option_count(self) -> int:
        """
        Get the total number of options the total number of options 
        

        :returns: the total number of options 
        :rtype: int
        """
        ...

    def bind_value(self, subject: "subject_t") -> "observer_t":
        """
        Bind an integer subject to a roller's value pointer to the created observer 
        
        :param subject: pointer to a subject 
        :type subject: "subject_t"

        :returns: pointer to the created observer 
        :rtype: "observer_t"
        """
        ...



class scale(obj):

    class MODE(object):

        HORIZONTAL_TOP: ClassVar[int] = ...
        HORIZONTAL_BOTTOM: ClassVar[int] = ...
        VERTICAL_LEFT: ClassVar[int] = ...
        VERTICAL_RIGHT: ClassVar[int] = ...
        ROUND_INNER: ClassVar[int] = ...
        ROUND_OUTER: ClassVar[int] = ...
        LAST: ClassVar[int] = ...
        
        def __init__(self, *, parent: "obj"):
            ...

    
    def __init__(self, *, parent: "obj"):
        """
        Create an scale object pointer to the created scale 
        """
        ...

    def set_mode(self, mode: "scale") -> None:
        """
        Set scale mode. See lv_scale_mode_t 
        
        :param mode: the new scale mode 
        :type mode: "scale"

        :returns: 
        :rtype: None
        """
        ...

    def set_total_tick_count(self, delay_ms: int) -> None:
        """
        Set scale total tick count (including minor and major ticks) 
        
        :param delay_ms: New total tick count 
        :type delay_ms: int

        :returns: 
        :rtype: None
        """
        ...

    def set_major_tick_every(self, delay_ms: int) -> None:
        """
        Sets how often the major tick will be drawn 
        
        :param delay_ms: the new count for major tick drawing 
        :type delay_ms: int

        :returns: 
        :rtype: None
        """
        ...

    def set_label_show(self, antialias: bool) -> None:
        """
        Sets label visibility 
        
        :param antialias: true/false to enable tick label 
        :type antialias: bool

        :returns: 
        :rtype: None
        """
        ...

    def set_range(self, x: int, y: int) -> None:
        """
        Set the minimal and maximal values on a scale 
        
        :param x: minimum value of the scale 
        :type x: int
        :param y: maximum value of the scale 
        :type y: int

        :returns: 
        :rtype: None
        """
        ...

    def set_angle_range(self, delay_ms: int) -> None:
        """
        Set properties specific to round scale 
        
        :param delay_ms: the angular range of the scale 
        :type delay_ms: int

        :returns: 
        :rtype: None
        """
        ...

    def set_rotation(self, index: int) -> None:
        """
        Set properties specific to round scale 
        
        :param index: the angular offset from the 3 o'clock position (clock-wise) 
        :type index: int

        :returns: 
        :rtype: None
        """
        ...

    def set_line_needle_value(self, needle_line: "obj", needle_length: int, value: int) -> None:
        """
        Point the needle to the corresponding value through the line 
        
        :param needle_line: needle_line of the scale. The line points will be allocated and managed by the scale unless the line point array was previously set using lv_line_set_points_mutable . 
        :type needle_line: "obj"
        :param needle_length: length of the needle needle_length>0 needle_length=needle_length; needle_length<0 needle_length=radius-|needle_length|; 
        :type needle_length: int
        :param value: needle to point to the corresponding value 
        :type value: int

        :returns: 
        :rtype: None
        """
        ...

    def set_image_needle_value(self, needle_img: "obj", value: int) -> None:
        """
        Point the needle to the corresponding value through the image, image must point to the right. E.g. -O--- > 
        
        :param needle_img: needle_img of the scale 
        :type needle_img: "obj"
        :param value: needle to point to the corresponding value 
        :type value: int

        :returns: 
        :rtype: None
        """
        ...

    def set_text_src(self, txt_src: List[str]) -> None:
        """
        Set custom text source for major ticks labels 
        
        :param txt_src: pointer to an array of strings which will be display at major ticks 
        :type txt_src: List[str]

        :returns: 
        :rtype: None
        """
        ...

    def set_post_draw(self, antialias: bool) -> None:
        """
        Draw the scale after all the children are drawn 
        
        :param antialias: true: enable post draw 
        :type antialias: bool

        :returns: 
        :rtype: None
        """
        ...

    def set_draw_ticks_on_top(self, antialias: bool) -> None:
        """
        Draw the scale ticks on top of all parts 
        
        :param antialias: true: enable draw ticks on top of all parts 
        :type antialias: bool

        :returns: 
        :rtype: None
        """
        ...

    def add_section(self) -> "scale":
        """
        Add a section to the given scale pointer to the new section 
        

        :returns: pointer to the new section 
        :rtype: "scale"
        """
        ...

    def section_set_range(self, minor_range: int, major_range: int) -> None:
        """
        Set the range for the given scale section 
        
        :param minor_range: section new minor range 
        :type minor_range: int
        :param major_range: section new major range 
        :type major_range: int

        :returns: 
        :rtype: None
        """
        ...

    def section_set_style(self, part: part_t, section_part_style: "style_t") -> None:
        """
        Set the style of the part for the given scale section 
        
        :param part: the part for the section, e.g. LV_PART_INDICATOR 
        :type part: part_t
        :param section_part_style: Pointer to the section part style 
        :type section_part_style: "style_t"

        :returns: 
        :rtype: None
        """
        ...

    def get_mode(self) -> "scale":
        """
        Get scale mode. See lv_scale_mode_t Scale mode 
        

        :returns: Scale mode 
        :rtype: "scale"
        """
        ...

    def get_total_tick_count(self) -> int:
        """
        Get scale total tick count (including minor and major ticks) Scale total tick count 
        

        :returns: Scale total tick count 
        :rtype: int
        """
        ...

    def get_major_tick_every(self) -> int:
        """
        Gets how often the major tick will be drawn Scale major tick every count 
        

        :returns: Scale major tick every count 
        :rtype: int
        """
        ...

    def get_label_show(self) -> bool:
        """
        Gets label visibility true if tick label is enabled, false otherwise 
        

        :returns: true if tick label is enabled, false otherwise 
        :rtype: bool
        """
        ...

    def get_angle_range(self) -> int:
        """
        Get angle range of a round scale Scale angle_range 
        

        :returns: Scale angle_range 
        :rtype: int
        """
        ...

    def get_range_min_value(self) -> int:
        """
        Get the min range for the given scale section section minor range 
        

        :returns: section minor range 
        :rtype: int
        """
        ...

    def get_range_max_value(self) -> int:
        """
        Get the max range for the given scale section section max range 
        

        :returns: section max range 
        :rtype: int
        """
        ...



class slider(obj):

    class MODE(object):

        NORMAL: ClassVar[int] = ...
        SYMMETRICAL: ClassVar[int] = ...
        RANGE: ClassVar[int] = ...
        
        def __init__(self, *, parent: "obj"):
            ...

    
    def __init__(self, *, parent: "obj"):
        """
        Create a slider object pointer to the created slider 
        """
        ...

    def set_value(self, x: int, anim_en: "anim_enable_t") -> None:
        """
        Set a new value on the slider 
        
        :param x: the new value 
        :type x: int
        :param anim_en: LV_ANIM_ON: set the value with an animation; LV_ANIM_OFF: change the value immediately 
        :type anim_en: "anim_enable_t"

        :returns: 
        :rtype: None
        """
        ...

    def set_left_value(self, x: int, anim_en: "anim_enable_t") -> None:
        """
        Set a new value for the left knob of a slider 
        
        :param x: new value 
        :type x: int
        :param anim_en: LV_ANIM_ON: set the value with an animation; LV_ANIM_OFF: change the value immediately 
        :type anim_en: "anim_enable_t"

        :returns: 
        :rtype: None
        """
        ...

    def set_range(self, x: int, y: int) -> None:
        """
        Set minimum and the maximum values of a bar 
        
        :param x: minimum value 
        :type x: int
        :param y: maximum value 
        :type y: int

        :returns: 
        :rtype: None
        """
        ...

    def set_mode(self, mode: "slider") -> None:
        """
        Set the mode of slider. 
        
        :param mode: the mode of the slider. See ::lv_slider_mode_t 
        :type mode: "slider"

        :returns: 
        :rtype: None
        """
        ...

    def get_value(self) -> int:
        """
        Get the value of the main knob of a slider the value of the main knob of the slider 
        

        :returns: the value of the main knob of the slider 
        :rtype: int
        """
        ...

    def get_left_value(self) -> int:
        """
        Get the value of the left knob of a slider the value of the left knob of the slider 
        

        :returns: the value of the left knob of the slider 
        :rtype: int
        """
        ...

    def get_min_value(self) -> int:
        """
        Get the minimum value of a slider the minimum value of the slider 
        

        :returns: the minimum value of the slider 
        :rtype: int
        """
        ...

    def get_max_value(self) -> int:
        """
        Get the maximum value of a slider the maximum value of the slider 
        

        :returns: the maximum value of the slider 
        :rtype: int
        """
        ...

    def is_dragged(self) -> bool:
        """
        Give the slider is being dragged or not true: drag in progress false: not dragged 
        

        :returns: true: drag in progress false: not dragged 
        :rtype: bool
        """
        ...

    def get_mode(self) -> "slider":
        """
        Get the mode of the slider. see ::lv_slider_mode_t 
        

        :returns: see ::lv_slider_mode_t 
        :rtype: "slider"
        """
        ...

    def is_symmetrical(self) -> bool:
        """
        Give the slider is in symmetrical mode or not true: in symmetrical mode false : not in 
        

        :returns: true: in symmetrical mode false : not in 
        :rtype: bool
        """
        ...

    def bind_value(self, subject: "subject_t") -> "observer_t":
        """
        Bind an integer subject to a slider's value pointer to the created observer 
        
        :param subject: pointer to a subject 
        :type subject: "subject_t"

        :returns: pointer to the created observer 
        :rtype: "observer_t"
        """
        ...



class spangroup(obj):
    
    def __init__(self, *, parent: "obj"):
        """
        Create a spangroup object pointer to the created spangroup 
        """
        ...

    def new_span(self) -> "span_t":
        """
        Create a span string descriptor and add to spangroup. pointer to the created span. 
        

        :returns: pointer to the created span. 
        :rtype: "span_t"
        """
        ...

    def delete_span(self, span: "span_t") -> None:
        """
        Remove the span from the spangroup and free memory. 
        
        :param span: pointer to a span. 
        :type span: "span_t"

        :returns: 
        :rtype: None
        """
        ...

    def set_overflow(self, overflow: span_overflow_t) -> None:
        """
        Set the overflow of the spangroup. 
        
        :param overflow: see lv_span_overflow_t for details. 
        :type overflow: span_overflow_t

        :returns: 
        :rtype: None
        """
        ...

    def set_indent(self, index: int) -> None:
        """
        Set the indent of the spangroup. 
        
        :param index: the first line indentation 
        :type index: int

        :returns: 
        :rtype: None
        """
        ...

    def set_mode(self, mode: span_mode_t) -> None:
        """
        Set the mode of the spangroup. 
        
        :param mode: see lv_span_mode_t for details. 
        :type mode: span_mode_t

        :returns: 
        :rtype: None
        """
        ...

    def set_max_lines(self, index: int) -> None:
        """
        Set maximum lines of the spangroup. 
        
        :param index: max lines that can be displayed in LV_SPAN_MODE_BREAK mode. < 0 means no limit. 
        :type index: int

        :returns: 
        :rtype: None
        """
        ...

    def get_span_count(self) -> int:
        """
        Get number of spans the span count of the spangroup. 
        

        :returns: the span count of the spangroup. 
        :rtype: int
        """
        ...

    def get_align(self) -> "text_align_t":
        """
        Get the align of the spangroup. the align value. 
        

        :returns: the align value. 
        :rtype: "text_align_t"
        """
        ...

    def get_overflow(self) -> "span_overflow_t":
        """
        Get the overflow of the spangroup. the overflow value. 
        

        :returns: the overflow value. 
        :rtype: "span_overflow_t"
        """
        ...

    def get_indent(self) -> int:
        """
        Get the indent of the spangroup. the indent value. 
        

        :returns: the indent value. 
        :rtype: int
        """
        ...

    def get_mode(self) -> "span_mode_t":
        """
        Get the mode of the spangroup. 
        

        :returns: 
        :rtype: "span_mode_t"
        """
        ...

    def get_max_lines(self) -> int:
        """
        Get maximum lines of the spangroup. the max lines value. 
        

        :returns: the max lines value. 
        :rtype: int
        """
        ...

    def get_max_line_height(self) -> int:
        """
        Get max line height of all span in the spangroup. 
        

        :returns: 
        :rtype: int
        """
        ...

    def get_expand_width(self, max_width: int) -> int:
        """
        Get the text content width when all span of spangroup on a line. text content width or max_width. 
        
        :param max_width: if text content width >= max_width, return max_width to reduce computation, if max_width == 0, returns the text content width. 
        :type max_width: int

        :returns: text content width or max_width. 
        :rtype: int
        """
        ...

    def get_expand_height(self, width: int) -> int:
        """
        Get the text content height with width fixed. 
        
        :param width: the width of the span group. 
        :type width: int

        :returns: 
        :rtype: int
        """
        ...

    def refr_mode(self) -> None:
        """
        Update the mode of the spangroup. 
        

        :returns: 
        :rtype: None
        """
        ...



class textarea(obj):
    
    def __init__(self, *, parent: "obj"):
        """
        Create a text area object pointer to the created text area 
        """
        ...

    def add_char(self, delay_ms: int) -> None:
        """
        Insert a character to the current cursor position. To add a wide char, e.g. 'Á' use lv_text_encoded_conv_wc('Á )` 
        
        :param delay_ms: a character (e.g. 'a') 
        :type delay_ms: int

        :returns: 
        :rtype: None
        """
        ...

    def add_text(self, text: str) -> None:
        """
        Insert a text to the current cursor position 
        
        :param text: a '\0' terminated string to insert 
        :type text: str

        :returns: 
        :rtype: None
        """
        ...

    def delete_char(self) -> None:
        """
        Delete a the left character from the current cursor position 
        

        :returns: 
        :rtype: None
        """
        ...

    def delete_char_forward(self) -> None:
        """
        Delete the right character from the current cursor position 
        

        :returns: 
        :rtype: None
        """
        ...

    def set_text(self, text: str) -> None:
        """
        Set the text of a text area 
        
        :param text: pointer to the text 
        :type text: str

        :returns: 
        :rtype: None
        """
        ...

    def set_placeholder_text(self, text: str) -> None:
        """
        Set the placeholder text of a text area 
        
        :param text: pointer to the text 
        :type text: str

        :returns: 
        :rtype: None
        """
        ...

    def set_cursor_pos(self, index: int) -> None:
        """
        Set the cursor position 
        
        :param index: the new cursor position in character index < 0 : index from the end of the text LV_TEXTAREA_CURSOR_LAST: go after the last character 
        :type index: int

        :returns: 
        :rtype: None
        """
        ...

    def set_cursor_click_pos(self, antialias: bool) -> None:
        """
        Enable/Disable the positioning of the cursor by clicking the text on the text area. 
        
        :param antialias: true: enable click positions; false: disable 
        :type antialias: bool

        :returns: 
        :rtype: None
        """
        ...

    def set_password_mode(self, antialias: bool) -> None:
        """
        Enable/Disable password mode 
        
        :param antialias: true: enable, false: disable 
        :type antialias: bool

        :returns: 
        :rtype: None
        """
        ...

    def set_password_bullet(self, text: str) -> None:
        """
        Set the replacement characters to show in password mode 
        
        :param text: pointer to the replacement text 
        :type text: str

        :returns: 
        :rtype: None
        """
        ...

    def set_one_line(self, antialias: bool) -> None:
        """
        Configure the text area to one line or back to normal 
        
        :param antialias: true: one line, false: normal 
        :type antialias: bool

        :returns: 
        :rtype: None
        """
        ...

    def set_accepted_chars(self, text: str) -> None:
        """
        Set a list of characters. Only these characters will be accepted by the text area 
        
        :param text: list of characters. Only the pointer is saved. E.g. "+-.,0123456789" 
        :type text: str

        :returns: 
        :rtype: None
        """
        ...

    def set_max_length(self, delay_ms: int) -> None:
        """
        Set max length of a Text Area. 
        
        :param delay_ms: the maximal number of characters can be added ( lv_textarea_set_text ignores it) 
        :type delay_ms: int

        :returns: 
        :rtype: None
        """
        ...

    def set_insert_replace(self, text: str) -> None:
        """
        In LV_EVENT_INSERT the text which planned to be inserted can be replaced by another text. It can be used to add automatic formatting to the text area. 
        
        :param text: pointer to a new string to insert. If "" no text will be added. The variable must be live after the event_cb exists. (Should be global or static ) 
        :type text: str

        :returns: 
        :rtype: None
        """
        ...

    def set_text_selection(self, antialias: bool) -> None:
        """
        Enable/disable selection mode. 
        
        :param antialias: true or false to enable/disable selection mode 
        :type antialias: bool

        :returns: 
        :rtype: None
        """
        ...

    def set_password_show_time(self, delay_ms: int) -> None:
        """
        Set how long show the password before changing it to '*' 
        
        :param delay_ms: show time in milliseconds. 0: hide immediately. 
        :type delay_ms: int

        :returns: 
        :rtype: None
        """
        ...

    def get_text(self) -> str:
        """
        Get the text of a text area. In password mode it gives the real text (not '*'s). pointer to the text 
        

        :returns: pointer to the text 
        :rtype: str
        """
        ...

    def get_placeholder_text(self) -> str:
        """
        Get the placeholder text of a text area pointer to the text 
        

        :returns: pointer to the text 
        :rtype: str
        """
        ...

    def get_label(self) -> "obj":
        """
        Get the label of a text area pointer to the label object 
        

        :returns: pointer to the label object 
        :rtype: "obj"
        """
        ...

    def get_cursor_pos(self) -> int:
        """
        Get the current cursor position in character index the cursor position 
        

        :returns: the cursor position 
        :rtype: int
        """
        ...

    def get_cursor_click_pos(self) -> bool:
        """
        Get whether the cursor click positioning is enabled or not. true: enable click positions; false: disable 
        

        :returns: true: enable click positions; false: disable 
        :rtype: bool
        """
        ...

    def get_password_mode(self) -> bool:
        """
        Get the password mode attribute true: password mode is enabled, false: disabled 
        

        :returns: true: password mode is enabled, false: disabled 
        :rtype: bool
        """
        ...

    def get_password_bullet(self) -> str:
        """
        Get the replacement characters to show in password mode pointer to the replacement text 
        

        :returns: pointer to the replacement text 
        :rtype: str
        """
        ...

    def get_one_line(self) -> bool:
        """
        Get the one line configuration attribute true: one line configuration is enabled, false: disabled 
        

        :returns: true: one line configuration is enabled, false: disabled 
        :rtype: bool
        """
        ...

    def get_accepted_chars(self) -> str:
        """
        Get a list of accepted characters. list of accented characters. 
        

        :returns: list of accented characters. 
        :rtype: str
        """
        ...

    def get_max_length(self) -> int:
        """
        Get max length of a Text Area. the maximal number of characters to be add 
        

        :returns: the maximal number of characters to be add 
        :rtype: int
        """
        ...

    def text_is_selected(self) -> bool:
        """
        Find whether text is selected or not. whether text is selected or not 
        

        :returns: whether text is selected or not 
        :rtype: bool
        """
        ...

    def get_text_selection(self) -> bool:
        """
        Find whether selection mode is enabled. true: selection mode is enabled, false: disabled 
        

        :returns: true: selection mode is enabled, false: disabled 
        :rtype: bool
        """
        ...

    def get_password_show_time(self) -> int:
        """
        Set how long show the password before changing it to '*' show time in milliseconds. 0: hide immediately. 
        

        :returns: show time in milliseconds. 0: hide immediately. 
        :rtype: int
        """
        ...

    def get_current_char(self) -> int:
        """
        Get a the character from the current cursor position a the character or 0 
        

        :returns: a the character or 0 
        :rtype: int
        """
        ...

    def clear_selection(self) -> None:
        """
        Clear the selection on the text area. 
        

        :returns: 
        :rtype: None
        """
        ...

    def cursor_right(self) -> None:
        """
        Move the cursor one character right 
        

        :returns: 
        :rtype: None
        """
        ...

    def cursor_left(self) -> None:
        """
        Move the cursor one character left 
        

        :returns: 
        :rtype: None
        """
        ...

    def cursor_down(self) -> None:
        """
        Move the cursor one line down 
        

        :returns: 
        :rtype: None
        """
        ...

    def cursor_up(self) -> None:
        """
        Move the cursor one line up 
        

        :returns: 
        :rtype: None
        """
        ...



class spinbox(obj):
    
    def __init__(self, *, parent: "obj"):
        """
        Create a spinbox object pointer to the created spinbox 
        """
        ...

    def set_value(self, index: int) -> None:
        """
        Set spinbox value 
        
        :param index: value to be set 
        :type index: int

        :returns: 
        :rtype: None
        """
        ...

    def set_rollover(self, antialias: bool) -> None:
        """
        Set spinbox rollover function 
        
        :param antialias: true or false to enable or disable (default) 
        :type antialias: bool

        :returns: 
        :rtype: None
        """
        ...

    def set_digit_format(self, time: int, delay: int) -> None:
        """
        Set spinbox digit format (digit count and decimal format) 
        
        :param time: number of digit excluding the decimal separator and the sign 
        :type time: int
        :param delay: number of digit before the decimal point. If 0, decimal point is not shown 
        :type delay: int

        :returns: 
        :rtype: None
        """
        ...

    def set_step(self, delay_ms: int) -> None:
        """
        Set spinbox step 
        
        :param delay_ms: steps on increment/decrement. Can be 1, 10, 100, 1000, etc the digit that will change. 
        :type delay_ms: int

        :returns: 
        :rtype: None
        """
        ...

    def set_range(self, x: int, y: int) -> None:
        """
        Set spinbox value range 
        
        :param x: maximum value, inclusive 
        :type x: int
        :param y: minimum value, inclusive 
        :type y: int

        :returns: 
        :rtype: None
        """
        ...

    def set_cursor_pos(self, delay_ms: int) -> None:
        """
        Set cursor position to a specific digit for edition 
        
        :param delay_ms: selected position in spinbox 
        :type delay_ms: int

        :returns: 
        :rtype: None
        """
        ...

    def set_digit_step_direction(self, dir: dir_t) -> None:
        """
        Set direction of digit step when clicking an encoder button while in editing mode 
        
        :param dir: the direction (LV_DIR_RIGHT or LV_DIR_LEFT) 
        :type dir: dir_t

        :returns: 
        :rtype: None
        """
        ...

    def get_rollover(self) -> bool:
        """
        Get spinbox rollover function status 
        

        :returns: 
        :rtype: bool
        """
        ...

    def get_value(self) -> int:
        """
        Get the spinbox numeral value (user has to convert to float according to its digit format) value integer value of the spinbox 
        

        :returns: value integer value of the spinbox 
        :rtype: int
        """
        ...

    def get_step(self) -> int:
        """
        Get the spinbox step value (user has to convert to float according to its digit format) value integer step value of the spinbox 
        

        :returns: value integer step value of the spinbox 
        :rtype: int
        """
        ...

    def step_next(self) -> None:
        """
        Select next lower digit for edition by dividing the step by 10 
        

        :returns: 
        :rtype: None
        """
        ...

    def step_prev(self) -> None:
        """
        Select next higher digit for edition by multiplying the step by 10 
        

        :returns: 
        :rtype: None
        """
        ...

    def increment(self) -> None:
        """
        Increment spinbox value by one step 
        

        :returns: 
        :rtype: None
        """
        ...

    def decrement(self) -> None:
        """
        Decrement spinbox value by one step 
        

        :returns: 
        :rtype: None
        """
        ...



class spinner(obj):
    
    def __init__(self, *, parent: "obj"):
        """
        Create a spinner widget the created spinner 
        """
        ...

    def set_anim_params(self, time: int, delay: int) -> None:
        """
        Set the animation time and arc length of the spinner 
        
        :param time: the animation time in milliseconds 
        :type time: int
        :param delay: the angle of the arc in degrees 
        :type delay: int

        :returns: 
        :rtype: None
        """
        ...



class switch(obj):
    
    def __init__(self, *, parent: "obj"):
        """
        Create a switch object pointer to the created switch 
        """
        ...


class table(obj):

    class CELL_CTRL(object):

        MERGE_RIGHT: ClassVar[int] = ...
        TEXT_CROP: ClassVar[int] = ...
        CUSTOM_1: ClassVar[int] = ...
        CUSTOM_2: ClassVar[int] = ...
        CUSTOM_3: ClassVar[int] = ...
        CUSTOM_4: ClassVar[int] = ...
        
        def __init__(self, *, parent: "obj"):
            ...

    
    def __init__(self, *, parent: "obj"):
        """
        Create a table object pointer to the created table 
        """
        ...

    def set_cell_value(self, row: int, col: int, txt: str) -> None:
        """
        Set the value of a cell. New roes/columns are added automatically if required 
        
        :param row: id of the row [0 .. row_cnt -1] 
        :type row: int
        :param col: id of the column [0 .. col_cnt -1] 
        :type col: int
        :param txt: text to display in the cell. It will be copied and saved so this variable is not required after this function call. 
        :type txt: str

        :returns: 
        :rtype: None
        """
        ...

    def set_row_count(self, delay_ms: int) -> None:
        """
        Set the number of rows 
        
        :param delay_ms: number of rows 
        :type delay_ms: int

        :returns: 
        :rtype: None
        """
        ...

    def set_column_count(self, delay_ms: int) -> None:
        """
        Set the number of columns 
        
        :param delay_ms: number of columns. 
        :type delay_ms: int

        :returns: 
        :rtype: None
        """
        ...

    def set_column_width(self, col_id: int, w: int) -> None:
        """
        Set the width of a column 
        
        :param col_id: id of the column [0 .. LV_TABLE_COL_MAX -1] 
        :type col_id: int
        :param w: width of the column 
        :type w: int

        :returns: 
        :rtype: None
        """
        ...

    def add_cell_ctrl(self, row: int, col: int, ctrl: "table") -> None:
        """
        Add control bits to the cell. 
        
        :param row: id of the row [0 .. row_cnt -1] 
        :type row: int
        :param col: id of the column [0 .. col_cnt -1] 
        :type col: int
        :param ctrl: OR-ed values from ::lv_table_cell_ctrl_t 
        :type ctrl: "table"

        :returns: 
        :rtype: None
        """
        ...

    def clear_cell_ctrl(self, row: int, col: int, ctrl: "table") -> None:
        """
        Clear control bits of the cell. 
        
        :param row: id of the row [0 .. row_cnt -1] 
        :type row: int
        :param col: id of the column [0 .. col_cnt -1] 
        :type col: int
        :param ctrl: OR-ed values from ::lv_table_cell_ctrl_t 
        :type ctrl: "table"

        :returns: 
        :rtype: None
        """
        ...

    def set_cell_user_data(self, row: int, col: int, obj: "obj") -> None:
        """
        Add custom user data to the cell. 
        
        :param row: id of the row [0 .. row_cnt -1] 
        :type row: int
        :param col: id of the column [0 .. col_cnt -1] 
        :type col: int
        :param obj: pointer to the new user_data. Should be allocated by lv_malloc , and it will be freed automatically when the table is deleted or when the cell is dropped due to lower row or column count. 
        :type obj: "obj"

        :returns: 
        :rtype: None
        """
        ...

    def set_selected_cell(self, row: int, col: int) -> None:
        """
        Set the selected cell 
        
        :param row: id of the cell row to select 
        :type row: int
        :param col: id of the cell column to select 
        :type col: int

        :returns: 
        :rtype: None
        """
        ...

    def get_cell_value(self, row: int, col: int) -> str:
        """
        Get the value of a cell. text in the cell 
        
        :param row: id of the row [0 .. row_cnt -1] 
        :type row: int
        :param col: id of the column [0 .. col_cnt -1] 
        :type col: int

        :returns: text in the cell 
        :rtype: str
        """
        ...

    def get_row_count(self) -> int:
        """
        Get the number of rows. number of rows. 
        

        :returns: number of rows. 
        :rtype: int
        """
        ...

    def get_column_count(self) -> int:
        """
        Get the number of columns. number of columns. 
        

        :returns: number of columns. 
        :rtype: int
        """
        ...

    def get_column_width(self, col: int) -> int:
        """
        Get the width of a column width of the column 
        
        :param col: id of the column [0 .. LV_TABLE_COL_MAX -1] 
        :type col: int

        :returns: width of the column 
        :rtype: int
        """
        ...

    def has_cell_ctrl(self, row: int, col: int, ctrl: "table") -> bool:
        """
        Get whether a cell has the control bits true: all control bits are set; false: not all control bits are set 
        
        :param row: id of the row [0 .. row_cnt -1] 
        :type row: int
        :param col: id of the column [0 .. col_cnt -1] 
        :type col: int
        :param ctrl: OR-ed values from ::lv_table_cell_ctrl_t 
        :type ctrl: "table"

        :returns: true: all control bits are set; false: not all control bits are set 
        :rtype: bool
        """
        ...

    def get_selected_cell(self, row: List[int], col: List[int]) -> None:
        """
        Get the selected cell (pressed and or focused) 
        
        :param row: pointer to variable to store the selected row (LV_TABLE_CELL_NONE: if no cell selected) 
        :type row: List[int]
        :param col: pointer to variable to store the selected column (LV_TABLE_CELL_NONE: if no cell selected) 
        :type col: List[int]

        :returns: 
        :rtype: None
        """
        ...

    def get_cell_user_data(self, row: int, col: int) -> Any:
        """
        Get custom user data to the cell. 
        
        :param row: id of the row [0 .. row_cnt -1] 
        :type row: int
        :param col: id of the column [0 .. col_cnt -1] 
        :type col: int

        :returns: 
        :rtype: Any
        """
        ...



class tabview(obj):
    
    def __init__(self, *, parent: "obj"):
        """
        Create a tabview widget the created tabview 
        """
        ...

    def add_tab(self, txt: str) -> "obj":
        """
        Add a tab to the tabview the widget where the content of the tab can be created 
        
        :param txt: the name of the tab, it will be displayed on the tab bar 
        :type txt: str

        :returns: the widget where the content of the tab can be created 
        :rtype: "obj"
        """
        ...

    def rename_tab(self, pos: int, txt: str) -> None:
        """
        Change the name of the tab 
        
        :param pos: the index of the tab to rename 
        :type pos: int
        :param txt: the new name as a string 
        :type txt: str

        :returns: 
        :rtype: None
        """
        ...

    def set_active(self, sel_opt: int, anim: "anim_enable_t") -> None:
        """
        Show a tab 
        
        :param sel_opt: the index of the tab to show 
        :type sel_opt: int
        :param anim: LV_ANIM_ON/OFF 
        :type anim: "anim_enable_t"

        :returns: 
        :rtype: None
        """
        ...

    def set_tab_bar_position(self, dir: dir_t) -> None:
        """
        Set the position of the tab bar 
        
        :param dir: LV_DIR_TOP/BOTTOM/LEFT/RIGHT 
        :type dir: dir_t

        :returns: 
        :rtype: None
        """
        ...

    def set_tab_bar_size(self, index: int) -> None:
        """
        Set the width or height of the tab bar 
        
        :param index: size of the tab bar in pixels or percentage. will be used as width or height based on the position of the tab bar) 
        :type index: int

        :returns: 
        :rtype: None
        """
        ...

    def get_tab_count(self) -> int:
        """
        Get the number of tabs the number of tabs 
        

        :returns: the number of tabs 
        :rtype: int
        """
        ...

    def get_tab_active(self) -> int:
        """
        Get the current tab's index the zero based index of the current tab 
        

        :returns: the zero based index of the current tab 
        :rtype: int
        """
        ...

    def get_content(self) -> "obj":
        """
        Get the widget where the container of each tab is created the main container widget 
        

        :returns: the main container widget 
        :rtype: "obj"
        """
        ...

    def get_tab_bar(self) -> "obj":
        """
        Get the tab bar where the buttons are created the tab bar 
        

        :returns: the tab bar 
        :rtype: "obj"
        """
        ...



class tileview(obj):
    
    def __init__(self, *, parent: "obj"):
        """
        Create a Tileview object pointer to the created tileview 
        """
        ...

    def add_tile(self, col_id: int, row_id: int, dir: dir_t) -> "obj":
        """
        :param col_id: 
        :type col_id: int
        :param row_id: 
        :type row_id: int
        :param dir: 
        :type dir: dir_t

        :returns: 
        :rtype: "obj"
        """
        ...

    def set_tile(self, tile_obj: "obj", anim_en: "anim_enable_t") -> None:
        """
        :param tile_obj: 
        :type tile_obj: "obj"
        :param anim_en: 
        :type anim_en: "anim_enable_t"

        :returns: 
        :rtype: None
        """
        ...

    def set_tile_by_index(self, col_id: int, row_id: int, anim_en: "anim_enable_t") -> None:
        """
        :param col_id: 
        :type col_id: int
        :param row_id: 
        :type row_id: int
        :param anim_en: 
        :type anim_en: "anim_enable_t"

        :returns: 
        :rtype: None
        """
        ...

    def get_tile_active(self) -> "obj":
        """

        :returns: 
        :rtype: "obj"
        """
        ...



class win(obj):
    
    def __init__(self, *, parent: "obj"):
        ...

    def add_title(self, txt: str) -> "obj":
        """
        :param txt: 
        :type txt: str

        :returns: 
        :rtype: "obj"
        """
        ...

    def add_button(self, icon: Any, btn_w: int) -> "obj":
        """
        :param icon: 
        :type icon: Any
        :param btn_w: 
        :type btn_w: int

        :returns: 
        :rtype: "obj"
        """
        ...

    def get_header(self) -> "obj":
        """

        :returns: 
        :rtype: "obj"
        """
        ...

    def get_content(self) -> "obj":
        """

        :returns: 
        :rtype: "obj"
        """
        ...



class ime_pinyin(obj):

    class PINYIN_MODE(object):

        K26: ClassVar[int] = ...
        K9: ClassVar[int] = ...
        K9_NUMBER: ClassVar[int] = ...
        
        def __init__(self, *, parent: "obj"):
            ...

    
    def __init__(self, *, parent: "obj"):
        ...

    def pinyin_set_keyboard(self, parent: "obj") -> None:
        """

        :returns: 
        :rtype: None
        """
        ...

    def pinyin_set_dict(self, dict: "pinyin_dict_t") -> None:
        """

        :returns: 
        :rtype: None
        """
        ...

    def pinyin_set_mode(self, mode: "ime_pinyin") -> None:
        """

        :returns: 
        :rtype: None
        """
        ...

    def pinyin_get_kb(self) -> "obj":
        """

        :returns: 
        :rtype: "obj"
        """
        ...

    def pinyin_get_cand_panel(self) -> "obj":
        """

        :returns: 
        :rtype: "obj"
        """
        ...

    def pinyin_get_dict(self) -> "pinyin_dict_t":
        """

        :returns: 
        :rtype: "pinyin_dict_t"
        """
        ...



class barcode(obj):
    
    def __init__(self, *, parent: "obj"):
        ...

    def set_dark_color(self, color: "color_t") -> None:
        """

        :returns: 
        :rtype: None
        """
        ...

    def set_light_color(self, color: "color_t") -> None:
        """

        :returns: 
        :rtype: None
        """
        ...

    def set_scale(self, scale: int) -> None:
        """

        :returns: 
        :rtype: None
        """
        ...

    def set_direction(self, dir: dir_t) -> None:
        """

        :returns: 
        :rtype: None
        """
        ...

    def set_tiled(self, antialias: bool) -> None:
        """

        :returns: 
        :rtype: None
        """
        ...

    def update(self, data: str) -> "result_t":
        """

        :returns: 
        :rtype: "result_t"
        """
        ...

    def get_dark_color(self) -> "color_t":
        """

        :returns: 
        :rtype: "color_t"
        """
        ...

    def get_light_color(self) -> "color_t":
        """

        :returns: 
        :rtype: "color_t"
        """
        ...

    def get_scale(self) -> int:
        """

        :returns: 
        :rtype: int
        """
        ...



class gif(obj):
    
    def __init__(self, *, parent: "obj"):
        ...

    def set_src(self, src: Any) -> None:
        """

        :returns: 
        :rtype: None
        """
        ...

    def restart(self) -> None:
        """

        :returns: 
        :rtype: None
        """
        ...

    def pause(self) -> None:
        """

        :returns: 
        :rtype: None
        """
        ...

    def resume(self) -> None:
        """

        :returns: 
        :rtype: None
        """
        ...

    def is_loaded(self) -> bool:
        """

        :returns: 
        :rtype: bool
        """
        ...

    def get_loop_count(self) -> int:
        """

        :returns: 
        :rtype: int
        """
        ...

    def set_loop_count(self, index: int) -> None:
        """

        :returns: 
        :rtype: None
        """
        ...



class qrcode(obj):
    
    def __init__(self, *, parent: "obj"):
        ...

    def set_dark_color(self, color: "color_t") -> None:
        """

        :returns: 
        :rtype: None
        """
        ...

    def set_light_color(self, color: "color_t") -> None:
        """

        :returns: 
        :rtype: None
        """
        ...

    def update(self, data: Any, data_len: int) -> "result_t":
        """

        :returns: 
        :rtype: "result_t"
        """
        ...



class _type_obj_class(TypedDict, total=False):
    pass


class obj_class(Struct):
    
    def __init__(self, *, kwargs: _type_obj_class = dict()):
        ...


class _type_image_class(TypedDict, total=False):
    pass


class image_class(Struct):
    
    def __init__(self, *, kwargs: _type_image_class = dict()):
        ...


class _type_animimg_class(TypedDict, total=False):
    pass


class animimg_class(Struct):
    
    def __init__(self, *, kwargs: _type_animimg_class = dict()):
        ...


class _type_arc_class(TypedDict, total=False):
    pass


class arc_class(Struct):
    
    def __init__(self, *, kwargs: _type_arc_class = dict()):
        ...


class _type_label_class(TypedDict, total=False):
    pass


class label_class(Struct):
    
    def __init__(self, *, kwargs: _type_label_class = dict()):
        ...


class _type_bar_class(TypedDict, total=False):
    pass


class bar_class(Struct):
    
    def __init__(self, *, kwargs: _type_bar_class = dict()):
        ...


class _type_button_class(TypedDict, total=False):
    pass


class button_class(Struct):
    
    def __init__(self, *, kwargs: _type_button_class = dict()):
        ...


class _type_buttonmatrix_class(TypedDict, total=False):
    pass


class buttonmatrix_class(Struct):
    
    def __init__(self, *, kwargs: _type_buttonmatrix_class = dict()):
        ...


class _type_calendar_class(TypedDict, total=False):
    pass


class calendar_class(Struct):
    
    def __init__(self, *, kwargs: _type_calendar_class = dict()):
        ...


class _type_calendar_header_arrow_class(TypedDict, total=False):
    pass


class calendar_header_arrow_class(Struct):
    
    def __init__(self, *, kwargs: _type_calendar_header_arrow_class = dict()):
        ...


class _type_calendar_header_dropdown_class(TypedDict, total=False):
    pass


class calendar_header_dropdown_class(Struct):
    
    def __init__(self, *, kwargs: _type_calendar_header_dropdown_class = dict()):
        ...


class _type_canvas_class(TypedDict, total=False):
    pass


class canvas_class(Struct):
    
    def __init__(self, *, kwargs: _type_canvas_class = dict()):
        ...


class _type_chart_class(TypedDict, total=False):
    pass


class chart_class(Struct):
    
    def __init__(self, *, kwargs: _type_chart_class = dict()):
        ...


class _type_checkbox_class(TypedDict, total=False):
    pass


class checkbox_class(Struct):
    
    def __init__(self, *, kwargs: _type_checkbox_class = dict()):
        ...


class _type_dropdown_class(TypedDict, total=False):
    pass


class dropdown_class(Struct):
    
    def __init__(self, *, kwargs: _type_dropdown_class = dict()):
        ...


class _type_imagebutton_class(TypedDict, total=False):
    pass


class imagebutton_class(Struct):
    
    def __init__(self, *, kwargs: _type_imagebutton_class = dict()):
        ...


class _type_keyboard_class(TypedDict, total=False):
    pass


class keyboard_class(Struct):
    
    def __init__(self, *, kwargs: _type_keyboard_class = dict()):
        ...


class _type_led_class(TypedDict, total=False):
    pass


class led_class(Struct):
    
    def __init__(self, *, kwargs: _type_led_class = dict()):
        ...


class _type_line_class(TypedDict, total=False):
    pass


class line_class(Struct):
    
    def __init__(self, *, kwargs: _type_line_class = dict()):
        ...


class _type_list_class(TypedDict, total=False):
    pass


class list_class(Struct):
    
    def __init__(self, *, kwargs: _type_list_class = dict()):
        ...


class _type_menu_class(TypedDict, total=False):
    pass


class menu_class(Struct):
    
    def __init__(self, *, kwargs: _type_menu_class = dict()):
        ...


class _type_menu_page_class(TypedDict, total=False):
    pass


class menu_page_class(Struct):
    
    def __init__(self, *, kwargs: _type_menu_page_class = dict()):
        ...


class _type_menu_cont_class(TypedDict, total=False):
    pass


class menu_cont_class(Struct):
    
    def __init__(self, *, kwargs: _type_menu_cont_class = dict()):
        ...


class _type_menu_section_class(TypedDict, total=False):
    pass


class menu_section_class(Struct):
    
    def __init__(self, *, kwargs: _type_menu_section_class = dict()):
        ...


class _type_menu_separator_class(TypedDict, total=False):
    pass


class menu_separator_class(Struct):
    
    def __init__(self, *, kwargs: _type_menu_separator_class = dict()):
        ...


class _type_msgbox_class(TypedDict, total=False):
    pass


class msgbox_class(Struct):
    
    def __init__(self, *, kwargs: _type_msgbox_class = dict()):
        ...


class _type_roller_class(TypedDict, total=False):
    pass


class roller_class(Struct):
    
    def __init__(self, *, kwargs: _type_roller_class = dict()):
        ...


class _type_scale_class(TypedDict, total=False):
    pass


class scale_class(Struct):
    
    def __init__(self, *, kwargs: _type_scale_class = dict()):
        ...


class _type_slider_class(TypedDict, total=False):
    pass


class slider_class(Struct):
    
    def __init__(self, *, kwargs: _type_slider_class = dict()):
        ...


class _type_spangroup_class(TypedDict, total=False):
    pass


class spangroup_class(Struct):
    
    def __init__(self, *, kwargs: _type_spangroup_class = dict()):
        ...


class _type_textarea_class(TypedDict, total=False):
    pass


class textarea_class(Struct):
    
    def __init__(self, *, kwargs: _type_textarea_class = dict()):
        ...


class _type_spinbox_class(TypedDict, total=False):
    pass


class spinbox_class(Struct):
    
    def __init__(self, *, kwargs: _type_spinbox_class = dict()):
        ...


class _type_spinner_class(TypedDict, total=False):
    pass


class spinner_class(Struct):
    
    def __init__(self, *, kwargs: _type_spinner_class = dict()):
        ...


class _type_switch_class(TypedDict, total=False):
    pass


class switch_class(Struct):
    
    def __init__(self, *, kwargs: _type_switch_class = dict()):
        ...


class _type_table_class(TypedDict, total=False):
    pass


class table_class(Struct):
    
    def __init__(self, *, kwargs: _type_table_class = dict()):
        ...


class _type_tabview_class(TypedDict, total=False):
    pass


class tabview_class(Struct):
    
    def __init__(self, *, kwargs: _type_tabview_class = dict()):
        ...


class _type_tileview_class(TypedDict, total=False):
    pass


class tileview_class(Struct):
    
    def __init__(self, *, kwargs: _type_tileview_class = dict()):
        ...


class _type_win_class(TypedDict, total=False):
    pass


class win_class(Struct):
    
    def __init__(self, *, kwargs: _type_win_class = dict()):
        ...


class _type_ime_pinyin_class(TypedDict, total=False):
    pass


class ime_pinyin_class(Struct):
    
    def __init__(self, *, kwargs: _type_ime_pinyin_class = dict()):
        ...


class _type_barcode_class(TypedDict, total=False):
    pass


class barcode_class(Struct):
    
    def __init__(self, *, kwargs: _type_barcode_class = dict()):
        ...


class _type_gif_class(TypedDict, total=False):
    pass


class gif_class(Struct):
    
    def __init__(self, *, kwargs: _type_gif_class = dict()):
        ...


class _type_qrcode_class(TypedDict, total=False):
    pass


class qrcode_class(Struct):
    
    def __init__(self, *, kwargs: _type_qrcode_class = dict()):
        ...


color_filter_shade: "color_filter_dsc_t" = ...
cache_class_lru_rb_count: "cache_class_t" = ...
cache_class_lru_rb_size: "cache_class_t" = ...
font_montserrat_14: "font_t" = ...
font_montserrat_16: "font_t" = ...
font_montserrat_24: "font_t" = ...

def memzero(dst: Any, len: int) -> None:
    """
    Same as memset(dst, 0x00, len) . 
    
    :param dst: pointer to the destination buffer 
    :type dst: Any
    :param len: number of byte to set 
    :type len: int

    :returns: 
    :rtype: None
    """
    ...


def sqr(x: int) -> int:
    """
    Calculate the square of an integer (input range is 0..32767). square 
    
    :param x: input 
    :type x: int

    :returns: square 
    :rtype: int
    """
    ...


def bidi_calculate_align(align: text_align_t, base_dir: base_dir_t, txt: str) -> None:
    """
    For compatibility if LV_USE_BIDI = 0 Get the real text alignment from the a text alignment, base direction and a text. 
    
    :param align: For LV_TEXT_ALIGN_AUTO give LV_TEXT_ALIGN_LEFT else leave unchanged, write back the calculated align here 
    :type align: text_align_t
    :param base_dir: Unused 
    :type base_dir: base_dir_t
    :param txt: Unused 
    :type txt: str

    :returns: 
    :rtype: None
    """
    ...


def style_get_prop_group(prop: "style_prop_t") -> int:
    """
    Tell the group of a property. If the a property from a group is set in a style the (1 << group) bit of style->has_group is set. It allows early skipping the style if the property is not exists in the style at all. the group [0..30] 30 means all the custom properties with index > 120 
    
    :param prop: a style property 
    :type prop: "style_prop_t"

    :returns: the group [0..30] 30 means all the custom properties with index > 120 
    :rtype: int
    """
    ...


def style_prop_has_flag(prop: "style_prop_t", flag: int) -> bool:
    """
    Do not pass multiple flags to this function as backwards-compatibility is not guaranteed for that. 
    
    true if the flag is set for this property  
    
    :param prop: Property ID 
    :type prop: "style_prop_t"
    :param flag: Flag 
    :type flag: int

    :returns: true if the flag is set for this property 
    :rtype: bool
    """
    ...


def task_handler() -> int:
    """

    :returns: 
    :rtype: int
    """
    ...


def version_major() -> int:
    """

    :returns: 
    :rtype: int
    """
    ...


def version_minor() -> int:
    """

    :returns: 
    :rtype: int
    """
    ...


def version_patch() -> int:
    """

    :returns: 
    :rtype: int
    """
    ...


def version_info() -> str:
    """

    :returns: 
    :rtype: str
    """
    ...


def init() -> None:
    """
    Initialize LVGL library. Should be called before any other LVGL related function. 
    

    :returns: 
    :rtype: None
    """
    ...


def deinit() -> None:
    """
    Deinit the 'lv' library 
    

    :returns: 
    :rtype: None
    """
    ...


def is_initialized() -> bool:
    """
    Returns whether the 'lv' library is currently initialized 
    

    :returns: 
    :rtype: bool
    """
    ...


def memcpy(dst: Any, src: Any, len: int) -> Any:
    """
    Pointer to the destination array. The function does not check for any overlapping of the source and destination memory blocks. 
    
    :param dst: Pointer to the destination array where the content is to be copied. 
    :type dst: Any
    :param src: Pointer to the source of data to be copied. 
    :type src: Any
    :param len: Number of bytes to copy. 
    :type len: int

    :returns: Pointer to the destination array. 
    :rtype: Any
    """
    ...


def memset(dst: Any, v: int, len: int) -> None:
    """
    :param dst: Pointer to the destination array to fill with the specified value. 
    :type dst: Any
    :param v: Value to be set. The value is passed as an int, but the function fills the block of memory using the unsigned char conversion of this value. 
    :type v: int
    :param len: Number of bytes to be set to the value. 
    :type len: int

    :returns: 
    :rtype: None
    """
    ...


def memmove(dst: Any, src: Any, len: int) -> Any:
    """
    Pointer to the destination array. 
    
    :param dst: Pointer to the destination array where the content is to be copied. 
    :type dst: Any
    :param src: Pointer to the source of data to be copied. 
    :type src: Any
    :param len: Number of bytes to copy 
    :type len: int

    :returns: Pointer to the destination array. 
    :rtype: Any
    """
    ...


def memcmp(p1: Any, p2: Any, len: int) -> int:
    """
    The difference between the value of the first unmatching byte. 
    
    :param p1: Pointer to the first memory block 
    :type p1: Any
    :param p2: Pointer to the second memory block 
    :type p2: Any
    :param len: Number of bytes to compare 
    :type len: int

    :returns: The difference between the value of the first unmatching byte. 
    :rtype: int
    """
    ...


def strlen(str: str) -> int:
    """
    The length of the string in bytes. 
    
    :param str: Pointer to the null-terminated byte string to be examined. 
    :type str: str

    :returns: The length of the string in bytes. 
    :rtype: int
    """
    ...


def strlcpy(dst: str, src: str, dst_size: int) -> int:
    """
    The length of src. The return value is equivalent to the value returned by lv_strlen(src) 
    
    :param dst: Pointer to the destination array where the content is to be copied. 
    :type dst: str
    :param src: Pointer to the source of data to be copied. 
    :type src: str
    :param dst_size: Maximum number of characters to be copied to dst, including the null character. 
    :type dst_size: int

    :returns: The length of src. The return value is equivalent to the value returned by lv_strlen(src) 
    :rtype: int
    """
    ...


def strncpy(dst: str, src: str, dest_size: int) -> str:
    """
    A pointer to the destination array, which is dst. dst will not be null terminated if dest_size bytes were copied from src before the end of src was reached. 
    
    :param dst: Pointer to the destination array where the content is to be copied. 
    :type dst: str
    :param src: Pointer to the source of data to be copied. 
    :type src: str
    :param dest_size: Maximum number of characters to be copied to dst. 
    :type dest_size: int

    :returns: A pointer to the destination array, which is dst. 
    :rtype: str
    """
    ...


def strcpy(dst: str, src: str) -> str:
    """
    A pointer to the destination array, which is dst. 
    
    :param dst: Pointer to the destination array where the content is to be copied. 
    :type dst: str
    :param src: Pointer to the source of data to be copied. 
    :type src: str

    :returns: A pointer to the destination array, which is dst. 
    :rtype: str
    """
    ...


def strcmp(s1: str, s2: str) -> int:
    """
    the difference between the value of the first unmatching character. 
    
    :param s1: pointer to the first string 
    :type s1: str
    :param s2: pointer to the second string 
    :type s2: str

    :returns: the difference between the value of the first unmatching character. 
    :rtype: int
    """
    ...


def strdup(src: str) -> str:
    """
    A pointer to the new allocated string. NULL if failed. 
    
    :param src: Pointer to the source of data to be copied. 
    :type src: str

    :returns: A pointer to the new allocated string. NULL if failed. 
    :rtype: str
    """
    ...


def strcat(dst: str, src: str) -> str:
    """
    A pointer to the destination string, which is dst. 
    
    :param dst: Pointer to the destination string where the content is to be appended. 
    :type dst: str
    :param src: Pointer to the source of data to be copied. 
    :type src: str

    :returns: A pointer to the destination string, which is dst. 
    :rtype: str
    """
    ...


def strncat(dst: str, src: str, dest_size: int) -> str:
    """
    A pointer to the destination string, which is dst. 
    
    :param dst: Pointer to the destination string where the content is to be appended. 
    :type dst: str
    :param src: Pointer to the source of data to be copied. 
    :type src: str
    :param dest_size: Maximum number of characters from src to be copied to the end of dst. 
    :type dest_size: int

    :returns: A pointer to the destination string, which is dst. 
    :rtype: str
    """
    ...


def mem_init() -> None:
    """
    Initialize to use malloc/free/realloc etc 
    

    :returns: 
    :rtype: None
    """
    ...


def mem_deinit() -> None:
    """
    Drop all dynamically allocated memory and reset the memory pools' state 
    

    :returns: 
    :rtype: None
    """
    ...


def mem_add_pool(mem: Any, bytes: int) -> "mem_pool_t":
    """
    :param mem: 
    :type mem: Any
    :param bytes: 
    :type bytes: int

    :returns: 
    :rtype: "mem_pool_t"
    """
    ...


def mem_remove_pool(pool: "mem_pool_t") -> None:
    """
    :param pool: 
    :type pool: "mem_pool_t"

    :returns: 
    :rtype: None
    """
    ...


def malloc(size: int) -> Any:
    """
    Allocate memory dynamically pointer to allocated uninitialized memory, or NULL on failure 
    
    :param size: requested size in bytes 
    :type size: int

    :returns: pointer to allocated uninitialized memory, or NULL on failure 
    :rtype: Any
    """
    ...


def malloc_zeroed(size: int) -> Any:
    """
    Allocate zeroed memory dynamically pointer to allocated zeroed memory, or NULL on failure 
    
    :param size: requested size in bytes 
    :type size: int

    :returns: pointer to allocated zeroed memory, or NULL on failure 
    :rtype: Any
    """
    ...


def free(data: Any) -> None:
    """
    Free an allocated data 
    
    :param data: pointer to an allocated memory 
    :type data: Any

    :returns: 
    :rtype: None
    """
    ...


def realloc(data_p: Any, new_size: int) -> Any:
    """
    Reallocate a memory with a new size. The old content will be kept. pointer to the new memory, NULL on failure 
    
    :param data_p: pointer to an allocated memory. Its content will be copied to the new memory block and freed 
    :type data_p: Any
    :param new_size: the desired new size in byte 
    :type new_size: int

    :returns: pointer to the new memory, NULL on failure 
    :rtype: Any
    """
    ...


def malloc_core(size: int) -> Any:
    """
    Used internally to execute a plain malloc operation 
    
    :param size: size in bytes to malloc 
    :type size: int

    :returns: 
    :rtype: Any
    """
    ...


def free_core(data: Any) -> None:
    """
    Used internally to execute a plain free operation 
    
    :param data: memory address to free 
    :type data: Any

    :returns: 
    :rtype: None
    """
    ...


def realloc_core(data_p: Any, new_size: int) -> Any:
    """
    Used internally to execute a plain realloc operation 
    
    :param data_p: memory address to realloc 
    :type data_p: Any
    :param new_size: size in bytes to realloc 
    :type new_size: int

    :returns: 
    :rtype: Any
    """
    ...


def mem_test_core() -> "result_t":
    """

    :returns: 
    :rtype: "result_t"
    """
    ...


def mem_test() -> "result_t":
    """
    LV_RESULT_OK if the memory allocation system is working properly, or LV_RESULT_INVALID if there is an error. 
    

    :returns: LV_RESULT_OK if the memory allocation system is working properly, or LV_RESULT_INVALID if there is an error. 
    :rtype: "result_t"
    """
    ...


def tick_inc(ms: int) -> None:
    """
    You have to call this function periodically 
    
    :param ms: the call period of this function in milliseconds 
    :type ms: int

    :returns: 
    :rtype: None
    """
    ...


def tick_get() -> int:
    """
    Get the elapsed milliseconds since start up the elapsed milliseconds 
    

    :returns: the elapsed milliseconds 
    :rtype: int
    """
    ...


def tick_elaps(prev_tick: int) -> int:
    """
    Get the elapsed milliseconds since a previous time stamp the elapsed milliseconds since 'prev_tick' 
    
    :param prev_tick: a previous time stamp (return value of :ref:`lv_tick_get()` ) 
    :type prev_tick: int

    :returns: the elapsed milliseconds since 'prev_tick' 
    :rtype: int
    """
    ...


def delay_ms(ms: int) -> None:
    """
    Delay for the given milliseconds. By default it's a blocking delay, but with :ref:`lv_delay_set_cb()` a custom delay function can be set too 
    
    :param ms: the number of milliseconds to delay 
    :type ms: int

    :returns: 
    :rtype: None
    """
    ...


def tick_set_cb(cb: "tick_get_cb_t") -> None:
    """
    Set the custom callback for 'lv_tick_get' 
    
    :param cb: call this callback on 'lv_tick_get' 
    :type cb: "tick_get_cb_t"

    :returns: 
    :rtype: None
    """
    ...


def delay_set_cb(cb: "delay_cb_t") -> None:
    """
    Set a custom callback for 'lv_delay_ms' 
    
    :param cb: call this callback in 'lv_delay_ms' 
    :type cb: "delay_cb_t"

    :returns: 
    :rtype: None
    """
    ...


def timer_handler() -> int:
    """

    :returns: 
    :rtype: int
    """
    ...


def timer_handler_run_in_period(prev_tick: int) -> int:
    """
    Call it in the super-loop of main() or threads. It will run lv_timer_handler() with a given period in ms. You can use it with sleep or delay in OS environment. This function is used to simplify the porting. the time after which it must be called again 
    
    :param prev_tick: the period for running lv_timer_handler() 
    :type prev_tick: int

    :returns: the time after which it must be called again 
    :rtype: int
    """
    ...


def timer_periodic_handler() -> None:
    """
    Call it in the super-loop of main() or threads. It will automatically call lv_timer_handler() at the right time. This function is used to simplify the porting. 
    

    :returns: 
    :rtype: None
    """
    ...


def timer_handler_set_resume_cb(cb: "timer_handler_resume_cb_t", data: Any) -> None:
    """
    Set the resume callback to the timer handler 
    
    :param cb: the function to call when timer handler is resumed 
    :type cb: "timer_handler_resume_cb_t"
    :param data: pointer to a resume data 
    :type data: Any

    :returns: 
    :rtype: None
    """
    ...


def timer_create_basic() -> "timer_t":
    """
    Create an "empty" timer. It needs to be initialized with at least lv_timer_set_cb and lv_timer_set_period  pointer to the created timer 
    

    :returns: pointer to the created timer 
    :rtype: "timer_t"
    """
    ...


def timer_create(user_data: Any, period: int, timer_xcb: Callable[["timer_t"], None]) -> "timer_t":
    """
    Create a new lv_timer pointer to the new timer 
    
    :param user_data: a callback to call periodically. (the 'x' in the argument name indicates that it's not a fully generic function because it not follows the func_name(object, callback, ...) convention) 
    :type user_data: Any
    :param period: call period in ms unit 
    :type period: int
    :param timer_xcb: custom parameter 
    :type timer_xcb: Callable[["timer_t"], None]

    :returns: pointer to the new timer 
    :rtype: "timer_t"
    """
    ...


def timer_enable(en: bool) -> None:
    """
    Enable or disable the whole lv_timer handling 
    
    :param en: true: lv_timer handling is running, false: lv_timer handling is suspended 
    :type en: bool

    :returns: 
    :rtype: None
    """
    ...


def timer_get_idle() -> int:
    """
    Get idle percentage the lv_timer idle in percentage 
    

    :returns: the lv_timer idle in percentage 
    :rtype: int
    """
    ...


def timer_get_time_until_next() -> int:
    """
    Get the time remaining until the next timer will run the time remaining in ms 
    

    :returns: the time remaining in ms 
    :rtype: int
    """
    ...


def trigo_sin(angle: int) -> int:
    """

    :returns: 
    :rtype: int
    """
    ...


def trigo_cos(angle: int) -> int:
    """

    :returns: 
    :rtype: int
    """
    ...


def cubic_bezier(x: int, x1: int, y1: int, x2: int, y2: int) -> int:
    """
    Calculate the y value of cubic-bezier(x1, y1, x2, y2) function as specified x. the value calculated 
    
    :param x: time in range of [0..LV_BEZIER_VAL_MAX] 
    :type x: int
    :param x1: x of control point 1 in range of [0..LV_BEZIER_VAL_MAX] 
    :type x1: int
    :param y1: y of control point 1 in range of [0..LV_BEZIER_VAL_MAX] 
    :type y1: int
    :param x2: x of control point 2 in range of [0..LV_BEZIER_VAL_MAX] 
    :type x2: int
    :param y2: y of control point 2 in range of [0..LV_BEZIER_VAL_MAX] 
    :type y2: int

    :returns: the value calculated 
    :rtype: int
    """
    ...


def bezier3(t: int, u0: int, u1: int, u2: int, u3: int) -> int:
    """
    Calculate a value of a Cubic Bezier function. the value calculated from the given parameters in range of [0..LV_BEZIER_VAL_MAX] 
    
    :param t: time in range of [0..LV_BEZIER_VAL_MAX] 
    :type t: int
    :param u0: must be 0 
    :type u0: int
    :param u1: control value 1 values in range of [0..LV_BEZIER_VAL_MAX] 
    :type u1: int
    :param u2: control value 2 in range of [0..LV_BEZIER_VAL_MAX] 
    :type u2: int
    :param u3: must be LV_BEZIER_VAL_MAX 
    :type u3: int

    :returns: the value calculated from the given parameters in range of [0..LV_BEZIER_VAL_MAX] 
    :rtype: int
    """
    ...


def atan2(x: int, y: int) -> int:
    """
    Calculate the atan2 of a vector. the angle in degree calculated from the given parameters in range of [0..360] 
    
    :param x: 
    :type x: int
    :param y: 
    :type y: int

    :returns: the angle in degree calculated from the given parameters in range of [0..360] 
    :rtype: int
    """
    ...


def sqrt(x: int, q: "sqrt_res_t", mask: int) -> None:
    """

    :returns: 
    :rtype: None
    """
    ...


def sqrt32(x: int) -> int:
    """
    Alternative (fast, approximate) implementation for getting the square root of an integer. 
    
    :param x: integer which square root should be calculated 
    :type x: int

    :returns: 
    :rtype: int
    """
    ...


def pow(base: int, exp: int) -> int:
    """
    Calculate the integer exponents. base raised to the power exponent 
    
    :param base: 
    :type base: int
    :param exp: 
    :type exp: int

    :returns: base raised to the power exponent 
    :rtype: int
    """
    ...


def map(x: int, x1: int, y1: int, x2: int, y2: int) -> int:
    """
    Get the mapped of a number given an input and output range the mapped number 
    
    :param x: integer which mapped value should be calculated 
    :type x: int
    :param x1: min input range 
    :type x1: int
    :param y1: max input range 
    :type y1: int
    :param x2: max output range 
    :type x2: int
    :param y2: max output range 
    :type y2: int

    :returns: the mapped number 
    :rtype: int
    """
    ...


def rand_set_seed(ms: int) -> None:
    """
    Set the seed of the pseudo random number generator 
    
    :param ms: a number to initialize the random generator 
    :type ms: int

    :returns: 
    :rtype: None
    """
    ...


def rand(min: int, max: int) -> int:
    """
    Get a pseudo random number in the given range return the random number. min <= return_value <= max 
    
    :param min: the minimum value 
    :type min: int
    :param max: the maximum value 
    :type max: int

    :returns: return the random number. min <= return_value <= max 
    :rtype: int
    """
    ...


def async_call(user_data: Any, async_xcb: Callable[[Any], None]) -> "result_t":
    """
    Call an asynchronous function the next time lv_timer_handler() is run. This function is likely to return before the call actually happens! 
    
    :param user_data: a callback which is the task itself. (the 'x' in the argument name indicates that it's not a fully generic function because it not follows the func_name(object, callback, ...) convention) 
    :type user_data: Any
    :param async_xcb: custom parameter 
    :type async_xcb: Callable[[Any], None]

    :returns: 
    :rtype: "result_t"
    """
    ...


def async_call_cancel(user_data: Any, async_xcb: Callable[[Any], None]) -> "result_t":
    """
    Cancel an asynchronous function call 
    
    :param user_data: a callback which is the task itself. 
    :type user_data: Any
    :param async_xcb: custom parameter 
    :type async_xcb: Callable[[Any], None]

    :returns: 
    :rtype: "result_t"
    """
    ...


def anim_delete(var: Any, exec_cb: "anim_exec_xcb_t") -> bool:
    """
    Delete animation(s) of a variable with a given animator function true: at least 1 animation is deleted, false: no animation is deleted 
    
    :param var: pointer to variable 
    :type var: Any
    :param exec_cb: a function pointer which is animating 'var', or NULL to ignore it and delete all the animations of 'var 
    :type exec_cb: "anim_exec_xcb_t"

    :returns: true: at least 1 animation is deleted, false: no animation is deleted 
    :rtype: bool
    """
    ...


def anim_delete_all() -> None:
    """
    Delete all the animations 
    

    :returns: 
    :rtype: None
    """
    ...


def anim_get(var: Any, exec_cb: "anim_exec_xcb_t") -> "anim_t":
    """
    Get the animation of a variable and its exec_cb . pointer to the animation. 
    
    :param var: pointer to variable 
    :type var: Any
    :param exec_cb: a function pointer which is animating 'var', or NULL to return first matching 'var' 
    :type exec_cb: "anim_exec_xcb_t"

    :returns: pointer to the animation. 
    :rtype: "anim_t"
    """
    ...


def anim_get_timer() -> "timer_t":
    """
    Get global animation refresher timer. pointer to the animation refresher timer. 
    

    :returns: pointer to the animation refresher timer. 
    :rtype: "timer_t"
    """
    ...


def anim_count_running() -> int:
    """
    Get the number of currently running animations the number of running animations 
    

    :returns: the number of running animations 
    :rtype: int
    """
    ...


def anim_speed(prev_tick: int) -> int:
    """
    Store the speed as a special value which can be used as time in animations. It will be converted to time internally based on the start and end values a special value which can be used as an animation time 
    
    :param prev_tick: the speed of the animation in with unit / sec resolution in 0..10k range 
    :type prev_tick: int

    :returns: a special value which can be used as an animation time 
    :rtype: int
    """
    ...


def anim_speed_clamped(speed: int, min_time: int, max_time: int) -> int:
    """
    Store the speed as a special value which can be used as time in animations. It will be converted to time internally based on the start and end values a special value in where all three values are stored and can be used as an animation time  internally speed is stored as 10 unit/sec  internally min/max_time are stored with 10 ms unit 
    
    :param speed: the speed of the animation in as unit / sec resolution in 0..10k range 
    :type speed: int
    :param min_time: the minimum time in 0..10k range 
    :type min_time: int
    :param max_time: the maximum time in 0..10k range 
    :type max_time: int

    :returns: a special value in where all three values are stored and can be used as an animation time 
    :rtype: int
    """
    ...


def anim_speed_to_time(speed: int, start: int, end: int) -> int:
    """
    Calculate the time of an animation based on its speed, start and end values. the time of the animation in milliseconds 
    
    :param speed: the speed of the animation 
    :type speed: int
    :param start: the start value 
    :type start: int
    :param end: the end value 
    :type end: int

    :returns: the time of the animation in milliseconds 
    :rtype: int
    """
    ...


def anim_refr_now() -> None:
    """
    Manually refresh the state of the animations. Useful to make the animations running in a blocking process where lv_timer_handler can't run for a while. Shouldn't be used directly because it is called in :ref:`lv_refr_now()` . 
    

    :returns: 
    :rtype: None
    """
    ...


def anim_timeline_create() -> "anim_timeline_t":
    """
    Create an animation timeline. pointer to the animation timeline. 
    

    :returns: pointer to the animation timeline. 
    :rtype: "anim_timeline_t"
    """
    ...


def pct(x: int) -> int:
    """
    Convert a percentage value to int32_t . Percentage values are stored in special range a coordinate that stores the percentage 
    
    :param x: the percentage (0..1000) 
    :type x: int

    :returns: a coordinate that stores the percentage 
    :rtype: int
    """
    ...


def pct_to_px(v: int, base: int) -> int:
    """
    :param v: 
    :type v: int
    :param base: 
    :type base: int

    :returns: 
    :rtype: int
    """
    ...


def color_format_get_bpp(cf: color_format_t) -> int:
    """
    Get the pixel size of a color format in bits, bpp the pixel size in bits  :ref:`LV_COLOR_FORMAT_GET_BPP` 
    
    :param cf: a color format ( LV_COLOR_FORMAT_... ) 
    :type cf: color_format_t

    :returns: the pixel size in bits 
    :rtype: int
    """
    ...


def color_format_get_size(cf: color_format_t) -> int:
    """
    Get the pixel size of a color format in bytes the pixel size in bytes  :ref:`LV_COLOR_FORMAT_GET_SIZE` 
    
    :param cf: a color format ( LV_COLOR_FORMAT_... ) 
    :type cf: color_format_t

    :returns: the pixel size in bytes 
    :rtype: int
    """
    ...


def color_format_has_alpha(src_cf: color_format_t) -> bool:
    """
    Check if a color format has alpha channel or not true: has alpha channel; false: doesn't have alpha channel 
    
    :param src_cf: a color format ( LV_COLOR_FORMAT_... ) 
    :type src_cf: color_format_t

    :returns: true: has alpha channel; false: doesn't have alpha channel 
    :rtype: bool
    """
    ...


def color_hex(c: int) -> "color_t":
    """
    Create a color from 0x000000..0xffffff input the color 
    
    :param c: the hex input 
    :type c: int

    :returns: the color 
    :rtype: "color_t"
    """
    ...


def color_make(r: int, g: int, b: int) -> "color_t":
    """
    Create an RGB888 color the color 
    
    :param r: the red channel (0..255) 
    :type r: int
    :param g: the green channel (0..255) 
    :type g: int
    :param b: the blue channel (0..255) 
    :type b: int

    :returns: the color 
    :rtype: "color_t"
    """
    ...


def color32_make(r: int, g: int, b: int, a: int) -> "color32_t":
    """
    Create an ARGB8888 color the color 
    
    :param r: the red channel (0..255) 
    :type r: int
    :param g: the green channel (0..255) 
    :type g: int
    :param b: the blue channel (0..255) 
    :type b: int
    :param a: the alpha channel (0..255) 
    :type a: int

    :returns: the color 
    :rtype: "color32_t"
    """
    ...


def color_hex3(c: int) -> "color_t":
    """
    Create a color from 0x000..0xfff input the color 
    
    :param c: the hex input (e.g. 0x123 will be 0x112233) 
    :type c: int

    :returns: the color 
    :rtype: "color_t"
    """
    ...


def color_16_16_mix(c1: int, c2: int, mix: int) -> int:
    """
    Mix two RGB565 colors mix == 0: c2 mix == 255: c1 mix == 128: 0.5 x c1 + 0.5 x c2 
    
    :param c1: the first color (typically the foreground color) 
    :type c1: int
    :param c2: the second color (typically the background color) 
    :type c2: int
    :param mix: 0..255, or LV_OPA_0/10/20... 
    :type mix: int

    :returns: mix == 0: c2 mix == 255: c1 mix == 128: 0.5 x c1 + 0.5 x c2 
    :rtype: int
    """
    ...


def color_hsv_to_rgb(h: int, s: int, v: int) -> "color_t":
    """
    Convert a HSV color to RGB the given RGB color in RGB (with LV_COLOR_DEPTH depth) 
    
    :param h: hue [0..359] 
    :type h: int
    :param s: saturation [0..100] 
    :type s: int
    :param v: value [0..100] 
    :type v: int

    :returns: the given RGB color in RGB (with LV_COLOR_DEPTH depth) 
    :rtype: "color_t"
    """
    ...


def color_rgb_to_hsv(r8: int, g8: int, b8: int) -> "color_hsv_t":
    """
    Convert a 32-bit RGB color to HSV the given RGB color in HSV 
    
    :param r8: 8-bit red 
    :type r8: int
    :param g8: 8-bit green 
    :type g8: int
    :param b8: 8-bit blue 
    :type b8: int

    :returns: the given RGB color in HSV 
    :rtype: "color_hsv_t"
    """
    ...


def color_white() -> "color_t":
    """
    A helper for white color a white color 
    

    :returns: a white color 
    :rtype: "color_t"
    """
    ...


def color_black() -> "color_t":
    """
    A helper for black color a black color 
    

    :returns: a black color 
    :rtype: "color_t"
    """
    ...


def color24_luminance(c: Union[str, List[int]]) -> int:
    """
    Get the luminance of a color24: luminance = 0.3 R + 0.59 G + 0.11 B the brightness [0..255] 
    
    :param c: a color 
    :type c: Union[str, List[int]]

    :returns: the brightness [0..255] 
    :rtype: int
    """
    ...


def palette_main(p: palette_t) -> "color_t":
    """
    :param p: 
    :type p: palette_t

    :returns: 
    :rtype: "color_t"
    """
    ...


def palette_lighten(p: palette_t, lvl: int) -> "color_t":
    """
    :param p: 
    :type p: palette_t
    :param lvl: 
    :type lvl: int

    :returns: 
    :rtype: "color_t"
    """
    ...


def palette_darken(p: palette_t, lvl: int) -> "color_t":
    """
    :param p: 
    :type p: palette_t
    :param lvl: 
    :type lvl: int

    :returns: 
    :rtype: "color_t"
    """
    ...


def draw_buf_get_handlers() -> "draw_buf_handlers_t":
    """
    Get the struct which holds the callbacks for draw buf management. Custom callback can be set on the returned value pointer to the struct of handlers 
    

    :returns: pointer to the struct of handlers 
    :rtype: "draw_buf_handlers_t"
    """
    ...


def draw_buf_get_font_handlers() -> "draw_buf_handlers_t":
    """

    :returns: 
    :rtype: "draw_buf_handlers_t"
    """
    ...


def draw_buf_get_image_handlers() -> "draw_buf_handlers_t":
    """

    :returns: 
    :rtype: "draw_buf_handlers_t"
    """
    ...


def draw_buf_align(buf: Any, color_format: color_format_t) -> Any:
    """
    Align the address of a buffer. The buffer needs to be large enough for the real data after alignment the aligned buffer 
    
    :param buf: the data to align 
    :type buf: Any
    :param color_format: the color format of the buffer 
    :type color_format: color_format_t

    :returns: the aligned buffer 
    :rtype: Any
    """
    ...


def draw_buf_width_to_stride(w: int, color_format: color_format_t) -> int:
    """
    Calculate the stride in bytes based on a width and color format the stride in bytes 
    
    :param w: the width in pixels 
    :type w: int
    :param color_format: the color format 
    :type color_format: color_format_t

    :returns: the stride in bytes 
    :rtype: int
    """
    ...


def draw_buf_create(w: int, h: int, cf: color_format_t, stride: int) -> "draw_buf_t":
    """
    Note: Eventually, lv_draw_buf_malloc/free will be kept as private. For now, we use create to distinguish with malloc. 
    
    Create an draw buf by allocating struct for :ref:`lv_draw_buf_t` and allocating a buffer for it that meets specified requirements.  
    
    :param w: the buffer width in pixels 
    :type w: int
    :param h: the buffer height in pixels 
    :type h: int
    :param cf: the color format for image 
    :type cf: color_format_t
    :param stride: the stride in bytes for image. Use 0 for automatic calculation based on w, cf, and global stride alignment configuration. 
    :type stride: int

    :returns: 
    :rtype: "draw_buf_t"
    """
    ...


def thread_init(user_data: Any, prio: thread_prio_t, callback: Callable[[Any], None], stack_size: int, thread: "thread_t") -> "result_t":
    """
    Create a new thread LV_RESULT_OK: success; LV_RESULT_INVALID: failure 
    
    :param user_data: a variable in which the thread will be stored 
    :type user_data: Any
    :param prio: priority of the thread 
    :type prio: thread_prio_t
    :param callback: function of the thread 
    :type callback: Callable[[Any], None]
    :param stack_size: stack size in bytes 
    :type stack_size: int
    :param thread: arbitrary data, will be available in the callback 
    :type thread: "thread_t"

    :returns: LV_RESULT_OK: success; LV_RESULT_INVALID: failure 
    :rtype: "result_t"
    """
    ...


def thread_delete(thread: "thread_t") -> "result_t":
    """
    Delete a thread LV_RESULT_OK: success; LV_RESULT_INVALID: failure 
    
    :param thread: the thread to delete 
    :type thread: "thread_t"

    :returns: LV_RESULT_OK: success; LV_RESULT_INVALID: failure 
    :rtype: "result_t"
    """
    ...


def mutex_init(mutex: "mutex_t") -> "result_t":
    """
    Create a mutex LV_RESULT_OK: success; LV_RESULT_INVALID: failure 
    
    :param mutex: a variable in which the thread will be stored 
    :type mutex: "mutex_t"

    :returns: LV_RESULT_OK: success; LV_RESULT_INVALID: failure 
    :rtype: "result_t"
    """
    ...


def mutex_lock(mutex: "mutex_t") -> "result_t":
    """
    Lock a mutex LV_RESULT_OK: success; LV_RESULT_INVALID: failure 
    
    :param mutex: the mutex to lock 
    :type mutex: "mutex_t"

    :returns: LV_RESULT_OK: success; LV_RESULT_INVALID: failure 
    :rtype: "result_t"
    """
    ...


def mutex_lock_isr(mutex: "mutex_t") -> "result_t":
    """
    Lock a mutex from interrupt LV_RESULT_OK: success; LV_RESULT_INVALID: failure 
    
    :param mutex: the mutex to lock 
    :type mutex: "mutex_t"

    :returns: LV_RESULT_OK: success; LV_RESULT_INVALID: failure 
    :rtype: "result_t"
    """
    ...


def mutex_unlock(mutex: "mutex_t") -> "result_t":
    """
    Unlock a mutex LV_RESULT_OK: success; LV_RESULT_INVALID: failure 
    
    :param mutex: the mutex to unlock 
    :type mutex: "mutex_t"

    :returns: LV_RESULT_OK: success; LV_RESULT_INVALID: failure 
    :rtype: "result_t"
    """
    ...


def mutex_delete(mutex: "mutex_t") -> "result_t":
    """
    Delete a mutex LV_RESULT_OK: success; LV_RESULT_INVALID: failure 
    
    :param mutex: the mutex to delete 
    :type mutex: "mutex_t"

    :returns: LV_RESULT_OK: success; LV_RESULT_INVALID: failure 
    :rtype: "result_t"
    """
    ...


def thread_sync_init(sync: "thread_sync_t") -> "result_t":
    """
    Create a thread synchronization object LV_RESULT_OK: success; LV_RESULT_INVALID: failure 
    
    :param sync: a variable in which the sync will be stored 
    :type sync: "thread_sync_t"

    :returns: LV_RESULT_OK: success; LV_RESULT_INVALID: failure 
    :rtype: "result_t"
    """
    ...


def thread_sync_wait(sync: "thread_sync_t") -> "result_t":
    """
    Wait for a "signal" on a sync object LV_RESULT_OK: success; LV_RESULT_INVALID: failure 
    
    :param sync: a sync object 
    :type sync: "thread_sync_t"

    :returns: LV_RESULT_OK: success; LV_RESULT_INVALID: failure 
    :rtype: "result_t"
    """
    ...


def thread_sync_signal(sync: "thread_sync_t") -> "result_t":
    """
    Send a wake-up signal to a sync object LV_RESULT_OK: success; LV_RESULT_INVALID: failure 
    
    :param sync: a sync object 
    :type sync: "thread_sync_t"

    :returns: LV_RESULT_OK: success; LV_RESULT_INVALID: failure 
    :rtype: "result_t"
    """
    ...


def thread_sync_signal_isr(sync: "thread_sync_t") -> "result_t":
    """
    Send a wake-up signal to a sync object from interrupt LV_RESULT_OK: success; LV_RESULT_INVALID: failure 
    
    :param sync: a sync object 
    :type sync: "thread_sync_t"

    :returns: LV_RESULT_OK: success; LV_RESULT_INVALID: failure 
    :rtype: "result_t"
    """
    ...


def thread_sync_delete(sync: "thread_sync_t") -> "result_t":
    """
    Delete a sync object LV_RESULT_OK: success; LV_RESULT_INVALID: failure 
    
    :param sync: a sync object to delete 
    :type sync: "thread_sync_t"

    :returns: LV_RESULT_OK: success; LV_RESULT_INVALID: failure 
    :rtype: "result_t"
    """
    ...


def lock() -> None:
    """
    Lock LVGL's general mutex. LVGL is not thread safe, so a mutex is used to avoid executing multiple LVGL functions at the same time from different threads. It shall be called when calling LVGL functions from threads different than lv_timer_handler's thread. It doesn't need to be called in LVGL events because they are called from lv_timer_handler(). It is called internally in lv_timer_handler(). 
    

    :returns: 
    :rtype: None
    """
    ...


def lock_isr() -> "result_t":
    """
    Same as :ref:`lv_lock()` but can be called from an interrupt. LV_RESULT_OK: success; LV_RESULT_INVALID: failure 
    

    :returns: LV_RESULT_OK: success; LV_RESULT_INVALID: failure 
    :rtype: "result_t"
    """
    ...


def unlock() -> None:
    """
    The pair of :ref:`lv_lock()` and :ref:`lv_lock_isr()` . It unlocks LVGL general mutex. It is called internally in lv_timer_handler(). 
    

    :returns: 
    :rtype: None
    """
    ...


def cache_entry_get_size(node_size: int) -> int:
    """
    Get the size of a cache entry. The size of the cache entry. 
    
    :param node_size: The size of the node in the cache. 
    :type node_size: int

    :returns: The size of the cache entry. 
    :rtype: int
    """
    ...


def cache_entry_get_ref(entry: "cache_entry_t") -> int:
    """
    Get the reference count of a cache entry. The reference count of the cache entry. 
    
    :param entry: The cache entry to get the reference count of. 
    :type entry: "cache_entry_t"

    :returns: The reference count of the cache entry. 
    :rtype: int
    """
    ...


def cache_entry_get_node_size(entry: "cache_entry_t") -> int:
    """
    Get the node size of a cache entry. Which is the same size with :ref:`lv_cache_entry_get_size()` 's node_size parameter. The node size of the cache entry. 
    
    :param entry: The cache entry to get the node size of. 
    :type entry: "cache_entry_t"

    :returns: The node size of the cache entry. 
    :rtype: int
    """
    ...


def cache_entry_is_invalid(entry: "cache_entry_t") -> bool:
    """
    Check if a cache entry is invalid. True: the cache entry is invalid. False: the cache entry is valid. 
    
    :param entry: The cache entry to check. 
    :type entry: "cache_entry_t"

    :returns: True: the cache entry is invalid. False: the cache entry is valid. 
    :rtype: bool
    """
    ...


def cache_entry_get_data(entry: "cache_entry_t") -> Any:
    """
    Get the data of a cache entry. The pointer to the data of the cache entry. 
    
    :param entry: The cache entry to get the data of. 
    :type entry: "cache_entry_t"

    :returns: The pointer to the data of the cache entry. 
    :rtype: Any
    """
    ...


def cache_entry_get_cache(entry: "cache_entry_t") -> "cache_t":
    """
    Get the cache instance of a cache entry. The pointer to the cache instance of the cache entry. 
    
    :param entry: The cache entry to get the cache instance of. 
    :type entry: "cache_entry_t"

    :returns: The pointer to the cache instance of the cache entry. 
    :rtype: "cache_t"
    """
    ...


def cache_entry_get_entry(data: Any, node_size: int) -> "cache_entry_t":
    """
    Get the cache entry of a data. The data should be allocated by the cache instance. The pointer to the cache entry of the data. 
    
    :param data: The data to get the cache entry of. 
    :type data: Any
    :param node_size: The size of the node in the cache. 
    :type node_size: int

    :returns: The pointer to the cache entry of the data. 
    :rtype: "cache_entry_t"
    """
    ...


def cache_entry_alloc(node_size: int, cache: "cache_t") -> "cache_entry_t":
    """
    Allocate a cache entry. The pointer to the allocated cache entry. 
    
    :param node_size: The size of the node in the cache. 
    :type node_size: int
    :param cache: The cache instance to allocate the cache entry from. 
    :type cache: "cache_t"

    :returns: The pointer to the allocated cache entry. 
    :rtype: "cache_entry_t"
    """
    ...


def cache_entry_init(entry: "cache_entry_t", cache: "cache_t", node_size: int) -> None:
    """
    Initialize a cache entry. 
    
    :param entry: The cache entry to initialize. 
    :type entry: "cache_entry_t"
    :param cache: The cache instance to allocate the cache entry from. 
    :type cache: "cache_t"
    :param node_size: The size of the node in the cache. 
    :type node_size: int

    :returns: 
    :rtype: None
    """
    ...


def cache_entry_delete(entry: "cache_entry_t") -> None:
    """
    Deallocate a cache entry. And the data of the cache entry will be freed. 
    
    :param entry: The cache entry to deallocate. 
    :type entry: "cache_entry_t"

    :returns: 
    :rtype: None
    """
    ...


def font_default() -> "font_t":
    """
    Just a wrapper around LV_FONT_DEFAULT because it might be more convenient to use a function in some cases pointer to LV_FONT_DEFAULT 
    

    :returns: pointer to LV_FONT_DEFAULT 
    :rtype: "font_t"
    """
    ...


def text_get_size(size_res: "point_t", text: str, font: "font_t", letter_space: int, line_space: int, max_width: int, flag: text_flag_t) -> None:
    """
    Get size of a text 
    
    :param size_res: pointer to a 'point_t' variable to store the result 
    :type size_res: "point_t"
    :param text: pointer to a text 
    :type text: str
    :param font: pointer to font of the text 
    :type font: "font_t"
    :param letter_space: letter space of the text 
    :type letter_space: int
    :param line_space: line space of the text 
    :type line_space: int
    :param max_width: max width of the text (break the lines to fit this size). Set COORD_MAX to avoid 
    :type max_width: int
    :param flag: settings for the text from :ref:`lv_text_flag_t` 
    :type flag: text_flag_t

    :returns: 
    :rtype: None
    """
    ...


def text_get_width(txt: str, length: int, font: "font_t", letter_space: int) -> int:
    """
    Give the length of a text with a given font length of a char_num long text 
    
    :param txt: a '\0' terminate string 
    :type txt: str
    :param length: length of 'txt' in byte count and not characters (Á is 1 character but 2 bytes in UTF-8) 
    :type length: int
    :param font: pointer to a font 
    :type font: "font_t"
    :param letter_space: letter space 
    :type letter_space: int

    :returns: length of a char_num long text 
    :rtype: int
    """
    ...


def layout_register(user_data: Any, cb: Callable[["obj", Any], None]) -> int:
    """
    Register a new layout the ID of the new layout 
    
    :param user_data: the layout update callback 
    :type user_data: Any
    :param cb: custom data that will be passed to cb 
    :type cb: Callable[["obj", Any], None]

    :returns: the ID of the new layout 
    :rtype: int
    """
    ...


def flex_init() -> None:
    """
    Initialize a flex layout to default values 
    

    :returns: 
    :rtype: None
    """
    ...


def grid_init() -> None:
    """

    :returns: 
    :rtype: None
    """
    ...


def grid_fr(x: int) -> int:
    """
    Just a wrapper to LV_GRID_FR for bindings. 
    
    :param x: 
    :type x: int

    :returns: 
    :rtype: int
    """
    ...


def style_register_prop(flag: int) -> "style_prop_t":
    """
    Register a new style property for custom usage a new property ID, or LV_STYLE_PROP_INV if there are no more available. Example: lv_style_prop_t MY_PROP; static inline void lv_style_set_my_prop(lv_style_t * style, lv_color_t value) {  lv_style_value_t v = {.color = value}; lv_style_set_prop(style, MY_PROP, v); }  ...  MY_PROP = lv_style_register_prop();  ...  lv_style_set_my_prop(&style1, lv_palette_main(LV_PALETTE_RED)); 
    
    :param flag: 
    :type flag: int

    :returns: a new property ID, or LV_STYLE_PROP_INV if there are no more available. Example:
    :rtype: "style_prop_t"
    """
    ...


def style_get_num_custom_props() -> "style_prop_t":
    """
    Get the number of custom properties that have been registered thus far. 
    

    :returns: 
    :rtype: "style_prop_t"
    """
    ...


def style_prop_get_default(prop: "style_prop_t") -> "style_value_t":
    """
    Get the default value of a property the default value 
    
    :param prop: the ID of a property 
    :type prop: "style_prop_t"

    :returns: the default value 
    :rtype: "style_value_t"
    """
    ...


def style_prop_lookup_flags(prop: "style_prop_t") -> int:
    """
    Get the flags of a built-in or custom property. 
    
    the flags of the property  
    
    :param prop: a style property 
    :type prop: "style_prop_t"

    :returns: the flags of the property 
    :rtype: int
    """
    ...


def event_send(list: "event_list_t", e: event_t, preprocess: bool) -> "result_t":
    """
    :param list: 
    :type list: "event_list_t"
    :param e: 
    :type e: event_t
    :param preprocess: 
    :type preprocess: bool

    :returns: 
    :rtype: "result_t"
    """
    ...


def event_add(user_data: Any, cb: Callable[["event_t"], None], filter: "event_code_t", list: "event_list_t") -> "event_dsc_t":
    """
    :param user_data: 
    :type user_data: Any
    :param cb: 
    :type cb: Callable[["event_t"], None]
    :param filter: 
    :type filter: "event_code_t"
    :param list: 
    :type list: "event_list_t"

    :returns: 
    :rtype: "event_dsc_t"
    """
    ...


def event_remove_dsc(list: "event_list_t", dsc: "event_dsc_t") -> bool:
    """
    :param list: 
    :type list: "event_list_t"
    :param dsc: 
    :type dsc: "event_dsc_t"

    :returns: 
    :rtype: bool
    """
    ...


def event_get_count(list: "event_list_t") -> int:
    """
    :param list: 
    :type list: "event_list_t"

    :returns: 
    :rtype: int
    """
    ...


def event_get_dsc(list: "event_list_t", index: int) -> "event_dsc_t":
    """
    :param list: 
    :type list: "event_list_t"
    :param index: 
    :type index: int

    :returns: 
    :rtype: "event_dsc_t"
    """
    ...


def event_remove(list: "event_list_t", index: int) -> bool:
    """
    :param list: 
    :type list: "event_list_t"
    :param index: 
    :type index: int

    :returns: 
    :rtype: bool
    """
    ...


def event_remove_all(list: "event_list_t") -> None:
    """
    :param list: 
    :type list: "event_list_t"

    :returns: 
    :rtype: None
    """
    ...


def event_register_id() -> int:
    """
    Register a new, custom event ID. It can be used the same way as e.g. LV_EVENT_CLICKED to send custom events the new event id Example: uint32_t LV_EVENT_MINE = 0; ...  e = lv_event_register_id();  ...  lv_obj_send_event(obj, LV_EVENT_MINE, &some_data); 
    

    :returns: the new event id Example:
    :rtype: int
    """
    ...


def fs_get_drv(letter: str) -> "fs_drv_t":
    """
    Give a pointer to a driver from its letter pointer to a driver or NULL if not found 
    
    :param letter: the driver letter 
    :type letter: str

    :returns: pointer to a driver or NULL if not found 
    :rtype: "fs_drv_t"
    """
    ...


def fs_is_ready(letter: str) -> bool:
    """
    Test if a drive is ready or not. If the ready function was not initialized true will be returned. true: drive is ready; false: drive is not ready 
    
    :param letter: letter of the drive 
    :type letter: str

    :returns: true: drive is ready; false: drive is not ready 
    :rtype: bool
    """
    ...


def fs_get_letters(buf: str) -> str:
    """
    Fill a buffer with the letters of existing drivers the buffer 
    
    :param buf: buffer to store the letters ('\0' added after the last letter) 
    :type buf: str

    :returns: the buffer 
    :rtype: str
    """
    ...


def fs_get_ext(fn: str) -> str:
    """
    Return with the extension of the filename pointer to the beginning extension or empty string if no extension 
    
    :param fn: string with a filename 
    :type fn: str

    :returns: pointer to the beginning extension or empty string if no extension 
    :rtype: str
    """
    ...


def fs_up(buf: str) -> str:
    """
    Step up one level the truncated file name 
    
    :param buf: pointer to a file name 
    :type buf: str

    :returns: the truncated file name 
    :rtype: str
    """
    ...


def fs_get_last(fn: str) -> str:
    """
    Get the last element of a path (e.g. U:/folder/file -> file) pointer to the beginning of the last element in the path 
    
    :param fn: pointer to a file name 
    :type fn: str

    :returns: pointer to the beginning of the last element in the path 
    :rtype: str
    """
    ...


def draw_init() -> None:
    """
    Used internally to initialize the drawing module 
    

    :returns: 
    :rtype: None
    """
    ...


def draw_deinit() -> None:
    """
    Deinitialize the drawing module 
    

    :returns: 
    :rtype: None
    """
    ...


def draw_create_unit(size: int) -> Any:
    """
    Allocate a new draw unit with the given size and appends it to the list of draw units 
    
    :param size: the size to allocate. E.g. sizeof(my_draw_unit_t) , where the first element of my_draw_unit_t is :ref:`lv_draw_unit_t` . 
    :type size: int

    :returns: 
    :rtype: Any
    """
    ...


def draw_add_task(layer: "layer_t", coords: "area_t") -> "draw_task_t":
    """
    Add an empty draw task to the draw task list of a layer. the created draw task which needs to be further configured e.g. by added a draw descriptor 
    
    :param layer: pointer to a layer 
    :type layer: "layer_t"
    :param coords: the coordinates of the draw task 
    :type coords: "area_t"

    :returns: the created draw task which needs to be further configured e.g. by added a draw descriptor 
    :rtype: "draw_task_t"
    """
    ...


def draw_finalize_task_creation(layer: "layer_t", t: "draw_task_t") -> None:
    """
    Needs to be called when a draw task is created and configured. It will send an event about the new draw task to the widget and assign it to a draw unit. 
    
    :param layer: pointer to a layer 
    :type layer: "layer_t"
    :param t: pointer to a draw task 
    :type t: "draw_task_t"

    :returns: 
    :rtype: None
    """
    ...


def draw_dispatch() -> None:
    """
    Try dispatching draw tasks to draw units 
    

    :returns: 
    :rtype: None
    """
    ...


def draw_dispatch_wait_for_request() -> None:
    """
    Wait for a new dispatch request. It's blocking if LV_USE_OS == 0 else it yields 
    

    :returns: 
    :rtype: None
    """
    ...


def draw_wait_for_finish() -> None:
    """
    Wait for draw finish in case of asynchronous task execution. If LV_USE_OS == 0 it just return. 
    

    :returns: 
    :rtype: None
    """
    ...


def draw_dispatch_request() -> None:
    """
    When a draw unit finished a draw task it needs to request dispatching to let LVGL assign a new draw task to it 
    

    :returns: 
    :rtype: None
    """
    ...


def draw_get_unit_count() -> int:
    """
    Get the total number of draw units. 
    

    :returns: 
    :rtype: int
    """
    ...


def draw_get_next_available_task(layer: "layer_t", t_prev: "draw_task_t", draw_unit_id: int) -> "draw_task_t":
    """
    Find and available draw task tan available draw task or NULL if there is no any 
    
    :param layer: the draw ctx to search in 
    :type layer: "layer_t"
    :param t_prev: continue searching from this task 
    :type t_prev: "draw_task_t"
    :param draw_unit_id: check the task where preferred_draw_unit_id equals this value or LV_DRAW_UNIT_NONE 
    :type draw_unit_id: int

    :returns: tan available draw task or NULL if there is no any 
    :rtype: "draw_task_t"
    """
    ...


def draw_layer_create(parent_layer: "layer_t", color_format: color_format_t, area: "area_t") -> "layer_t":
    """
    Create a new layer on a parent layer the new target_layer or NULL on error 
    
    :param parent_layer: the parent layer to which the layer will be merged when it's rendered 
    :type parent_layer: "layer_t"
    :param color_format: the color format of the layer 
    :type color_format: color_format_t
    :param area: the areas of the layer (absolute coordinates) 
    :type area: "area_t"

    :returns: the new target_layer or NULL on error 
    :rtype: "layer_t"
    """
    ...


def draw_layer_alloc_buf(layer: "layer_t") -> Any:
    """
    Try to allocate a buffer for the layer. pointer to the allocated aligned buffer or NULL on failure 
    
    :param layer: pointer to a layer 
    :type layer: "layer_t"

    :returns: pointer to the allocated aligned buffer or NULL on failure 
    :rtype: Any
    """
    ...


def draw_layer_go_to_xy(layer: "layer_t", x: int, y: int) -> Any:
    """
    Got to a pixel at X and Y coordinate on a layer buf offset to point to the given X and Y coordinate 
    
    :param layer: pointer to a layer 
    :type layer: "layer_t"
    :param x: the target X coordinate 
    :type x: int
    :param y: the target X coordinate 
    :type y: int

    :returns: buf offset to point to the given X and Y coordinate 
    :rtype: Any
    """
    ...


def display_create(hor_res: int, ver_res: int) -> "display_t":
    """
    Create a new display with the given resolution pointer to a display object or NULL on error 
    
    :param hor_res: horizontal resolution in pixels 
    :type hor_res: int
    :param ver_res: vertical resolution in pixels 
    :type ver_res: int

    :returns: pointer to a display object or NULL on error 
    :rtype: "display_t"
    """
    ...


def display_get_default() -> "display_t":
    """
    Get the default display pointer to the default display 
    

    :returns: pointer to the default display 
    :rtype: "display_t"
    """
    ...


def screen_load(scr: "obj") -> None:
    """
    Load a screen on the default display 
    
    :param scr: pointer to a screen 
    :type scr: "obj"

    :returns: 
    :rtype: None
    """
    ...


def screen_load_anim(scr: "obj", anim_type: "screen_load_anim_t", time: int, delay: int, auto_del: bool) -> None:
    """
    Switch screen with animation 
    
    :param scr: pointer to the new screen to load 
    :type scr: "obj"
    :param anim_type: type of the animation from lv_screen_load_anim_t , e.g. LV_SCR_LOAD_ANIM_MOVE_LEFT 
    :type anim_type: "screen_load_anim_t"
    :param time: time of the animation 
    :type time: int
    :param delay: delay before the transition 
    :type delay: int
    :param auto_del: true: automatically delete the old screen 
    :type auto_del: bool

    :returns: 
    :rtype: None
    """
    ...


def screen_active() -> "obj":
    """
    Get the active screen of the default display pointer to the active screen 
    

    :returns: pointer to the active screen 
    :rtype: "obj"
    """
    ...


def layer_top() -> "obj":
    """
    Get the top layer of the default display pointer to the top layer 
    

    :returns: pointer to the top layer 
    :rtype: "obj"
    """
    ...


def layer_sys() -> "obj":
    """
    Get the system layer of the default display pointer to the sys layer 
    

    :returns: pointer to the sys layer 
    :rtype: "obj"
    """
    ...


def layer_bottom() -> "obj":
    """
    Get the bottom layer of the default display pointer to the bottom layer 
    

    :returns: pointer to the bottom layer 
    :rtype: "obj"
    """
    ...


def dpx(x: int) -> int:
    """
    Scale the given number of pixels (a distance or size) relative to a 160 DPI display considering the DPI of the default display. It ensures that e.g. lv_dpx(100) will have the same physical size regardless to the DPI of the display. n x current_dpi/160 
    
    :param x: the number of pixels to scale 
    :type x: int

    :returns: n x current_dpi/160 
    :rtype: int
    """
    ...


def clamp_width(width: int, min_width: int, max_width: int, ref_width: int) -> int:
    """
    Clamp a width between min and max width. If the min/max width is in percentage value use the ref_width the clamped width 
    
    :param width: width to clamp 
    :type width: int
    :param min_width: the minimal width 
    :type min_width: int
    :param max_width: the maximal width 
    :type max_width: int
    :param ref_width: the reference width used when min/max width is in percentage 
    :type ref_width: int

    :returns: the clamped width 
    :rtype: int
    """
    ...


def clamp_height(width: int, min_width: int, max_width: int, ref_width: int) -> int:
    """
    Clamp a height between min and max height. If the min/max height is in percentage value use the ref_height the clamped height 
    
    :param width: height to clamp 
    :type width: int
    :param min_width: the minimal height 
    :type min_width: int
    :param max_width: the maximal height 
    :type max_width: int
    :param ref_width: the reference height used when min/max height is in percentage 
    :type ref_width: int

    :returns: the clamped height 
    :rtype: int
    """
    ...


def draw_rect(layer: "layer_t", dsc: "draw_rect_dsc_t", coords: "area_t") -> None:
    """
    The rectangle is a wrapper for fill, border, bg. image and box shadow. Internally fill, border, image and box shadow draw tasks will be created. 
    
    :param layer: pointer to a layer 
    :type layer: "layer_t"
    :param dsc: pointer to an initialized draw descriptor variable 
    :type dsc: "draw_rect_dsc_t"
    :param coords: the coordinates of the rectangle 
    :type coords: "area_t"

    :returns: 
    :rtype: None
    """
    ...


def draw_label(layer: "layer_t", dsc: "draw_label_dsc_t", coords: "area_t") -> None:
    """
    Crate a draw task to render a text 
    
    :param layer: pointer to a layer 
    :type layer: "layer_t"
    :param dsc: pointer to draw descriptor 
    :type dsc: "draw_label_dsc_t"
    :param coords: coordinates of the character 
    :type coords: "area_t"

    :returns: 
    :rtype: None
    """
    ...


def draw_character(layer: "layer_t", dsc: "draw_label_dsc_t", point: "point_t", unicode_letter: int) -> None:
    """
    Crate a draw task to render a single character 
    
    :param layer: pointer to a layer 
    :type layer: "layer_t"
    :param dsc: pointer to draw descriptor 
    :type dsc: "draw_label_dsc_t"
    :param point: position of the label 
    :type point: "point_t"
    :param unicode_letter: the letter to draw 
    :type unicode_letter: int

    :returns: 
    :rtype: None
    """
    ...


def draw_image(layer: "layer_t", dsc: "draw_image_dsc_t", coords: "area_t") -> None:
    """
    Create an image draw task coords can be small than the real image area (if only a part of the image is rendered) or can be larger (in case of tiled images). . 
    
    :param layer: pointer to a layer 
    :type layer: "layer_t"
    :param dsc: pointer to an initialized draw descriptor 
    :type dsc: "draw_image_dsc_t"
    :param coords: the coordinates of the image 
    :type coords: "area_t"

    :returns: 
    :rtype: None
    """
    ...


def draw_layer(layer: "layer_t", dsc: "draw_image_dsc_t", coords: "area_t") -> None:
    """
    Create a draw task to blend a layer to another layer coords can be small than the total widget area from which the layer is created (if only a part of the widget was rendered to a layer) 
    
    :param layer: pointer to a layer 
    :type layer: "layer_t"
    :param dsc: pointer to an initialized draw descriptor 
    :type dsc: "draw_image_dsc_t"
    :param coords: the coordinates of the layer. 
    :type coords: "area_t"

    :returns: 
    :rtype: None
    """
    ...


def draw_line(layer: "layer_t", dsc: "draw_line_dsc_t") -> None:
    """
    Create a line draw task 
    
    :param layer: pointer to a layer 
    :type layer: "layer_t"
    :param dsc: pointer to an initialized :ref:`lv_draw_line_dsc_t` variable 
    :type dsc: "draw_line_dsc_t"

    :returns: 
    :rtype: None
    """
    ...


def draw_arc(layer: "layer_t", dsc: "draw_arc_dsc_t") -> None:
    """
    Create an arc draw task. 
    
    :param layer: pointer to a layer 
    :type layer: "layer_t"
    :param dsc: pointer to an initialized draw descriptor variable 
    :type dsc: "draw_arc_dsc_t"

    :returns: 
    :rtype: None
    """
    ...


def draw_arc_get_area(x: int, y: int, radius: int, start_angle: "value_precise_t", end_angle: "value_precise_t", w: int, rounded: bool, area: "area_t") -> None:
    """
    Get an area the should be invalidated when the arcs angle changed between start_angle and end_ange 
    
    :param x: the x coordinate of the center of the arc 
    :type x: int
    :param y: the y coordinate of the center of the arc 
    :type y: int
    :param radius: the radius of the arc 
    :type radius: int
    :param start_angle: the start angle of the arc (0 deg on the bottom, 90 deg on the right) 
    :type start_angle: "value_precise_t"
    :param end_angle: the end angle of the arc 
    :type end_angle: "value_precise_t"
    :param w: width of the arc 
    :type w: int
    :param rounded: true: the arc is rounded 
    :type rounded: bool
    :param area: store the area to invalidate here 
    :type area: "area_t"

    :returns: 
    :rtype: None
    """
    ...


def group_create() -> "group_t":
    """
    Create a new object group pointer to the new object group 
    

    :returns: pointer to the new object group 
    :rtype: "group_t"
    """
    ...


def group_get_default() -> "group_t":
    """
    Get the default group pointer to the default group 
    

    :returns: pointer to the default group 
    :rtype: "group_t"
    """
    ...


def group_swap_obj(obj: "obj", parent: "obj") -> None:
    """
    Swap 2 object in a group. The object must be in the same group 
    
    :param obj: pointer to an object 
    :type obj: "obj"
    :param parent: pointer to another object 
    :type parent: "obj"

    :returns: 
    :rtype: None
    """
    ...


def group_remove_obj(obj: "obj") -> None:
    """
    Remove an object from its group 
    
    :param obj: pointer to an object to remove 
    :type obj: "obj"

    :returns: 
    :rtype: None
    """
    ...


def group_focus_obj(obj: "obj") -> None:
    """
    Focus on an object (defocus the current) 
    
    :param obj: pointer to an object to focus on 
    :type obj: "obj"

    :returns: 
    :rtype: None
    """
    ...


def group_get_count() -> int:
    """
    Get the number of groups number of groups 
    

    :returns: number of groups 
    :rtype: int
    """
    ...


def group_by_index(index: int) -> "group_t":
    """
    Get a group by its index pointer to the group 
    
    :param index: index of the group 
    :type index: int

    :returns: pointer to the group 
    :rtype: "group_t"
    """
    ...


def indev_create() -> "indev_t":
    """
    Create an indev Pointer to the created indev or NULL when allocation failed 
    

    :returns: Pointer to the created indev or NULL when allocation failed 
    :rtype: "indev_t"
    """
    ...


def indev_read_timer_cb(arg1: "timer_t") -> None:
    """
    Called periodically to read the input devices 
    
    :param arg1: pointer to a timer to read 
    :type arg1: "timer_t"

    :returns: 
    :rtype: None
    """
    ...


def indev_active() -> "indev_t":
    """
    Get the currently processed input device. Can be used in action functions too. pointer to the currently processed input device or NULL if no input device processing right now 
    

    :returns: pointer to the currently processed input device or NULL if no input device processing right now 
    :rtype: "indev_t"
    """
    ...


def indev_get_active_obj() -> "obj":
    """
    Gets a pointer to the currently active object in the currently processed input device. pointer to currently active object or NULL if no active object 
    

    :returns: pointer to currently active object or NULL if no active object 
    :rtype: "obj"
    """
    ...


def indev_search_obj(obj: "obj", point: "point_t") -> "obj":
    """
    Search the most top, clickable object by a point pointer to the found object or NULL if there was no suitable object 
    
    :param obj: pointer to a start object, typically the screen 
    :type obj: "obj"
    :param point: pointer to a point for searching the most top child 
    :type point: "point_t"

    :returns: pointer to the found object or NULL if there was no suitable object 
    :rtype: "obj"
    """
    ...


def objid_builtin_destroy() -> None:
    """

    :returns: 
    :rtype: None
    """
    ...


def refr_now(disp: "display_t") -> None:
    """
    Redraw the invalidated areas now. Normally the redrawing is periodically executed in lv_timer_handler but a long blocking process can prevent the call of lv_timer_handler . In this case if the GUI is updated in the process (e.g. progress bar) this function can be called when the screen should be updated. 
    
    :param disp: pointer to display to refresh. NULL to refresh all displays. 
    :type disp: "display_t"

    :returns: 
    :rtype: None
    """
    ...


def binfont_create(path: str) -> "font_t":
    """
    Loads a :ref:`lv_font_t` object from a binary font file pointer to font where to load 
    
    :param path: path to font file 
    :type path: str

    :returns: pointer to font where to load 
    :rtype: "font_t"
    """
    ...


def binfont_destroy(font: "font_t") -> None:
    """
    Frees the memory allocated by the :ref:`lv_binfont_create()` function 
    
    :param font: :ref:`lv_font_t` object created by the lv_binfont_create function 
    :type font: "font_t"

    :returns: 
    :rtype: None
    """
    ...


def span_stack_init() -> None:
    """

    :returns: 
    :rtype: None
    """
    ...


def span_stack_deinit() -> None:
    """

    :returns: 
    :rtype: None
    """
    ...


def snapshot_take(obj: "obj", cf: color_format_t) -> "draw_buf_t":
    """

    :returns: 
    :rtype: "draw_buf_t"
    """
    ...


def snapshot_create_draw_buf(obj: "obj", cf: color_format_t) -> "draw_buf_t":
    """

    :returns: 
    :rtype: "draw_buf_t"
    """
    ...


def snapshot_reshape_draw_buf(obj: "obj", draw_buf: "draw_buf_t") -> "result_t":
    """

    :returns: 
    :rtype: "result_t"
    """
    ...


def snapshot_take_to_draw_buf(obj: "obj", cf: color_format_t, draw_buf: "draw_buf_t") -> "result_t":
    """

    :returns: 
    :rtype: "result_t"
    """
    ...


def snapshot_free(dsc: "image") -> None:
    """

    :returns: 
    :rtype: None
    """
    ...


def snapshot_take_to_buf(obj: "obj", cf: color_format_t, dsc: "image", buf: Any, buf_size: int) -> "result_t":
    """

    :returns: 
    :rtype: "result_t"
    """
    ...


def gridnav_add(obj: "obj", ctrl: "gridnav_ctrl_t") -> None:
    """

    :returns: 
    :rtype: None
    """
    ...


def gridnav_remove(obj: "obj") -> None:
    """

    :returns: 
    :rtype: None
    """
    ...


def gridnav_set_focused(tv: "obj", tile_obj: "obj", anim_en: "anim_enable_t") -> None:
    """

    :returns: 
    :rtype: None
    """
    ...


def imgfont_create(user_data: Any, path_cb: Callable[["font_t", int, int, List[int], Any], Any], height: int) -> "font_t":
    """

    :returns: 
    :rtype: "font_t"
    """
    ...


def imgfont_destroy(font: "font_t") -> None:
    """

    :returns: 
    :rtype: None
    """
    ...


def bin_decoder_init() -> None:
    """
    Initialize the binary image decoder module 
    

    :returns: 
    :rtype: None
    """
    ...


def bin_decoder_info(decoder: "image", dsc: "image", header: "image") -> "result_t":
    """
    Get info about a lvgl binary image LV_RESULT_OK: the info is successfully stored in header ; LV_RESULT_INVALID: unknown format or other error. 
    
    :param decoder: the decoder where this function belongs 
    :type decoder: "image"
    :param dsc: image descriptor containing the source and type of the image and other info. 
    :type dsc: "image"
    :param header: store the image data here 
    :type header: "image"

    :returns: LV_RESULT_OK: the info is successfully stored in header ; LV_RESULT_INVALID: unknown format or other error. 
    :rtype: "result_t"
    """
    ...


def bin_decoder_get_area(decoder: "image", dsc: "image", full_area: "area_t", decoded_area: "area_t") -> "result_t":
    """
    :param decoder: 
    :type decoder: "image"
    :param dsc: 
    :type dsc: "image"
    :param full_area: 
    :type full_area: "area_t"
    :param decoded_area: 
    :type decoded_area: "area_t"

    :returns: 
    :rtype: "result_t"
    """
    ...


def bin_decoder_open(decoder: "image", dsc: "image") -> "result_t":
    """
    Open a lvgl binary image LV_RESULT_OK: the info is successfully stored in header ; LV_RESULT_INVALID: unknown format or other error. 
    
    :param decoder: the decoder where this function belongs 
    :type decoder: "image"
    :param dsc: pointer to decoder descriptor. src , style are already initialized in it. 
    :type dsc: "image"

    :returns: LV_RESULT_OK: the info is successfully stored in header ; LV_RESULT_INVALID: unknown format or other error. 
    :rtype: "result_t"
    """
    ...


def bin_decoder_close(decoder: "image", dsc: "image") -> None:
    """
    Close the pending decoding. Free resources etc. 
    
    :param decoder: pointer to the decoder the function associated with 
    :type decoder: "image"
    :param dsc: pointer to decoder descriptor 
    :type dsc: "image"

    :returns: 
    :rtype: None
    """
    ...


def bmp_init() -> None:
    """

    :returns: 
    :rtype: None
    """
    ...


def bmp_deinit() -> None:
    """

    :returns: 
    :rtype: None
    """
    ...


def lodepng_init() -> None:
    """

    :returns: 
    :rtype: None
    """
    ...


def lodepng_deinit() -> None:
    """

    :returns: 
    :rtype: None
    """
    ...


def tjpgd_init() -> None:
    """

    :returns: 
    :rtype: None
    """
    ...


def tjpgd_deinit() -> None:
    """

    :returns: 
    :rtype: None
    """
    ...


def draw_triangle(layer: "layer_t", draw_dsc: "draw_triangle_dsc_t") -> None:
    """
    Create a triangle draw task 
    
    :param layer: pointer to a layer 
    :type layer: "layer_t"
    :param draw_dsc: pointer to an initialized :ref:`lv_draw_triangle_dsc_t` object 
    :type draw_dsc: "draw_triangle_dsc_t"

    :returns: 
    :rtype: None
    """
    ...


def draw_sw_init() -> None:
    """
    Initialize the SW renderer. Called in internally. It creates as many SW renderers as defined in LV_DRAW_SW_DRAW_UNIT_CNT 
    

    :returns: 
    :rtype: None
    """
    ...


def draw_sw_deinit() -> None:
    """
    Deinitialize the SW renderers 
    

    :returns: 
    :rtype: None
    """
    ...


def draw_sw_rgb565_swap(buf: Any, buf_size_px: int) -> None:
    """
    Swap the upper and lower byte of an RGB565 buffer. Might be required if a 8bit parallel port or an SPI port send the bytes in the wrong order. The bytes will be swapped in place. 
    
    :param buf: pointer to buffer 
    :type buf: Any
    :param buf_size_px: number of pixels in the buffer 
    :type buf_size_px: int

    :returns: 
    :rtype: None
    """
    ...


def draw_sw_i1_invert(buf: Any, buf_size_px: int) -> None:
    """
    Invert a draw buffer in the I1 color format. Conventionally, a bit is set to 1 during blending if the luminance is greater than 127. Depending on the display controller used, you might want to have different behavior. The inversion will be performed in place. 
    
    :param buf: pointer to the buffer to be inverted 
    :type buf: Any
    :param buf_size_px: size of the buffer in bytes 
    :type buf_size_px: int

    :returns: 
    :rtype: None
    """
    ...


def draw_sw_rotate(src: Any, dest: Any, src_width: int, src_height: int, src_stride: int, dest_stride: int, rotation: display_rotation_t, color_format: color_format_t) -> None:
    """
    Rotate a buffer into another buffer 
    
    :param src: the source buffer 
    :type src: Any
    :param dest: the destination buffer 
    :type dest: Any
    :param src_width: source width in pixels 
    :type src_width: int
    :param src_height: source height in pixels 
    :type src_height: int
    :param src_stride: source stride in bytes (number of bytes in a row) 
    :type src_stride: int
    :param dest_stride: destination stride in bytes (number of bytes in a row) 
    :type dest_stride: int
    :param rotation: LV_DISPLAY_ROTATION_0/90/180/270 
    :type rotation: display_rotation_t
    :param color_format: LV_COLOR_FORMAT_RGB565/RGB888/XRGB8888/ARGB8888 
    :type color_format: color_format_t

    :returns: 
    :rtype: None
    """
    ...


def draw_sw_mask_init() -> None:
    """

    :returns: 
    :rtype: None
    """
    ...


def draw_sw_mask_deinit() -> None:
    """

    :returns: 
    :rtype: None
    """
    ...


def draw_sw_mask_apply(masks: Any, mask_buf: opa_t, abs_x: int, abs_y: int, len: int) -> "draw_sw_mask_res_t":
    """

    :returns: 
    :rtype: "draw_sw_mask_res_t"
    """
    ...


def draw_sw_mask_free_param(data: Any) -> None:
    """
    Free the data from the parameter. It's called inside lv_draw_sw_mask_remove_id and lv_draw_sw_mask_remove_custom Needs to be called only in special cases when the mask is not added by lv_draw_mask_add and not removed by lv_draw_mask_remove_id or lv_draw_mask_remove_custom 
    
    :param data: pointer to a mask parameter 
    :type data: Any

    :returns: 
    :rtype: None
    """
    ...


def theme_get_from_obj(obj: "obj") -> "theme_t":
    """
    Get the theme assigned to the display of the object the theme of the object's display (can be NULL) 
    
    :param obj: pointer to a theme object 
    :type obj: "obj"

    :returns: the theme of the object's display (can be NULL) 
    :rtype: "theme_t"
    """
    ...


def theme_apply(obj: "obj") -> None:
    """
    Apply the active theme on an object 
    
    :param obj: pointer to an object 
    :type obj: "obj"

    :returns: 
    :rtype: None
    """
    ...


def theme_get_font_small(obj: "obj") -> "font_t":
    """
    Get the small font of the theme pointer to the font 
    
    :param obj: pointer to an object 
    :type obj: "obj"

    :returns: pointer to the font 
    :rtype: "font_t"
    """
    ...


def theme_get_font_normal(obj: "obj") -> "font_t":
    """
    Get the normal font of the theme pointer to the font 
    
    :param obj: pointer to an object 
    :type obj: "obj"

    :returns: pointer to the font 
    :rtype: "font_t"
    """
    ...


def theme_get_font_large(obj: "obj") -> "font_t":
    """
    Get the subtitle font of the theme pointer to the font 
    
    :param obj: pointer to an object 
    :type obj: "obj"

    :returns: pointer to the font 
    :rtype: "font_t"
    """
    ...


def theme_get_color_primary(obj: "obj") -> "color_t":
    """
    Get the primary color of the theme the color 
    
    :param obj: pointer to an object 
    :type obj: "obj"

    :returns: the color 
    :rtype: "color_t"
    """
    ...


def theme_get_color_secondary(obj: "obj") -> "color_t":
    """
    Get the secondary color of the theme the color 
    
    :param obj: pointer to an object 
    :type obj: "obj"

    :returns: the color 
    :rtype: "color_t"
    """
    ...


def theme_default_init(disp: "display_t", color_primary: "color_t", color_secondary: "color_t", dark: bool, font: "font_t") -> "theme_t":
    """
    Initialize the theme a pointer to reference this theme later 
    
    :param disp: pointer to display 
    :type disp: "display_t"
    :param color_primary: the primary color of the theme 
    :type color_primary: "color_t"
    :param color_secondary: the secondary color for the theme 
    :type color_secondary: "color_t"
    :param dark: 
    :type dark: bool
    :param font: pointer to a font to use. 
    :type font: "font_t"

    :returns: a pointer to reference this theme later 
    :rtype: "theme_t"
    """
    ...


def theme_default_get() -> "theme_t":
    """
    Get default theme a pointer to default theme, or NULL if this is not initialized 
    

    :returns: a pointer to default theme, or NULL if this is not initialized 
    :rtype: "theme_t"
    """
    ...


def theme_default_is_inited() -> bool:
    """
    Check if default theme is initialized true if default theme is initialized, false otherwise 
    

    :returns: true if default theme is initialized, false otherwise 
    :rtype: bool
    """
    ...


def theme_default_deinit() -> None:
    """
    Deinitialize the default theme 
    

    :returns: 
    :rtype: None
    """
    ...


def theme_simple_init(disp: "display_t") -> "theme_t":
    """
    Initialize the theme a pointer to reference this theme later 
    
    :param disp: pointer to display to attach the theme 
    :type disp: "display_t"

    :returns: a pointer to reference this theme later 
    :rtype: "theme_t"
    """
    ...


def theme_simple_is_inited() -> bool:
    """
    Check if the theme is initialized true if default theme is initialized, false otherwise 
    

    :returns: true if default theme is initialized, false otherwise 
    :rtype: bool
    """
    ...


def theme_simple_get() -> "theme_t":
    """
    Get simple theme a pointer to simple theme, or NULL if this is not initialized 
    

    :returns: a pointer to simple theme, or NULL if this is not initialized 
    :rtype: "theme_t"
    """
    ...


def theme_simple_deinit() -> None:
    """
    Deinitialize the simple theme 
    

    :returns: 
    :rtype: None
    """
    ...

