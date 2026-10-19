# cleat-fgo-build

构建 FGO 日服汉化 APK。使用 [cleat-fgo-helper](https://github.com/jhq223/cleat-fgo-helper) 处理 XAPK、注入 [cleat-fgo](https://github.com/jhq223/cleat-fgo) 最新模块库，并签名发布。

计划任务同时检查游戏版本和模块 Release 版本；任一变化都会构建，手动运行 workflow_dispatch 可强制构建。构建期间固定使用首次查询到的模块 Release，避免下载文件和版本标记不一致。

Release 标签为 `v<游戏版本>-mod<模块版本>`，包含：

- `fgo-mod.apk`：已签名安装包。
- `update.json`：游戏版本、versionCode、模块版本、下载地址、文件大小和 SHA-256，供模块自动检查与下载。

更新清单由 scripts/update_manifest.py 从已签名 APK 生成。模块比对游戏和模块版本，校验下载后交给 Android 确认安装；发布同版本游戏的新模块不会被漏过，也不会降级较新的游戏。

仓库需要配置 KEYSTORE_BASE64、KEYSTORE_PASS、KEY_ALIAS Secrets。继续使用同一签名，才能覆盖安装并保留应用数据。签名文件和密码不要写入源码。

剧情和字体资源由 helper 另行构建，发布到 cleat-fgo 的 resources Release；该资源 Release 不应标记为 latest。它与此仓库的 APK 更新通道独立。