primos = []
for num in range (2, 100):
    es_primo = True
    for i in range (2, num):
        if num % i == 0:
            es_primo = False
            break
    if es_primo: 
        primos.append(num)
    if len(primos) == 20:
        break
print (primos)