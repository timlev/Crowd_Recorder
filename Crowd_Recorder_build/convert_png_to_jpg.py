#Converts all images in Lessons to .png

import os
import Image

print "*************************************\n" * 5
print os.path.basename(os.getcwd())

basedir = "dist/recording.app/Contents/Resources"
basedir = os.path.join(basedir, "Lessons")
print os.path.abspath(basedir)

for r, d, f in os.walk(basedir):
    if "sounds" in d:
        for item in f:
            filename, ext = os.path.splitext(os.path.join(r,item))
            print filename, ext
            if item.startswith("."):
               print "Removing", os.path.join(r,item)
               os.remove(os.path.join(r, item))
            elif not item.endswith(".png"):
                im = Image.open(os.path.join(r, item))
                im.save(filename + ".png")
                os.remove(filename + ext)
