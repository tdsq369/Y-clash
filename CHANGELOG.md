# Changelog

## Unreleased

### 新增
- 新增 `worker-roundrobin.ini` 与 `scripts/build-roundrobin-openclash-yaml.py`，用于从完整生成 YAML 构建多连接 CF 轮询候选配置。
- 新增 `docs/openclash-roundrobin-load-balance.md`，记录当前候选、验证结果、启用边界和回滚路径。

### 说明
- 候选配置使用 `strategy: round-robin`，仅分配多个新连接，不聚合单条 TCP/WebSocket 带宽。
- 候选配置未自动替换当前生产活动配置；Bybit 维持稳定代理策略，不进入轮询负载均衡。

## v3.3-simple (2026-06-15)

### 新增
- 新增 `subconverter-ext/Simple_Clash.ini`，用于 SubConverter-Extended 简化分组订阅。

### 变更
- 简化版不使用地区分组、自动选择、故障转移、负载均衡；规则继续引用当前仓库 `rules/` 内容，便于后续维护。

## v3.2 (2026-05-30)

### 新增
- 合并 ACL4SSR 规则集: LocalAreaNetwork/UnBan/BanAD/BanProgramAD/GoogleCN/SteamCN/ChinaDomain/ChinaCompanyIp/Telegram/ProxyMedia/ProxyLite
- 新增 cmliu: adobe (Adobe 广告) / CloudflareCIDR (Cloudflare CDN)
- 新增策略组: ☁️ CloudFlareCDN

### 变更
- 规则组织重构: 局域网/解禁 → 广告拦截 → 中国直连 → 分类代理 → 兜底
- GEOSITE/GEOIP + ACL4SSR 双覆盖，互相补充
- 规则数从 173,706 增至 181,721

## v3.1.1 (2026-05-30)

### 修复
- 修复 ProxyGroup 循环引用：子组(AI/流媒体/社交/开发/游戏)不再引用「🚀 节点选择」，消除 Mihomo "loop is detected" 报错

## v3.1 (2026-05-30)

### 新增
- 合并 Yjhermes 需VPN的BT站点 (18个) 到 proxy.list
- 新增 debug/ 调试脚本 (test-dns.sh, test-rules.sh)
- 规则文件拆分为 rules/ 目录 (proxy.list, direct.list, block.list)
- YAML 格式规则同步更新 (openclash/proxy.yaml 等)

### 变更
- 所有自定义规则 URL 从 GitHub raw 迁移到 CNB raw
- 订阅转换器配置 URL 更新为 CNB 仓库地址
- 策略组从 6 个升级到 12 个 (按服务细分)
- 测速 URL 从 zl.369529.xyz 统一为 gstatic.com/generate_204
- 广告规则从 Aethersailor (失效) 替换为 Loyalsoldier (稳定)
- GEO 数据库启用自动更新 (720h)

### 移除
- 旧版 ACL4SSR_Online_Mini_MultiMode.ini (被 cm.ini 取代)
- vps/ 目录 (VPS 用户直接用 cm.ini)

## v3.0 (2026-05-30)

### 新增
- 终极版配置: 按服务细分策略组
- AI/流媒体/社交/开发/游戏 独立分组
- tcp_concurrent + unified_delay + geodata_mode 全开
- 完整 fake-ip-filter 配置

## v2

- CF优选IP + 甲骨文SG落地
- Loyalsoldier 广告拦截
- Aethersailor PT/BT 端口放行

## v1

- 初始版本
