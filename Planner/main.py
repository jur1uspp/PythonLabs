import tkinter as tk
from tkinter import ttk, messagebox
from tkcalendar import Calendar, DateEntry
import json

# Збереження даних подій
data_file = "events.json"

def load_events():
    try:
        with open(data_file, "r") as f:
            return json.load(f)
    except FileNotFoundError:
        return {}

def save_events(events):
    with open(data_file, "w") as f:
        json.dump(events, f, indent=4)

# Головне вікно
class EventPlanner:
    def __init__(self, root):
        self.root = root
        self.root.title("Планувальник подій")

        self.events = load_events()

        self.calendar = Calendar(self.root, selectmode="day")
        self.calendar.pack(pady=20)

        self.add_event_button = tk.Button(self.root, text="Додати подію", command=self.open_add_event_window)
        self.add_event_button.pack()

        self.view_events_button = tk.Button(self.root, text="Переглянути події дня", command=self.open_view_events_window)
        self.view_events_button.pack()

        self.exit_button = tk.Button(self.root, text="Вийти", command=self.root.quit)
        self.exit_button.pack(pady=10)

    def open_add_event_window(self):
        AddEventWindow(self.root, self.events, self.refresh_calendar)

    def open_view_events_window(self):
        selected_date = self.calendar.get_date()
        ViewEventsWindow(self.root, selected_date, self.events, self.refresh_calendar)

    def refresh_calendar(self):
        self.events = load_events()

# Вікно додавання події
class AddEventWindow:
    def __init__(self, master, events, refresh_callback):
        self.master = master
        self.events = events
        self.refresh_callback = refresh_callback

        self.window = tk.Toplevel(master)
        self.window.title("Додати подію")

        tk.Label(self.window, text="Назва події:").pack(pady=5)
        self.title_entry = tk.Entry(self.window)
        self.title_entry.pack(pady=5)

        tk.Label(self.window, text="Дата:").pack(pady=5)
        self.date_entry = DateEntry(self.window)
        self.date_entry.pack(pady=5)

        tk.Label(self.window, text="Опис:").pack(pady=5)
        self.description_text = tk.Text(self.window, height=5, width=30)
        self.description_text.pack(pady=5)

        self.save_button = tk.Button(self.window, text="Зберегти", command=self.save_event)
        self.save_button.pack(pady=5)

        self.cancel_button = tk.Button(self.window, text="Скасувати", command=self.window.destroy)
        self.cancel_button.pack(pady=5)

    def save_event(self):
        title = self.title_entry.get()
        date = self.date_entry.get()
        description = self.description_text.get("1.0", tk.END).strip()

        if not title:
            messagebox.showerror("Помилка", "Назва події не може бути порожньою.")
            return

        if date not in self.events:
            self.events[date] = []
        
        self.events[date].append({"title": title, "description": description})
        save_events(self.events)
        self.refresh_callback()
        self.window.destroy()

# Вікно перегляду подій дня
class ViewEventsWindow:
    def __init__(self, master, date, events, refresh_callback):
        self.master = master
        self.date = date
        self.events = events
        self.refresh_callback = refresh_callback

        self.window = tk.Toplevel(master)
        self.window.title(f"Події на {date}")

        self.event_list = ttk.Treeview(self.window, columns=("title", "description"), show="headings")
        self.event_list.heading("title", text="Назва події")
        self.event_list.heading("description", text="Опис")
        self.event_list.pack(fill=tk.BOTH, expand=True, pady=10)

        self.event_list.bind("<Double-1>", self.show_event_details)

        self.close_button = tk.Button(self.window, text="Закрити", command=self.window.destroy)
        self.close_button.pack(pady=5)

        self.populate_events()

    def populate_events(self):
        for item in self.event_list.get_children():
            self.event_list.delete(item)

        if self.date in self.events:
            for event in self.events[self.date]:
                self.event_list.insert("", tk.END, values=(event["title"], event["description"]))
        else:
            messagebox.showinfo("Інформація", "На цей день немає подій.")

    def show_event_details(self, event):
        selected_item = self.event_list.selection()[0]
        event_details = self.event_list.item(selected_item, "values")
        messagebox.showinfo("Деталі події", f"Назва: {event_details[0]}\nОпис: {event_details[1]}")

# Запуск програми
if __name__ == "__main__":
    root = tk.Tk()
    app = EventPlanner(root)
    root.mainloop()
