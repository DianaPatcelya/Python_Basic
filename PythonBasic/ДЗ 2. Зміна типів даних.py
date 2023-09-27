a_1 = (1, 3, "fff", None, True)

a_2 = (1, 3, "fff", None, True)

print(id(a_1))
print(id(a_2))

print(a_1 == a_2)

print(a_1 is a_2)

b_1 = {4: "Hello", 111: ["AOT"]}

b_2 = {4: "Hello", 111: ["AOT"]}

print(id(a_1))
print(id(a_2))

print(b_1 == b_2)

print(b_1 is b_2)
