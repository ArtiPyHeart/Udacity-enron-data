

filename = 'poi_names.txt'

with open(filename) as f:
    raw_text = f.readlines()

text = [i.strip() for i in raw_text]

print len(text[2:])