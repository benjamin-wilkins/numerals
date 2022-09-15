numerals = {
    "I":1,
    "V":5,
    "X":10,
    "L":50,
    "C":100,
    "D":500,
    "M":1000,
}

places = [
    "",
    "a",
    "aa",
    "aaa",
    "ab",
    "b",
    "ba",
    "baa",
    "baaa",
    "ac",
    "c"
]

tens = [
    "I",
    "X",
    "C",
    "M"
]

fives = [
    "V",
    "L",
    "D"
]

def numeralToInt(numeral):
    numeral = numeral.upper()
    tokens1 = []
    for letter in numeral:
        tokens1.append(numerals[letter])
    tokens2 = []
    for i in range(len(tokens1)):
        if i == 0:
            tokens2.append(tokens1[i])
        elif tokens1[i-1] < tokens1[i]:
            tokens2.pop()
            tokens2.append(tokens1[i]-tokens1[i-1])
        else:
            tokens2.append(tokens1[i])
    return sum(tokens2)

def intToNumeral(integer):
    integer = str(integer)
    tokens = []
    for i in range(len(integer)):
        place = len(integer) - i - 1
        token = places[int(integer[i])]
        token = token.replace("a", tens[place])
        token = token.replace("b", fives[place])
        if place + 1 < len(tens):
            token = token.replace("c", tens[place+1])
        tokens.append(token)
    return "".join(tokens)