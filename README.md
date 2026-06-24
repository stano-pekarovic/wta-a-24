# wta-a-24
Úložisko na účely git workshopu v AjTyvIT.

## Automatizované testy

Mini PoC test suite kontroluje základnú integritu sample repozitára:

- `README.md` existuje, nie je prázdny a má nadpis.
- Vybrané sample súbory existujú a nie sú prázdne.
- Vybrané sample súbory neobsahujú merge conflict markery.

Lokálne spustenie:

```bash
make test
```
