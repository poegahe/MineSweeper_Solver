import pyautogui
from enum import Enum

#screenshot = pyautogui.screenshot()
#pixel = screenshot.getpixel((250, 250))
#print(pixel)
class States(Enum):
    UNKNOWN = 1
    BLANK = 2
    FLAG = 3
    ONW = 4
    TWO = 5
    THREE = 6
    FOUR = 7
    FIVE = 8
    SIX = 9
    SEVEN = 10
    EIGHT = 11

def Setup():
    print("give board size. (first horizontal then vertical)")
    print("example: 15x30")
    size = input("board size: ")
    boardSize = size.split("x")

    if len(boardSize) != 2 or not boardSize[0].isdigit() or not boardSize[1].isdigit():
        print("you need to give numbers in format: (horizontal size)x(vertical size)")
        return Setup()

    board = [[States.UNKNOWN for _ in range(int(boardSize[0]))] for _ in range(int(boardSize[1]))]
    return board