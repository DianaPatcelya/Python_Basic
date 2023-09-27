var_1 = "Перший рядок"
var_2 = "Другий рядок"
var_3 = "Третій рядок"
var_4 = "Четвертий рядок"

f = open('Збереження_дозапис у файл.txt', 'w')
f.write(f'{var_1}\n{var_2}\n')
f.close()
with open('Збереження,дозапис у файл.txt', 'a') as f:
    f.write(f'{var_3}\n{var_4}\n')
