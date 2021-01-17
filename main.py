# import built-in modules
from math import pi


# function that takes the radius of a circle as an argument and returns the area of said circle
def get_area_of_circle(radius):
    return pi * radius ** 2


# run from the main file
if __name__ == "__main__":
    # get the area of a circle with radius 5
    get_area_of_circle(5)
