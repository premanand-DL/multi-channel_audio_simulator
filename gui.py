import sys
from PyQt5.QtWidgets import QDialog, QApplication, QPushButton, QVBoxLayout,QMainWindow

from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.backends.backend_qt5agg import NavigationToolbar2QT as NavigationToolbar
import matplotlib.pyplot as plt
from matplotlib.figure import Figure
import random
import random


# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'gui.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
import numpy as np


class Ui_d_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(455, 900)
        global no_chn,no_spk,T60,fs,center,types,room,angles,pos,reflec,dim
        m = PlotCanvas(MainWindow, width=4.5, height=3)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(50, 350, 251, 311))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setSizeConstraint(QtWidgets.QLayout.SetFixedSize)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.room = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(13)
        self.room.setFont(font)
        self.room.setText("Room")
        self.room.setText(self.room.text() + '::                     '+room[0])
        self.type_arr = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(13)
        self.type_arr.setFont(font)
        self.type_arr.setText("Array Type")
        self.type_arr.setText(self.type_arr.text() + '::             '+types[0])
        self.no_chn = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(13)
        self.no_chn.setFont(font)
        self.no_chn.setText("No. of Channels")
        self.no_chn.setText(self.no_chn.text() + ':      '+str(no_chn))
        self.center = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(13)
        self.center.setFont(font)
        self.center.setText("Array Location")
        self.center.setText(self.center.text() + '::       '+str(center[0]))
        self.no_spk = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(13)
        self.no_spk.setFont(font)
        self.no_spk.setText("No. of Speakers")
        self.no_spk.setText(self.no_spk.text() + '::     '+ str(no_spk))
        self.pos = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(13)
        self.pos.setFont(font)
        self.pos.setText("Spk. Locations")
        self.pos.setText(self.pos.text() + '::       '+ str(pos))
        self.fs = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(13)
        self.fs.setFont(font)
        self.fs.setText("Sampling Freq")
        self.fs.setText(self.fs.text() + '::      '+str(fs[0][0]))
        self.t60 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(13)
        self.t60.setFont(font)
        self.t60.setText("T60")
        self.t60.setText(self.t60.text() + '::                       '+str(T60[0][0]))
        self.reflec = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(13)
        self.reflec.setFont(font)
        self.reflec.setText("Reflection Coeff")
        self.reflec.setText(self.reflec.text() + '::   '+str(reflec[0][0]))
        self.angles = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(13)
        self.angles.setFont(font)
        self.angles.setText("Angles") 
        self.angles.setText(self.angles.text() + ':                   '+str(angles))
        self.tdoa = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(13)
        self.tdoa.setFont(font)
        self.tdoa.setText("TDOAs")
        self.tdoa.setText(self.tdoa.text() + '::                   '+'[5, 3]')
        self.verticalLayout.addWidget(self.room)
        self.verticalLayout.addWidget(self.type_arr)
        self.verticalLayout.addWidget(self.no_chn)
        self.verticalLayout.addWidget(self.center)
        self.verticalLayout.addWidget(self.no_spk)
        self.verticalLayout.addWidget(self.pos)
        self.verticalLayout.addWidget(self.fs)
        self.verticalLayout.addWidget(self.t60)
        self.verticalLayout.addWidget(self.reflec)
        self.verticalLayout.addWidget(self.angles)
        self.verticalLayout.addWidget(self.tdoa)
        #self.graphicsView = QtWidgets.QGraphicsView(self.centralwidget)
        #self.graphicsView.setGeometry(QtCore.QRect(50, 0, 251, 192))
        #self.graphicsView.setObjectName("graphicsView")
        #scene = QtWidgets.QGraphicsScene()
        #self.scene = scene
        #self.scene.addWidget(m)
        #self.graphicsView.setScene(scene)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 335, 22))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        
    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))

class PlotCanvas(FigureCanvas):

    def __init__(self, parent=None, width=10, height=8, dpi=100):
        fig = Figure(figsize=(width, height), dpi=dpi)
        self.axes = fig.add_subplot(111)
    

        FigureCanvas.__init__(self, fig)
        self.setParent(parent)
        #self.addWidget(toolbar)


        
        FigureCanvas.updateGeometry(self)
        self.plot()
    def plot(self):
        #data = [random.random() for i in range(250)]
        global no_chn,no_spk,T60,fs,center,types,room,angles,pos,reflec,dim
        ax = self.figure.add_subplot(111)
        data = np.array([2,1.5])
        for i in range(no_spk):
            ax.scatter(pos[i,0],pos[i,1],color='green')
            ax.text(pos[i,0]+0.05,pos[i,1]+0.05,'S'+str(i+1),fontsize=9)
        ax.scatter(float(center[0][0]),float(center[0][1]),color='red')
        #print(dim)
        ax.text(center[0][0]+0.05,center[0][1]+0.05,types[0]+' Array',fontsize=10)
        ax.set_title('Room Configuration')
        ax.set_yticks([])
        ax.set_xticks([])
        ax.set_xlim([0,dim[0][0]])
        ax.set_ylim([0,dim[0][1]])
        ax.set_xlabel(str(dim[0][0])+' m')
        ax.set_ylabel(str(dim[0][1])+' m')
        self.draw()




