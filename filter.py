#!/usr/bin/env python3

import json
import sys

image_list = json.load(sys.stdin)
tag = sys.argv[1] if len(sys.argv) > 1 else ''
indent = ' ' * int(sys.argv[2]) if len(sys.argv) > 2 else ''
images = []

for image in image_list:
    if tag and not any(
            x == tag or x.startswith(tag + '__') for x in image['tags']):
        continue
    images.append(('{}{}: {}'.format(
        indent, json.dumps(image['digest']), json.dumps(image['tags'])
    ), tuple(image['tags'])))

images.sort(key=lambda x: x[1])
for image in images:
    print(image[0])
