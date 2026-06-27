# Exportcontracten

Referentie voor **exportmechanismen**: hoe afgeleide in een samenstelling worden
ontsloten. Authoring-syntax leeft in
[VSA-tooling](https://github.com/orthodox-groningen/VSA-tooling/blob/main/docs/spec-vsa-document-samenstellen.md).

Export is **geen** conversie: export verwijst naar reeds (of tijdens build) gegenereerde
afgeleide, of naar handmatige siblings.

---

## embed `svg`

| Veld | Waarde |
| ---- | ------ |
| **Exporttype in markdown** | `:::include svg "pad/melodie.vsa"` of `:::include melodie.vsa` |
| **Benodigde input** | `.vsa`-bron; afgeleide `.svg` |
| **Eisen** | VSA gevalideerd; SVG gegenereerd (`vsa svg` of build-markdown) |
| **Uitvoer** | `<img>` / Hugo shortcode in HTML |
| **Uitgaveprofielen** | Afdruk, Online |
| **Niet geschikt voor** | Bewerking in MuseScore |

---

## `coria`

| Veld | Waarde |
| ---- | ------ |
| **Exporttype** | `:::include coria "pad/melodie.vsa"` |
| **Benodigde input** | `.vsa`-bron; **of** `{stem}.coria.html` sibling **of** afgeleide `.mxl` |
| **Eisen** | HTML-sibling: partij al gekozen; MXL-fallback: Coria `play_from_url` |
| **Uitvoer** | Link naar Coria HTML of Coria-speler |
| **Uitgaveprofielen** | Online |
| **Niet geschikt voor** | Afdruk (verberg via CSS `.coria-play`) |

---

## `mxl` (download)

| Veld | Waarde |
| ---- | ------ |
| **Exporttype** | `:::include mxl "pad/melodie.vsa"` |
| **Benodigde input** | Afgeleide `.mxl` |
| **Eisen** | `vsa musicxml` gedraaid; bestand bereikbaar op gepubliceerde URL |
| **Uitvoer** | Download-link |
| **Uitgaveprofielen** | Bewerking, Online (optioneel) |
| **Niet geschikt voor** | Inline print |

---

## Handmatige siblings

| Bestand | Rol |
| ------- | --- |
| `{stem}.coria.html` | Coria-export met gekozen partij; naast `.vsa` in content-source |

In de bron-repo primair VSA + scans; Coria-HTML kan in parochie-build content voorkomen.
