#!/usr/bin/env bash

set -euxo pipefail

echo "Running linters and formatters..."

isort html_to_json/ tests/

black html_to_json/ tests/

mypy html_to_json/ tests/

pylint --fail-under 9 html_to_json/*.py

flake8 html_to_json/
