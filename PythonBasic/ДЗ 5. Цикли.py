numb = int(input("Введіть натуральне число: "))
count = 0
resalt = 0
summa = 0
while count < numb:
    count += 1
    if count % 3 == 0:
        continue
    resalt = count ** 3
    summa = summa + resalt
print("Resalt: ", summa)

print('-' * 50)

numb = int(input("Введіть натуральне число: "))
resalt = 1
summa = 0
for i in range(1, numb + 1):
    if i % 3 == 0:
        continue
    resalt = i ** 3
    summa = summa + resalt
print("Resalt: ", summa)