import re
import math
import itertools
import copy

test = '''mask = XXXXXXXXXXXXXXXXXXXXXXXXXXXXX1XXXX0X
mem[8] = 11
mem[7] = 101
mem[8] = 0'''

test2 = '''mask = 000000000000000000000000000000X1001X
mem[42] = 100
mask = 00000000000000000000000000000000X0XX
mem[26] = 1'''

file = open('input','r')
file = file.read()

def part1():
    #formatted = test.split('\n')
    formatted = [i for i in file.split('\n') if "" != i]
    mem = {}
    mask = ''


    def maskops(i,j):
        if "X" == i: return j
        else: return i


    for instruction in formatted:
        task_list = instruction.split(" = ")
        if 'mask' in task_list[0]:
            mask = task_list[1]
        else:
            binarynum = f'{int(task_list[1]):036b}'
            newnum = ""
            for a,b in zip(mask,binarynum):
                newnum += maskops(a,b)
            num = int(re.findall(r'[0-9]+',task_list[0])[0])
            mem[num] = int(newnum,2)

    print(sum(mem.values()))

def part2():
    #formatted = test2.split('\n')
    formatted = [i for i in file.split('\n') if "" != i]
    mem = {}
    mask = ''

    def maskops(i,j):
        if '0' == i: return j
        elif '1' == i: return "1"
        else: return "X"

    def getWildNums(st):
        output = []

        a = [(0,1) if e =='X' else (e,) for e in st]
        for c in itertools.product(*a):
            output.append("".join(map(lambda x: str(x),c)))
        return map(lambda x: int(x,2),output)

    for instruction in formatted:
        task_list = instruction.split(" = ")
        if 'mask' in task_list[0]:
            mask = task_list[1]
        else:
            num = int(re.findall(r'[0-9]+',task_list[0])[0])
            binarynum = f'{num:036b}'
            newnum = ""

            for a,b in zip(mask,binarynum):
                newnum += maskops(a,b)

            for address in getWildNums(newnum):
                mem[address] = int(task_list[1])

    print(sum(mem.values()))

part1()
part2()
