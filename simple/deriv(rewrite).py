def derivative(variable, power, coefficient):
    derived = str(int(power) * int(coefficient)) + (str(variable + "^") + str(int(power) - 1))

    if derived == '0x^-1':
        return '0'
    else:
        return derived


def splitter(equation):
    new_list = equation.split('+')
    answer = []

    for i in range(0, len(new_list)):

        for j in range(0, len(new_list[i])):
            if new_list[i][j].isalpha():
                variable = new_list[i][j]
            elif new_list[i][j] == '^':
                power = new_list[i][j + 1::]
            elif new_list[i][j].isdigit():
                if new_list[i][j - 1] != '^':
                    coefficient = new_list[i][j]
            try:
                answer.append(derivative(variable, power, coefficient))
                variable, power, coefficient, = '', '', ''

            except:
                pass

    return '+'.join(answer)


print(splitter(input("Enter a function to derive : ")))
