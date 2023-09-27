values = [1, 2, '3', 'forth', 'end', 99, True, None]

result_2 = list(map(lambda item: (str(item) if (type(item) is int) else item), values))

print(result_2)
