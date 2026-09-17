"""Module to collect colours objects in order to print coloured logger messages.

Examples
--------
print(Colours.RED + "This message will appear in red." + Colours.ENDC)
"""


class Colour:
    RED = "\033[31m"
    GREEN = "\033[32m"
    YELLOW = "\033[33m"
    BLUE = "\033[34m"

    ENDC = "\033[m"
