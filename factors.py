# factors.py
# Name: Mutaz Al-shara
# Instructor: Rita M. Ghantous
# Date: April 16, 2025
# Class: Engr_103_401_S2025
# Description: This program asks the user for a positive integer and prints all its positive factors in ascending order.

def main():
    # Ask the user to enter a positive integer
    num = int(input("Please enter a positive integer: "))
    
    # Ensure the input is positive
    if num <= 0:
        print("Please enter a positive integer.")
        return
    
    # Find and print the factors
    print(f"The factors of {num} are:")
    for i in range(1, num + 1):
        if num % i == 0:
            print(i)

if __name__ == "__main__":
    main()