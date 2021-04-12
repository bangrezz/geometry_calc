# module for execute area & circumference circle
from modules.clearscreen import clear
from modules.PlaneGeometry.Circle.calculate import Circle
from modules.banners import circle_banner
from modules.wannaquit import question

def Execute_Circle():
    clear()
    circle_banner()
    print("Calculate area and circumference of the circle")
    #initiating
    def Input_radius():   #input side length
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
    ExecCircle = Circle(radius,PI)
    ExecCircle.Calculating_Area();ExecCircle.Calculating_Circumference()
    result = ExecCircle.Result();print(result)
    question()