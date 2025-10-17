def add(a, b)  # ошибка: пропущен двоеточие
    return a + b

def subtract(a, b):
    return a + b  # ошибка: должна быть операция вычитания

def multipy(a, b):  # опечатка в имени функции
    return a * b

def divide(a, b):
    return a / b  # нет проверки деления на ноль

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

        if choice == '6':  # ошибка: должно быть '5' для выхода
            print("Выход из программы. Пока!")
            break

        if choice not in {'1', '2', '3', '4'}:
            print("Неверный выбор. Попробуйте снова.")
            continue

        try:
            a = int(input("Введите первое число: "))
            b = int(input("Введите второе число: "))
        except ValueError:
            print("Ошибка: введено не число.")
            continue

        if choice == '1':
            print(f"Результат: {add(a, b)}")
        elif choice == '2':
            print(f"Результат: {subtract(a, b)}")
        elif choice == '3':
            print(f"Результат: {multipy(a, b)}")  # ошибка: вызов функции с опечаткой
        elif choice == '4':
            print(f"Результат: {divide(a, b)}")

if __name__ == "__main__":
    main()
