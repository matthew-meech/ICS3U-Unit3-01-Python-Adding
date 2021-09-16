#!/usr/bin/env python3

# Created by: Matthew Meech
# Created on: Sep 2021
# This program Calculates 2 numbers being added


def main():

    # input
    number1 = int(input("Enter the frist number you would like to add : "))
    number2 = int(input("Enter the second number you would like to add : "))

    # process
    answer = number1 + number2

    # output
    print("")
    print("Answer is {0}.".format(answer))


if __name__ == "__main__":
    main()
