# Модель
class Model:
    def __init__(self):
        self.data = "Привіт, шаблон MVC!"

    def get_data(self):
        return self.data

    def set_data(self, data):
        self.data = data

# Подання
class View:
    def show_data(self, data):
        print(f"Відображення даних: {data}")

# Контролер
class Controller:
    def __init__(self, model, view):
        self.model = model
        self.view = view

    def update_data(self, new_data):
        self.model.set_data(new_data)
        self.show_data()

    def show_data(self):
        data = self.model.get_data()
        self.view.show_data(data)

# Використання
if __name__ == "__main__":
    model = Model()         # Створення моделі
    view = View()           # Створення подання
    controller = Controller(model, view)  # Створення контролера

    # Відображення даних
    controller.show_data()

    # Оновлення даних
    controller.update_data("Нові дані від Контролера!")
