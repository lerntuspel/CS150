#recnum.py
def intInput(message):
    isint = False
    x = None
    while (isint==False):
        try:
            x = input(message)
            x = int(x)
            if (x>=1):
                isint = True
                return x
            else:
                print("Please enter a number greater than zero")
        except ValueError:
            print("Not an integer, Try again.")


def power(a,b):
    if b == 1:
        return a
    else:
        return (a*power(a,b-1))

def pSquares(a):
    if a == 1:
        return 1
    else:
        return (power(a,2) + pSquares(a-1))


n = intInput("Enter positive number for n: ")
k = intInput("Enter positive number for k: ")
print(n, "raised to the power of", k, "is", power(n,k))
print("The sum of the first",n ,"perfect squares is", pSquares(n))
