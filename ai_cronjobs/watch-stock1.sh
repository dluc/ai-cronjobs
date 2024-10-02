#!/usr/bin/env bash

set -e

HERE="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
cd "$HERE"

poetry run python watch-stock1.py > watch-stock1.log 2>&1
