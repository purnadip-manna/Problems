#Find exact sum using minimum number of elements of a list.

def giveSmallest(num, arr):
    flag = 0
    for i in range(len(arr)):
        if arr[i]<=num:
            re = arr[i]
            flag = 1
            break
            
    if flag == 0:
        return -1
    else:
        return re



mainArr = list(map(int, input("Enter the list (comma-separated): ").split(",")))
findSum = int(input("Enter the exact sum: "))
mainArr.sort(reverse=True)
tempArr = mainArr.copy()
arr = tempArr.copy()
usedElement = []
ln = len(mainArr)
flag = 1
for i in range(ln):
    temp = findSum
    while temp>0:
        n = giveSmallest(temp, arr)
        if(n == -1):
            flag = 0
            break
        temp = temp - n
        usedElement.append(n)
        arr.remove(n)

    if flag == 0:
        arr = tempArr[i+1:].copy()
        usedElement = []
        flag = 1

    else:
        break

print(usedElement)

'''
Test Case:
7, 8, 19, 7, 8, 7, 10, 20
29
'''