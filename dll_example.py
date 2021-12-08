import os
import ctypes as C

os.add_dll_directory(os.getcwd()) # must add cwd or DLL not found
# (PATH and cwd are no longer auto searched during C.cdll.LoadLibrary)

dll = C.cdll.LoadLibrary("MathLibrary") # load DLL (64bit Python -> 64bit DLL)

# pick through docs (or header (.h) and source code (.cpp) files) to find DLL
# calls. Find out what they do and then format arguments and return values
# using correct 'ctypes' data type:

dll.fibonacci_init.argtypes = [C.c_ulonglong, C.c_ulonglong] # init with f0, f1 
dll.fibonacci_init.restype = None

dll.get_fn = dll.fibonacci_current # optional renaming
dll.get_fn.argtypes = None
dll.get_fn.restype = C.c_ulonglong # current value in sequence

dll.get_n = dll.fibonacci_index # optional renaming
dll.get_n.argtypes = None
dll.get_n.restype = C.c_uint # current index in sequence

dll.fibonacci_next.argtypes = None
dll.fibonacci_next.restype = C.c_bool # checks overflow and returns bool

def dll_fibonacci_number(f0, f1, n):
    dll.fibonacci_init(f0, f1) # mandatory call, arguments formated by .argtypes
    for i in range(n):
        fn = dll.get_fn() # returns formated by .restype
        n  = dll.get_n()
        overflow_ok = dll.fibonacci_next()
        print('dll_Fn:%21i (n:%2i, overflow_ok: %s)'%(fn, n, overflow_ok))
        if not overflow_ok: break
    return None

n = 10
f0, f1 = 0, 1
dll_fibonacci_number(f0, f1, n)

### compare to python:
##def python_fibonacci_number(f0, f1, n):
##    fn_minus_2 = f0
##    fn_minus_1 = f1
##    for i in range(n):
##        if i == 0:
##            fn = f0
##        if i == 1:
##            fn = f1
##        if i > 1:
##            fn = fn_minus_1 + fn_minus_2
##            fn_minus_2 = fn_minus_1
##            fn_minus_1 = fn
##        print('pyt_Fn:%21i (n:%2i)'%(fn, i))
##    return None
##
##python_fibonacci_number(f0, f1, n)
