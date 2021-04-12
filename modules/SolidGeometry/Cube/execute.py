# module for execute surface area & volume cube

from modules.clearscreen import clear
from modules.SolidGeometry.Cube.calculate import Cube
from modules.banners import cube_banner
from modules.wannaquit import question

def Execute_Cube():
    clear()
    cube_banner()
    print("Calculate surface area and volume of the cube")
    #initiating
    def Input_side():   #input side length
        try:
            global side
            side = float(input("\nEnter side length (s) = "))
            if side <= 0:print("[ERROR] The value must greater than 0 !");Input_side()
        except ValueError:
            print("[ERROR] Enter again !")
            Input_side()
        except KeyboardInterrupt:
            print("\n\nThank you for using Geometry Calc :)")
            exit()
    Input_side()    #return to Input_Side()
    ExecCube = Cube(side)
    ExecCube.Calculating_Volume();ExecCube.Calculating_SurfaceArea()
    result = ExecCube.Result();print(result)
    question()