# Rundesk Game Development Skills

Rundesk's guidance-only catalog for designing, planning, building, testing, and polishing games.
The skills are engine-neutral unless a package names an engine explicitly, and they are designed to
compose with Rundesk's general C++, testing, performance, research, and asset-creation skills.

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

Removing a catalog revokes its grants. When migrating an agent from the general catalog, install
this catalog and grant the corresponding `rundesk-skills-gamedev/<skill>` before revoking the old
grant.

## Included skills

- `axmol-patterns` — version-aware Axmol ownership, scenes, input, graphics, builds, and migration.
- `building-isometric-worlds` — projection, coordinates, elevation, picking, depth, and visibility.
- `building-tile-based-worlds` — grids, connectivity, autotiling, footprints, edits, and dirty data.
- `creating-2d-game-art` — runtime-ready sprites, tiles, modular kits, atlases, and art validation.
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

Generic language and operational concerns remain in
[`rundesk-skills`](https://github.com/rundesk-ai/rundesk-skills): use `cpp-patterns` for C++,
`testing-code` for automated correctness, `performance-engineering` for profiling and benchmarks,
and `creating-design-assets` for provider-neutral asset creation.

## Manifest contract

`manifest.json` supplies the catalog name and version. Rundesk discovers packages under `skills/`;
the repository also checks its maintained `skills` index and this README against the filesystem.
See [RELEASING.md](RELEASING.md) for publication.
