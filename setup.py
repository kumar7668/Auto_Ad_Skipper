from cx_Freeze import setup, Executable
import sys

# Dependencies are automatically detected, but it might need fine tuning.
build_exe_options = {"packages": ["selenium"], "excludes": []}

base = None
if sys.platform == "win32":
    base = "Win32GUI"

setup(  name = "YoutubeAdSkipper",
        version = "1.0",
        description = "Skip YouTube ads automatically",
        options = {"build_exe": build_exe_options},
        executables = [Executable("youtube_ad_skipper.py", base=base)])
