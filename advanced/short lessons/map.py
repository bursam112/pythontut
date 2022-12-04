# map() =   applies a function to each item in an iterable
# map(function, iterable)

# Changeable data values
international_items = [('100% Cotton Designer shirt', 79.99, 'CAD'),
                       ('Levi\'s pants', 39.99, 'USD'),
                       ('Sleeveless Puffer jacket', 69.99, 'EUR'),
                       ('Christmas socks', 15.99, 'CAD')]


def to_eur(data):
    if data[2] == 'EUR':
        return data[0], data[1], 'EUR'
    elif data[2] == 'CAD':
        return data[0], data[1] * 0.72, 'EUR'  # if error, specify tuple
    else:
        return data[0], data[1] * 0.96, 'EUR'  # from usd to euros


def to_usd(data):
    if data[2] == 'USD':
        return data[0], data[1], 'USD'
    elif data[2] == 'CAD':
        return data[0], data[1] * 0.75, 'USD'  # if error, specify tuple
    else:
        return data[0], data[1] * 1.04, 'USD'  # from euros to usd


def to_cad(data):
    if data[2] == 'EUR':
        return data[0], data[1] * 1.39, 'CAD'  # if error, specify tuple
    elif data[2] == 'USD':
        return data[0], data[1] * 1.33, 'CAD'
    else:
        return data[0], data[1], 'CAD'  # from euros to usd


# MAPPING SO USEFUL
store_eur = list(map(to_eur, international_items))
store_cad = list(map(to_cad, international_items))
store_usd = list(map(to_usd, international_items))

choice = input('How will you be shopping today? (CAD, USD, EUR) : ')
print('\nSelection:')

if choice == 'CAD':
    for i in store_cad:
        print(f'    {i[0]}, {round(i[1], 2)} {i[2]}')

elif choice == 'USD':
    for i in store_usd:
        print(f'    {i[0]}, {round(i[1], 2)} {i[2]}')

elif choice == 'EUR':
    for i in store_eur:
        print(f'    {i[0]}, {round(i[1], 2)} {i[2]}')
