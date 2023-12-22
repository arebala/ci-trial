import pickle
from collections import namedtuple

Transaction = namedtuple('Transaction', ['date', 'price', 'quantity'])

class Stock:
    def __init__(self, code, quantity, date, price):
        self.code = code
        self.ave_buy_price = price
        self.quantity = quantity
        self.transactions = {'buy': [], 'sell': []}
        self.transactions['buy'].append(Transaction(date, price, quantity))

    def buy(self, date, price, quantity):
        self.transactions['buy'].append(Transaction(date, price, quantity))
        self.quantity += quantity

    def sell(self, date, price, quantity):
        if quantity <= self.quantity:
            self.transactions['sell'].append(Transaction(date, price, quantity))
            self.quantity -= quantity
        else:
            raise ValueError("Not enough stocks to sell")
        
    def calculate_average_buy_price(self):
        total_buy_price = sum(t.price * t.quantity for t in self.transactions['buy'])
        total_quantity = sum(t.quantity for t in self.transactions['buy'])
        self.ave_buy_price = total_buy_price / total_quantity
        return total_buy_price / total_quantity

    def calculate_profit_loss(self, current_price):
        total_buy_price = sum(t.price * t.quantity for t in self.transactions['buy'])
        total_sell_price = sum(t.price * t.quantity for t in self.transactions['sell'])
        return (current_price * self.quantity + total_sell_price) - total_buy_price

    def save_to_file(self, filename):
        with open(filename, 'wb') as f:
            pickle.dump(self, f)

    @staticmethod
    def load_from_file(filename):
        with open(filename, 'rb') as f:
            return pickle.load(f)