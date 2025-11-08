a = float(input("Введите первое число: "))
b = float(input("Введите второе число: "))
action = input("Какое действие вы хотите сделать?: ")
result = 0
if action == "+":
    result = a + b
if action == "-":
    result = a - b
if action == "/":
    result = a / b
if action == "*":
    result = a * b
print(result)
