## Summary

<!-- State what changes and why in one or two lines. -->

-

## Scope and compatibility

- Packages changed:
- User-visible guidance:
- Preserved behavior:
- Sources added or updated:
- Executables, scripts, services, dependencies, credentials, or network behavior added: none
- Adapted third-party work: none

## Critical risk

<!-- Required for privacy, licensing, incompatible package changes, destructive guidance, or other critical risk. Write "None" when no critical risk applies. -->

- Risk:
- Guard:

## Validation

- [ ] `python3 -m unittest discover -s tests -v`
- [ ] Local reference links resolve and every touched `SKILL.md` satisfies the package contract.
- [ ] Current engine, platform, and version claims were verified against the primary sources recorded below, or none changed.
- [ ] A substantial new or changed skill was forward-tested against a realistic raw game task, or no forward-test was required.
- [ ] `git diff --check`
- [ ] Required GitHub checks pass for the exact head commit.

```text
# Exact validation, source-verification, and forward-test commands with observed results
```

## Repository gates

- [ ] The diff contains no secret, customer identifier, private-project language, owner-specific path, private evidence, or unrelated artifact.
- [ ] The catalog remains guidance-only: no package adds scripts, executables, services, credentials, dependencies, network calls, or provider-specific agent metadata.
- [ ] Routing triggers are distinct, descriptions stay within 1,024 characters, and touched `SKILL.md` files stay below 500 lines.
- [ ] Guidance states defaults, deviation conditions, failure modes, preferred replacements, and observable proof without promising that a pattern makes a game fun.
- [ ] Every touched package has `references/sources.md`; claims distinguish source evidence from catalog conclusions and label heuristics appropriately.
- [ ] Local links resolve, conditional depth stays one level down, and no package adds a README, changelog, empty directory, or forbidden metadata.
- [ ] `README.md`, `manifest.json`, `tests/test_catalog.py`, and `skills/` agree.
- [ ] Adapted work records its license, exact upstream commit, and modifications in `THIRD_PARTY_NOTICES.md`, or none was adapted.
- [ ] Any required semantic `manifest.json` version change follows `RELEASING.md` and is stated below.

## Release

- Manifest version: `<before>` → `<after>`
- SemVer reason:
- Release or follow-up required after merge:

## Manual user path

<!-- Give the realistic raw game task used to exercise the changed guidance and the observed routing, decisions, traps, composition, and proof. State clearly when no forward-test was required. -->

```text

```
