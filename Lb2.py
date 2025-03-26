#Функция факториал
#Написать функцию Является ли число простым
#Дается список,вернуть уникальные элементы этого списка (set)
#Группировать список слов по их длине,возвращаем словарь где ключ это длина слова,а значение это список слов этой длинны

from math import factorial

def fact(x):
    if(x == 0):
        return 1
    return factorial(x) 

print(fact(0))

##Написать функцию Является ли число простым

def simple(q):
    if q <= 1:
        return "Составное"
    for i in range(2, q):
        if q % i == 0:
            return "Составное"
    return "Простое"

##Дается список,вернуть уникальные элементы этого списка (set)

print(simple(5))

def elements(input_list):
    return list(set(input_list))

my_list = [1, 2, 2, 3, 4, 4, 5]
unique_list = elements(my_list)
print(unique_list)

##Группировать список слов по их длине,возвращаем словарь где ключ это длина слова,а значение это список слов этой длинны

def group_words(words):
    list = {}
    for word in words:
        length = len(word)
        if length not in list:
            list[length] = []
        list[length].append(word)
    return list

words_list = ["apple", "banana", "pear", "kiwi", "grape", "fig"]
result = group_words(words_list)
print(result)