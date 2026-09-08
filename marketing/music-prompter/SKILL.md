---
name: music-prompter
description: "Design production-ready music prompts and optionally generate music through SandBase. Use for songs, instrumentals, soundtracks, jingles, loops, or multi-part music; use a speech or sound-effect workflow when music is not the main deliverable."
---

# Music Prompter

Turn a musical brief into a coherent prompt, an approved SandBase generation, or a verified multi-clip deliverable. Keep prompt writing useful without an external service, and use SandBase for every generative music call.

Read [the SandBase API map](references/sandbase-api-map.md) before selecting or running a model.

## Choose the delivery mode

- **Prompt only**: return a polished prompt, optional lyrics, and arrangement plan. Do not call a paid model.
- **Generate one track**: select and inspect a current SandBase music model, show the execution price and arguments, obtain confirmation, then generate.
- **Produce a long or multi-part piece**: plan the full arrangement, generate an approved set of clips, assemble them locally, and verify the result.

If the six `sandbase_*` MCP tools are unavailable, continue only in **Prompt only** mode. Point the user to the current setup instructions in the [SandBase CLI repository](https://github.com/sandbaseai/cli); do not request a provider-specific API key or silently switch services.

## Define the musical brief

Resolve only the choices that materially affect the result:

- purpose, audience, platform, and target duration;
- genre and stylistic era without imitating a living artist's identity;
- emotional arc, energy, tempo, meter, and harmonic character;
- core instrumentation, arrangement density, and sonic palette;
- instrumental or vocal, language, lyric ownership, and explicit-content limits;
- loopable ending, clean ending, fade, stems, or other delivery requirements;
- preferred file format, sample rate, and bitrate when the selected model supports them.

State reasonable assumptions for missing details. Treat lyrics, reference audio, and unpublished compositions as private user data and send only what the inspected endpoint needs.

## Build the prompt

Describe the piece as one coherent production brief. Include the dimensions that matter rather than filling every field mechanically:

1. **Global direction** — intended duration, instrumental or vocal mode, language, tempo, and output purpose.
2. **Genre and style** — genre family, period, performance character, and relevant production tradition.
3. **Rhythm and tempo** — BPM or tempo range, meter, groove, swing, syncopation, and rhythmic intensity.
4. **Harmony and tonality** — key or tonal center, major/minor/modal color, chord density, and harmonic movement.
5. **Mood and arc** — starting emotion, development, peak, release, and ending state.
6. **Instrumentation** — lead, rhythm, bass, percussion, texture, and how layers enter or leave.
7. **Density and brightness** — sparse or dense arrangement, register, frequency emphasis, and dynamic range.
8. **Space and ambience** — room character, reverb, stereo width, distance, environmental texture, and intimacy.
9. **Production quality** — polished or raw, modern or vintage, clean or saturated, and mastering intent.

Use direct positive language first, followed by concise exclusions such as “instrumental only, no vocals” or “no drums or percussion.” Do not invent a `negative_prompt` field unless `sandbase_inspect` shows that the chosen endpoint supports it.

For precise arrangements, add chronological cues whose final timestamp matches the intended duration:

```text
Instrumental only. Create a 60-second warm, introspective lo-fi cue at 80 BPM.

[0:00-0:12] Intro — solo electric piano, soft room tone, intensity 1/10.
[0:12-0:36] Development — relaxed drums, sub-bass, and a restrained synth motif, intensity 4/10.
[0:36-0:50] Peak — fuller harmony and wider stereo image, intensity 6/10.
[0:50-1:00] Outro — remove drums and resolve to a clean, spacious ending, intensity 2/10.
```

Timestamp cues are prompt content, not guaranteed controls. Disclose that timing, lyrics, and structure may vary unless the inspected model exposes explicit controls for them.

## SandBase execution contract

For generation, follow this sequence:

1. Call `sandbase_discover` with a short capability query such as `text to music`, `instrumental music`, or `music with lyrics`.
2. Call `sandbase_inspect` for serious candidates. Compare the live schema, prompt and lyric limits, instrumental control, output formats, duration behavior, price, and sync or async execution mode.
3. Prefer the smallest number of calls that can satisfy the requested duration and structure. Do not assume a universal maximum track length from an earlier model.
4. Before the first paid call, show the selected endpoint, important arguments, per-call price, call count, and total estimate or uncertainty. Obtain confirmation for that exact call or batch.
5. For an approved batch of multiple calls, use `sandbase_account` to check the available balance.
6. Call `sandbase_run` with the exact discovered name and only arguments defined by the current inspection response.
7. If a run ID is returned, poll that same ID with `sandbase_run_get` until it completes or fails. Never create a replacement merely because a music run is still pending.
8. Use `sandbase_runs` only to recover a lost run or reconcile status and actual cost.

Do not hard-code a model, duration limit, price, schema, or output URL. Availability changes, and discovery plus inspection is the source of truth.

## Handle long and multi-part music

Use one call when the inspected model can produce the requested duration and a single generation is musically appropriate. Otherwise:

1. Plan the entire structure before generating any clip.
2. Keep genre, BPM, meter, production character, tonal center, core instruments, and ambience stable unless a deliberate change is part of the composition.
3. Vary mood, density, brightness, and arrangement by section.
4. Align the ending state of each clip with the opening state of the next: instrumentation, energy, harmony, rhythm, ambience, and loudness should match.
5. Generate dependent clips sequentially. Independent clips may be batched only within the confirmed budget.
6. Join clips with local deterministic audio tools. Choose beat-aligned edits or short crossfades and preserve the requested total duration.

If the inspected models cannot control continuation or duration reliably, explain the limitation before generation rather than promising seamless output.

## Lyrics and vocals

- Use an explicit instrumental control when the schema provides one; reinforce it in the prompt when useful.
- Supply lyrics only when the user owns them, has permission, or requests newly written lyrics.
- Use structure tags only when the inspected schema documents them.
- Check language support and lyric length before generation.
- Do not clone a real person's voice or imply endorsement without the required rights and consent.

## Verify and hand off

For generated audio, verify as much as the host supports:

- the run reached a terminal successful state and every output URL or file exists;
- container, codec, duration, sample rate, channels, and decodability;
- audible playback, clean start and ending, clipping, silence, and unwanted vocals;
- adherence to the intended mood, instrumentation, structure, and lyric language;
- continuity and loudness across joins for multi-clip work.

Return the final prompt and lyrics, selected SandBase endpoint and run ID, generated file or URL, estimated and observed cost, verification results, and any timing or continuity compromises. Do not claim completion while a required run is pending or an output has not been checked.
