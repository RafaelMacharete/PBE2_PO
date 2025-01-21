# Exercise 1:

def is_even_or_odd(number):
    if number % 2 == 0:
        return False
    else:
        return True
    
number = 1

print(is_even_or_odd(number))

# Exercise 2:
grade_student = [10,10,10,5,3]

avarage = sum(grade_student) / len(grade_student)
print(avarage)

if avarage >= 5:
    print('Student: Aprroved')
elif avarage >= 2.5:
    print('Studend: Recovering ')
else:
    print('Student: Failed')
