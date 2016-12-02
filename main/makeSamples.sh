opencv_createsamples -img side.jpg -bg bg.txt -info info/info.lst -pngoutput info -maxxangle 1.5 -maxyangle 1.5 -maxzangle 1.5 -num 1950 -bgcolor 255 -bgthresh 30
opencv_createsamples -info info/info.lst -num 1950 -w 20 -h 20 -vec positives.vec
opencv_traincascade -data data -vec positives.vec -bg bg.txt -numPos 1000 -numNeg 1000 -numStages 10 -w 20 -h 20
