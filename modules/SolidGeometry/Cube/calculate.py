# module for calculate surface area & volume cube

class Cube:
    def __init__(self, side):
        self.s = side

    def Calculating_Volume(self):
        global volume
        volume = self.s * self.s * self.s
        return volume

    def Calculating_SurfaceArea(self):
        global surface_area
        surface_area = 6 * self.s ** 2
        return surface_area

    def Result(self):
        res = f"""\n
        ----------------------------------------------
                          CALCULATE
        ----------------------------------------------

        Side (s)                       = {self.s} cm       
        
        Formula the cube surface area  = 6 * s^2
                                       = 6 * ({self.s})^2 cm
        
        Formula the cube volume        = s * s * s
                                       = {self.s} cm * {self.s} cm * {self.s} cm

        --------------------RESULT--------------------
        
        Cube surface area              = {surface_area} cm^2
        
        Cube volume                    = {volume} cm^3
                    """
        return res