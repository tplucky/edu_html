"""Sync original HTML pages and validate the public directory without dependencies."""

from html.parser import HTMLParser
from pathlib import Path
import shutil
from urllib.parse import unquote, urlsplit


ROOT = Path(__file__).resolve().parent.parent
SITE = ROOT / "site"
LESSON = ROOT / "认识立体图形 第一课时 分享"
PAGES = {
    LESSON / "360°立体商品观测台.html": "observer-360.html",
    LESSON / "商品上架.html": "shelf-up.html",
    LESSON / "小小建筑师.html": "little-architect.html",
    LESSON / "超市广播猜一猜.html": "radio-guess.html",
    LESSON / "《超市广播谜题游戏》.html": "radio-riddle.html",
    LESSON / "离线互动游戏.html": "offline-game.html",
    ROOT / "数独" / "数独对战.html": "sudoku.html",
}


class DirectoryParser(HTMLParser):
    def __init__(self):
        super().__init__()
        self.pages = set()

    def handle_starttag(self, tag, attrs):
        if tag != "a":
            return
        href = dict(attrs).get("href", "")
        url = urlsplit(href)
        if url.scheme or url.netloc or not url.path:
            return
        path = unquote(url.path)
        target = (SITE / path).resolve()
        if not target.is_relative_to(SITE.resolve()) or not target.is_file():
            raise ValueError(f"目录链接无效：{href}")
        if target.suffix == ".html":
            self.pages.add(path)


def main():
    SITE.mkdir(exist_ok=True)
    for source, name in PAGES.items():
        if not source.is_file() or source.stat().st_size == 0:
            raise ValueError(f"原始页面缺失或为空：{source.relative_to(ROOT)}")
        shutil.copyfile(source, SITE / name)

    parser = DirectoryParser()
    parser.feed((SITE / "index.html").read_text(encoding="utf-8"))
    if parser.pages != set(PAGES.values()):
        raise ValueError("目录页必须包含全部 7 个互动页面，且不能有多余页面链接")
    print(f"PASS：已同步 {len(PAGES)} 个页面，目录链接全部有效。")


if __name__ == "__main__":
    main()
