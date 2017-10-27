
# Debug Messages
DEBUG_DEFAULT = "Debug Default Return Statement."


# Game Actions
RESERVE_CARD = "Reserve Card"
PURCHASE_CARD_MARKET = "Purchase Card From the Marketplace"
PURCHASE_CARD_RESERVE = "Purchase Card From Reserve"
TAKE_THREE_COINS = "Take Three Coins"
TAKE_TWO_COINS = "Take Two Coins"
TAKE_BONUS_CARD = "Take Bonus Card"

ERR_000 = "No Error"
ERR_001 = "Cannot Draw Card to marketplace.  Deck at that level is empty"
ERR_002 = "Cannot Draw Card to marketplace.  Marketplace at that level is Full"

# Error 100-199 = Errors pertaining to taking coins from the bank
ERR_101 = "Cannot collect Coin.  Bank does not have enough to give."
ERR_102 = "Cannot collect 2 Coins of that type. There must be at least 4 of that type in the bank"


# Error 200-299 = Errors Pertaining to Purchasing Cards
ERR_201 = "Cannot Purchase Card. Insufficient Funds"
ERR_202 = "Cannot Purchase Card from Market.  Card is not available for purchase."
ERR_203 = "Cannot Purchase Card from Private Reserve. Card is not available for Purchase"
ERR_204 = "Cannot Purchase Card from Private Reserve. Reserve is Empty"


# Error 300-399 = Errors Pertaining to Reserving Cards
ERR_101 = "Cannot Reserve Card. Player's Reserve Hand is full"
ERR_102 = "Cannot Reserve Card. Card is not in Marketplace"