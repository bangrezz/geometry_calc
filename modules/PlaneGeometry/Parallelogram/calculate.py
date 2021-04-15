#parallelogram

class Parallelogram:
    def __init__(self, base, height):
        self.b  = base
        self.h  = height
    
    def Calculating_Area(self):
        global area
        area = self.b * self.h
        return area
    
    def Calculating_Perimeter(self):
        global perimeter
        perimeter = 2 * (self.b + self.h)
        return perimeter
    
    def Result(self):
        res = f"""\n
        ----------------------------------------------
                          CALCULATE
        ----------------------------------------------

        Base (b)                        = {self.b} cm

        Height (h)                      = {self.h} cm       

        Formula the parallelogram 
        perimeter                       = 2 (b + h)
                                        = 2 ({self.b} cm + {self.h} cm)
        
        Formula the parallelogram area  = b * h
                                        = {self.b} cm * {self.h} cm

        --------------------RESULT--------------------

        Parallelogram perimeter         = {perimeter} cm

        Parallelogram area              = {area} cm^2
                    """
        return res