# ███ ITEMS ████████████████████████████████████████████████████████████████████████████████████████████████████████████
# └──▶ This submodule defines WFM's "Items" endpoints.


# ███ DEPENDENCIES █████████████████████████████████████████████████████████████████████████████████████████████████████
import requests
from src.wfm import __WFM_API_BASE_URL__, Generic, exceptions
from typing import Self


# ███ CLASSES ██████████████████████████████████████████████████████████████████████████████████████████████████████████

# ▓▓▓ Item class ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓
class Item(Generic):
    # └──▶ Game item class

    # ▒▒▒ Constructor ▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒
    def __init__(self,
                 url_name=None
                 ):

        # ┌──▶ Initialize super
        super().__init__()

        # ┌──▶ Set url name
        self._attributes["url_name"] = url_name

    # ▒▒▒ Data methods ▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒
    def update(self) -> Self:
        # └──▶ Update or turn partial to full

        # ┌──▶ Fetch url_name, or None if unset.
        url_name = self._attributes.get("url_name")

        # ┌──▶ If url_name is set
        if url_name is not None:

            # ┌──▶ Request full item info
            response = requests.get(
                url=__WFM_API_BASE_URL__+"/items/"+url_name,
            )

            # ┌──▶ 200 OK - item found; set all attributes, set non-partial
            if response.status_code == 200:
                item_set_data = response.json()["payload"]["item"]["items_in_set"]

                # ┌──▶ Extract item data
                item_data = [d for d in item_set_data if d["url_name"] == url_name]

                # ┌──▶ If not found, it could be because the API returned the blueprint, so check that
                if len(item_data) == 0:
                    item_data = [d for d in item_set_data if d["url_name"] == url_name+"_blueprint"]

                    # ┌──▶ If successful, update self._attributes["url_name"] as well
                    if len(item_data) != 0:
                        self._update_attributes({"url_name": url_name+"_blueprint"})

                # ┌──▶ Update attributes with fetched data
                self._update_attributes({"item": item_data[0]})
                self._update_attributes({"items_in_set": item_set_data})

                # ┌──▶ Object is now complete; return self for chaining methods
                self._partial = False
                return self

            # ┌──▶ Any other status code is an error, so raise an exception
            else:
                raise exceptions.ApiException(exceptions.API_ERROR + response.text)

        # ┌──▶ If _attributes is improperly set, raise an exception
        else:
            raise exceptions.ItemException(exceptions.ITEM_INCORRECTLY_INITIALIZED_ERROR)

    def get_item_data(self) -> dict:
        # └──▶ Get item data

        item_data = self._attributes.get("item")

        # ┌──▶ Return if correctly set
        if item_data is not None:
            return item_data

        # ┌──▶ Raise exception if incorrectly set
        else:
            raise KeyError(exceptions.ITEM_IS_PARTIAL_ERROR)

    def get_set_data(self) -> list:
        # └──▶ Get item data, accounting for sets

        # ┌──▶ Fetch items in set
        item_set_data = self._attributes.get("items_in_set")

        # ┌──▶ If item_set_data is set
        if item_set_data is not None:
            return item_set_data

        # ┌──▶ If item_set_data is not set
        else:
            raise exceptions.ItemException(exceptions.ITEM_IS_PARTIAL_ERROR)

    # ▒▒▒ Item-related methods ▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒
    def get_orders(self):

        # ┌──▶ Fetch url_name, or None if unset.
        url_name = self._attributes.get("url_name")

        # ┌──▶ If url_name is set
        if url_name is not None:

            endpoint = ""

            # ┌──▶ Get orders
            response = requests.get(
                url=__WFM_API_BASE_URL__ + "/items/" + url_name + "/orders"
            )

            # ┌──▶ 200 OK - orders retrieved
            if response.status_code == 200:

                # ┌──▶ Extract orders from payload
                orders_raw = response.json()["payload"]["orders"]

                orders = []  # ───▶ List of order objects

                # ┌──▶ Encapsulate orders from order objects
                for order_raw in orders_raw:
                    order = Order()
                    order._set_attributes(order_raw)
                    orders.append(order)

                # ┌──▶ Return orders
                return orders

            # ┌──▶ Any other status code is an error, so raise an exception
            else:
                raise exceptions.ApiException(exceptions.API_ERROR + response.text)

        # ┌──▶ If _attributes is improperly set, raise an exception
        else:
            raise exceptions.ItemException(exceptions.ITEM_INCORRECTLY_INITIALIZED_ERROR)


# ▓▓▓ Order class ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓
class Order(Generic):
    # └──▶ Game order class
    pass


# ███ FUNCTIONS ████████████████████████████████████████████████████████████████████████████████████████████████████████

# ▓▓▓ Get all tradeable items ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓
def get_all_items() -> list[Item]:
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
            items.append(Item())
            items[-1]._set_attributes(item_raw)

        # ┌──▶ Return parsed list
        return items

    # ┌──▶ Any other status code is an error, so raise an exception
    else:
        raise KeyError(exceptions.API_ERROR + response.text)

