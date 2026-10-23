# 小学数学互动资源

小学数学教学动画与互动游戏，包含立体图形观察、分类、搭建、广播谜题与数独。

- [在线目录](https://tplucky.github.io/edu_html/)
- [GitHub 仓库](https://github.com/tplucky/edu_html)

## 页面目录

| 页面 | 用途 |
| --- | --- |
| [360° 立体商品观测台](site/observer-360.html) | 旋转观察长方体、正方体、圆柱和球 |
| [商品上架](site/shelf-up.html) | 按形状分类生活物品 |
| [小小建筑师](site/little-architect.html) | 用立体图形组合搭建 |
| [超市广播猜一猜](site/radio-guess.html) | 根据描述识别图形 |
| [超市广播谜题游戏](site/radio-riddle.html) | 多轮广播谜题挑战 |
| [离线互动游戏](site/offline-game.html) | 图形超市整合版 |
| [数独对战](site/sudoku.html) | 数独逻辑练习与同屏对战 |

## 本地运行

无需安装依赖，使用 Python 3：

```sh
python3 scripts/build_site.py
python3 -m http.server 8000 --directory site
```

在浏览器打开 <http://localhost:8000/>。也可以直接打开 `site/index.html`。
页面图片和主要脚本已内嵌；数独的背景音乐使用外部链接，离线时不保证可播放。
最大单页约 29 MiB，首次访问可能需要等待。

## 更新与发布

- `认识立体图形 第一课时 分享/` 和 `数独/` 保存原始页面，在这里修改游戏。
- `site/index.html` 是网站目录页，新增游戏时同时更新目录和构建脚本中的映射。
- `python3 scripts/build_site.py` 将原始页面同步到 `site/`，并检查目录链接。
- GitHub Pages 的发布来源设为 **GitHub Actions**。推送到 `main` 后，工作流同步并检查页面，仅将 `site/` 发布到网站；也可以在 Actions 中手动运行。
- 本地图片制作缓存、浏览器记录及工具状态由 `.gitignore` 排除，不进入仓库或网站。

## 开源许可

项目原创代码按 [MIT License](LICENSE) 开源。页面中内嵌的 Three.js 和
OrbitControls 保留各自 MIT 版权与许可声明。第三方图片、音频等素材的权利归其原权利人，
本仓库的 MIT 许可不额外授予这些素材的使用权；数独背景音乐仍使用原页面中的外部资源地址。
