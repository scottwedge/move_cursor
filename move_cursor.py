#!/usr/bin/env python3

# A simple script to move cursor around the screen

# Imports
import time

# To generate BEL
def bel():	
    print("\a")  # To generate BEL sound

def num_bel(n):
    for j in range(n+1):
        bel()
        time.sleep(0.2)

