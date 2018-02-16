myList1 =[['apple', 'Jacob', 'fire hazard', 'Jameson', 'whiskey'],
          ['orange', 'Kevin', 'Zulu', 'Fox', 'Mark'],
          ['Snake', 'George', 'Golf' , 'Tennis', 'range'],
          ['Snake', 'George', 'Golf' , 'Tennis', 'rage']]

def neatPrint(x):
    colWidths = [0] * len(myList1)
    for i in range(len(myList1)):
        for j in range(len(myList1[i])):
            if colWidths[i] <= len(myList1[i][j]):
                colWidths[i] = len(myList1[i][j])
            else:
                colWidths[i] = colWidths[i]

    for k in range(len(myList1[0])):
        for l in range(len(myList1)):
            print(myList1[l][k].center(colWidths[l]), end = " ")
        print()

neatPrint(myList1)
