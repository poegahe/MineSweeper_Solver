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

#20 on X and 23 on Y to check color

def Setup():
    print("give board size. (first horizontal then vertical)")
    print("example: 15x30")
    size = input("board size: ")
    boardSize = size.split("x")

    if len(boardSize) != 2 or not boardSize[0].isdigit() or not boardSize[1].isdigit():
        print("you need to give numbers in format: (horizontal size)x(vertical size)")
        return Setup()

    bottomRightX = topLeftX + (int(boardSize[0]) * 32 - 1)
    bottomRightY = topLeftY + (int(boardSize[1]) * 32 - 1)
    board = [["-" for _ in range(int(boardSize[0]))] for _ in range(int(boardSize[1]))]
    return board

board = Setup()

def GetBetterBoardPrint():
    boardString = ""
    for column in board:
        boardString += "\n"
        for cell in column:
            boardString += " " + str(cell)
    return boardString[1:]

def GetPixelToCheck(x, y):
    xPos = (topLeftX + (x * 32)) + 20
    yPos = (topLeftY + (y * 32)) + 23
    return xPos, yPos

def GetCellPixel(x, y):
    xPos = (topLeftX + (x * 32))
    yPos = (topLeftY + (y * 32))
    return xPos, yPos

def GetState(x, y, screenshot):
    xPos, yPos = GetPixelToCheck(x, y)
    pixel = screenshot.getpixel((xPos, yPos))
    if screenshot.getpixel((xPos - 20, yPos - 23)) == (255, 255, 255) and pixel == (189, 189, 189):
        return "-"
    elif screenshot.getpixel((xPos - 20, yPos - 23)) == (255, 255, 255) and pixel == (0, 0, 0):
        return "@"
    elif pixel == (189, 189, 189):
        return "0"
    elif pixel == (0, 0, 255):
        return "1"
    elif pixel == (0, 123, 0):
        return "2"
    elif pixel == (255, 0, 0):
        return "3"
    elif pixel == (0, 0, 123):
        return "4"
    elif pixel == (123, 0, 0):
        return "5"
    elif pixel == (0, 123, 123):
        return "6"
    elif pixel == (0, 0, 0):
        return "7"
    elif pixel == (123, 123, 123):
        return "8"

def CheckAllUnknownCells(screenshot = pyautogui.screenshot()):
    for y in range(len(board)):
        for x in range(len(board[y])):
            if board[y][x] == "-":
                board[y][x] = GetState(x, y, screenshot)

def ClickCell(x, y):
    pyautogui.click(GetCellPixel(x, y))

    time.sleep(0.05)

def RightClickCell(x, y):
    pyautogui.click(GetCellPixel(x, y), button = "right")
    board[y][x] = "@"

    time.sleep(0.05)

def GetAllNeighbours(x, y):
    neighbours = []
    directions = [
        (-1, -1), (0, -1), (1, -1),
        (-1,  0),          (1,  0),
        (-1,  1), (0,  1), (1,  1)
    ]

    for dx, dy in directions:
        newX = x + dx
        newY = y + dy

        if 0 <= newX < len(board[0]) and 0 <= newY < len(board):
            neighbours.append((newX, newY, board[newY][newX]))
    return neighbours


def AILoop():
    ClickCell(0, 0)
    loop = True
    while loop == True:
        screenshot = pyautogui.screenshot()
        CheckAllUnknownCells(screenshot)
        if screenshot.getpixel((521, 176)) == (0, 0, 0):
            print("WINNER WINNER CHICKEN DINNER!!")
            print(GetBetterBoardPrint())
            loop = False
        elif screenshot.getpixel((513, 190)) == (0, 0, 0):
            print("Oh no, we died")
            print(GetBetterBoardPrint())
            loop = False
        for y in range(len(board)):
            for x in range(len(board[y])):
                if board[y][x] == "-" or board[y][x] == "@":
                    continue

                neighbours = GetAllNeighbours(x, y)

                flagCount = sum(1 for n in neighbours if n[2] == "@")
                unknownCount = sum(1 for n in neighbours if n[2] == "-")

                if unknownCount == 0:
                    continue

                if int(board[y][x]) == unknownCount + flagCount:
                    for nx, ny, state in neighbours:
                        if state == "-":
                            RightClickCell(nx, ny)
                elif int(board[y][x]) == flagCount:
                    for nx, ny, state in neighbours:
                        if state == "-":
                            ClickCell(nx, ny)

AILoop()