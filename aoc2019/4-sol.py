
def checkNumber(n: int) -> bool:
    number = []
    while n > 0:
        digit = n % 10
        n = n // 10
        number.insert(0, digit)
    
    # check adj rule
    foundSameAdj = False
    # 0 1 2 3 4 5
    # 8 8 x x x x
    # x 8 8 x x x
    # x x 8 8 x x
    # x x x 8 8 x
    # x x x x 8 8

    d0 = number[0]
    d1 = number[1]
    d2 = number[2]
    d3 = number[3]
    d4 = number[4]
    d5 = number[5]

    if d0 == d1 and d1 != d2:
        foundSameAdj = True
    elif d1 == d2 and d0 != d1 and d2 != d3:
        foundSameAdj = True
    elif d2 == d3 and d1 != d2 and d3 != d4:
        foundSameAdj = True
    elif d3 == d4 and d2 != d3 and d4 != d5:
        foundSameAdj = True
    elif d4 == d5 and d3 != d4:
        foundSameAdj = True

    if foundSameAdj == False:
        return False
    
    # check non-decreasing
    for i in range(len(number) - 1):
        cur = number[i]
        nxt = number[i+1]
        if nxt < cur:
            return False
        
    return True
        
count = 0
for i in range(147981, 691424):
    if checkNumber(i):
        # print(i)
        count += 1
print(count)