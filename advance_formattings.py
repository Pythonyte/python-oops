# formatting numbers
for i in range(9,11):
    print('Num is {:02}'.format(i))
    print('Num is {:04}'.format(i))

# format decimal precisons
pi = 3.1415667777
print('pi is {:.2f}'.format(pi))


# add commas in large numbers
money_in_bank = 100000000000000
print('Total money: {:,}'.format(money_in_bank))

"""
Num is 09
Num is 0009
Num is 10
Num is 0010
pi is 3.14
Total money: 100,000,000,000,000
"""