# Roman Number => Integer Number

romanDict = {
    'I' : 1,
    'V' : 5,
    'X' : 10,
    'L' : 50,
    'C' : 100,
    'D' : 500,
    'M' : 1000
}

s = input("Enter the Roman Number: ")
intNum = 0
length = len(s)
for i in range(length-1):
    if(romanDict[s[i]]<romanDict[s[i+1]]):
        intNum -= romanDict[s[i]]
    else:
        intNum += romanDict[s[i]]

intNum += romanDict[s[length-1]]
print("Integer:", intNum)
            