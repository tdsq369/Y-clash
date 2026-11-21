#!/usr/bin/env python3
"""Build a separate OpenClash YAML with round-robin load balancing.

This never changes the active OpenClash config path. Run Mihomo's config test
before switching to the generated candidate on a router.
"""

from __future__ import annotations

import sys
from pathlib import Path

try:
    import yaml
except ImportError as exc:
    raise SystemExit("PyYAML is required: python3 -m pip install pyyaml") from exc

GROUP_NAME = "🔮 负载均衡"


def main() -> int:
    if len(sys.argv) != 3:
        raise SystemExit(f"usage: {Path(sys.argv[0]).name} SOURCE.yaml DESTINATION.yaml")

    source = Path(sys.argv[1])
    destination = Path(sys.argv[2])
    if not source.is_file():
        raise SystemExit(f"source does not exist: {source}")

    with source.open(encoding="utf-8") as handle:
        config = yaml.safe_load(handle)

    groups = config.get("proxy-groups", [])
    group = next((item for item in groups if item.get("name") == GROUP_NAME), None)
    if not group or group.get("type") != "load-balance":
        raise SystemExit(f"missing load-balance group: {GROUP_NAME}")

    group["strategy"] = "round-robin"
    group["lazy"] = True

    destination.parent.mkdir(parents=True, exist_ok=True)
    with destination.open("w", encoding="utf-8") as handle:
        yaml.safe_dump(config, handle, allow_unicode=True, sort_keys=False)

    provider_names = ",".join(group.get("use", []))
    print(f"output={destination}")
    print(
        f"group={group['name']} type={group['type']} "
        f"strategy={group['strategy']} lazy={group['lazy']} use={provider_names}"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
