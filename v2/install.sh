#!/usr/bin/env bash
set -Eeuo pipefail

ROOT="$(cd "$(dirname "$0")" && pwd)"
cd "$ROOT"

if [[ ! -f .env ]]; then
  cp .env.example .env
  echo "Created .env from .env.example — edit it before starting."
fi

# Ensure PANEL_PORT is present
if ! grep -q '^PANEL_PORT=' .env; then
  echo "PANEL_PORT=8000" >> .env
fi

echo "Starting BAT-PANEL V2 with Docker Compose..."
docker compose -p batman-v2 up -d --build
echo "Done. Panel should be on http://127.0.0.1:$(grep PANEL_PORT .env | cut -d= -f2)"
