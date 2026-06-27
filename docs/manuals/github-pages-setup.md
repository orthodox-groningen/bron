# GitHub Pages — eenmalige instelling

Na de eerste succesvolle workflow-run:

1. **Repository → Settings → Pages**
2. **Build and deployment → Source:** `Deploy from a branch`
3. **Branch:** `gh-pages` / `/ (root)`

De workflow `.github/workflows/docs-pages.yml` publiceert:

| Branch | URL |
| ------ | --- |
| `main` | https://orthodox-groningen.github.io/bron/ |
| overige branches | https://orthodox-groningen.github.io/bron/preview/ |

`keep_files: true` zorgt dat production en preview elkaar niet overschrijven.

## Workflow-rechten

Onder **Settings → Actions → General → Workflow permissions** moet
**Read and write permissions** aan staan (voor `GITHUB_TOKEN` → `gh-pages`).

## Lokaal

```bash
python -m pip install -r requirements-docs.txt
python -m mkdocs serve
```
