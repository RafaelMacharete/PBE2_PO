# Exercise 1:
number1 = int(input('Type a number: '))

if number1 < 0:
    number1 *= -1

print(number1)

while number1:
    number1 -= 1
    print(number1)

# Exercise 2:
number2 = int(input('Type a number: '))

number_list = []
while number2 >= 0:
    number_list.append(number2)
    number2 = int(input('Type a number: '))

biggest_number = 0
for idx in number_list:
    if biggest_number < idx:
        biggest_number = idx

print(biggest_number)