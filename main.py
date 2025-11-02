# Функція Образцова Д.Є.
# Функція для запису даних у текстовий файл
def write_to_file(filename):
    try: 
        with open(filename, "w") as f:
            f.write("Образцов\n")
            f.write("Питання: Як працює оператор try-except у Python?\n")
    except Exception as e: print("Помилка під час роботи з файлом:", e)
    else: print("Дані записано у файл.")

write_to_file("python.txt")

# Функція Гришанова К.А.
# Функція для запису даних у текстовий файл
def student_2_add_answer(filename):
    try:
        # encoding='utf-8' потрібен для кирилиці
        with open(filename, "a", encoding="utf-8") as f:
            f.write("Гришанов\n")
            # Відповідь на питання "Як працює try-except?"
            f.write("Відповідь: try-except - це інструмент для обробки помилок. Код, який може 'впасти', кладуть у блок 'try'. Якщо помилка стається, Python виконує блок 'except' замість 'падіння' програми.\n")
            # Нове питання
            f.write("Питання: Яка різниця між 'списком' (list) та 'кортежем' (tuple) в Python?\n")

            print("Дані Студента 2 успішно додано.")
    except FileNotFoundError:
        # Конкретна обробка: якщо файлу не існує
        print(f"ПОМИЛКА: Файл '{filename}' не знайдено!")
    except PermissionError:
        # Конкретна обробка: якщо немає прав доступу
        print(f"ПОМИЛКА: Немає доступу до файлу '{filename}'.")
    except Exception as e:
        # "Запасний" варіант для всіх інших помилок
        print(f"ПОМИЛКА: Сталася неочікувана помилка: {e}")

student_2_add_answer("python.txt")