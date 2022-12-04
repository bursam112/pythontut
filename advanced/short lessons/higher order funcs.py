def backwards(text):
    return text[::-1]


def quiet(text):
    return text.lower() + '...'


def loud(text):
    return text.upper() + '!'


def hello(func):
    text = func('Hello')
    print(text)


hello(backwards)
hello(loud)
hello(quiet)


# ------------------------------------------------------------

# nested functions
def divide(x):
    def divisor(y):
        return x / y

    return divisor


print(divide(15)(5))  # 2 parentheses??
# divides 15 by 5
