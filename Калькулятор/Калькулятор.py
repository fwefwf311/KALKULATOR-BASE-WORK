#ЭТО V1 МОГУТ БЫТЬ  ОШИБКИ
print('Простой Калькулятор')
#ПРОСТОЙ ПРИМЕР КАЛЬКУЛЯТОРА ОТ НАЧИНАЮЩЕГО
l1 = float(input('Введите первое число: '))
operator = input('Введите операцыю: ')
l2 = float(input('Введите второе число: '))
if operator == '+':
    result = l1 + l2
elif operator ==  '-':
    result = l1 - l2
elif operator == '*':
    result = l1 * l2
elif operator ==  '/':
    result = l1 / l2
if l2 == 0:
    print('Ошибка!!! Деление на Ноль')
else: 
 print("Результат: ", result)