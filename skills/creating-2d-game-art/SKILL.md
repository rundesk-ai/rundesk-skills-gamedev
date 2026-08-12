---
name: creating-2d-game-art
description: Use when defining, creating, generating, reviewing, or integrating production 2D game art such as sprites, tiles, props, characters, modular environment kits, animation sheets, or atlases. It supplies an engine-neutral workflow for art direction, native-scale readability, pivots and footprints, variants, export metadata, and in-game validation. Do not use it for renderer implementation, projection math, or general-purpose image prompting alone.
---

# Creating 2D game art

Treat an asset as complete only when it communicates the intended gameplay state in the target
scene and survives the runtime pipeline. A polished source image with the wrong scale, base point,
alpha, or state vocabulary is not production-ready art.

Use `creating-design-assets` alongside this skill when choosing a medium, prompting an image model,
or establishing general visual grammar and rights provenance. This skill owns the game-facing asset
contract.

## Work in this order

1. **Write the runtime brief.** Record the camera/view, target displays, reference resolution,
   expected on-screen size, sampler and scaling behavior, lighting responsibility, interaction
   states, animation needs, and memory or atlas constraints. Separate pixel art, filtered raster,
   and vector-derived raster; they require different scaling and cleanup rules.
2. **Prove one representative asset.** Build the smallest difficult asset and place it at native
   gameplay size in a representative scene. Test silhouette, value grouping, overlap, state cues,
   and background variation before producing a family.
3. **Lock the visual grammar.** Define perspective, pixel or detail density, palette roles, outline
   behavior, light direction, material cues, edge treatment, shadow ownership, and acceptable
   variation. State which rules are authored into pixels and which the renderer adds.
4. **Define spatial metadata.** Give every gameplay sprite a stable identity, visible bounds,
   logical footprint, base/pivot, optional sockets or hot spots, collision or selection shape, and
   layer role. The opaque image rectangle is rarely the gameplay footprint.
5. **Build a reusable family.** Produce key states and structural variants before decorative
   volume. For environment art, validate seams, corners, transitions, occluders, and repeated
   placement. For actors, keep the base point stable while poses change.
6. **Export source plus derived data.** Preserve editable source separately from generated sheets.
   Export stable region names and explicit frame, pivot, trim, and slice metadata. Make atlas
   rotation, trimming, padding, alpha treatment, sampling, and scale variants declared settings.
7. **Validate the shipped path.** Import the packed result, not a loose source PNG. Inspect all
   target scales, backgrounds, animation transitions, atlas pages, color/accessibility modes, and
   supported devices. Record failures as art-contract defects, not manual runtime offsets.

Read [the runtime art contract](references/runtime-art-contract.md) when specifying sprites, modular
kits, animation sheets, generated images, or atlas handoff. Read [the source map](references/sources.md)
when changing a claim or reviewing the evidence behind a default.

## Make readability a gameplay requirement

Judge important assets in motion, at actual gameplay scale, and against the worst plausible
background—not only enlarged on a transparent checkerboard. Preserve more than color alone for
critical distinctions: combine value, silhouette, outline, shape, pattern, label, or motion as the
experience permits.

Create a validation board containing:

- the asset at minimum, typical, and maximum gameplay size;
- quiet, bright, dark, and visually busy representative backgrounds;
- neutral, selected, disabled, damaged, hostile, friendly, and interactable states that apply;
- nearby assets at their real relative scale;
- color-vision and high-contrast checks for gameplay-critical cues.

Do not chase detail that disappears at the intended scale. When two entities must be distinguished
quickly, start with silhouette and value grouping, then add internal detail.

## Keep art and gameplay geometry related but separate

Use a named base or pivot as the stable placement contract. Derive it from the logical contact
point—feet, wheel contact, building foundation, wall base—not the center of each trimmed rectangle.
Keep collision, occupancy, and interaction shapes explicit; changing a glow or shadow must not
silently change gameplay.

```text
Good: tree_oak_a has stable ID, bottom-center base, trunk selection shape, canopy occlusion role.
Bad:  gameplay derives position and selection from the current PNG's nontransparent bounds.
```

For tall or overhanging sprites, keep the footprint small enough to describe occupied ground while
the visible bounds may extend across several cells. Route isometric placement and depth decisions to
`building-isometric-worlds`; route grid occupancy to `building-tile-based-worlds`.

## Design kits around composition, not isolated beauty

For tile and modular environment families, begin with a placement matrix: straight runs, inside and
outside corners, ends, transitions, elevation changes, occlusion cases, and repeated clusters. Add
variants where repetition is visible, but keep their structural seams and semantic metadata
compatible.

Avoid baking dynamic neighbors, transient selection, global atmospheric light, or one specific map
composition into reusable base sprites. Baked information that contradicts adjacent tiles or runtime
lighting makes a technically valid kit visibly incoherent.

## Keep animation semantics stable

Name animation states by gameplay meaning and export their frame order and timing. Author strong key
poses first; add frames only when they improve readability, timing, or style on the target display.
Keep the contact/base point stable unless motion intentionally moves the actor in world space.

```text
Good: `attack_heavy` carries ordered frames, durations, a stable base, and named effect sockets.
Bad:  `sheet_final_3.png` relies on alphabetical regions and per-frame centering.
```

The animation may expose event markers, but gameplay authority remains in the simulation. Route
runtime timing and state ownership to `programming-gameplay`.

## Treat generated art as untrusted source material

When an image model or procedural tool contributes, preserve the prompt/reference/provenance record
required by the project, then inspect every output for perspective drift, inconsistent light,
unstable silhouettes, broken transparency, near-duplicate frames, unintended marks, and rights
constraints. Rebuild pivots, tile edges, states, and metadata explicitly. A contact sheet is useful
for selection; it is not a runtime atlas contract.

Do not upscale, slice, or pack generated art before selecting a coherent family. Early automation
multiplies inconsistency and makes later cleanup harder.

## Common traps

| Trap | Preferred replacement | Failure avoided |
|---|---|---|
| Approving art only at editor zoom | Review at runtime size in representative scenes | Detail exists but gameplay state is unreadable |
| One color carries a critical state | Add shape, value, outline, pattern, or another channel | State disappears for some players/backgrounds |
| Every frame uses its trimmed center as pivot | Export one logical base/pivot through trim metadata | Actors jitter and props move when animation changes |
| Collision follows alpha automatically | Author explicit collision/selection/footprint data | Cosmetic edits change gameplay |
| Atlas packing flattens paths and rotates silently | Preserve stable IDs and declare transform support | Name collisions or incorrectly rendered regions |
| Linear filtering samples transparent neighbors | Match padding/bleed and sampler to the asset style | Seams and colored halos appear at scale |
| All shadows and light are baked | Declare baked versus runtime lighting ownership | Double shadows and contradictory illumination |
| Generated sheet goes directly to production | Select, normalize, clean, annotate, import, and review | Inconsistent family and missing runtime metadata |

## Prove completion

Produce evidence from the actual import and representative scene:

- stable region IDs resolve after repacking and source renames;
- pivots, footprints, sockets, and shapes remain aligned through every state and frame;
- tile and kit seams hold under allowed transforms and repeated placement;
- packed output has no bleed, halo, sampling, alpha, or unexpected rotation defect;
- important entities and states remain distinguishable at target scales and backgrounds;
- atlas page, texture format, and memory results fit declared budgets;
- source, export settings, provenance, and generated outputs are reproducible.

Use `engineering-2d-rendering` for draw order, batching, sampling implementation, and render proof;
use `performance-engineering` when establishing or diagnosing budgets rather than guessing limits.
