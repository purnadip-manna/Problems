#Problem statement:
#https://codingcompetitions.withgoogle.com/kickstart/round/000000000019ffc7/00000000001d3f56

T = int(input())
for i in range(T):
    N, B = map(int, input().split())
    arr = list(map(int, input().split()))
    arr.sort()
    out = 0
    for j in range(N):
        num = arr[j]
        if B-num<0:
            break
        else:
            B-=num
            out+=1
            
    print(f"Case #{i+1}: {out}")

'''
3
4 100
20 90 40 90
4 50
30 30 10 10
3 300
999 999 999
'''
