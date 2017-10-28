import pygame
import time
import random
import csv
import player
import globals

pygame.init()

display_width = 800
display_height = 600

# Colors:
black = (0,0,0)
blue = (0,0,255)
green = (0,255,0)
white = (255,255,255)
red = (255,0,0)

# Game Globals
CARDS_PER_MARKETPLACE_ROW = 4
b_DEBUG = True

# Game State
num_players = 2
card_catalog = {}   # Used to hold all information regarding the playing cards
bonus_catalog = {}  # Used to hold all information regarding bonus point cards
card_decks = {}     # Cards decks based on their level (in base: 3 levels)
bonus_options = []
coin_bank = {
    "Dark Matter" :0,
    "Water" :0,
    "Green" :0,
    "Antimatter" :0,
    "White" :0
}
marketplace = {}

player_list = []

gameDisplay = pygame.display.set_mode((display_width,display_height))
pygame.display.set_caption("Race Game")
clock = pygame.time.Clock()


# --------------------------------------------------------------
# Debug
# --------------------------------------------------------------
def d_print(message):
    """Debug print message"""
    if b_DEBUG:
        print("Debug Message: {}".format(message))


# --------------------------------------------------------------
# Game Setup
# --------------------------------------------------------------
def setup_load_card_catalogs():
    # Create Card Catalog of all cards in game
    with open('cards.csv') as card_csv_file:
        reader = csv.reader(card_csv_file)
        card_counter = [0, 0, 0]
        for row in reader:
            if len(row) == 8:
                card_counter[int(row[0]) - 1] += 1
                card = {
                    "name": "no_name_given",
                    "type": row[1],
                    "level": row[0],
                    "vp": row[2],
                    "cost": {
                        str(row[3].split(" Cost:")[0]): row[3].split(" Cost:")[1],
                        str(row[4].split(" Cost:")[0]): row[4].split(" Cost:")[1],
                        str(row[5].split(" Cost:")[0]): row[5].split(" Cost:")[1],
                        str(row[6].split(" Cost:")[0]): row[6].split(" Cost:")[1],
                        str(row[7].split(" Cost:")[0]): row[7].split(" Cost:")[1]
                    }
                }
                card_catalog[int(row[0]) * 1000 + card_counter[int(row[0]) - 1]] = card
    card_csv_file.close()

    # Create Bonus Point Catalog
    with open('bonus.csv') as bonus_csv_file:
        reader = csv.reader(bonus_csv_file)
        bonus_id = -1
        for row in reader:
            bonus_id += 1
            if bonus_id != 0:
                bonus = {
                    "id": id,
                    "name": row[0],
                    "vp": row[1],
                    "cost": {
                        str(row[2].split(" Cost:")[0]): row[2].split(" Cost:")[1],
                        str(row[3].split(" Cost:")[0]): row[3].split(" Cost:")[1],
                        str(row[4].split(" Cost:")[0]): row[4].split(" Cost:")[1],
                        str(row[5].split(" Cost:")[0]): row[5].split(" Cost:")[1],
                        str(row[6].split(" Cost:")[0]): row[6].split(" Cost:")[1]
                    }
                }
                bonus_catalog[bonus_id] = bonus
    bonus_csv_file.close()


