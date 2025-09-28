#!/usr/bin/env python3
# Created By: Yoma Ozoh
# Date: September 28, 2025
# This program calculates circumference using user input

import constants


def main():
    # get radius from the user
    radius = float(input("Enter the radius of the circle (mm): "))

    # calculate circumference
    circumference = constants.TAU * radius

    # display the circumference
    print("")
    print("The circumference of the circle is: {} mm".format(circumference))


if __name__ == "__main__":
    main()
