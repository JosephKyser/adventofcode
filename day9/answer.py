with open('input','r') as file:
    files = file.readlines()
    files = [int(i.strip()) for i in files] #List[Int]



    max_len = len(files)
    start = 25

    invalid_num = 0
    invalid_index = 0

    for i in range(start,max_len):
        sortedlist = sorted(files[i-25:i])
        max_num = sum(sortedlist[23:25])
        min_num = sum(sortedlist[0:2])

        if (max_num < files[i] or min_num > files[i]):
            invalid_num = files[i]
            invalid_index = i
            break

    new_list = files[:]

    i = 0
    j = 1


    working_sum = new_list[i] + new_list[j]
    while invalid_num != working_sum:
        if invalid_num > working_sum:
            j += 1
            working_sum += new_list[j]
        else:
            working_sum -= new_list[i]
            i += 1

    j += 1
    print(min(new_list[i:j]) + max(new_list[i:j]))
