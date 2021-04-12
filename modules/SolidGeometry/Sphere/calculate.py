# module for calculate surface area & volume sphere

class Sphere:
    def __init__(self, radius, PI):
        self.r  = radius
        self.PI = PI

    def Calculating_Volume(self):
        global volume
        volume = 4/3 * self.PI * self.r ** 3
        return volume

    def Calculating_SurfaceArea(self):
        global surface_area
        surface_area = 4 * self.PI * self.r ** 2
        return surface_area

    def Result(self):
        res = f"""\n
        ----------------------------------------------
                          CALCULATE
        ----------------------------------------------

        Radius (r)                       = {self.r} cm

        Pi value (π)                     = {self.PI}       
        
        Formula the sphere surface area  = 4 * π * r^2
                                         = 4 * {self.PI} * ({self.r})^2 cm
        
        Formula the sphere volume        = 4/3 * π * r^3
                                         = 4/3 * {self.PI} * ({self.r})^3 cm

        --------------------RESULT--------------------
        
        Sphere surface area              = {surface_area} cm^2
        
        Sphere volume                    = {volume} cm^3
                    """
        return res