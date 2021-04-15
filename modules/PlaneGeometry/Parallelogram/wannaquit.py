from modules.clearscreen import clear
from rich import print

def MainQuestion():
    print("""
        ________________________________________________
        What you want to do ?
        
        1. Count again
        2. Go to the previous menu
        99. Exit
        """)
    def question():
        try:
            select = int(input("Select : "))
            if select == 1:
                from modules.PlaneGeometry.Parallelogram.execute import Execute_Parallelogram
                Execute_Parallelogram()
            elif select == 2:
                print("Press [blue]<enter>[/blue] to continue")
                input()
            elif select == 99:
                print("\n\nThank you for using Geometry Calc :)")
                exit()
            else:
                print("[red][ERROR][/red] Invalid input. Enter again !")
                question()
        except ValueError:
            print("[red][ERROR][/red] Value error. Enter again !")
            question()
        except KeyboardInterrupt:
            print("\n\nThank you for using Geometry Calc :)")
            exit()
    question()