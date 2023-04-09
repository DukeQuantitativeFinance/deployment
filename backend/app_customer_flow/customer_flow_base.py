import random
import numpy as np
import importlib

class Market:
    def __init__(self, mean, stdev):
        self.mean = mean
        self.stdev = stdev

    def generateMarket(self):
        market = []
        for i in range(10):
            trade = [random.choice(["buy","sell"]),round(np.random.normal(self.mean,self.stdev))]
            market.append(trade)
        return market

class Trader(): 
    def __init__(self) -> None:
        pass
    def getTrades(self, market, player_position, time):
        trades = ""
        for trade in market:
            trades += "1"

        return trades

class Game():

    def __init__(self, market_mean = 100, market_stdev = 10, player_balance = 100, position_punishment = 5):
        self.Player = None
        self.market_mean = market_mean
        self.market_stdev = market_stdev
        self.player_balance = player_balance
        self.position_punishment = position_punishment
        self.player_position = [0] * 10
        
    def import_individual_trader(self, filename):
        print("filename:", filename)
        module_name = filename[:-3]
        print("module name: ", module_name)
        # module = importlib.import_module(f'{os.path.dirname(__file__)}.backend.{dirname}.{module_name}')
        module = importlib.import_module(f'.{module_name}', package=__package__)
        
        class_name = 'Trader'
        trader_class = getattr(module, class_name)
        
        # trader_instance = trader_class(id)
        # print("created trader instance")
        # self.traders.append(trader_instance)
        # self.id_to_trader[id] = trader_instance
        self.Player = trader_class()
        print("trader class imported successfully")      

    def getMarket(self):
        market = Market(self.market_mean, self.market_stdev).generateMarket()
        return market
        
    def runGame(self):
        # for each timestamp, generate random market of 10 trades with bid asks with value gain between -1 and 1
        # 1 player determines if they want to buy or sell
        # keep player's position and balance
        # incentivize player based on order fulfillment rate and punish player's position every x time stamps
        
        incentive = 0
        for t in range(10):
            self.market = self.getMarket()
            decisions = self.Player.getTrades(self.market, self.player_position, t)
            for i in range(len(decisions)):
                if decisions[i] not in ["0","1"] or len(decisions) != 10:
                    print("Invalid input")
                    return
                    
                if decisions[i] == "1":
                    if(self.market[i][0] == "buy"): 
                        self.player_position[i] += 1
                        self.player_balance -= self.market[i][1]
                        incentive += self.market[i][1]
                    else:
                        self.player_position[i] -= 1
                        self.player_balance += self.market[i][1]
                        incentive -= self.market[i][1]

            # Incentive for order fullfilment rate, applied every time step
            order_fulfillment_rate = 0
            if self.player_balance != 0:
                order_fulfillment_rate = incentive / self.player_balance
            incentive = 2 * order_fulfillment_rate
            self.player_balance += incentive

            # Penalty for deviation from avg pos, applied every 3 time steps
            if t % 3 == 0:
                avg_pos = 0
                deviation = sum(abs(p - avg_pos) for p in self.player_position) / len(self.player_position)
                penalty = deviation * 0.005
                self.player_position = [p - penalty for p in self.player_position]


        self.player_balance -= sum([abs(p) for p in self.player_position]) * self.position_punishment
        print("Player position: ", self.player_position)
        print("Player balance: ", self.player_balance)
        print("Player net worth: ", self.player_balance + sum(p * self.market_mean for p in self.player_position))
        print()
   

if __name__ == "__main__":
    market_mean = 100
    market_stdev = 10
    g = Game(market_mean, market_stdev)
    g.runGame()