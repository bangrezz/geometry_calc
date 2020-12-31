from os import system, name
from rich import print
def clear(): 

	# for windows 
	if name == 'nt': 
		_ = system('cls') 

	# for mac and linux(here, os.name is 'posix') 
	else: 
		_ = system('clear')

def question():
    try:
        def Repeat():
            count_again = input("\nDo you want to count again ? [y/n] : ")
            if count_again == 'y':
                print("Press [blue]<enter>[/blue] to continue")
                input()
            elif count_again == 'n':
                print("\nThank you for using Geometry Calc :)")
                exit()
            else:
                print("[red][ERROR][/red] Invalid input. Repeat again !")
                Repeat()
        Repeat()
            
    except KeyboardInterrupt:
        print("\n\nThank you for using Geometry Calc :)")
        exit()