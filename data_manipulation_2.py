houses = [
    {"price":115910,
     "rooms":4,
     "square_meter":128},

     {"price": 48718,
     "rooms":3,
     "square_meter": 210},

     {"price": 28977,
     "rooms":2,
     "square_meter":58},

     {"price": 36932,
     "rooms":3,
     "square_meter":79},

    {"price": 83903,
     "rooms":3,
     "square_meter":111},
]

for h in houses:
    h["price_per_sqm"] = h["price"]/h["square_meter"]

import pprint
pprint.pprint(houses)

pps = []

for h in houses:
    pps.append(h["price_per_sqm"])

avg = sum(pps) / len(pps)
print(avg)