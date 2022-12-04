# := is two in one : assigning a variable and using it
# specifying what to assign to your variable is very important (with parentheses!)


while (name := input('What\'s your name? ').upper()) != 'SAM':
    print("This isn't your computer! Try again.")

print(f"Welcome back, {name}!\n")

# Two programs in one!
new_list = []
while (food := input('Add an item to your grocery list: ')) != 'quit':
    new_list.append(food)
    print(f'\n{new_list}\n')

print(f'\n{new_list}, Total: {len(new_list)} item(s).')
