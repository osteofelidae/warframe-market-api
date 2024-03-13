# ███ ITEMS ████████████████████████████████████████████████████████████████████████████████████████████████████████████
# └──▶ This submodule defines WFM's "Items" endpoints.


# ███ DEPENDENCIES █████████████████████████████████████████████████████████████████████████████████████████████████████
import requests
from src.wfm import __WFM_API_BASE_URL__
from src.wfm import exceptions
from src.wfm import classes
from typing import Self


# ███ FUNCTIONS ████████████████████████████████████████████████████████████████████████████████████████████████████████

# ▓▓▓ Get all tradeable items ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓
def get_all_items() -> list[classes.Item]:
    # └──▶ Get an array of all tradeable items.

    # ┌──▶ Make request
    response = requests.get(
        url=__WFM_API_BASE_URL__ + "/items"
    )

    # ┌──▶ 200 OK - successful response,
    if response.status_code == 200:

        items = []  # ───▶ List of items
        items_raw = response.json()["payload"]["items"]  # ───▶ List of item json

        # ┌──▶ Iterate through item json, and create a list of wfm.Item by parsing them.
        for item_raw in items_raw:
            items.append(classes.Item())
            items[-1]._set_attributes(item_raw)

        # ┌──▶ Return parsed list
        return items

    # ┌──▶ Any other status code is an error, so raise an exception
    else:
        raise KeyError(exceptions.API_ERROR + response.text)

