import tkinter as tk
from tkinter import ttk, messagebox
import random
import json

window = tk.Tk()
window.title("Random Task Generator")
window.geometry("400x500")

#список дел
tasks = [
    "Прочитать статью (учёба)",
    "Сделать зарядку (спорт)", 
    "Написать отчёт (работа)",
    "Решить задачу (учёба)",
    "Пробежать 5 км (спорт)",
    "Позвонить клиенту (работа)"
]

history = []
#кнопка
current_label = tk.Label(window, text="Нажми кнопку!")
current_label.pack(pady=20)
#генерация задачи
def generate_task():
    global current_label
    task = random.choice(tasks)
    current_label.config(text=task)
    history.append(task)
    update_list()

generate_btn = tk.Button(window, text="Сгенерировать задачу", command=generate_task, width=20, height=2)
generate_btn.pack(pady=10)
#сортировка
filter_var = "все"
filter_label = tk.Label(window, text="Фильтр: все, учёба, спорт, работа")
filter_label.pack()

def change_filter():
    global filter_var
    if filter_var == "все":
        filter_var = "учёба"
    elif filter_var == "учёба":
        filter_var = "спорт"
    elif filter_var == "спорт":
        filter_var = "работа"
    else:
        filter_var = "все"
    filter_label.config(text=f"Фильтр: {filter_var}")
    update_list()

#сменить фильтр
filter_btn = tk.Button(window, text="Сменить фильтр", command=change_filter)
filter_btn.pack(pady=5)

history_list = tk.Listbox(window, height=15, width=50)
history_list.pack(pady=10)

def update_list():
    history_list.delete(0, tk.END)
    for task in history:
        if filter_var == "все" or filter_var in task:
            history_list.insert(tk.END, task)

#новая задачка

new_task_entry = tk.Entry(window, width=40)
new_task_entry.pack(pady=5)
add_btn = tk.Button(window, text="Добавить задачу", command=lambda: add_new_task())
add_btn.pack()

def add_new_task():
    text = new_task_entry.get().strip()
    if text:
        tasks.append(text)
        new_task_entry.delete(0, tk.END)
    else:
        tk.messagebox.showerror("Ошибка", "Задача не может быть пустой!")

#история

def save_history():
    with open("history.json", "w") as f:
        json.dump(history, f)

def load_history():
    global history
    try:
        with open("history.json", "r") as f:
            history = json.load(f)
        update_list()
    except:
        history = []

load_history()
window.protocol("WM_DELETE_WINDOW", save_history)
window.mainloop()