from modules.clearscreen import clear
from rich import print

class TriangleQuestion:
    def AreaQuestion(self):
        print("""
            ________________________________________________
            What you want to do ?
            
            1. Count again
            2. Go to the previous menu
            99. Exit
            """)
        def select_question():
            try:
                select = int(input("Select : "))
                if select == 1:
                    from modules.PlaneGeometry.Triangle.execute import Execute_Area
                    Execute_Area()
                elif select == 2:
                    print("Press [blue]<enter>[/blue] to continue")
                    input()
                elif select == 99:
                    print("\n\nThank you for using Geometry Calc :)")
                    exit()
                else:
                    print("[red][ERROR][/red] Invalid input. Enter again !")
                    select_question()
            except ValueError:
                print("[red][ERROR][/red] Value error. Enter again !")
                select_question()
            except KeyboardInterrupt:
                print("\n\nThank you for using Geometry Calc :)")
                exit()
        select_question()

    def PerimeterQuestion(self):
        print("""
            ________________________________________________
            What you want to do ?
            
            1. Count again
            2. Go to the previous menu
            99. Exit
            """)
        def select_question():
            try:
                select = int(input("Select : "))
                if select == 1:
                    from modules.PlaneGeometry.Triangle.execute import Execute_Perimeter
                    Execute_Perimeter()
                elif select == 2:
                    print("Press [blue]<enter>[/blue] to continue")
                    input()
                elif select == 99:
                    print("\n\nThank you for using Geometry Calc :)")
                    exit()
                else:
                    print("[red][ERROR][/red] Invalid input. Enter again !")
                    select_question()
            except ValueError:
                print("[red][ERROR][/red] Value error. Enter again !")
                select_question()
            except KeyboardInterrupt:
                print("\n\nThank you for using Geometry Calc :)")
                exit()
        select_question()

class PythagoreanQuestion:
    def A_Question(self):
        print("""
        ________________________________________________
        What you want to do ?
        
        1. Count again
        2. Go to the previous menu
        99. Exit
        """)
        def select_question():
            try:
                select = int(input("Select : "))
                if select == 1:
                    from modules.PlaneGeometry.Triangle.execute import Execute_Pythagorean
                    side_a = Execute_Pythagorean()
                    side_a.Execute_side_a()
                elif select == 2:
                    print("Press [blue]<enter>[/blue] to continue")
                    input()
                elif select == 99:
                    print("\n\nThank you for using Geometry Calc :)")
                    exit()
                else:
                    print("[red][ERROR][/red] Invalid input. Enter again !")
                    select_question()
            except ValueError:
                print("[red][ERROR][/red] Value error. Enter again !")
                select_question()
            except KeyboardInterrupt:
                print("\n\nThank you for using Geometry Calc :)")
                exit()
        select_question()

    def B_Question(self):
        print("""
        ________________________________________________
        What you want to do ?
        
        1. Count again
        2. Go to the previous menu
        99. Exit
        """)
        def select_question():
            try:
                select = int(input("Select : "))
                if select == 1:
                    from modules.PlaneGeometry.Triangle.execute import Execute_Pythagorean
                    side_b = Execute_Pythagorean()
                    side_b.Execute_side_b
                elif select == 2:
                    print("Press [blue]<enter>[/blue] to continue")
                    input()
                elif select == 99:
                    print("\n\nThank you for using Geometry Calc :)")
                    exit()
                else:
                    print("[red][ERROR][/red] Invalid input. Enter again !")
                    select_question()
            except ValueError:
                print("[red][ERROR][/red] Value error. Enter again !")
                select_question()
            except KeyboardInterrupt:
                print("\n\nThank you for using Geometry Calc :)")
                exit()
        select_question()

    def C_Question(self):
        print("""
        ________________________________________________
        What you want to do ?
        
        1. Count again
        2. Go to the previous menu
        99. Exit
        """)
        def select_question():
            try:
                select = int(input("Select : "))
                if select == 1:
                    from modules.PlaneGeometry.Triangle.execute import Execute_Pythagorean
                    side_c = Execute_Pythagorean()
                    side_c.Execute_Hypotenuse()
                elif select == 2:
                    print("Press [blue]<enter>[/blue] to continue")
                    input()
                elif select == 99:
                    print("\n\nThank you for using Geometry Calc :)")
                    exit()
                else:
                    print("[red][ERROR][/red] Invalid input. Enter again !")
                    select_question()
            except ValueError:
                print("[red][ERROR][/red] Value error. Enter again !")
                select_question()
            except KeyboardInterrupt:
                print("\n\nThank you for using Geometry Calc :)")
                exit()
        select_question()