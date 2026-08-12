# Depth, visibility, and rotation

Use this reference when simple row traversal no longer proves correct occlusion, or when adding
stacked surfaces, culling, and quarter-turn views.

## State the ordering assumptions

A single scalar order is valid only under matching geometry constraints.

| Visible world | Smallest defensible model |
|---|---|
| Flat, unit cells with no overhang | Back-to-front oriented grid rows plus stable within-row order |
| Overhang-free heightfield cells | Oriented row order plus the declared surface/base-height relation |
| Tall or multi-cell objects | Projected-overlap filter plus world-footprint dependencies |
| Bridges, tunnels, roofs, stacked floors | Explicit surface identity, height interval, and occlusion role |
| Interpenetrating or cyclic silhouettes | Split geometry, clipping, or a depth-capable representation |

`x + y` is a traversal key for one common orientation, not a universal depth equation. Adding an
arbitrary multiple of `z` can repair one screenshot while reversing another overlap. A stable ID may
break a true tie, but must never override a known behind/in-front dependency.

## Build dependencies only where pixels may overlap

For each visible item, retain both:

- a projected visual bound for cheap overlap rejection; and
- a world footprint or bounding volume for relative-position tests.

When two projected bounds do not overlap, their relative draw order is irrelevant. When they do,
derive whether one is wholly behind the other along a separating world axis or surface relation. Add
that directed dependency and topologically order the visible graph. This is more work than row sorting,
so reserve it for objects whose footprints make row sorting invalid and keep the broad phase bounded to
visible spatial neighbours.

Detect cycles. A cycle means no whole-item painter order can satisfy every silhouette. Do not hide it
with an unstable comparator; split a long object at tile or occlusion boundaries, clip the crossing,
or move opaque geometry to a depth-capable path. Transparent pixels and blended layers may still require
ordered compositing even when opaque geometry uses a depth buffer.

## Model stacked surfaces explicitly

Give each independently visible or selectable surface:

```text
stable surface id and owning assembly id
world footprint and z interval or exact support geometry
connection/contact edges used by adjacent pieces
occlusion class and transparency/reveal behavior
pick priority and tool selectability
```

Keep underground, ground, deck, roof, and effect categories as policy, not as the sole depth key.
Actual height and overlap decide visibility. Group dependent pieces deliberately: a deck, its support,
and an underpassing route can require different local ordering while still belonging to one assembly.

Test views where one layer disappears behind terrain, reappears in a reveal mode, crosses another layer,
and approaches every viewport edge. Real failures in mature isometric renderers cluster at these combined
conditions rather than at isolated flat tiles.

## Derive a conservative cull region

Start with the viewport rectangle in projected-world coordinates. Expand it by the maximum visual
overhang of the class being queried. Invert every expanded corner at the supported minimum and maximum
surface heights, include the resulting grid points in a conservative hull or axis-aligned grid bound,
then expand for the largest world footprint and animation/effect reach.

For the canonical basis in `coordinate-and-picking.md`, maximum elevation shifts the flat inverse by:

```text
height_grid_margin = ceil(max_abs_z * rise / (2 * half_h))
```

Here `max_abs_z` is the greatest supported distance from the plane used for the flat inverse. That
term covers the elevation-induced grid shift only. Sprite tops, leaning art, shadows, particles,
multi-cell footprints, camera filtering, and rounding need their own declared visual expansion. If an
object's visual bounds are data-driven, cull by those bounds rather than one global sprite guess.

Prove culling with a slow reference query in tests: enumerate all scene items, project their full visual
bounds, and compare the optimized visible set. The optimized set may include extras; it must never omit
an item whose pixels intersect the viewport.

## Define quarter-turn remaps

For a zero-based map of width `W` and height `H`, one clockwise world-to-view convention is:

| Orientation | World `(x, y)` to view `(u, v)` | View size |
|---|---|---|
| 0 | `(x, y)` | `W x H` |
| 1 | `(y, W - 1 - x)` | `H x W` |
| 2 | `(W - 1 - x, H - 1 - y)` | `W x H` |
| 3 | `(H - 1 - y, x)` | `H x W` |

Its inverses are respectively `(u,v)`, `(W-1-v,u)`, `(W-1-u,H-1-v)`, and
`(v,H-1-u)`. A different clockwise convention is fine; pin one table and use it everywhere. Test a
non-square map because square dimensions conceal swapped-axis mistakes.

If the projection consumes view coordinates, the ordinary row key can be derived from `(u, v)` rather
than maintained as four unrelated formulas. Apply the same orientation to directional edge/corner
metadata, footprint extents, and sprite selection. Stored simulation data remains in world orientation.

## Use an orientation proof matrix

For each orientation, automate:

- every world cell maps in bounds and inverse-maps to itself;
- projected cell centres and corners match the expected handedness;
- far-to-near traversal agrees with pairwise dependencies;
- each directional edge/corner maps to the expected screen-facing edge/corner;
- picking returns the surface drawn under representative pixels at every supported elevation;
- culling contains the slow reference set at every viewport edge;
- non-square extents, multi-cell footprints, and maximum overhang remain visible; and
- applying four clockwise remaps returns coordinates and direction metadata to identity.

Add live scenes with asymmetric landmarks, slopes in every direction, tall objects, crossings, and map
edges. Symmetric test art can make a wrong mirror or direction remap look correct.
