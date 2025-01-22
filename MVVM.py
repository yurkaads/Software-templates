# Модель
class Model:
    def __init__(self):
        self.data = "Привіт, шаблон MVVM!"

    def get_data(self):
        return self.data

    def set_data(self, data):
        self.data = data


# Модель подання
class ViewModel:
    def __init__(self, model):
        self.model = model

    def get_data(self):
        return self.model.get_data()

    def set_data(self, data):
        self.model.set_data(data)


# Подання
class View:
    def show_data(self, data):
        print(f"Відображення даних: {data}")

    def get_input(self):
        return input("Введіть нові дані: ")

# Використання
if __name__ == "__main__":
    model = Model()                # Створення моделі
    view_model = ViewModel(model)  # Створення моделі подання
    view = View()                  # Створення подання

    # Відображення даних
    view.show_data(view_model.get_data())

    # Оновлення даних
    new_data = view.get_input()
    view_model.set_data(new_data)

    # Відображення оновлених даних
    view.show_data(view_model.get_data())
