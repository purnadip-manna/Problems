'''
#Add_Substract problem:
Write a function, add_subtract, which alternately adds and subtracts curried arguments. Here are some sample operations:
add_subtract(7) -> 7
add_subtract(1)(2)(3) -> 1 + 2 - 3 -> 0
add_subtract(-5)(10)(3)(9) -> -5 + 10 - 3 + 9 -> 11
'''

def add_subtract(*arg):
    ans = arg[0]
    j = 0
    for i in range(1, len(arg)):
        if j%2==0:
            ans+=arg[i]

        else:
            ans-=arg[i]

        j+=1

    return ans

print(add_subtract(7))
print(add_subtract(1,2,3))
print(add_subtract(-5,10,3,9))