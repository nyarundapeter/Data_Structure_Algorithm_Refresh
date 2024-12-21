"""
Create the expense array to hold the values as outlined in the array_exercise.md file.
"""

expense = [2200, 2350, 2600, 2130, 2190]

"""
Q1: In Feb, how many dollars you spent extra compare to January
"""
print(f"extra spent in Feb compared to Jan: {expense[1] - expense[0]}")

"""
Q2: Find out your total expense for the first quarter
"""
print(f"total expense for first quarter: {sum(expense[:3])}")

"""
Q3: Find out if you spent exactly 2000 dollars in any month
"""
print(f"spent exactly 2000 dollars in any month: {2000 in expense}")

"""
Q4: June month just finished and your expense is 1980 dollar. Add this item to our monthly expense list
"""
expense.append(1980)
print(f"expense after adding June: {expense}")

"""
Q5: You returned an item that you bought in a month of April and
    got a refund of 200$. Make a correction to your monthly expense list
    based on this
"""
expense[3] -= 200
print(f"expense after refund: {expense}")