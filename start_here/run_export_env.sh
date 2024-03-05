#!/bin/sh

pip_packages=$(conda env export | grep -A9999 ".*- pip:" | grep -v "^prefix: ")

conda env export --from-history | grep -v "^prefix: " > environment.yml

echo "$pip_packages" >> environment.yml