def main():
    print("Welcome to the Python Number Application!")
    print("You can enter up to 10 numbers.")
    
    numbers = []  # List to store the numbers
    max_count = 10  # Maximum numbers allowed

    for i in range(max_count):
        try:
            num = float(input(f"Enter number {i+1} (or press Enter to finish): "))
            numbers.append(num)
        except ValueError:
            print("Input is not a valid number. Try again or press Enter to finish.")
            break
    
    if not numbers:
        print("No numbers entered. Exiting...")
        return

    # Perform calculations
    total = sum(numbers)
    average = total / len(numbers)
    max_num = max(numbers)
    min_num = min(numbers)

    # Display results
    print("\nResults:")
    print(f"Numbers entered: {numbers}")
    print(f"Total: {total}")
    print(f"Average: {average}")
    print(f"Maximum: {max_num}")
    print(f"Minimum: {min_num}")

if __name__ == "__main__":
    main()
