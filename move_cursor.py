#!/usr/bin/env python3

# A simple script to draw shapes on the screen

# Based on info at wepbage:
# https://gist.github.com/fnky/458719343aabd01cfb17a3a4f7296797

# Imports
import time

# Constants
CHAR = "*"

# Functions

def bel():  # To generate single BEL sound
    print("\a") 

def num_bel(n):  # To generate 'n' BEL sounds
    for j in range(n+1):
        bel()
        time.sleep(0.2)  # Without delay only hear single BEL

def pos(x, y, char):  # Place char at X,Y position
    print("\033[{};{}H".format(x,y))
    time.sleep(0.2)

def move_rel():  # Move relative to current position
    # With "j" to move one spot left, "k" or "l" to move one spot right
    # "i" or "o" to move one spot up
    # "n" or "m" to move one spot down
    key = input("Enter key: ")

    if key == "i" or key == "o": print("\033[1A{}".format(CHAR))  # Move up one
    elif key == "n" or key == "m": print("\033[1B{}".format(CHAR))  # Move down one
    elif key == "j": print("\033[1D{}".format(CHAR))  # Move left one column
    elif key == "k" or key == "l": print("\033[1C{}".format(CHAR))  # Move right one column
    else: pass  # Skip and continue
        
def home():  # Position cursor at home (0,0) (top left)
    print("\033[HCHAR")

def rectangle(x1, y1, x2, y2,  char):
    # print grid from (x1,y1) to (x2,y2) with character 'char'
    # Work from smaller number to larger number
    # Remember print statement format is {line/y};{column/x} with (0,0) at screen top left
    x_min = min(x1, x2)
    x_max = max(x1, x2) 
    x_diff = x_max - x_min
    y_min = min(y1, y2)
    y_max = max(y1, y2) 
    y_diff = y_max - y_min

    # Print top and bottom horizontal lines
    for j in range(x_min, x_max + 1):
        print("\033[{};{}f{}".format(y_min, j, char))
        print("\033[{};{}H{}".format(y_max, j, char))

    # Print left and right vertical lines
    for j in range(y_min, y_max+ 1):
        print("\033[{};{}H{}".format(j, x_min, char))
        print("\033[{};{}H{}".format(j, x_max, char))


rectangle(5, 5, 65, 20, '*')
