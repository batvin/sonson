#!/usr/bin/env python3
"""
BAT-PANEL node agent (reference implementation)
=================================================

Runs on a VPN node (the actual server running xray-core / WireGuard / OpenVPN).
Reports traffic and receives config updates from the central BAT-PANEL API.

This is a reference implementation; production hardening and full protocol
support are left for future work.
"""

from __future__ import annotations

import argparse
import hashlib
import hmac
import json
import os
import sys
import time
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

import urllib.request
import urllib.error


def utc_now() -> str:
    return datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")


def sign(secret: str, body: bytes) -> str:
    return hmac.new(secret.encode(), body, hashlib.sha256).hexdigest()


def post_json(url: str, payload: dict, secret: str, timeout: int = 15) -> dict:
    body = json.dumps(payload, separators=(",", ":")).encode()
    req = urllib.request.Request(
        url,
        data=body,
        headers={
            "Content-Type": "application/json",
            "X-Agent-Signature": sign(secret, body),
            "User-Agent": "bat-agent/0.1",
        },
        method="POST",
    )
    with urllib.request.urlopen(req, timeout=timeout) as resp:
        return json.loads(resp.read().decode())


def get_json(url: str, secret: str, timeout: int = 15) -> dict:
    req = urllib.request.Request(
        url,
        headers={
            "X-Agent-Signature": sign(secret, b""),
            "User-Agent": "bat-agent/0.1",
        },
        method="GET",
    )
    with urllib.request.urlopen(req, timeout=timeout) as resp:
        return json.loads(resp.read().decode())


def main() -> int:
    parser = argparse.ArgumentParser(description="BAT-PANEL node agent")
    parser.add_argument("--api", required=True, help="Central panel API base, e.g. http://panel:8000")
    parser.add_argument("--node-id", required=True, help="Node identifier registered in the panel")
    parser.add_argument("--secret", required=True, help="Shared HMAC secret")
    parser.add_argument("--interval", type=int, default=30, help="Report interval in seconds")
    parser.add_argument("--once", action="store_true", help="Run a single report cycle and exit")
    args = parser.parse_args()

    api = args.api.rstrip("/")
    print(f"[{utc_now()}] bat-agent starting for node={args.node_id} api={api}", flush=True)

    while True:
        try:
            # Placeholder traffic report (real implementation would read from xray/WireGuard stats)
            payload = {
                "node_id": args.node_id,
                "reported_at": utc_now(),
                "traffic": {
                    "up": 0,
                    "down": 0,
                },
                "clients": [],
            }
            result = post_json(f"{api}/api/agent/traffic", payload, args.secret)
            print(f"[{utc_now()}] traffic reported: {result}", flush=True)

            # Optional: pull desired config
            try:
                cfg = get_json(f"{api}/api/agent/config?node_id={args.node_id}", args.secret)
                print(f"[{utc_now()}] config pull: keys={list(cfg.keys()) if isinstance(cfg, dict) else type(cfg)}", flush=True)
            except Exception as e:
                print(f"[{utc_now()}] config pull skipped: {e}", flush=True)

        except Exception as e:
            print(f"[{utc_now()}] error: {e}", flush=True)

        if args.once:
            break
        time.sleep(max(5, args.interval))

    return 0


if __name__ == "__main__":
    sys.exit(main())
