# ███ CLASSES ██████████████████████████████████████████████████████████████████████████████████████████████████████████
# └──▶ This file defines this module's classes.


# ███ DEPENDENCIES █████████████████████████████████████████████████████████████████████████████████████████████████████
import requests
from src.wfm import __WFM_API_BASE_URL__
from src.wfm import exceptions
from typing import Self


# ███ CLASS DEFINITIONS ████████████████████████████████████████████████████████████████████████████████████████████████

# ▓▓▓ Generic class ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓
class Generic:
    # └──▶ Generic parent class for all other warframe-market-api classes; internal use only

    # ▒▒▒ Constructor ▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒
    def __init__(
            self
    ) -> None:
        # └──▶ Generic constructor encompassing all shared class members.

        self._attributes: dict = {}  # ───▶ Generic attributes
        self._partial: bool = True  # ───▶ Whether generic is partial or not (Partial types may arise, for example,
        #                                  when items are returned in a list)

    # ▒▒▒ Get item ▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒
    def __getitem__(self,
                    attribute: str
                    ):
        # └──▶ Get something from self._attributes

        return self._attributes[attribute]

    # ▒▒▒ Attributes interface ▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒
    def get_attributes(self) -> dict:
        # └──▶ Generic _attributes getter.
        #      Should only be necessary if further postprocessing or a JSON dump is required

        return self._attributes.copy()  # ───▶ Return a copy of _attributes

    def _set_attributes(self,
                        attributes: dict
                        ) -> None:
        # └──▶ Generic _attributes setter.
        #      Should not be necessary at all except for internal use.

        # ┌──▶ Set _attributes to the given attributes
        self._attributes = attributes.copy()

    def _update_attributes(self,
                           attributes: dict
                           ) -> None:
        # └──▶ Update _attributes according to the following:
        #      1. If a new attribute is set, set it.
        #      2. If an existing attribute is set, update it.
        #      3. Any unset existing attributes will remain.

        # ┌──▶ Update _attributes with the given
        self._attributes.update(attributes)


# ▓▓▓ User class ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓
class User(Generic):
    # └──▶ User class for use with authenticated functions.
    #      Should typically be instantiated through wfm.auth.sign_in()
    pass  # TODO finish


# ▓▓▓ Item class ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓
class Item(Generic):
    # └──▶ Game item class

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
                raise Exception(exceptions.API_ERROR + response.text)

        # ┌──▶ If _attributes is improperly set, raise an exception
        else:
            raise KeyError(exceptions.ITEM_INCORRECTLY_INITIALIZED_ERROR)

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
            raise KeyError(exceptions.ITEM_IS_PARTIAL_ERROR)

