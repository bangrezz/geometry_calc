# module for all banner

from pyfiglet import Figlet
import colorama
colorama.init()

def main_banner():
    fontsbanner = Figlet(font='big')
    textbanner = (fontsbanner.renderText("Geometry Calc"))
    print(colorama.Fore.LIGHTGREEN_EX, textbanner)   # set textbanner color to light green
    print(colorama.Fore.RESET)  #for reset color to default
    maintext = """
                    [Version : 1.0.0]

            Geometry calculator for calculate 2D plane
                and 3D solid geometry shapes.

                    "Developer : Bangrez"

            ========================================
                          Main Menu
            ========================================
        

            1. Plane Geometry
            2. Solid Geometry
            3. About Geometry Calc

            99. Exit
        """
    print(maintext)

def PlaneGeo_banner():
    fontsbanner = Figlet(font='slant')
    textbanner = (fontsbanner.renderText("Plane Geometry"))
    print(colorama.Fore.LIGHTCYAN_EX, textbanner)   # set textbanner color to light green
    print(colorama.Fore.RESET)  #for reset color to default
    planeGeo_text = """
                    [Version : 1.0.0]

            Geometry calculator for calculate 2D plane
                and 3D solid geometry shapes.

                    "Developer : Bangrez"

            ========================================
                     Plane Geometry Menu
            ========================================
        

            1. Square
            2. Rectangle
            3. Triangle

            99. Go back to the previous menu
                """
    print(planeGeo_text)

def SolidGeo_banner():
    fontsbanner = Figlet(font='slant')
    textbanner = (fontsbanner.renderText("Solid Geometry"))
    print(colorama.Fore.LIGHTYELLOW_EX, textbanner)   # set textbanner color to light green
    print(colorama.Fore.RESET)  #for reset color to default
    solidGeo_text = """
                    [Version : 1.0.0]

            Geometry calculator for calculate 2D plane
                and 3D solid geometry shapes.

                    "Developer : Bangrez"

            ========================================
                     Solid Geometry Menu
            ========================================
        

            1. Cube
            2. Rectangular Prism
            3. Sphere

            99. Go back to the previous menu
                    """
    print(solidGeo_text)

""" Plane Geometry banners 
        |
        V
"""

def triangle_banner():
    fontsbanner = Figlet(font='slant')
    textbanner = (fontsbanner.renderText("Triangle"))
    print(colorama.Fore.LIGHTMAGENTA_EX, textbanner)   # set textbanner color
    print(colorama.Fore.RESET)  #for reset color to default
    list_menu = """
                        Calculate Triangle
            
            1. Triangle area
            2. Triangle perimeter
            3. Pythagorean theorem

            99. Go back to the previous menu
    """
    print(list_menu)

def pythagorean_banner():
    fontsbanner = Figlet(font='slant')
    textbanner = (fontsbanner.renderText("Triangle"))
    print(colorama.Fore.LIGHTMAGENTA_EX, textbanner)   # set textbanner color
    print(colorama.Fore.RESET)  #for reset color to default
    list_menu = """
                        Calculate Pythagorean
            
            1. Find side a
            2. Find side b
            3. Find side hypotenuse (c)

            99. Go back to the previous menu
    """
    print(list_menu)

def square_banner():
    fontsbanner = Figlet(font='slant')
    textbanner = (fontsbanner.renderText("Square"))
    print(colorama.Fore.LIGHTMAGENTA_EX, textbanner)   # set textbanner color
    print(colorama.Fore.RESET)  #for reset color to default

def rectangle_banner():
    fontsbanner = Figlet(font='slant')
    textbanner = (fontsbanner.renderText("Rectangle"))
    print(colorama.Fore.LIGHTMAGENTA_EX, textbanner)   # set textbanner color
    print(colorama.Fore.RESET)  #for reset color to default

""" Solid Geometry banners 
        |
        V
"""

def cube_banner():
    fontsbanner = Figlet(font='slant')
    textbanner = (fontsbanner.renderText("Cube"))
    print(colorama.Fore.LIGHTMAGENTA_EX, textbanner)   # set textbanner color
    print(colorama.Fore.RESET)  #for reset color to default

def rectangularprism_banner():
    fontsbanner = Figlet(font='slant')
    textbanner = (fontsbanner.renderText("Rectangular Prism"))
    print(colorama.Fore.LIGHTMAGENTA_EX, textbanner)   # set textbanner color
    print(colorama.Fore.RESET)  #for reset color to default

def sphere_banner():
    fontsbanner = Figlet(font='slant')
    textbanner = (fontsbanner.renderText("Sphere"))
    print(colorama.Fore.LIGHTMAGENTA_EX, textbanner)   # set textbanner color
    print(colorama.Fore.RESET)  #for reset color to default