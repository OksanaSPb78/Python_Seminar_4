# Задача №25. Решение в группах
# Напишите программу, которая принимает на вход строку, и отслеживает, сколько раз 
# каждый символ уже встречался. Количество повторов добавляется к символам с помощью 
# постфикса формата _n.
# Input: a a a b c a a d c d d
# Output: a a_1 a_2 b c a_3 a_4 d c_1 d_1 d_2
# Для решения данной задачи используйте функцию.split()

my_string='a a a b c a a d c d d'
print(my_string)
my_string=list(my_string.split())
print(my_string)
temp=[]
for i in my_string:
    if i in temp:
        print(f'{i}_{temp.count(i)}', end=' ')
        temp.append(i)
    else:
        print(i, end=' ')
        temp.append(i)


# Задача №27. Решение в группах
# Пользователь вводит текст(строка). Словом считается последовательность непробельных 
# символов идущих подряд, слова разделены одним или большим числом пробелов. Определите, 
# сколько различных слов содержится в этом тексте.
# Input:
# She sells sea shells on the sea shore The shells that she sells are sea shells I'm sure.So 
# if she sells sea shells on the sea shore I'm sure that the shells are sea shore shells
# Output: 13

# my_text= "She sells sea shells on the sea shore The shells that she sells are sea shells I'm sure. So if she sells sea shells on the sea shore I'm sure that the shells are sea shore shells"


# print(len(set(my_text.split())))


# Задача №29. Решение в группах
# Ваня и Петя поспорили, кто быстрее решит следующую задачу: “Задана последовательность
# неотрицательных целых чисел. Требуется определить значение наибольшего элемента
# последовательности, которая завершается первым встретившимся нулем (число 0 не входит в
# последовательность)”. Однако 2 друга оказались не такими смышлеными. Никто из ребят 
# не смог до конца сделать это задание. Они решили так: у кого будет меньше ошибок в коде,
# тот и выиграл спор. За помощью товарищи обратились к Вам, студентам.
# Примечание: Программные коды на следующих
# слайдах
# Ваня:
# n = int(input())
# max_number = 1000
# while n != 0:
#  n = int(input())
#  if max_number > n:
#  max_number = n
# print(max_number)

# Петя:
# n = int(input())
# max_number = -1
# while n < 0:
#  n = int(input())
#  if max_number < n:
#  n = max_number
# print(n) 