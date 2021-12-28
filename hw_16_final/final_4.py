# USD,RATE:27.5,AVAILABLE:13500.98
# UAH,RATE:27.3,AVAILABLE:39345.5

class ExchangerCurrency:
    """class ExchangerCurrency"""

    def __init__(self, file_path: str):
        """init class"""
        self.file_path: str = file_path
        self.data: dict = {}

    def read_file(self):
        with open(self.file_path, 'r') as file:
            for i in file.read().splitlines():
                line: list = i.split(',')
                currency: str = line[0]
                self.data[currency] = {'RATE': float(line[1].split(':')[1]), 'AVAILABLE': float(line[2].split(':')[1])}

    def get_currency_info(self, currency: str):
        if currency in self.data.keys():
            return f'RATE {self.data[currency]["RATE"]} AVAILABLE {self.data[currency]["AVAILABLE"]}\n'
        else:
            return f'INVALID CURRENCY {currency}\n'

    def write_file(self):
        with open(self.file_path, 'w') as file:
            for currency in self.data.keys():
                file.write(f'{currency}, RATE:{self.data[currency]["RATE"]}, '
                           f'AVAILABLE:{self.data[currency]["AVAILABLE"]}\n')

    def exchange_currency(self, desired_currency: str, value: float):
        if desired_currency in self.data.keys():
            for currency_in_cash_register in self.data.keys():
                if desired_currency != currency_in_cash_register:
                    if self.data[desired_currency]["RATE"] < self.data[currency_in_cash_register]["RATE"]:
                        rate: float = 1 / self.data[currency_in_cash_register]["RATE"]
                    else:
                        rate: float = self.data[currency_in_cash_register]["RATE"]
                    product: float = value * rate
                    if self.data[currency_in_cash_register]["AVAILABLE"] - product >= 0.0:
                        self.data[currency_in_cash_register]["AVAILABLE"] -= product
                        self.data[desired_currency]["AVAILABLE"] += value
                        return f'{currency_in_cash_register} {product}, RATE {rate}\n'
                    else:
                        return f'UNAVAILABLE, REQUIRED BALANCE {currency_in_cash_register} {product}, ' \
                               f'AVAILABLE {self.data[currency_in_cash_register]["AVAILABLE"]}\n'
        else:
            return f'INVALID CURRENCY {desired_currency}\n'


if __name__ == '__main__':
    exchanger = ExchangerCurrency(r'./data.txt')

    while True:
        input_user_command: str = input(f'COMMAND?\n').upper()
        command: list = input_user_command.split()

        if len(command) == 0:
            print(f'INVALID INPUT\n')
        elif command[0] == 'STOP':
            print(f'SERVICE STOPPED\n')
            exit()
        elif command[0] == 'COURSE':
            try:
                exchanger.read_file()
                print(exchanger.get_currency_info(command[1]))
            except FileNotFoundError:
                print('File of currency not found!')
            except IndexError:
                print(f'INVALID INPUT\n')

        elif command[0] == 'EXCHANGE':
            try:
                exchanger.read_file()
                print(exchanger.exchange_currency(command[1], float(command[2])))
                exchanger.write_file()
            except FileNotFoundError:
                print('File of currency not found!')
            except (IndexError, ValueError):
                print(f'INVALID INPUT\n')
        else:
            print(f'INVALID INPUT\n')
