'''
# Love Song ==>
link: https://codeforces.com/contest/1539/problem/B
'''

memoList = [0]
n, q = map(int, input().split())
s = input()
count = 0
for i in range(n):
    count += ord(s[i])-96
    memoList.append(count)

#print(memoList)
for i in range(q):
    l, r = map(int, input().split())
    print(memoList[r]-memoList[l-1])
