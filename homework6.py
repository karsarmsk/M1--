my_dict = {'Name' : 'Сергей', 'year of birth' : 1963} # Создал словарь
print(my_dict) # вывел словарь на экран
print(my_dict.get('Namf')) # Вывод по несуществующему ключу None
print(my_dict.get('Name')) # Вывод по существующему ключу
my_dict['surname'] = 'Карасев' # добавил пару
my_dict['city'] = 'Москва' # добавил пару
print(my_dict) # вывел словарь на экран
city = my_dict.pop('city') # вынул из словоря пару и записал ее значение в переменную
print(city) # вывод значения
print(my_dict) # вывел словарь на экран
my_set = {1,25,'Сергей', 25  } # создал множество
print(my_set) # вывел множество на экран
print(my_set.add('Карасев')) # добавил элемент в множество
print(my_set.add(1963)) # добавил элемент в множество
print(my_set.remove(1963)) # удалил элемент из множества
print(my_set) # вывел множество на экран