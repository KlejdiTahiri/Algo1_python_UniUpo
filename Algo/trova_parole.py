"""word_list = ["ciao", "ciao", "mimmo"]
my_dic = {}

for i in word_list:
    my_dic[i] = 1 + my_dic.get(i, 0)

max_value = max(my_dic.values())
max_items = [(key, value) for key, value in my_dic.items() if value == max_value]

print(max_items)"""

def serie_armonica():
    n = 1
    while True:
        yield 1/n
        n += 1



sum = serie_armonica()

for i in range(10):
    print(next(sum))

def lista_rimuovi(lista, x, index=0):
    if index == len(lista):
        return

    if lista[index] % x != 0:
        lista.pop(index)
        lista_rimuovi(lista, x, index)
    else:
        lista_rimuovi(lista, x, index + 1)

lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
lista_rimuovi(lista, 2)
print(lista)
