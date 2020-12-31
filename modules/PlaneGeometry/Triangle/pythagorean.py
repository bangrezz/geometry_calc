# module for calculate pythagorean
import math

class Pythagorean_Side_a:
    def __init__(self, side_b, side_c):
        self.b = side_b
        self.c = side_c
    def Find_Side_a(self):    #for calculate side a
        global side_a
        side_a = math.sqrt(self.c**2 - self.b**2)
        return side_a

    def Result_Side_a(self):    # print result side a
        print_side_a = f"""\n
        ----------------------------------------------
                        CALCULATE SIDE A
        ----------------------------------------------

        Side b                      = {self.b} cm
        
        Hypotenuse (c)              = {self.c} cm

        Formula the side a          = sqrt(c^2 - b^2) 
                                    = sqrt(({self.c})^2 cm - ({self.b})^2 cm)

        --------------------RESULT--------------------

        Side a                      = {side_a} cm
                    """
        return print_side_a

class Pythagorean_Side_b:
    def __init__(self, side_a, side_c):
        self.a = side_a
        self.c = side_c

    def Find_Side_b(self):    #for calculate side b
        global side_b
        side_b = math.sqrt(self.c**2 - self.a**2)
        return side_b

    def Result_Side_b(self):    # print result side b
        print_side_b = f"""\n
        ----------------------------------------------
                        CALCULATE SIDE B
        ----------------------------------------------

        Side a                      = {self.a} cm
        
        Hypotenuse (c)              = {self.c} cm

        Formula the side b          = sqrt(c^2 - a^2) 
                                    = sqrt(({self.c})^2 cm - ({self.a})^2 cm)

        --------------------RESULT--------------------

        Side b                      = {side_b} cm
                    """
        return print_side_b

class Pythagorean_Hypotenuse:
    def __init__(self, side_a, side_b):
        self.a = side_a
        self.b = side_b

    def Find_Hypotenuse(self):    #for calculate side c
        global side_c
        side_c = math.sqrt(self.a**2 + self.b**2)
        return side_c

    def Result_Hypotenuse(self):    # print result side c
        print_side_b = f"""\n
        ----------------------------------------------
                    CALCULATE HYPOTENUSE
        ----------------------------------------------

        Side a                      = {self.a} cm
        
        Side b                      = {self.b} cm

        Formula the hypotenuse (c)  = sqrt(a^2 + b^2) 
                                    = sqrt(({self.a})^2 cm + ({self.b})^2 cm)

        --------------------RESULT--------------------

        Side c                      = {side_c} cm
                    """
        return print_side_b