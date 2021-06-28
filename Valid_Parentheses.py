# Valid Parentheses
s = input()
stact = []
for x in s:
    if x == '(' or x == '{' or x == '[':
        stact.append(x)
    else:
        if stact != []:
            ele = stact.pop()
            if (x == ')' and ele != '(') or (x == '}' and ele != '{') or (x == ']' and ele != '['):
                #return False
                print(False)

        else:
            #return False
            print(False)

if stact == []:
    print(True)

else:
    print(False)