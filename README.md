# Y-clash

> OpenClash / Mihomo (Clash Meta) 规则仓库
> AI 可直接修改 rules/ 目录下的文件来添加/删除规则

## 快速开始

### 使用订阅转换器

配置文件: `cm.ini`

```
{订阅转换器后端}/sub?target=clash&config=https://raw.githubusercontent.com/tdsq369/Y-clash/main/cm.ini&url=你的订阅链接
```

### WorkerVless2sub (CF Worker)

配置文件: `lyj.ini`

CF Worker 环境变量:
- SUBAPI: `{订阅转换器后端域名}`
- SUBCONFIG: `https://raw.githubusercontent.com/tdsq369/Y-clash/main/lyj.ini`

### OpenClash 覆写

OpenClash → 覆写设置 → 自定义配置 → 粘贴 `cm.ini` 内容 → 应用

## 规则格式

每行一条:
```
DOMAIN-SUFFIX,example.com     # 匹配 example.com 及所有子域名
DOMAIN-KEYWORD,example        # 匹配域名中包含 example 的
DOMAIN,example.com            # 精确匹配
```

## 文件结构

```
Y-clash/
├── cm.ini                 ← 主配置 (订阅转换器用)
├── lyj.ini                ← WorkerVless2sub 配置 (CF Worker 用)
├── worker-roundrobin.ini  ← 多连接 CF 轮询候选配置标识
├── rules/                 ← 规则文件 (AI 维护)
│   ├── proxy.list         ← 代理规则 (BT/PT/VRChat/流媒体)
│   ├── direct.list        ← 直连规则
│   └── block.list         ← 屏蔽规则
├── openclash/             ← YAML 格式规则 (rule-providers)
│   ├── proxy.yaml
│   ├── direct.yaml
│   └── block.yaml
├── debug/                 ← 调试脚本
│   ├── test-dns.sh        ← DNS 分流测试
│   └── test-rules.sh      ← 规则匹配测试
├── CHANGELOG.md
├── docs/
│   └── openclash-roundrobin-load-balance.md ← 轮询候选、验证与启用边界
├── scripts/
│   └── build-roundrobin-openclash-yaml.py ← 对生成 YAML 注入 round-robin
└── README.md
```

## 多连接 CF 负载均衡

多线程下载或并发连接需要使用 `round-robin`，但单条 TCP/WebSocket 不会叠加带宽。当前独立候选、验证记录、启用前置条件和回滚方法见 [docs/openclash-roundrobin-load-balance.md](docs/openclash-roundrobin-load-balance.md)。交易和认证会话应保持稳定策略，不应路由到轮询组。

## 添加规则

告诉 AI:
- "把 example.com 加到代理规则" → 编辑 `rules/proxy.list`
- "把 example.com 加到直连规则" → 编辑 `rules/direct.list`
- "把 example.com 加到屏蔽规则" → 编辑 `rules/block.list`

AI 会自动同步更新 `openclash/*.yaml` 并推送。

## 调试

```sh
# DNS 分流测试
bash debug/test-dns.sh

# 规则匹配测试
bash debug/test-rules.sh github.com
```

## 变更规则后

AI 需要同步:
1. 编辑 `rules/*.list` (clash-domain 格式)
2. 运行同步脚本生成 `openclash/*.yaml` (YAML payload 格式)
3. git commit + push

## 参考

- [Aethersailor/Custom_OpenClash_Rules](https://github.com/Aethersailor/Custom_OpenClash_Rules)
- [mihomo 官方文档](https://wiki.metacubex.one/config/)
- [Yjhermes 经验包](https://cnb.cool/yxsdos/Yjhermes)
