import tkinter as tk
from tkinter import *
from PIL import Image, ImageTk
import random

# --- FUNCTIONS ---

def createWidget(parent, widgetType, **options):
    return widgetType(parent, **options)

def createDiceButton(parent, text, image):
    path = "images/" + text + ".png"
    return createWidget(
        parent, tk.Button,
        bd = 0, cursor = 'hand2',
        bg = container.cget("bg"),
        fg = "black", font = ("Arial", 12, "bold"),
        activebackground = container.cget("bg"),
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
wWidth, wHeight = 1100, 800
## Center the pop-up
centerX = (root.winfo_screenwidth() // 2) - (wWidth // 2)
centerY = (root.winfo_screenheight() // 2) - (wHeight // 2)
root.geometry(f"{wWidth}x{wHeight}+{centerX}+{centerY}")

# --- UI ---
## Content container 
container = createWidget(
    root, tk.Frame,
    height = 600, width = 1000,
    bg='lightblue', bd=3,
    highlightcolor='red',
    highlightbackground='black',
    highlightthickness=2,
)
container.pack()
container.pack_propagate(False)

## Displayed app title
appTitle = createWidget(
    container, tk.Label,
    text='TTRPG Digital Dice Roller',
    font=("Arial", 24, ), 
    bd = 0, bg = None
)
appTitle.pack(padx=50, pady=20)

## Create dice menu
diceDisplay = createWidget(
    container, tk.Frame,
    height = 160, width = 1000
)
diceDisplay.pack()
diceTypes = ["d4", "d6", "d8", "d10", "d12", "d20"]
diceButtons = {}
selected = None # no dice is selected when window opens
for die in diceTypes:
    photo = PhotoImage(file = "images/" + die + ".png")
    diceButton = createDiceButton(diceDisplay, die, photo)
    diceButton.pack(side = LEFT)
    diceButton.pack_propagate(False)
    diceButtons[die] = (diceButton,photo)

## Display result
resultLabel = createWidget(
    container, tk.Label,
    text='Result: ',
    font='50', bg='lightblue',
    bd=3, cursor='hand2',
    highlightcolor='red',
    highlightbackground='black',
    highlightthickness=2
)
resultLabel.pack(pady=5)

# --- MAIN ---
root.mainloop()