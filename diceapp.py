import tkinter as tk
from tkinter import *
from PIL import Image, ImageTk
import random
import ctypes

# --- FUNCTIONS ---

def loadFont(path):
    FR_PRIVATE = 0x10
    FR_NOT_ENUM = 0x20
    ctypes.windll.gdi32.AddFontResourceExW(path, FR_PRIVATE, 0)

def createWidget(parent, widgetType, **options):
    return widgetType(parent, **options)

def createDiceButton(parent, text, image):
    return createWidget(
        parent, tk.Button,
        bd = 0, cursor = 'hand2',
        bg = root.cget("bg"),
        fg = "#6a070b", font = ("Ithaca", 18),
        activebackground = root.cget("bg"),
        activeforeground = "#350408",
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
root.iconphoto(True, tk.PhotoImage(file="assets/images/d4.png"))
loadFont("assets/Ithaca-LVB75.ttf")

# --- UI ---
## Load Title Photo
titlePhoto = PhotoImage(file = "assets/images/upperUI.png")
titleImage = createWidget(
    root, tk.Label,
    image = titlePhoto,
    bg = root.cget("bg")
)
titleImage.photo = titlePhoto
titleImage.pack(pady = (75, 30))

## Create dice menu
diceDisplay = createWidget(
    root, tk.Frame,
    bg = root.cget("bg"),
    height = 160, width = 1000
)
diceDisplay.pack()
diceTypes = ["d4", "d6", "d8", "d10", "d12", "d20"]
diceButtons = {}
selected = None # no dice is selected when window opens
for die in diceTypes:
    photo = PhotoImage(file = "assets/images/" + die + ".png")
    diceButton = createDiceButton(diceDisplay, die, photo)
    diceButton.pack(side = LEFT, padx = 5)
    diceButton.pack_propagate(False)
    diceButtons[die] = (diceButton,photo)
diceDisplay.pack()

## Display result
resultLabel = createWidget(
    root, tk.Label,
    bg = root.cget("bg"), bd = 0, 
    text = 'Select a dice to start',
    fg = "#6a070b", font = ("Ithaca", 40)
)
resultLabel.pack(pady = (50,0))

## Load Background photo
backgroundPhoto = PhotoImage(file = "assets/images/lowerUI.png")
backgroundImage = createWidget(
    root, tk.Label,
    image = backgroundPhoto,
    bg = root.cget("bg")
)
backgroundImage.photo = backgroundPhoto
backgroundImage.pack()

# --- MAIN ---
root.mainloop()