
'''n = int(input("Введите количество слов: "))
words = []
for i in range(n):
    words.append(str(input()))
print(" ".join(words))

'''Модифицируйте предыдущую программу так, чтобы число вводимых слов не было задано,
а программа работала до того момента, как пользователь введет слово «stop».'''


words = []
# программа останавливается при вводе слова "stop"
while (new_word := str(input())) != "stop":
    words.append(new_word)

print(" ".join(words))'''


'''import random
error_count=0
coun=0
while error_count<3:
    a=random.randint(0;100)
    b=random.randint(0;100)
    if int(input(f"{a}+{b}="))
==a+b:
        count+=1
        print('Правильно')
    else:
        error_count+=1
        print('Неправильно'))
print(f"Игра окончена. Правильных ответов {count}")'''
