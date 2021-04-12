# module for execute surface area & volume sphere

from os import system, name
from modules.SolidGeometry.Sphere.calculate import Sphere
from modules.banners import sphere_banner
from modules.wannaquit import question

def clear(): 
	# for windows 
	if name == 'nt': 
		_ = system('cls') 
	# for mac and linux(here, os.name is 'posix') 
	else: 
		_ = system('clear')

def Execute_Sphere():
    clear()
    sphere_banner()
    print("Calculate surface area and volume of the sphere")
    #initiating
    def Input_radius():
        try:
            global radius
            radius = float(input("\nEnter radius length (r) = "))
            if radius <= 0:print("[ERROR] The value must greater than 0 !");Input_radius()
        except ValueError:
            print("[ERROR] Enter again !")
            Input_radius()
        except KeyboardInterrupt:
            print("\n\nThank you for using Geometry Calc :)")
            exit()
    Input_radius()
    def Input_pi():
        try:
            global PI
            # select pi value
            select_pi = input("\nUsing pi (π) default value : 3.14 ? [y/n] = ")
            if select_pi == 'y':PI = 3.14   # set default pi value to 3.14
            elif select_pi == 'n':
                print("""\n\n[NOTE] pi value must 3.14. But, you can custom decimal value of pi. 
Example : 3.14159""")
                PI = float(input("\nEnter custom pi value (π) = "))
            else:print("\n[ERROR] Please enter correctly");Input_pi()
        except ValueError:
            print("[ERROR] Enter again !")
            Input_pi()
        except KeyboardInterrupt:
            print("\n\nThank you for using Geometry Calc :)")
            exit()
    Input_pi()
    ExecSphere = Sphere(radius,PI)
    ExecSphere.Calculating_Volume();ExecSphere.Calculating_SurfaceArea()
    result = ExecSphere.Result();print(result)
    question()