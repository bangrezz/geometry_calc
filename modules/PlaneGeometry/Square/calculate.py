# module for calculate area & perimeter square

class Square:
    def __init__(self, side):
        self.s = side

    def Calculating_Area(self):
        global area
        area = self.s * self.s
        return area

    def Calculating_Perimeter(self):
        global perimeter
        perimeter = 4 * self.s
        return perimeter

    def Result(self):
        res = f"""\n
        ----------------------------------------------
                          CALCULATE
        ----------------------------------------------

        Side (s)                       = {self.s} cm       
        
        Formula the square perimeter   = 4 * s
                                       = 4 * {self.s} cm
        
        Formula the square area        = s * s
                                       = {self.s} cm * {self.s} cm

        --------------------RESULT--------------------
        
        Square perimeter               = {perimeter} cm
        
        Square area                    = {area} cm^2
                    """
        return res