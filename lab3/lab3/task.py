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
from datetime import datetime

class ClientAlreadyExists(Exception):
    # Ошибка, клиент с таким именем уже существует.
    pass

class SuchACurrencyDoesNotExists(Exception):
    # Ошибка, такой валюты не существует.
    pass

class YourBalanceIsNotEnoughFunds(Exception):
    # Ошибка, на вашем балансе недостаточно средств.
    pass

class IncorrectPassword(Exception):
    # Ошибка, вы ввели неправильный пароль.
    pass

class AccountWithSuchACurrencyAlreadyExists(Exception):
    # Ошибка, счет с такой валютой уже существует.
    pass

class NotFoundAnAccountWithThisCurrency(Exception):
    # Ошибка, счет с этой валютой не найден.
    pass



class Bank:
    def initialisation (self, client = None):
        if client:
            self.client = client
        else:
            self.client = []        # self.client = client if client else []

    def create_client(self, name, surname, client_id):
        if client_id not in self.client:
            self.client[client_id] = idclient(name, surname, client_id) # ???
            print(f'Клиент Добавлен: {surname}, {name}, ID: {client_id}')
        else:
            print('Такой клиент уже существует.')

    def in_client(self, client_id):
        if client_id not in self.client:
            raise "Такого клиента не существует." #???

    def Client_Find(self, client_id):


# def (self, client_id):
# def (self, client_id):




