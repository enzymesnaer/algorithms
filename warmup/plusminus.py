def plusMinus(arr):
    nop = 0
    non = 0
    noz = 0

    for i in range(n):
        if arr[i] > 0:
            nop += 1
        elif arr[i] < 0:
            non += 1
        else:
            noz += 1
             
    print(round(float(nop/n),6), round(float(non/n),6), round(float(noz/n), 6), sep='\n')  
      
    
n = int(input())

arr = list(map(int, input().rstrip().split()))

plusMinus(arr)
