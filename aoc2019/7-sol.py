EXIT_YIELD = 0

class Amplifier():
    def __init__(self, intCode: str, in_buffer, out_buffer, name):
        super().__init__()
        self.program = list(map(lambda c: int(c), intCode.split(",")))
        self.input_buffer = in_buffer
        self.output_buffer = out_buffer
        self.name = name
        self.instruction_pointer = 0


    def evaluate(self):

        iptr = self.instruction_pointer
        program = self.program
        input_buffer = self.input_buffer
        output_buffer = self.output_buffer

        
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
                if len(input_buffer) == 0:
                    self.instruction_pointer = iptr
                    return EXIT_YIELD
                inputElem = input_buffer.pop(0)
                program[program[iptr+1]] = inputElem
                # input_index += 1
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
# end of Amplifier Class

###################################################
f = open("7-in.txt", "r")
program = f.read()


# ## answer to part 1 ##
# def rec_eval(used_settings, amp_input):
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


buf01 = []
buf12 = []
buf23 = []
buf34 = []
buf40 = []


# for setting_permutation in permutations([5,6,7,8,9]):
thrusts = []
for setting_permutation in permutations([5,6,7,8,9]):
    
    # clear out buffers from prev run
    buf40.clear()
    buf01.clear()
    buf12.clear()
    buf23.clear()
    buf34.clear()

    # append phase settings to buffers
    buf40.append(setting_permutation[0])
    buf01.append(setting_permutation[1])
    buf12.append(setting_permutation[2])
    buf23.append(setting_permutation[3])
    buf34.append(setting_permutation[4])

    # append input signal to amp 0
    buf40.append(0)

    ## instantiate amplifiers for new runs
    amp0 = Amplifier(program + "", buf40, buf01, "amp0") # amp 0
    amp1 = Amplifier(program + "", buf01, buf12, "amp1") # amp 1
    amp2 = Amplifier(program + "", buf12, buf23, "amp2") # amp 2
    amp3 = Amplifier(program + "", buf23, buf34, "amp3") # amp 3
    amp4 = Amplifier(program + "", buf34, buf40, "amp4") # amp 4
    

    retval = EXIT_YIELD
    while retval == EXIT_YIELD:
        amp0.evaluate()
        amp1.evaluate()
        amp2.evaluate()
        amp3.evaluate()
        retval = amp4.evaluate()
    thrusts.append(buf40[0])

print(max(thrusts))
    



