"""
==========================================
Buddy v1.0
File: apps/browser.py

Purpose:
    Launch Chrome, websites, Google search
    and YouTube.
==========================================
"""

import subprocess
import urllib.parse

from config import CHROME_PATH, CHROME_PROFILE


class BrowserApps:

    def __init__(self):

        self.urls = {
            "google": "https://www.google.com",
            "youtube": "https://www.youtube.com",
            "gmail": "https://mail.google.com",
            "github": "https://github.com",
            "gemini": "https://gemini.google.com",
        }

        self.domain_extensions = (
            ".com",
            ".org",
            ".net",
            ".io",
            ".dev",
            ".ai",
            ".co",
            ".edu",
            ".gov",
            ".in",
            ".app",
            ".xyz",
        )

    # =====================================
    # Internal
    # =====================================

    def open_url(self, url):

        try:

            subprocess.Popen([
                CHROME_PATH,
                f"--profile-directory={CHROME_PROFILE}",
                url
            ])

            return True

        except Exception as e:

            print(f"Browser Error: {e}")
            return False

    # =====================================
    # Open
    # =====================================

    def open(self, command):

        target = command.replace("open", "", 1).strip().lower()

        # Open only Chrome
        if target == "chrome":

            try:

                subprocess.Popen([
                    CHROME_PATH,
                    f"--profile-directory={CHROME_PROFILE}"
                ])

                return True

            except Exception as e:

                print(e)
                return False

        # Predefined websites
        if target in self.urls:

            return self.open_url(self.urls[target])

        # Domain
        if any(target.endswith(ext) for ext in self.domain_extensions):

            return self.open_url("https://" + target)

        # Otherwise Google search
        url = (
            "https://www.google.com/search?q="
            + urllib.parse.quote(target)
        )

        return self.open_url(url)

    # =====================================
    # Google Search
    # =====================================

    def search(self, command):

        query = command.replace("search", "", 1).strip()

        url = (
            "https://www.google.com/search?q="
            + urllib.parse.quote(query)
        )

        return self.open_url(url)

    # =====================================
    # YouTube
    # =====================================

    def play(self, command):

        song = command.replace("play", "", 1).strip()

        url = (
            "https://www.youtube.com/results?search_query="
            + urllib.parse.quote(song)
        )

        return self.open_url(url)


browser = BrowserApps()