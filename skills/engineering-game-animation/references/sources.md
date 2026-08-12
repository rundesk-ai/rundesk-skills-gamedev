# Engineering game animation source map

Checked 12 August 2026. This package independently synthesizes current engine documentation, an
interchange specification, asset-tool contracts, and named-practitioner timing guidance. It does not
adapt AAABench or another skill package. AAABench informed topic discovery only.

## State graphs, transitions, blends, and layers

- Epic Games, Unreal Engine 5.8,
  [State Machines](https://dev.epicgames.com/documentation/en-us/unreal-engine/state-machines-in-unreal-engine),
  documents entry, states that produce poses, directed transitions, blend behavior, and reset-on-
  entry semantics. It establishes that transition direction and re-entry are explicit graph
  contracts; it does not require one graph structure or semantic vocabulary for every game.
- Godot stable,
  [Using AnimationTree](https://docs.godotengine.org/en/stable/tutorials/animation/animation_tree.html),
  documents one-shots and aborts, blend trees, time seek/scale, state machines, immediate/synchronized/
  at-end transition modes, crossfades, reset, priority, and advance conditions. This supports the
  state/blend/one-shot selection and explicit transition table. Exact nodes and priority rules remain
  Godot-specific.
- Unity 6,
  [Animation State Machines](https://docs.unity3d.com/6000.0/Documentation/Manual/AnimationStateMachines.html)
  and [Animation Layers](https://docs.unity3d.com/6000.0/Documentation/Manual/AnimationLayers.html),
  document state/transition graphs plus override or additive layers and body masks. They corroborate
  separating independent pose concerns and declaring composition; they do not prove that layering is
  simpler or cheaper for an unmeasured graph.

The recommendation to minimize full-body state multiplication, reserve global transitions for true
high-priority reactions, and declare overlapping-layer ownership is a catalog conclusion from these
graph capabilities and their interaction surface.

## Clip and import contracts

- Khronos Group,
  [glTF 2.0 animation specification](https://registry.khronos.org/glTF/specs/2.0/glTF-2.0.html#animations),
  defines animation samplers, input/output accessors, interpolation, channels, target nodes, and
  translation, rotation, scale, and morph-weight paths. This establishes explicit sampled clip data
  and target bindings for one interchange format; the skill's semantic IDs, root policy, masks, and
  validation schema are broader integration requirements.
- Aseprite, [Tags](https://www.aseprite.org/docs/tags/) and
  [Slices](https://www.aseprite.org/docs/slices/), documents named animation ranges and playback
  directions plus slice bounds, pivots, and JSON export. This supports stable 2D clip grouping and
  pivot metadata rather than filename order or trimmed centers.
- Tiled, [Working with Objects](https://doc.mapeditor.org/en/stable/manual/objects/), documents that
  tile-object alignment changes an image relative to its object origin and that isometric alignment
  defaults differ from other orientations. This supports keeping a logical contact point independent
  from bitmap bounds; `creating-2d-game-art` and `building-isometric-worlds` own the detailed art and
  projection contracts.

The clip contract and import rejection/fallback rules are catalog synthesis. No source mandates one
file format, clip naming convention, direction count, rig, frame rate, or runtime graph.

## Motion authority and presentation time

- Epic Games, Unreal Engine 5.8,
  [Root Motion](https://dev.epicgames.com/documentation/en-us/unreal-engine/root-motion-in-unreal-engine),
  distinguishes movement-component-driven characters with animation layered on top from animations
  whose root-bone displacement drives character motion when extraction is enabled. It also exposes
  root locking and extraction modes. This supports choosing one displacement authority; collision,
  networking, and interruption details must be verified in the active engine.
- Unity 6, [How Root Motion works](https://docs.unity3d.com/6000.0/Documentation/Manual/RootMotion.html),
  independently documents body/root transform projection and applying or baking motion from clips.
  It corroborates that root data and runtime object motion are separate contracts, not that every
  action should use root motion.
- Glenn Fiedler,
  [Fix Your Timestep!](https://gafferongames.com/post/fix_your_timestep/) (2004), derives rendering
  between previous and current simulation states using the accumulator remainder. It supports
  presentation-only snapshot interpolation; `programming-gameplay` owns the fixed-step and overload
  policy, and the article is practitioner derivation rather than an engine requirement.

The explicit authority handoff, teleport/correction discontinuity, and no-feedback-to-simulation
rules are catalog safeguards built on those separate motion and presentation clocks.

## Events, synchronization, and durable facts

- Epic Games, Unreal Engine 5.8,
  [Animation Notifies](https://dev.epicgames.com/documentation/en-us/unreal-engine/animation-notifies-in-unreal-engine),
  documents events and duration states synchronized to animation, including sound, particles, sync
  markers, sockets, blend-weight thresholds, trigger chance, LOD filtering, leader/follower behavior,
  and queued versus more precise montage delivery. These features establish both useful presentation
  timing and multiple conditions under which delivery varies.
- Unity 6,
  [Add an Animation Event to an imported animation clip](https://docs.unity3d.com/6000.0/Documentation/Manual/AnimationEventsOnImportedClips.html),
  documents calling a function at a specified imported-clip time with a parameter. It corroborates
  clip-timed callbacks; it does not guarantee authoritative, once-only delivery through blending,
  seeking, replay, rollback, or LOD.

Derived pair: **good** commits damage or transfer in the authoritative action timeline and lets a
marker present the fact; **bad** lets a filtered, blended, skipped, or repeated presentation callback
be its only owner. This is the catalog's conservative conclusion from documented notify variability,
not a statement that engine animation events can never call gameplay code.

## 2D and isometric synthesis boundaries

- Stable bases, frame-family bounds, and semantic clip names are shared contracts with
  `creating-2d-game-art`; placement and depth remain in `engineering-2d-rendering` and
  `building-isometric-worlds`.
- World-facing to view-facing remap, explicit mirror eligibility, and rotation-wide attachment tests
  are catalog conclusions from those neighboring skills. No cited source establishes one universal
  four- or eight-direction layout.
- State/transition proof belongs here because it is animation-domain behavior. General automated-test
  structure belongs to `testing-code`, visual renderer proof to `engineering-2d-rendering`, and
  performance claims to `performance-engineering`.

## Good/bad pair mapping

- **Semantic action authority:** Epic's documented notify filters, blend thresholds, chance, and
  delivery modes establish why a visible frame or callback is an unsafe sole owner. The committed-
  action pair is the catalog's integration rule with `programming-gameplay`.
- **Transition priority:** Unreal and Godot expose directed transition, priority, and reset behavior.
  The stun/recovery pair applies those explicit contracts instead of allowing callback arrival to
  choose a pose.
- **Movement authority:** Epic and Unity distinguish in-place presentation from extracted root
  displacement. The two good examples select one owner; the bad example applies both documented
  motion sources and therefore double-integrates movement.
