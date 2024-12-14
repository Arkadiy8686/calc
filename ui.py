import tkinter as tk
from calc_operations import (
    addition, subtraction, multiplication, division, modulus, power,
    square_root, sine, cosine, floor_value, ceil_value,
)

from calc_operations import Memory

# Создаем экземпляр класса Memory
memory = Memory()

# Глобальная переменная для отображения текста в поле ввода
entry_text = None

def on_button_click(value):
    """Обрабатывает нажатие кнопок цифр и операций."""
    entry_text.set(entry_text.get() + value)

def on_clear():
    """Очищает поле ввода."""
    entry_text.set("")

def on_backspace():
    """Удаляет последний символ из поля ввода."""
    current_text = entry_text.get()
    entry_text.set(current_text[:-1])

def on_equal():
    """Выполняет вычисление введенного выражения."""
    try:
        # Преобразуем ^ в ** для возведения в степень
        expression = entry_text.get().replace("^", "**")
        result = eval(expression)
        entry_text.set(result)
    except ZeroDivisionError:
        entry_text.set("Error: Division by zero")
    except SyntaxError:
        entry_text.set("Error: Invalid syntax")
    except Exception as e:
        entry_text.set(f"Error: {e}")

def on_memory_add():
    """Добавить значение в память."""
    try:
        value = float(entry_text.get())
        memory.m_add(value)
        entry_text.set("")
    except ValueError:
        entry_text.set("Error: Invalid input")

def on_memory_subtract():
    """Вычесть значение из памяти."""
    try:
        value = float(entry_text.get())
        memory.m_subtract(value)
        entry_text.set("")
    except ValueError:
        entry_text.set("Error: Invalid input")

def on_memory_multiply():
    """Умножить значение в памяти."""
    try:
        value = float(entry_text.get())
        memory.m_multiply(value)
        entry_text.set("")
    except ValueError:
        entry_text.set("Error: Invalid input")

def on_memory_divide():
    """Разделить значение в памяти."""
    try:
        value = float(entry_text.get())
        memory.m_divide(value)
        entry_text.set("")
    except ValueError:
        entry_text.set("Error: Invalid input")
    except ZeroDivisionError:
        entry_text.set("Error: Cannot divide by zero")

def on_memory_recall():
    """Получить значение из памяти."""
    entry_text.set(str(memory.m_recall()))

def on_memory_clear():
    """Очистить память."""
    memory.m_clear()
    entry_text.set("")

def on_memory_delete():
    """Удалить последнюю операцию из памяти."""
    try:
        memory.delete_last()
        entry_text.set(str(memory.m_recall()))
    except ValueError:
        entry_text.set("Error: No operations to delete")

def on_history():
    """Открывает окно с историей операций с памятью."""
    history_window = tk.Toplevel()
    history_window.title("Memory History")
    
    # Получаем историю из памяти
    history_list = memory.get_history()

    # Отображаем историю в окне
    history_text = tk.Text(history_window, width=40, height=10)
    history_text.pack(padx=10, pady=10)

    if history_list:
        for operation in history_list:
            history_text.insert(tk.END, f"{operation}\n")
    else:
        history_text.insert(tk.END, "No operations in history.")
    
    # Делаем поле только для чтения
    history_text.config(state=tk.DISABLED)

def on_modulus():
    """Добавляет знак остатка от деления в поле ввода."""
    entry_text.set(entry_text.get() + " % ")

def on_sine():
    """Вычисляет синус."""
    try:
        value = float(entry_text.get())
        result = sine(value)
        entry_text.set(result)
    except ValueError:
        entry_text.set("Error: Invalid input")

def on_cosine():
    """Вычисляет косинус."""
    try:
        value = float(entry_text.get())
        result = cosine(value)
        entry_text.set(result)
    except ValueError:
        entry_text.set("Error: Invalid input")

def on_power():
    """Добавляет знак возведения в степень в поле ввода."""
    entry_text.set(entry_text.get() + " ^ ")

def on_square_root():
    """Вычисляет квадратный корень."""
    try:
        value = float(entry_text.get())
        result = square_root(value)
        entry_text.set(result)
    except ValueError:
        entry_text.set("Error: Invalid input")

def on_floor():
    """Округляет число в меньшую сторону."""
    try:
        value = float(entry_text.get())
        result = floor_value(value)
        entry_text.set(result)
    except ValueError:
        entry_text.set("Error: Invalid input")

