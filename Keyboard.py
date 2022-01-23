from PIL import Image, ImageDraw, ImageFont
import math

font_path = "C:/Fonts/InputSans/InputSans/InputSans-Regular.ttf"
myfont = ImageFont.truetype(font_path, 16)
layout = []
startingPos = {}
frequencyMap = {}
coord_to_freq = {}
posToLetter = {}

def createFreqMap(fileName):

    with open(fileName,"r") as f:
        lines = f.readlines()
        for line in lines:
            line = line.split("|")
            letter = line[0]
            frequency = float(line[1])
            frequencyMap[letter] = frequency
    
    print(frequencyMap)

class Coordinates:
    def __init__(self, x, y):
        self.x = x
        self.y = y

def createKeyboard():

    width = 1020
    height = 300
    tileSize= 100
    img = Image.new('RGB', (width, height))
    draw = ImageDraw.Draw(img)
    #row 1
    for i in range(0,1000):
        for j in range(tileSize):
            if((i == 0 or (i+1) % tileSize == 0) or ((j == 0 or j == (tileSize-1)))):
                img.putpixel((i,j), (255,255,255))
            if(j == 50 and i % tileSize == 50):
                coord = Coordinates(i,j)
                layout.append((coord.x,coord.y))
                draw.text((i,j),"*",font = myfont, fill = (255,255,255))
    #row 2
    for i in range(25, width):
        for j in range(tileSize, tileSize*2):
            if((i == 25 or i == (width-1) or (i+1) % tileSize == 25) or (j == 100 or j == ((tileSize*2)-1))):
                img.putpixel((i,j), (255,255,255))
            if(j == 150 and i % tileSize == 75):
                coord = Coordinates(i,j)
                layout.append((coord.x,coord.y))
                draw.text((i,j),"*",font = myfont, fill = (255,255,255))
    #row 3
    for i in range(85, width-235):
        for j in range(tileSize*2, tileSize*3):
            if((i == 85 or i == (width-1) or (i+1) % tileSize == 85) or (j == 200 or j == ((tileSize*3)-1))):
                img.putpixel((i,j), (255,255,255))
            if(j == 250 and i % tileSize == 35):
                coord = Coordinates(i,j)
                layout.append((coord.x,coord.y))
                draw.text((i,j),"*",font = myfont, fill = (255,255,255))

    img.save('Keyboard.png')
    print(layout)

def getDist(pos1, pos2):

    xDist = abs(pos2[0] - pos1[0])
    yDist = abs(pos1[1] - pos2[1])
    dist = math.sqrt((xDist * xDist) + (yDist * yDist))
    return dist

def drawKeyboard():

    width = 1020
    height = 300
    finalImg = Image.new('RGB', (width, height))
    finalDraw = ImageDraw.Draw(finalImg)

    for i in range(len(layout)):
        finalDraw.text((layout[i].x,layout[i].y),finalOrder[i], fill = (255,255,255))
    finalImg.save('Keyboard.png')

def mapLetterToCoord():
    posToNum = {}
    for pos1 in layout:
        totalDist = 0
        for pos2 in startingPos:
            dist = getDist(pos1, pos2) * startingPos[pos2]
            totalDist += dist

        posToNum[pos1] = totalDist
    
    a = sorted(posToNum.items(), key=lambda x: x[1])

    count = 0
    for letter in frequencyMap:
        posToLetter[a[count][0]] = letter
        count += 1
    print(posToLetter)
                

#assign a val to each finger position on keyboard to break ties for letters by creating a preference value for each finger
def createStartingPos():
    for i in range(len(layout)):
        if(i>=10 and i<=13):
            startingPos[layout[i]] = 1 +((13-i)/10000)+ 0.00005
        elif(i>=16 and i<=19):
            startingPos[layout[i]] = 1 +((i-16)/10000)
    
    print(startingPos)

def createFinalKeyboard():

    width = 1020
    height = 300
    tileSize= 100
    img = Image.new('RGB', (width, height))
    draw = ImageDraw.Draw(img)
    #row 1
    for i in range(0,1000):
        for j in range(tileSize):
            if((i == 0 or (i+1) % tileSize == 0) or ((j == 0 or j == (tileSize-1)))):
                img.putpixel((i,j), (255,255,255))
            if(j == 50 and i % tileSize == 50):
                coord = Coordinates(i,j)
                layout.append((coord.x,coord.y))
                draw.text((i,j),posToLetter[(i,j)],font = myfont, fill = (255,255,255))
    #row 2
    for i in range(25, width):
        for j in range(tileSize, tileSize*2):
            if((i == 25 or i == (width-1) or (i+1) % tileSize == 25) or (j == 100 or j == ((tileSize*2)-1))):
                img.putpixel((i,j), (255,255,255))
            if(j == 150 and i % tileSize == 75):
                coord = Coordinates(i,j)
                layout.append((coord.x,coord.y))
                draw.text((i,j),posToLetter[(i,j)],font = myfont, fill = (255,255,255))
    #row 3
    for i in range(85, width-235):
        for j in range(tileSize*2, tileSize*3):
            if((i == 85 or i == (width-1) or (i+1) % tileSize == 85) or (j == 200 or j == ((tileSize*3)-1))):
                img.putpixel((i,j), (255,255,255))
            if(j == 250 and i % tileSize == 35):
                coord = Coordinates(i,j)
                layout.append((coord.x,coord.y))
                draw.text((i,j),posToLetter[(i,j)],font = myfont, fill = (255,255,255))

    img.save('Keyboard.png')


createKeyboard()
print()
createFreqMap("letterFrequency.txt")
print()
createStartingPos()
print()
mapLetterToCoord()
createFinalKeyboard()


#drawKeyboard()




