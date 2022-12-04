from time import ctime, time, sleep, localtime, strftime

print(ctime(0))  # beginning of time apparently (epoch)
print(time())  # how many seconds since the beginning of time
print(ctime(time()), '\n')  # current date
sleep(1)

time_object = localtime()
print(time_object)
print(strftime("%B %d, %Y %H:%M:%S", time_object), '\n')
sleep(1)

if (woo := strftime('%A', localtime())) == 'Thursday':
    print(f'I made this code on a {woo}')
