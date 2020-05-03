
def additionalFuel(n: int) -> int:
    s = 0
    while n > 0:
        n = ((n // 3) - 2)
        # print(n)
        s += max(n,0)
    return s

num = input()
t = 0
while num != "":
    z = (int(num)//3) - 2 
    t += z + additionalFuel(z)
    print(t)
    num = input()