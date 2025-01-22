# Модель
class Model:
    def __init__(self):
        self.data = "Привіт, шаблон MVP!"

    def get_data(self):
        return self.data

    def set_data(self, data):
        self.data = data

# Подання
class View:
    def show_data(self, data):
        print(f"Відображення даних: {data}")

    def get_input(self):
        return input("Введіть нові дані: ")

# Презентер
class Presenter:
    def __init__(self, model, view):
        self.model = model
        self.view = view

    def update_data(self):
        new_data = self.view.get_input()
        self.model.set_data(new_data)
        self.show_data()

    def show_data(self):
        data = self.model.get_data()
        self.view.show_data(data)

# Використання
if __name__ == "__main__":
    model = Model()          # Створення моделі
    view = View()            # Створення подання
    presenter = Presenter(model, view)  # Створення презентера

    # Відображення даних
    presenter.show_data()

    # Оновлення даних
    presenter.update_data()
    presenter.show_data()  # Відображення оновлених даних
