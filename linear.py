def linear_search(roll_numbers, target):
    for i in range(len(roll_numbers)):
        if roll_numbers[i] == target:
            return True
    return False

def sentinel_search(roll_numbers, target):
    # Append the target at the end of the array and set it as a sentinel
    roll_numbers.append(target)
    i = 0
    while roll_numbers[i] != target:
        i += 1
    roll_numbers.pop()  # Remove the sentinel
    return i < len(roll_numbers)

def main():
    # Example: Storing roll numbers in an array
    roll_numbers = [101, 105, 110, 115, 120, 125, 130, 135]

    # Asking user for input
    target_roll_number = int(input("Enter the roll number to search: "))

    # Linear search
    if linear_search(roll_numbers, target_roll_number):
        print(f"{target_roll_number} attended the training program (Linear Search).")
    else:
        print(f"{target_roll_number} did not attend the training program (Linear Search).")

    # Sentinel search
    if sentinel_search(roll_numbers, target_roll_number):
        print(f"{target_roll_number} attended the training program (Sentinel Search).")
    else:
        print(f"{target_roll_number} did not attend the training program (Sentinel Search).")

if __name__ == "__main__":
    main()
