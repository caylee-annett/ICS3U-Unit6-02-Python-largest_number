#!/usr/bin/env python3

# Created by: Caylee Annett
# Created on: June 2021
# This program finds the largest number from a list of random numbers

import random


def calculate_number(list_of_numbers):
    # This function finds the largest number

    largest_number = 0

    for loop_counter in range(len(list_of_numbers)):
        if list_of_numbers[loop_counter] >= largest_number:
            largest_number = list_of_numbers[loop_counter]

    return largest_number


def main():
    # This function generates the random numbers

    number_list = []

    # Process
    print("This program prints the largest number from a list.")
    print("")
    for loop_counter in range(0, 10):
        random_number = random.randint(1, 100)
        print("The random number is: {}".format(random_number))
        number_list.append(random_number)

    # Call functions
    number = calculate_number(number_list)

    # Output
    print("")
    print("The largest number is: {}".format(number))
    print("\nDone.")


if __name__ == "__main__":
    main()
