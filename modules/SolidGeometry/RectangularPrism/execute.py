# module for execute surface area & volume rectangular prism

from modules.clearscreen import clear
from modules.SolidGeometry.RectangularPrism.calculate import RectangularPrism
from modules.banners import rectangularprism_banner
from modules.wannaquit import question

def Execute_RectangularPrism():
    clear()
    rectangularprism_banner()
    print("Calculate surface area and volume of the rectangular prism")
    #initiating
    def Input_length():
        try:
            global length
            length = float(input("\nEnter length (l) = "))
            if length <= 0:print("[ERROR] The value must greater than 0 !");Input_length()
        except ValueError:
            print("[ERROR] Enter again !")
            Input_length()
        except KeyboardInterrupt:
            print("\n\nThank you for using Geometry Calc :)")
            exit()
    Input_length()
    def Input_width():
        try:
            global width
            width = float(input("\nEnter width (w)  = "))
            if width <= 0:print("[ERROR] The value must greater than 0 !");Input_width()
        except ValueError:
            print("[ERROR] Enter again !")
            Input_width()
        except KeyboardInterrupt:
            print("\n\nThank you for using Geometry Calc :)")
            exit()
    Input_width()
    def Input_height():
        try:
            global height
            height = float(input("\nEnter height (h)  = "))
            if height <= 0:print("[ERROR] The value must greater than 0 !");Input_height()
        except ValueError:
            print("[ERROR] Enter again !")
            Input_height()
        except KeyboardInterrupt:
            print("\n\nThank you for using Geometry Calc :)")
            exit()
    Input_height()
    if length == width == height:
        print("\n[WARN] The rectangular prism is a cube. Because the length, width, and height value are same.")
        def same_value():
            select = input("Are you sure to continue ? [y/n] : ")
            if select=='y':pass
            elif select=='n':
                input("\nPress <enter> to go to repeat enter value\n")
                rectangularprism_banner();print("Calculate Rectangular Prism Surface Area & Volume")
                Input_length();Input_width();Input_height()
            else:print("\n[ERROR] Please enter correctly");same_value()
        same_value()
    ExecRectangularPrism = RectangularPrism(length,width,height)
    ExecRectangularPrism.Calculating_Volume();ExecRectangularPrism.Calculating_SurfaceArea()
    result = ExecRectangularPrism.Result();print(result)
    question()