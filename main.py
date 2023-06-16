from tkinter import *
import posterCompiler
import webcam
import os

outputPoster = posterCompiler.PC('Pictures\\WantedBG.png')
#pic = camera.camclass()
root = Tk()
root.iconbitmap('Pictures\\CowboyHat.ico')
root.title("Outlaw Alley")
root.geometry("1280x1000")
root.resizable(False,False)
backgroundimg = PhotoImage(file= 'Pictures\\PaperBG.png')
background=Label(root, image=backgroundimg, bg = 'black')
background.place(x = 0,y =0)



#Live Videofeed is a go.
camfile = webcam.Box(root, width=750, height=550)
camfile.show_frames()  # Show the created Box

creatortag = Label (root, text= 'Patrick Madonna 2023', font = ('Stencil',10), bg = '#D2B48C', fg = '#1a0d00')
creatortag.place(x=10, y=975)

versionNo = Label (root, text= 'V 1.0.0', font = ('Stencil',10), bg = '#D2B48C', fg = '#1a0d00')
versionNo.place(x= 1200, y= 975)

title = Label (root, text= 'Outlaw Alley', font = ('Stencil',120), bg = '#D2B48C', fg = '#1a0d00')
titleOL = Label(root, text="What's your \n Outlaw Name?".center(20), font=('Stencil', 85), bg='#D2B48C', fg='#1a0d00')
titleBA = Label(root, text ='How much is your \n Bounty?'.center(10), font = ('Stencil', 70), bg ='#D2B48C', fg ='#1a0d00')
titleSC = Label(root, text='SAY YEEHAW! \n BANDIT TO BE! ', font=('Stencil', 80), bg='#D2B48C', fg='#1a0d00')
titleRT = Label(root, text= 'YEEHAW COME \n AGAIN!!', font=('Stencil', 85), bg='#D2B48C', fg='#1a0d00')


title.place(x = 75, y = 50)
subTitle = Label (root, text= 'The Wanted Poster Generator',font = ('Stencil',30),bg = '#D2B48C', fg = '#1a0d00')
subTitle.place(x = 300, y = 225)

nameEntry = Entry(root, font=('Arial', 45))
bountyEntry = Entry(root, font=('Arial', 45))

startButton = Button(root, text = "Yeehaw (Start)", font = ('Stencil', 20), height = 2, width = 30,bg = '#D2B48C', fg = '#1a0d00', command=lambda: outlawName())
buttonOL = Button(root, text ="Enter", font = ('Stencil', 20), height = 2, width = 10, bg ='#D2B48C', fg ='#1a0d00', command=lambda: bountyAmtEntry())
buttonBA = Button(root, text="Enter", font=('Stencil', 20), height=2, width=10, bg='#D2B48C', fg='#1a0d00', command=lambda: sayCheese())
buttonSC = Button(root, text="Take Picture", font=('Stencil', 20), height=2, width=30, bg='#D2B48C', fg='#1a0d00', command=lambda: takePic())
buttonRT = Button(root, text="Restart", font=('Stencil', 25), height=3, width=30, bg='#D2B48C', fg='#1a0d00', command=lambda: restart())
startButton.place(x=350, y=875)


def outlawName():
    titleOL.place(x=200, y=30)
    #this is to avoid having to restart the program each time
    title.place(x=10000,y=10000)
    subTitle.place(x=10000, y= 10000)
    startButton.place(x=10000, y = 10000)
    nameEntry.place(x = 280, y = 910)
    buttonOL.place(x = 775, y = 900)

def bountyAmtEntry():
    outputPoster.nameGet(nameEntry.get())
    nameEntry.delete(0, "end")
    titleOL.place(x= 10000, y= 10000)
    titleBA.place(x = 180, y = 50)
    bountyEntry.place(x=280, y=910)
    buttonOL.place(x= 10000, y= 10000)
    buttonBA.place(x=775, y=900)

def sayCheese():
    #Add the photo stuff later, this is just GUI
    outputPoster.bountyGet(bountyEntry.get())
    bountyEntry.delete(0, "end")
    bountyEntry.place(x= 10000, y= 10000)
    titleBA.place(x=10000, y= 10000)
    titleSC.place(x=235, y=20)
    buttonBA.place(x=10000, y=10000)
    buttonSC.place(x=350, y=900)

def takePic():
    titleSC.place(x=10000, y=10000)
    buttonSC.place(x=10000, y=10000)
    buttonRT.place(x=292, y=875)
    titleRT.place(x=225, y=10)
    camfile.take_pic()
    outputPoster.compilepost()
    os.startfile('Pictures\\FinalPoster.png', 'print')


def restart():
    buttonRT.place(x=10000, y=10000)
    titleRT.place(x= 10000, y= 10000)
    titleOL.place(x=200, y=30)
    nameEntry.place(x = 280, y = 910)
    buttonOL.place(x = 775, y = 900)
    #os.execv('main.py', sys.argv)

#the camera script will take a picture of the feed
mainloop()
