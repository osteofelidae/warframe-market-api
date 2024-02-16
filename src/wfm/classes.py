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
        self._partial: bool = False  # ───▶ Whether generic is partial or not (Partial types may arise, for example,
        #                                   when items are returned in a list)

    # ▒▒▒ Attributes interface ▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒
    def get_attributes(self) -> dict:
        # └──▶ Generic _attributes getter.
        #      Should only be necessary if further postprocessing or a JSON dump is required

        return self._attributes.copy()  # ───▶ Return _attributes

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

        # ┌──▶ Iterate through given attributes
        self._attributes.update(attributes)

