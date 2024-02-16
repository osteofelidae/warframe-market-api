# ███ DEPENDENCIES █████████████████████████████████████████████████████████████████████████████████████████████████████
import unittest
import string
import random
from src import wfm


# ███ CONSTANTS ████████████████████████████████████████████████████████████████████████████████████████████████████████
RAND_LEN = 5  # ───▶ Affects things like the number of elements in a random array


# ███ FUNCTIONS ████████████████████████████████████████████████████████████████████████████████████████████████████████
def rand_str(length: int = RAND_LEN  # ───▶ Length of random string
             ) -> str:
    # └──▶ Generate a random string of a certain length

    # ┌──▶ Generate and return the string
    result: str = "".join(random.choices(string.ascii_uppercase + string.digits,
                                         k=length))
    return result


def rand_int(lower: int = 1,  # ───▶ Lower bound
             upper: int = RAND_LEN,  # ───▶ Lower bound
             ) -> int:
    # └──▶ Generate a random int in a certain range

    # ┌──▶ Generate and return the int
    result: int = random.randint(lower, upper)
    return result


# ███ TEST CASES ███████████████████████████████████████████████████████████████████████████████████████████████████████
class TestGenericClass(unittest.TestCase):
    # └──▶ Test wfm.Generic class

    def test_constructor(self):
        # └──▶ Test wfm.Generic.__init__()

        # ┌──▶ Test proper setting of instance variables
        generic = wfm.Generic()
        self.assertEqual(generic._attributes,
                         {})
        self.assertEqual(generic._partial,
                         False)

        # ┌──▶ Test proper referential integrity of instance variables
        test_attributes = {}
        for i in range(rand_int(lower=2)):
            test_attributes[rand_str()] = rand_str()
        generic._attributes = test_attributes
        for i in range(rand_int(lower=2)):
            test_attributes[rand_str()] = rand_str()
        self.assertNotEqual(generic._attributes,
                            False)

    def test_attributes_interface(self):
        # └──▶ Test wfm.Generic types' attribute interfaces

        # ┌──▶ Test wfm.Generic.get_attributes()
        test_attributes = {}
        for i in range(rand_int(lower=2)):
            test_attributes[rand_str()] = rand_str()
        generic = wfm.Generic()
        generic._attributes = test_attributes
        attributes = generic.get_attributes()
        self.assertEqual(attributes,
                         test_attributes)
        test_attributes = {}
        for i in range(rand_int(lower=2)):
            test_attributes[rand_str()] = rand_str()
        self.assertNotEqual(attributes,
                            test_attributes)

        # ┌──▶ Test wfm.Generic._set_attributes()
        test_attributes = {}
        for i in range(rand_int(lower=2)):
            test_attributes[rand_str()] = rand_str()
        generic = wfm.Generic()
        generic._set_attributes(attributes=test_attributes)
        self.assertEqual(generic._attributes,
                         test_attributes)

        # ┌──▶ Test wfm.Generic._update_attributes()
        test_attributes = {}
        for i in range(rand_int(lower=2)):
            test_attributes[rand_str()] = rand_str()
        updater_attributes = {random.choice(list(test_attributes.keys())): rand_str()}
        generic = wfm.Generic()
        generic._attributes = test_attributes.copy()
        updated_attributes = test_attributes.copy()
        updated_attributes.update(updater_attributes)
        generic._update_attributes(updater_attributes)
        self.assertEqual(generic._attributes,
                         updated_attributes)


# ███ RUN ██████████████████████████████████████████████████████████████████████████████████████████████████████████████
if __name__ == '__main__':
    unittest.main()
