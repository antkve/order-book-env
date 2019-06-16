from numpy import random

class Env:

    def __init__(self, num_agents, dividend_period=30, 
            dividend_mean=0, dividend_var=10):
        self.num_agents = num_agents
        self.sell_ob = [{} for agent in range(num_agents)]
        self.buy_ob = [{} for agent in range(num_agents)]
        self.balance_sheet = [0 for agent in range(num_agents)]
        self.time = 0
        self.dividend_counter = self.dividend_period = dividend_period
        self.dividend_mean = dividend_mean
        self.dividend_var = dividend_var


    def get_min_sell_price(self):
        return min([
            price for price in agent 
            for agent in self.sell_ob 
            if agent[price] != 0])

    def get_max_buy_price(self):
        return max([
            price for price in agent_ob 
            for agent_ob in self.buy_ob 
            if agent_ob[price] != 0])

    def total_amount_selling_at_price(self, price):
        return sum([agent_ob[price] 
            for agent_ob in self.sell_ob 
            if price in agent_ob])

    def total_amount_buying_at_price(self, price):
        return sum([agent[price] 
            for agent_ob in self.buy_ob 
            if price in agent_ob])

    def total_amount_selling(self, agent):
        return sum(self.sell_ob[agent].values())

    def total_amount_buying(self, agent):
        return sum(self.buy_ob[agent].values())

    def make_exchange(self, selling_agent, buying_agent, volume, price):
        if self.stock_
        self.stock_sheet[selling_agent] -= volume

    def make_trade(self, price, volume, buying_agent, selling_agent):
        self.stock_sheet[buying_agent] += volume
        self.stock_sheet[selling_agent] -= volume
        self.balance_sheet[buying_agent] -= price * volume
        self.balance_sheet[selling_agent] += price * volume

    # if buy order is greater than proposed sell order, decrements buy order
    # and returns 0
    # else, erases buy order and returns amount of sell order left unfilled
    def execute_buy_order(self, selling_agent, buying_agent, 
            buy_price, sell_price, volume):
        buying_agent_volume = self.buy_ob[buying_agent][max_price]
        if buying_agent_volume > volume:
            selling_agent_balance = self.balance_book[selling_agent]
            self.make_trade(price, volume, buying_agent, selling_agent)
            self.buy_ob[buying_agent][max_price] -= volume
            return 0, selling_agent_balance - self.balance_book[selling_agent]
        else:
            self.make_trade(price, buying_agent_volume, buying_agent, selling_agent)
            del self.buy_ob[buying_agent][max_price]
            return volume - buying_agent_volume, selling_agent_balance - self.balance_book[selling_agent]

    # if buy order is greater than proposed sell order, decrements buy order
    # and returns 0
    # else, erases buy order and returns amount of sell order left unfilled
    def execute_buy_order(self, selling_agent, buying_agent, 
            buy_price, sell_price, volume):
        buying_agent_volume = self.buy_ob[buying_agent][max_price]
        if buying_agent_volume > volume:
            selling_agent_balance = self.balance_book[selling_agent]
            self.make_trade(price, volume, buying_agent, selling_agent)
            self.buy_ob[buying_agent][max_price] -= volume
            return 0, selling_agent_balance - self.balance_book[selling_agent]
        else:
            self.make_trade(price, buying_agent_volume, buying_agent, selling_agent)
            del self.buy_ob[buying_agent][max_price]
            return volume - buying_agent_volume, selling_agent_balance - self.balance_book[selling_agent]

    # if buy orders exist satisfying the sell order, then
    # it cancels them out until there are no more satisfying it,
    # and puts the rest of the volume up on the sell order book.
    # Returns the amount put up on the order book and the total
    # amount made by the seller on immediate trades.
    
    def place_sell_order(self, asset, volume, price, agent):

        if self.stock_sheet[agent] <= self.total_amount_selling(agent) + volume:
            raise Exception("Agent attempted to place a trade too large")

        orig_volume = volume
        return_amount = 0

        while self.get_max_buy_price() >= price:
            for buying_agent in range(self.num_agents):
                max_price = self.get_max_buy_price()
                if max_price in self.buy_ob[buying_agent]:
                    volume, earnings = self.execute_buy_order(
                            agent, buying_agent, 
                            max_price, price, volume)

        if price in self.sell_ob[agent]:
            self.sell_ob[agent][price] += volume
        else:
            self.sell_ob[agent][price] = volume

        return volume, earnings
            

    def place_buy_order(self, agent, volume, price):

        orig_volume = volume

        while self.get_max_sell_price() >= price:
            for selling_agent in range(self.num_agents):
                max_price = self.get_max_sell_price()
                if max_price in self.sell_ob[selling_agent]:
                    volume = self.execute_sell_order(
                            agent, selling_agent, 
                            max_price, price, volume)

        if price in self.buy_ob[agent]:
            self.buy_ob[agent][price] += volume
        else:
            self.buy_ob[agent][price] = volume

        return volume

    def next_tick(self):
        self.time += 1
        if self.time % self.dividend_period = 0:
            returns = [self.next_dividend * volume 
                    for volume in self.balance_sheet]
            for a in range(self.num_agents):
                self.balance_book[a] += returns[a]
            self.next_dividend = random.normal(
                    loc=self.dividend_mean, 
                    scale=self.dividend_var)

