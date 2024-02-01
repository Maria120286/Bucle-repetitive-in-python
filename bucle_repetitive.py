'''
in programare o bucla(ciclu repetitiv)este o secventa de instructiuni care se executa in mod repetat pana se indeplineste o anumita conditi
(conditia o sa fie definita de noi)
o bucla infinita este una fara un mod functional  de oprire,rezultatul este ca bucla se va repeta in continuu pana ce sistemul de operare va simtii actiunea si o va termina cu o eroare

'''
# while
# putem executa un set de instructiuni paan ce o conditie este adevarata
count = 0
while count < 3:
    count += 1  # prin comentarea liniei se forteaza o bucla infinita
    print(f'count: {count}')
# exp 2
# iterarea prin lista,parcurgerea eleemnt cu element
l = [1, 2, 3, 4, 5]
index = 0
while index < len(l):
    print(l[index])
    index += 1
print(30 * "----")

# break
print(30 * "----")
i = 1
while i < 6:
    print(i)
    if i == 3:
        break
    i += 1
print(30 * "----")
# continue
i = 0
while i < 6:
    i += 1
    if i == 3:
        continue
    print(i)
# else
count = 0
while count < 3:
    count += 1
    print(f'count : {count}')
else:
    print('Sunt in else!')
# else cu break
count = 0
while count < 3:
    count += 1
    print(f'count : {count}')
    if count == 1:
        break
else:
  print('Sunt in else!')

#for
'''
este folosita pentru a itera o secventa(lista,tuplu,set sau string)
'''
for i in range(10): # va genera o secventa de la 0 la 9 fara 10
    print(i)
print(30*'!')
for i in range(5,10): # va genera o secventa de la 5 pana la 9 fara 10

    print(i)
print(30*'!')
for i in range(2,30,2): #va genera o secventa de la 2 la 30 ,dar 30 nu este inclus cu pasul 2
    print(i)
#iterare prin lista de lemente
lst=[1,2,3,4,5]
for i in range(len(lst)):
    print(lst[i]) #indexul este i iar lst e lista
#for each
animale=['leu','caine','pisica']
for x in animale: #in loc sa iteram prin index iteram direct prin lista iar x ia valoarea fiecarui index
    print(x)
#iterare prin string
for x in 'Ana are mere':
    print(x)
#iterare prin dictionar ce face implicit prin chei
persoana={
    'nume':'Dan',
    'prenume':'Andrei',
    'varsta':30
}
for x in persoana:
    print(x)

for x in persoana.values():
    print(x)
for x,y in persoana.items():
    print(x,y)

print(30*'!')
#break cu  for
fructe=['mere','pere','banane']
for x in fructe:
    if x=='pere':
        break
    print(x)
#continue cu for
for x in fructe:
    if x=='mere':
        continue
    print(x)
#for cu else
for x in fructe:
    print(x)
else:
    print('sunt in else')
print(30*'!')
# else + break
for x in fructe:
    if x == 'pere':
        break
    print(x)
else:
    print('sunt in else')
#nested for
lista = ['mere', 'pere', 'banane','cirese']
adj=['mari','galbene','dulci']
for x in lista:
    for y in adj:
        print(x,y)
lungime_for=len(lista) * len(adj)
print(lungime_for)
print(30 * '!!')
# pass , nu face nimic
for x in [1,2,3]:
    pass

for x in range(100_000_000) :
    pass
print('gata')

print(30 * '!!')






