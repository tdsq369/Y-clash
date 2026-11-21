{% if request.target == "clash" or request.target == "clashr" %}

port: {{ default(global.clash.http_port, "7890") }}
socks-port: {{ default(global.clash.socks_port, "7891") }}
allow-lan: {{ default(global.clash.allow_lan, "true") }}
mode: Rule
log-level: {{ default(global.clash.log_level, "info") }}
external-controller: {{ default(global.clash.external_controller, "127.0.0.1:9090") }}

# Persist Mihomo fake-IP mappings across core/OpenClash restarts.
# This prevents browser/client cached 198.18.x.x addresses from pointing to
# a different domain after a restart, which can cause TLS certificate mismatch.
profile:
  store-selected: true
  store-fake-ip: true

{% if default(request.clash.dns, "") == "1" %}
dns:
  enable: true
  nameserver:
  - https://dns.alidns.com/dns-query#h3=true
  - https://doh.pub/dns-query
  direct-nameserver:
  - https://dns.alidns.com/dns-query#h3=true
  - https://doh.pub/dns-query
  proxy-server-nameserver:
  - https://doh.pub/dns-query
  - https://dns.alidns.com/dns-query#h3=true
  default-nameserver:
  - tls://119.29.29.29
  - tls://223.5.5.5
# Fake-IP 模式下，建议不要启用 fallback-server
{% endif %}
{% if local.clash.new_field_name == "true" %}
proxy-groups: ~
rules: ~
{% else %}
proxy-groups: ~
rules: ~
{% endif %}

{% endif %}
