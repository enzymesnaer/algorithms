import math
import os
import random
import re
import sys

def gradingStudents(grades):
    for i in grades:
        round_fig = math.ceil(i/5) * 5
        if ((round_fig - i) < 3) and (i >= 38):
            i = round_fig
            print(i)    
        else:
            print(i)
      
grades_count = int(input().strip())

grades = []

for _ in range(grades_count):
    grades_item = int(input().strip())
    grades.append(grades_item)

result = gradingStudents(grades)


