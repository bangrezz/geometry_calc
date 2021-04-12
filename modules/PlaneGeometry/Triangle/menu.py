from modules.clearscreen import clear
from modules.PlaneGeometry.Triangle.execute import Execute_Area, Execute_Perimeter,  Execute_Pythagorean
from modules.banners import triangle_banner, pythagorean_banner

# pythagorean main menu, triangle submenu
def __pythagorean__():
    clear()
    pythagorean_banner() # print banner and pythagorean main menu
    def select_pythagorean():
        try:
            select_menu = int(input("\n\t  Select from the menu [ 1 | 2 | 3 | 99 ] : "))
            if select_menu == 1:
                Executes_1 = Execute_Pythagorean(); Executes_1.Execute_side_a()
                __pythagorean__()
            elif select_menu == 2:
                Executes_2 = Execute_Pythagorean(); Executes_2.Execute_side_b() 
                __pythagorean__()
            elif select_menu == 3:
                Executes_3 = Execute_Pythagorean(); Executes_3.Execute_Hypotenuse()
                __pythagorean__()
            elif select_menu == 99:
                clear()
            else:
                print("\n\t  [ERROR] Select the menu correctly !")
                select_pythagorean()
        except ValueError:
            print("\n\t  [ERROR] Your selection is invalid. Repeat again !")
            select_pythagorean()
        except KeyboardInterrupt:
            print("\n\n\t  Thank you for using Geometry Calc :)")
            exit()
    select_pythagorean()

# triangle main menu
def __triangle__():
    clear()
    triangle_banner() # print banner and triangle main menu
    def select_triangle():
        try:
            select_menu = int(input("\n\t  Select from the menu [ 1 | 2 | 3 | 99 ] : "))

            if select_menu == 1:
                Execute_Area()  #for execute triangle area
                __triangle__()
            elif select_menu == 2:
                Execute_Perimeter()
                __triangle__()
            elif select_menu == 3:
                __pythagorean__() #go to pythagorean main menu
                __triangle__()
            elif select_menu == 99:
                clear() # go to Plane Geometry main menu
            else:
                print("\n\t  [ERROR] Select the menu correctly !")
                select_triangle()
        except ValueError:
            print("\n\t  [ERROR] Your selection is invalid. Repeat again !")
            select_triangle()
        except KeyboardInterrupt:
            print("\n\n\t  Thank you for using Geometry Calc :)")
            exit()
    select_triangle()