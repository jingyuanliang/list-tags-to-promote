#!/bin/bash

if [ $# -lt 1 ]; then
  echo "usage: $(basename "$0") image_name [tag_name [indention]]"
  exit 1
fi

image=$1; shift

gcloud container images list-tags "$image" --format=json | python3 filter.py "$@"
