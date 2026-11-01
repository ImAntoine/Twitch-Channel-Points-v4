#!/usr/bin/env bash
set -Eeuo pipefail

cd "$(dirname "$0")/.."

if [[ ! -f requirements.txt ]]; then
  echo "requirements.txt not found; skipping Python dependency setup."
  exit 0
fi

upm lock --lang python3-pip
upm install --lang python3-pip --quiet
