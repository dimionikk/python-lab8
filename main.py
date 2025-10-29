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
