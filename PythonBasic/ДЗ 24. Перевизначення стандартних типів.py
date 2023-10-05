class MyString(str):

    def __add__(self, other):
        return MyString(str(self) + str(other))

    def __radd__(self, other):
        return MyString(str(other) + str(self))

    def __sub__(self, other):
        return MyString(str(self).replace(str(other), "", 1))

    def __rsub__(self, other):
        return MyString(str(other).replace(str(self), "", 1))


print(MyString("New") + MyString(890) + "         " + type(MyString("New") + MyString(890)))
print((MyString(1234) + 5678) + "         " + type(MyString(1234) + 5678))
print((MyString("New") + "castle") + "            " + type(MyString("New") + "castle"))
print((MyString("New") + 77) + "          " + type(MyString("New") + 77))
print((MyString("New") + True) + "            " + type(MyString("New") + True))
print((MyString("New") + ["s", " ", 23]) + "          " + type(MyString("New") + ["s", " ", 23]))
print((MyString("New") + None) + "            " + type(MyString("New") + None))

print("-" * 50)

print((MyString("New bala7nce") - 7) + "         " + type(MyString("New bala7nce") - 7))
print((MyString("New balance") - "bal") + "           " + type(MyString("New balance") - "bal"))
print((MyString("New balance") - "Bal") + "           " + type((MyString("New balance") - "Bal")))
print((MyString("pineapple apple pine") - "apple") + "     " + type(MyString("pineapple apple pine") - "apple"))
print((MyString("New balance") - "apple") + "         " + type(MyString("New balance") - "apple"))
print((MyString("NoneType") - None) + "           " + type(MyString("NoneType") - None))
print((MyString(55678345672) - 7) + "         " + type(MyString(55678345672) - 7))
