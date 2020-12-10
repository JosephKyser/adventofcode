with open('input','r') as file:
    lists = [int(i.strip()) for i in file.readlines() if i != '\n']
    sortedList = sorted(lists)
    sortedList = [0] + sortedList
    sortedList.append(max(sortedList)+3) #formatting

    shiftedList = sortedList[1:] #shift the list by one to subtract List[i] from List[i+1]
    shiftedList.append(0)

    diffs = sorted([a - b for a,b in zip(shiftedList,sortedList)])
    difbyone = [i for i in diffs if i == 1]
    difbythree = [i for i in diffs if i == 3]

   # print((len(difbyone)+1)*(len(difbythree)+1)) part1

    adapt = {} #{Int:List[Int]}

    memo= [-1 for i in range(0,187)][:]

    for volts in sortedList:
        potential = []
        for i in range(1,4):
            if (volts+i) in sortedList:
                potential += [volts+i]

        adapt[volts] = potential


    def Helper(voltage) -> int:
        if 186 == voltage:
            return 1
        elif memo[voltage] >= 0:
            return memo[voltage]
        else:
            memo[voltage] = sum([Helper(i) for i in adapt[voltage]])
            return memo[voltage]

    Helper(0)
    print(memo[0])
