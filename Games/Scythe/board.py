"""
The Scythe board is a 2-d board of hexagonal locations

"""

LAKE = "Lake"



class hex():
    def __init__(self):
        pass


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