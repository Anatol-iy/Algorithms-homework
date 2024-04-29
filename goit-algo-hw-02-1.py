import queue
import time 
import random


count = 0

# Створення черги заявок
request_queue = queue.Queue()

class Request:
    def __init__(self, id_number):
        self.id_number = id_number

def generate_request():
    global count
    while True:
        # Створити нову заявку
        new_request = Request(count)
        count += 1
        # Додати заявку до черги
        request_queue.put(new_request)
        print(f"Заявка {new_request.id_number} додана до черги.")
        time.sleep(random.uniform(0.5, 2.0))

def process_request():   
    while True:
        if not request_queue.empty():
            # Видаляємо заявку з черги
            request = request_queue.get()
            print(f"Заявка {request.id_number} обробляється.")
            # Симуляція затримки обробки
            time.sleep(random.uniform(0.5, 2.0))
        else:
            print("Черга порожня.")
        time.sleep(1)

try:
    while True:
        generate_request()
        process_request()
# Ctrl+C
except KeyboardInterrupt:
    print("Програма завершена користувачем")



