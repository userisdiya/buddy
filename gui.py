"""
==========================================
Buddy v1.0
File: gui.py
Purpose:
    Main GUI of the Buddy Desktop Assistant.
==========================================
"""

from PySide6.QtCore import Qt
from PySide6.QtGui import QFont
from PySide6.QtWidgets import (
    QMainWindow,
    QWidget,
    QLabel,
    QPushButton,
    QTextEdit,
    QVBoxLayout,
    QHBoxLayout,
)

from config import (
    WINDOW_TITLE,
    WINDOW_WIDTH,
    WINDOW_HEIGHT,
    PRIMARY_COLOR,
    SECONDARY_COLOR,
    BUTTON_COLOR,
    BUTTON_HOVER,
    TEXT_COLOR,
    SUBTEXT_COLOR,
    STATUS_READY,
    DEFAULT_FONT,
    DEFAULT_FONT_SIZE,
    CHAT_FONT_SIZE,
)


class BuddyWindow(QMainWindow):
    """
    Main Buddy Window
    """

    def __init__(self):
        super().__init__()

        self.setWindowTitle(WINDOW_TITLE)
        self.setFixedSize(WINDOW_WIDTH, WINDOW_HEIGHT)

        self.setup_ui()

    def setup_ui(self):

        # ============================
        # Central Widget
        # ============================

        central_widget = QWidget()
        self.setCentralWidget(central_widget)

        # ============================
        # Main Layout
        # ============================

        main_layout = QVBoxLayout()
        main_layout.setContentsMargins(20, 20, 20, 20)
        main_layout.setSpacing(18)

        # ============================
        # Title
        # ============================

        self.title = QLabel("🤖 Buddy")

        self.title.setAlignment(Qt.AlignCenter)

        self.title.setFont(QFont(DEFAULT_FONT, 22, QFont.Bold))

        self.title.setStyleSheet(f"""
            color:{TEXT_COLOR};
        """)

        main_layout.addWidget(self.title)

        # ============================
        # Status
        # ============================

        self.status = QLabel(STATUS_READY)

        self.status.setAlignment(Qt.AlignCenter)

        self.status.setFont(QFont(DEFAULT_FONT, 12))

        self.status.setStyleSheet(f"""
            color:{SUBTEXT_COLOR};
        """)

        main_layout.addWidget(self.status)

        # ============================
        # Conversation
        # ============================

        self.chat_box = QTextEdit()

        self.chat_box.setReadOnly(True)

        self.chat_box.setFont(QFont(DEFAULT_FONT, CHAT_FONT_SIZE))

        self.chat_box.setPlainText("")

        self.chat_box.setStyleSheet(f"""
            QTextEdit {{
                background:{SECONDARY_COLOR};
                color:{TEXT_COLOR};
                border-radius:12px;
                padding:12px;
                border:none;
            }}
        """)

        main_layout.addWidget(self.chat_box)

        # ============================
        # Buttons
        # ============================

        button_layout = QHBoxLayout()

        self.history_button = QPushButton("History")

        self.exit_button = QPushButton("Exit")

        button_style = f"""
        QPushButton {{
            background:{BUTTON_COLOR};
            color:white;
            border:none;
            padding:10px;
            border-radius:8px;
            font-size:12px;
        }}

        QPushButton:hover {{
            background:{BUTTON_HOVER};
        }}
        """

        self.history_button.setStyleSheet(button_style)
        self.exit_button.setStyleSheet(button_style)

        self.exit_button.clicked.connect(self.close)

        button_layout.addWidget(self.history_button)
        button_layout.addStretch()
        button_layout.addWidget(self.exit_button)

        main_layout.addLayout(button_layout)

        # ============================
        # Apply Layout
        # ============================

        central_widget.setLayout(main_layout)

        # ============================
        # Window Style
        # ============================

        self.setStyleSheet(f"""
            QMainWindow {{
                background:{PRIMARY_COLOR};
            }}
        """)

    # ===================================
    # Helper Functions
    # ===================================

    def set_status(self, text):
        self.status.setText(text)

    def add_message(self, speaker, message):
        self.chat_box.append(f"\n<b>{speaker}</b>\n{message}\n")

    def set_listening(self):
        self.set_status("🎤 Listening...")

    def set_thinking(self):
        self.set_status("🧠 Thinking...")

    def set_speaking(self):
        self.set_status("🗣 Speaking...")

    def set_ready(self):
        self.set_status("Ready")