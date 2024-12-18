class Task:
    def __init__(self, name, description, priority, status='не виконано'):
        self.name = name
        self.description = description
        self.priority = priority
        self.status = status

    def __str__(self):
        return f"Завдання: {self.name}, Опис: {self.description}, Пріоритет: {self.priority}, Статус: {self.status}"

    def __repr__(self):
        return f"Task('{self.name}', '{self.description}', '{self.priority}', '{self.status}')"

class TaskList:
    def __init__(self):
        self.tasks = {}

    def add_task(self, task_id, task):
        self.tasks[task_id] = task

    def change_status(self, task_id, status):
        if task_id in self.tasks:
            self.tasks[task_id].status = status
        else:
            print(f"Завдання з ID {task_id} не знайдено.")

    def filter_by_priority(self, priority):
        return {k: v for k, v in self.tasks.items() if v.priority == priority and v.status != 'виконано'}

    def filter_by_status(self, status):
        return {k: v for k, v in self.tasks.items() if v.status == status}

    def task_statistics(self):
        completed = sum(1 for task in self.tasks.values() if task.status == 'виконано')
        not_completed = sum(1 for task in self.tasks.values() if task.status == 'не виконано')
        return {'completed': completed, 'not_completed': not_completed}

    def __str__(self):
        return "\n".join(f"ID {task_id}: {task}" for task_id, task in self.tasks.items())

# Приклад використання
task_list = TaskList()
task_list.add_task(1, Task('Вивчити Python', 'Пройти базовий курс по Python', 'високий'))
task_list.add_task(2, Task('Зробити домашнє завдання', 'Розв\'язати задачі з математики', 'середній'))
task_list.add_task(3, Task('Запланувати зустріч', 'Організувати зустріч з колегами', 'низький'))

# Зміна статусу завдання з ID  на 'виконано'
task_list.change_status(2, 'виконано')


# Виведення всіх завдань у консолі
print("______________________________________________________________________________________________________________________________")
print("Список завдань:")
print(task_list)
print("______________________________________________________________________________________________________________________________")

# Фільтрація за пріоритетом
high_priority_tasks = task_list.filter_by_priority('високий')
print("\nЗавдання з високим пріоритетом:", high_priority_tasks)
print("______________________________________________________________________________________________________________________________")

# Фільтрація за статусом
not_completed_tasks = task_list.filter_by_status('не виконано')
print("\nНе виконані завдання:", not_completed_tasks)
print("______________________________________________________________________________________________________________________________")

# Виведення статистики
statistics = task_list.task_statistics()
print("\nСтатистика завдань:", statistics)
print("______________________________________________________________________________________________________________________________")

