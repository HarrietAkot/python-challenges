
# QN4
# Write a program that computes the net amount of a bank account based a transaction log from console input.
#  The transaction log format is shown as following:

bal = 1000
s = input('enter option')
    x = s.split(' ')
    first = (x[0])
    second = int(x[1])
    if first == 'D':
        bal+=second
        print(bal)
    elif first == 'W':
        bal-=second
        print(bal)
    else:
        print('Invalid input')


