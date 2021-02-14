# module for execute area & perimeter square
from os import system, name
from modules.PlaneGeometry.Square.calculate import Square
from modules.banners import square_banner
from modules.wannaquit import question

def clear(): 
	# for windows 
	if name == 'nt': 
		_ = system('cls') 
	# for mac and linux(here, os.name is 'posix') 
	else: 
		_ = system('clear')

def Execute_Square():
    clear()
    square_banner()
    print("Calculate area and perimeter of the square")
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
    ExecSquare = Square(side)
    ExecSquare.Calculating_Area();ExecSquare.Calculating_Perimeter()
    result = ExecSquare.Result();print(result)
    question()