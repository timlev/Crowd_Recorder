import os


soundsdir = os.path.abspath(os.path.join("..","sounds"))
transdir = os.path.abspath(os.path.join("..","Translations"))
eng_files = [x for x in os.listdir(transdir) if x.startswith("English")]


for f in eng_files:
    newname = f.replace("English_","")
    os.rename(os.path.join(transdir,f), os.path.join(soundsdir,newname))
