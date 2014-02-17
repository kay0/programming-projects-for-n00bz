#!/usr/bin/env python3


def ask():
    print("How old are you?")
    age = input("> ")
    return age


def calculate(age):
    seconds = int(age) * 365 * 24 * 60 * 60
    print("You are " + str(seconds) + " seconds old.")


def main():
    age = ask()
    calculate(age)

if __name__ == "__main__":
    main()
