"""
Є список з набором елементів (рандомних), при запуску коду користовучу доступний вибір:

1. Вивести елементи на екран (звичайний юзер)

2. Редагувaти список, як адмін (тут потрібно ввести логін + пароль)

Якщо вхід адміністратора виконано - адміністратор може використовувати ВСІ методи, які є у списках. Як і в попередньому
завданні- кожна дія передбачає запитів типів елементів, перевірку чи такий елемент вже є в списку та відповідно- повідомлення,
чи потрібно додати ще?

Також при видаленні- спочатку необхідно виконати перевірку- чи такий елемент присутній? У випадку з методом sort()- ми
маємо враховувати, що список може містити різні типи елементів, відповідно- для сортування ми забираємо зі списку
стрічки, сортуємо цифри і після цього додаємо назад стрічки.

Кожен крок, кожна окрема дія знаходиться в окремому циклі while True + кожен такий крок має власне інформаційне меню,
в якому передбачено перезапуск або ж повернення з даного циклу на крок назад.
"""
lst = [5, 3, 1, 2, 4, 'q', 'w', 'e', 'r', 't', 'y']
print(lst)
login, password = input('Щоб редагувати список, введіть логін та пароль: ').split()
if login == 'python' and password == 'developer':
    print('Вхід виконано успішно ')
    while True:
        option = input('Оберіть варіант взаємодії(append, insert, remove, index, sort) або якщо бажаєте завершити програму(exit): ')
        option == 'append' or 'insert' or 'remove' or 'index' or 'sort'
        if option == 'append':
            while True:
                type = input('Виберіть тип(int, str) або назад(back): ')
                if type == 'int':
                    element = int(input('Введіть елемент: '))
                    if element in lst:
                        print('Такий елемент вже існує, чи бажаєте додати ще один?')
                        answer = input()
                        if answer == 'yes':
                             element1 = int(input('Введіть ще раз елемент: '))
                             lst.append(element1)
                             print(lst)
                        else:
                             lst.append(element)
                             print(lst)
                elif type == 'str':
                    element = input('Введіть елемент: ')
                    if element in lst:
                        print('Такий елемент вже існує, чи бажаєте додати ще один?')
                        answer = input()
                        if answer == 'yes':
                            element1 = input('Введіть ще раз елемент: ')
                            lst.append(element1)
                            print(lst)
                    else:
                        lst.append(element)
                        print(lst)
                else:
                    break

        elif option == 'insert':
            while True:
                type = input('Виберіть тип(int, str) або назад(back): ')
                if type == 'int':
                    element = int(input('Введіть елемент: '))
                    if element in lst:
                        print('Такий елемент вже існує, чи бажаєте додати ще один?')
                        answer = input()
                        if answer == 'yes':
                            element1 = int(input('Введіть ще раз елемент: '))
                            index = int(input('Введіть індекс: '))
                            lst.insert(index, element1)
                            print(lst)
                    else:
                        index = int(input('Введіть індекс: '))
                        lst.insert(index, element)
                        print(lst)
                elif type == 'str':
                    element = input('Введіть елемент: ')
                    if element in lst:
                        print('Такий елемент вже існує, чи бажаєте додати ще один?')
                        answer = input()
                        if answer == 'yes':
                            element1 = input('Введіть ще раз елемент: ')
                            index = int(input('Введіть індекс: '))
                            lst.insert(index, element1)
                            print(lst)
                    else:
                        index = int(input('Введіть індекс: '))
                        lst.insert(index, element)
                        print(lst)
                else:
                    break

        elif option == 'remove':
            while True:
                type = input('Виберіть тип(int, str) або назад(back): ')
                if type == 'int':
                    element = int(input('Введіть елемент, який хочете видалити: '))
                    if element not in lst:
                        print('Такого елемента немає')
                    lst.remove(element)
                    print(lst)

                elif type == 'str':
                    element = input('Введіть елемент, який хочете видалити: ')
                    if element not in lst:
                        print('Такого елемента немає')
                    lst.remove(element)
                    print(lst)
                else:
                     break

        elif option == 'index':
            while True:
                type = input('Виберіть тип(int, str) або назад(back): ')
                if type == 'int':
                    element = int(input('Введіть елемент: '))
                    print(lst.index(element))
                elif type == 'str':
                    element = input('Введіть елемент: ')
                    print(lst.index(element))
                else:
                    break

        elif option == 'sort':
            lst_int = [i for i in lst if type(i) == int]
            lst_str = [i for i in lst if type(i) == str]
            lst_int.sort()
            lst_str.sort()
            print(lst_int + lst_str)

        else:
            break
else:
    print('Неправильно введено логін або пароль, спробуйте ще раз ')
