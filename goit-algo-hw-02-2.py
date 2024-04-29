from collections import deque

def is_palindrome(s) -> bool:
    # Видалення пробілів та перетворення рядка у нижній регістр
    s = ''.join([ch.lower() for ch in s if ch.isalpha()])
    # Створення двосторонньої черги та додавання символів до неї
    deq = deque(s)

    # Порівняння символів з обох кінців черги
    while len(deq) > 1:        
        if deq.pop() != deq.popleft():     
            return False
    return True
    

# Приклад використання:
input_str = "redivider"
print(is_palindrome(input_str))