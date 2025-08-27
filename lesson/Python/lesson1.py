'''
18.08.2025 кол-во часов занятия:
'''


first_str = 'abcdefg'
print(first_str[0], first_str[::-1], first_str[::2])
str_a = 'a'
print(str_a*3, first_str+str_a)


x = set('123asdzxcasd')
y = set('1234asdfqwr')

x.isdisjoint(y)


# num = 10
# if num > 5:
#     raise Exception(f'Число не должно быть больше 5. {num = }')
# print(num)

num = 10
assert num < 5, 'Число не должно превышать 5'

print(num)






