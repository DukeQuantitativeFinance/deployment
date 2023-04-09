class Trader(): 
    def __init__(self) -> None:
        pass
    def getTrades(self, market, player_position, time):
        trades = ""
        for trade in market:
            trades += "1"

        return trades