## Plotting Above

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1059, 798)
        MainWindow.setLayoutDirection(QtCore.Qt.LeftToRight)
        MainWindow.setDocumentMode(False)
        MainWindow.setTabShape(QtWidgets.QTabWidget.Rounded)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setEnabled(False)                               ##
        self.pushButton.setGeometry(QtCore.QRect(290, 410, 161, 41))
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(self.rir)                 ##
        self.process = QtCore.QProcess()                          ##
        self.process.finished.connect(self.show_status)      
        self.process.readyReadStandardOutput.connect(self.handleStdOut)
        self.process.readyReadStandardError.connect(self.handleStdErr)        ##
        self.comboBox_array = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox_array.setGeometry(QtCore.QRect(40, 170, 141, 25))
        self.comboBox_array.activated[str].connect(self.get_array)     ##
        font = QtGui.QFont()
        font.setPointSize(13)
        self.comboBox_array.setFont(font)
        self.comboBox_array.setEditable(False)
        self.comboBox_array.setObjectName("comboBox_array")
        self.comboBox_array.addItem("")
        self.comboBox_array.addItem("")
        self.room = QtWidgets.QLabel(self.centralwidget)
        self.room.setGeometry(QtCore.QRect(50, 60, 151, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.room.setFont(font)
        self.room.setObjectName("room")
        self.comboBox_room = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox_room.setGeometry(QtCore.QRect(40, 80, 171, 25))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.comboBox_room.setFont(font)
        self.comboBox_room.setObjectName("comboBox_room")
        self.comboBox_room.addItem("")
        self.comboBox_room.addItem("")
        self.comboBox_room.addItem("")
        self.comboBox_room.activated[str].connect(self.set_positions)     ## 
        self.array = QtWidgets.QLabel(self.centralwidget)
        self.array.setGeometry(QtCore.QRect(40, 140, 121, 17))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.array.setFont(font)
        self.array.setObjectName("array")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(40, 240, 121, 17))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.channels = QtWidgets.QLabel(self.centralwidget)
        self.channels.setGeometry(QtCore.QRect(250, 140, 121, 17))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.channels.setFont(font)
        self.channels.setObjectName("channels")
        self.comboBox_channels = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox_channels.setGeometry(QtCore.QRect(250, 170, 121, 25))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.comboBox_channels.setFont(font)
        self.comboBox_channels.setObjectName("comboBox_channels")
        self.comboBox_channels.addItem("")
        self.comboBox_channels.addItem("")
        self.comboBox_channels.addItem("")
        self.center = QtWidgets.QLabel(self.centralwidget)
        self.center.setGeometry(QtCore.QRect(430, 140, 91, 17))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.center.setFont(font)
        self.center.setObjectName("center")
        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        self.label_8.setGeometry(QtCore.QRect(420, 170, 41, 17))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_8.setFont(font)
        self.label_8.setObjectName("label_8")
        self.label_9 = QtWidgets.QLabel(self.centralwidget)
        self.label_9.setGeometry(QtCore.QRect(490, 170, 41, 17))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_9.setFont(font)
        self.label_9.setObjectName("label_9")
        self.dimen = QtWidgets.QLabel(self.centralwidget)
        self.dimen.setGeometry(QtCore.QRect(570, 140, 91, 17))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.dimen.setFont(font)
        self.dimen.setObjectName("dimen")
        self.speaker = QtWidgets.QSpinBox(self.centralwidget)
        self.speaker.setGeometry(QtCore.QRect(200, 230, 48, 31))
        self.speaker.setMinimum(2)
        self.speaker.setMaximum(5)
        self.speaker.setObjectName("speaker")
        self.speaker.valueChanged.connect(self.set_speakers)               #
        self.room_2 = QtWidgets.QLabel(self.centralwidget)
        self.room_2.setGeometry(QtCore.QRect(320, 40, 101, 25))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.room_2.setFont(font)
        self.room_2.setObjectName("room_2")
        self.room_3 = QtWidgets.QLabel(self.centralwidget)
        self.room_3.setGeometry(QtCore.QRect(400, 40, 101, 25))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.room_3.setFont(font)
        self.room_3.setObjectName("room_3")
        self.doubleSpinBox = QtWidgets.QDoubleSpinBox(self.centralwidget)
        self.doubleSpinBox.setGeometry(QtCore.QRect(310, 70, 69, 41))
        self.doubleSpinBox.setMinimum(0.3)
        self.doubleSpinBox.setMaximum(1.0)
        self.doubleSpinBox.setSingleStep(0.01)
        self.doubleSpinBox.setObjectName("doubleSpinBox")
        self.doubleSpinBox1 = QtWidgets.QDoubleSpinBox(self.centralwidget)
        self.doubleSpinBox1.setGeometry(QtCore.QRect(420, 70, 69, 41))
        self.doubleSpinBox1.setMinimum(-1)
        self.doubleSpinBox1.setMaximum(0)
        self.doubleSpinBox1.setSingleStep(0.01)
        self.doubleSpinBox1.setObjectName("doubleSpinBox1")
        self.doubleSpinBox1.setEnabled(False)
        self.doubleSpinBox1.setValue(-1)
        self.label_10 = QtWidgets.QLabel(self.centralwidget)
        self.label_10.setGeometry(QtCore.QRect(60, 330, 41, 17))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_10.setFont(font)
        self.label_10.setObjectName("label_10")
        self.label_11 = QtWidgets.QLabel(self.centralwidget)
        self.label_11.setGeometry(QtCore.QRect(110, 330, 41, 17))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_11.setFont(font)
        self.label_11.setObjectName("label_11")
        self.label_12 = QtWidgets.QLabel(self.centralwidget)
        self.label_12.setGeometry(QtCore.QRect(200, 330, 41, 17))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_12.setFont(font)
        self.label_12.setObjectName("label_12")
        self.label_13 = QtWidgets.QLabel(self.centralwidget)
        self.label_13.setGeometry(QtCore.QRect(250, 330, 41, 17))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_13.setFont(font)
        self.label_13.setObjectName("label_13")
        self.label_14 = QtWidgets.QLabel(self.centralwidget)
        self.label_14.setGeometry(QtCore.QRect(330, 330, 41, 17))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_14.setFont(font)
        self.label_14.setObjectName("label_14")
        self.label_15 = QtWidgets.QLabel(self.centralwidget)
        self.label_15.setGeometry(QtCore.QRect(380, 330, 41, 17))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_15.setFont(font)
        self.label_15.setObjectName("label_15")
        self.label_16 = QtWidgets.QLabel(self.centralwidget)
        self.label_16.setGeometry(QtCore.QRect(470, 330, 41, 17))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_16.setFont(font)
        self.label_16.setObjectName("label_16")
        self.label_17 = QtWidgets.QLabel(self.centralwidget)
        self.label_17.setGeometry(QtCore.QRect(520, 330, 41, 17))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_17.setFont(font)
        self.label_17.setObjectName("label_17")
        self.label_18 = QtWidgets.QLabel(self.centralwidget)
        self.label_18.setGeometry(QtCore.QRect(610, 330, 41, 17))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_18.setFont(font)
        self.label_18.setObjectName("label_18")
        self.label_19 = QtWidgets.QLabel(self.centralwidget)
        self.label_19.setGeometry(QtCore.QRect(660, 330, 41, 17))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_19.setFont(font)
        self.label_19.setObjectName("label_19")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(60, 300, 67, 17))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(190, 300, 67, 17))
        self.label_3.setObjectName("label_3")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(330, 300, 67, 17))
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(470, 300, 67, 17))
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(610, 300, 67, 17))
        self.label_7.setObjectName("label_7")
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setGeometry(QtCore.QRect(0, 210, 731, 16))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.label_20 = QtWidgets.QLabel(self.centralwidget)
        self.label_20.setGeometry(QtCore.QRect(40, 280, 241, 17))
        self.label_20.setObjectName("label_20")
        self.radioButton = QtWidgets.QRadioButton(self.centralwidget)
        self.radioButton.setGeometry(QtCore.QRect(20, 20, 131, 23))
        font = QtGui.QFont()
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(75)
        self.radioButton.setFont(font)
        self.radioButton.setObjectName("radioButton")
        self.radioButton.setChecked(True)
        self.radioButton.toggled.connect(self.choose_rir)                               #
        self.radioButton_2 = QtWidgets.QRadioButton(self.centralwidget)
        self.radioButton_2.setGeometry(QtCore.QRect(20, 480, 141, 23))
        font = QtGui.QFont()
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(75)
        self.radioButton_2.setFont(font)
        self.radioButton_2.setObjectName("radioButton_2")
        self.radioButton_2.toggled.connect(self.choose_rir)                             #
        self.line_3 = QtWidgets.QFrame(self.centralwidget)
        self.line_3.setGeometry(QtCore.QRect(0, 0, 731, 16))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.line_3.setFont(font)
        self.line_3.setLineWidth(3)
        self.line_3.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_3.setObjectName("line_3")
        self.line_4 = QtWidgets.QFrame(self.centralwidget)
        self.line_4.setGeometry(QtCore.QRect(0, 460, 731, 16))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.line_4.setFont(font)
        self.line_4.setLineWidth(3)
        self.line_4.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_4.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_4.setObjectName("line_4")
        self.browse = QtWidgets.QPushButton(self.centralwidget)
        self.browse.setGeometry(QtCore.QRect(230, 510, 91, 31))
        self.browse.setObjectName("browse")
        self.browse.clicked.connect(self.browse_rir)                                  #
        self.label_21 = QtWidgets.QLabel(self.centralwidget)
        self.label_21.setGeometry(QtCore.QRect(30, 520, 191, 17))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_21.setFont(font)
        self.label_21.setObjectName("label_21")
        self.line_2 = QtWidgets.QFrame(self.centralwidget)
        self.line_2.setGeometry(QtCore.QRect(720, 10, 20, 701))
        self.line_2.setLineWidth(3)
        self.line_2.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        #self.label = QtWidgets.QLabel(self.centralwidget)
        #self.label.setGeometry(QtCore.QRect(730, 10, 321, 351))
        #self.label.setFrameShape(QtWidgets.QFrame.Box)
        #self.label.setText("")
        #self.label.setObjectName("label")
        self.lineEdit = QtWidgets.QTextEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(730, 370, 321, 341))
        self.lineEdit.setObjectName("lineEdit")
        self.line_5 = QtWidgets.QFrame(self.centralwidget)
        self.line_5.setGeometry(QtCore.QRect(0, 110, 731, 20))
        self.line_5.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_5.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_5.setObjectName("line_5")
        self.center_x = QtWidgets.QDoubleSpinBox(self.centralwidget)
        self.center_x.setGeometry(QtCore.QRect(430, 160, 51, 31))
        self.center_x.setSingleStep(0.01)
        self.center_x.setObjectName("center_x")
        self.center_y = QtWidgets.QDoubleSpinBox(self.centralwidget)
        self.center_y.setGeometry(QtCore.QRect(500, 160, 51, 31))
        self.center_y.setSingleStep(0.01)
        self.center_y.setObjectName("center_y")
        self.radius = QtWidgets.QDoubleSpinBox(self.centralwidget)
        self.radius.setGeometry(QtCore.QRect(590, 160, 51, 31))
        self.radius.setSingleStep(1.0)
        self.radius.setObjectName("radius")
        self.spinBox_6 = QtWidgets.QDoubleSpinBox(self.centralwidget)
        self.spinBox_6.setGeometry(QtCore.QRect(40, 350, 51, 31))
        self.spinBox_6.setSingleStep(0.01)
        self.spinBox_6.setObjectName("spinBox_6")
        self.spinBox_7 = QtWidgets.QDoubleSpinBox(self.centralwidget)
        self.spinBox_7.setGeometry(QtCore.QRect(100, 350, 51, 31))
        self.spinBox_7.setSingleStep(0.01)
        self.spinBox_7.setObjectName("spinBox_7")
        self.spinBox = QtWidgets.QDoubleSpinBox(self.centralwidget)
        self.spinBox.setGeometry(QtCore.QRect(180, 350, 51, 31))
        self.spinBox.setSingleStep(0.01)
        self.spinBox.setObjectName("spinBox")
        self.spinBox_8 = QtWidgets.QDoubleSpinBox(self.centralwidget)
        self.spinBox_8.setGeometry(QtCore.QRect(240, 350, 51, 31))
        self.spinBox_8.setObjectName("spinBox_8")
        self.spinBox_9 = QtWidgets.QDoubleSpinBox(self.centralwidget)
        self.spinBox_9.setGeometry(QtCore.QRect(320, 350, 51, 31))
        self.spinBox_9.setSingleStep(0.01)
        self.spinBox_9.setObjectName("spinBox_9")
        self.spinBox_10 = QtWidgets.QDoubleSpinBox(self.centralwidget)
        self.spinBox_10.setGeometry(QtCore.QRect(380, 350, 51, 31))
        self.spinBox_10.setSingleStep(0.01)
        self.spinBox_10.setObjectName("spinBox_10")
        self.spinBox_11 = QtWidgets.QDoubleSpinBox(self.centralwidget)
        self.spinBox_11.setGeometry(QtCore.QRect(460, 350, 51, 31))
        self.spinBox_11.setSingleStep(0.01)
        self.spinBox_11.setObjectName("spinBox_11")
        self.spinBox_12 = QtWidgets.QDoubleSpinBox(self.centralwidget)
        self.spinBox_12.setGeometry(QtCore.QRect(520, 350, 51, 31))
        self.spinBox_12.setSingleStep(0.01)
        self.spinBox_12.setObjectName("spinBox_12")
        self.spinBox_13 = QtWidgets.QDoubleSpinBox(self.centralwidget)
        self.spinBox_13.setGeometry(QtCore.QRect(600, 350, 51, 31))
        self.spinBox_13.setSingleStep(0.01)
        self.spinBox_13.setObjectName("spinBox_13")
        self.spinBox_14 = QtWidgets.QDoubleSpinBox(self.centralwidget)
        self.spinBox_14.setGeometry(QtCore.QRect(660, 350, 51, 31))
        self.spinBox_14.setSingleStep(0.01)
        self.spinBox_14.setObjectName("spinBox_14")
        self.spinBox_channels = QtWidgets.QSpinBox(self.centralwidget)
        self.spinBox_channels.setGeometry(QtCore.QRect(280, 170, 48, 26))
        self.spinBox_channels.setMinimum(2)
        self.spinBox_channels.setMaximum(5)
        self.spinBox_channels.setObjectName("spinBox_channels")
        self.rir_1 = QtWidgets.QLabel(self.centralwidget)
        self.rir_1.setGeometry(QtCore.QRect(30, 540, 481, 51))
        self.rir_1.setObjectName("rir_1")
        self.textEdit = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit.setGeometry(QtCore.QRect(310, 550, 301, 90))
        self.textEdit.setObjectName("textEdit")
        self.multi_audio = QtWidgets.QPushButton(self.centralwidget)
        self.multi_audio.setEnabled(True)
        self.multi_audio.setGeometry(QtCore.QRect(280, 700, 221, 41))
        self.multi_audio.setObjectName("multi_audio")
        self.multi_audio.clicked.connect(self.get_audio)
        self.sc_1 = QtWidgets.QPushButton(self.centralwidget)
        self.sc_1.setEnabled(True)
        self.sc_1.setGeometry(QtCore.QRect(240, 650, 81, 31))
        self.sc_1.setObjectName("sc_1")
        self.sc_2 = QtWidgets.QPushButton(self.centralwidget)
        self.sc_2.setEnabled(True)
        self.sc_2.setGeometry(QtCore.QRect(330, 650, 81, 31))
        self.sc_2.setObjectName("sc_2")
        self.sc_3 = QtWidgets.QPushButton(self.centralwidget)
        self.sc_3.setEnabled(True)
        self.sc_3.setGeometry(QtCore.QRect(420, 650, 81, 31))
        self.sc_3.setObjectName("sc_3")
        self.sc_4 = QtWidgets.QPushButton(self.centralwidget)
        self.sc_4.setEnabled(True)
        self.sc_4.setGeometry(QtCore.QRect(510, 650, 81, 31))
        self.sc_4.setObjectName("sc_4")
        self.sc_5 = QtWidgets.QPushButton(self.centralwidget)
        self.sc_5.setEnabled(True)
        self.sc_5.setGeometry(QtCore.QRect(600, 650, 81, 31))
        self.sc_5.setObjectName("sc_5")
        self.rir_2 = QtWidgets.QLabel(self.centralwidget)
        self.rir_2.setGeometry(QtCore.QRect(30, 650, 161, 31))
        self.rir_2.setObjectName("rir_2")
        self.channels.hide()
        self.comboBox_array.setEnabled(False)                                                     ##....
        self.comboBox_channels.hide()                                             
        self.spinBox_channels.hide()                                             
        self.radius.hide()                                                   
        self.center.hide()                                             
        self.label_8.hide()                                                 
        self.label_9.hide()                                             
        self.center_x.hide()                                                 
        self.center_y.hide()                                                     
        self.dimen.hide()                                                                 
        self.browse.setEnabled(False)                                              
        self.label_5.hide()
        self.label_14.hide()
        self.label_15.hide()
        self.spinBox_9.hide()
        self.spinBox_10.hide()
        self.label_6.hide()
        self.label_16.hide()
        self.label_17.hide()
        self.spinBox_11.hide()
        self.spinBox_12.hide()
        self.label_7.hide()
        self.label_18.hide()
        self.label_19.hide()
        self.spinBox_13.hide()
        self.spinBox_14.hide()                                             #....##
        self.sc_1.setEnabled(False) 
        self.sc_2.setEnabled(False) 
        self.sc_3.setEnabled(False) 
        self.sc_4.setEnabled(False) 
        self.sc_5.setEnabled(False) 
        self.multi_audio.setEnabled(False)
        self.rir_1.hide()
        self.rir_2.hide()
        self.textEdit.hide() 
        self.sc_1.clicked.connect(self.get_source_files1)
        self.sc_2.clicked.connect(self.get_source_files2)
        self.sc_3.clicked.connect(self.get_source_files3)
        self.sc_4.clicked.connect(self.get_source_files4)
        self.sc_5.clicked.connect(self.get_source_files5)
        self.num_sources = 0  
        self.fileName= ''                                           # ....##
        self.plotting = QtWidgets.QPushButton(self.centralwidget)
        self.plotting.setEnabled(False)
        self.plotting.setGeometry(QtCore.QRect(740, 120, 300, 100))
        self.plotting.clicked.connect(self.mat_plotting)
        self.plotting.setObjectName("Get Room Configuration")

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1059, 22))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.comboBox_array.setCurrentIndex(-1)
        self.comboBox_room.setCurrentIndex(-1)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
    def handleStdOut(self):
        data = self.process.readAllStandardOutput().data()
        self.lineEdit.append(data.decode('utf-8'))
    def handleStdErr(self):
        data = self.process.readAllStandardError().data()
        self.lineEdit.append(data.decode('utf-8')) 

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Multi-channel RIR - Audio Simulator"))
        self.pushButton.setText(_translate("MainWindow", "Generate RIR"))
        self.plotting.setText(_translate("MainWindow", "Show Room Configuration"))
        self.comboBox_array.setItemText(0, _translate("MainWindow", "Linear"))
        self.comboBox_array.setItemText(1, _translate("MainWindow", "Circular"))
        self.room.setText(_translate("MainWindow", "Choose  the Room (LxW) "))   ##
        self.room.resize(self.room.sizeHint())                         ##  
        self.comboBox_room.setItemText(0, _translate("MainWindow", "Room 1 430 x 330 (cm)"))                ##
        self.comboBox_room.setItemText(1, _translate("MainWindow", "Room 2 610 x 400 (cm)"))                ##
        self.comboBox_room.setItemText(2, _translate("MainWindow", "Room 3 10.5 x 5 (m)"))                 ## 
        self.comboBox_room.resize(self.comboBox_room.sizeHint())                                          ##
        self.array.setText(_translate("MainWindow", " Array Type"))
        self.label_4.setText(_translate("MainWindow", "No. of Speakers"))
        self.channels.setText(_translate("MainWindow", "No. of Channels"))
        self.comboBox_channels.setItemText(0, _translate("MainWindow", "4 - MIC"))                 ##
        self.comboBox_channels.setItemText(1, _translate("MainWindow", "5 - MIC"))                 ##
        self.comboBox_channels.setItemText(2, _translate("MainWindow", "8 - MIC"))                   ##
        self.center.setText(_translate("MainWindow", "Array Center"))
        self.label_8.setText(_translate("MainWindow", "X"))
        self.label_9.setText(_translate("MainWindow", "Y"))
        self.dimen.setText(_translate("MainWindow", "Array Radius"))
        self.room_2.setText(_translate("MainWindow", "T60(s)"))
        self.room_3.setText(_translate("MainWindow", "Refl. Index"))
        self.room_3.resize(self.room_3.sizeHint())
        self.label_10.setText(_translate("MainWindow", "X"))
        self.label_11.setText(_translate("MainWindow", "Y"))
        self.label_12.setText(_translate("MainWindow", "X"))
        self.label_13.setText(_translate("MainWindow", "Y"))
        self.label_14.setText(_translate("MainWindow", "X"))
        self.label_15.setText(_translate("MainWindow", "Y"))
        self.label_16.setText(_translate("MainWindow", "X"))
        self.label_17.setText(_translate("MainWindow", "Y"))
        self.label_18.setText(_translate("MainWindow", "X"))
        self.label_19.setText(_translate("MainWindow", "Y"))
        self.label_2.setText(_translate("MainWindow", "Speaker 1"))
        self.label_3.setText(_translate("MainWindow", "Speaker 2"))
        self.label_5.setText(_translate("MainWindow", "Speaker 3"))
        self.label_6.setText(_translate("MainWindow", "Speaker 4"))
        self.label_7.setText(_translate("MainWindow", "Speaker 5"))
        self.label_20.setText(_translate("MainWindow", "Enter Speaker Co-ordinates"))
        self.radioButton.setText(_translate("MainWindow", "Generate RIR"))
        self.radioButton.resize(self.radioButton.sizeHint())
        self.radioButton_2.setText(_translate("MainWindow", "Generate Data"))
        self.radioButton_2.resize(self.radioButton_2.sizeHint())
        self.browse.setText(_translate("MainWindow", "Browse"))
        self.label_21.setText(_translate("MainWindow", "Choose the RIR file..."))
        self.rir_1.setText(_translate("MainWindow", "The above selected  file conatins RIR for : "))
        self.multi_audio.setText(_translate("MainWindow", "Generate Multi-channel Audio"))
        self.sc_1.setText(_translate("MainWindow", "Source 1"))
        self.sc_2.setText(_translate("MainWindow", "Source 2"))
        self.sc_3.setText(_translate("MainWindow", "Source 3"))
        self.sc_4.setText(_translate("MainWindow", "Source 4"))
        self.sc_5.setText(_translate("MainWindow", "Source 5"))
        self.rir_2.setText(_translate("MainWindow", "Upload Source files : "))



    def set_positions(self):
        room = str(self.comboBox_room.currentText())
        if (room == "Room 1 430 x 330 (cm)"): 
             len_room = 4.3
             width_room = 3.3
             height_room = 1
        elif (room == "Room 2 610 x 400 (cm)"):
             len_room = 6.1
             width_room = 4
             height_room = 1
        else : 
             len_room = 10.5
             width_room = 5
             height_room = 1

        if (room == "Room 1 430 x 330 (cm)"):
            self.center_x.setValue(1.8)
            self.center_y.setValue(1.5)
            self.spinBox_6.setValue(1.6)
            self.spinBox_7.setValue(0.9)
            self.spinBox.setValue(1.6)
            self.spinBox_8.setValue(2.1)
            self.spinBox_9.setValue(2.2)
            self.spinBox_10.setValue(0.9)
            self.spinBox_11.setValue(2.2)
            self.spinBox_12.setValue(2.1)
            self.spinBox_13.setValue(3.0)
            self.spinBox_14.setValue(2.1)
        elif (room == "Room 2 610 x 400 (cm)"):
            self.center_x.setValue(2.6)
            self.center_y.setValue(1.8)
            self.spinBox_6.setValue(2)
            self.spinBox_7.setValue(1.5)
            self.spinBox.setValue(2)
            self.spinBox_8.setValue(3.1)
            self.spinBox_9.setValue(3.2)
            self.spinBox_10.setValue(1.5)
            self.spinBox_11.setValue(3.2)
            self.spinBox_12.setValue(3.1)
            self.spinBox_13.setValue(4)
            self.spinBox_14.setValue(3.1)
        else : 
            self.center_x.setValue(3.6)
            self.center_y.setValue(3.2) 
            self.spinBox_6.setValue(4.1)
            self.spinBox_7.setValue(2.4)
            self.spinBox.setValue(4.1)
            self.spinBox_8.setValue(3.5) 
            self.spinBox_9.setValue(4.4)
            self.spinBox_10.setValue(2.4)
            self.spinBox_11.setValue(4.4)
            self.spinBox_12.setValue(3.5)
            self.spinBox_13.setValue(4.9)
            self.spinBox_14.setValue(3.5) 
        self.spinBox_6.setMaximum(len_room-0.8)
        self.spinBox_6.setMinimum(0.8)
        self.spinBox_7.setMaximum(width_room-0.8)
        self.spinBox_7.setMinimum(0.8)
        self.spinBox.setMaximum(len_room-0.8)
        self.spinBox.setMinimum(0.8)
        self.spinBox_8.setMaximum(width_room-0.8)
        self.spinBox_8.setMinimum(0.8)
        self.spinBox_9.setMaximum(len_room-0.8)
        self.spinBox_9.setMinimum(0.8)
        self.spinBox_10.setMaximum(width_room-0.8)
        self.spinBox_10.setMinimum(0.8)
        self.spinBox_11.setMaximum(len_room-0.8)
        self.spinBox_11.setMinimum(0.8)
        self.spinBox_12.setMaximum(width_room-0.8)
        self.spinBox_12.setMinimum(0.8)
        self.spinBox_13.setMaximum(len_room-0.8)
        self.spinBox_13.setMinimum(0.8)
        self.spinBox_14.setMaximum(width_room-0.8)
        self.spinBox_14.setMinimum(0.8)  
        self.comboBox_array.setEnabled(True)    
    def choose_rir(self):
        if self.radioButton_2.isChecked():
            self.browse.setEnabled(True)                                              ## 
            self.pushButton.setEnabled(False)                                              ## 
            

        if self.radioButton.isChecked():
            self.browse.setEnabled(False)                                              ##                                              ##
            global file_list
            file_list = []
            self.textEdit.setEnabled(False)
            #self.pushButton.setEnabled(True)
        self.sc_1.setEnabled(False) 
        self.sc_2.setEnabled(False) 
        self.sc_3.setEnabled(False)
        self.sc_4.setEnabled(False)
        self.sc_5.setEnabled(False)
        self.plotting.setEnabled(False)
        self.textEdit.setEnabled(False) 
        self.multi_audio.setEnabled(False)
    def set_speakers(self):
        if (self.speaker.value() == 2):
            self.label_5.hide()
            self.label_14.hide()
            self.label_15.hide()
            self.spinBox_9.hide()
            self.spinBox_10.hide()
            self.label_6.hide()
            self.label_16.hide()
            self.label_17.hide()
            self.spinBox_11.hide()
            self.spinBox_12.hide()
            self.label_7.hide()
            self.label_18.hide()
            self.label_19.hide()
            self.spinBox_13.hide()
            self.spinBox_14.hide()
        elif (self.speaker.value() == 3):
            self.label_5.show()
            self.label_14.show()
            self.label_15.show()
            self.spinBox_9.show()
            self.spinBox_10.show()
            self.label_6.hide()
            self.label_16.hide()
            self.label_17.hide()
            self.spinBox_11.hide()
            self.spinBox_12.hide()
            self.label_7.hide()
            self.label_18.hide()
            self.label_19.hide()
            self.spinBox_13.hide()
            self.spinBox_14.hide()          
        elif (self.speaker.value() == 4):
            self.label_5.show()
            self.label_14.show()
            self.label_15.show()
            self.spinBox_9.show()
            self.spinBox_10.show()
            self.label_6.show()
            self.label_16.show()
            self.label_17.show()
            self.spinBox_11.show()
            self.spinBox_12.show()          
            self.label_7.hide()
            self.label_18.hide()
            self.label_19.hide()
            self.spinBox_13.hide()
            self.spinBox_14.hide() 
        else:
            self.label_5.show()
            self.label_14.show()
            self.label_15.show()
            self.spinBox_9.show()
            self.spinBox_10.show()
            self.label_6.show()
            self.label_16.show()
            self.label_17.show()
            self.spinBox_11.show()
            self.spinBox_12.show()
            self.label_7.show()
            self.label_18.show()
            self.label_19.show()
            self.spinBox_13.show()
            self.spinBox_14.show()          


    def browse_rir(self):
        options = QtWidgets.QFileDialog.Options()
        self.fileName, _ = QtWidgets.QFileDialog.getOpenFileName(None,"QFileDialog.getOpenFileName()", "","Matrix (*.mat);;All Files (*)", options=options)
        global file_list
        global no_chn,no_spk,T60,fs,center,types,room,angles,pos,reflec,dim
        file_list = []
        self.multi_audio.setEnabled(False)
        import scipy.io 
        mat = scipy.io.loadmat(self.fileName)
        num_sources = mat['rir'].shape[2]
        no_spk = num_sources
        self.num_sources = num_sources
        num_chn = mat['rir'].shape[0]
        no_chn = num_chn
        t60 = mat['t60']
        fs=mat['fs']
        reflec = mat['orders']
        center = mat['center']
        types = mat['arr_type']
        room = mat['rooms']
        dim = mat['L']
        pos = mat['s']
        angles = []
        print(pos,center)
        for i in range(num_sources):
             angles.append(get_angle(pos[i][0],pos[i][1],center[0][0],center[0][1]))
        print(angles)
        T60 = t60
        self.textEdit.setReadOnly(True)
        self.textEdit.setEnabled(True)
        self.textEdit.clear()
        self.textEdit.append('Number of channels :'+str(num_chn)+'\n')
        self.textEdit.append('Number of Speakers :'+str(num_sources)+'\n')
        self.textEdit.append('T60 used :'+str(t60))
        self.textEdit.setTextBackgroundColor(QtGui.QColor(0,0,255))
        self.textEdit.show()
        if (num_sources == 2):
            self.sc_1.setEnabled(True)
            self.sc_2.setEnabled(True)
            self.sc_3.setEnabled(False)
            self.sc_4.setEnabled(False)
            self.sc_5.setEnabled(False) 
        elif (num_sources == 3):
            self.sc_1.setEnabled(True)
            self.sc_2.setEnabled(True)          
            self.sc_3.setEnabled(True)
            self.sc_4.setEnabled(False) 
            self.sc_5.setEnabled(False)   
        elif (num_sources == 4):
            self.sc_1.setEnabled(True)
            self.sc_2.setEnabled(True)          
            self.sc_3.setEnabled(True)
            self.sc_4.setEnabled(True) 
            self.sc_5.setEnabled(False)         
        else :
            self.sc_1.setEnabled(True)
            self.sc_2.setEnabled(True)          
            self.sc_3.setEnabled(True)
            self.sc_4.setEnabled(True)
            self.sc_5.setEnabled(True)
        self.rir_1.show()
        self.rir_2.show()
        self.plotting.setEnabled(True)
        #Complete this function
        


    def get_source_files(self):
        options = QtWidgets.QFileDialog.Options()
        fileName, _ = QtWidgets.QFileDialog.getOpenFileName(None,"QFileDialog.getOpenFileName()", "","All Files (*);;Audio Files (*.wav)", options=options)
        global file_list
        file_list.append(fileName)
        #print(self.num_sources)
        #print(len(file_list))
        if(self.num_sources == len(file_list)):
            self.multi_audio.setEnabled(True)
    def get_source_files1(self):
        options = QtWidgets.QFileDialog.Options()
        fileName, _ = QtWidgets.QFileDialog.getOpenFileName(None,"QFileDialog.getOpenFileName()", "","FLAC file(*.flac);;WAV file (*.wav);;All Files (*)", options=options)
        global file_list
        file_list.append(fileName)
        self.sc_1.setEnabled(False)
        #print(self.num_sources)
        #print(len(file_list))
        if(self.num_sources == len(file_list)):
            self.multi_audio.setEnabled(True)
    def get_source_files2(self):
        options = QtWidgets.QFileDialog.Options()
        fileName, _ = QtWidgets.QFileDialog.getOpenFileName(None,"QFileDialog.getOpenFileName()", "","FLAC file(*.flac);;WAV file (*.wav);;All Files (*)", options=options)
        global file_list
        file_list.append(fileName)
        self.sc_2.setEnabled(False)
        #print(self.num_sources)
        #print(len(file_list))
        if(self.num_sources == len(file_list)):
            self.multi_audio.setEnabled(True)
    def get_source_files3(self):
        options = QtWidgets.QFileDialog.Options()
        fileName, _ = QtWidgets.QFileDialog.getOpenFileName(None,"QFileDialog.getOpenFileName()", "","FLAC file(*.flac);;WAV file (*.wav);;All Files (*)", options=options)
        global file_list
        file_list.append(fileName)
        self.sc_3.setEnabled(False)
        #print(self.num_sources)
        #print(len(file_list))
        if(self.num_sources == len(file_list)):
            self.multi_audio.setEnabled(True)
    def get_source_files4(self):
        options = QtWidgets.QFileDialog.Options()
        fileName, _ = QtWidgets.QFileDialog.getOpenFileName(None,"QFileDialog.getOpenFileName()", "","FLAC file(*.flac);;WAV file (*.wav);;All Files (*)", options=options)
        global file_list
        file_list.append(fileName)
        self.sc_4.setEnabled(False)
        #print(self.num_sources)
        #print(len(file_list))
        if(self.num_sources == len(file_list)):
            self.multi_audio.setEnabled(True)
    def get_source_files5(self):
        options = QtWidgets.QFileDialog.Options()
        fileName, _ = QtWidgets.QFileDialog.getOpenFileName(None,"QFileDialog.getOpenFileName()", "","FLAC file(*.flac);;WAV file (*.wav);;All Files (*)", options=options)
        global file_list
        file_list.append(fileName)
        self.sc_5.setEnabled(False)
        #print(self.num_sources)
        #print(len(file_list))
        if(self.num_sources == len(file_list)):
            self.multi_audio.setEnabled(True)
    def rir(self):
        room = str(self.comboBox_room.currentText())
        if (room == "Room 1 430 x 330 (cm)"): 
            len_room = 4.3
            width_room = 3.3
            height_room = 1
        elif (room == "Room 2 610 x 400 (cm)"):
            len_room = 6.1
            width_room = 4
            height_room = 1
        else : 
            len_room = 10.5
            width_room = 5
            height_room = 1


        center_x = self.center_x.value()
        center_y = self.center_y.value()
        radius = self.radius.value()
        if(self.speaker.value() == 2):
            post_spks1 = np.array([self.spinBox_6.value(),self.spinBox_7.value(),1])
            post_spks2 = np.array([self.spinBox.value(),self.spinBox_8.value(),1])
            post_spks = np.stack((post_spks1,post_spks2),axis=0)
        elif(self.speaker.value() == 3):
            post_spks1 = np.array([self.spinBox_6.value(),self.spinBox_7.value(),1])
            post_spks2 = np.array([self.spinBox.value(),self.spinBox_8.value(),1])        
            post_spks3 = np.array([self.spinBox_9.value(),self.spinBox_10.value(),1])
            post_spks = np.stack((post_spks1,post_spks2,post_spks3),axis=0)
        elif(self.speaker.value() == 4):
            post_spks1 = np.array([self.spinBox_6.value(),self.spinBox_7.value(),1])
            post_spks2 = np.array([self.spinBox.value(),self.spinBox_8.value(),1])
            post_spks3 = np.array([self.spinBox_9.value(),self.spinBox_10.value(),1])
            post_spks4 = np.array([self.spinBox_11.value(),self.spinBox_12.value(),1])
            post_spks = np.stack((post_spks1,post_spks2,post_spks3,post_spks4),axis=0)
        else:
            post_spks1 = np.array([self.spinBox_6.value(),self.spinBox_7.value(),1])
            post_spks2 = np.array([self.spinBox.value(),self.spinBox_8.value(),1])
            post_spks3 = np.array([self.spinBox_9.value(),self.spinBox_10.value(),1])
            post_spks4 = np.array([self.spinBox_11.value(),self.spinBox_12.value(),1])
            post_spks5 = np.array([self.spinBox_13.value(),self.spinBox_14.value(),1])  
            post_spks = np.stack((post_spks1,post_spks2,post_spks3,post_spks4,post_spks5),axis=0)   
        arr_type = self.comboBox_room.currentText()    
        if(self.comboBox_array.currentText()=="Linear"): 
            num_channels = self.spinBox_channels.value() 
            arr = 'Linear'
        else: 
            arr = 'Circular'
            types = self.comboBox_channels.currentText()
            if (types == "4 - MIC"):
                num_channels = 4
            elif (types == "5 - MIC"):
                num_channels = 5
            else:
                num_channels = 8
        t60 = self.doubleSpinBox.value()
        command = get_rir(arr,num_channels,np.array([center_x,center_y,0]),radius,post_spks,np.array([len_room,width_room,height_room]),t60,room)
        #room = str(self.comboBox_array.currentText())
        #if (room == "Room 1 430 x 330 (cm)"): 
        #command = 'matlab -nodisplay -nosplash -nodesktop -r "rir(3,2,16000,[1 1 1;1 7 1],[2 3 1;2 4 1;2 5 1],[10 10 2],0.4);exit;"'
        self.lineEdit.clear()
        self.textEdit.setReadOnly(True)
        self.process.start(command)


    def show_status(self):
        self.lineEdit.append("Done")
    def get_audio(self):
        import scipy.io 
        import soundfile as sf
        global file_list
        mat = scipy.io.loadmat(self.fileName)
        #print(int(mat['fs']))
        sil = np.zeros(int(mat['fs']))
        data = mat['rir']
        self.lineEdit.clear()
        self.lineEdit.append("Generating multi-channel audio")
        self.lineEdit.append(str(data.shape[0])+' multi-channel files selected')
        self.lineEdit.append(str(data.shape[2])+' speakers present')
        multi_audio= []
        for i in range(data.shape[0]):
            multi_spk = []
            for j in range(data.shape[2]):
                y,fs = sf.read(file_list[j])
                output = np.convolve(y,data[i,:,j])
                multi_spk.append(np.concatenate((sil,output),axis=0))
            x =np.concatenate(multi_spk,axis=0)
            multi_audio.append(x)
            #print(multi_spk[0].shape,multi_spk[1].shape)
        multi_audio =np.stack(multi_audio,axis=0)
        x = self.fileName.split('.')[0]
        y = self.fileName.split('.')[1]
        z = self.fileName.split('/')[-1]
        self.lineEdit.append("Done")
        self.lineEdit.append("File Saved at :  multi_audio/"+z+".wav")
        sf.write('multi_audio/'+z+'.wav',multi_audio.transpose(1,0),int(mat['fs']))
        self.plotting.setEnabled(True)




    def get_array(self):
        array = str(self.comboBox_array.currentText())
        self.label_8.show()
        self.label_9.show()
        if(array == "Linear"):
            self.spinBox_channels.show()
            self.center.setText("Left Mic Pos. ")
            self.center.resize(self.center.sizeHint())  
            self.dimen.setText("Array Spacing (cm)")
            self.dimen.resize(self.dimen.sizeHint()) 
            self.comboBox_channels.hide()       
        else:                                
            self.comboBox_channels.show()
            self.spinBox_channels.hide()
            self.center.setText("Array Center")
            self.dimen.setText("Array Radius (cm)")
            self.dimen.resize(self.dimen.sizeHint()) 
            self.center.resize(self.center.sizeHint())   
        self.radius.show() 
        self.dimen.show()
        self.center.show()
        self.channels.show()
        self.center_x.show()
        self.center_y.show()
        self.radius.setValue(5)
        if(self.radioButton.isChecked()):
            self.pushButton.setEnabled(True) 
