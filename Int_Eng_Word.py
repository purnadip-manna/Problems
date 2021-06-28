"""
#Integer to English Words:
-------------------------------
            <== International Number System ==>
                ---------------------------
            x  x  x, x  x  x, x    x  x,xxx
            HB TB  B|HM TM  M|Hth Tth Th|HTO
numFrame = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

"""
placeName = {
    0: "Hundred",
    3: "Hundred",
    6: "Hundred",
    9: "Hundred",
    1: "Ten",
    4: "Ten",
    7: "Ten",
    10: "Ten",
    2: "One",
    5: "One",
    8: "One",
    11: "One",
}
ones = {
    0: "",
    1: "One ",
    2: "Two ",
    3: "Three ",
    4: "Four ",
    5: "Five ",
    6: "Six ",
    7: "Seven ",
    8: "Eight ",
    9: "Nine ",
}
tens = {
    1: "Ten ",
    2: "Twenty ",
    3: "Thirty ",
    4: "Forty ",
    5: "Fifty ",
    6: "Sixty ",
    7: "Seventy ",
    8: "Eighty ",
    9: "Ninety ",
    11: "Eleven ",
    12: "Twelve ",
    13: "Thirteen ",
    14: "Fourteen ",
    15: "Fifteen ",
    16: "Sixteen ",
    17: "Seventeen ",
    18: "Eighteen ",
    19: "Nineteen ",
}

def getWords(start, end, numFrame):
    engWord = ""
    status = False
    i = start
    while (i<end):
        if numFrame[i] != 0:
            status = True
            if placeName[i] == "Hundred":
                engWord += ones[numFrame[i]] + "Hundred "

            elif placeName[i] == "Ten":
                if numFrame[i] == 1 and numFrame[i+1] != 0:
                    engWord += tens[numFrame[i]*10+numFrame[i+1]]
                    i+=1

                else:
                    engWord += tens[numFrame[i]]

            elif placeName[i] == "One":
                engWord += ones[numFrame[i]]

        i+=1

    return engWord, status


num = int(input("Enter the number: "))
if num == 0:
    print("Zero")
else:
    numFrame = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    i = 11
    while num != 0 and i >= 0:
        numFrame[i] = num%10
        num = num // 10
        i -= 1

    Word = ""
    # Billion:
    partWord, status = getWords(0, 3,numFrame)
    if status:
        Word += partWord+"Billion "
    # Million:
    partWord, status = getWords(3, 6,numFrame)
    if status:
        Word += partWord+"Million "
    # Thousand:
    partWord, status = getWords(6, 9,numFrame)
    if status:
        Word += partWord+"Thousand "
    # Ones:
    partWord, status = getWords(9, 12,numFrame)
    if status:
        Word += partWord

    print(Word)