import math
import os
import random
import re
import sys


def staircase(n):
    for i in range(1, n+1):
        for j  in range(0, n-i):
            print(" ", end="")
    
        print("#"*i)


n = int(input())

staircase(n)
