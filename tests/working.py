from src import wfm
import json


x = wfm.items.Item(url_name="mirage_prime_systems")
y = x.get_orders()
for i in y:
    print(i.get_attributes())
    print("\n")