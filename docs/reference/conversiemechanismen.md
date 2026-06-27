# Conversiemechanismen

Referentiekaarten voor geautomatiseerde conversie. Implementatie:
[VSA-tooling](https://github.com/orthodox-groningen/VSA-tooling).

Afgeleide output hoort **niet** in de `bron`-repository (zie `.gitignore`).

---

## `vsa svg`

| Veld | Waarde |
| ---- | ------ |
| **CLI** | `vsa svg <input.vsa> <output.svg>` |
| **Input** | `.vsa` (gevalideerd) |
| **Output** | `.svg` |
| **Output-locatie** | `derived/` lokaal; parochie `static/vsa/` of CI-artefact |
| **Kenmerken** | Vector; VSA-glyphs + omringende tekst; schaalbaar; geen audio |
| **Geschikt als input voor export** | embed `svg` |
| **Metadata** | optioneel frontmatter; rendering-config via VSA-tooling |
| **Trigger** | build-workflow / handmatig |

---

## `vsa musicxml`

| Veld | Waarde |
| ---- | ------ |
| **CLI** | `vsa musicxml <input.vsa> <output.mxl>` |
| **Input** | `.vsa` (gevalideerd; muziek-metadata in frontmatter aanbevolen) |
| **Output** | `.mxl` (default) of `.musicxml` |
| **Output-locatie** | `derived/` lokaal; parochie static of CI |
| **Kenmerken** | MusicXML compressed; playback- of engraving-profiel; MuseScore/Coria |
| **Geschikt als input voor export** | `coria` (via URL), `mxl` download |
| **Trigger** | build-workflow / handmatig |

Standaardprofiel: `playback`. Zie
[MusicXML-export (VSA-tooling)](https://github.com/orthodox-groningen/VSA-tooling/blob/main/docs/user/musicxml-export.md).

---

## Toekomstige conversies

| Mechanisme | Input | Output | Status |
| ---------- | ----- | ------ | ------ |
| Scan → VSA | PDF/png | `.vsa` | Niet geautomatiseerd; handmatige transcriptie |
| Audio | — | — | Nog niet gedefinieerd |

Nieuwe mechanismen krijgen dezelfde kaartstructuur voordat ze in CI worden opgenomen.
