import cv2
import numpy as np
from PIL import Image

def faceDetect():
    faceCascade = cv2.CascadeClassifier('Pictures/haarcascade_frontalface_default.xml')
    img = cv2.imread('Pictures/feed.png')
    imgGray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    try:
        faces = faceCascade.detectMultiScale(imgGray,1.5,4)
        for (x,y,w,h) in faces:
            cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)

    #the following returns the X and Y values which we will use to place the hat on the figure (Stored in a Numpy Array)
        fx = faces [0,0]
        fy = faces [0,1]
        return [fx, fy]
    except TypeError:
        #this will only run if there is no face found with OpenCV
        print("ERROR: FACE NOT FOUND")
        return [1000,1000]


def addCowboyHat():
    # Opening the primary image (used in background)
    headVals = faceDetect()
    img1 = Image.open(r"Pictures/feed.png")

    #We must now tweak headVals
    headVals[0] -= 115
    headVals[1] -= 170

    # Opening the secondary image (overlay image)
    img2 = Image.open(r"Pictures/Cowboy-hat.jpg")
    img2 = img2.resize((500,300))
    transpColor = Image.open(r"Pictures/Cowboy-hat-mask.jpg")
    transpColor = transpColor.resize((500,300))

    #then you mast add the alpha channel
    transpColor = transpColor.convert('L')  # greyscale
    img2.putalpha(transpColor)

    # Pasting img2 image on top of img1
    img1.paste(img2, headVals, mask = transpColor)

    img1.save(r"Pictures/feed.png")
    return 0

def addBandana():
    # Opening the primary image (used in background)
    headVals = faceDetect()
    img1 = Image.open(r"Pictures/feed.png")

    #We must now tweak headVals
    headVals[0] -= 155
    headVals[1] += 100

    # Opening the secondary image (overlay image)
    img2 = Image.open(r"Pictures/red-bandana.jpg")
    img2 = img2.resize((600,400))
    transpColor = Image.open(r"Pictures/red-bandana-mask.jpg")
    transpColor = transpColor.resize((600,400))

    #then you mast add the alpha channel
    transpColor = transpColor.convert('L')  # greyscale
    img2.putalpha(transpColor)

    # Pasting img2 image on top of img1
    img1.paste(img2, headVals, mask = transpColor)


    #img1.show()
    #/\ FOR DEBUGGING

    img1.save(r"Pictures/feed.png")
    return 0

def addAltCowboyHat():
    # Opening the primary image (used in background)
    headVals = faceDetect()
    img1 = Image.open(r"Pictures/feed.png")

    #We must now tweak headVals
    headVals[0] -= 155
    headVals[1] -= 170

    # Opening the secondary image (overlay image)
    img2 = Image.open(r"Pictures/black-cowboy-hat.jpg")
    img2 = img2.resize((600,300))
    transpColor = Image.open(r"Pictures/black-cowboy-hat-mask.jpg")
    transpColor = transpColor.resize((600,300))

    #then you mast add the alpha channel
    transpColor = transpColor.convert('L')  # greyscale
    img2.putalpha(transpColor)

    # Pasting img2 image on top of img1
    img1.paste(img2, headVals, mask = transpColor)

    #img1.show()
    # /\ FOR DEBUGGING

    img1.save(r"Pictures/feed.png")
    return 0

def addMustache():
    # Opening the primary image (used in background)
    headVals = faceDetect()
    img1 = Image.open(r"Pictures/feed.png")

    #We must now tweak headVals
    headVals[0] -= 5
    headVals[1] += 100

    # Opening the secondary image (overlay image)
    img2 = Image.open(r"Pictures/handlebar-mustache.jpg")
    img2 = img2.resize((275,200))
    transpColor = Image.open(r"Pictures/handlebar-mustache-mask.jpg")
    transpColor = transpColor.resize((275,200))

    #then you mast add the alpha channel
    transpColor = transpColor.convert('L')  # greyscale
    img2.putalpha(transpColor)

    # Pasting img2 image on top of img1
    img1.paste(img2, headVals, mask = transpColor)


    #img1.show()
    #/\ FOR DEBUGGING

    img1.save(r"Pictures/feed.png")
    return 0

def addCigar():
    # Opening the primary image (used in background)
    headVals = faceDetect()
    img1 = Image.open(r"Pictures/feed.png")

    #We must now tweak headVals
    headVals[0] += 20
    headVals[1] += 200

    # Opening the secondary image (overlay image)
    img2 = Image.open(r"Pictures/cigar.jpg")
    img2 = img2.resize((100,100))
    transpColor = Image.open(r"Pictures/cigar-mask.jpg")
    transpColor = transpColor.resize((100,100))

    #then you mast add the alpha channel
    transpColor = transpColor.convert('L')  # greyscale
    img2.putalpha(transpColor)

    # Pasting img2 image on top of img1
    img1.paste(img2, headVals, mask = transpColor)


    #img1.show()
    #/\ FOR DEBUGGING

    img1.save(r"Pictures/feed.png")
    return 0

#faceDetect()
#addCowboyHat()
#addBandana()
#addAltCowboyHat()
#addMustache()
#addCigar()