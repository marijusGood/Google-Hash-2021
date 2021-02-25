import collections






#6 4 5 2 1000
#2 0 rue-de-londres 1
#0 1 rue-d-amsterdam 1
#3 1 rue-d-athenes 1
#2 3 rue-de-rome 2
#1 2 rue-de-moscou 3
#4 rue-de-londres rue-d-amsterdam rue-de-moscou rue-de-rome
#3 rue-d-athenes rue-de-moscou rue-de-londres
lett = ["b", "c", "d", "e", "f"]
for l in lett:
    file1 = open(l + ".txt", "r")
    Lines = file1.readlines()
    inputs = Lines[0].split()

    streetDic = {}
    numStreet = {}
    interDic = {}
    carsStartAt = {}
    carsList = []


    seconds = int(inputs[0])
    intersections = int(inputs[1])
    streets = int(inputs[2])
    cars = int(inputs[3])
    points = int(inputs[4])

    for i in range(streets):
        input = Lines[i+1]
        input = input.split()
        startIntersection = int(input[0])
        endIntersection = int(input[1])
        streetName = input[2]
        streetLenght = int(input[3])

        if endIntersection in interDic:
            temp = interDic[endIntersection]
            temp[streetName] = 0
            interDic[endIntersection] = temp
        else:
            theStreets = {}
            theStreets[streetName] = 0
            interDic[endIntersection] = theStreets


        if endIntersection in carsStartAt:
            temp = carsStartAt[endIntersection]
            temp[streetName] = 0
            carsStartAt[endIntersection] = temp
        else:
            theStreets = {}
            theStreets[streetName] = 0
            carsStartAt[endIntersection] = theStreets


        numStreet[streetName] = 0
        streetDic[streetName] = [startIntersection, endIntersection, streetLenght]

    for i in range(cars):
        input = Lines[i+1+streets]
        input = input.split()

        carNum = int(input[0])
        listOfStreet = input[1:]
        carsList.append(listOfStreet)
        temp = carsStartAt[streetDic[input[1]][1]]
        temp[input[1]] = temp[input[1]] +1
        carsStartAt[streetDic[input[1]][1]] = temp



    for car in carsList:
        for strr in car:
            numStreet[strr] = numStreet[strr] +1


    for streetInDic in numStreet.keys():
        temp = interDic[streetDic[streetInDic][1]]
        temp[streetInDic] = temp[streetInDic] + numStreet[streetInDic]

    #print (numStreet)
    #print(streetDic)
    #print(interDic)



    outputList = []
    for inter in interDic.keys():
        temp = interDic[inter]
        temp2 = carsStartAt[inter]
        temp2 = sorted(temp2.items(), key=lambda item: item[0], reverse=True)

        sums = 1
        streetsIn = []
        for st in temp.keys():
            sums += temp[st]
        for st in temp2:

            st = st[0]

            deltas = min(int(2 * (temp[st] / sums)), seconds - 1)

            if len(temp) == 1:
                streetsIn.append([st, 1])
            else:
                if deltas != 0:
                    streetsIn.append([st, deltas])
                else:
                    streetsIn.append([st, 1])


        if len(streetsIn) != 0:
            outputList.append([inter, len(streetsIn), streetsIn])



    def output(pList):
        f = open(l +"output.txt", "w+")
        # num of intersections

        f.write(str(len(pList)) + "\n")
        for i in range(len(pList)):
            f.write(str(outputList[i][0]))
            f.write("\n")
            f.write(str(outputList[i][1]))

            f.write("\n")
            for j in range(len(outputList[i][2])):
                f.write(str(outputList[i][2][j][0]) + " ")
                f.write(str(outputList[i][2][j][1]))
                f.write("\n")
            #f.write("\n")
        f.close()

    output(outputList)

    #print(carsStartAt)
    #print(outputList)

