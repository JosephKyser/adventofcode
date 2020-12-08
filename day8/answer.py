#This a spaghetti brute force 

with open('input','r') as file:

    lines = file.readlines()

    lines = [i.strip().split(" ")+[0] for i in lines] #Cut off \n and split the list into 3 fields
    lines = [[i[0],int(i[1]),i[2]] for i in lines]

    instruction = 0
    max_inst = len(lines)
    accum = 0

    acc = False

    def part1():

        while(instruction < max_inst):
            if 0 == lines[instruction][2]:

                if 'acc' == lines[instruction][0]:
                    accum += lines[instruction][1]
                    lines[instruction][2] = accum

                elif 'nop' == lines[instruction][0]:
                    lines[instruction][2] = accum

                else: #jump
                    lines[instruction][2] = accum
                    instruction += (lines[instruction][1]-1)

                instruction += 1

            else:
                print(accum)
                break

    def part2_help(instruction_start,lines):

        lines = [[i[0],i[1],0] for i in lines] #reset the data

        instruction = instruction_start

        if 'nop' == lines[instruction][0]:
            lines[instruction][0] = 'jmp'

        elif 'jmp' == lines[instruction][0]:
            lines[instruction][0] = 'nop'

        else:
            pass

        return lines


    def part2(lines,accum=0):

        swap_instruction = 0
        while (swap_instruction < max_inst):

            print(f"{swap_instruction}/{max_inst}")

            instruction = 0
            linesf = part2_help(swap_instruction,lines)

            accum = 0

            while(instruction < max_inst):
                if  "acc" == linesf[swap_instruction][0]: #No need to run algorithm if the instr to chang in acc
                    break

                if 0 == linesf[instruction][2]:

                    if 'acc' == linesf[instruction][0]:
                        accum += linesf[instruction][1]
                        linesf[instruction][2] = accum

                    elif 'nop' == linesf[instruction][0]:
                        linesf[instruction][2] = accum

                    else: #jump
                        linesf[instruction][2] = accum
                        instruction += (linesf[instruction][1]-1)

                    instruction += 1

                else:
                    print("Loop")
                    break


            if max_inst == instruction: #Did it make EOF?
                print(accum)
                break

            swap_instruction += 1


    part2(lines,acc)
