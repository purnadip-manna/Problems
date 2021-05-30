#Problem Statement:
# https://leetcode.com/problems/container-with-most-water/

def maxArea(height):
    max_area = 0
    left = 0
    right = len(height)-1
    while(left<right):
        area = min(height[left], height[right])*(right-left)
        if area > max_area:
            max_area = area
        if (height[left] < height[right]):
            left+=1
        elif (height[left] >= height[right]):
            right-=1

    return max_area

print(maxArea([1,3,2,5,25,24,5]))
