import tkinter as tk
from tkinter import *
from PIL import Image, ImageTk
import random

# --- FUNCTIONS ---

def createWidget(parent, widgetType, **options):
    return widgetType(parent, **options)

def createDiceButton(parent, text, image):
    return createWidget(
        parent, tk.Button,
        bd = 0, cursor = 'hand2',
        bg = root.cget("bg"),
        fg = "black", font = ("Arial", 12, "bold"),
        activebackground = root.cget("bg"),
        activeforeground = None,
        relief = "flat",
        command=lambda d=die: selectDice(d),
        image = image, text = text,
        compound = TOP,
        padx = 15, pady = 5
    )

def selectDice(type):
    global selected
    selected = type
    roll()

def roll():
    if selected is None:
        resultLabel.config(text="Select your dice first")
        return
    result = random.randint(1,int(selected[1:]))
    resultLabel.config(text=f"{result}")


# --- CREATE WINDOW ---
root = createWidget(None, tk.Tk)
root.title("Dice Roller")
wWidth, wHeight = 1200, 1000
root.config(bg = '#1E0F11')
## Center the pop-up
centerX = (root.winfo_screenwidth() // 2) - (wWidth // 2)
centerY = (root.winfo_screenheight() // 2) - (wHeight // 2)
root.geometry(f"{wWidth}x{wHeight}+{centerX}+{centerY}")

# --- UI ---
## Load Title Photo
titlePhoto = PhotoImage(file = "assets/images/upperUI.png")
titleImage = createWidget(
    root, tk.Label,
    image = titlePhoto,
    bg = root.cget("bg")
)
titleImage.photo = titlePhoto
titleImage.pack(pady = (50, 0))

## Create dice menu
diceDisplay = createWidget(
    root, tk.Frame,
    height = 160, width = 1000
)
diceDisplay.pack()
diceTypes = ["d4", "d6", "d8", "d10", "d12", "d20"]
diceButtons = {}
selected = None # no dice is selected when window opens
for die in diceTypes:
    photo = PhotoImage(file = "assets/images/" + die + ".png")
    diceButton = createDiceButton(diceDisplay, die, photo)
    diceButton.pack(side = LEFT)
    diceButton.pack_propagate(False)
    diceButtons[die] = (diceButton,photo)
diceDisplay.pack(pady = 10)

## Display result
resultLabel = createWidget(
    root, tk.Label,
    text='Result: ',
    font='50', bg='lightblue',
    bd=3, cursor='hand2',
    highlightcolor='red',
    highlightbackground='black',
    highlightthickness=2
)
resultLabel.pack(pady = (20,0))

## Load Background photo
backgroundPhoto = PhotoImage(file = "assets/images/lowerUI.png")
backgroundImage = createWidget(
    root, tk.Label,
    image = backgroundPhoto,
    bg = root.cget("bg")
)
backgroundImage.photo = backgroundPhoto
backgroundImage.pack(pady = (50, 0))

# --- MAIN ---
root.mainloop()