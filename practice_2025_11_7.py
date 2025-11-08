# num = 2
# num2 = 5
# print(num2%num)
def outer():
    def inner(y):
        x = 1
        x += y
        return x
    return inner
f = outer(); print(f(2))