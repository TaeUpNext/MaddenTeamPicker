# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/Volumes/Buffalo_SSD/Programming/Python/Madden Team Picker/MaddenTeamPicker.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.

import random 


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(842, 578)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.afc_Button = QtWidgets.QPushButton(self.centralwidget)
        self.afc_Button.setGeometry(QtCore.QRect(40, 380, 241, 91))
        font = QtGui.QFont()
        font.setFamily("Starboard DEMO")
        font.setPointSize(36)
        font.setItalic(False)
        self.afc_Button.setFont(font)
        self.afc_Button.setObjectName("afc_Button")
        self.random_Button = QtWidgets.QPushButton(self.centralwidget)
        self.random_Button.setGeometry(QtCore.QRect(300, 380, 241, 91))
        font = QtGui.QFont()
        font.setFamily("Starboard DEMO")
        font.setPointSize(36)
        self.random_Button.setFont(font)
        self.random_Button.setObjectName("random_Button")
        self.nfc_Button = QtWidgets.QPushButton(self.centralwidget)
        self.nfc_Button.setGeometry(QtCore.QRect(570, 380, 241, 91))
        font = QtGui.QFont()
        font.setFamily("Starboard DEMO")
        font.setPointSize(36)
        self.nfc_Button.setFont(font)
        self.nfc_Button.setObjectName("nfc_Button")
        self.teamLabel = QtWidgets.QLabel(self.centralwidget)
        self.teamLabel.setGeometry(QtCore.QRect(110, 150, 571, 141))
        font = QtGui.QFont()
        font.setFamily("Starboard DEMO")
        font.setPointSize(36)
        font.setBold(False)
        font.setItalic(True)
        font.setWeight(50)
        self.teamLabel.setFont(font)
        self.teamLabel.setAutoFillBackground(True)
        self.teamLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.teamLabel.setObjectName("teamLabel")
        self.intoLabel = QtWidgets.QLabel(self.centralwidget)
        self.intoLabel.setGeometry(QtCore.QRect(70, 30, 671, 71))
        font = QtGui.QFont()
        font.setFamily("Starboard DEMO")
        font.setPointSize(48)
        self.intoLabel.setFont(font)
        self.intoLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.intoLabel.setObjectName("intoLabel")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 842, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        
        #event creation
        self.afc_Button.clicked.connect(self.pick_AFC)
        self.nfc_Button.clicked.connect(self.pick_NFC)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        
        

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.afc_Button.setText(_translate("MainWindow", "AFC Team"))
        self.random_Button.setText(_translate("MainWindow", "Random Team"))
        self.nfc_Button.setText(_translate("MainWindow", "NFC Team"))
        self.teamLabel.setText(_translate("MainWindow", "<html><head/><body><p><br/></p></body></html>"))
        self.intoLabel.setText(_translate("MainWindow", "The Team You Will Use IS The"))
        
    def pick_AFC(self):
        pafc = randomTeamPicker()
        pafc.pickAFC()
        
    def pick_NFC(self):
        pnfc = randomTeamPicker()
        pnfc.pickNFC()
    


class randomTeamPicker():
    global teams_AFC, teams_NFC
    teams_AFC = [ "Baltimore Ravens",    "Buffalo Bills",    "Cincinnati Bengals",    "Cleveland Browns",    "Denver Broncos",    "Houston Texans",    "Indianapolis Colts",  "Jacksonville Jaguars", "Kansas City Chiefs",    "Las Vegas Raiders",    "Los Angeles Chargers",    "Miami Dolphins",    "New England Patriots",    "New York Jets",   "Pittsburgh Steelers", "Tennessee Titans"] #list consisitng of the teams in the AFC
    
    teams_NFC = [ "Arizona Cardinals",    "Atlanta Falcons",    "Carolina Panthers",    "Chicago Bears",    "Dallas Cowboys",    "Detroit Lions",    "Green Bay Packers",    "Los Angeles Rams",    "Minnesota Vikings",    "New Orleans Saints",    "New York Giants",    "Philadelphia Eagles",    "San Francisco 49ers",    "Seattle Seahawks",    "Tampa Bay Buccaneers",    "Washington Football Team"] #list of NFL teams in the NFC
    
    
    def pickAFC(self):
        random.shuffle(teams_AFC)
        random_Team = random.choice(teams_AFC)
        teams_AFC.remove(random_Team)
        ui.teamLabel.setText(random_Team)
    
    def pickNFC(self):
        random.shuffle(teams_NFC)
        random_Team = random.choice(teams_NFC)
        teams_NFC.remove(random_Team)
        ui.teamLabel.setText(random_Team)
    
    

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())