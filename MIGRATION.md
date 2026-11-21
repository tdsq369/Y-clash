# 迁移说明：CNB → GitHub

原库 `https://cnb.cool/yxsdos/Y-Clash` 于 2026-11-07 被平台封禁（`freeze: true`，git `Repository Not Found`，web 403，raw 404），已不可用。

本仓库是它的完整替代，内容取自封禁前的本地快照（最后 commit `3a84623`，2026-10-29），并做了两件事：

1. 把全部 `.ini` 里指向 CNB raw 的 45 处引用，替换为本仓库的 GitHub raw 地址；
2. 保留目录结构与文件名，方便旧配置逐条对照。

## 新地址

| 用途 | URL |
|---|---|
| rules 原始列表 | `https://raw.githubusercontent.com/tdsq369/Y-clash/main/rules/<name>.list` |
| rulesets（domain 列表） | `https://raw.githubusercontent.com/tdsq369/Y-clash/main/rulesets/<name>.txt` |
| OpenClash rule-provider | `https://raw.githubusercontent.com/tdsq369/Y-clash/main/openclash/<name>.yaml` |
| subconverter 模板 | `https://raw.githubusercontent.com/tdsq369/Y-clash/main/subconverter-ext/all_base.tpl` |
| 订阅转换 ini | `https://raw.githubusercontent.com/tdsq369/Y-clash/main/worker.ini` |

国内直连不稳定的场景可用 jsDelivr 镜像（同路径）：

```
https://cdn.jsdelivr.net/gh/tdsq369/Y-clash@main/rules/direct.list
```

## 仍需同步的现役引用

本地这两处此前指向 CNB 旧地址，需要改成上面的 GitHub 地址：

- `/root/.hermes/gongju/cf-youxuan/cfctl.py` → `FINAL_ROUTER_URL`
- `/root/mihomo-lab/scripts/validate_369696_direct_latest.py` → `RAW`

## 维护规矩

- 规则改动直接在本库提交；`.ini` 里的自引用已统一指向本库，别再写回 CNB 地址。
- 本库为公开库，**不要**放入订阅链接、token、节点凭据。
