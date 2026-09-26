# codeonym docs

The source of [docs.codeonym.work](https://docs.codeonym.work/), the hub of codeonym's project
docs, built with Sphinx and the Shibuya theme on Read the Docs.

Each project keeps its own docs in its repository and is added as a Read the Docs subproject of
this one, served at `docs.codeonym.work/projects/<name>/`. To list a new project, add it to
`docs/index.md`.

Preview locally:

```sh
uv run --with-requirements requirements.txt sphinx-build -W -b dirhtml docs docs/_build/html
```
