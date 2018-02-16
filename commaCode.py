def comma(aList):
    count = 0
    aString = ''
    while count < len(aList)-1:
        aString += aList[count] + ', '
        count+=1
    return aString + 'and ' + aList[count]
        
spam = ['George', 'Kyle', 'Peter', 'Suzie']
print(comma(spam))



