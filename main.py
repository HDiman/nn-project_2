import random
import math
import time


stock_price = 100.0 # stock start price
bond_price = 1000.0 # bond start price
volatility = 0.2 # волатильность акции (стандартное отклонение ежемесячных процентных изменений цены)
time_horizon = 120 # количество дней наблюдения

# Market Prices
for month in range(time_horizon):

    # Stock Market
    monthly_return = math.exp(random.gauss(0.0, volatility)) - 1.0
    stock_price *= 1.0 + monthly_return
    # Force Majeure in Stock Market Happens Once in 2 years
    force_majeure = random.randint(1, 36)
    if force_majeure == 18:
        print("Crash -50%")
        stock_price = stock_price / 2
    stock_price = round(stock_price, 2)

    # Bond Market
    bond_price = round((bond_price + bond_price * 0.0058), 2)

    print(f"Month: {month+1}")
    print(f"Stock: {stock_price}")
    print(f"Bond: {bond_price}")
    time.sleep(2)


