# filter(function, iterable)
# if the function applied to the iterable's data returns True, it is made into a new list separated from the rest.

friends = [('Ethan', 18),
           ('Sam', 18),
           ('Ayla', 19),
           ('Cami', 19),
           ('Braydon', 17),
           ('Will', 18)]

# drinking_buddies = list(filter(lambda data: data[1] >= 18, friends))

# drinking_buddies = [i if i[1] >= 18 else tuple((f'{i[0]} is too young', i[1])) for i in friends]

drinking_buddies = [i                                           # expression (return)
                    if i[1] >= 18                               # condition
                    else tuple((f'{i[0]} is too young', i[1]))  # if condition isn't met
                    for i in friends]                           # amount of iterations

list_sorted = sorted(drinking_buddies, key=lambda func: func[1])

for i in list_sorted:
    print(i)
