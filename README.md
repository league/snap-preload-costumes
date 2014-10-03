snap-preload-costumes
=====================

Creates an importable [Snap](http://snap.berkeley.edu/) project containing a set of costumes for the first sprite.

First split a sprite sheet using an ImageMagick command like this:

````
convert robotboy.png -crop 150x150 'robotboy-%02d.png'
````

Then you can run this Python script to generate the XML file containing those split images as costumes:

````
./snap-preload-costumes.py robotboy-*.png > robotboy.xml
````

