def calculate_factorial(num):
    """
    Calculate the factorial of a given number.

    Args:
        num (int): The number to calculate the factorial for.

    Returns:
        int: The factorial of the given number.
    """
    if num < 0:
        return "Factorial is not defined for negative numbers."
    elif num == 0 or num == 1:
        return 1
    else:
        factorial = 1
        for i in range(2, num + 1):
            factorial *= i
        return factorial

# Main function to run the program
if __name__ == "__main__":
    try:
        number = int(input("Enter a number to find its factorial: "))
        result = calculate_factorial(number)
        print(f"The factorial of {number} is {result}.")
    except ValueError:
        print("Please enter a valid integer.")
