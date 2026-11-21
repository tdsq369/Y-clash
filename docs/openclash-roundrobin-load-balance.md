# OpenClash 多连接 CF 轮询负载均衡

## 目标与边界

本方案仅用于多个独立连接的 CF 入口分配，例如多线程下载、视频分片和并发请求。

- `round-robin`：每个新连接按顺序分配到负载均衡组内不同节点。
- 不聚合单个 TCP 连接的带宽。
- 不聚合单条 WebSocket 的带宽。
- 多 WAN 的物理出口叠加还需要上游路由器的多 WAN 分流；Mihomo 只负责代理节点选择。
- 交易和认证会话不应进入轮询组。Bybit 维持在稳定的 `🚀 节点选择` 策略。

官方语义参考：<https://wiki.metacubex.one/en/config/proxy-groups/load-balance>

## 当前文件和状态

| 项目 | 路径/值 | 状态 |
| --- | --- | --- |
| 当前活动配置 | `/etc/openclash/config/php-dyq-zl.yaml` | 运行中 |
| 当前负载均衡策略 | `consistent-hashing` | 运行中 |
| 轮询候选配置 | `/etc/openclash/config/php-dyq-zl-roundrobin.yaml` | 已生成，未启用 |
| 候选策略 | `round-robin` | 已验证 |
| 节点来源 | `Provider_25A91C` | 与活动配置相同 |
| Bybit 规则 | `rules/proxy.list` | 已运行时验证，走 `🚀 节点选择` |

候选 YAML 是从当前活动 YAML 复制后生成。除 `🔮 负载均衡` 的 `strategy` 从 `consistent-hashing` 改为 `round-robin` 外，其他 YAML 设置一致；候选组同样设置 `lazy: true`。

## 仓库文件

- `worker-roundrobin.ini`：完整规则和完整策略组的独立配置标识。它不单独保证输出 YAML 包含 `strategy`。
- `scripts/build-roundrobin-openclash-yaml.py`：将已生成的完整 YAML 复制为候选，并对 `🔮 负载均衡` 显式注入 `strategy: round-robin` 和 `lazy: true`。

传统 SubConverter 的 `custom_proxy_group` INI 格式不能作为 `strategy` 持久化的唯一依据。后续更新订阅后，必须重新对输出 YAML 运行该脚本，再用 Mihomo 做配置测试。

## 已完成验证

2026-08-07：

1. `worker-roundrobin.ini` 与 `worker.ini` 的 `ruleset=` 和 `custom_proxy_group=` 行逐项一致。
2. 独立候选 YAML 的 `🔮 负载均衡` 确认为：
   ```yaml
   type: load-balance
   strategy: round-robin
   lazy: true
   use:
     - Provider_25A91C
   ```
3. 路由器执行：
   ```sh
   /etc/openclash/clash -t -d /etc/openclash \
     -f /etc/openclash/config/php-dyq-zl-roundrobin.yaml
   ```
   返回 `configuration file ... test is successful`。
4. 当前活动路径仍为 `/etc/openclash/config/php-dyq-zl.yaml`；没有因创建候选文件而切换生产流量。

## 后续调整入口

### 调整轮询行为

编辑候选 YAML 的 `🔮 负载均衡` 组；推荐保持：

```yaml
strategy: round-robin
lazy: true
```

不要把 Bybit、银行、交易所、登录态敏感域名路由到该组。

### 为下载流量单独使用轮询

不要把整个 `🚀 节点选择` 改成 `🔮 负载均衡`，否则 Bybit 也会进入轮询。应新增“下载专用”策略组并配套精确下载规则，或在下载客户端显式选择该组。变更前需要确认下载器、目标域名和是否允许影响其他应用。

### 准备启用候选配置

切换会重启 OpenClash，约造成短暂代理中断。切换前必须：

1. 备份 `/etc/config/openclash` 和当前活动 YAML。
2. 再次执行候选 YAML 的 Mihomo `-t` 测试。
3. 显式确认将 `openclash.config.config_path` 改为候选路径的生产范围。
4. 重启后验证进程路径、监听端口、策略组运行态和多连接下载日志。

回滚方式是将 `openclash.config.config_path` 恢复为 `/etc/openclash/config/php-dyq-zl.yaml` 后重启 OpenClash。

## 关联提交与备份

- Y-clash 提交：`6febfef feat: add round-robin OpenClash candidate config`
- 路由器候选创建备份：`/etc/openclash/backup/roundrobin-candidate-20260807-191458`
- 本地源文件备份：`/root/.hermes/memories/backups/20260807-191225/y-clash-roundrobin`