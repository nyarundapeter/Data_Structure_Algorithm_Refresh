"""
Create a list of all odd numbers between 1 and a max number.
Max number is something you need to take from a user using input() function
"""

def get_max_number():
    while True:
        try:
            max_number = int(input("Enter a max number: "))
            break
        except ValueError:
            print("Invalid input. Please enter a number.")
    return max_number

def get_odd_numbers(max_number):
    odd_numbers = []
    for i in range(1, max_number+1):
        if i % 2 != 0:
            odd_numbers.append(i)
    return odd_numbers

if __name__ == '__main__':
    max_number = get_max_number()
    odd_numbers = get_odd_numbers(max_number)
    print(f"Odd numbers between 1 and {max_number}: {odd_numbers}")