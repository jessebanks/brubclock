import time
import sys
from subprocess import Popen, call
from brubclock_ui import Ui_MainWindow
from PySide.QtGui import *
from PySide.QtCore import *

class BrubMainWindow(QMainWindow):

    def __init__(self, parent=None):

        QMainWindow.__init__(self, parent)

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.timer = QTimer(self)
        self.timer.timeout.connect(self.second)
        self.timer.start(1000)

    @Slot()
    def second(self):
        current = time.localtime()

        broob, broobz = broobhour(current.tm_hour)

        clockstring = "{0:02}:{1:02} {2}".format(broob,
                                          current.tm_min,
                                          broobz)

        self.ui.clock.setText(clockstring)

        if current.tm_sec == 0 and (current.tm_min == 30 or
                                    current.tm_min == 0):
            speak(broob, current.tm_min, broobz)



def speak(hour, min, broobz):

    call(["play", "brubeep.mp3"])

    if broobz == "PB":
        speech = "it is now {0} hours {1} minutes post broobs".format(hour, min)
    else:
        speech = "it is now {0} hours and {1} minutes ante broobs".format(hour, min)


    command = ["espeak", "-s", "150", "\"" + speech + "\""]
    print command
    Popen(command)


def broobhour(hour):

    if hour >= 10 and hour <= 16:
        broob = 16 - hour
        broobz = "AB"

    elif hour < 10: 
        broob = hour + 9
        broobz = "PB"

    elif hour > 16:
        broob = hour - 16
        broobz = "PB"

    return broob, broobz


if __name__ == "__main__":
    app = QApplication(sys.argv)

    mainWindow = BrubMainWindow()
    mainWindow.show()
    sys.exit(app.exec_())
