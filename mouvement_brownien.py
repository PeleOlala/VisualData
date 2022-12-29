from random import choice


class BrownienMouve:
    """класс що генерує броуновські рухи"""

    def __init__(self, num_pointes=5000):
        """Iніціалізуємо атрибути блукання"""
        self.num_pointes = num_pointes
        self.x_values = [0]
        self.y_values = [0]
    def get_demarcher(self):
        return choice([-1, 1])*choice([i for i in range(4)])
    def fill_walk(self):
        """обчислемо всі точки блукання"""
        while len(self.x_values) < self.num_pointes:
            x_demarche = self.get_demarcher()
            y_demarche = self.get_demarcher()

            if x_demarche + y_demarche == 0:
                continue
            x = self.x_values[-1] + x_demarche
            y = self.y_values[-1] + y_demarche

            self.x_values.append(x)
            self.y_values.append(y)
