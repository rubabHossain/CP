
def evaluate(intCode, noun, verb):
    program = list(map(lambda c: int(c), intCode.split(",")))
    program[1] = noun
    program[2] = verb

    iptr = 0
    while True:
        opCode = program[iptr]
        if opCode == 99:
            break
        src1ptr = program[iptr+1]
        src2ptr = program[iptr+2]
        destptr = program[iptr+3]
        src1 = program[src1ptr]
        src2 = program[src2ptr]
        if opCode == 1:
            program[destptr] = src1 + src2
        elif opCode == 2:
            program[destptr] = src1 * src2
        iptr+=4
    return program

    

program = input()

for i in range(100):
    for j in range(100):
        result = evaluate(program, i, j)
        if result[0] ==19690720:
            print(i, j)