test = """F10
N3
F7
R90
F11"""

with open('input','r') as file:
    directions = [{i.strip()[0:1]:int(i.strip()[1:])} for i in file.readlines() if i != "\n"]
    #directions = [{i.strip()[0:1]:int(i.strip()[1:])} for i in test.split("\n") if i != "\n"]
    dir = {0: 'E', 1: 'S', 2: 'W', 3: 'N'}
    curr = 0

    distance = {"N":0,"S":0,"E":0,"W":0}


    for instruction_dic in directions:
        for key in instruction_dic:
            if key in distance:
                distance[key] += instruction_dic[key]
            elif "R" == key:
                curr = (curr + instruction_dic[key]//90) % 4
            elif "L" == key:
                curr = (curr - instruction_dic[key]//90) % 4
            else:
                distance[dir[curr]] += instruction_dic[key]

    manhattan = abs(distance["N"]-distance["S"]) + abs(distance["E"]-distance["W"])
    print(manhattan)

#part2

    waypoint = [10,0,0,1] #ESWN distances

    distance = [0,0,0,0] #ESWN
    dir_ind = {'E':0,'S':1,'W':2,'N':3}

    for instruction_dic in directions:
        for key in instruction_dic:
            if key in dir_ind:
                waypoint[dir_ind[key]] += instruction_dic[key]
            elif "L" == key:
                for i in range(0,instruction_dic[key]//90): waypoint = waypoint[1:] + waypoint[0:1]
            elif "R" == key:
                for i in range(0,instruction_dic[key]//90): waypoint = waypoint[3:] + waypoint[0:3]
            else:
                distance = [instruction_dic[key]*waypoint[i] + distance[i] for i in range(len(distance))]

    manhattan = abs(distance[1]-distance[3]) + abs(distance[0]-distance[2])
    print(manhattan)
