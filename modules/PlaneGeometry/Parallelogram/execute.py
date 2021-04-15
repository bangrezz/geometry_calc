# execute parralelogram
from modules.clearscreen import clear
from modules.PlaneGeometry.Parallelogram.calculate import Parallelogram
from modules.banners import parallelogram_banner
from modules.PlaneGeometry.Parallelogram.wannaquit import MainQuestion

def Execute_Parallelogram():
    clear()
    parallelogram_banner()
    print("Calculate area and perimeter of the parallelogram")
    #initiating
    def Input_Base():   #input base length
        try:
            global Base
            Base = float(input("\nEnter base length (b) = "))
            if Base <= 0:print("[ERROR] The value must greater than 0 !");Input_Base()
        except ValueError:
            print("[ERROR] Enter again !")
            Input_Base()
        except KeyboardInterrupt:
            print("\n\nThank you for using Geometry Calc :)")
            exit()
    Input_Base()    #return to Input_Base()
    def Input_Height(): #input height length
        try:
            global Height
            Height = float(input("\nEnter height length (h) = "))
            if Height <= 0:print("[ERROR] The value must greater than 0 !");Input_Height()
        except ValueError:
            print("[ERROR] Enter again !")
            Input_Height()
        except KeyboardInterrupt:
            print("\n\nThank you for using Geometry Calc :)")
            exit()
    Input_Height()  #return to Input_Height()
    ExecParallelogram = Parallelogram(Base, Height)
    ExecParallelogram.Calculating_Area();ExecParallelogram.Calculating_Perimeter()
    result = ExecParallelogram.Result();print(result)
    MainQuestion()