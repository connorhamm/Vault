"""
Logic:
1. Create a timer
2. Add in a note system that is shared with phone

"""
import vlc
import webbrowser
import subprocess
import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import pyqtSlot

class App(QWidget):

    def __init__(self):
        super().__init__()
        self.title = 'The Vault'
        self.left = 10
        self.top = 10
        self.width = 320
        self.height = 200
        self.initUI()

    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)

        # Brilliant Button
        button = QPushButton('Brilliant', self)
        button.setToolTip('This is an example button')
        button.move(0, 70)
        button.clicked.connect(self.on_click_1)

        # Udacity Button
        button2 = QPushButton('Udacity', self)
        button2.setToolTip('This is an example button')
        button2.move(100, 70)
        button2.clicked.connect(self.on_click_2)

        # Udemy Button
        button3 = QPushButton('Udemy', self)
        button3.setToolTip('This is an example button')
        button3.move(200, 70)
        button3.clicked.connect(self.on_click_3)

        # Anki Button
        button4 = QPushButton('Anki', self)
        button4.setToolTip('This is an example button')
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
        button5.setToolTip('This is an example button')
        button5.move(200, 140)
        button5.clicked.connect(self.on_click_5)

        # Evernote Button
        button6 = QPushButton('Evernote', self)
        button6.setToolTip('This is an example button')
        button6.move(0, 0)
        button6.clicked.connect(self.on_click_6)

        # Social Media Button
        button7 = QPushButton('Social Media', self)
        button7.setToolTip('This is an example button')
        button7.move(0, 140)
        button7.clicked.connect(self.on_click_7)

        # Spotify
        button8 = QPushButton('Spotify', self)
        button8.setToolTip('This is an example button')
        button8.move(100, 140)
        button8.clicked.connect(self.on_click_8)

        # Financial Information
        button9 = QPushButton('Financial Info', self)
        button9.setToolTip('This is an example button')
        button9.move(100, 0)
        button9.clicked.connect(self.on_click_9)

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
        webbrowser.open_new("https://web.whatsapp.com/")
        webbrowser.open_new("https://messages.android.com/")
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

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())
