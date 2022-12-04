# .sort() used for lists ONLY
# sorted(iterable) used for all iterables

# data
students = [("Squidward", "F", 60),
            ("Sandy", "A", 33),
            ("Patrick", "D", 36),
            ("Spongebob", "B", 20),
            ("Mr.Krabs", "C", 78)]

decision = ''  # can't walrus a while loop that expects nested change, will just reassign variable.
while decision != 'n':
    data_type = int(input('Sort by:\n    1: Names, 2: Grades, 3: Ages\n')) - 1
    data_func = lambda iterable: iterable[data_type]
    sorted_students = sorted(students, key=data_func)

    data_print = lambda find: f'{i[0]}, {i[data_type]}' if find != 0 else f'{i[0]}'

    for i in sorted_students:
        print(data_print(data_type))
    print()

    decision = input('Would you like to continue? (y/n) : ')
    print('Goodbye!') if decision == 'n' else print('Continuing...\n')
