#!/usr/bin/env python3

import string
import random


def generate(length):
    character_pool = string.ascii_letters + string.digits + '!@#$%^&*()-_=+'
    for _ in range(0, length):
        print(random.choice(character_pool), end="")

    print()


def main():
    generate(20)

if __name__ == "__main__":
    main()
