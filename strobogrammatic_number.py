def checkOddEven(n):
    if n%2:
        return "odd"
    else:
        return "even"

good_no = {0, 6, 8, 9}
rotate = {'0' : '0', '6' : '9', '8' : '8', '9' : '6'}
num = input("Enter the number: ")
isStgNum = True
for x in num:
    if int(x) not in good_no:
        isStgNum = False
        break

if isStgNum:
    ln = len(num)
    #is the length of the number odd or even ?
    if checkOddEven(ln) == "even":
        l = 0
        r = len(num)-1
        while (l<r):
            if num[l] != rotate[num[r]]:
                isStgNum = False
                break
            l+=1
            r-=1
    else:
        mid = ln//2
        if num[mid] is '6' or num[mid] is '9':
            isStgNum = False
        else:
            l = 0
            r = len(num)-1
            while (l<r and l!=mid and r!=mid):
                if num[l] != rotate[num[r]]:
                    isStgNum = False
                    break
                l+=1
                r-=1

print(isStgNum)