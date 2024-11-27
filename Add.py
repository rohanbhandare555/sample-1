def add_ten_numbers():
    print("Enter 10 numbers to calculate their sum:")
    total = 0
    for i in range(1, 11):  # Loop from 1 to 10
        while True:
            try:
                number = float(input(f"Enter number {i}: "))
                break
            except ValueError:
                print("Invalid input. Please enter a valid number.")
        total += number
    print(f"\nThe sum of the 10 numbers is: {total}")

# Run the application
if __name__ == "__main__":
    add_ten_numbers()
