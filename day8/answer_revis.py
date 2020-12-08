import copy

def run_instruction(line):
    lines = copy.deepcopy(line)
    instruction = 0
    max_inst = len(lines)
    accum = 0

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
                #print(accum) #uncomment for part1
                return False
    print(accum) #part2
    return True


def swap_instruction(instruction_num,lines):
    line = copy.deepcopy(lines)
    if 'nop' == line[instruction_num][0]:
        line[instruction_num][0] = 'jmp'

    elif 'jmp' == line[instruction_num][0]:
        line[instruction_num][0] = 'nop'

    else:
        pass

    return line


def find_EOF(line):
    lines = copy.deepcopy(line)
    instruction = 0

    while(False == run_instruction(swap_instruction(instruction,lines))):
        instruction += 1

with open('input','r') as file:

    lines = file.readlines()
    lines = [i.strip().split(" ")+[0] for i in lines] #Cut off \n and split the list into 3 fields
    lines = [[i[0],int(i[1]),i[2]] for i in lines]
    find_EOF(lines)