######################################################################################################################
    def mat_plotting(self):
        #apps = QtWidgets.QApplication(sys.argv)
        #MainWindows = QtWidgets.QMainWindow()
        self.w = QtWidgets.QMainWindow()
        self.uis = Ui_d_MainWindow()
        self.uis.setupUi(self.w)
        self.w.show()
        global no_chn,no_spk,T60,fs,center,types,room,angles,pos,reflec,dim
        uis.show()
        #sys.exit(apps.exec_())
#####################################################################################################################
def get_angle(x,y,a,b):
    if(x>=a and y>b):
        angle = (np.arctan((y-b)/(x-a+np.finfo(float).eps)))*180/np.pi
    elif(x<a and y>b):
        angle = (np.pi-np.arctan((y-b)/(a-x)))*180/np.pi
    elif(x<a and y<b):
        angle = (-np.pi+np.arctan((b-y)/(a-x)))*180/np.pi
    else:
        angle = (np.arctan((y-b)/(x-a+np.finfo(float).eps)))*180/np.pi
    return np.floor(angle)

def get_rir(arr,num_c,center,radius,spks,room,t60,rooms):
    post_arr = []
    if(arr == 'Linear'):
        for i in range(num_c):
            post = np.add(center,np.array([i*radius/100,0,0]))
            post_arr.append(post.tolist())
    else:
        if(num_c == 4):
            theta = np.pi/2
            for i in range(num_c):
                post = np.add(center,np.array([np.cos(i*theta)*radius/100,np.sin(i*theta)*radius/100,0]))
                post_arr.append(post.tolist())          
        elif(num_c == 5):
            theta = np.pi/2
            for i in range(num_c-1):
                post = np.add(center,np.array([np.cos(i*theta)*radius/100, np.sin(i*theta)*radius/100,0]))
                post_arr.append(post.tolist())
            post_arr.append(center.tolist())  
        else:
            theta = np.pi/4
            for i in range(num_c):
                post = np.add(center,np.array([np.cos(i*theta)*radius/100 ,np.sin(i*theta)*radius/100 ,0]))
                post_arr.append(post.tolist())  
    num_spk = spks.shape[0]
    spks = spks.tolist()
    room = np.expand_dims(room,axis=0)
    room = room.tolist()
    rooms = "'"+rooms+"'"
    arr = "'"+arr+"'"
    command = 'octave --silent --eval "rir('+str(num_spk)+','+str(num_c)+','+'16000,'+mat_arr(post_arr)+','+mat_arr(spks)+','+mat_arr(room)+','+str(t60)+','+rooms+','+arr+')"'
               #mat_arr(post_arr)+','+mat_arr(room)+','+str(t60)+');exit;'
    #command = 'matlab -nodisplay -nosplash -nodesktop -r "rir(3,2,16000,[1 1 1;1 7 1],[2 3 1;2 4 1;2 5 1],[10 10 2],0.4);exit;"'
    print(command)
    return command
