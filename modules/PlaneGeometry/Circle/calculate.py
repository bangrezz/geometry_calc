#module for calculate area & circumference circle

class Circle:
    def __init__(self, radius, PI):
        self.r = radius
        self.PI = PI
    
    def Calculating_Area(self):
        global area
        area = self.PI * self.r ** 2
        return area
    
    def Calculating_Circumference(self):
        global perimeter
        perimeter = 2 * self.PI * self.r
        return perimeter
    
    def Result(self):
        res = f"""\n
        ----------------------------------------------
                          CALCULATE
        ----------------------------------------------

        Radius (r)                       = {self.r} cm

        Pi value (π)                     = {self.PI}       
        
        Formula the circle perimeter     = 2 * π * r
                                         = 2 * {self.PI} * {self.r} cm
        
        Formula the circle area          = π * r^2
                                         = {self.PI} * ({self.r})^2 cm

        --------------------RESULT--------------------
        
        Circle perimeter                 = {perimeter} cm
        
        Circle area                      = {area} cm^2
                    """
        return res