# ███ DEPENDENCIES █████████████████████████████████████████████████████████████████████████████████████████████████████
import requests
from src.wfm import __WFM_API_BASE_URL__


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

    def fetch(self) -> None:
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
                self._attributes = response.json()["payload"]["item"]
                self._partial = False

            # ┌──▶ Any other status code is an error, so raise an exception
            else:
                raise KeyError("Requested item was not found. No matching url_name was found. If this class was most "
                               "recently created or initialized by a warframe-market-api function or method, please "
                               "open an issue on GitHub.")

        # ┌──▶ If _attributes is improperly set, raise an exception
        else:
            raise KeyError("Item is incorrectly initialized. If this class was most recently created or initialized by "
                           "a warframe-market-api function or method, please open an issue on GitHub.")
