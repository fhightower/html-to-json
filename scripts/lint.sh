#!/usr/bin/env bash

set -euxo pipefail

echo "Running linters and formatters..."

uv run ruff check html_to_json/ tests/
uv run ruff format --check html_to_json/ tests/
uv run mypy html_to_json/ tests/
