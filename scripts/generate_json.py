import csv
import errno
import json
import os

def create_path(path):
    try:
        os.makedirs(path)
    except OSError as exception:
        if exception.errno != errno.EEXIST:
            raise

def write_json(filepath):

    with open(filepath) as f:
        reader = csv.DictReader(f)
        rows = list(reader)

    with open('outputs/datastores.json', 'w') as f:
        f.write(json.dumps(rows,
            indent=4,
            separators=(',', ': '),
            encoding="utf-8",
            ensure_ascii=False
            ))

create_path('outputs')
write_json('data/datasources.csv')
