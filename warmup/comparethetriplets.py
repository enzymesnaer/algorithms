import math
import os
import random
import re
import sys

# Complete the compareTriplets function below.
def compareTriplets(a, b):
    if len(a) == len(b):
        res = []
        player1 = 0
        player2 = 0

        i = 0

        for i in range(len(a)):
            if a[i] > b[i]:
                player1 += 1
            elif b[i] > a[i]:
                player2 += 1
            else:
                pass
            
        res.append(player1)
        res.append(player2)
    return res

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    a = list(map(int, input().rstrip().split()))

    b = list(map(int, input().rstrip().split()))

    result = compareTriplets(a, b)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
