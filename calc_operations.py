import math
import decimal  
from decimal import Decimal

def addition(a, b):
    a = validate_decimal(a)  # Валидация входных данных
    b = validate_decimal(b)  # Валидация входных данных
    return a + b

def subtraction(a, b):
    a = validate_decimal(a)
    b = validate_decimal(b)
    return a - b

def multiplication(a, b):
    a = validate_decimal(a)
    b = validate_decimal(b)
    return a * b

def division(a, b):
    a = validate_decimal(a)
    b = validate_decimal(b)
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b

def modulus(a, b):
    a = validate_decimal(a)
    b = validate_decimal(b)
    return a % b

def power(a, b):
    a = validate_decimal(a)
    b = validate_decimal(b)
    return a ** b

def square_root(a):
    a = validate_decimal(a)
    if a < 0:
        raise ValueError("Cannot take square root of a negative number")
    return a.sqrt()

def sine(a):
    a = validate_decimal(a)  # Валидация
    return round(math.sin(math.radians(a)), 15)

def cosine(a):
    a = validate_decimal(a)  # Валидация
    return round(math.cos(math.radians(a)), 15)

def floor_value(a):
    return math.floor(a)

def ceil_value(a):
    return math.ceil(a)

def validate_decimal(value):
    try:
        # Попытка преобразовать значение в Decimal
        return Decimal(value)
    except (ValueError, TypeError, decimal.InvalidOperation):
        # Бросаем исключение с понятным сообщением
        raise ValueError("Invalid input: Please enter a valid number")

class Memory:
    def __init__(self):
        self.memory = Decimal(0)
        self.history = []

    def m_add(self, value):
        """Добавить значение в память."""
        value = validate_decimal(value)  # Валидация значения
        self.memory += value
        self.history.append(value)

    