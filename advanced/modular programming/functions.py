def hello():
    print('Hello from your file neighbour!')


def goodbye():
    print('I have to go, goodbye!')


if __name__ == '__main__':  # when functions.py is imported into other programs,
    print('This is the attached program')  # __name__ == 'functions' as opposed to '__main__' (default)
