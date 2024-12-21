"""
Create an array to hold the marvel superheroes
"""
heroes = ['spider man','thor','hulk','iron man','captain america']

"""
Q1: Length of list
"""
print(f"The Heroes list has",len(heroes),"heroes")

"""
Q2: Add 'black panther' at the end of this list
"""
heroes.append('black panther')
print(f"The Heroes list now is {heroes}")

"""
Q3: You realize that you need to add 'black panther' after 'hulk',
    so remove it from the list first and then add it after 'hulk'
"""
heroes.remove('black panther')
heroes.insert(3,'black panther')
print(f"The Heroes list now is {heroes}")

"""
Q4: Now you don't like thor and hulk because they get angry easily :)
    So you want to remove thor and hulk from list and replace them with doctor strange (because he is cool).
    Do that with one line of code.
"""
heroes[1:3] = ['doctor strange']
print(f"The Heroes list now is {heroes}")

"""
Q5: Sort the heros list in alphabetical order (Hint. Use dir() functions to list down all functions available in list)
"""
heroes.sort()
print(f"The Heroes list now is {heroes}")