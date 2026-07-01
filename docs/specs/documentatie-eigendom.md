# Documentatie-eigendom (orthodox-groningen)

**Status:** normatief (juni 2026).

Voorkomt dubbele, uit elkaar lopende specificaties tussen repository's.

---

## Waar hoort wat?

| Type documentatie                     | Canonieke repo         | Voorbeelden                                                                                                                                                                                                |
| ------------------------------------- | ---------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Organisatie-breed, tool-onafhankelijk | **`bron`**             | [terminologie.md](terminologie.md), [inhoudslevenscyclus.md](inhoudslevenscyclus.md), [zangstuk-formaat.md](zangstuk-formaat.md), [parochie-lokaal zangstukken](../manuals/parochie-lokaal-zangstukken.md) |
| Tool-specifiek (VSA)                  | **VSA-tooling**        | VSA-syntax, parser, SVG-rendering, Hugo-demo build                                                                                                                                                         |
| Toekomstige andere tool               | **eigen tool-repo**    | Alleen wat bij die tool hoort; link naar `bron` voor gedeelde termen                                                                                                                                       |
| Parochie-inhoud                       | **parochie Hugo-repo** | Samenstellingen, `lokaal/` — **geen** normatieve specs dupliceren                                                                                                                                          |

---

## Regels

| Regel                    | Inhoud                                                                                                                   |
| ------------------------ | ------------------------------------------------------------------------------------------------------------------------ |
| **D1 — één bron**        | Normatieve org-specs staan **alleen** in `bron/docs/`. Andere repo's: **link**, geen volledige kopie.                    |
| **D2 — stub toegestaan** | Een korte stub (≤ ~30 regels) met link naar `bron` is oké voor discoverability in een tool-repo.                         |
| **D3 — wijzigingspad**   | Wijzig org-brede specs via PR op `bron`; daarna stubs/links in andere repo's controleren.                                |
| **D4 — terminologie**    | [terminologie.md](terminologie.md) §0 (R1–R5) geldt overal; zie ook `.cursor/rules/orthodox-groningen-terminologie.mdc`. |

---

## Cursor-regel (alle org-repo's)

Elke repository onder `github.com/orthodox-groningen` hoort het bestand `.cursor/rules/orthodox-groningen-terminologie.mdc` **in git** te hebben (zelfde inhoud).

---

## Gerelateerd

- [Specificaties — index](index.md)
- [Terminologie](terminologie.md)
- [VSA-tooling](https://github.com/orthodox-groningen/VSA-tooling) — tool-specifieke documentatie
