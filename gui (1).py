# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'gui.ui'
#
# Created by: PyQt5 UI code generator 5.5.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
import sys
import random
import time
localScore = 0
cnt = 0
org = []
jum = []

class Ui_Game(object):
	def __init__(self,parent=None):
			super(Ui_Game,self).__init__()
			global org, jum
			i=0
			a = ['sherlock', 'threshold', 'fame', 'friends', 'office', 'flash', 'Lost', 'bigbang', 'dexter', 'suits', 'madmen', 'breathe','atlanta','StrangerThings','haunting','homecoming','maniac','westworld','queereye','BigMouth','pose','AmericanVandal','JessicaJones','arrow','counterpart','WalkingDead','hatim','pokemon','ninja','doremon']
			while(i<10): 
				pick = random.choice(a)
				if pick not in org:
					org.append(pick)
					i+=1
			for i in range(len(org)):
				l_word = random.sample(org[i],len(org[i]))
				jumbled = ''.join(l_word)
				jum.append(jumbled)

	def setupUi(self, Game):
		Game.setObjectName("Game")
		Game.resize(565, 287)
		self.Heading = QtWidgets.QLabel(Game)
		self.Heading.setGeometry(QtCore.QRect(190, 20, 181, 51))
		self.Heading.setStyleSheet("font: 75 14pt \"Ubuntu\";")
		self.Heading.setObjectName("Heading")
		self.Score = QtWidgets.QLabel(Game)
		self.Score.setGeometry(QtCore.QRect(220, 190, 131, 17))
		self.Score.setObjectName("Score")
		self.label_4 = QtWidgets.QLabel(Game)
		self.label_4.setGeometry(QtCore.QRect(20, 110, 111, 71))
		self.label_4.setObjectName("label_4")
		self.label_5 = QtWidgets.QLabel(Game)
		self.label_5.setGeometry(QtCore.QRect(20, 90, 111, 17))
		self.label_5.setObjectName("label_5")
		self.jum_word = QtWidgets.QLabel(Game)
		self.jum_word.setGeometry(QtCore.QRect(160, 90, 151, 17))
		self.jum_word.setObjectName("jum_word")
		self.submit = QtWidgets.QPushButton(Game)
		self.submit.setGeometry(QtCore.QRect(400, 130, 81, 27))
		self.submit.setObjectName("submit")
		self.plainTextEdit = QtWidgets.QPlainTextEdit(Game)
		self.plainTextEdit.setGeometry(QtCore.QRect(160, 130, 221, 31))
		self.plainTextEdit.setObjectName("plainTextEdit")

		self.retranslateUi(Game)
		QtCore.QMetaObject.connectSlotsByName(Game)

		self.retranslateUi(Game)
		QtCore.QMetaObject.connectSlotsByName(Game)

		self.submit.clicked.connect(self.myfunc)

	def retranslateUi(self, Game):
		global jum
		_translate = QtCore.QCoreApplication.translate
		Game.setWindowTitle(_translate("Game", "Game"))
		self.Heading.setText(_translate("Game", "Jumble Word Game"))
		self.Score.setText(_translate("Game", ""))
		self.label_4.setText(_translate("Game", "Original Word : "))
		self.label_5.setText(_translate("Game", "Jumbled Word :"))
		self.jum_word.setText(_translate("Game", "Null"))
		self.submit.setText(_translate("Game", "Submit"))
		self.jum_word.setText(jum[0])

	def myfunc(self):
		global cnt, jum, org, localScore
		data = self.plainTextEdit.toPlainText()
		if(data==org[cnt]):
			localScore+=1
		cnt+=1
		if(cnt!=10):
			self.jum_word.setText(jum[cnt])
			self.plainTextEdit.setPlainText("")
		else:
			self.Score.setText("Your Score is " + str(localScore))
			#time.sleep(5)
			#sys.exit()


app = QtWidgets.QApplication(sys.argv)
MainWindow = QtWidgets.QMainWindow()
ui = Ui_Game()
ui.setupUi(MainWindow)
MainWindow.show()
sys.exit(app.exec_())
