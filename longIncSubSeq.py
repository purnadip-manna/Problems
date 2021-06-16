# Max length of longest increasing contiguous subsequence

def longIncSubSeq(ls, n):
    # ls = list[]
    # n = Length(ls)
    tempLength = maxLength = 1
    for i in range(1, n):
        if ls[i]>ls[i-1]:
            tempLength+=1

        else:
            if maxLength < tempLength:
                maxLength = tempLength
                
            tempLength = 1

    if maxLength < tempLength:
         maxLength = tempLength     

    return maxLength


ls = list(map(int, input().split(" ")))
print(longIncSubSeq(ls, len(ls)))