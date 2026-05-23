def find_min_max(arr):
    if not arr:
        raise ValueError("Масив не може бути порожнім")

    def _divide_and_conquer(start_idx, end_idx):
        # Базовий випадок 1: у підмасиві лише один елемент
        if start_idx == end_idx:
            return (arr[start_idx], arr[start_idx])

        # Базовий випадок 2: у підмасиві два елементи
        if end_idx == start_idx + 1:
            if arr[start_idx] < arr[end_idx]:
                return (arr[start_idx], arr[end_idx])
            else:
                return (arr[end_idx], arr[start_idx])

        # Рекурсивний крок: ділимо масив навпіл
        mid = (start_idx + end_idx) // 2

        # Отримуємо мінімум і максимум для обох половин
        min_left, max_left = _divide_and_conquer(start_idx, mid)
        min_right, max_right = _divide_and_conquer(mid + 1, end_idx)

        # Порівнюємо результати половин і повертаємо загальний мінімум і максимум
        return (min(min_left, min_right), max(max_left, max_right))

    return _divide_and_conquer(0, len(arr) - 1)


numbers = [3, 1, 9, 7, 5, 2, 8, 4, 0, 6]
min_val, max_val = find_min_max(numbers)
print(f"Мінімум: {min_val}, Максимум: {max_val}")
