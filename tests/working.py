from src import wfm

# TODO testing
#wfm.auth.sign_up(email="osteofelidae@gmail.com",
#                 password="Testing123")

i = wfm.Item()
i._update_attributes({"url_name": "mirage_prime_systems"})
i.fetch()
print(i.get_attributes())