def setup_build_decks():
    # Create the card Decks based on card level
    for id in card_catalog.keys():
        if int(id) // 1000 in card_decks:
            card_decks[int(id) // 1000].append(id)
        else:
            card_decks[int(id) // 1000] = []
            card_decks[int(id) // 1000].append(id)
    for level in card_decks.keys():
        random.shuffle(card_decks[level])

    # Select bonus cards
    bonus_options.extend(random.sample(list(bonus_catalog), num_players + 1))


def setup_coin_bank():
    # Set up the coin bank
    if num_players == 2:
        start_coin = 4
    if num_players == 3:
        start_coin = 5
    if num_players == 4:
        start_coin = 7
    coin_bank["Dark Matter"] = start_coin
    coin_bank["Water"] = start_coin
    coin_bank["Green"] = start_coin
    coin_bank["Antimatter"] = start_coin
    coin_bank["White"] = 5


def setup_player_creation():
    global player_list

    player_list.extend([
        player.Player("Player 1"),
        player.Player("Player 2")])
    if num_players >2:
        player_list.append(player.Player("Player 3"))
    if num_players >3:
        player_list.append(player.Player("Player 4"))


def setup_marketplace():
    for level in card_decks:
        marketplace[level] = [None] * CARDS_PER_MARKETPLACE_ROW
        for _ in range(CARDS_PER_MARKETPLACE_ROW):
            draw_card_to_marketplace(level)


def game_setup(n_players = 2):
    """Main Game Setup Function. Calls all other Setup Functions"""
    global num_players
    num_players = n_players

    # Game Setup Functions
    setup_load_card_catalogs()
    setup_build_decks()
    setup_coin_bank()
    setup_player_creation()
    setup_marketplace()


# --------------------------------------------------------------
# Game Mechanics
# --------------------------------------------------------------
def draw_card_to_marketplace(level):
    # Check if draw deck is empty
    if len(card_decks[level]) == 0:
        d_print(globals.ERR_001)
        return globals.ERR_001
    # Check if marketplace has space
    for card_space in marketplace[level]:
        if card_space is None:
            marketplace[level][marketplace[level].index(None)] = card_decks[level].pop()
            return globals.ERR_000

    else:
        d_print(globals.ERR_002)
        return globals.ERR_002


def is_in_marketplace(id):
    """Checks to see if the card is available for purchase."""
    for level in marketplace:
        return any(card_id == id for card_id in marketplace[level])


# --------------------------------------------------------------
# Text Display
# --------------------------------------------------------------
def text_display_marketplace():
    horizontal_card_spacing = "    "
    market_display = {}

    print("Marketplace:")
    for level in marketplace:
        print(marketplace[level])

    level_print_order = list(marketplace.keys())
    level_print_order.reverse()

    for level in level_print_order:
        for card_id in marketplace[level]:
            card_display = text_display_card(card_id)
            for line in card_display:
                market_line = (level-1)*len(card_display) + line
                if market_line in market_display:
                    market_display[market_line] += horizontal_card_spacing + card_display[line]
                else:
                    market_display[market_line] = card_display[line]

    print(market_display)
    s_market_display = ""
    for full_line in market_display:
        s_market_display += market_display[full_line] + "\n"

    return s_market_display




def text_display_card(id):
    """Text based Display of the card"""
    text = {}
    text[0] = "+----------------+"
    text[1] = "| {0}VP      {1} |".format(card_catalog[id]["vp"], card_catalog[id]["type"][:5])
    text[2] = "|                |"
    text[3] = "|          lvl {} |".format(card_catalog[id]["level"])
    text[4] = "|   COST         |"
    text[5] = "| {} Dark Matter  |".format(card_catalog[id]["cost"]["Dark Matter"])
    text[6] = "| {} Water        |".format(card_catalog[id]["cost"]["Water"])
    text[7] = "| {} Green        |".format(card_catalog[id]["cost"]["Green"])
    text[8] = "| {} Anti Matter  |".format(card_catalog[id]["cost"]["Antimatter"])
    text[9] = "| {} White        |".format(card_catalog[id]["cost"]["White"])
    text[10] ="|         id{} |".format(id)
    text[11] = "+----------------+"
    return text

# --------------------------------------------------------------
# Game Loop
# --------------------------------------------------------------
def game_loop():
    b_game_end = False
    while b_game_end == False:
        # Every player gets equal number of turns
        for agent in player_list:
            err_message = globals.ERR_000
            b_action_complete = False
            # Player makes a decision, game_loop checks if decision is valid, if not, requests new decision.
            while b_action_complete == False:
                b_action_complete = True
                action = agent.perform_main_action(err_message)

                if action["message"] == globals.PURCHASE_CARD_MARKET:
                    if is_in_marketplace:
                        pass
                    pass

                if action["message"] == globals.RESERVE_CARD:
                    agent.reserve.append(action["card_id"])

                if action["message"] == globals.PURCHASE_CARD_RESERVE:
                    pass

        b_game_end = True

    # Player performs main action
    #       Purchase Card from Marketplace
    #       Reserve Card
    #       Purchase Card from Reserve
    #       Collect 3 unique coin
    #       Collect 2 same coin
    # Player may claim bonus card
    # Victory Check
    # Coin check
    # Reset Marketplace
    # next Player

    pass



game_setup(3)
print("Number of Players: {}".format(num_players))
print(text_display_marketplace())


print(coin_bank)
game_loop()
pygame.quit()
quit()
