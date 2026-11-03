"""產生 sitemap.xml 和 feed.xml（RSS）。

用法：在 repo 根目錄執行 `python tools/gen_sitemap.py`
- 掃描 index.html、contact.html 和 post/*.html（不含 draft/、lab/、temp/）
- lastmod 用 git 最後一次 commit 的時間；還沒 commit 的檔案用今天
- RSS 從每篇文章的 og:title、description、JSON-LD datePublished 讀出
"""
import html
import re
import subprocess
from datetime import datetime, timezone
from email.utils import format_datetime
from pathlib import Path

SITE = "https://xd3an.github.io"
ROOT = Path(__file__).resolve().parent.parent


def git_lastmod(path):
    """檔案最後一次 commit 的時間（ISO 8601）；有未 commit 的修改就用現在"""
    rel = path.relative_to(ROOT).as_posix()
    dirty = subprocess.run(["git", "status", "--porcelain", "--", rel], cwd=ROOT,
                           capture_output=True, text=True).stdout.strip()
    if not dirty:
        out = subprocess.run(["git", "log", "-1", "--format=%cI", "--", rel], cwd=ROOT,
                             capture_output=True, text=True).stdout.strip()
        if out:
            return out
    return datetime.now(timezone.utc).replace(microsecond=0).isoformat()


def meta(text, attr, name):
    """讀 <meta name/property="..." content="...">，屬性可以跨行"""
    m = re.search(r'<meta\s+%s="%s"\s+content="([^"]*)"' % (attr, re.escape(name)), text, re.S)
    return html.unescape(m.group(1).strip()) if m else ""


def read_post(path):
    text = path.read_text(encoding="utf-8")
    title = meta(text, "property", "og:title")
    if not title:
        m = re.search(r"<title>\s*(.*?)\s*</title>", text, re.S)
        title = html.unescape(m.group(1)) if m else path.stem
    title = re.sub(r"\s*\|\s*XD3an Blog\s*$", "", title)
    desc = meta(text, "name", "description")
    m = re.search(r'"datePublished"\s*:\s*"(\d{4}-\d{2}-\d{2})', text)
    date = m.group(1) if m else None
    return title, desc, date


def main():
    pages = [(ROOT / "index.html", f"{SITE}/", "1.00"),
             (ROOT / "contact.html", f"{SITE}/contact.html", "0.50")]
    posts = sorted((ROOT / "post").glob("*.html"))
    pages += [(p, f"{SITE}/post/{p.name}", "0.80") for p in posts]

    urls = []
    for path, loc, prio in pages:
        urls.append(f"  <url>\n    <loc>{loc}</loc>\n    <lastmod>{git_lastmod(path)}</lastmod>\n"
                    f"    <priority>{prio}</priority>\n  </url>")
    sitemap = ('<?xml version="1.0" encoding="UTF-8"?>\n'
               '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'
               + "\n".join(urls) + "\n</urlset>\n")
    (ROOT / "sitemap.xml").write_text(sitemap, encoding="utf-8")

    items = []
    for p in posts:
        title, desc, date = read_post(p)
        if not date:
            continue
        pub = format_datetime(datetime.fromisoformat(date).replace(tzinfo=timezone.utc))
        items.append((date, f"    <item>\n      <title>{html.escape(title)}</title>\n"
                            f"      <link>{SITE}/post/{p.name}</link>\n"
                            f"      <guid>{SITE}/post/{p.name}</guid>\n"
                            f"      <pubDate>{pub}</pubDate>\n"
                            f"      <description>{html.escape(desc)}</description>\n    </item>"))
    items.sort(reverse=True)
    feed = ('<?xml version="1.0" encoding="UTF-8"?>\n<rss version="2.0">\n  <channel>\n'
            "    <title>XD3an Blog</title>\n"
            f"    <link>{SITE}/</link>\n"
            "    <description>XD3an 的技術部落格：AI 輔助開發、軟體架構、資安研究</description>\n"
            "    <language>zh-TW</language>\n"
            + "\n".join(i for _, i in items) + "\n  </channel>\n</rss>\n")
    (ROOT / "feed.xml").write_text(feed, encoding="utf-8")
    print(f"sitemap.xml: {len(urls)} 個網址；feed.xml: {len(items)} 篇文章")


if __name__ == "__main__":
    main()
