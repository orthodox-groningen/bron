# Schrijfconventies

Richtlijnen voor alle documentatie in de `bron`-repository en verwante specs
(VSA-tooling). Doel: een lezer zonder volledige voorkennis kan documenten
zelfstandig volgen.

---

## Algemene stijl

**Compleet en begrijpelijk gaat boven compact.**

Per concept expliciet maken:

| Vraag                 | Wat de lezer moet kunnen vinden                     |
| --------------------- | --------------------------------------------------- |
| Waarvoor?             | Doel, gebruikersscenario, uitgaveprofiel            |
| Wat gebeurt er?       | Tool, pipeline-moment, input → output               |
| Effect van waarden    | Wat verandert bij keuze A vs. B                     |
| Toegestaan / verboden | Lijsten, voorbeelden fout vs. goed                  |
| Standaard             | Gedrag als een parameter ontbreekt                  |
| Fouten                | Concrete melding, oorzaak, oplossing                |
| TBD                   | Open punten expliciet — geen stilzwijgende aannames |

Gebruik korte alinea’s, genummerde stappen waar een workflow wordt beschreven,
en admonitions (`!!! note`, `!!! warning`) voor uitzonderingen.

---

## Markdown-tabellen

Kolommen **aligneren in de bron**: cellen in dezelfde kolom even breed (spatiëring
met spaties). Separator-regel per cel: spatie + `---` + alignment + spatie.

Voorbeeld:

```markdown
| Parameter | Verplicht? | Standaard       |
| --------- | ---------- | --------------- |
| `alt`     | Nee        | `"VSA notatie"` |
| `scale`   | Nee        | geen schaling   |
```

Dezelfde regel geldt voor Cursor-agents via `.cursor/rules/markdown-table-layout.mdc`
(in deze repo en in VSA-tooling). Bulk formatteren:
`python scripts/align_markdown_tables.py docs/` (VSA-tooling).

---

## Contractpagina’s

Twee families met vaste structuur:

| Familie       | Overzicht                                                    | Per type                                                                                                                                                 |
| ------------- | ------------------------------------------------------------ | -------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Export**    | [Exportcontracten](../reference/exportcontracten.md)         | [exporttype-svg](../reference/exporttype-svg.md), [exporttype-coria](../reference/exporttype-coria.md), [exporttype-mxl](../reference/exporttype-mxl.md) |
| **Conversie** | [Conversiemechanismen](../reference/conversiemechanismen.md) | [conversie-vsa-svg](../reference/conversie-vsa-svg.md), [conversie-vsa-musicxml](../reference/conversie-vsa-musicxml.md)                                 |

### Parameters documenteren

Elke parameter minimaal met: naam, verplicht?, type, standaard, doel, toegestane
waarden, verboden waarden, effect per waarde, interactie met andere parameters,
voorbeeld (geldig; waar zinvol ook ongeldig met verwachte fout).

---

## Taal en terminologie

| Term          | Gebruik                                                                              |
| ------------- | ------------------------------------------------------------------------------------ |
| **Conversie** | Tool met vaste I/O (`vsa svg`, `vsa musicxml`)                                       |
| **Export**    | Hoe afgeleide in een samenstelling verschijnt (`:::include svg\|coria\|mxl`)         |
| **Kanaal**    | Verouderd — gebruik *conversie* of *exporttype*                                      |

Cross-links naar implementatie in
[VSA-tooling](https://github.com/orthodox-groningen/VSA-tooling) waar relevant;
normatieve contracten staan in `bron/docs/reference/`.

---

## MkDocs

- Nederlandse prose; code en paden in monospace
- Mermaid-diagrammen voor ketens en pipeline-fases
- `mkdocs build --strict` moet slagen vóór merge
