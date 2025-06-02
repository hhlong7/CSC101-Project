from classes import *
from funcs import *
routes = {
    # Sacramento ─────────────────────────────────────────────
    ("Sacramento", "San Francisco"): [87.6, Time(1, 35, 0)],
    ("Sacramento", "San Jose")     : [121.2, Time(1, 55, 0)],
    ("Sacramento", "Fremont")      : [90.3, Time(1, 30, 0)],
}





if get_distance("Sacramento", "San Jose") is not None:
    # Do something with my_variable, assuming it's not None
    print(get_distance("Sacramento", "San Jose"))
else:
    # Handle the case where my_variable is None
    print("Location not in CA")





