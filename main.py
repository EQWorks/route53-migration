import json
import argparse
import os


def transform(f, w):
    j = json.load(f)
    rs = j.get('ResourceRecordSets')
    # remove NS and SOA records
    # create Change set
    changes = {
        'Comment': 'from juicemobile',
        'Changes': [
            {
                'Action': 'CREATE',
                'ResourceRecordSet': r,
            }
            for r in rs if r['Type'] not in ('NS', 'SOA')
        ]
    }
    json.dump(changes, w, indent=2)


def main(directory):
    for fn in os.listdir(directory):
        with open(f'change/{fn}', 'w') as w:
            with open(f'{directory}/{fn}') as f:
                transform(f, w)


if __name__ == "__main__":
    main(directory='public')
