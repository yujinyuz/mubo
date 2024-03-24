#!/usr/bin/env bash
# Exit on error
set -o errexit

python setup.py bdist_wheel

pip install dist/*.whl
django-project collectstatic --no-input
