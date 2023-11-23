#!/usr/bin/env sh
openapi-generator generate -g python -i ../../immich-openapi-specs.json -p packageVersion=1.88.2
