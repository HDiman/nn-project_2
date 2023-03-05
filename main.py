import random
import math
import time
import os

def clear():
    os.system("clear")


start_capital = 100000.00
from_salary = 10000.00
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
    force_majeure = random.randint(1, 48)
    if force_majeure == 24:
        print("Падение -50%")
        stock_price = stock_price / 2
    elif force_majeure == 12 or force_majeure == 48:
        print("Рост +100%")
        stock_price = stock_price * 2
    stock_price = round(stock_price, 2)


    # Цена облигации вместе с процентами
    bond_price = round((bond_price + bond_price * 0.0058), 2)

    # Блок оценки стоимости портфеля
    stock_case = round((stock_price * stock_num), 2)
    bond_case = round((bond_price * bond_num), 2)
    personal_case = round((stock_case + bond_case), 2)
    stock_interest = round(stock_case / (personal_case / 100))
    bond_interest = 100 - stock_interest

    # Блок вывода информации портфеля
    print(f"Месяц: {month+1}")
    print("")
    print(f"Цена акции: {stock_price}")
    print(f"У вас: {stock_num} акций")
    print(f"Капитал в акциях: {stock_case} руб.")
    print(f"Капитал в акциях: {stock_interest} %")
    print("")
    print(f"У вас: {bond_num} облигаций")
    print(f"Капитал в облигациях: {bond_case} руб.")
    print(f"Капитал в облигациях: {bond_interest} %")
    print("")
    print(f"Всего у вас: {personal_case} руб.")

    # Блок уравнивания
    answer = int(input("Уравнять 50% на 50% (Да - 1, Нет - 0): "))
    if answer == 1:
        first_part = round(personal_case) / 2
        second_part = round(personal_case) - first_part
        stock_num = round(first_part / stock_price)
        bond_price = 1000
        bond_num = round(second_part / bond_price)

    # time.sleep(3)

    clear()




