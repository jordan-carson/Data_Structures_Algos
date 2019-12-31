def find_busiest_period(data):
    # 0 = exiting
    # 1 = entering
    # we want to return [1487800378, 10, 1],
    # we need to return the time where the mall is at its busiest
    nbr_of_people = 0
    max_time = 0
    max_people = 0
    print('Start: The Max Time is: ', max_time)
    # iterate though the nested array's indices
    for i in range(len(data)):
        # create a helper variable to set j to the value of i
        # j = data[i]
        if data[i][2] == 1:
            nbr_of_people += data[i][1]
        else:
            nbr_of_people -= data[i][1]
        print('Number of people before the loop is: ', nbr_of_people)
        print('Length of data -1 is: ', len(data) - 1)
        if i == len(data) - 1 or data[i][0] != data[i + 1][0]:
            if nbr_of_people > max_people:
                max_people = nbr_of_people

                max_time = data[i][0]
                print('End: Number of Max People is: ', max_people)
                print('End: The Max Time is: ', max_time)

    return max_time


data = [[1487799425,14,1]
        ,[1487799425,4,1]
        ,[1487799425,2,1]
        ,[1487800378,10,1]
        ,[1487801478,18,1]
        ,[1487901013,1,1]
        ,[1487901211,7,1]
        ,[1487901211,7,1]]

print(find_busiest_period(data))
