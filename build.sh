#!/usr/bin/env bash
# Exit on error
set -o errexit

pip install setuptools wheel
python setup.py bdist_wheel

pip install dist/*.whl
django-project collectstatic --no-input

django-admin migrate --settings=mubo.conf.settings
