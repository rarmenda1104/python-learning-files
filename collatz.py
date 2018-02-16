
def collatz(number):
    if number % 2 == 0:
        return number // 2
        print(number)
    else:
        return 3 * number + 1
        print(number)

while True:
    try:
        value = int(input("Enter a number: "))
        break
    except ValueError:
        print('Type an integer, please.')
while value != 1:
    print(collatz(value))
    value = collatz(value)
