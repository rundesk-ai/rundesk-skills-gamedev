# Rundesk Game Development Skills

Rundesk's guidance-only catalog for designing, planning, building, testing, and polishing games.
Skills are engine-neutral unless a package names an engine explicitly. The catalog owns its C++
guidance and composes with Rundesk's general testing, performance, research, and asset-creation
skills.

## Skills

- `axmol-patterns` — version-aware Axmol ownership, scenes, input, graphics, builds, and migration.
- `building-isometric-worlds` — projection, coordinates, elevation, picking, depth, and visibility.
- `building-tile-based-worlds` — grids, connectivity, autotiling, footprints, edits, and dirty data.
- `creating-2d-game-art` — runtime-ready sprites, tiles, modular kits, atlases, and art validation.
- `cpp-patterns` — modern C++ ownership, undefined behavior, organization, CMake, tools, and proof.
- `designing-game-cameras-and-controls` — views, framing, behavior, action semantics, and comfort.
- `designing-game-levels` — metrics, blockouts, spatial guidance, encounters, and pacing.
- `designing-games` — player promise, experience hypotheses, core loops, rules, progression, and balance.
- `designing-player-experience` — onboarding, feedback, HUDs, difficulty options, and accessibility.
- `designing-systemic-management-games` — constraints, indirect control, crises, recovery, and loops.
- `engineering-2d-rendering` — render snapshots, spaces, layers, culling, batching, pixels, and proof.
- `engineering-game-animation` — semantic states, transitions, authority, events, and runtime proof.
- `engineering-world-simulations` — causal layers, deterministic updates, fidelity, and invariants.
- `generating-game-worlds` — seeded pipelines, constraints, repair, seed sweeps, and multiscale proof.
- `planning-game-production` — prototypes, vertical slices, scope, risks, milestones, and content plans.
- `playtesting-games` — player-research hypotheses, sessions, measures, analysis, and iteration.
- `programming-gameplay` — runtime loops, state, input handoff, time, determinism, replays, and saves.

## Install

Rundesk previews a catalog before changing the install. Review the preview, confirm it, then grant
only the skills an agent needs:

```sh
rundesk skills install https://github.com/rundesk-ai/rundesk-skills-gamedev
rundesk skills install https://github.com/rundesk-ai/rundesk-skills-gamedev --confirm
rundesk skills grant ava rundesk-skills-gamedev/designing-games
```

Installation adds the complete catalog and grants no skills automatically. Its namespace owns later
lifecycle commands:

```sh
rundesk skills catalogs
rundesk skills update rundesk-skills-gamedev
rundesk skills update rundesk-skills-gamedev --confirm
rundesk skills remove rundesk-skills-gamedev
rundesk skills remove rundesk-skills-gamedev --confirm
```

Removing a catalog revokes every grant from that catalog.

## Requirements

- The catalog is public and installs from its GitHub repository with the current Rundesk CLI.
- Packages are guidance-only and require no catalog runtime, credentials, dependencies, or network
  access. Engine-specific skills document the versions and tools relevant to their guidance.
- Rundesk is optional. Copy or symlink a complete package, including its references and assets, into
  a provider's supported skill directory. For Codex use `.agents/skills/`; for Claude Code use
  `.claude/skills/`. Review an existing same-name destination before replacing it.
- Install companion skills from
  [`rundesk-skills`](https://github.com/rundesk-ai/rundesk-skills) when a workflow needs generic
  automated testing, performance engineering, research, or provider-neutral asset creation.
- One agent cannot hold two grants with the same name. During a migration from the general catalog,
  install this catalog first, then revoke and re-grant each affected skill; use `--as <name>` only
  for a deliberate alias.

Use `designing-games` to define the experience and recurring player decisions,
`planning-game-production` to prove risky assumptions before scaling, and `playtesting-games` to
learn from representative players. Add craft and engineering skills for the game's actual systems,
engine, and production risks.

## Repository layout

```text
.
├── .github/
│   ├── ISSUE_TEMPLATE/
│   ├── pull_request_template.md
│   └── workflows/
├── skills/<name>/
│   ├── SKILL.md
│   ├── references/sources.md
│   ├── references/<topic>.md       optional
│   └── assets/                     optional, only when consumed
├── tests/test_catalog.py
├── AGENTS.md
├── CLAUDE.md
├── README.md
├── RELEASING.md
├── THIRD_PARTY_NOTICES.md          required when adapted work exists
├── LICENSE
└── manifest.json
```

`manifest.json` supplies the published catalog name and version. Rundesk discovers packages under
`skills/`; the repository's legacy manifest `skills` index remains intentionally maintained and
must match package directories, frontmatter names, and this README.

## Development

Read [AGENTS.md](AGENTS.md) before changing the repository. The complete offline gate is:

```sh
python3 -m unittest discover -s tests -v
git diff --check
```

The suite requires Python 3.9+ and checks manifest, package, README, links, privacy boundaries,
release automation, contributor templates, and guide contracts. A substantial skill change also
requires current source verification and a realistic raw-game-task forward test covering routing,
decisions, traps, cross-skill composition, and proof.

## Creating a skill catalog

Use the
[canonical skill-catalog guide](https://github.com/rundesk-ai/rundesk-cli/blob/main/docs/catalogs.md)
for catalog boundaries, manifests, package layout, installation, and validation.

This catalog's skills are researched judgment, not condensed manuals. Every package keeps
`references/sources.md`, uses a mixed evidence base, distinguishes sourced facts from heuristics and
catalog conclusions, and keeps conditional depth in focused references. Frontmatter contains only
`name` and `description`; routing belongs in the description, and `SKILL.md` stays below 500 lines.
No scripts, executables, credentials, services, dependencies, network calls, or provider-specific
agent metadata belong here.

## Contributing

Use the repository templates to keep reports bounded and reviewable:

- [Report a reproducible bug](.github/ISSUE_TEMPLATE/bug-report.md)
- [Propose a change](.github/ISSUE_TEMPLATE/change-proposal.md)
- [Prepare a pull request](.github/pull_request_template.md)

Search before adding a skill, keep public documentation synchronized with package changes, and
include exact validation evidence. Never publish credentials, personal or customer identifiers,
private-project language, private evidence, or owner-specific paths. Adapted work must retain its
license and record its exact upstream commit and modifications in `THIRD_PARTY_NOTICES.md`.

## Releases

Published skill content and behavior changes follow [RELEASING.md](RELEASING.md) and its semantic
version policy. Repository-process-only changes to agent guides, contributor templates, or tests
that enforce those files do not require a manifest version bump. Rundesk compares catalog content,
not only the version, when deciding whether an installed tree changed.

## License

This catalog is available under the [MIT License](LICENSE). Adapted packages remain subject to their
retained upstream licenses and any notices recorded in `THIRD_PARTY_NOTICES.md`.
