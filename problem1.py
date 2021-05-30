'''
Given an integer, find the next permutation of it in absolute order. 
For example, given 48975, the next permutation would be 49578.
'''
ls = list(map(int, input("Enter the number: ")))
print(ls)
temp = ls[1:]
if temp == sorted(temp, reverse=True):
    d0 = ls[0]
    ls.sort()
    idx = ls.index(d0)
    if idx+1 != len(ls):
        d1 = ls[idx+1]
        ls.remove(d1)
        ls.insert(0, d1)
        print(ls)


    else:
        print("Error")

else:
    print("No")