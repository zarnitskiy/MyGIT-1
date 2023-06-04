import re
def calculate(expression):
    # Удаление пробелов из выражения
    expression = expression.replace(" ", "")

    # Проверка наличия только разрешенных символов
    if not re.match(r'^[\d+\-*/().]+$', expression):
        return "Некорректное выражение"

    try:
        result = eval(expression)  # Вычисление выражения с помощью функции eval()
        return result
    except ZeroDivisionError:
        return "Деление на ноль недопустимо"
    except Exception:
        return "Ошибка вычисления"

# Пример использования калькулятора
expression = input("Введите математическое выражение: ")
result = calculate(expression)
print("Результат:", result)