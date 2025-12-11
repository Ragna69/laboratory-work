# класс кошка, кошка может быть домашняя, а может быть дикая, у каждой кошки есть свои методы и характеристики:
# цвет, возраст, пол. У кошек есть методы, гулять где хочет, сладко спать, играть с мячом, охотится,
# показать процесс наследования классов и переопределение методов. через пользовательский ввод создать кошку,
# выбрать кошку, с которой будем взаимодействовать, попросить сделать действие
# (например прошу метод помяукать и выводится слово мяу, есть просить покушать, то длинное мяууу и тд).
# нужно сделать свою ошибку через новый класс WildHasNoNameError(Exception): pass и обработать ее в классе WildCat

class Cat:
    def __init__(self, name, color, age, gender):
        self.name = name
        self.color = color
        self.age = age
        self.gender = gender

    def meow(self):
        print(f'{self.name}: Мяу!')

    def sleep(self):
        print(f'{self.name}: Кошка заснула...')

    def eat(self):
        print(f'{self.name}: Кошка кушает: "Ням Ням!"')

    def play(self):
        print(f'{self.name}: Кошка играет!')
        self.meow()

    def __str__(self):
        return f'{self.name} - {self.color}, {self.age}, {self.gender}'


class HomeCat(Cat):
    def meow(self):
        print(f"{self.name}: Мяу! (домашнее)")

    def sleep(self):
        print(f'{self.name}: Кошка заснула на кровати...')

    def eat(self):
        print(f'{self.name}: Кошка кушает: "Ням Ням!"')

    def play(self):
        print(f'{self.name}: Кошка играет с мячом!')


class WildCatHasNoNameError(Exception):
    """Исключение: дикому коту нельзя давать имя"""
    pass

class WildCat(Cat):
    def __init__(self, name, color, age, gender):
        if name.strip():
            raise WildCatHasNoNameError("Ошибка: Дикий кот не может иметь имя!")
        super().__init__("ДикийКот", color, age, gender)

    def meow(self):
        print(f'{self.name}: Мяяяу! (Дико)')

    def sleep(self):
        print(f'{self.name}: Кошка заснула на траве...')

    def eat(self):
        print(f'{self.name}: Кошка кушает мертвую мышь...')

    def play(self):
        print(f'{self.name}: Бегает за птицами...')


class CatCreate:
    def __init__(self):
        self.cats = {}
        self.next_id = 1

    def create_cat(self):
        print("Выберите тип кошки: 1 - домашняя, 2 - дикaя")
        choice = input("Введите номер: ").strip()
        name = input("Введите имя кошки: ").strip()
        color = input("Цвет: ").strip()
        age = input("Возраст: ").strip()
        gender = input("Пол: ").strip()

        try:
            if choice == "1":
                cat = HomeCat(name, color, age, gender)
            elif choice == "2":
                cat = WildCat(name, color, age, gender)
            else:
                print("Ошибка: Неверный выбор типа кошки.")
                return
        except WildCatHasNoNameError as e:
            print(e)
            return

        cat_id = self.next_id
        self.cats[cat_id] = cat
        self.next_id += 1
        print(f"Кошка создана (ID: {cat_id}): {cat.name}, {cat.color}, {cat.age}, {cat.gender}")

    def interact(self):
        if not self.cats:
            print("Нет кошек для взаимодействия.")
            return
        print("Доступные кошки:")
        for c_id, cat in self.cats.items():
            print(f"- {c_id}: {cat.name} ({'домашняя' if isinstance(cat, HomeCat) else 'дикая'})")
        try:
            c_id = int(input("Введите ID: "))
            cat = self.cats[c_id]
            print("1 - мяукать, 2 - спать, 3 - кушать, 4 - поиграть")
            action = input("Выберите действие: ").strip()
            if action == "1": cat.meow()
            elif action == "2": cat.sleep()
            elif action == "3": cat.eat()
            elif action == "4": cat.play()
            else: print("Ошибка: Нет такого действия.")
        except (ValueError, KeyError):
            print("Ошибка: Неверный ID.")

    def start(self):
        while True:
            print("\nМеню:")
            print("1 - Создать кошку")
            print("2 - Взаимодействовать")
            print("0 - Выход")
            choice = input("Выберите: ").strip()
            if choice == "1": self.create_cat()
            elif choice == "2": self.interact()
            elif choice == "0": print("Выход из системы"); break
            else: print("Ошибка: Неверный ввод.")


CatCreate().start()