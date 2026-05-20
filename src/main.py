import pyautogui
from enum import Enum
import pyautogui
import time
import keyboard

topLeftX = 265 #this is in the top left of the top left cell not outside the field of cells
topLeftY = 233

#bottomRightX = 776 and bottomRightY = 744 this is for 16 by 16 cells
bottomRightX = 0
bottomRightY = 0

#cell size is 32 by 32 if website size is 80% and min sweeper display is 200%
# - is not down, 0 is 0 bombs nearby same for 1 and 2 etc, 8 is flag

#513 190 to check if we died
#521 176 to check if we won

#19 and 20 on X and 19 20 21 22 on Y to check color


def Setup():
    print("give board size. (first horizontal then vertical)")
    print("example: 15x30")
    size = input("board size: ")
    boardSize = size.split("x")

    if len(boardSize) != 2 or not boardSize[0].isdigit() or not boardSize[1].isdigit():
        print("you need to give numbers in format: (horizontal size)x(vertical size)")
        return Setup()

    bottomRightX = topLeftX + (boardSize[0] * 32 - 1)
    bottomRightY = topLeftY + (boardSize[1] * 32 - 1)
    board = [["-" for _ in range(int(boardSize[0]))] for _ in range(int(boardSize[1]))]
    return board

board = Setup()

def getPixelToCheck(x, y)
    xPos = (topLeftX + (x * 32)) + 20
    yPos = (topLeftY + (y * 32)) + 20
    return xPos, yPos

def GetState(x, y):
    screenshot = pyautogui.screenshot()
    xPos, yPos = getPixelToCheck(x, y)
    pixel = screenshot.getpixel((xPos, yPos))
    if screenshot.getpixel((xPos - 20, yPos - 20)) = (255, 255, 255) and pixel = (189, 189, 189):
        return "-"
    elif screenshot.getpixel((xPos - 20, yPos - 20)) = (255, 255, 255) and pixel = (0, 0, 0):
        return "9"
    elif pixel = (189, 189, 189):
        return "0"
    elif pixel = (0, 0, 255):
        return "1"
    elif pixel = (0, 123, 0):
        return "2"
    elif pixel = (255, 0, 0):
        return "3"
    elif pixel = (0, 0, 123):
        return "4"
    elif pixel = (123, 0, 0):
        return "5"
    elif pixel = (0, 123, 123):
        return "6"
    elif pixel = (0, 0, 0):
        return "7"
    elif pixel = (123, 123, 123):
        return "8"