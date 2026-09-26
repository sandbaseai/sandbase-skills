---
name: video-generator
description: "Plan and produce short AI videos with SandBase image, video, music, and speech models. Use for commercials, social clips, explainers, short films, storyboards, or multi-shot video generation; use a simpler image or audio skill when no video deliverable is needed."
---

# Video Generator

Turn a creative brief into a production-ready plan or a finished short video. Use SandBase for every generative media call and local media tools only for deterministic operations such as frame extraction, concatenation, mixing, and format checks.

Read [the SandBase API map](references/sandbase-api-map.md) before selecting or running models.

## Choose the delivery mode

- **Plan only**: produce the brief, global style, shot plan, prompts, timing, and cost-aware model shortlist. Do not call a generative model.
- **Generate assets**: create approved reference images, keyframes, clips, music, speech, or sound effects.
- **Assemble final video**: generate the assets, combine them with available local media tooling, and verify the rendered file.

Do not turn a planning request into paid generation. If the user requests generation, gather only missing choices that materially affect the result, then summarize the execution batch for confirmation.

## SandBase execution contract

Use this sequence for image, video, music, TTS, and sound-effect generation:

If the six `sandbase_*` MCP tools are unavailable, continue only in **Plan only** mode. Tell the user that generation requires an authorized SandBase connection and point them to the current setup instructions in the [SandBase CLI repository](https://github.com/sandbaseai/cli). Do not silently substitute another generation provider, request provider API keys, or claim that assets were generated.

1. Call `sandbase_discover` with a short capability query. Search separately for materially different capabilities such as text-to-image, image editing, image-to-video, text-to-music, or TTS.
2. Call `sandbase_inspect` for each serious candidate. Compare the live input schema, output shape, price, duration and aspect-ratio limits, reference-input support, audio support, and execution mode.
3. Call `sandbase_account` before an approved batch of multiple paid generations.
4. Present the selected endpoint names, important arguments, per-call price, expected call count, and a total estimate or clearly stated unknown. Obtain confirmation before the first paid call.
5. Call `sandbase_run` with the exact discovered name and only schema-defined arguments from the current `sandbase_inspect` response.
6. If a call returns a run ID, poll that same ID with `sandbase_run_get` until it completes or fails. Never submit a duplicate merely because generation is still running.
7. Use `sandbase_runs` only to reconcile status or cost when the response is lost or the user asks for recent usage.

Never invent a SandBase model name, parameter, price, output URL, or capability. Model availability changes, so do not hard-code a provider as universally preferred.

## Phase 1: Creative brief

Resolve these decisions before planning shots:

| Field | Decision |
|---|---|
| Purpose | Audience, message, and desired action |
| Narrative | Beginning, development, payoff, and ending |
| Duration | Total target duration and platform limit |
| Format | 16:9 or 9:16 unless the selected model and destination require another ratio |
| Visual language | Medium, subgenre, rendering, palette, lighting, and detail density |
| Recurring elements | Character, product, wardrobe, prop, and location continuity |
| Audio | On-screen speech, narration, music, effects, silence, and language |
| References | User-owned images, brand rules, examples, and prohibited elements |
| Deliverable | Plan, loose assets, or assembled file and required codec/container |

Ask a compact question only for missing information that changes the production. Otherwise state reasonable assumptions. Before paid generation, show the finalized brief and the SandBase execution batch together for confirmation.

## Phase 2: Global definitions

Create a reusable production bible:

- **Visual style**: rendering method, line/texture treatment, palette, lighting, lens language, and detail density.
- **Character or product anchors**: stable name, appearance, proportions, wardrobe/materials, colors, and distinctive features.
- **Environment anchors**: location layout, time of day, weather, recurring background objects, and continuity constraints.
- **Voice profiles**: speaker, language, tone, pace, pronunciation notes, and whether the voice is on-screen or off-screen.
- **Music direction**: genre, tempo range, key or tonal center when relevant, instrumentation, sonic texture, and emotional arc.

Treat references as private user data unless the user says otherwise. Upload only what the selected model needs. Do not clone a real person's face or voice, or imitate a living artist's identity, without the required rights and consent.

## Phase 3: Shot and audio plan

Prefer clips of 3–10 seconds with one primary action and one coherent location. For each clip, record:

| Field | Required detail |
|---|---|
| Purpose | Establish, develop, transition, climax, resolve, or insert |
| Timing | Start, end, and target duration |
| Scene | Environment and elements present from the first frame |
| Action | Subject, movement trajectory, state changes, and end state |
| Camera | Framing, angle, lens feel, and camera movement |
| Continuity | Scene cut or continuous boundary; new keyframe or prior final-frame reuse |
| Audio | Dialogue, narration span, effects, music cue, or silence |
| Dependencies | Required reference, prior clip, voice, or music segment |

Write every video prompt with enough temporal detail to constrain the transition. Include what exists at the start, how the subject and camera move, what changes over time, what remains present, and how the shot ends. Avoid compressing unrelated actions into one clip.

For narration, budget text against the available time. As a rough check, allow about four CJK characters or 2.5 English words per second, then leave breathing room. Generate narration per coherent span rather than as one monolithic track.

If using separate music, create a timecoded emotional arc after the shot plan. Merge adjacent spans only when their mood, density, instrumentation, and energy are genuinely the same.

## Phase 4: Model selection and references

Inspect live SandBase candidates against the plan before generating anything:

- The image model must support the needed aspect ratio and either reference conditioning or image editing when continuity depends on it.
- The video model must support the chosen input mode, duration, ratio, and resolution. Treat native audio, lip sync, start/end frames, and reference video as optional capabilities that must be verified.
- The audio model must support the requested language, duration, voice controls, music mode, or effect type.

Generate only references used by planned shots:

1. Create one primary visual anchor for each recurring subject or product.
2. Generate additional angles or expressions only when required by a shot.
3. Use a SandBase model with inspected reference or editing support; do not assume a generic variation operation exists.
4. Verify identity, clothing/materials, colors, orientation, aspect ratio, and absence of unwanted text or marks before continuing.

If a required capability is unavailable, revise the plan with the user instead of silently substituting an incompatible model.

## Phase 5: Keyframes and clips

For a new shot, generate a first keyframe from the approved references and include the global style, scene, framing, visible content, subject anchor, aspect ratio, and exclusions.

For a continuous boundary:

1. Wait for the preceding SandBase video run to complete.
2. Save the rendered clip with the host's available file tools.
3. Extract the last decodable frame with a local media tool.
4. Verify orientation, ratio, identity, wardrobe, scene, and framing.
5. Supply that frame to an inspected image-to-video endpoint for the dependent clip.

Generate dependency chains sequentially. Independent clips may run in parallel only when the approved budget covers the full batch and the host can track every run ID without confusion.

On-screen dialogue, singing, or lip sync may be embedded only when `sandbase_inspect` confirms the chosen video model supports it. Otherwise generate silent picture and use an inspected speech or lip-sync capability; explain the compromise before running it.

## Phase 6: Music, narration, and effects

- **Music**: translate the timecoded emotional arc into the inspected music model's schema. Lock total duration and core musical identity; vary arrangement by the planned time spans.
- **Narration**: use one consistent inspected TTS endpoint and voice configuration across spans. Keep each result within its narration budget.
- **Effects**: use a dedicated inspected sound-effect model when the video model cannot create them reliably.
- **Embedded audio**: use only when the inspected video model explicitly supports it and the user approved that model.

Store every returned run ID and asset URL in an asset ledger with the clip/span number, selected endpoint, important arguments, status, and actual cost when available.

## Phase 7: Assembly and verification

Use local deterministic media tooling when available. Do not send completed assets to another external service merely to concatenate or mix them.

Assembly rules:

- Normalize clips to one resolution, orientation, frame rate, codec, and audio sample rate before concatenation.
- Preserve intended production audio. Mix narration and separate music as overlays; do not accidentally replace clip audio.
- Duck music under speech, keep narration levels consistent, and prevent clipping.
- Respect the planned order and duration. Use transitions only when they are in the approved shot plan.
- Export to the requested container and codec; otherwise use a broadly compatible MP4/H.264/AAC deliverable.

Verify the final file by checking duration, dimensions, orientation, decodability, audio presence, and representative frames at the beginning, shot boundaries, and end. Watch or inspect the full render when the host supports it.

If local assembly tools are unavailable, return the ordered assets, timecodes, prompts, run IDs, and an explicit assembly manifest instead of claiming a finished video.

## Final handoff

Return:

- the final video or ordered generated assets;
- the approved creative brief and shot list;
- a concise asset ledger with SandBase endpoint names and run IDs;
- estimated and observed cost when available;
- known compromises, failed shots, or continuity issues;
- enough assembly detail to reproduce the result.

Do not claim completion while a SandBase run is pending, an output is missing, or the assembled file has not passed basic media checks.
