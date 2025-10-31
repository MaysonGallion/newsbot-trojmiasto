# SOURCE_MAP: gdansk_wiadomosci

RSS URL: https://www.gdansk.pl/subpages/rss/wiadomosci_rss.xml
Item → NewsItem:
- title            ← <title>
- link (unique)    ← <link> (fallback: <guid>)
- published_ts     ← <pubDate> (RFC822, tz +0200)
- summary_raw      ← <description> (CDATA, HTML)
- image_url        ← первый <img> src в description или content:encoded
- source           = "Gdańsk.pl"
- source_domain    = "gdansk.pl"
- lang             = "PL"

Особенности:
- description/content:encoded дублируются; достаточно одного.
- Картинка всегда 150×100 (минимум); доступны более крупные версии по пути /download/....
- Часовой пояс: Europe/Warsaw (+01/+02).
- Частота обновления: hourly (по каналу).
