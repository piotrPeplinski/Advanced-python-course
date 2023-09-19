import numpy as np
import matplotlib.pyplot as plt
import pandas as pd


class BankAccount:
    accounts = []

    def __init__(self, balance: float, owner_age: int):
        self.__balance = balance
        self.owner_age = owner_age
        BankAccount.accounts.append(self)

    def deposit(self, amount: int) -> bool:
        """Method used to add money to account

        Args:
            amount (int): Amount to deposit

        Returns:
            bool: Return True if deposit successful. Returns False if invalid amount is passed.
        """
        if amount > 0:
            self.__balance += amount
            return True
        else:
            return False

    def withdraw(self, amount):
        if amount > 0 and amount <= self.__balance:
            self.__balance -= amount
            return True
        else:
            return False

    @classmethod
    def summary(cls):
        money = 0
        for account in cls.accounts:
            money += account.__balance
        return money

    @classmethod
    def age_balance_chart(cls):
        balances = []
        ages = []
        for account in cls.accounts:
            balances.append(account.__balance)
            ages.append(account.owner_age)
        df = pd.DataFrame({
            'Savings': balances,
            'Age': ages
        })
        df.sort_values(by=['Age'], inplace=True)

        plt.plot(df['Age'], df['Savings'])
        plt.title('Age impact on savings')
        plt.xlabel('Age')
        plt.grid()
        plt.ylabel('Savings')
        plt.show()

    @classmethod
    def balance_pie_chart(cls):
        balances = [
            account.__balance
            for account in cls.accounts
        ]
        labels = ['Kacper', 'Kacper', 'Kacper', 'Kacper', 'Kacper']
        explode_values = [0, 0, 0.15, 0, 0]
        plt.pie(np.array(balances), labels=labels, explode=explode_values, shadow=True)

        plt.show()

    @staticmethod
    def currency_converter(amount, exchange_rate):
        return amount*exchange_rate

    def __str__(self):
        return f'Bank account: {self.__balance} PLN'


class JuniorBankAccount(BankAccount):
    def __init__(self, balance: float, owner_age: int, interest_rate: float = 2.5):
        super().__init__(balance, owner_age)
        self.__interest_rate = interest_rate

    def add_interest(self):
        self._BankAccount__balance += self._BankAccount__balance * \
            (self.__interest_rate/100)
        return True
# BankAccount()


marek = BankAccount(200, 30)

piotr = BankAccount(230, 35)

andrzej = BankAccount(400, 40)

janusz = BankAccount(100, 45)


kacperek = JuniorBankAccount(100, 15)
# BankAccount.age_balance_chart()
BankAccount.balance_pie_chart()
