#Problem Statement:
#https://practice.geeksforgeeks.org/problems/269f61832b146dd5e6d89b4ca18cbd2a2654ebbe/1

import numpy

def isAllInfected(arr):
    for x in arr:
        for y in x:
            if y == 1:
                return False
    return True    

def spreadCovid(arr, row, col, infectedId):
    if infectedId == 2:
        newInfectedId = 3
    else:
        newInfectedId = 2

    for i in range(row):
        for j in range(col):
            if(arr[i][j] == infectedId):
                #Up
                if i-1 >= 0:
                    if arr[i-1][j] == 1:
                        arr[i-1][j] = newInfectedId
                #Down
                if i+1 < row:
                    if arr[i+1][j] == 1:
                        arr[i+1][j] = newInfectedId
                #Left
                if j-1 >= 0:
                    if arr[i][j-1] == 1:
                        arr[i][j-1] = newInfectedId
                #Right
                if j+1 < col:
                    if arr[i][j+1] == 1:
                        arr[i][j+1] = newInfectedId

    if isAllInfected(arr):
        return 1
    else:
        return (1 + spreadCovid(arr, row, col, newInfectedId))

row, col = map(int, input().split())
arr = []
for i in range(row):
    arr.append(list(map(int, input().split())))

arr = numpy.array(arr)
try:
    print(spreadCovid(arr, row, col, 2))
except:
    print("-1")
