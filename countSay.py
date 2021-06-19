"""
# Count and Say
-----------------------
Input: n = 1
Output: "1"
Explanation: This is the base case.

Input: n = 4
Output: "1211"
Explanation:
countAndSay(1) = "1"
countAndSay(2) = say "1" = one 1 = "11"
countAndSay(3) = say "11" = two 1's = "21"
countAndSay(4) = say "21" = one 2 + one 1 = "12" + "11" = "1211"

"""

def countAndSay(num):
    num += 'x'
    l = len(num)
    newStr = ""
    i = 0
    digit = num[i]
    count = 0
    while True:
        if num[i] == digit:
            count += 1
        else:
            newStr += str(count)+digit
            digit = num[i]
            count = 1

        if num[i] == 'x':
            break

        i += 1

    return newStr

n = int(input())
temp = '1'
for i in range(n-1):
    temp = countAndSay(temp)

print(temp)