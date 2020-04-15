def isDigitPresent(x, d):
    # Breal loop if d is present as digit
    while (x > 0):

        if (x % 10 == d):
            break

        x = x / 10

    # If loop broke
    return (x > 0)


# function to display the values
def printNumbers(n, d):
    # Check all numbers one by one
    for i in range(0, n + 1):

        # checking for digit
        if (i == d or isDigitPresent(i, d)):
            print(i, end=" ")

for _ in range(int(input())):
    n =int(input())
    d = int(input())
    printNumbers(n,d)
