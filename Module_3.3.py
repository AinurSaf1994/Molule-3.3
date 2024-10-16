def print_params(a = 1, b = 'строка', c = True):
    print(a, b, c)
#1
print_params(1, 10)
print_params()
print_params(b = 25) #работает
print_params(c = [1,2,3]) #работает

#2
values_list = [1, None, 'Nik']
values_dict = {'a': 1, 'b': None, 'c': 'Cool'}
print_params(*values_list)
print_params(**values_dict)

#3
values_list_2 = [54.32, 'Строка']
print_params(*values_list_2, 42)
print(print_params(*values_list_2), 42)

