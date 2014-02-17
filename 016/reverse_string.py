#!/usr/bin/env python3


def reverse():
    print("Insert a string of characters:")
    userString = input("> ")
    for i in range(len(userString) - 1, -1, -1):
        print(userString[i], end="")


def main():
    reverse()


if __name__ == "__main__":
    main()
