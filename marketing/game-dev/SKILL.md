---
name: game-dev
description: "Build, extend, and verify playable browser games, optionally using SandBase for generated concept art and game assets. Use for substantial 2D or 3D web-game work; use a general frontend workflow for non-game interactive sites."
---

# Game Dev

Turn a game brief into a playable, visually coherent browser game. Keep the game code, deterministic asset processing, builds, and tests local. Use SandBase only for optional generative assets that the user requests.

Read [the SandBase API map](references/sandbase-api-map.md) before generating concept art, textures, sprites, backgrounds, or other AI media.

## Establish the build target

Before implementation, resolve only the choices that materially affect the architecture:

- genre, player goal, failure and success conditions;
- input methods and target devices;
- 2D or 3D presentation, camera, aspect ratio, and art direction;
- required mechanics, content scope, and accessibility expectations;
- supplied assets, rights restrictions, target repository, and delivery format.

Inspect the existing project and preserve its framework, package manager, engine, and conventions. For a new project, choose the smallest suitable stack: native canvas or a focused 2D engine for simple 2D games, and a WebGL engine such as Babylon.js for substantial 3D work. Do not replace an established engine merely because another is familiar.

## Plan around risk

Write a compact implementation plan for work that spans more than one mechanic. Identify the riskiest slice first: physics feel, procedural generation, animation state, navigation, camera behavior, pointer lock, shaders, networking, asset import, or performance.

Define observable acceptance criteria for each slice. A criterion should describe something a player can see or do, not merely a class or file that exists.

Keep gameplay state and rules independent from the UI shell where practical. Separate input, simulation, rendering, audio, persistence, and scene transitions enough that each can be tested without rebuilding the entire game.

## Build a playable vertical slice

Implement the smallest loop that demonstrates the intended experience:

1. load into a valid starting state;
2. accept the primary controls;
3. update the world deterministically enough to debug;
4. communicate goals, feedback, damage or progress, and end states;
5. restart without a page reload or corrupted state.

Use temporary local primitives when necessary to prove mechanics, but do not present placeholders as finished art. Add a deterministic `demo` or equivalent mode when it helps visual regression checks and screenshots reach meaningful gameplay states.

Handle lifecycle boundaries explicitly: initialize the engine once, dispose listeners and render resources, resize safely, pause or mute when appropriate, and avoid duplicate loops during development remounts.

## Generate optional art through SandBase

Do not call an image model merely because the task is a game. First decide whether supplied assets, procedural graphics, vector drawing, or local transformations already satisfy the brief.

When generated art is needed:

1. Call `sandbase_discover` with the required capability, such as `text to image`, `image editing`, or `transparent background image`.
2. Call `sandbase_inspect` for viable candidates and compare the live schema, aspect ratios, reference-input support, output format, price, and execution mode.
3. Create an asset plan listing each asset's purpose, dimensions, transparency, viewpoint, visual anchors, and expected in-game transformation.
4. Before any paid call, show the endpoint name, important arguments, current per-call price, call count, and total estimate or uncertainty. Obtain confirmation for that exact call or batch.
5. Use `sandbase_account` before an approved multi-call batch, then call `sandbase_run` with only current schema-defined arguments.
6. Poll an asynchronous result with `sandbase_run_get` using the same run ID. Never create a duplicate because a run remains pending.
7. Use `sandbase_runs` only to recover status or reconcile actual cost.

Record each generated asset's purpose, prompt summary, endpoint, run ID, local path, dimensions, provenance, and observed cost. Verify that sprites and textures work at actual gameplay scale; attractive source images are not automatically usable game assets.

Do not imitate a living artist's identity or use protected characters, logos, faces, or voices without the necessary rights. Send only the minimum user material required by the inspected endpoint.

## Integrate and tune

- Keep controls responsive and document them in the start screen or HUD.
- Use delta time correctly and avoid frame-rate-dependent movement.
- Bound spawned objects, particles, event handlers, audio nodes, and GPU resources.
- Keep essential text readable at the smallest supported viewport.
- Add loading, error, pause, restart, victory, and failure states appropriate to the scope.
- Preserve player progress only when the brief requires it, and version saved data defensively.

Treat game feel as part of correctness. Tune acceleration, friction, camera lag, hit feedback, animation timing, sound cues, and difficulty against the stated experience rather than arbitrary constants.

## Verify the game

Run the project's type checks, tests, and production build. Then exercise the game in a real browser at representative viewport sizes and inputs.

Verify at least:

- first load and restart;
- every required control and core mechanic;
- success, failure, pause, and recovery paths;
- resize and focus changes;
- missing or delayed assets;
- console errors and obvious resource growth;
- representative screenshots during real gameplay, not only menus.

When code and the rendered result disagree, treat the rendered result as the defect report. Do not claim completion while the core loop is unplayable, generated assets are still pending, or the production build fails.

## Handoff

Return the playable project or requested build, control summary, implemented mechanics, validation results, asset ledger, SandBase run IDs and costs when applicable, and any known limitations. Deployment or publication is a separate external action unless the user explicitly requested it.
