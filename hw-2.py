import re
from typing import Callable, Generator

def generator_numbers(text: str) -> Generator[float, None, None]:
    # Знаходимо всі числа з десятковою крапкою, які відокремлені пробілами
    numbers = re.findall(r'\b\d+\.\d+\b', text)
    for num in numbers:
        yield float(num)

def sum_profit(text: str, func: Callable[[str], Generator[float, None, None]]) -> float:
    return sum(func(text))