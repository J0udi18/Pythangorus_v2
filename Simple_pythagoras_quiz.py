from math import sqrt

def getLength() :
    length = float(input("please enter length of Triangle side"))
    return length

side1 = getLength ()
side2 = getLength ()

def calcTriangle(side1, side2):
    side3 = sqrt(side1 * side1 + side2 * side2)
    print("The length of your third side is: %.2f" % side3)


calcTriangle(side1, side2)