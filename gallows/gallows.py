import random
with open("questions.txt", encoding="UTF-8") as f:
    a = f.read()
    b = a.split("\n\n")
    for i in range (len(b)):
        b[i] = b[i].split("\n")
a = random.choice(b)
bukva = "_"*len(a[1])
health = "❤️❤️❤️❤️❤️"
print(a[0], health, bukva, sep='\n')
while bukva!=a[1] and "❤️" in health:
    q = input("Выберите букву ").lower()
    if q in a[1] or q.upper() in a[1]:
        for w in range (len(a[1])):
            if q==a[1][w].lower():
                bukva = bukva[:w] + a[1][w] + bukva[w+1:]
    else:
        print('Вы не угадали :( ')
        health = health.replace('❤️', '🤍', 1)
    print(a[0], health, bukva, sep='\n')
if bukva == a[1]:
    print ("Вы победили ")
else:
    print ("Вы проиграли :( ")






