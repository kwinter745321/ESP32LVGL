# test_memory.py
import gc
import micropython

def show():
    gc.collect()
    f = gc.mem_free()
    a = gc.mem_alloc()
    t = f + a
    s = micropython.stack_use()
    tot = f"Total: {t/(1024*1024):.2f} M"
    alc = f"Alloc: {a/1024:.2f} K"
    fre = f"Free:  {f/(1024*1024):.2f} M  ({f/t*100:.2f} %)"
    stk = f"Stack: {s/1024:.2f} K"
    print(tot)
    print(alc)
    print(fre)
    print(stk)

show()