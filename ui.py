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

