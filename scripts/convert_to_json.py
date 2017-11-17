import csv, json

with open('data/bootcamp_data.csv') as f:
    reader = csv.DictReader(f)
    rows = list(reader)

with open('data/bootcamp_data.json', 'w') as f:
    json.dump(rows, f)
    f.write('/n')