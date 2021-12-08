# Make the simple "MathLibrary.dll":
- Navigate to p301 in "C_and_C++_projects_and_build_systems_in_Visual_Studio.pdf"
- Follow tutorial: "Walkthrough: Create and use your own Dynamic Link Library (C++)"
- Note: this requires an install of Microsoft Visual Studio & dependencies to run:
	- C++ core desktop features
	- MSVC v143 - VS 2022 C++ x64/x86 build tools
	- Windows 10 SDK (10.0.19041.0))
	- more? or updated versions?
- Stop at p310 ("Create a client app that uses the DLL")
- This produce the directory "MathLibrary" and contents (many files and folders), including:
	- MathLibrary.h
	- MathLibrary.cpp
	- MathLibrary.dll
- It's kind of a mess but this seems typical when dealing with .dll's (i.e. finding and picking through
the header file (.h) and source code file (.cpp) may be needed to run the .dll)