import math
import os
import random
import re
import sys


def miniMaxSum(arr):
    sum = 0
    for i in range(len(arr)):
        sum += arr[i]
        # print(f"sum for {i}",sum)   
        # print(f"max for {i}",max(arr))
        # print(f"min for {i}",min(arr)) 
    print(sum-max(arr), sum-min(arr))

arr = list(map(int, input().rstrip().split()))

miniMaxSum(arr)
