# module for execute area & perimeter square

from modules.clearscreen import clear
from modules.PlaneGeometry.Rectangle.calculate import Rectangle
from modules.banners import rectangle_banner
from modules.PlaneGeometry.Rectangle.wannaquit import MainQuestion
from rich import print

def Execute_Rectangle():
    clear()
    rectangle_banner()
    print("Calculate area and perimeter of the rectangle")
    #initiating
    def Input_length():
        try:
            global length
            length = float(input("\nEnter length (l) = "))
            if length <= 0:print("[red][ERROR][/red] Invalid value. The value must greater than 0 !");Input_length()
        except ValueError:
            print("[red][ERROR][/red] Value error. Enter again !")
            Input_length()
        except KeyboardInterrupt:
            print("\n\nThank you for using Geometry Calc :)")
            exit()
    Input_length()
    def Input_width():
        try:
            global width
            width = float(input("\nEnter width (w)  = "))
            if width <= 0:print("[red][ERROR][/red] Invalid value. The value must greater than 0 !");Input_width()
        except ValueError:
            print("[red][ERROR][/red] Value error. Enter again !")
            Input_width()
        except KeyboardInterrupt:
            print("\n\nThank you for using Geometry Calc :)")
            exit()
    Input_width()
    if length == width:
        print(f"\n[yellow][WARN][/yellow] The rectangle is a square. Because the length value ({length}) as same as the width value ({width}).")
        def width_sameAs_length():
            select = input("Are you sure to continue ? [y/n] : ")
            if select=='y':pass
            elif select=='n':
                print("\nPress [magenta]<enter>[/magenta] to go to repeat enter value\n");input()
                rectangle_banner();print("Calculate Rectangle Area & Perimeter")
                Input_length();Input_width()
            else:print("\n[red][ERROR][/red] Please enter correctly");width_sameAs_length()
        width_sameAs_length()
    ExecRectangle = Rectangle(length,width)
    ExecRectangle.Calculating_Area();ExecRectangle.Calculating_Perimeter()
    result = ExecRectangle.Result();print(result)
    MainQuestion()