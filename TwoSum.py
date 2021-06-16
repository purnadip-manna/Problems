'''
Example:
input:
0,4,3,0
0

Output:
[0, 3]

Explanation:
nums[0] + num[3] = 0+0 == target => 0

'''

nums = list(map(int, input().split(",")))
target = int(input())
n = len(nums)
for i in range(n-1):
    for j in range(i+1, n):
        if nums[i]+nums[j] == target:
            print([i, j])
        j+=1
    i+=1
    
print("[]")