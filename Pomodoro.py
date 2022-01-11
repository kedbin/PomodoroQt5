#!/usr/bin/python3
import os
from PyQt5.QtWidgets import QApplication, QLabel, QVBoxLayout, QWidget, QPushButton, QGridLayout
from PyQt5.QtGui import QFont
from PyQt5.QtCore import QTime, QTimer, Qt

class AppDemo(QWidget):
    def __init__(self):
        super().__init__()
        self.resize(450,150)
        self.setWindowTitle("Kedbin's Pomodoro App")

        self.counter = 0

        self.startBtn=QPushButton('Start')
        self.endBtn=QPushButton('Stop')
        self.breakBtn=QPushButton('Break')

        self.layout = QGridLayout()

        fnt = QFont('Helvetica', 120)

        self.lbl = QLabel()
        self.lbl.setFont(fnt)
        self.lbl.setAlignment(Qt.AlignCenter)

        self.layout.addWidget(self.lbl,0,0,1,2)
        self.layout.addWidget(self.startBtn,1,0)
        self.layout.addWidget(self.endBtn,1,1)
        
        self.setLayout(self.layout)

        self.timer = QTimer()
        self.timer.timeout.connect(self.displayTime)

        self.startBtn.clicked.connect(self.startTimer)
        self.endBtn.clicked.connect(self.endTimer)
        self.breakBtn.clicked.connect(self.breakTimer)

    def displayTime(self):
        if self.pomodoro == 0:
            self.lbl.setText("Time's Up!")
            os.system("vlc ./kubo8.mp4 > /dev/null 2>&1 &")
            self.layout.addWidget(self.breakBtn,2,0,1,2)
            self.startBtn.setEnabled(True)
            self.breakBtn.setEnabled(True)
            self.timer.stop()
            return
        mins = int(self.pomodoro // 60)
        sec = int(self.pomodoro % 60)

        displayText = f"{mins}:{sec}"

        self.lbl.setText(displayText)

        self.pomodoro -=1
    
    def startTimer(self):
        self.pomodoro = 0.1*60
        self.timer.start(1000)
        self.startBtn.setEnabled(False)
        self.endBtn.setEnabled(True)
        self.breakBtn.setEnabled(False)
        self.counter += 1

    def endTimer(self):
        self.timer.stop()
        self.startBtn.setEnabled(True)
        self.endBtn.setEnabled(False)

    def breakTimer(self):
        if self.counter > 0 and self.counter % 4 == 0:
            self.pomodoro = 30*60
        else:
            self.pomodoro = 0.15*60
        self.timer.start(1000)
        self.startBtn.setEnabled(False)
        self.breakBtn.setEnabled(False)



app = QApplication([])
demo = AppDemo()
demo.show()

app.exec_()