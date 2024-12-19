# TODO решите задачу
import json
def task() -> float:
    # Открываем и читаем JSON файл
    with open('input.json.', 'r') as file:
        data = json.load(file)

    # Вычисляем сумму произведений
    total = sum(item['score'] * item['weight'] for item in data if 'score' in item and 'weight' in item)

    # Возвращаем округленное значение
    return round(total, 3)
print(task())
