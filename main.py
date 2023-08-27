my_name = input('Enter your name:' )
my_age = input('Enter your age:' )
print(f'My name is {my_name} and I am {my_age} years old')

first_number = int (input('enter the first number:'))
second_number = int (input('your second number:'))
Operation = input('enter your wanted opertion:')


if Operation==('+'):
    print(first_number+second_number)
elif Operation==('-'):
    print(first_number-second_number)
elif Operation==('*'):
    print(first_number*second_number)
elif Operation==('/'):
    print(first_number/second_number)
else:
    print('the operation is not valid')


bus_capacity = 200
people_inbus = int(input('enter available seats:'))
people_gettingin = int(input('enter the amount of people that want to get into the bus:'))

empty_seats = bus_capacity - people_inbus

if people_inbus > people_gettingin :
   print("There is available seats")
elif people_inbus <= people_gettingin :
   print("There is no available seats")