# module for calculate cylinder

class Cylinder:
    def __init__(self, radius, height, PI):
        self.r  = radius
        self.PI = PI
        self.h  = height
        
    def Calculating_Volume(self):
        global volume
        volume = self.PI * self.r ** 2 * self.h     # π * r^2 * h
        return volume
    
    def Calculating_SurfaceArea(self):
        global surface_area
        surface_area = 2 * self.PI * self.r * (self.h + self.r)
        return surface_area
    
    def Result(self):
        res = f"""\n
        ----------------------------------------------
                          CALCULATE
        ----------------------------------------------

        Radius (r)                       = {self.r} cm
        
        Height (h)                       = {self.h} cm
        
        Pi value (π)                     = {self.PI}       
        
        Formula the closed cylinder
        surface area                     = 2 * π * r (h + r) 
                                         = 2 * {self.PI} * {self.r} cm ({self.h} cm + {self.r} cm)
        
        Formula the cylinder volume      = π * r^2 * h
                                         = {self.PI} * {self.r}^2 cm * {self.h} cm

        --------------------RESULT--------------------
        
        Sphere surface area              = {surface_area} cm^2
        
        Sphere volume                    = {volume} cm^3
                    """
        return res