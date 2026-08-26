# Brief — rundesk-skills-gamedev

*What this catalog is and why it exists. One screen, and it changes when the catalog does.*

## Story

`rundesk-skills-gamedev` is the game design and development guidance catalog for Rundesk agents. Its
packages carry portable practice across game concept, production planning, player experience,
playtesting, gameplay engineering, world simulation, 2D rendering, isometric and tile worlds,
procedural generation, art direction, and the C++ and Axmol stacks a game is built on.

It is guidance only. Nothing here runs a command, calls a service, or holds a credential.

## Why it exists

Game work has its own failure modes, and general engineering guidance answers almost none of them.
A frame loop is not a request cycle, a playtest is not a test suite, and a rendering seam breaks in
ways no web stack does.

Keeping that practice in its own catalog means an agent doing game work loads it and an agent doing
anything else does not pay for it.

## Users

- Rundesk agents working on a game — engine code, design, production, or art direction.
- The owner and contributors, changing a method once rather than in every game repository.

*Sourced from the readme and the package contract. Which projects install this catalog is not
recorded here.*

## Scope

- **Covers:** game design and player experience; production planning and playtesting; gameplay,
  simulation, animation, camera and control engineering; 2D rendering, isometric and tile worlds,
  procedural generation; game art direction; C++ and Axmol.
- **Refuses:**
  - Executables, service adapters, credentials, network calls, and `rundesk.json` declarations.
  - General engineering method the default catalog already owns — research, planning, review,
    testing, naming.
  - Engine-specific API reference. A package teaches the decision and the trap, and points at the
    engine's own documentation for the call signature.
  - Guidance for a second engine that has not been used here. An unverified engine note is a
    liability, not a skill.

## External systems

- Rundesk — installs this catalog and grants its packages to named agents.
- GitHub — hosts the repository and serves the release a catalog install fetches.
