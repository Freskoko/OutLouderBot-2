import sys
from PyQt6.QtWidgets import QApplication, QWidget, QLineEdit, QPushButton, QTextEdit, QVBoxLayout, QHBoxLayout, QProgressBar
from PyQt6.QtGui import QIcon
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from mainfuncVaskReal import UpvoteSong
from addToList import AddToTxt


vaskeriet = "https://outloud.dj/5n4p8"
test_site = "https://outloud.dj/vbmzb"

#INSTALLATIONS REQUIRED  
# pip install selenium
# pip install pyqt6

# Links to DJ rooms for easy access
vaskeriet = "https://outloud.dj/5n4p8"
test_site = "https://outloud.dj/vbmzb"


urltogoto = vaskeriet


#the function uses "urltogoto", it makes easier to change between 
# vaskeriet and test site up here rather than line 93

# UpvoteSong() will log in to the URL specified, and vote for
# the first result that comes up when searching for the given song.

#--------------------




class MyApp(QWidget):
    #make the app like make it exist
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Outlouder")
        #self.setWindowIcon(QIcon("tf2 1.png"))
        
        #make a layout
        layout = QVBoxLayout()
        layoutHoz = QHBoxLayout()
        layoutHoz2 = QHBoxLayout()

        #widgets
        #the two input fields
        self.inputField1 = QLineEdit("add to txt")
        self.inputField1.setFixedSize(400, 50)

        self.inputField2 = QLineEdit("votes")
        self.inputField2.setFixedSize(150, 50)

        #progress bar
        steps = 10
        self.progressBar = QProgressBar()
        self.progressBar.setRange(0,steps)

        
        #output text (where text goes)
        self.output= QTextEdit("Message field")
        self.output.setReadOnly(True)
    
        #buttons activate progress bar and activate the browser

        self.buttonMult = QPushButton("Start!")

        #give the button functions

        self.buttonMult.clicked.connect(lambda:self.startingText())
        self.buttonMult.clicked.connect(self.startUpvoting)
        self.buttonMult.clicked.connect(lambda status, n_size = steps: self.run(n_size))
        
        #add to text file
        self.buttonAddToTxt = QPushButton("Add song", clicked = self.WriteToSongFile)
        
        #exit button
        self.buttonBye = QPushButton("Exit program", clicked = self.done)

        #SET SIZES
        self.resize(400,200)
        self.buttonMult.setFixedSize(100, 50)
        self.output.setFixedSize(400, 50)
        self.inputField1.setFixedSize(300, 50)
        self.inputField2.setFixedSize(300, 50)
        self.progressBar.setFixedSize(400, 50)
        self.buttonBye.setFixedSize(400, 50)
        self.buttonAddToTxt.setFixedSize(100, 50)
        
        #we have multiple layers so add a hoz layer and hozlayer2 here
    
        layout.addLayout(layoutHoz2)
        layout.addLayout(layoutHoz)
       

        #add the widgets to the layout

        layoutHoz2.addWidget(self.buttonMult)
        layoutHoz2.addWidget(self.inputField2)
        
        layoutHoz.addWidget(self.buttonAddToTxt)
        layoutHoz.addWidget(self.inputField1)

        layout.addWidget(self.output)

        layout.addWidget(self.buttonBye)
        #layout.addWidget(self.progressBar)
        

        #set layout
        self.setLayout(layout)

    #functions for the buttons
 
    #runs progress bar
    def run(self, steps):
        for i in range(steps):
            time.sleep(0.1)
            self.progressBar.setValue(i+1)

    def WriteToSongFile(self):
        inputText1 = (self.inputField1.text())
        AddToTxt(inputText1)
    
    #runs the upvote song from mainfuncVaskReal.py
    def startUpvoting(self):
        try:
            #set text here to tell user upvote started
            self.progressBar.setValue(0)


            inputText2 = int(self.inputField2.text())

            time.sleep(1)

            #def UpvoteSong(url, votes,DownVoting):
            # UpvoteSong(song, URL, inputText2)
            UpvoteSong(urltogoto, inputText2, DownVoting=False) ### here the magic happens
            self.output.setText("Upvoting Completed!")

        except ValueError: #(string where there should be int)
            self.output.setText("Please input numbers in text field 2")
            pass

    # yes this is fuckign stupid i have to make a fucntion for this
    # but i have to set lamdba function thing so this is the best way to do it
    def startingText(self):
        self.output.setText("Upvoting Started")

    #exits app
    def done(self):
        sys.exit(app.exec())


#CSS style text sheet which creates good looking page (font size etc)
app = QApplication(sys.argv)
app.setStyleSheet('''
    QWidget {
        font-size: 25px;
        }

    QPushButton{
        font-size: 20px;
        }
    
    QTextedit{
        font-size: 200px;
        }

    QProgressBar {
        border: 2px solid #2196F3;
        border-radius: 5px;
        background-color: #F44336;
    }

''')

window = MyApp()
window.show()

app.exec()
