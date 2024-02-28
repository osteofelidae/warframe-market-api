from src import wfm
import json

# TODO testing
#wfm.auth.sign_up(email="osteofelidae@gmail.com",
#                 password="Testing123")

i = wfm.Item()
i._update_attributes({"url_name": "mirage_prime_systems"})
#i._update_attributes({"url_name": "oull"})
i.update()
print(i.get_attributes())
print(i.get_item_data())
print(i.get_set_data())

fp = open("temp.json", "w")
json.dump(i.get_attributes(), fp, indent=4)
fp.close()

fp = open("temp2.json", "w")
json.dump(i.get_item_data(), fp, indent=4)
fp.close()

fp = open("temp3.json", "w")
json.dump(i.get_set_data(), fp, indent=4)
fp.close()