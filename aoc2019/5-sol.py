def evaluate(intCode: str):
    program = list(map(lambda c: int(c), intCode.split(",")))
    iptr = 0

    while True:
        
        opCode = program[iptr] % 100
        param1_mode = (program[iptr] // 100) % 10
        param2_mode = (program[iptr] // 1000) % 10
        param3_mode = (program[iptr] // 10000) % 10

        if opCode == 99:
            # halt
            break
        

        if opCode == 1:
            # add
            src1 = program[program[iptr+1]] if param1_mode == 0 else program[iptr+1]
            src2 = program[program[iptr+2]] if param2_mode == 0 else program[iptr+2]
            dest = program[iptr+3]

            program[dest] = src1 + src2
            iptr+=4


        elif opCode == 2:
            # mult
            src1 = program[program[iptr+1]] if param1_mode == 0 else program[iptr+1]
            src2 = program[program[iptr+2]] if param2_mode == 0 else program[iptr+2]
            dest = program[iptr+3]
            
            program[dest] = src1 * src2
            iptr+=4


        elif opCode == 3:
            # input
            program[program[iptr+1]] = int(input())
            iptr += 2


        elif opCode == 4:
            # output
            src1 = program[program[iptr+1]] if param1_mode == 0 else program[iptr+1]
            print(src1)
            iptr += 2
        

        elif opCode == 5:
            # jump if true
            src1 = program[program[iptr+1]] if param1_mode == 0 else program[iptr+1]
            src2 = program[program[iptr+2]] if param2_mode == 0 else program[iptr+2]
            
            iptr = src2 if src1 != 0 else iptr + 3


        elif opCode == 6:
            # jump if false
            src1 = program[program[iptr+1]] if param1_mode == 0 else program[iptr+1]
            src2 = program[program[iptr+2]] if param2_mode == 0 else program[iptr+2]
            
            iptr = src2 if src1 == 0 else iptr + 3
            

        elif opCode == 7:
            # less than cond
            src1 = program[program[iptr+1]] if param1_mode == 0 else program[iptr+1]
            src2 = program[program[iptr+2]] if param2_mode == 0 else program[iptr+2]
            dest = program[iptr+3]

            program[dest] = 1 if src1 < src2 else 0
            iptr += 4

        elif opCode == 8:
            # equals to cond
            src1 = program[program[iptr+1]] if param1_mode == 0 else program[iptr+1]
            src2 = program[program[iptr+2]] if param2_mode == 0 else program[iptr+2]
            dest = program[iptr+3]
            
            program[dest] = 1 if src1 == src2 else 0
            iptr += 4


        else:
            # error
            raise Exception(str(opCode) + ": Encountered Unrecognized Opcode in IntCode Program.")
    

    return program
## end evaluate(program)
    

program = input()
# program = """3,21,1008,21,8,20,1005,20,22,107,8,21,20,1006,20,31,
# 1106,0,36,98,0,0,1002,21,125,20,4,20,1105,1,46,104,
# 999,1105,1,46,1101,1000,1,20,4,20,1105,1,46,98,99"""
evaluate(program)