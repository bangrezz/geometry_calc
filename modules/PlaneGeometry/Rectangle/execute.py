# module for execute area & perimeter square

from os import system, name
from modules.PlaneGeometry.Rectangle.calculate import Rectangle
from modules.banners import rectangle_banner
from modules.wannaquit import question

def clear(): 
	# for windows 
	if name == 'nt': 
		_ = system('cls') 
	# for mac and linux(here, os.name is 'posix') 
	else: 
		_ = system('clear')

def Execute_Rectangle():
    clear()
    rectangle_banner()
    print("Calculate Rectangle Area & Perimeter")
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
    if length == width:
        print("\n[WARN] The rectangle is a square. Because the length value as same as the width value.")
        def width_sameAs_length():
            select = input("Are you sure to continue ? [y/n] : ")
            if select=='y':pass
            elif select=='n':
                input("\nPress <enter> to go to repeat enter value\n")
                rectangle_banner();print("Calculate Rectangle Area & Perimeter")
                Input_length();Input_width()
            else:print("\n[ERROR] Please enter correctly");width_sameAs_length()
        width_sameAs_length()
    ExecRectangle = Rectangle(length,width)
    ExecRectangle.Calculating_Area();ExecRectangle.Calculating_Perimeter()
    result = ExecRectangle.Result();print(result)
    question()