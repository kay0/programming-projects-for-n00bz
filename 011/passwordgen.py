import string
import random


def generate(length):
    characterPool = string.ascii_letters + string.digits + '!@#$%^&*()-_=+'
    for _ in range(0, length):
        print(random.choice(characterPool), end="")

    print()


def main():
    generate(20)

if __name__ == "__main__":
    main()
