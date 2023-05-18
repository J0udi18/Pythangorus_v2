import math


def int_check(side_1=None):
    int_check("Please enter the length of the first side: ", 1)
    side_2 = int_check()("PLease enter the length of the second side: ", 1)
    hypotenuse = round(math.sqrt(side_1 ** 2 + side_2 **
                                2), 2)
    print(f"The length of the hypotenuse is {hypotenuse} units. ")


