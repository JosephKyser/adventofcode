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

    memo= [-1 for i in range(0,187)][:] #initializes a list of -1s

    '''
    adapt is a dict that store a voltage to a list of possible connections from that voltage

    if voltage = [1,2,3,4]
    then adapt = {1:[2,3,4],2:[3,4],3:[4]}
    '''

    for volts in sortedList:
        potential = []
        for i in range(1,4):
            if (volts+i) in sortedList:
                potential += [volts+i]

        adapt[volts] = potential


    def Helper(voltage) -> int:
        if 186 == voltage: #Found a valid combination
            return 1
        elif memo[voltage] >= 0: #Found a valid combination of a subproblem that already occurred
            return memo[voltage]
        else:
            memo[voltage] = sum([Helper(i) for i in adapt[voltage]])
            return memo[voltage]
    # Essentially, you run recursion on all numbers in the list of possible connections and add them up.

    Helper(0)
    print(memo[0])
