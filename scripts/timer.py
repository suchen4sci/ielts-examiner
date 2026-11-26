"""Per-call audible IELTS timers for interactive Windows Codex sessions."""
import argparse
import hashlib
import json
import os
from pathlib import Path
import subprocess
import sys
import tempfile
import time
import uuid
import winsound

LIMITS = {"part1": 30, "prepare": 60, "part2": 120, "part3": 60}


def run():
    parser = argparse.ArgumentParser()
    parser.add_argument("action", choices=[*LIMITS, "cancel", "status", "_wait"])
    parser.add_argument("session", help="Unique identifier for this mock")
    parser.add_argument("token", nargs="?")
    args = parser.parse_args()
    key = hashlib.sha256(args.session.encode()).hexdigest()
    state = Path(tempfile.gettempdir()) / ("ielts-timer-" + key + ".json")

    def read():
        try:
            return json.loads(state.read_text(encoding="utf-8"))
        except FileNotFoundError:
            return {}

    def write(data):
        tmp = state.with_suffix("." + uuid.uuid4().hex)
        tmp.write_text(json.dumps(data), encoding="utf-8")
        os.replace(tmp, state)

    if args.action == "cancel":
        write({})
        return
    if args.action == "status":
        print(json.dumps(read()))
        return
    if args.action == "_wait":
        while True:
            current = read()
            if current.get("token") != args.token:
                return
            remaining = current["deadline"] - time.monotonic()
            if remaining <= 0:
                winsound.Beep(880, 300)
                return
            time.sleep(min(remaining, 0.2))

    token = uuid.uuid4().hex
    limit = LIMITS[args.action]
    write(dict(token=token, phase=args.action, deadline=time.monotonic() + limit))
    try:
        proc = subprocess.Popen(
            [sys.executable, str(Path(__file__).resolve()), "_wait", args.session, token],
            creationflags=subprocess.CREATE_NO_WINDOW | subprocess.CREATE_NEW_PROCESS_GROUP,
            stdin=subprocess.DEVNULL, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL,
        )
    except OSError:
        write({})
        raise
    print(json.dumps(dict(phase=args.action, seconds=limit, pid=proc.pid)))


if __name__ == "__main__":
    run()
