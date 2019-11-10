#!/usr/bin/env python3

# Created by: Douglass Jeffrey
# Created on: Oct 2019
# This program lists every rgb combination

# This function lists every rgb combination
# Process/ output
def main():
    for red in range(255):
        for green in range(255):
            for blue in range(255):
                print("RGB: " + str(red) + ", " + str(green) + ", " +
                      str(blue))


if __name__ == "__main__":
    main()
