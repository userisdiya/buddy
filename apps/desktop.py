"""
==========================================
Buddy v1.0
File: apps/desktop.py

Purpose:
    Launch desktop applications.
==========================================
"""

import subprocess

from config import BLENDER_PATH, VSCODE_PATH


class DesktopApps:

    def open_blender(self):

        try:
            subprocess.Popen([BLENDER_PATH])
            return True

        except Exception as e:
            print(f"Blender Error: {e}")
            return False

    def open_vscode(self):

        try:
            subprocess.Popen([VSCODE_PATH])
            return True

        except Exception as e:
            print(f"VS Code Error: {e}")
            return False

    def open_file_explorer(self):

        try:
            subprocess.Popen(["explorer"])
            return True

        except Exception as e:
            print(f"Explorer Error: {e}")
            return False

    def open_calculator(self):

        try:
            subprocess.Popen(["calc"])
            return True

        except Exception as e:
            print(f"Calculator Error: {e}")
            return False

    def execute(self, command):

        command = command.lower().strip()

        if command == "open blender":
            return self.open_blender()

        elif command in ["open vscode", "open vs code"]:
            return self.open_vscode()

        elif command == "open file explorer":
            return self.open_file_explorer()

        elif command == "open calculator":
            return self.open_calculator()

        return False


desktop = DesktopApps()