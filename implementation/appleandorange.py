import math
import os
import random
import re
import sys

def countApplesAndOranges(s, t, a, b, apples, oranges):
    App_dists = []
    for A in  apples:
        A = A + a
        App_dists.append(A)
    noAps_inrange = 0

    for k, v in enumerate(App_dists):
        if v in range(s,t+1):
            noAps_inrange += 1
    print(noAps_inrange)

    Org_dists = []
    for O in  oranges:
        O = O + b
        Org_dists.append(O)
    noOrs_inrange = 0

    for k, v in enumerate(Org_dists):
        if v in range(s,t+1):
            noOrs_inrange += 1
    print(noOrs_inrange)


st = input().split() 

s = int(st[0]) # house start pt

t = int(st[1]) # house end pt

ab = input().split()

a = int(ab[0])  # apple tree origin

b = int(ab[1]) # orange tree origin

mn = input().split()

m = int(mn[0]) # nos apples

n = int(mn[1]) # nos oranges

apples = list(map(int, input().rstrip().split())) # apples origins

oranges = list(map(int, input().rstrip().split())) # oranges origins

countApplesAndOranges(s, t, a, b, apples, oranges)
