# Exporttype: MXL-download

Contract voor het **mxl**-exporttype: downloadlink naar MusicXML (`.mxl`) voor
bewerking in MuseScore of als fallback voor Coria.

---

## Samenvatting

Exporttype **mxl** plaatst een link in de samenstelling waarmee de lezer een
`.mxl`-bestand kan downloaden. Het bestand moet vooraf zijn gegenereerd via
[conversie-vsa-musicxml](conversie-vsa-musicxml.md) en bereikbaar op de
gepubliceerde site staan. De build **genereert geen** MXL tijdens export-resolve.

---

## Beoogde doelen

- **Bewerking** in MuseScore of andere MusicXML-editor
- Archief / uitwisseling met musici
- Optionele download naast Coria (online profiel)
- **Niet:** inline notatie op papier (→ [svg](exporttype-svg.md))

---

## Authoring

### Doelsyntax (gepland)

```markdown
:::include mxl "praktijk/zondagen/tropaar-zondag-toon-3.vsa" label="Download MusicXML":::
```

### Huidige stand

`:::include mxl` is **nog niet geïmplementeerd** in `markdown_include.py`.
URL-afleiding bestaat wel in `content_assets.resolve_asset(…, channel="mxl")`.
Tot implementatie: handmatige link naar gepubliceerde MXL of wachten op Spoor B.

---

## Parameters

### `pad` (eerste argument)

| Veld                   | Waarde                                                     |
| ---------------------- | ---------------------------------------------------------- |
| **Verplicht?**         | Ja                                                         |
| **Type**               | Relatief pad naar `.vsa`                                   |
| **Doel**               | Afleiden public URL `{prefix}/{relatief-pad-met-.mxl}`     |
| **Toegestane waarden** | Bestaand `.vsa` onder content-root                         |
| **Verboden**           | Ontbrekend `.vsa`, pad buiten content-root                 |
| **Effect**             | Link wijst naar `/vsa/mxl/…/melodie.mxl` (default prefix)  |
| **Voorbeeld**          | `"praktijk/melodie.vsa"` → `/vsa/mxl/praktijk/melodie.mxl` |

### `label`

| Veld                   | Waarde                                                  |
| ---------------------- | ------------------------------------------------------- |
| **Verplicht?**         | Nee                                                     |
| **Type**               | String: `label="…"`                                     |
| **Standaard**          | TBD bij implementatie (voorstel: `"Download MusicXML"`) |
| **Doel**               | Linktekst voor download                                 |
| **Toegestane waarden** | Willekeurige tekst                                      |
| **Effect**             | `<a download>` of Hugo shortcode (implementatiedetail)  |

---

## Inputs

| Input            | Vereist?     | Opmerking                                                               |
| ---------------- | ------------ | ----------------------------------------------------------------------- |
| `.vsa`           | Ja           | Anker voor URL-afleiding                                                |
| `.mxl` afgeleide | Ja (runtime) | Moet fysiek op static staan; build kopieert nog niet overal automatisch |

Sibling-conventie: `melodie.mxl` hoort bij `melodie.vsa` (zelfde stem, andere extensie).

---

## Validatie vóór export

| Check                    | Moment  | Blokkeert?                 |
| ------------------------ | ------- | -------------------------- |
| `.vsa` bestaat           | resolve | Ja                         |
| Pad onder content-root   | resolve | Ja                         |
| `.mxl` bestaat op schijf | —       | **Nee** (huidige resolver) |
| MXL well-formed          | —       | **Nee** bij export         |

!!! warning "Runtime vs. build"
    Build kan slagen terwijl download 404 geeft als MXL niet is gegenereerd en
    gekopieerd. CI moet conversie + static deploy afdwingen (TBD).

---

## Build-gedrag

**Gepland:** zelfde fase als `:::coria` — na includes, vóór VSA-SVG-render.

Resolver (`resolve_asset`, channel `mxl`):

- Berekent public URL; **kopieert geen** bestand (anders dan coria-html)
- Emitteert Hugo shortcode (TBD: `{{< mxl-download >}}` of generieke link)

MXL-generatie: altijd via `vsa musicxml`, niet via export-pass.

---

## Output

| Profiel   | Eindgebruiker                        |
| --------- | ------------------------------------ |
| Bewerking | Download `.mxl`, open in MuseScore   |
| Online    | Optionele extra link naast svg/coria |

---

## Geschikt / niet geschikt

| Geschikt                    | Niet geschikt                       |
| --------------------------- | ----------------------------------- |
| MuseScore-bewerking         | Pixel-perfect afdruk van VSA-glyphs |
| Muzikale analyse buiten VSA | Inline weergave in liturgieboek     |

---

## Fouten en oplossingen

| Probleem                    | Oorzaak                          | Oplossing                                   |
| --------------------------- | -------------------------------- | ------------------------------------------- |
| 404 op download             | MXL niet in static               | `vsa musicxml` draaien; CI kopieerstap      |
| Verkeerde toonsoort in MXL  | Verkeerd exportprofiel conversie | `--profile` bij musicxml (zie conversiedoc) |
| `Verwacht een .vsa-bestand` | Pad naar `.mxl` i.p.v. `.vsa`    | Eerste argument moet `.vsa` zijn            |
| Link werkt lokaal niet      | Hugo `baseURL`                   | Preview via `hugo server` met juiste static |

---

## Open punten (TBD)

- Implementatie `:::include mxl` + Hugo shortcode
- Build-kopie `.mxl` → `static/vsa/mxl/…`
- Validatie dat MXL bestaat vóór build (fail fast)
- `label`-default en toegankelijkheid (bestandsgrootte, icoon)

---

## Gerelateerd

- [Conversie vsa musicxml](conversie-vsa-musicxml.md)
- [Exporttype coria](exporttype-coria.md) (deelt MXL-URL)
