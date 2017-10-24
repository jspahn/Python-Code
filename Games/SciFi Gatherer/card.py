
class Card:
    ''' Represents a single card in the game: SciFi Gatherer.
    These are the cards that the players will purchase throughout the game.'''
    def __init__(self,level, color, cost, victory_points):
        '''
        level
            - Integer value: 1, 2 or 3
        color
            - String value: "Red", "Blue", "Black", "Green" or "White"
        cost
            - Dictionary value storing the cost of the cards:
                example: {"Red": 4}
                         {"Red": 1, "Blue":1, "Black":1, "Green":1}
        victory_points
            - Integer value representing the number of victory points the card is worth for owning
        '''
        self.level = level
        self.color = color
        self.cost = cost
        self.victory_points = victory_points
