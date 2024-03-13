# ███ EXCEPTIONS ███████████████████████████████████████████████████████████████████████████████████████████████████████
# └──▶ This file defines this module's exceptions.


# ███ CONSTANTS ████████████████████████████████████████████████████████████████████████████████████████████████████████

# ▓▓▓ Generic ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓
# ┌──▶ Error messages
API_ERROR = "The following API error occurred: "

# ▓▓▓ Items ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓
ITEM_INCORRECTLY_INITIALIZED_ERROR = ("Item is incorrectly initialized. If this class was most recently created or "
                                      "initialized by a warframe-market-api function or method, please open an issue "
                                      "on GitHub.")
ITEM_NOT_FOUND_ERROR = ("Requested item was not found. No matching url_name was found. If this class was most recently"
                        " initialized by a warframe-market-api function or method, please open an issue on GitHub.")
ITEM_IS_PARTIAL_ERROR = "This item appears to only be partially initialized. Please run <Item>.update() to fix this."


# ███ EXCEPTIONS ███████████████████████████████████████████████████████████████████████████████████████████████████████
class ApiException(Exception):
    pass


class ItemException(Exception):
    pass
