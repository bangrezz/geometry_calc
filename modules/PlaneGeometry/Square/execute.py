# module for execute area & perimeter square
from modules.clearscreen import clear
from modules.PlaneGeometry.Square.calculate import Square
from modules.banners import square_banner
from modules.PlaneGeometry.Square.wannaquit import MainQuestion
from rich import print

def Execute_Square():
    clear()
    square_banner()
    print("Calculate area and perimeter of the square")
    #initiating
    def Input_side():   #input side length
        try:
            global side
            side = float(input("\nEnter side length (s) = "))
            if side <= 0:print("[red][ERROR][/red] Invalid value. The value must greater than 0 !");Input_side()
        except ValueError:
            print("[red][ERROR][/red] Value error. Enter again !")
            Input_side()
        except KeyboardInterrupt:
            print("\n\nThank you for using Geometry Calc :)")
            exit()
    Input_side()    #return to Input_Side()
    ExecSquare = Square(side)
    ExecSquare.Calculating_Area();ExecSquare.Calculating_Perimeter()
    result = ExecSquare.Result();print(result)
    MainQuestion()