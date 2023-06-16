import cv2

class PC:
    # add name and bounty later and place this class at the end of main.p file
    def __init__(self,posterBase):
        self.posterBase = posterBase
        self.name = ""
        self.bounty = ""
        #this establishes the background of the file

    def nameGet(self, name):
        self.name = name

    def bountyGet(self, bounty):
        self.bounty = bounty

    def compilepost(self):
        background = cv2.resize(cv2.imread(self.posterBase, 1), (0, 0), fx=0.5, fy=0.85)
        #Put all of the Fixed Text here
        cv2.putText(background, "WANTED", (85, 175), cv2.FONT_HERSHEY_TRIPLEX,6,(20,20,20), 5)
        cv2.putText(background, "DEAD or ALIVE", (210, 250), cv2.FONT_HERSHEY_TRIPLEX, 2, (60, 50, 75), 5)
        cv2.putText(background, "REWARD", (225, 975), cv2.FONT_HERSHEY_TRIPLEX, 4, (40, 50, 75), 5)



        #Put all of the Inputted Text and Picture Here
        cv2.putText(background, self.name, (250, 725), cv2.FONT_HERSHEY_TRIPLEX, 3, (20, 20, 20), 3)
        cv2.putText(background, "$" + self.bounty + "$", (300, 850), cv2.FONT_HERSHEY_TRIPLEX, 3, (20, 20, 20), 3)
        pic = cv2.resize(cv2.imread('Pictures\\feed.png',1), (0,0), fx=1, fy=0.9)
        x_offset = 165
        y_offset = 200
        background[y_offset:y_offset + pic.shape[0], x_offset:x_offset + pic.shape[1]] = pic



        #Put all of the markup/decorations here
        cv2.line(background, (85,195), (885, 195), (0,0,0), 5)
        cv2.line(background, (85, 25), (885, 25), (0, 0, 0), 5)
        cv2.line(background, (85, 185), (885, 185), (0, 0, 0), 5)
        cv2.line(background, (85, 750), (885, 750), (0, 0, 0), 5)

        #making a star made out of 5 lines
        cv2.line(background, (100,875), (200,975), (0,0,0),5)
        cv2.line(background, (200,975), (50,925), (0,0,0), 5)
        cv2.line(background, (50,925), (150, 875), (0,0,0), 5)
        cv2.line(background, (150,875), (50, 1025), (0, 0, 0), 5)
        cv2.line(background, (50, 1025), (100, 875), (0, 0, 0), 5)

        #making a star made out of 5 lines
        cv2.line(background, (825,860), (925,960), (0,0,0),5)
        cv2.line(background, (925,960), (775,910), (0,0,0), 5)
        cv2.line(background, (775,910), (875, 860), (0,0,0), 5)
        cv2.line(background, (875,860), (775, 1010), (0, 0, 0), 5)
        cv2.line(background, (775, 1010), (825, 860), (0, 0, 0), 5)
        #this follwoing line should be taken out later as it's only meant for debugging

        wantedPosterFin = background.copy()
        cv2.imshow('Wanted Poster', background)
        cv2.imwrite('Pictures\\FinalPoster.png', wantedPosterFin)



