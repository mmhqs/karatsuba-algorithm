# Multiply two integers using traditional multiplication
def traditional_multiplication(number1, number2):
    return number1 * number2


# Multiply two integers using the Karatsuba algorithm
def karatsuba_multiplication(number1, number2):

    # Base case of recursion if numbers have only one digit, we use traditional multiplication
    if number1 < 10 or number2 < 10:
        return traditional_multiplication(number1, number2)

    # Convert integers to string so we can calculate the number of digits
    number1_string = str(number1)
    number2_string = str(number2)

    # Maximum length
    max_digits = max(len(number1_string), len(number2_string))

    # Round ‘n’ to the nearest even number to ensure that the division is exact
    if max_digits % 2 != 0:
        max_digits += 1

    # Add padding to the left to until max digits
    number1_string = number1_string.zfill(max_digits)
    number2_string = number2_string.zfill(max_digits)

    # Find the middle point
    middle_point = max_digits // 2

    # Divide each number into two halves a, b, c, d.
    a = int(number1_string[:middle_point])
    b = int(number1_string[middle_point:])
    c = int(number2_string[:middle_point])
    d = int(number2_string[middle_point:])

    # Recursive products
    # z2 = a * c
    z2 = karatsuba_multiplication(a, c)

    # z0 = b * d
    z0 = karatsuba_multiplication(b, d)

    # z1 = (a + b) * (c + d)
    z1 = karatsuba_multiplication(a + b, c + d)

    # Calculate the middle term
    middle_term = z1 - z2 - z0

    # Result = (z2 * 10^n) + (middle_term * 10^(n^2)) + z0
    result = (z2 * 10**max_digits) + (middle_term * 10**middle_point) + z0

    return result


def main():
    print("----- Karatsuba calculator -----\n")
    try:
        number1_string = input("Enter the first number: ")
        number1 = int(number1_string)

        number2_string = input("Enter the second number: ")
        number2 = int(number2_string)

        karatsuba_result = karatsuba_multiplication(number1, number2)
        traditional_result = number1 * number2

        print(
            f"\nMultiplying {number1} x {number2}...\n")
        print(
            f"\nResult (Karatsuba) = {karatsuba_result}")

        print(
            f"Result (Traditional method) = {traditional_result}\n")

        if (karatsuba_result == traditional_result):
            print("Your implementation is correct! ✅\n")
        else:
            print("Your implementation is incorrect! ❌\n")

    except ValueError:
        print("\nError: Please enter only valid numbers.")


if __name__ == "__main__":
    main()
