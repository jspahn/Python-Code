"""
The Scythe board is a 2-d board of hexagonal locations

"""

HB_Green  = "Home Base - Green"
HB_Blue   = "Home Base - Blue"
HB_White  = "Home Base - White"
HB_Red    = "Home Base - Red"
HB_Black  = "Home Base - Black"
HB_Yellow = "Home Base - Yellow"
HB_Purple = "Home Base - Purple"

LAKE = "Lake"
FACTORY = "Factory"
FARM = "Farm"
FOREST = "Forest"
MOUNTAIN = "Mountain"
TUNDRA = "Tundra"
VILLAGE = "Village"

"""
map = [
    [HB_Green,   None,     None, HB_Blue,     None,      None,     None,     None,   None,      None],
    [MOUNTAIN,   FARM,  VILLAGE,  FOREST,   TUNDRA,   VILLAGE,     None,     None,   None,      None],
    [    LAKE, TUNDRA,     LAKE,  TUNDRA, MOUNTAIN,      FARM,     FARM,     None,   None,      None],
    [HB_White, FOREST, MOUNTAIN,  FOREST,     LAKE,    FOREST,  VILLAGE,   HB_Red,   None,      None],
    [    None,   FARM,  VILLAGE,    LAKE,  FACTORY,  MOUNTAIN,   TUNDRA, MOUNTAIN,   None,      None],
    [    None, FOREST,   FOREST,    FARM,   TUNDRA,      LAKE,  VILLAGE,     LAKE,   None,      None],
    [    None,   None, MOUNTAIN, VILLAGE,  VILLAGE,    TUNDRA,   FOREST, MOUNTAIN, TUNDRA,      None],
    [    None,   None, HB_Black,  TUNDRA,     LAKE,      FARM, MOUNTAIN,  VILLAGE,   FARM, HB_Purple],
    [    None,   None,     None,    None,     None, HB_Yellow,  VILLAGE,     None,   None,      None]
]
"""
map = [
    [HB_Green,  MOUNTAIN,     LAKE,  HB_White,     None,    None,     None,      None,      None],
    [None,          FARM,   TUNDRA,    FOREST,     FARM,  FOREST,     None,      None,      None],
    [None,       VILLAGE,     LAKE,  MOUNTAIN,  VILLAGE,  FOREST, MOUNTAIN,  HB_Black,      None],
    [HB_Blue,     FOREST,   TUNDRA,    FOREST,     LAKE,    FARM,  VILLAGE,    TUNDRA,      None],
    [None,        TUNDRA, MOUNTAIN,      LAKE,  FACTORY,  TUNDRA,  VILLAGE,      LAKE,      None],
    [None,       VILLAGE,     FARM,    FOREST, MOUNTAIN,    LAKE,   TUNDRA,      FARM, HB_Yellow],
    [None,          None,     FARM,   VILLAGE,   TUNDRA, VILLAGE,   FOREST,  MOUNTAIN,   VILLAGE],
    [None,          None,     None,    HB_Red, MOUNTAIN,    LAKE, MOUNTAIN,   VILLAGE,      None],
    [None,          None,     None,      None,     None,    None,   TUNDRA,      FARM,      None],
    [None,          None,     None,      None,     None,    None,     None, HB_Purple,      None]
]


rivers = [
    [None, None, None, None, None, None, None, None, None],
    [None, None, None, None, None, None, None, None, None],
    [None, None, None, None, None, None, None, None, None],
    [None, None, None, None, None, None, None, None, None],
    [None, None, None, None, None, None, None, None, None],
    [None, None, None, None, None, None, None, None, None],
    [None, None, None, None, None, None, None, None, None],
    [None, None, None, None, None, None, None, None, None],
    [None, None, None, None, None, None, None, None, None],
    [None, None, None, None, None, None, None, None, None]
]

rivers[2][1] = [2,3]
rivers[3][1] = [4,5]
rivers[4][1] = [2,3]
rivers[5][1] = [5]

rivers[1][2] = [4]
rivers[3][2] = [1,2,6]
rivers[4][2] = [2,3,5]
rivers[5][2] = [3,5,6]
rivers[6][2] = [3,4]

rivers[1][3] = [1,2]
rivers[2][3] = [4,5]
rivers[5][3] = [2,3,6]
rivers[6][3] = [1,5,6]

rivers[1][4] = [3,4]
rivers[2][4] = [1,3,4]
rivers[5][4] = [2]
rivers[6][4] = [4,5,6]

rivers[1][5] = [1,3]
rivers[2][5] = [1,3,4,6]
rivers[3][5] = [4,6]
rivers[6][5] = []

rivers[1][6] = []

rivers[5][7] = [1,6]
rivers[6][7] = [1,2,6]
rivers[7][7] = [5]

class hex():
    def __init__(self):
        self.encounter = False
        self.tunnel = False
        pass

    def add_encounter(self):
        self.encounter = True



    hex_type = ""

    """
    What does this have to keep track of?
    What type of hex is it?  -
            Null - is not part of the playing area
            Home Base - Where the character starts for each faction. Players cannot move there unless they are retreating
            Farm     - Food
            Forest   - Wood
            Mountain - Metal
            Tundra   - Oil
            Village  - Workers
            Factory  - Center of Board (counts as 3 hexes)
            Lake
    Encounter?
            True False
    Tunnel?
            True False
    Rivers?
            starting at 1:00 position and going clockwise
            [True, False, False, False, False, True]
    Are there resourses on it?
            {"oil" : 0, "metal" : 0, "wood" : 0, "food" : 0 }
    Is there a Structure on it?
            mine, armory, monument, mill
            () = No
            ("red"  , "mine")
    Are there Units on there?
            [] = No
            [{"color" : "red", "worker" : 0, "mech" : 1, "character" : 1, "airship" : 0}]
            [ {red ....} , {blue...}] to indicate when 2 or more people are in the same location
    Who controls the region?
            Are there units on there?      - No? Look for Structure
               - Yes? Of Multiple Colors?  - Only 1 color? Found Solution       
               - Multiple - Ignore Airships.  If still disputed, combat needs to occur, or a rule was broken.
            
    """

test = [hex(),hex()]
print(test)

print(map[0][0], map[1][0], map[2][0])

print(map)