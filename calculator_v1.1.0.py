a = int(input("Введите первое число: "))
b = int(input("Введите второе число: "))
action = input("Какое действие вы хотите сделать?: ")
result = 0
if action == "+":
    result = a + b
if action == "-":
    result = a - b
print(result)
    
