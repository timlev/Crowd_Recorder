# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'recording.ui'
#
# Created: Sat May 24 09:07:21 2014
#      by: PyQt4 UI code generator 4.10.4
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui, QtMultimedia
import wave
import json
import sound_button_rc

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(917, 644)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8(":/icon/cloudsound2.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setIconSize(QtCore.QSize(300, 300))
        MainWindow.setToolButtonStyle(QtCore.Qt.ToolButtonTextBesideIcon)
        MainWindow.setAnimated(True)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.verticalLayout_2 = QtGui.QVBoxLayout(self.centralwidget)
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setSizeConstraint(QtGui.QLayout.SetDefaultConstraint)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.soundbutton = QtGui.QPushButton(self.centralwidget)
        self.soundbutton.setMinimumSize(QtCore.QSize(80, 80))
        self.soundbutton.setMaximumSize(QtCore.QSize(80, 80))
        self.soundbutton.setStyleSheet(_fromUtf8("background-image: url(:/icon/sound.png);"))
        self.soundbutton.setText(_fromUtf8(""))
        self.soundbutton.setObjectName(_fromUtf8("soundbutton"))
        self.horizontalLayout.addWidget(self.soundbutton)
        self.word_display = QtGui.QTextBrowser(self.centralwidget)
        self.word_display.setMaximumSize(QtCore.QSize(16777215, 100))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Didact Gothic"))
        font.setPointSize(24)
        self.word_display.setFont(font)
        self.word_display.setObjectName(_fromUtf8("word_display"))
        self.horizontalLayout.addWidget(self.word_display)
        self.languagebox = QtGui.QComboBox(self.centralwidget)
        self.languagebox.setMaximumSize(QtCore.QSize(16777215, 200))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Didact Gothic"))
        font.setPointSize(18)
        self.languagebox.setFont(font)
        self.languagebox.setObjectName(_fromUtf8("languagebox"))
        #self.languagebox.addItem(_fromUtf8(""))
        #self.languagebox.addItem(_fromUtf8(""))
        #self.languagebox.addItem(_fromUtf8(""))
        #self.languagebox.addItem(_fromUtf8(""))
        #self.languagebox.addItem(_fromUtf8(""))
        self.horizontalLayout.addWidget(self.languagebox)
        self.verticalLayout_2.addLayout(self.horizontalLayout)
        self.gridLayout_2 = QtGui.QGridLayout()
        self.gridLayout_2.setObjectName(_fromUtf8("gridLayout_2"))
        self.verticalLayout_5 = QtGui.QVBoxLayout()
        self.verticalLayout_5.setObjectName(_fromUtf8("verticalLayout_5"))
        self.recordbutton = QtGui.QPushButton(self.centralwidget)
        self.recordbutton.setMinimumSize(QtCore.QSize(80, 80))
        self.recordbutton.setMaximumSize(QtCore.QSize(80, 80))
        self.recordbutton.setStyleSheet(_fromUtf8("background-image: url(:/icon/mic.png);"))
        self.recordbutton.setText(_fromUtf8(""))
        self.recordbutton.setObjectName(_fromUtf8("recordbutton"))
        self.verticalLayout_5.addWidget(self.recordbutton)
        self.nextbutton = QtGui.QPushButton(self.centralwidget)
        self.nextbutton.setMaximumSize(QtCore.QSize(100, 100))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Didact Gothic"))
        font.setPointSize(28)
        self.nextbutton.setFont(font)
        self.nextbutton.setObjectName(_fromUtf8("nextbutton"))
        self.verticalLayout_5.addWidget(self.nextbutton)
        self.gridLayout_2.addLayout(self.verticalLayout_5, 0, 2, 1, 1)
        self.label = QtGui.QLabel(self.centralwidget)
        self.label.setMinimumSize(QtCore.QSize(500, 500))
        self.label.setBaseSize(QtCore.QSize(0, 0))
        self.label.setText(_fromUtf8(""))
        self.label.setObjectName(_fromUtf8("label"))
        self.gridLayout_2.addWidget(self.label, 0, 1, 1, 1)
        self.verticalLayout_2.addLayout(self.gridLayout_2)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 917, 18))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        self.menuFile = QtGui.QMenu(self.menubar)
        self.menuFile.setObjectName(_fromUtf8("menuFile"))
        self.menuDo = QtGui.QMenu(self.menubar)
        self.menuDo.setObjectName(_fromUtf8("menuDo"))
        self.menuView = QtGui.QMenu(self.menubar)
        self.menuView.setObjectName(_fromUtf8("menuView"))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)
        self.actionQuit = QtGui.QAction(MainWindow)
        self.actionQuit.setObjectName(_fromUtf8("actionQuit"))
        self.actionRecord = QtGui.QAction(MainWindow)
        self.actionRecord.setObjectName(_fromUtf8("actionRecord"))
        self.actionFullscreen = QtGui.QAction(MainWindow)
        self.actionFullscreen.setObjectName(_fromUtf8("actionFullscreen"))
        self.actionRegular = QtGui.QAction(MainWindow)
        self.actionRegular.setObjectName(_fromUtf8("actionRegular"))
        self.menuFile.addAction(self.actionQuit)
        self.menuDo.addAction(self.actionRecord)
        self.menuView.addAction(self.actionFullscreen)
        self.menuView.addAction(self.actionRegular)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuDo.menuAction())
        self.menubar.addAction(self.menuView.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QObject.connect(self.actionQuit, QtCore.SIGNAL(_fromUtf8("triggered()")), MainWindow.close)
        QtCore.QObject.connect(self.actionFullscreen, QtCore.SIGNAL(_fromUtf8("triggered()")), MainWindow.showFullScreen)
        QtCore.QObject.connect(self.actionRegular, QtCore.SIGNAL(_fromUtf8("triggered()")), MainWindow.showNormal)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)


    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "Recording", None))
        self.word_display.text = "What is your name? My name is Tim Leverentz."
        self.word_display.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Didact Gothic\'; font-size:24pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">"+ self.word_display.text +"</p></body></html>", None))
        #self.languagebox.setItemText(0, _translate("MainWindow", "Chinese", None))
        #self.languagebox.setItemText(1, _translate("MainWindow", "Karen", None))
        #self.languagebox.setItemText(2, _translate("MainWindow", "Burmese", None))
        #self.languagebox.setItemText(3, _translate("MainWindow", "Nepalese", None))
        #self.languagebox.setItemText(4, _translate("MainWindow", "Somali", None))
        self.nextbutton.setText(_translate("MainWindow", "Next", None))
        self.menuFile.setTitle(_translate("MainWindow", "File", None))
        self.menuDo.setTitle(_translate("MainWindow", "Do", None))
        self.menuView.setTitle(_translate("MainWindow", "View", None))
        self.actionQuit.setText(_translate("MainWindow", "Quit", None))
        self.actionQuit.setShortcut(_translate("MainWindow", "Ctrl+Q", None))
        self.actionRecord.setText(_translate("MainWindow", "Record", None))
        self.actionRecord.setShortcut(_translate("MainWindow", "Space", None))
        self.actionFullscreen.setText(_translate("MainWindow", "Fullscreen", None))
        self.actionRegular.setText(_translate("MainWindow", "Regular", None))

    def soundsetup2(self, MainWindow):
        self.file = QtCore.QFile()
        self.file.setFileName("testMicIn.wav")
        self.file.open(QtCore.QIODevice.WriteOnly)

        self.format = QtMultimedia.QAudioFormat()
        self.format.setFrequency(44100)
        self.format.setChannels(1)
        self.format.setCodec("audio/pcm")
        self.format.setByteOrder(QtMultimedia.QAudioFormat.LittleEndian)
        self.format.setSampleType(QtMultimedia.QAudioFormat.UnSignedInt)
        self.info = QtMultimedia.QAudioDeviceInfo(QtMultimedia.QAudioDeviceInfo.defaultInputDevice())
        self.format = self.info.nearestFormat(self.format)
        self.audio = QtMultimedia.QAudioInput(self.format)

    def soundsetup(self, MainWindow):
        self.bitsPerSample = 32
        self.samplingRate = 44100
        

        self.format = QtMultimedia.QAudioFormat()
        self.format.setChannelCount(1)
        self.format.setSampleRate(self.samplingRate)
        self.format.setSampleSize(self.bitsPerSample)
        #format.setCodec(self.audioType)
        self.format.setByteOrder(QtMultimedia.QAudioFormat.LittleEndian)
        self.format.setSampleType(QtMultimedia.QAudioFormat.UnSignedInt)

        self.audiodevice = QtMultimedia.QAudioDeviceInfo.defaultInputDevice()
        if not self.audiodevice.isFormatSupported(self.format):
            self.format = self.audiodevice.nearestFormat(self.format)
        self.audio = QtMultimedia.QAudioInput(self.audiodevice, self.format)

    def eventFilter(self, widget, event):
        if (event.type() == QtCore.QEvent.KeyPress):
            key = event.key()
            print key
            if key == QtCore.Qt.Key_Escape:
                print('escape')
        return QtGui.QWidget.eventFilter(self, widget, event)
            
    def keyPressEvent(self, event):
        print event.key()
        
    def startRecording(self):
        self.io = self.audio.start()
        self.io.readyRead.connect(self.handleDataReadyRead)

    def pasueRecording(self):
        self.audio.suspend()

    def resumeRecording(self):
        self.audio.resume()

    def stopRecording(self):
        self.audio.stop()

    def handleDataReadyRead(self):
        databuffer = self.io.readAll().data()
        # print type(databuffer)
        self.sendbuffer.append(databuffer)

    def handleNotify(self):
        print len(self.sendbuffer)
        primarydata = ''.join(self.sendbuffer)
        data = primarydata.encode("base64")
        jsondata = json.loads(json.dumps(data)).decode("base64")
        self.wavfw.writeframes(jsondata)
        self.sendbuffer = []

    def stopAudioRecord(self):
        self.stopRecording()
        self.handleNotify()
        self.wavfw.close()

    def initAudio(self,filename):
        self.sendbuffer = []
        self.bitsPerSample = 8
        self.samplingRate = 8000
        # self.wavfw = wave.open("%s.wav" % time.strftime("%Y-%m-%d %H-%M-%S", time.localtime()), 'w')
        self.wavfw = wave.open(filename, 'w')
        self.wavfw.setnchannels(1)
        self.wavfw.setsampwidth(self.bitsPerSample / 8)
        self.wavfw.setframerate(self.samplingRate)

        format = QtMultimedia.QAudioFormat()
        format.setChannelCount(1)
        format.setSampleRate(self.samplingRate)
        format.setSampleSize(self.bitsPerSample)
        #format.setCodec(self.audioType)
        format.setByteOrder(QtMultimedia.QAudioFormat.LittleEndian)
        format.setSampleType(QtMultimedia.QAudioFormat.UnSignedInt)

        self.audiodevice = QtMultimedia.QAudioDeviceInfo.defaultInputDevice()
        if not self.audiodevice.isFormatSupported(format):
            format = self.audiodevice.nearestFormat(format)

        self.audio = QtMultimedia.QAudioInput(self.audiodevice, format)
        #self.audio.setNotifyInterval(self.notifyinterval * 1000)
        #self.audio.notify.connect(self.handleNotify)
#import sound_button_rc

if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    MainWindow = QtGui.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

