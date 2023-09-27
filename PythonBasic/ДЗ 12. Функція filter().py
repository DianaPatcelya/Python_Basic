inputdata = ('Країна', 'шалаш', 'Летел', 'вертольот', 'УЧУ', 'мем', 'мова')

result = filter(lambda item: item.upper() == ''.join(reversed(item.upper())), inputdata)
print(list(result))
