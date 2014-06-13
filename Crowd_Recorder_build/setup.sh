python setup.py py2app;
cp ~/GitProjects/Crowd_Recorder/recording/languages.txt dist/recording.app/Contents/Resources/;
cp -R ~/GitProjects/Crowd_Recorder/recording/Lessons dist/recording.app/Contents/Resources/;
python convert_png_to_jpg.py;
