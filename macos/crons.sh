#!/usr/bin/env bash

set -e

ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)/.."
cd "$ROOT/ai_cronjobs"

./watch-sk-version.sh
./watch-stock1.sh
