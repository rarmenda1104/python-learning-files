tableData = [['apples', 'oranges', 'cherries', 'banana'],
             ['Alice', 'Bob', 'Carol', 'David'],
             ['dogs', 'cats', 'moose', 'goose']]

def printTable(tableData):
    colWidths = [0] * len(tableData)
    for i in range(len(tableData)):
        for j in tableData[i]:
            if len(j) > colWidths[i]:
                colWidths[i]=len(j)

    for i in range(len(tableData[0])):
        for x in range(len(tableData)):
            print(tableData[x][i].rjust(colWidths[x]))
            if x == len(tableData)-1:
                print('\r')
printTable(tableData)
