# zip(*iterables) joins two iterables by their indexes

usernames = ['TheFakeAsian', 'Pointic', 'aj', 'YESSIE_', 'Arg0']
passwords = ['i<3val', 'myrealpassword', 'ih8baolong', 'monkeyassmuncher', 'theeast322']

users = dict(zip(usernames, passwords))

for key, value in users.items():
    print(f'{key} : {value}')

alphabet = 'abcdefghijklmnopqrstuvwxyz'
backwards = 'zyxwvutsrqponmlkjihgfedcba'

print()

letters = list(zip(alphabet, backwards))
for i in letters:
    print(i[0]+':'+i[1], end=', ')
