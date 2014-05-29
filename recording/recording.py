from include.recording_ui import *

import os

def plang():
    print str(ui.languagebox.currentText())

def getbestratio(boxheight,boxwidth,picheight,picwidth):
    height_ratio = float(boxheight) / float(picheight)
    width_ratio = float(boxwidth) / float(picwidth)
    picwidth *= min(width_ratio, height_ratio)
    picheight *= min(width_ratio, height_ratio)
    return int(picwidth), int(picheight)

def playrecordedsound(filename):
    QtGui.QSound.play(filename)

def playenglishsound():
    QtGui.QSound.play(soundfile)

def record2():
    global currentpath
    print "Output pressed"
    language = str(ui.languagebox.currentText())
    directory = os.path.join(currentpath, "Translations")
    print directory
    filename = os.path.join(directory,language + "_" + rdisplay_word(ui.word_display.text) + ".wav")
    print filename
    #print ui.audio.state(), QtMultimedia.QAudio.ActiveState
    if ui.audio.state() == QtMultimedia.QAudio.ActiveState:
        print "Active"
        ui.stopAudioRecord()
        ui.recordbutton.setStyleSheet(u"background-image: url(:/icon/mic.png);")
        print "Stopped"
        print QtMultimedia.QAudioOutput
        playrecordedsound(filename)
        return 0
    elif ui.audio.state() == QtMultimedia.QAudio.StoppedState:
        #ui.filename = filename
        #ui.audio.reset()
        ui.initAudio(filename)
        ui.startRecording()
        print ui.audio.state()
        print "Started"
        ui.recordbutton.setStyleSheet(u"background-image: url(:/icon/recorddot.png);")
        #ui.nextbutton.clicked.connect(stopinput)
        return 0

def populate_language_choicebox():
#populate language choices
    with open("languages.txt","r") as fp:
        contents = fp.readlines()
    contents = [x.rstrip() for x in contents]
    print contents
    for count, lang in enumerate(contents):
            ui.languagebox.addItem("")
            ui.languagebox.setItemText(count, lang)


def display_word(word):
    replacementsdict = {'.exclamationmark': '!', '.apostrophe': "'", '.questionmark': '?', '.comma': ',', '.colon': ':'}
    print replacementsdict.values()
    word_display = word[:word.rindex(".")]
    for sym in [sym for sym in replacementsdict.keys() if sym in word_display]:
        word_display = word_display.replace(sym,replacementsdict[sym])
    return word_display

def rdisplay_word(word_display):
    replacementsdict = {'.exclamationmark': '!', '.apostrophe': "'", '.questionmark': '?', '.comma': ',', '.colon': ':'}
    for sym in [sym for sym in replacementsdict.values() if sym in word_display]:
        key = (key for key,value in replacementsdict.items() if value==sym).next()
        word_display = word_display.replace(sym, key)
    return word_display

def nextpressed():
	global lessonpics, finished
	current_choices = [f for f in lessonpics if f not in finished]
	if len(current_choices) == 0:
		sys.exit()
	loadpicture(currentpath, current_choices[0])
	finished.append(current_choices[0])
	print "Next"
	

def loadpicture(currentpath, picfile):
    global soundfile
    #picture
    mypixmap = QtGui.QPixmap(os.path.join(currentpath,picfile))
    picheight = mypixmap.size().height()
    picwidth = mypixmap.size().width()
    HEIGHT = ui.label.size().height()
    WIDTH = ui.label.size().width()
    newheight, newwidth = getbestratio(HEIGHT, WIDTH, picheight, picwidth)
    ui.label.setPixmap(mypixmap.scaled(newheight, newwidth))
    
    #text
    print display_word(picfile)
    ui.word_display.text = display_word(picfile)
    ui.word_display.setHtml("<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Didact Gothic\'; font-size:24pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">"+ ui.word_display.text +"</p></body></html>")
    
    #sound
    soundfile = os.path.join(currentpath, "sounds")
    changedending = picfile[:picfile.rfind(".")] + ".wav"
    soundfile = os.path.join(soundfile, changedending)
    print soundfile, os.path.isfile(soundfile)
    playenglishsound()
    #set window title to currentpath

if __name__ == "__main__":
    import sys
    lessonsroot = "Lessons"
    currentlesson = "Personal Questions"
    currentpath = os.path.join(lessonsroot, currentlesson)
    app = QtGui.QApplication(sys.argv)
    MainWindow = QtGui.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    populate_language_choicebox()
    ui.initAudio(None)
    lessonpics = [f for f in os.listdir(currentpath) if os.path.isfile(os.path.join(currentpath,f))]
    print "lessonpics", lessonpics
    finished = []
    nextpressed()
    MainWindow.show()
    text = str(ui.languagebox.currentText())
    ui.languagebox.activated.connect(plang)
    ui.recordbutton.clicked.connect(record2)
    ui.soundbutton.clicked.connect(playenglishsound)
    ui.nextbutton.clicked.connect(nextpressed)
    ui.actionRecord.triggered.connect(record2)
    print text
    sys.exit(app.exec_())
