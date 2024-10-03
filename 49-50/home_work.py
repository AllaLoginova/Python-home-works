import tkinter as tk
from abc import ABC, abstractmethod

class NoteModel:
    """База данных для хранения заметок"""

    def __init__(self):
        self._notes = [{"id": 1, "text": "Сижу на паре"}]

    def get_notes(self):
        """Посмотреть все заметки"""
        return self._notes

    def add_note(self, text):
        """Добавить заметку"""
        next_id = self._get_last_id() + 1  # получаем новый id
        note = {"id": next_id, "text": text}  # создаем заметку
        self._notes.append(note)  # добавляем в список

    def _get_last_id(self):
        """Получить крайний id"""
        max = self._notes[0]['id']
        for note in self._notes:
            if note['id'] > max:
                max = note['id']

        return max

    def _check_id(self, id_to_delete):
        """Проверить и получить индекс id из базы"""
        index_to_delete = None
        for i, note in enumerate(self._notes):
            for key, value in note.items():
                if key == 'id' and value == id_to_delete:
                    index_to_delete = i

        return index_to_delete

    def delete_note(self, id_to_delete):
        """Удалить заметку"""
        index_id_to_delete = self._check_id(id_to_delete)
        if index_id_to_delete != None:
            self._notes.pop(index_id_to_delete)
            return True
        else:
            return False


class AbstractView(ABC):
    @abstractmethod
    def render_notes(self, notes):
        pass


class GrafocView(AbstractView):
    def __init__(self):
        self.root = tk.Tk()
        self.root.title('Тестовое окошко')
        self.listbox = tk.Listbox(self.root, height=10, width=50)
        self.listbox.pack(padx=10, pady=10)

    def render_notes(self, notes):
        for note in notes:
            text = f"{note['id']} --- {note['text']}"
            self.listbox.insert(tk.END, text)
        self.root.mainloop()


class ConsoleViewe(AbstractView):
    def render_notes(self, notes):
        if len(notes) == 0:
            print("Заметок нет")
        for note in notes:
            text = f"{note['id']} --- {note['text']}"
            print(text)

    @staticmethod
    def delete_note():
        print("Заметка удалена")

    @staticmethod
    def error_id_note():
        print("Такого id нет")


class Controller:
    def __init__(self, model, view):
        self.model = model
        self.view = view

    def show_notes(self):
        """ Покзать все заметки"""
        notes = self.model.get_notes()
        self.view.render_notes(notes)
        # for note in notes:
        #     print(f"{note['id']} - {note['text']}")

    def add_note(self):
        text = input('Введи текст заметки ')
        self.model.add_note(text)

    def delete_note(self):
        self.show_notes()
        id_to_delete = int(input('Введи номер id заметки для удаления: '))
        if self.model.delete_note(id_to_delete):
            self.view.delete_note()
        else:
            self.view.error_id_note()
            self.show_notes()

model = NoteModel()
grafic_view = GrafocView()
consol_view = ConsoleViewe()
contr = Controller(model, consol_view)

while True:
    print("1 - Посмотреть все заметки ")
    print("2 - Добавить заметку ")
    print("3 - Удалить заметку ")
    print("q - Выйти")

    choice = input("Выбирай: ")
    if choice == '1':
        contr.show_notes()
    elif choice == '2':
        contr.add_note()
    elif choice == '3':
        contr.delete_note()
    elif choice == 'q':
        break