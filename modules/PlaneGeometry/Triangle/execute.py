# module for execute area & perimeter triangle and pythagorean

from modules.clearscreen import clear
from modules.PlaneGeometry.Triangle.calculate import TriangleArea, TrianglePerimeter
from modules.PlaneGeometry.Triangle.pythagorean import Pythagorean_Side_a, Pythagorean_Side_b, Pythagorean_Hypotenuse
from modules.wannaquit import question

def Execute_Area():
    clear()
    print("Calculate area of the triangle")
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
    # execute triangle area
    area = TriangleArea(Base, Height)
    area.Calculating_Area()
    result = area.Result_Area()
    print(result)
    question()

def Execute_Perimeter():
    clear()
    print("Calculate perimeter of the triangle")
    #initiating
    def Input_side_a(): #side a
        try:
            global a
            a = float(input("\nEnter the length of side a = "))
            if a <= 0:print("[ERROR] The value must greater than 0 !");Input_side_a()
        except ValueError:
            print("[ERROR] Enter again !")
            Input_side_a()
        except KeyboardInterrupt:
            print("\n\nThank you for using Geometry Calc :)")
            exit()
    Input_side_a()
    def Input_side_b(): #side b
        try:
            global b
            b = float(input("\nEnter the length of side b = "))
            if b <= 0:print("[ERROR] The value must greater than 0 !");Input_side_b()
        except ValueError:
            print("[ERROR] Enter again !")
            Input_side_b()
        except KeyboardInterrupt:
            print("\n\nThank you for using Geometry Calc :)")
            exit()
    Input_side_b()
    def Input_side_c(): #side c
        try:
            global c
            c = float(input("\nEnter the length of side c = "))
            if c <= 0:print("[ERROR] The value must greater than 0 !");Input_side_c()
        except ValueError:
            print("[ERROR] Enter again !")
            Input_side_c()
        except KeyboardInterrupt:
            print("\n\nThank you for using Geometry Calc :)")
            exit()
    Input_side_c()
    # execute triangle perimeter
    perimeter = TrianglePerimeter(a, b, c)
    perimeter.Calculating_Perimeter()
    result = perimeter.Result_Perimeter()
    print(result)
    question()

class Execute_Pythagorean:
    def Execute_side_a(self):  # function for find side a
        clear()
        print("--- Find Side A of Pythagorean ---")
        #initiating
        def Input_side_b(): # side b
            try:
                global b
                b = float(input("\nEnter the length of side b = "))
                if b <= 0:print("[ERROR] The value must greater than 0 !");Input_side_b()
            except ValueError:
                print("[ERROR] Enter again !")
                Input_side_b()
            except KeyboardInterrupt:
                print("\n\nThank you for using Geometry Calc :)")
                exit()
        Input_side_b()
        def Input_side_c(): #side hypotenuse c
            try:
                global c
                c = float(input("\nEnter the length of side hypotenuse (c) = "))
                if c <= 0:print("[ERROR] The value must greater than 0 !");Input_side_c()
                if c <= b:
                    print("\n[ERROR] The value of side hypotenuse (c) must greater than side b. Please repeat again !")
                    input("Press <enter> to continue\n\n")
                    print("--- Find Side A of Pythagorean ---")
                    Input_side_b();Input_side_c()
            except ValueError:
                print("[ERROR] Enter again !")
                Input_side_c()
            except KeyboardInterrupt:
                print("\n\nThank you for using Geometry Calc :)")
                exit()
        Input_side_c()
        # execute side a
        ExecSide_a = Pythagorean_Side_a(b,c)
        ExecSide_a.Find_Side_a()
        result = ExecSide_a.Result_Side_a(); print(result)
        question()

    def Execute_side_b(self):  # function for find side b
        clear()
        print("--- Find Side B of Pythagorean ---")
        #initiating
        def Input_side_a(): #side a
            try:
                global a
                a = float(input("\nEnter the length of side a = "))
                if a <= 0:print("[ERROR] The value must greater than 0 !");Input_side_a()
            except ValueError:
                print("[ERROR] Enter again !")
                Input_side_a()
            except KeyboardInterrupt:
                print("\n\nThank you for using Geometry Calc :)")
                exit()
        Input_side_a()
        def Input_side_c(): #side hypotenuse c
            try:
                global c
                c = float(input("\nEnter the length of side hypotenuse (c) = "))
                if c <= 0:print("[ERROR] The value must greater than 0 !");Input_side_c()
                if c <= a:
                    print("\n[ERROR] The value of side hypotenuse (c) must greater than side a. Please repeat again !")
                    input("Press <enter> to continue\n\n")
                    print("--- Find Side B of Pythagorean ---")
                    Input_side_a();Input_side_c()
            except ValueError:
                print("[ERROR] Enter again !")
                Input_side_c()
            except KeyboardInterrupt:
                print("\n\nThank you for using Geometry Calc :)")
                exit()
        Input_side_c()
        # execute side b
        ExecSide_b = Pythagorean_Side_b(a,c)
        ExecSide_b.Find_Side_b()
        result = ExecSide_b.Result_Side_b(); print(result)
        question()

    def Execute_Hypotenuse(self):  # function for find side hypotenuse
        clear()
        print("--- Find Side Hypotenuse (c) of Pythagorean ---")
        #initiating
        def Input_side_a(): #side a
            try:
                global a
                a = float(input("\nEnter the length of side a = "))
                if a <= 0:print("[ERROR] The value must greater than 0 !");Input_side_a()
            except ValueError:
                print("[ERROR] Enter again !")
                Input_side_a()
            except KeyboardInterrupt:
                print("\n\nThank you for using Geometry Calc :)")
                exit()
        Input_side_a()
        def Input_side_b(): # side b
            try:
                global b
                b = float(input("\nEnter the length of side b = "))
                if b <= 0:print("[ERROR] The value must greater than 0 !");Input_side_b()
            except ValueError:
                print("[ERROR] Enter again !")
                Input_side_b()
            except KeyboardInterrupt:
                print("\n\nThank you for using Geometry Calc :)")
                exit()
        Input_side_b()
        # execute side hypotenuse
        Exec_Hypotenuse = Pythagorean_Hypotenuse(a,b)
        Exec_Hypotenuse.Find_Hypotenuse()
        result = Exec_Hypotenuse.Result_Hypotenuse(); print(result)
        question()