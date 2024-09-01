class FizzBuzz:
    def convert(self, number: int) -> str:
        result = ""

        if '3' in str(number) and '5' in str(number):
            result += "FizzBuzz"
        elif '3' in str(number):
            result += "Fizz"
        elif '5' in str(number):
            result += "Buzz"

        if number % 15 == 0:
            result += "FizzBuzz"
        if number % 3 == 0:
            result += "Fizz"
        if number % 5 == 0:
            result += "Buzz"
        else:
            result += str(number)

        return result
