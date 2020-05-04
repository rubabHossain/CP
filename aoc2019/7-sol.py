def evaluate(intCode: str, input_buffer_):
    program = list(map(lambda c: int(c), intCode.split(",")))

    iptr = 0
    input_index = 0
    input_buffer = input_buffer_
    output_buffer = []
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
            program[program[iptr+1]] = input_buffer[input_index]
            input_index += 1
            iptr += 2


        elif opCode == 4:
            # output
            src1 = program[program[iptr+1]] if param1_mode == 0 else program[iptr+1]
            output_buffer.append(src1)
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
    

    return output_buffer
## end evaluate(program)

###################################################
f = open("7-in.txt", "r")
program = f.read()


# ## answer to part 1 ##
# def rec_eval(used_settings, amp_input):
#     # print(used_settings)
#     if(len(used_settings) == 5):
#         print(amp_input)
#     else:
#         for i in range(5):
#             if i in used_settings:
#                 continue
#             used_settings.append(i)
#             input_buf = [i, amp_input]
#             output = evaluate(program, input_buf)
#             rec_eval(used_settings, output[0])
#             used_settings.remove(i)

# rec_eval([], 0) ## pipe print statements of this into temp script to read max



## answer to part 22 ##
from itertools import permutations

buf0 = []
buf1 = []
buf2 = []
buf3 = []
buf4 = []

for setting_permutation in permutations([5,6,7,8,9]):
    print(setting_permutation)
    buf0.append(setting_permutation[0])
    buf1.append(setting_permutation[1])
    buf2.append(setting_permutation[2])
    buf3.append(setting_permutation[3])
    buf4.append(setting_permutation[4])

