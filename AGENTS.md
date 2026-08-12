# AGENTS

Rules for agents working in this repository.

This repository publishes Rundesk's guidance-only game design and development catalog. It teaches
portable practice across game concept, production, player experience, playtesting, gameplay
engineering, cameras, levels, 2D worlds, and supported engines. It does not run tools, generate
assets, call services, hold credentials, or replace current engine and platform documentation.

## Start here

1. Read `README.md`, then every `SKILL.md` and `references/sources.md` you will touch. Read each file
   before editing it.
2. Follow the current Rundesk `writing-skills` skill for every package. Use `researching-topics`
   before adding or changing substantive guidance. Use `python-patterns` for
   `tests/test_catalog.py`. For a release, read `RELEASING.md` and use `managing-github` release
   guidance.
3. Search this catalog before adding a package. Extend the existing owner unless the proposed skill
   has distinct triggers, decisions, workflow, and proof.
4. Verify engine and version claims against current primary sources. Treat practitioner heuristics
   as hypotheses to test with the intended players and target hardware, not universal laws.

## Portfolio boundaries

Keep game-domain judgment here and cross-route generic disciplines instead of copying them:

- `cpp-patterns` owns C++ correctness, ownership, build targets, sanitizers, and language tooling.
- `testing-code` owns automated test design; game skills add domain-specific replays, simulations,
  playtests, and proof scenes.
- `performance-engineering` owns profiling and benchmark method; game skills define representative
  workloads and frame-sensitive failure surfaces.
- `creating-design-assets` owns provider-neutral asset creation and prompting; game art skills own
  runtime-facing sprite, tile, atlas, pivot, and readability contracts.
- Engine packages such as `axmol-patterns` own engine APIs. Portable skills use pseudocode and name
  the observable contract rather than copying Unity, Unreal, Godot, or Axmol calls.

Distinguish a player/core loop (the player's recurring decision and feedback cycle) from the
runtime game loop (software scheduling). Never promise that a pattern “makes a game fun.” State the
experience hypothesis, audience, constraints, and how a prototype or playtest will test it.

## A skill is researched judgment

Teach work in execution order. Give a strong default, the condition for deviating, the failure a
trap causes, its preferred replacement, and observable proof. A good/bad pair is traceable evidence,
not an invented slogan.

Every touched package has `references/sources.md`. Use a mixed evidence base appropriate to the
claim:

- primary specifications, official engine documentation, source, releases, and platform guidance;
- original research with method and limitations;
- named practitioner material with scope and context;
- maintainer issues or reproducible failures that establish a real trap.

Separate what a source states from this catalog's conclusion. Label weak or context-specific
evidence as a heuristic. Do not publish private project names, customer information, secrets,
absolute owner paths, or first-hand evidence that has not been anonymized.

## Package contract

```text
skills/<name>/
├── SKILL.md
├── references/sources.md
├── references/<focused-topic>.md   optional
└── assets/                         optional, only when the skill consumes them
```

- `SKILL.md` frontmatter contains only `name` and `description`.
- The directory and frontmatter name match and use lowercase letters, digits, and single hyphens.
- Put all routing triggers in the description; keep it within 1,024 characters.
- Keep `SKILL.md` below 500 lines. Put conditional depth one level down and link it with the exact
  condition for reading it.
- Do not add package READMEs, changelogs, empty directories, scripts, executables, network calls,
  credentials, or provider-specific agent metadata.
- Adapted work retains its license and records the exact upstream commit and modifications in
  `THIRD_PARTY_NOTICES.md`.

## Keep the catalog synchronized

Adding, removing, or renaming a skill updates `manifest.json`, `README.md`, and
`tests/test_catalog.py` in the same change. The manifest's legacy `skills` index, package
directories, frontmatter names, and README list must agree.

Before shipping a substantial new skill, forward-test it against a realistic raw game task without
giving the evaluator the expected answer. Check routing, decision quality, traps, cross-skill
composition, and proof—not only formatting.

## Ask first

- Add an executable, script, service adapter, credential, dependency, or network behavior.
- Delete a package or file outside the immediate task.
- Commit, tag, release, or push.
- Modify this file after the repository's initial creation.

## Validate

```sh
python3 -m unittest discover -s tests -v
```

Completion requires a discovered passing suite, clean link and whitespace checks, required review,
and green CI. Report any governing skill or source link that could not be loaded or verified.
