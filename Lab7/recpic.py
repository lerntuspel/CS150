#recpic.py
import drawing

#only loop for integer validation
def choiceInput(message):
    isint = False
    x = None
    while (isint==False):
        try:
            x = input(message)
            x = int(x)
            if ((x==1)or(x==2)):
                isint = True
                return x
            else:
                print("Please enter either 1 or 2")
        except ValueError:
            print("Not an integer, Try again.")

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


#size is the legth of one side of the section(1/9)
def carpet(canvas, x, y, size, depth):
    #base case depth = 0
    if depth == 0:
        return
    #Draw some squares
    canvas.drawRectFill(x+size//3, y+size//3, size//3, size//3)
    #Recurse to the 8 sub sections
    #Upper left
    carpet(canvas, x, y, size//3, depth-1)
    #Upper Mid
    carpet(canvas, x+size//3, y, size//3, depth-1)
    #Upper Right
    carpet(canvas, x+2*size//3, y, size//3, depth-1)
    #Mid Left
    carpet(canvas, x, y+size//3, size//3, depth-1)
    #Mid Right
    carpet(canvas, x+2*size//3, y+size//3, size//3, depth-1)
    #Lower Left
    carpet(canvas, x, y+2*size//3, size//3, depth-1)
    #Lower Mid
    carpet(canvas, x+size//3, y+2*size//3, size//3, depth-1)
    #Lower Right
    carpet(canvas, x+2*size//3, y+2*size//3, size//3, depth-1)

#x,y describe the upper left tip of the triangle
#size is width and hight of square that fits the triangle
def gasket(canvas, x, y, size, depth):
    #base case
    if depth == 1:
        return
    #Draw antitriangle
    canvas.drawPolygonFill([(x,y),(x+size,y),(x+size/2,y+size)])
    #Recurse around
    #Lower Left
    gasket(canvas, x-size/4, y+size/2, size/2, depth-1)
    #Lower Right
    gasket(canvas, x+3*size/4, y+size/2, size/2, depth-1)
    #Upper Mid
    gasket(canvas, x+size/4, y-size/2, size/2, depth-1)

print("Welcome to recursive pic")
print("1. carpet")
print("2. gasket")
choice = 0
print("Enter the number corresponding to the pattern you wish to see: ")
choice = choiceInput("")
print("Enter the size of the Canvas: ")
s = intInput("")
print("Enter the depth of recusions you wnat to see: ")
d = intInput("")

pic = drawing.Drawing(s,s)
pic.setFillColor(135,110,231)
pic.setOutlineColor(135,110,231)

if choice==1:
    carpet(pic,0,0, s, d)
else:
    pic.drawPolygonFill([(0,s),(s,s),(s/2,0)])
    pic.setFillColor(255,255,255)
    pic.setOutlineColor(255,255,255)
    gasket(pic, s/4, s/2, s/2, d)
