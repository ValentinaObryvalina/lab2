
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


