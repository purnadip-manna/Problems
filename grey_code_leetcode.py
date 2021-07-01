"""
Input: n = 2
Output: [0,1,3,2]
Explanation:
The binary representation of [0,1,3,2] is [00,01,11,10].
- 00 and 01 differ by one bit
- 01 and 11 differ by one bit
- 11 and 10 differ by one bit
- 10 and 00 differ by one bit
[0,2,3,1] is also a valid gray code sequence, whose binary representation is [00,10,11,01].
- 00 and 10 differ by one bit
- 10 and 11 differ by one bit
- 11 and 01 differ by one bit
- 01 and 00 differ by one bit


Input: n = 1
Output: [0,1]


Input: n = 4
Output: [0,1,3,2,6,7,5,4,12,13,15,14,10,11,9,8]


"""

def div_grey_swap(ls):
    length = len(ls)
    if length <= 4:
        if length == 2:
            return ls
        else:
            ls[length-1], ls[length-2] = ls[length-2], ls[length-1]
            return ls
    else:
        mid = length//2
        l1 = ls[0:mid].copy()
        left_arr = div_grey_swap(l1)
        l2 = ls[mid:].copy()
        right_arr = div_grey_swap(l2)
        right_arr.reverse()
        return left_arr + right_arr

    

class Solution:
    def grayCode(self, n: int) -> List[int]:
        grey_list = list(range(2**n))
        return div_grey_swap(grey_list)
        