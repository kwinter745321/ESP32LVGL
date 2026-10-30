import gc
start=gc.mem_free()
print(f"Starting heap:{start}")
import lvgl as lv
end=gc.mem_free()
print(f"After LV import:{end} Difference:{start-end}")
print(f"Using LVGL {lv.version_major()}.{lv.version_minor()}")