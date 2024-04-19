### PNG Stacker

Various tools to generate new .png file based on stacking layers of .png files with transparent background.

Boiler code from this [tutorial](https://youtu.be/o0qNS_pOVqw?si=gvpyi6HtBye5XXHA).

Note: Current version is a rough rough build requiring precise path to images and sequence.

Simple cmd via Typer:
```
python <path to make_blobert.py> \ 
-i <path to first trait image> \ 
-i <path to 2nd trait image> \
...
-o <path to output image>
```