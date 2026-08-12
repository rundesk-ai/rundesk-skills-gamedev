# Rundesk Game Development Skills

Rundesk's guidance-only catalog for designing, planning, building, testing, and polishing games.
The skills are engine-neutral unless a package names an engine explicitly. The catalog includes its
C++ guidance and composes with Rundesk's general testing, performance, research, and asset-creation
skills.

## Install with Rundesk CLI

Rundesk CLI is the default installation path. It manages catalog updates, the
`rundesk-skills-gamedev` namespace, and per-agent grants.

```sh
rundesk skills install https://github.com/rundesk-ai/rundesk-skills-gamedev
rundesk skills install https://github.com/rundesk-ai/rundesk-skills-gamedev --confirm
rundesk skills grant <agent> rundesk-skills-gamedev/designing-games
```

Installation previews until `--confirm`, installs the complete catalog, and grants no skill
automatically. Skills are addressed as `<catalog>/<skill>`.

```sh
rundesk skills catalogs
rundesk skills update rundesk-skills-gamedev
rundesk skills update rundesk-skills-gamedev --confirm
rundesk skills remove rundesk-skills-gamedev
rundesk skills remove rundesk-skills-gamedev --confirm
```

Removing a catalog revokes its grants. When migrating a same-named game or C++ skill from the core
catalog, install this catalog first; then revoke the agent's old core grant and immediately grant the
corresponding `rundesk-skills-gamedev/<skill>`. One agent cannot hold both under the same grant name.
Use `--as <name>` only if a temporary alias is intentionally needed.

## Use without Rundesk

Rundesk is not required. Copy or symlink any complete directory under `skills/`; keep its
`references/` and other package files beside `SKILL.md`.

For Codex, use `.agents/skills/` in a game repository or `~/.agents/skills/` for personal use. For
Claude Code, use `.claude/skills/` in a project or `~/.claude/skills/` for personal use. Restart or
begin a new session if the agent does not detect a newly copied skill.

```sh
# Codex project skills
mkdir -p .agents/skills
cp -R /path/to/rundesk-skills-gamedev/skills/designing-games .agents/skills/
cp -R /path/to/rundesk-skills-gamedev/skills/programming-gameplay .agents/skills/

# Claude Code project skills
mkdir -p .claude/skills
cp -R /path/to/rundesk-skills-gamedev/skills/designing-games .claude/skills/
cp -R /path/to/rundesk-skills-gamedev/skills/programming-gameplay .claude/skills/
```

Install companion skills from another Rundesk catalog the same way when a package routes to them,
such as `testing-code`, `performance-engineering`, or `creating-design-assets`. Review an existing
same-name destination before replacing it so an update cannot retain stale package files.

## Included skills

- `axmol-patterns` — version-aware Axmol ownership, scenes, input, graphics, builds, and migration.
- `building-isometric-worlds` — projection, coordinates, elevation, picking, depth, and visibility.
- `building-tile-based-worlds` — grids, connectivity, autotiling, footprints, edits, and dirty data.
- `creating-2d-game-art` — runtime-ready sprites, tiles, modular kits, atlases, and art validation.
- `cpp-patterns` — modern C++ ownership, undefined behavior, organization, CMake, tools, and proof.
- `designing-game-cameras-and-controls` — views, framing, camera behavior, action semantics, and comfort.
- `designing-game-levels` — metrics, blockouts, spatial guidance, encounters, and pacing.
- `designing-games` — player promise, experience hypotheses, core loops, rules, progression, and balance.
- `designing-player-experience` — onboarding, feedback, HUDs, difficulty options, and accessibility.
- `engineering-2d-rendering` — render snapshots, spaces, layers, culling, batching, pixels, and proof.
- `planning-game-production` — prototypes, vertical slices, scope, risks, milestones, and content planning.
- `playtesting-games` — player-research hypotheses, sessions, measures, analysis, and iteration.
- `programming-gameplay` — runtime loops, state, input handoff, time, determinism, replays, and saves.

## How the portfolio composes

Start with `designing-games` to define the intended experience and recurring player decisions. Use
`planning-game-production` to prove the riskiest assumptions before scaling production, and
`playtesting-games` to learn from representative players. Add the relevant craft and engineering
skills for cameras, levels, player experience, runtime architecture, 2D worlds, art, rendering, or
Axmol.

Use `cpp-patterns` alongside `programming-gameplay` for C++ games and alongside `axmol-patterns` for
Axmol projects. Other cross-cutting concerns remain in
[`rundesk-skills`](https://github.com/rundesk-ai/rundesk-skills): use `testing-code` for automated
correctness, `performance-engineering` for profiling and benchmarks, and `creating-design-assets`
for provider-neutral asset creation.

## Manifest contract

`manifest.json` supplies the catalog name and version. Rundesk discovers packages under `skills/`;
the repository also checks its maintained `skills` index and this README against the filesystem.
See [RELEASING.md](RELEASING.md) for publication.

## Rundesk Skills collection

| Catalog | Purpose |
|---|---|
| [rundesk-skills](https://github.com/rundesk-ai/rundesk-skills) | General guidance and software-development workflows |
| [rundesk-skills-gamedev](https://github.com/rundesk-ai/rundesk-skills-gamedev) | Game design, production, C++, 2D systems, and Axmol |
| [rundesk-skills-apple](https://github.com/rundesk-ai/rundesk-skills-apple) | Guarded local Apple integrations for macOS |
| [rundesk-skills-integrations](https://github.com/rundesk-ai/rundesk-skills-integrations) | Guarded service integration CLIs |

Standalone layout details: [Codex skills](https://learn.chatgpt.com/docs/build-skills) and
[Claude Code skills](https://code.claude.com/docs/en/slash-commands).
