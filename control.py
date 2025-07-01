from pynput.mouse import Controller as MouseController
from pynput.keyboard import Controller as KeyboardController


def controlMouse():
    mouse=MouseController()
    mouse.position=(500,200)

def controlKeyboard():
    keyboard=KeyboardController()
    keyboard.type("I am Stronger!")

controlKeyboard()

