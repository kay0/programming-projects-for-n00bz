#!/usr/bin/env python3


def fib(n):
    first = 0
    second = 1
    total = 0

    print(first)
    print(second)

    for _ in range(0, n):
        total = first + second
        print(total)
        first = second
        second = total


def main():
    fib(15)

if __name__ == "__main__":
    main()
