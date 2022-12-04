# lambda function -- parameters :(return) expression
area = lambda length, width: f'Area : {length * width} m^2'
volume = lambda length, width, height: f'Volume : {length * width * height} m^3'
age_check = lambda age: 'You\'re of age!' if age >= 18 else 'You\'re too young!'
be_quiet = lambda name: name.lower()[:-1] + '...'

print(area(20, 15))
print(volume(10, 20, 30))
print(age_check(7))
print()
print(be_quiet('THIS IS SO COOL!'))
