# SOURCE MAP — Gdańsk Komunikaty (gdansk_komunikaty)

**Feed:** https://www.gdansk.pl/subpages/rss/komunikaty_rss.xml  
**Channel title:** Komunikaty www.gdansk.pl  
**Update:** hourly (sy:updatePeriod=hourly, Frequency=1)  
**Lang:** pl

## Поля item → нормализация
- title          ← `<title>` (строка, как есть)
- link           ← `<link>` (канонический URL; использовать и как `guid` при дедупе)
- guid           ← если есть `<guid>` (в данном фиде отсутствует) → использовать `link`
- summary        ← пусто (в этом фиде `<description/>` часто пустой)
- published_ts   ← `<pubDate>` (parse RFC-822, TZ +0200)
- source         ← "gdansk.pl/komunikaty"
- image_url      ← `null` (нет media)
- category       ← "komunikaty"

## Наблюдения и особенности
- Многие записи — обвieszczenia, zawiadomienia и powiadomienia (юридически значимые оголошения).
- Нет изображений; постим как текст.
- Формулировки длинные: возможно понадобится усечение заголовков/описания при форматировании.

## Риски и проверки
- Дубли: использовать `link` как уникальный ключ (UNIQUE в БД).
- Даты всегда есть (pubDate). Если нет — ставить `now()` и помечать `ts_inferred=true`.
