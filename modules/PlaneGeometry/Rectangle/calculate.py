#module for calculate area & perimeter rectangle

class Rectangle:
    def __init__(self, length, width):
        self.l = length
        self.w = width

    def Calculating_Area(self):
        global area
        area = self.l * self.w
        return area

    def Calculating_Perimeter(self):
        global perimeter
        perimeter = 2*(self.l + self.w)
        return perimeter

    def Result(self):
        res = f"""\n
        ----------------------------------------------
                          CALCULATE
        ----------------------------------------------

        Length (l)                          = {self.l} cm
        
        Width (w)                           = {self.w} cm
        
        Formula the rectangle perimeter     = 2 * (l + w)
                                            = 2 * ({self.l} cm + {self.w} cm)

        Formula the rectangle area          = l * w
                                            = {self.l} cm * {self.w} cm

        --------------------RESULT--------------------
        
        Rectangle perimeter                 = {perimeter} cm
        
        Rectangle area                      = {area} cm^2
                    """
        return res