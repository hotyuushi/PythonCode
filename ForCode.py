# def f(name, age=0):
#     print(f"name = {name},age = {age}")

# f("小明", 12)
# f("小红")
# f("小丽", 22)

def get_sum(*args):
    sum = 0
    for i in args:
        sum += i
    return sum

sum = get_sum(1, 2, 3, 5, 6,7)
print(sum)