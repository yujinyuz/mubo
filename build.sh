#!/usr/bin/env bash
# Exit on error
set -o errexit

pip install wheel hatch pex

hatch build

pex dist/*.whl -o mubo.pex -c mubo

ls -l

echo $PWD

chmod +x mubo.pex

./mubo.pex collectstatic
./mubo.pex migrate

