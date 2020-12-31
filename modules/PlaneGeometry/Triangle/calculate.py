# module for calculate perimeter & area triangle

class TriangleArea:
    def __init__(self, base, height):
        self.b = base
        self.h = height

    def Calculating_Area(self): #calculate triangle area
        global area
        area = (self.b * self.h)/2    #triangle area formula
        return area

    def Result_Area(self):  #print result triangle area
        print_area = f"""\n
        ----------------------------------------------
                        CALCULATE AREA
        ----------------------------------------------

        Base (b)                    = {self.b} cm
        
        Height (h)                  = {self.h} cm
        
        Formula the triangle area   = (b * h)/2
                                    = ({self.b} cm * {self.h} cm)/2
        
        --------------------RESULT--------------------

        Triangle area               = {area} cm^2
                    """
        return print_area

class TrianglePerimeter:
    def __init__(self, side_a, side_b, side_c):
        self.a = side_a
        self.b = side_b
        self.c = side_c

    def Calculating_Perimeter(self):
        global perimeter
        perimeter = self.a + self.b + self.c     #triangle perimeter formula
        return perimeter

    def Result_Perimeter(self): #print result triangle perimeter
        print_perimeter = f"""\n
        ----------------------------------------------
                    CALCULATE PERIMETER
        ----------------------------------------------

        Side a                          = {self.a} cm
        
        Side b                          = {self.b} cm
        
        Side c                          = {self.c} cm
        
        Formula the triangle perimeter  = a + b + c
                                        = {self.a} cm + {self.b} cm + {self.c} cm

        --------------------RESULT--------------------

        Triangle perimeter              = {perimeter} cm
                    """
        return print_perimeter