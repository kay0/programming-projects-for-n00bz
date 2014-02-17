#!/usr/bin/env python3

import math


def triangle(base, height):
    area = .5 * base * height
    return area


def circle(radius):
    area = math.pi * math.pow(radius, 2)
    return area


def ellipse(x, y):
    area = math.pi * x * y
    return area


def rectangle(width, height):
    area = width * height
    return area


def main():
    print("triangle(10, 5) =", triangle(10, 5))
    print("circle(5) =", circle(5))
    print("ellipse(3, 5) =", ellipse(3, 5))
    print("rectangle(5, 6) =", rectangle(5, 6))

if __name__ == "__main__":
    main()
