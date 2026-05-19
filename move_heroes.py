#!/usr/bin/env python3
"""Move and Rename Files with shutil"""

import shutil  # For moving and renaming files
import os  # For directory operations

def main():
    """Main logic"""
    # Ensure the script starts in the correct directory
    os.chdir("/home/student/JPcode/")

    # Move Raynor to battlecruiser
    if os.path.exists("battlecruiser/raynor.obj"):
        ans = input("raynor.obj already exists in battlecruiser. Do you want to overwrite? (y/n)")
        if ans == "y":
            shutil.move("battlecruiser/raynor.obj", "battlecruiser/raynor.obj")
        elif ans == "n":
            print("not moving file")
        else:
            print("error. How are we here?")
    else:
        shutil.move("raynor.obj", "battlecruiser/")

    # Prompt for Kerrigan's new name
    # xname = input("What is the new name for kerrigan.obj? ")

    # Rename Kerrigan
    # shutil.move("battlecruiser/kerrigan.obj", f"battlecruiser/{xname}")

main()

