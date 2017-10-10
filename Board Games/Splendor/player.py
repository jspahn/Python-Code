
class Player:
    """A Player designed for the Game: Splendor"""
    def __init__(self, name):
        self.name = name
        self.victory_points = 0
        self.tableau = []
        self.discounts = {"Red"  :0,
                          "Blue" :0,
                          "Green":0,
                          "White":0,
                          "Black":0}
        # The Gems they can spend
        self.purse =     {"Red"  : 0,
                          "Blue" : 0,
                          "Green": 0,
                          "White": 0,
                          "Black": 0,
                          "Yellow":0}
        self.reserve = []
        self.nobles = []

    def recalculateScore(self):
        """Looks through cards purchased and Nobles Gained to recalculate the player's score.
            self.victory_points is updated"""
        self.victory_points = 0
        for tab_card in self.tableau:
            self.victory_points += tab_card.victoryPoints
        for tab_noble in self.nobles:
            self.victory_points += tab_noble.victoryPoints




    pass


'''    Player
        - ID
        - Victory Points
        - Reserve Cards
        - # of each color of chips
               6 Colors - Red (Ruby)
                          White (Diamond)
                          Blue (Sapphire)
                          Green (Emerald)
                          Black
                          Yellow (Gold)
        - Tableau Cards
        - Discounts for each Color

    Player Actions
        - Draw 2 chips of 1 type
        - Draw 3 chips of 3 different types
        - Purchase a Card from board
        - Purchase a Card from Reserve
        - Reserve a Card (and get a gold)

        - Claim a Noble
        - Discard Chips (down to 10)
        - Check for end of Game Condition (15VP)
'''
