#!/usr/bin/env bash

set -e

HERE="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
cd "$HERE"

poetry run python watch-sk-version.py > watch-sk-version.log 2>&1
