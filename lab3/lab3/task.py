# Создайте классы, для описания банковской системы: банк, банковский
# счет, клиент. Каждый счет должен быть закреплен за клиентом, и иметь свою
# валюту. Клиент может иметь несколько счетов, но только по одному для каждой валюты.
# Для каждой сущности добавьте уместные поля (на ваш выбор).
# Реализуйте следующие методы:
# 1. Открыть счет для клиента.
# 2. Закрыть счет клиента.
# 3. Пополнить банковский счет.
# 4. Снять сумму со счета.
# 5. Перевести деньги между счетами.
# Добавьте исключения там, где это уместно (например, при попытке
# снять со счета больше, чем текущий баланс).
# Реализуйте интерфейс в терминале для задачи. Используйте цикл while
# True, на каждой итерации показывая пользователю меню с возможными
# действиями и предлагая пользователю выбрать одно из них через input().
# Интерфейс должен запрашивать у пользователя его ID, а потом
# предоставлять ему возможность для выполнения описанных банковских
# операций. Добавьте проверки на то, что только владелец счета может
# выполнять операции над ним.
# Добавьте возможность сделать выписку по всем счетам пользователя:
# сохранение в файл информации о счетах, их текущем балансе, и суммарном
# балансе.

import json

class ClientAlreadyExists(Exception): # Ошибка: клиент с таким ID уже существует
    pass

class AccountAlreadyExists(Exception): # Ошибка: счёт в валюте уже открыт у клиента
    pass

class AccountNotFound(Exception): # счёт в указанной валюте не найден
    pass

class InsufficientFunds(Exception): # недостаточно средств на счёте
    pass

class CurrencyMismatch(Exception): # попытка перевода между разными валютами
    pass

class ClientNotFound(Exception): # клиент с таким ID не найден
    pass

class Client:
    def __init__(self, name, surname, client_id):
        self.name = name
        self.surname = surname
        self.client_id = client_id
        self.accounts = {} # словарь: ключ — валюта, значение — объект Account;

    def open_account(self, currency):
        if currency in self.accounts:
            raise AccountAlreadyExists(f"Счёт в валюте {currency} уже существует.")
        self.accounts[currency] = Account(currency)  # создаёт новый счёт в указанной валюте
        print(f"Счёт в {currency} открыт.")

    def close_account(self, currency):
        if currency not in self.accounts:
            raise AccountNotFound(f"Счёт в валюте {currency} не найден.")
        del self.accounts[currency] # удаляет счёт из словаря
        print(f"Счёт в {currency} закрыт.")

    def get_account(self, currency):
        if currency not in self.accounts:
            raise AccountNotFound(f"Счёт в валюте {currency} не найден.")
        return self.accounts[currency] # возвращает объект счёта по валюте

    def get_summary(self): # осздаёт словарь: валюта → баланс
        summary = {cur: acc.balance for cur, acc in self.accounts.items()}
        total = sum(summary.values()) # суммарный баланс по всем счетам
        return summary, total # возвращает словарь и сумму

# Класс счёта
class Account:
    def __init__(self, currency, balance=0):
        self.currency = currency  # валюта счёта
        self.balance = balance  # начальный баланс (по умолчанию 0)

    def deposit(self, amount):
        self.balance += amount # увеличивает баланс на указанную сумму
        print(f"Пополнено: {amount} {self.currency}")

    def withdraw(self, amount):
        if amount > self.balance:
            raise InsufficientFunds("Недостаточно средств.")# проверка на превышение баланса
        self.balance -= amount # уменьшает баланс
        print(f"Снято: {amount} {self.currency}")


