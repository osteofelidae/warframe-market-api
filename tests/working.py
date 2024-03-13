from src import wfm
import json


x = wfm.items.get_all_items()

for i in x:
    print(i.get_attributes())