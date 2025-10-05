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
class Bank:


    # def Client_Find(self, client_id):

    def TransferOfCurrency(self, from_client_id, from_currency, to_client_id, to_currency, amount):
        from_client = self.in_client(from_client_id)
        to_client = self.in_client(to_client_id)
        from_account = from_client.get_account(from_currency)
        to_account = to_client.get_account(to_currency)
        if from_account.currency != to_account.currency:
            raise CurrencyMismatch("Переводы разных валют запрещены.")
        from_account.withdraw(amount)
        to_account.deposit(amount)
        print(
            f"Перевод {amount} {from_currency} со счета {from_client.name} "
            f"в {to_currency} на счет {to_client.name} в {to_currency}"
        )