class Bank:
    def __init__(self):
        self.clients = {}  # словарь: client_id → объект Client

    def create_client(self, name, surname, client_id):
        if client_id in self.clients:
            raise ClientAlreadyExists("Клиент уже существует.")
        self.clients[client_id] = Client(name, surname, client_id) # Создаём клиента
        print(f"Клиент создан: {surname} {name}, ID: {client_id}")

    def get_client(self, client_id):
        if client_id not in self.clients:
            raise ClientNotFound("Клиент не найден.")
        return self.clients[client_id] # возвращает клиента по ID

    def transfer(self, from_client_id, from_currency, to_client_id, to_currency, amount):
        from_client = self.get_client(from_client_id)  # получает отправителя
        to_client = self.get_client(to_client_id)  # получает получателя

        from_acc = from_client.get_account(from_currency)  # счёт отправителя
        to_acc = to_client.get_account(to_currency)  # счёт получателя

        if from_acc.currency != to_acc.currency:
            raise CurrencyMismatch("Нельзя переводить между разными валютами.")

        from_acc.withdraw(amount)  # снимает средства
        to_acc.deposit(amount)  # переводит получателю
        print(f"Переведено {amount} {from_currency} от {from_client.name} к {to_client.name}")

    def export_summary(self, client_id):
        client = self.get_client(client_id) # получает клиента
        summary, total = client.get_summary() # получает данные по счетам
        data = {
            "client": f"{client.surname} {client.name}", # имя клиента
            "accounts": summary, # балансы по валютаи
            "total_balance": total # общий баланс
        }
        # сохраняет данные в JSON-файл
        with open(f"{client_id}_summary.json", "w", encoding="utf-8") as f: # "w" если файл существует, он будет перезаписан.
            json.dump(data, f, ensure_ascii=False) #indent=
        print("Выписка сохранена.")# ensure_ascii=False позволяет сохранять не-ASCII символы (например, кириллицу) как есть

def main():
    bank = Bank()  # создаёт объект в банке

    while True:
        print("\n╭─┬─┬──────────────────────┬─┬─╮")
        print("│ │ │   БАНКОВСКОЕ МЕНЮ    │ │ │")
        print("├─┴─┴──────────────────────┴─┴─┤")
        print("│ ╭─╮  1.Создать клиента   ╭─╮ │")
        print("├─┴─┴──────────────────────┴─┴─┤")
        print("│       2.Открыть счёт         │")
        print("├─┬─┬──────────────────────┬─┬─┤")
        print("│ ╰─╯    3.Закрыть счёт    ╰─╯ │")
        print("├─┬─┬──────────────────────┬─┬─┤")
        print("│ │ │   4.Пополнить счёт   │ │ │")
        print("├─┴─┴──────────────────────┴─┴─┤")
        print("│ ╭─╮   5.Снять со счёта   ╭─╮ │")
        print("├─┴─┴──────────────────────┴─┴─┤")
        print("│ 6. Перевести между клиентами │")
        print("├─┬─┬──────────────────────┬─┬─┤")
        print("│ ╰─╯ 7. Выписка по счетам ╰─╯ │")
        print("├─┬─┬──────────────────────┬─┬─┤")
        print("│ │ │       0. Выход       │ │ │")
        print("╰─┴─┴──────────────────────┴─┴─╯")

        choice = input("Выберите действие: ")

        try:
            if choice == "1":
                name = input("Имя: ")
                surname = input("Фамилия: ")
                client_id = input("ID: ")
                bank.create_client(name, surname, client_id)

            elif choice == "2":
                client_id = input("Ваш ID: ")
                currency = input("Валюта счёта: ")
                bank.get_client(client_id).open_account(currency)

            elif choice == "3":
                client_id = input("Ваш ID: ")
                currency = input("Валюта счёта: ")
                bank.get_client(client_id).close_account(currency)

            elif choice == "4":
                client_id = input("Ваш ID: ")
                currency = input("Валюта: ")
                amount = float(input("Сумма: "))
                bank.get_client(client_id).get_account(currency).deposit(amount)

            elif choice == "5":
                client_id = input("Ваш ID: ")
                currency = input("Валюта: ")
                amount = float(input("Сумма: "))
                bank.get_client(client_id).get_account(currency).withdraw(amount)

            elif choice == "6":
                from_id = input("Ваш ID: ")
                to_id = input("ID получателя: ")
                currency = input("Валюта: ")
                amount = float(input("Сумма: "))
                bank.transfer(from_id, currency, to_id, currency, amount)

            elif choice == "7":
                client_id = input("Ваш ID: ")
                bank.export_summary(client_id)

            elif choice == "0":
                print("Выход из системы.")
                break

            else:
                print("Неверный выбор.")

        except Exception as e: # сохраняет ошибку в переменную и выводит ее потом, чтоб программа не прерывалась, а сообщала об ошибке
            print(f"Ошибка: {e}")

if __name__ == "__main__":
    main() # запускаем интерфейс



