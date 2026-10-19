# 构建与发布

## 配置构建

在仓库 Settings → Secrets and variables → Actions 中添加：

| Secret | 内容 |
|---|---|
| `KEYSTORE_BASE64` | 签名文件的 Base64 内容 |
| `KEYSTORE_PASS` | 签名文件密码 |
| `KEY_ALIAS` | 签名别名 |

后续版本使用同一签名，支持覆盖安装并保留应用数据。

进入 Actions → **Build FGO Mod APK (JP)** → **Run workflow**，即可手动构建。计划任务在每周三、五检查游戏和模块版本，发现更新后自动构建。

构建过程下载游戏 XAPK 和最新模块库，通过 [cleat-fgo-helper](https://github.com/jhq223/cleat-fgo-helper) 打包并签名。

## 发布文件

Release 标签为 `v<游戏版本>-mod<模块版本>`，包含：

| 文件 | 用途 |
|---|---|
| `fgo-mod.apk` | 已签名安装包 |
| `update.json` | 游戏版本、模块版本、APK 下载地址、大小和 SHA-256 |

工作流使用 [scripts/update_manifest.py](scripts/update_manifest.py) 生成更新清单并随 APK 发布，供模块检查更新。