def mat_arr(array):
    return '[' + "; ".join(" ".join("%1g" % val for val in line) for line in array) + ']'



if __name__ == "__main__":
    import sys
    import argparse
    from subprocess import Popen,PIPE

    parser = argparse.ArgumentParser()
    parser.add_argument('gui', help="Whether to train or test 1/0",type=int,choices=[0,1])
    #parser.add_argument('--r_type', help="Whether to train or test 1/0",type=int,choices=[1,2,3])
    parser.add_argument('--a_type', help="Whether to train or test 1/0",type=str,choices=['l','c'])
    parser.add_argument("--num_c",help="Number of samples in the batch",type=int,choices=[2,3,4,5,6,7,8])
    parser.add_argument("--num_s",help="Number of samples in the batch",type=int)
    parser.add_argument("--center", nargs="+",type=float)
    parser.add_argument("--radius",help="Number of samples in the batch",type=float)
    parser.add_argument('--spk_loc',nargs='+',type=float)
    parser.add_argument("--room", nargs="+",type=float)
    parser.add_argument("--t60",help="Number of samples in the batch",type=float)
    args = parser.parse_args()
    #print(args.gui)
    if(args.gui == 0):
        arr = args.a_type
        num_c = args.num_c
        center = np.array(args.center)
        radius = args.radius
        spks = np.array(args.spk_loc)
        spks = spks.reshape(-1,3)
        room = np.array(args.room)
        t60 = args.t60
        if(arr == 'l'): 
            arr = "Linear"
        else:
            ar = "Circular"
        cmd=get_rir(arr,num_c,center,radius,spks,room,t60)
        #print(cmd)
        p = Popen(cmd,stdout=PIPE, )
        out, err = p.communicate()
        #Code here
        sys.exit()  
    no_spk=''
    no_chn=''
    T60 = ''
    center=''
    pos = ''
    types=''
    room=''
    reflec=''
    fs=''
    angles=''
    dim=''
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())














