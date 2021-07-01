"""
gameOfThrones
#Anagram #Palindrom

"""
def gameOfThrones(s):
    length = len(s)
    str_list = sorted(s)
    str_dict = dict()
    ele = str_list[0]
    count = 0
    for x in str_list:
        if x == ele:
            count += 1

        else:
            str_dict[ele] = count
            ele = x
            count = 1

    str_dict[ele] = count

    if length % 2 == 0:
        for val in str_dict.values():
            if val%2 == 1:
                return "NO"

        return "YES"

    else:
        flag = 0
        for val in str_dict.values():
            if val%2 == 1:
                flag += 1

        if flag == 1:
            return "YES"
        else:
            return "NO"        


s = input()
print(gameOfThrones(s))