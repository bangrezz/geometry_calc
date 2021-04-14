# module for calculate surface area & volume rectangular prism

class RectangularPrism:
    def __init__(self,length, width, height):
        self.l = length
        self.w = width
        self.h = height

    def Calculating_Volume(self):
        global volume
        volume = self.l * self.w * self.h
        return volume

    def Calculating_SurfaceArea(self):
        global surface_area
        surface_area = 2*(self.l + self.w + self.h)
        return surface_area

    def Result(self):
        res = f"""\n
        ----------------------------------------------
                          CALCULATE
        ----------------------------------------------

        Length (l)                       = {self.l} cm
        
        Width (w)                        = {self.w} cm
        
        Height (h)                       = {self.h} cm

        Formula the rectangular 
        prism surface area               = 2 * (l + w + h)
                                         = 2 * ({self.l} cm + {self.w} cm + {self.h} cm)
        
        Formula the rectangular
        prism volume                     = l * w * h
                                         = {self.l} cm * {self.w} cm * {self.h} cm

        --------------------RESULT--------------------
        
        Rectangular prism surface area   = {surface_area} cm^2
        
        Rectangular prism volume           = {volume} cm^3
                    """
        return res