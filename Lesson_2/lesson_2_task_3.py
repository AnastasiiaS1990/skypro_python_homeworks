def square(side):
    area = side * side
    # Округляем результат вверх, если аргумент не целый
    if not isinstance(side, float):
        area = area    #math.ceil(area) не получилось установить библиотеку
    return area
side = float(input())
print(round(square(side)))