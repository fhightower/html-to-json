#!/usr/bin/env bash

set -euxo pipefail

echo "Running linters and formatters..."

isort html_to_json/ tests/

black html_to_json/ tests/

mypy html_to_json/ tests/

pylint --fail-under 9 html_to_json/*.py

flake8 html_to_json/

# we run black again at the end to undo any odd changes made by any of the linters above
black html_to_json/ tests/
