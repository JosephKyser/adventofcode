with open('input','r') as file:
    passes = file.readlines()
    passes = [i.replace("B","1") for i in passes]
    passes = [i.replace("F","0") for i in passes]
    passes = [i.replace("R","1") for i in passes]
    passes = [i.replace("L","0") for i in passes]
    passes = [i.strip() for i in passes]

    splitpasses = [(int(i[:7],base=2),int(i[7:],base=2)) for i in passes]
    uniqueIDs =  set(map(lambda x: x[0] * 8 + x[1],splitpasses))

    print(max(uniqueIDs)) #part 1
    print(uniqueIDs)

    for i in range(min(uniqueIDs),max(uniqueIDs),1):
        if i not in uniqueIDs:
            print(i)
