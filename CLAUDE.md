# AGENTS

Rules for every agent working in this repository. These instructions define how to work here; where
they conflict with general habits, this file wins.

## Purpose

This repository publishes Rundesk's guidance-only game design and development catalog. It teaches
portable practice across game concept, production, player experience, playtesting, gameplay
engineering, cameras, levels, 2D worlds, C++, and supported engines. It does not run tools, generate
assets, call services, hold credentials, or replace current engine and platform documentation.

`README.md` defines the public catalog and portfolio. `manifest.json` defines the published catalog
metadata and maintained package index. Each package's `SKILL.md` and references define its guidance;
`RELEASING.md` defines publication.

Use the
[canonical skill-catalog guide](https://github.com/rundesk-ai/rundesk-cli/blob/main/docs/catalogs.md)
for organization-wide catalog structure and boundaries.

## Before you work

1. Read `README.md`, this file, any applicable release documentation, and the complete contents of
   every file you may change. For skill work, also read that package's `SKILL.md` and
   `references/sources.md`.
2. Load the smallest set of available skills that applies to the task. Use the current Rundesk
   `writing-skills` guidance for skill changes and `managing-github` for pull requests or releases
   when available. Use `researching-topics` for substantive guidance research and
   `naming-grammar-conventions` for recurring or cross-layer terminology when available. If
   governing guidance is unavailable, preserve established conventions and report the limitation;
   do not invent another required skill.
3. Search this catalog before adding or renaming anything. Reuse the established term, package,
   pattern, and source of truth. Extend the existing owner unless a proposed skill has distinct
   triggers, decisions, workflow, and proof.
4. Inspect the worktree before editing. Preserve unrelated work and coordinate overlapping changes.
5. Verify engine and version claims against current primary sources. Treat practitioner heuristics
   as hypotheses to test with intended players and target hardware, not universal laws.
6. Investigate an owner's concern before contradicting it. Bring evidence, not a hunch.

## Repository layout

```text
.
├── .github/
│   ├── ISSUE_TEMPLATE/
│   │   ├── bug-report.md
│   │   └── change-proposal.md
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
└── manifest.json
```

`AGENTS.md` and `CLAUDE.md` are the same repository guide and must remain byte-identical. Do not add
empty optional directories or package-level READMEs, changelogs, installation guides, or creation
diaries.

## Package and artifact contract

- Keep each package entirely under `skills/<name>/` so a catalog update replaces it atomically.
- Every package contains `SKILL.md` and `references/sources.md`.
- `SKILL.md` frontmatter contains only `name` and `description`.
- The directory and frontmatter `name` match and use lowercase letters, digits, and single hyphens;
  names are at most 64 characters.
- The manifest contract is `schema`, `name`, `version`, and `description`. Rundesk discovers
  `skills/<name>/SKILL.md` from the tree.
- This repository retains a legacy manifest `skills` index that the CLI ignores but the catalog
  tests require. Keep it aligned with package directories, frontmatter names, and the README list
  until an approved migration removes it.
- No script, executable, `rundesk.json`, service, dependency, credential, network call, or
  provider-specific agent metadata belongs in this guidance-only catalog.

## Safety and approval gates

Get explicit approval before you:

- add executable, service, credential, dependency, or network behavior;
- delete a package or any file outside the immediate task;
- change a public contract, compatibility boundary, version, tag, or release;
- commit, push, publish, deploy, or modify repository settings; or
- modify this guide outside an authorized guide-maintenance task.

The current request may supply one or more of those approvals; never expand it beyond its stated
scope. Never publish secrets, personal or customer identifiers, private-project language,
owner-specific paths, private first-hand evidence, debug material, generated filler, unsupported
claims, or dropped attribution. Do not reset, overwrite, force-push, or otherwise undo shared work.
Keep validation offline except for explicit source and link checks. Never claim a test, review, or
source verification that you did not observe.

## Delegation

Delegate only bounded work with explicit file ownership, constraints, and observable completion
criteria. Assign non-overlapping scopes and tell collaborators not to revert or overwrite other
work. Delegation never expands the request's authority. The parent remains responsible for
decisions, integration, full-diff review, validation, privacy, and the final result. Never treat
delegated output as proof until the parent verifies it.

## Architecture and conventions

Keep game-domain judgment here and cross-route generic disciplines instead of copying them:

- `cpp-patterns` owns C++ correctness, ownership, build targets, sanitizers, and language tooling.
- `testing-code` owns generic automated test design; game skills add domain-specific replays,
  simulations, playtests, and proof scenes.
- `performance-engineering` owns profiling and benchmark method; game skills define representative
  workloads and frame-sensitive failure surfaces.
- `creating-design-assets` owns provider-neutral asset creation and prompting; game art skills own
  runtime-facing sprite, tile, atlas, pivot, and readability contracts.
- Engine packages such as `axmol-patterns` own engine APIs. Portable skills use pseudocode and name
  the observable contract instead of copying engine calls.

Distinguish a player/core loop, the player's recurring decision and feedback cycle, from the runtime
game loop, the software scheduler. Never promise that a pattern makes a game fun. State the intended
experience, audience, constraints, and how a prototype or playtest will test the hypothesis.

A skill is researched judgment. Teach work in execution order. Give a strong default, the condition
for deviating, the failure a trap causes, the preferred replacement, and observable proof. Good/bad
pairs must come from traceable evidence, not invented slogans.

Route precisely and spend context once:

- Make `description` the complete routing instruction because the body is unavailable until the
  skill triggers. Name direct and indirect goals and exclude only likely near-misses. Keep it within
  1,024 characters.
- Keep core steps, defaults, and gotchas in `SKILL.md`. Keep it below 500 lines.
- Put conditional depth and larger examples in focused references one level down. Link each
  reference from `SKILL.md` with the exact condition for reading it.
- Keep one source of truth per instruction. Do not add a table of contents that repeats headings or
  duplicate guidance across packages.

## Documentation duties

Research before drafting technical claims. Every touched `references/sources.md` must cite the
specific source and state what it establishes. Use a mixed evidence base appropriate to the claim:

- primary specifications, official engine documentation, source, releases, and platform guidance;
- original research with author, date, method, sample, and limitations;
- named practitioner material with scope and context; and
- maintainer issues or reproducible failures that establish a real trap.

Separate source statements from catalog conclusions. Label weak or context-specific evidence as a
heuristic, quote only when exact wording matters, and verify every relied-on link. Anonymize and
scope recorded experience.

Adding, removing, or renaming a skill updates `manifest.json`, `README.md`, and
`tests/test_catalog.py` together. Adapted work retains its license and records the exact upstream
commit and modifications in `THIRD_PARTY_NOTICES.md`. Update `RELEASING.md` when the release process
changes. Keep all public documentation true in the same change as the behavior or contract it
describes.

## Build, test, and run

Run the offline Python 3.9+ catalog suite:

```sh
python3 -m unittest discover -s tests -v
```

Run the full suite after every change and record the exact command, discovered test count, and
result. Also run `git diff --check`, verify local links and every changed external source link, and
inspect the final diff for privacy and package-boundary failures.

Before shipping a substantial new or changed skill, forward-test it against a realistic raw game
task without giving the evaluator the expected answer. Check routing, decision quality, traps,
cross-skill composition, and proof, not only formatting.

## Pull requests and releases

Use `.github/pull_request_template.md` for every pull request. Preserve its headings and checklists.
Fill it with exact commands and observed results from the exact proposed head commit. Mark a check
complete only from evidence; explain anything not applicable. Inspect the complete diff and
commit-visible artifacts for privacy before publication. Required CI must pass for that exact head
before merge.

Follow `RELEASING.md` for catalog publication. Skill content changes use the documented semantic
version policy. Repository-process-only changes, including `AGENTS.md`, `CLAUDE.md`, tests that
enforce their parity or structure, and pull request templates, do not require a manifest version
bump. Never tag unmerged content, reuse a published tag, or maintain a second release ledger.

## Definition of done

Work is complete only when:

- the full requested scope is implemented without unrelated changes;
- package, manifest, README, attribution, and guide parity contracts hold;
- the full catalog suite passes with discovered tests;
- applicable source, link, forward-test, and material user-path checks pass;
- `git diff --check` and the privacy review are clean;
- no placeholder, debug artifact, unexplained skip, or temporary file remains; and
- the pull request reports exact-head evidence and required CI is green, when publication is in
  scope.

Report every unrun check, unavailable governing skill, unverified source, failed gate, or remaining
blocker plainly.
