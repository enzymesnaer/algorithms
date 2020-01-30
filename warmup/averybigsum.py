import math
import os
import random
import re
import sys


def aVeryBigSum(ar):
    out = sum(ar)
    return out

ar_count = int(input())

ar = list(map(int, input().rstrip().split()))

print(ar)

result = aVeryBigSum(ar)

print(result)



