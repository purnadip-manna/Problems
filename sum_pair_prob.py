#Find pairs for Exact Sum
def findPairs(input_arr, sumValue):
    input_arr.sort()
    return_list = []
    i = 0
    j = len(input_arr)-1
    while i<j:
        s = input_arr[i] + input_arr[j]
        if s == sumValue:
            return_list.append((input_arr[i], input_arr[j]))
            i+=1
            j-=1

        elif s < sumValue:
            i+=1
        
        else:
            j-=1

    return return_list


input_arr = list(map(int, input("Enter the list elements (comma separated): ").split(",")))
sum_val = int(input("Exact Sum Value: "))
print(findPairs(input_arr, sum_val))

'''
Test Case:
-----------------
Enter the list elements (comma separated): 4,3,2,3
Exact Sum Value: 6
[(2, 4), (3, 3)]

'''