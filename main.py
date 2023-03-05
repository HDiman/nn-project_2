import random
import math
import time
import os

def clear():
    os.system("clear")


start_capital = 100000.00
each_month_add = 10000.00
stock_price = 100.0 # stock start price
bond_price = 1000.0 # bond start price
volatility = 0.2 # волатильность акции (стандартное отклонение ежемесячных процентных изменений цены)
time_horizon = 120 # количество дней наблюдения



print(f"У вас на счету: {start_capital} рублей")
print(f"Цена акции: {stock_price}")
print(f"Цена облигации: {bond_price}")
stock_num = int(input("Сколько акций купить? "))
bond_num = int(input("Сколько облигаций купить? "))

# Market Prices
for month in range(time_horizon):

    # Цена акции
    monthly_return = math.exp(random.gauss(0.0, volatility)) - 1.0
    stock_price *= 1.0 + monthly_return
    # Форс Мажор происходит раз в 3 года
    force_majeure = random.randint(1, 36)
    if force_majeure == 18:
        print("Падение -50%")
        stock_price = stock_price / 2
    stock_price = round(stock_price, 2)

    # Цена облигации вместе с процентами
    bond_price = round((bond_price + bond_price * 0.0058), 2)

    # Блок оценки стоимости портфеля
    stock_case = round((stock_price * stock_num), 2)
    bond_case = round((bond_price * bond_num), 2)

    # Блок вывода информации портфеля
    print(f"Month: {month+1}")
    print(f"Stock: {stock_case}")
    print(f"Bond: {bond_case}")
    time.sleep(3)
    clear()




