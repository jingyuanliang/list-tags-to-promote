#!/usr/bin/env python3

import argparse
import json
import subprocess
import sys

parser = argparse.ArgumentParser()

parser.add_argument('image')
parser.add_argument('tags', nargs='*')
parser.add_argument('--indent', type=int, default=0)

args = parser.parse_args()

gcloud = subprocess.Popen([
    'gcloud', 'container', 'images', 'list-tags', args.image,
    '--format=json',
], stdout=subprocess.PIPE)

image_list = json.load(gcloud.stdout)
image_entries = []
tag_set = set(args.tags)

for image in image_list:
    if tag_set and not tag_set & set(
            x.split('__')[0] for x in image['tags']):
        continue
    image_entries.append(('{}{}: {}'.format(
        ' ' * args.indent,
        json.dumps(image['digest']),
        json.dumps(image['tags']),
    ), tuple(image['tags'])))

image_entries.sort(key=lambda x: x[1])
for image in image_entries:
    print(image[0])
