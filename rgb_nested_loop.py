#!/usr/bin/env python3

# Created by: Sarah
# Created on: May, 1st, 2022
# This program displays different RGB colour codes up to 50 using a nested for
# loop.


def main():
    # initialize counters
    counter1 = 0
    counter2 = 0
    counter3 = 0

    # display opening message
    print("These are RGB colour combinations up to 50:")
    print("")

    # determines the different colour codes
    # displays results to the console
    for counter1 in range(51):
        for counter2 in range(51):
            for counter3 in range(51):
                print("RGB: {}, {}, {}". format(counter1, counter2, counter3))


if __name__ == "__main__":
    main()
