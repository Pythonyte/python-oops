person = {
    'name':'ono',
    'age': 21,
}

# way 1
print('my name is ' + person['name'] + '. I am ' + str(person['age']) + ' yrs old')

# way 2
print('my name is {}. I am {} yrs old'.format(person['name'], str(person['age'])))

# way 3
print('my name is {0}. I am {1} yrs old'.format(person['name'], str(person['age'])))

# way 4
print('my name is {0[name]}. I am {1[age]} yrs old'.format(person, person))

# way 5
print('my name is {0[name]}. I am {0[age]} yrs old'.format(person))



##### If person is a list
person = ['ono', 21]

# way 6
print('my name is {0[0]}. I am {0[1]} yrs old'.format(person))




##### If person is a class
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

person = Person(name='ono', age=21)

# way 7
print('my name is {0.name}. I am {0.age} yrs old'.format(person))



## Some more templates

# way 8
# create an html tag
html = {
    'tag':'p',
    'text': 'goal',
}

print('<{0[tag]}> {0[text]} </{0[tag]}>'.format(html))