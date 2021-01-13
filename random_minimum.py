#!/usr/bin/env python3

# Created by Ryan Nguyen
# Created on Decemebr 2020
# This program generates 10 random numbers and determines the lowest

import random


def find_lowest(list_of_randoms):
    # this function determines the lowest number out of an array
    lowest = list_of_randoms[0]

    for random_number in list_of_randoms:
        if lowest > random_number:
            lowest = random_number

    return lowest


def main():
    # this function generates 10 random numbers and outputs the lowest one

    list_of_randoms = []

    # generates numbers, puts them in list
    for loop_counter in range(0, 10):
        random_number = random.randint(1, 100)
        list_of_randoms.append(random_number)
        print("Random number {0}: {1}".format(loop_counter + 1, random_number))

    print(" ")

    # calls find_lowest function
    final = find_lowest(list_of_randoms)

    # final output
    print("Lowest: {0}".format(final))


if __name__ == "__main__":
    main()
