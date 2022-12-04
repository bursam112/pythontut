sentence = input("Enter a sentence to dashify : ")
new_list = [*sentence]
while ' ' in new_list:
    new_list.remove(' ')
print('-'.join(new_list))
