def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return "Ошибка: деление на ноль!"
    return a / b

def main():
    print("Простой калькулятор")
    while True:
        print("\nВыберите операцию:")
        print("1. Сложение")
        print("2. Вычитание")
        print("3. Умножение")
        print("4. Деление")
        print("5. Выход")

        choice = input("Введите номер операции (1-5): ")

        if choice == '5':
            print("Выход из программы. Пока!")
            break

        if choice not in {'1', '2', '3', '4'}:
            print("Неверный выбор. Попробуйте снова.")
            continue

        try:
            a = float(input("Введите первое число: "))
            b = float(input("Введите второе число: "))
        except ValueError:
            print("Ошибка: введено не число.")
            continue

        if choice == '1':
            print(f"Результат: {add(a, b)}")
        elif choice == '2':
            print(f"Результат: {subtract(a, b)}")
        elif choice == '3':
            print(f"Результат: {multiply(a, b)}")
        elif choice == '4':
            result = divide(a, b)
            print(f"Результат: {result}")

if __name__ == "__main__":
    main()
