import tkinter
import asyncio
import random as rd
from PIL import Image, ImageTk
from itertools import count, cycle


rd.randint(1,6)
Dice_Count =None
counter=0
# load images for dice
dice =["image\\dice1.png", "image\\dice2.png", 
       "image\\dice3.png", "image\\dice4.png", 
       "image\\dice5.png", "image\\dice6.png", ]


class ImageLabel(tkinter.Label):
    """
    A Label that displays images, and plays them if they are gifs
    :im: A PIL Image instance or a string filename
    """
    def load(self, im):
        if isinstance(im, str):
            im = Image.open(im)
            frames = []

        try:
            for i in count(1):
                frames.append(ImageTk.PhotoImage(im.copy()))
                im.seek(i)
        except EOFError:
            pass
        self.frames = cycle(frames)

        try:
            self.delay = im.info['duration']
        except:
            self.delay = 100

        if len(frames) == 1:
            self.config(image=next(self.frames))
        else:
            self.next_frame()

    def unload(self):
        self.config(image=None)
        self.frames = None

    def next_frame(self):
        global counter
        if(counter <23):
            counter+=1
            if self.frames:
                self.config(image=next(self.frames))
                self.after(self.delay, self.next_frame)
                rd.randint(1,6)
                roll()        
        

def roll():
    
    u_input =   int(Number_of_Dice.get())

    if u_input == 1:
        image1 = ImageTk.PhotoImage(Image.open(rd.choice(dice)))
    
        dice_one = tkinter.Label(StartScreen, image = image1)
        dice_one.pack()
        dice_one.place(x = 300, y = 550)
    
        dice_one.configure(image = image1)
        dice_one.image = image1

    elif u_input == 2:
        image1 = ImageTk.PhotoImage(Image.open(rd.choice(dice)))
        image2 = ImageTk.PhotoImage(Image.open(rd.choice(dice)))
        
        dice_one = tkinter.Label(StartScreen, image = image1)
        dice_one.pack()
        dice_one.place(x = 200, y = 550)
        
        dice_two = tkinter.Label(StartScreen, image = image2)
        dice_two.pack()
        dice_two.place(x = 400, y = 550)
    
        dice_one.configure(image = image1)
        dice_one.image = image1
        
        dice_two.configure(image = image2)
        dice_two.image = image2
    
    elif u_input == 3:
        image1 = ImageTk.PhotoImage(Image.open(rd.choice(dice)))
        image2 = ImageTk.PhotoImage(Image.open(rd.choice(dice)))
        image3 = ImageTk.PhotoImage(Image.open(rd.choice(dice)))
        
        dice_one = tkinter.Label(StartScreen, image = image1)
        dice_one.pack()
        dice_one.place(x = 100, y = 550)
        
        dice_two = tkinter.Label(StartScreen, image = image2)
        dice_two.pack()
        dice_two.place(x = 300, y = 550)
        
        dice_th = tkinter.Label(StartScreen, image = image3)
        dice_th.pack()
        dice_th.place(x = 500, y = 550)
    
        dice_one.configure(image = image1)
        dice_one.image = image1

        dice_two.configure(image = image2)
        dice_two.image = image2
        
        dice_th.configure(image = image3)
        dice_th.image = image3


def Play():
    global label_text
    try:
        Dice_Count = int(Number_of_Dice.get())
        if(Dice_Count <1 or Dice_Count>3) :    
            Warning_Message.config(text = 'You should enter at most 3 or at least 1 number of dice')
        else:
            Warning_Message.config(text = '')
            global counter
            counter=0
            lbl.load('gifs\\giphy.gif')
    except:
        Warning_Message.config(text = 'You should enter the number of dice you want to play with at most 3 or at least 1')




# -------- StartScreen ----------
StartScreen = tkinter.Tk()
StartScreen.title("Dice Rolling")
StartScreen.geometry("800x800")
label_text = ""


welcome_Message = tkinter.Label(StartScreen, text="Welcome to Dice Rolling!", font=("Algerian", 20, "bold"))

Info = tkinter.Label(StartScreen,
                         text="Please enter the number of dice you want to play with: ",
                         font=("Algerian", 12, "bold"))

Number_of_Dice = tkinter.Entry(StartScreen, width=30, font=("Algerian", 12))

Dice_Roll_Button = tkinter.Button(StartScreen, text="Dice Roll", width=10, height=2, command=Play, font=("Algerian", 12))
Dice_Roll_Button.place(x=270, y=170)

Exit_Button = tkinter.Button(StartScreen, text="Quit Game", width=10, height=2, command=quit, font=("Algerian", 12))
Exit_Button.place(x=420, y=170)

Warning_Message = tkinter.Label(StartScreen, text=label_text, font=("Algerian", 12), fg="red")



welcome_Message.pack(pady=10)
Info.pack(pady=10)
Number_of_Dice.pack(pady=10)
Warning_Message.pack()
lbl = ImageLabel(StartScreen)
lbl.pack(pady=70)
StartScreen.mainloop()