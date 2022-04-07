############
# Part 1   #
############


class MelonType:
    """A species of melon at a melon farm."""

    def __init__(self, code, name, first_harvest, color, is_seedless, is_bestseller):
        """Initialize a melon."""
        self.code = code
        self.first_harvest = first_harvest
        self.color = color
        self.is_seedless = is_seedless
        self.is_bestseller = is_bestseller
        self.name = name

        self.pairings = []


    def add_pairing(self, pairing):
        """Add a food pairing to the instance's pairings list."""

        self.pairings.append(pairing)

    def update_code(self, new_code):
        """Replace the reporting code with the new_code."""
        self.code = new_code


def make_melon_types():
    """Returns a list of current melon types."""

    all_melon_types = []
    musk = MelonType("musk", "Muskmelon", 1998, "green", True, True)
    musk.add_pairing("Mint")
    casaba = MelonType("cas", "Casaba", 2003, "orange", False, False)
    casaba.add_pairing("Strawberries")
    casaba.add_pairing("Mint")
    crenshaw = MelonType("cren", "Crenshaw", 1996, "green", False, False)
    crenshaw.add_pairing("Prosciutto")
    yw = MelonType("yw", "Yellow Watermelon", 2013, "yellow", False, True)
    yw.add_pairing("Ice Cream")

    all_melon_types.append(musk)
    all_melon_types.append(casaba)
    all_melon_types.append(crenshaw)
    all_melon_types.append(yw)
    

    return all_melon_types


def print_pairing_info(melon_types):
    """Prints information about each melon type's pairings."""

    for melon in melon_types:
        print (f"\n{melon.name} pairs with")
        for pairing in melon.pairings:
            print (f" - {pairing}")


def make_melon_type_lookup(melon_types):
    """Takes a list of MelonTypes and returns a dictionary of melon type by code."""
    all_melons = {}

    for melon in melon_types:
        all_melons[melon.code] = melon

    return all_melons



############
# Part 2   #
############


class Melon:
    """A melon in a melon harvest."""

    def __init__(self, type, shape_rating, color_rating, from_field, harvested_by):
        self.type = type
        self.shape_rating = shape_rating
        self.color_rating = color_rating
        self.from_field = from_field
        self.harvested_by = harvested_by

    def is_sellable(self):
        return (self.shape_rating > 5 and self.color_rating > 5 and self.from_field != 3)

def make_melons(melon_dict):
    """Returns a list of Melon objects."""

    melons = []

    melons.append(Melon(melon_dict['yw'], 8, 7, 2, 'Sheila'))
    melons.append(Melon(melon_dict['yw'], 3, 4, 2, 'Sheila'))
    melons.append(Melon(melon_dict['yw'], 9, 8, 3, 'Sheila'))
    melons.append(Melon(melon_dict['cas'], 10, 6, 35, 'Sheila'))
    melons.append(Melon(melon_dict['cren'], 8, 9, 35, 'Michael'))
    melons.append(Melon(melon_dict['cren'], 8, 2, 35, 'Michael'))
    melons.append(Melon(melon_dict['cren'], 2, 3, 4, 'Michael'))
    melons.append(Melon(melon_dict['musk'], 6, 7, 4, 'Michael'))
    melons.append(Melon(melon_dict['yw'], 7, 10, 3, 'Sheila'))

    return melons



def get_sellability_report(melons):
    """Given a list of melon object, prints whether each one is sellable."""

    for melon in melons:
        print (f"Harvested by {melon.harvested_by} from Field {melon.from_field} {'CAN BE SOLD' if melon.is_sellable() else 'NOT SELLABLE'}")



#  ****** Driver code ********

melon_types = make_melon_types()
print_pairing_info(melon_types)
melon_dict = make_melon_type_lookup(melon_types)
melon_harvest = make_melons(melon_dict)
get_sellability_report(melon_harvest)

