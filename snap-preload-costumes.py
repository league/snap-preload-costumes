#!/usr/bin/python3
# Usage: snap-preload-costumes.py megaman-*.png > project.xml

# Contributed to public domain by
# Christopher League <league@contrapunctus.net>

from PIL import Image
import base64
import os.path
import sys

prevID = 9

def main():
    global prevID
    costumes = [costume_item(f) for f in sys.argv[1:]]
    prevID += 1
    print(empty_xml % ('\n'.join(costumes), prevID))

def costume_item(fileName):
    global prevID
    name, ext = os.path.splitext(os.path.basename(fileName))
    with open(fileName, mode='rb') as file:
        with Image.open(fileName) as image:
            size = image.size
            center_x = size[0]//2
            center_y = size[1]//2
            data = file.read()
            bits = base64.b64encode(data).decode('ascii')
            prevID += 1
            return (
                """<item><costume name="%s" center-x="%d" center-y="%d"
                image="data:image/png;base64,%s" id="%d"/></item>""" %
                (name, center_x, center_y, bits, prevID))

empty_xml = """<project name="empty" app="Snap! 4.0, http://snap.berkeley.edu" version="1">
  <notes/>
  <thumbnail>data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAKAAAAB4CAYAAAB1ovlvAAABrElEQVR4nO3SQUqCYQBFUfcijsVd6OwHVym4I8F9COoXBUVBGkRw0c6BN3+DOxsQmtUH+N8ESEqApARISoCkBEhKgKQESEqApARISoCkBEhKgKQESEqApARISoCkBEhKgKQESEqApARISoCkBEhKgKQESEqApARISoCkBEhKgKQESEqApARISoCkBEhKgKQESEqApARISoCkBEhKgKQESEqApARISoCkBEhKgKQESEqApARISoCkBEhKgKQESEqANywWi7Hf7+sbT0+Ad0zT9LHVajWOx2N96ekI8I7r9folwvdtt9ux2WzG+XyuLz48Af7guwBft16vx+l0eouU3xPgHZ+DWy6X43A4CO6PCfCG+Xw+drvduFwu9ZWnJkBSAiQlQFICJCVAUgIkJUBSAiQlQFICJCVAUgIkJUBSAiQlQFICJCVAUgIkJUBSAiQlQFICJCVAUgIkJUBSAiQlQFICJCVAUgIkJUBSAiQlQFICJCVAUgIkJUBSAiQlQFICJCVAUgIkJUBSAiQlQFICJCVAUgIkJUBSAiQlQFICJCVAUgIkJUBSAiQlQFIvMO2vX332to0AAAAASUVORK5CYII=</thumbnail>
  <stage name="Stage" width="480" height="360" costume="0" tempo="60" threadsafe="false" lines="round" codify="false" scheduled="false" id="1">
    <pentrails>data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAeAAAAFoCAYAAACPNyggAAACtUlEQVR4nO3BMQEAAADCoPVPbQwfoAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA+Bo3+AAF/RMkcAAAAAElFTkSuQmCC</pentrails>
    <costumes>
      <list id="2"/>
    </costumes>
    <sounds>
      <list id="3"/>
    </sounds>
    <variables/>
    <blocks/>
    <scripts/>
    <sprites>
      <sprite name="Sprite" idx="1" x="0" y="0" heading="90" scale="1" rotation="1" draggable="true" costume="0" color="80,80,80" pen="tip" id="8">
        <costumes>
          <list id="9">
            %s
          </list>
        </costumes>
        <sounds>
          <list id="%d"/>
        </sounds>
        <variables/>
        <blocks/>
        <scripts/>
      </sprite>
    </sprites>
  </stage>
  <hidden/>
  <headers/>
  <code/>
  <blocks/>
  <variables/>
</project>
"""

if __name__ == "__main__":
    main()
