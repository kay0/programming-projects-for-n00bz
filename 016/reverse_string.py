#!/usr/bin/env python3


def reverse():
    print("Insert a string of characters:")
    userstring = input("> ")
    for i in range(len(userstring) - 1, -1, -1):
        print(userstring[i], end="")


def main():
    reverse()

if __name__ == "__main__":
    main()
