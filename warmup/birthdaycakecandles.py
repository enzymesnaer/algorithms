import math
import os
import random
import re
import sys

def birthdayCakeCandles(ar):
    highest_in_the_room = max(ar)
    blows = 0

    for i in range(0,len(ar)):
        if ar[i] == highest_in_the_room:
            blows += 1

    return print(blows)

ar_count = int(input())

ar = list(map(int, input().rstrip().split()))

result = birthdayCakeCandles(ar)

