python setup.py py2app;
cp ../recording/languages.txt dist/recording.app/Contents/Resources/;
cp -R ../recording/Lessons dist/recording.app/Contents/Resources/;
python convert_png_to_jpg.py;
