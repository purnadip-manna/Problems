# Integer Number => Roman Number

romanDict = {
    1 :'I',
    4 :'IV',
    5 :'V',
    9 :'IX',
    10 :'X',
    40 :'XL',
    50 :'L',
    90 :'XC',
    100 :'C',
    400 :'CD',
    500 :'D',
    900 :'CM',
    1000 :'M'
}

def getRoman(num):
    if num in {4, 9, 40, 90, 400, 900}:
        return romanDict[num]

    else:
        divisor = 1
        for x in [1, 5, 10, 50, 100, 500, 1000]:
            if x > num:
                break

            divisor = x
        if num%divisor == 0:
            return romanDict[divisor]*(num//divisor)

        else:
            return romanDict[divisor]+getRoman(num%divisor)

num = int(input("Enter the Number: "))
roman = ''
l = len(str(num))
for x in str(num):
    n = x+'0'*(l-1)
    if n != '0':
        roman += getRoman(int(n))

    l-=1

print(roman)