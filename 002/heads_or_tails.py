#!/usr/bin/env python3

import random


def flip():
    result = random.choice(["heads", "tails"])
    print(result)


def main():
    flip()

if __name__ == "__main__":
    main()
