import json
import datetime

class TaskManager:
    def __init__(self):
        self.tasks = []

    def add_task(self, title, description, due_date):
        task_id = len(self.tasks) + 1
        task = {
            'id': task_id,
            'title': title,
            'description': description,
            'due_date': due_date
        }
        self.tasks.append(task)

    def remove_task(self, task_id):
        self.tasks = [task for task in self.tasks if task['id'] != task_id]

    def update_task(self, task_id, title=None, description=None, due_date=None):
        for task in self.tasks:
            if task['id'] == task_id:
                if title:
                    task['title'] = title
                if description:
                    task['description'] = description
                if due_date:
                    task['due_date'] = due_date
                break

    def save_tasks_to_file(self, filename):
        with open(filename, 'w') as file:
            json.dump(self.tasks, file)

    def load_tasks_from_file(self, filename):
        try:
            with open(filename, 'r') as file:
                self.tasks = json.load(file)
        except FileNotFoundError:
            self.tasks = []

    def display_tasks(self, day=None):
        if not self.tasks:
            print("Brak zapisanych zadań.")
            return

        if day:
            day = day.lower()
            tasks_to_display = [
                task for task in self.tasks if self._get_day_of_week(task['due_date']) == day
            ]
        else:
            tasks_to_display = self.tasks

        for task in tasks_to_display:
            print(f"ID: {task['id']}, Tytuł: {task['title']}, Termin: {task['due_date']}")

    def _get_day_of_week(self, date_string):
        date = datetime.datetime.strptime(date_string, '%Y-%m-%d').date()
        return date.strftime('%A')

def main():
    task_manager = TaskManager()
    task_manager.load_tasks_from_file('tasks.json')

    while True:
        print("\n==== Zarządzanie Zadaniami ====")
        print("1. Dodaj nowe zadanie")
        print("2. Usuń zadanie")
        print("3. Aktualizuj zadanie")
        print("4. Wyświetl zadania")
        print("5. Zapisz zadania do pliku")
        print("6. Wyjście")

        choice = input("Wybierz opcję (1-6): ")

        if choice == '1':
            title = input("Podaj tytuł zadania: ")
            description = input("Podaj opis zadania: ")
            due_date = input("Podaj termin wykonania zadania (YYYY-MM-DD): ")
            task_manager.add_task(title, description, due_date)
            print("Zadanie zostało dodane.")

        elif choice == '2':
            task_id = int(input("Podaj ID zadania do usunięcia: "))
            task_manager.remove_task(task_id)
            print("Zadanie zostało usunięte.")

        elif choice == '3':
            task_id = int(input("Podaj ID zadania do aktualizacji: "))
            title = input("Podaj nowy tytuł zadania (naciśnij Enter, aby nie zmieniać): ")
            description = input("Podaj nowy opis zadania (naciśnij Enter, aby nie zmieniać): ")
            due_date = input("Podaj nowy termin wykonania zadania (YYYY-MM-DD) (naciśnij Enter, aby nie zmieniać): ")
            task_manager.update_task(task_id, title, description, due_date)
            print("Zadanie zostało zaktualizowane.")

        elif choice == '4':
            print("1. Wyświetl zadania z konkretnego dnia tygodnia")
            print("2. Wyświetl zadania z całego tygodnia")
            display_choice = input("Wybierz opcję (1-2): ")

            if display_choice == '1':
                day = input("Podaj dzień tygodnia (np. 'poniedziałek'): ")
                task_manager.display_tasks(day)
            elif display_choice == '2':
                task_manager.display_tasks()
            else:
                print("Nieprawidłowy wybór.")

        elif choice == '5':
            task_manager.save_tasks_to_file('tasks.json')
            print("Zadania zostały zapisane do pliku.")

        elif choice == '6':
            break

        else:
            print("Nieprawidłowy wybór. Wybierz opcję od 1 do 6.")

if __name__ == '__main__':
    main()