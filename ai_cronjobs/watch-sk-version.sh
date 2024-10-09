#!/usr/bin/env bash

set -e

HERE="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
cd "$HERE"

# Check if 'poetry' is available
if command -v poetry >/dev/null 2>&1; then
    POETRY_CMD="poetry"
elif [ -x "/opt/homebrew/bin/poetry" ]; then
    POETRY_CMD="/opt/homebrew/bin/poetry"
else
    echo "Error: 'poetry' is not installed. Please install it."
    exit 1
fi

$POETRY_CMD run python watch-sk-version.py > watch-sk-version.log 2>&1
