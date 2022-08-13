# Purpose: Advise Day Traders
# Author: Xiaofeng Paul Lin

import time
from config import spread, daily_average, daily_high, daily_low, weekly_average


class Advisor:
    def __init__(self):
        start_time = time()
        while time() - start_time < 3600000:
            previous_price, current_price = current_price, float(
                input("Current Price: "))
            delta = previous_price - current_price
            advice = self.eval(delta, current_price)
            print(advice)

    def eval(self, delta, price):
        if price < daily_low + spread * price and delta > 0 and price < daily_average < weekly_average:
            return "BUY"
        elif price > daily_high - spread * price and delta < 0:
            return "SELL"
        else:
            return "HOLD"
