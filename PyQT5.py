"""
Logic:
-1. Create current program into a more modular design
0. Make executeable - done with the use of anaconda for package dependencies
1. Create prompt for asking you what you need, and do you need to really get this?
2, Create a button for routines

# Perhaps add in android emulator for bumble / hinge

"""
import vlc
import webbrowser
import subprocess
import sys
import os

from PyQt5.QtWidgets import QMainWindow, QApplication, QWidget, QPushButton, QAction, QLineEdit, QMessageBox
from PyQt5.QtCore import pyqtSlot
from PyQt5.QtGui import QIcon

class App(QWidget):

    def __init__(self):
        super().__init__()
        self.title = 'The Vault'
        self.left = 10
        self.top = 10
        self.width = 281
        self.height = 400
        self.initUI()

    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)

        # Brilliant Button
        button = QPushButton('Brilliant', self)
        button.move(0, 70)
        button.clicked.connect(self.on_click_1)

        # Udacity Button
        button2 = QPushButton('Udacity', self)
        button2.move(100, 70)
        button2.clicked.connect(self.on_click_2)

        # Udemy Button
        button3 = QPushButton('Udemy', self)
        button3.move(200, 70)
        button3.clicked.connect(self.on_click_3)

        # Anki Button
        button4 = QPushButton('Anki', self)
        button4.move(200, 0)
        button4.clicked.connect(self.on_click_4)

        # Rain
        """
        Logic:
        1. add button press counter
        2. switch if statement to check
        3. turn off or on based on counter
        """
        button5 = QPushButton('Rain.mp3', self)
        button5.move(200, 140)
        button5.clicked.connect(self.on_click_5)

        # Evernote Button
        button6 = QPushButton('Evernote', self)
        button6.move(0, 0)
        button6.clicked.connect(self.on_click_6)

        # Social Serious
        button7 = QPushButton('Social Work', self)
        button7.move(0, 140)
        button7.clicked.connect(self.on_click_7)

        # Spotify
        button8 = QPushButton('Spotify', self)
        button8.move(100, 140)
        button8.clicked.connect(self.on_click_8)

        # Financial Information
        button9 = QPushButton('Financial Info', self)
        button9.move(100, 0)
        button9.clicked.connect(self.on_click_9)

        # Amazon
        button10 = QPushButton('Amazon', self)
        button10.move(200, 210)
        button10.clicked.connect(self.on_click_10)

        # Debug
        button11 = QPushButton('Debug', self)
        button11.move(100, 210)
        button11.clicked.connect(self.on_click_11)

        # Wolfram Alpha
        button12 = QPushButton('Wolfram Alpha', self)
        button12.move(0, 210)
        button12.clicked.connect(self.on_click_12)

        # Netflix
        # Prompt User to Set a timer for how long they spend on it?
        button13 = QPushButton('Netflix', self)
        button13.move(100, 210)
        button13.clicked.connect(self.on_click_13)

        # Pomodoro Timer
        button14 = QPushButton('Timer', self)
        button14.move(0, 280)
        button14.clicked.connect(self.on_click_14)

        # Routine & Rules
        button15 = QPushButton('Routine/Rules', self)
        button15.move(100, 280)
        button15.clicked.connect(self.on_click_15)


        # Social X
        button16 = QPushButton('Messaging', self)
        button16.move(200, 280)
        button16.clicked.connect(self.on_click_16)

        self.show()

    @pyqtSlot()
    def on_click_1(self):
        webbrowser.open_new("https://www.brilliant.org")

    def on_click_2(self):
        webbrowser.open_new("https://www.udacity.com")

    def on_click_3(self):
        webbrowser.open_new("https://www.udemy.com")

    def on_click_4(self):
        command = 'anki'
        process = subprocess.Popen(command.split(), stdout=subprocess.PIPE)
        # output, error = process.communicate()

    def on_click_5(self):
        p = vlc.MediaPlayer("/home/connor/Desktop/rain.mp3")
        p.play()

    def on_click_6(self):
        webbrowser.open_new("https://evernote.com/")

    def on_click_7(self):
        webbrowser.open_new("https://www.gmail.com/")
        webbrowser.open_new("https://jabil.okta.com/")

    def on_click_8(self):
        command = 'spotify'
        process = subprocess.Popen(command.split(), stdout=subprocess.PIPE)
        # output, error = process.communicate()

    def on_click_9(self):
        webbrowser.open_new("https://www.uasecho.com/Account/SignIn")
        webbrowser.open_new("https://www.allstate.com/auto-insurance.aspx")
        webbrowser.open_new("https://www.starone.org/")

    def on_click_10(self):
        print("textbox")
        # Textbox Generation

        # Create a conditional website open
        webbrowser.open_new("https://www.amazon.com")

    def on_click_11(self):
        webbrowser.open_new("https://www.stackoverflow.com")
        webbrowser.open_new("https://www.python.org")
        webbrowser.open_new("https://www.wikipedia.org")
        webbrowser.open_new("https://examine.com/")

    def on_click_12(self):
        webbrowser.open_new("https://www.wolframalpha.com/")

    def on_click_13(self):
        webbrowser.open_new("https://www.netflix.com")

    def on_click_14(self):
        print("test")
        os.chdir("/home/connor/thomas")
        command = 'npm start'
        process = subprocess.Popen(command.split(), stdout=subprocess.PIPE)

    def on_click_15(self):
        routine = open("/home/connor/Desktop/Routine", "r")
        routine.seek(0)
        print(routine.read())
        routine.close()

        rules = open("/home/connor/Desktop/Rules", "r")
        rules.seek(0)
        print(rules.read())
        rules.close()

    def on_click_16(self):
        webbrowser.open_new("https://www.tinder.com")
        webbrowser.open_new("https://web.whatsapp.com")
        webbrowser.open_new("https://messages.android.com/")


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())
