# module for execute surface area & volume cube

from os import system, name
from modules.SolidGeometry.Cube.calculate import Cube
from modules.banners import cube_banner
from modules.wannaquit import question

def clear(): 
	# for windows 
	if name == 'nt': 
		_ = system('cls') 
	# for mac and linux(here, os.name is 'posix') 
	else: 
		_ = system('clear')

def Execute_Cube():
    clear()
    cube_banner()
    print("Calculate Cube Surface Area & Volume")
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