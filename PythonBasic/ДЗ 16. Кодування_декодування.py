name = b'r\xc3\xa9sum\xc3\xa9'
print(name)
print(type(name))
print("-" * 50)

name_utf8 = name.decode()
print(name_utf8)
print(type(name_utf8))
print("-" * 50)

name_Latin1 = name_utf8.encode('Latin1')
print(name_Latin1)
print(type(name_Latin1))
print("-" * 50)

name_Latin1_str = name_Latin1.decode('Latin1')
print(name_Latin1_str)
print(type(name_Latin1_str))
print("-" * 50)
