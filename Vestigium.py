#Google Codejam
#https://codingcompetitions.withgoogle.com/codejam/round/000000000019fd27/000000000020993c

T = int(input())
for x in range(T):
    N = int(input())
    arr = []
    for i in range(N):
        arr.append(list(map(int, input().split())))
        
    t = 0
    for i in range(N):
        t+=arr[i][i]
        
    r = c = 0
    for i in range(N):
        if len(set(arr[i]))!=N:
            r+=1

        col = []
        for j in range(N):
            col.append(arr[j][i])

        if len(set(col))!=N:
            c+=1

        col.clear()
            
    print(f"Case #{x+1}: {t} {r} {c}")


"""
#Input:
3
4
1 2 3 4
2 1 4 3
3 4 1 2
4 3 2 1
4
2 2 2 2
2 3 2 3
2 2 2 3
2 2 2 2
3
2 1 3
1 3 2
1 2 3

#Output:
Case #1: 4 0 0
Case #2: 9 4 4
Case #3: 8 0 2
"""
