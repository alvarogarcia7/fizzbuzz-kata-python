from fizzbuzz.conversion import FizzBuzz


def main() -> int:
    fizzbuzz = FizzBuzz()
    for i in range(1, 100 + 1):
        print(fizzbuzz.convert(i))
    return 0


if __name__ == '__main__':
    main()
