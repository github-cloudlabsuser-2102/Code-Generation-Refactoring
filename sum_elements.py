#A poorly written example of a program in Python. It prompts the user for the number of elements to sum, takes those integers as input, and handles some basic error cases

MAX = 100

def sum_elements(arr):
    return sum(arr)

def main():
    try:
        n = int(input("Enter the number of elements (1-100): "))
        if not 1 <= n <= MAX:
            print("Invalid input. Please provide a digit ranging from 1 to 100.")
            return

        arr = []
        print(f"Enter {n} integers:")
        for _ in range(n):
            while True:
                try:
                    arr.append(int(input()))
                    break
                except ValueError:
                    print("Invalid input. Please enter valid integers.")

        result = sum_elements(arr)
        print(f"The sum of the elements is: {result}")

    except ValueError:
        print("Invalid input. Please enter a valid number.")

if __name__ == "__main__":
    main()