# dll_example
A simple example of using Python with a "dynamic-link library" (DLL) or ".dll" file
- Sometimes we want to interact with a .dll file using Python (for example in the context of controlling hardware), but this can be confusing (especially if the hardware is complex, or the library is extensive and has a rich architecture).
- Here the "MathLibrary.dll" is a simple library for returning the 'Fibonacci numbers', so no hardware is needed. It can also be generated or modified following the contents of the "make_dll" folder.
- The "dll_example.py" then shows how to make calls to the .dll (with the correct formatting for arguments and return values etc) with minimal complications.
