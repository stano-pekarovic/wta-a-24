# Test Data — počasie

Sample testovacie JSON dáta o počasí. Slúžia na vývoj a testovanie, **nie sú reálne namerané hodnoty**.

## Štruktúra

```
test-data/
├── current/      ← aktuálne počasie, 1 súbor per mesto
│   ├── bratislava.json
│   ├── kosice.json
│   └── poprad.json
└── forecast/     ← predpovede
    ├── bratislava-5day.json   (denná predpoveď, 5 dní)
    └── kosice-hourly.json     (hodinová predpoveď)
```

## Schémy

### current/*.json
| pole | typ | popis |
|------|-----|-------|
| `city`, `country` | string | mesto, ISO kód krajiny |
| `coord` | object | `lat`, `lon` |
| `observed_at` | ISO 8601 | čas merania (UTC) |
| `weather` | object | `condition`, `description`, `icon` |
| `temperature_c`, `feels_like_c` | number | teplota / pocitová (°C) |
| `humidity_pct` | number | vlhkosť (%) |
| `pressure_hpa` | number | tlak (hPa) |
| `wind` | object | `speed_ms`, `deg`, `gust_ms` |
| `clouds_pct` | number | oblačnosť (%) |
| `visibility_m` | number | viditeľnosť (m) |
| `rain_1h_mm` | number | zrážky za 1h (mm), voliteľné |

### forecast/*-5day.json
Pole `daily[]`: `date`, `temp_min_c`, `temp_max_c`, `condition`, `humidity_pct`, `wind_speed_ms`, `pop` (pravdepodobnosť zrážok 0–1).

### forecast/*-hourly.json
Pole `hourly[]`: `time` (ISO 8601), `temp_c`, `condition`, `pop`, `wind_speed_ms`.

## Hodnoty `condition`
`Clear` · `Clouds` · `Rain` · `Thunderstorm` · `Snow` · `Mist`
