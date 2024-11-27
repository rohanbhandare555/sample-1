def calculate_average():
    print("Enter 5 numbers to calculate their average:")
    numbers = []

    # Collect 5 numbers from the user
    for i in range(1, 6):
        while True:
            try:
                number = float(input(f"Enter number {i}: "))
                numbers.append(number)
                break
            except ValueError:
                print("Invalid input. Please enter a numerical value.")

    # Calculate the average
    total = sum(numbers)
    average = total / len(numbers)

    # Display the result
    print("\nNumbers entered:", numbers)
    print(f"The average of the 5 numbers is: {average:.2f}")


# Run the application
if __name__ == "__main__":
    calculate_average()
