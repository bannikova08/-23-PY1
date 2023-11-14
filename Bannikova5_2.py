import csv
import json

def csv_to_json(csv_file, d=",", nl="\n"):
    with open(csv_file, 'r') as f:
        csv_reader = csv.DictReader(f, delimiter=d, lineterminator=nl)
        data = list(reader)
        json_data = json.dumps(data, indent=4)
        return(json_data)

csv_file = "example.csv"
print(csv_to_json(csv_file))
