import random
import math
import time

price = 100.0 # начальная цена акции
volatility = 0.2 # волатильность акции (стандартное отклонение ежемесячных процентных изменений цены)
time_horizon = 120 # количество дней наблюдения

for month in range(time_horizon):
    monthly_return = math.exp(random.gauss(0.0, volatility)) - 1.0
    price *= 1.0 + monthly_return

    force_majeure = random.randint(1, 24)
    if force_majeure == 12:
        price = price / 2

    price = round(price, 2)

    print(force_majeure)
    print(f"Month {month+1}: {price}")
    time.sleep(2)


