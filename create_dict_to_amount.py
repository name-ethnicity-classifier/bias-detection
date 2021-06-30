import pickle
import json

pickle_file = "INPUT.pickle"

with open(pickle_file, 'rb') as f:
    x = pickle.load(f)

nat_to_amount = {}
for key in x:
    nat_to_amount[key]=len(x[key])

with open("OUTPUT.json", 'w') as fp:
    json.dump(nat_to_amount, fp)