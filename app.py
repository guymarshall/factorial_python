def calculate_factorial(number: int):
    result: int = 1
    counter: int = 2

    if number > 1:
        while counter <= number:
            result *= counter
            counter += 1

    return result


def approximate_factorial(number):
    number_power = number ** number

    e = 2.7182818
    e_minus_n = e ** (-1 * number)

    root_number = number ** 0.5

    pi = 3.1415926
    root_two_pi = (2 * pi) ** 0.5

    return number_power * e_minus_n * root_number * root_two_pi


def main():
    user_input: int = int(input("Enter an integer: "))
    print(f"{user_input}! = {calculate_factorial(user_input)}")
    # print(f"{user_input}! ~ {approximate_factorial(user_input)}")
    # approximate = approximate_factorial(user_input)
    # print("Approximate result calculated")
    # exact = calculate_factorial(user_input)
    # print("Exact result calculated")
    # print(f"Ratio = {exact / approximate}")


if __name__ == "__main__":
    main()
