# Codemap — rundesk-skills-gamedev

Where each part lives. Counts are of artifacts, so they survive a rename and go wrong visibly when
the tree moves on without this page.

A catalog is mostly one shape repeated: every package is a directory under `skills/` holding a
`SKILL.md` and the references it loads on demand. Nothing else in the repository is large.

## Packages (skills/ — 17, 41 reference files)

Each holds `SKILL.md` for routing and core procedure, and `references/` for detail loaded on demand.
`references/sources.md` is required in every touched package.

| Package | References | Command |
|---|---|---|
| `axmol-patterns` | 8 | — |
| `building-isometric-worlds` | 3 | — |
| `building-tile-based-worlds` | 1 | — |
| `cpp-patterns` | 8 | — |
| `creating-2d-game-art` | 2 | — |
| `designing-game-cameras-and-controls` | 1 | — |
| `designing-game-levels` | 1 | — |
| `designing-games` | 2 | — |
| `designing-player-experience` | 1 | — |
| `designing-systemic-management-games` | 1 | — |
| `engineering-2d-rendering` | 4 | — |
| `engineering-game-animation` | 1 | — |
| `engineering-world-simulations` | 1 | — |
| `generating-game-worlds` | 1 | — |
| `planning-game-production` | 2 | — |
| `playtesting-games` | 2 | — |
| `programming-gameplay` | 2 | — |

Every package is guidance only: no script, executable, credential, or network call.

## Identity (root)

| File | What it is |
|---|---|
| `manifest.json` | schema, name, version (`0.3.0`), and description |
| `README.md` | the consumer contract: what the catalog is, how to install it, and every package |
| `AGENTS.md`, `CLAUDE.md` | the repository guide, byte-identical by contract |
| `RELEASING.md` | the publication contract |

## Tests (tests/ — 1 suite)

The repository contract: the manifest and the tree agree, every package is complete and correctly
named, the README lists exactly what ships, and the guide pair stays byte-identical.

## Automation (.github/)

Issue templates, the pull-request template, and the workflow that runs the suite.

## Documentation (docs/)

`README.md`, `BRIEF.md`, and `CODEMAP.md` at the root.
