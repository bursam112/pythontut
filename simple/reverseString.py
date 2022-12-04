user_input = input()

# reverse
print(user_input[::-1])

# switch first and last character
print(user_input[-1] + user_input[1:-1] + user_input[0])

# pig latin
print(f"{user_input[1:]}{user_input[0]}ay")


# def lowercase
def lowercase(string):
    result = ""
    for i in range(len(string)):
        if 65 <= ord(string[i]) <= 90:
            result += chr(ord(string[i]) + 32)
        else:
            result += string[i]
    return result


print(lowercase(user_input))
