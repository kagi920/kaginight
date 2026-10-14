# 3D Motion Reference: implementation evidence and KAGIXR translation

Research date: 2026-10-14. Primary target: https://takayustudio.jp/3d-motion-reference/

## Evidence boundary

This report separates (A) statements retrieved from the site's public HTML text, (B) independently verified engine/API documentation, and (C) original implementation recommendations. It is not a source-code audit of TakayuStudio. Direct HTTP retrieval of the page was refused by the execution network; that route was not retried or bypassed. The web reader reached the page through its homepage link, but received a client-rendered shell with zero populated catalog records. No served JavaScript, shader, dependency manifest, repository, per-item recipe, or numerical demo setting has yet been inspected here. A zero count in this shell does not mean the live catalog is empty. Browser visual/catalog research is a separate workstream.

## A. Verified statements in the public page shell

Source: [3D Motion Reference](https://takayustudio.jp/3d-motion-reference/), reached from the [studio homepage](https://takayustudio.jp/).

The site describes its demos as original Three.js scenes. Catalog previews are exported videos; hovered previews and details render live. Its learning model combines depth cues, object movement, and camera work. Controls include speed, pause, frame stepping, effect off/on/comparison, and camera/backstage/split views. Backstage supports orbit and zoom and depicts camera frustum/path. Lab lens adjustment preserves subject size while changing field of view; angle rotates around the target. The interface offers copying settings and minimal recipes for Three.js, CSS, After Effects, and Blender. These are page claims, not verified implementation internals.

## B. Engine/API facts verified independently

- [PerspectiveCamera](https://threejs.org/docs/pages/PerspectiveCamera.html): field of view is vertical and expressed in degrees; camera projection must be updated after property changes. Near must be positive. Camera focus does not itself add depth of field.
- [Sprite](https://threejs.org/docs/pages/Sprite.html): a camera-facing plane commonly used with transparent imagery. It does not cast shadows. This is a viable representation for a protected 2D face in a 3D scene.
- [InstancedMesh](https://threejs.org/docs/pages/InstancedMesh.html): instances share geometry/material while varying transforms, reducing draw calls. Changed instance transforms/colors need their update flags; bounds may need recalculation after transforms.
- [CameraHelper](https://threejs.org/docs/pages/CameraHelper.html): renders camera-frustum line segments; refresh after camera/projection changes. Suitable for an independently implemented backstage inspector, but its use by TakayuStudio is unverified.
- [ShaderMaterial](https://threejs.org/docs/pages/ShaderMaterial.html): custom GLSL for WebGLRenderer; uniforms can update every frame. Line primitive width is generally one pixel, so thick ribbons should use geometry rather than relying on linewidth.
- [WebGLRenderer](https://threejs.org/docs/pages/WebGLRenderer.html): current documentation targets WebGL2. Provides render targets, viewport/scissor, performance statistics, asynchronous shader precompilation, and an animation-loop API. Object-level transparency sorting cannot solve every overlap. These current docs do not establish the reference site's installed Three.js version.
- [Web MIDI API specification](https://webaudio.github.io/web-midi-api/) and [MDN API guidance](https://developer.mozilla.org/en-US/docs/Web/API/Web_MIDI_API): receive device messages through input events; enumerate devices; handle connection changes. Secure-context, permissions-policy, and user permission constraints apply. Browser support is incomplete, so feature detection and fallback are required.

## C. Original KAGIXR implementation proposal

Everything below is a proposed translation of spatial-motion principles, not extracted TakayuStudio code or a claim that its demos implement these formulas.

### 1. Art-direction invariant

The recognizable front face remains the original 2D artwork. Depth belongs mainly to repeated silhouettes, contour ribbons, particles, and the environment. Do not invent a full character head, facial side planes, sculpted nose, rounded eyes, or physically lit facial surfaces. Preserve the source proportions, eye/mouth placement, line quality, palette, and alpha boundary.

Three useful modes:
1. Identity lock: hero art rendered in an unlit camera-facing plane; spatial echoes extend behind it.
2. Shallow card: hero may yaw/pitch slightly; cap angles before foreshortening compromises recognition. Side/back appearance is an intentional graphic edge or silhouette.
3. Spatial ensemble: hero remains protected while separate duplicate cards orbit, recede, or trace a helix.

Default to identity lock. A card viewed edge-on is not a successful 3D face. Treat extreme-angle controls as an explicit alternate composition, never the default.

### 2. Scene and control architecture

Use modules with distinct ownership:
- Asset layer: immutable hero artwork, alpha silhouette, optional authored contour paths, source color-space declaration.
- Hero layer: unlit plane or sprite, consistent anchor and source aspect ratio, optional subtle bob/scale.
- Spatial layer: echo cards, ribbon strips, bursts, background depth landmarks.
- Camera rig: target, orbit azimuth/elevation, dolly distance, vertical FOV, optional roll.
- Timeline: monotonic simulation time, tempo/beat phase, deterministic seed, playback rate, seek/scrub.
- Parameter bus: named ranges, defaults, target values, smoothing, clamps, mappings, preset serialization.
- Input adapters: keyboard, UI, MIDI; all feed the same parameter bus.
- Renderer: measured quality tier, resize, context-loss handling, GPU disposal, output capture if separately requested.
- Inspector: output view, external camera view, side-by-side comparison; never changes the production camera simply because the inspector is moved.

Separate camera and subject animation: camera-only orbit should not silently rotate the hero geometry. Separate artistic depth from temporal lag: more historical samples and greater Z spacing are independent controls.

A preset should store version, stable ID, seed, asset reference, camera settings, motion settings, palette, quality tier, and MIDI map. Do not store device-sensitive identifiers unnecessarily. Import validates numeric ranges and ignores unknown fields rather than executing expressions.

### 3. Motion kernels and formulas

All equations are original engineering recipes. Use seconds/radians internally; expose friendly units in the UI.

**Smooth live parameters:** for a target value q, update x ← x + (q−x)(1−exp(−dt/τ)). The time constant τ makes smoothing largely frame-rate independent. Use separate attack/release constants if an effect should strike quickly and decay slowly. Cap pathological dt after tab suspension; do not integrate a huge step.

**Beat phase:** beat(t) = beat0 + (t−t0)·BPM/60. Loop phase = fractionalPart(beat/beatsPerLoop). Re-anchor phase when switching clock sources. Tempo changes must not reset all motion accidentally.

**Circular/elliptic motion:** p(t) = center + (a cos θ, b sin θ, z(t)). θ = 2π·cyclesPerSecond·t + phase. A depth orbit can instead use XZ so its near/far crossings produce scale and overlap cues. Layer small vertical motion separately.

**Helix:** p(t) = (r cos θ, r sin θ, pitch·θ/(2π)), or retain a stationary head and place delayed echoes along the curve. For a closed loop, make the depth term periodic or hide/recycle the tail where opacity approaches zero; an unbounded helix will eventually leave the scene.

**Temporal echo:** store hero poses in a fixed-size ring buffer with timestamps. For echo i, sample the interpolated historical pose at t−i·delay. Add deliberate depth spacing z_i = z_head − i·spacing along the chosen scene axis, not necessarily world Z after arbitrary rig rotation. Scale s_i = s0·exp(−i·taper); opacity a_i = a0·exp(−i·fade). Historical transforms plus depth offset make motion readable without altering the face.

**Elastic displacement:** use a damped spring d²x/dt² + 2ζω·dx/dt + ω²(x−target) = 0 for overshoot. Integrate with a fixed step or stable analytic method, not naive frame-dependent increments. Expose damping/settle time rather than arbitrary internal coefficients.

**Velocity-linked trail length:** measure filtered speed |p(t)−p(t−dt)|/dt. Map it through a bounded curve to trail length; do not let a MIDI jump create an infinite ribbon. Enforce a maximum teleport distance and break the strip when exceeded.

**Ribbon geometry:** sample centerline points p_i; estimate a tangent from neighboring samples; build a stable perpendicular frame; emit left/right vertices p_i ± width_i·normal_i/2 and triangle-strip indices. Parallel transport or a carried frame avoids abrupt flips where a cross-product degenerates. Taper width and alpha toward the tail. Subdivide based on curvature/spacing, not only frame count.

**Dolly/FOV compensation:** for a camera looking squarely at a subject plane, projected subject size is proportional to 1/[d·tan(FOV/2)]. Preserve framing by d_new = d_old·tan(FOV_old/2)/tan(FOV_new/2). This assumes fixed subject scale, aspect ratio, and camera zoom. Update projection and place the camera along its target-to-camera direction. It is not exact for arbitrary rotated or deep subjects; fit bounds if necessary.

**Small parallax:** move the camera or independent layers by bounded offsets weighted by depth. Screen displacement grows as camera-space depth decreases under perspective. Add static depth landmarks so the effect remains perceptible without excessively moving the face.

### 4. Depth, material, and compositing decisions

Begin with perspective scale, occlusion, Z spacing, and restrained parallax; these give depth before costly post-processing. Keep the hero high contrast and sharp. Tail tint, fade, and reduced detail establish hierarchy.

For the hero, use an unlit material and correct texture color space so stage lighting/tone mapping does not arbitrarily recolor the source. Validate alpha edges on light and dark backgrounds. Do not use broad bloom on the face. A soft shadow, if desired, must be a separate authored plane/blob or dedicated shadow strategy; Three.js sprites do not cast shadows.

Opaque/cutout silhouettes are easier to depth-sort than many translucent cards. If translucent echoes are required, choose an explicit strategy: back-to-front sorting where sufficient, additive emission where stylistically appropriate, or a compositing pass. Disabling depth writes can prevent some artifacts but does not solve every transparency intersection. Instancing reduces draw calls but does not automatically sort transparent instances; use sorted instance order/custom batching, a cutout treatment, or accept a designed additive look.

Keep the hero visible through a protected composition pass if that is the art requirement. Do not just disable all depth tests globally; that destroys the spatial relationship of the other elements. A hero rendered last as an overlay may look like a sticker, so test the desired balance rather than assuming it is always superior.

Shader uniforms can include time, normalized age, velocity magnitude, palette positions, opacity envelope, width, and beat pulse. Restrict heavy distortion to trails/background; use a face-protection mask if a global post effect is unavoidable. UV animation should not sample outside intended borders. Prefer geometry for thick 3D trails.

### 5. Suggested MIDI control contract

This is a new mapping proposal, not a feature verified on the reference site.

- Continuous controls: depth amount, trail duration, echo opacity, orbit azimuth, camera elevation, FOV/dolly pair, palette interpolation, and motion energy.
- Note triggers: bounded pulse, radial burst, preset change, freeze/release, or reset-to-home. Normalize velocity to 0–1 and optionally apply a response curve.
- Pitch bend: signed −1..1 control for subtle orbit or trail twist; center deadband prevents drift.
- MIDI learn: explicitly select target parameter, listen for the next eligible input, show device/channel/message mapping, then save on user confirmation.
- Channel filter and per-device enable controls prevent unintended mappings.
- Treat note-on with zero velocity as note-off. Track held-note state. Provide a panic/reset control that releases gates, clears stuck envelopes, and returns camera to safe framing without deleting presets.
- Optional external clock: estimate tempo from incoming clock timestamps with smoothing, handle start/continue/stop, and specify clock-loss behavior. Do not infer transport solely from note activity.
- All incoming values pass through normalization, range mapping, clamping, optional smoothing, and conflict arbitration. Manual UI values and MIDI targets must have a documented precedence rule.
- Offer UI/keyboard fallback when Web MIDI is missing or denied. No SysEx access is required for ordinary note/CC performance controls. Ask for the minimal capability only.

### 6. Performance and stability specification

Use a fixed allocation pool for echoes/particles and reuse typed arrays. Avoid generating geometries/materials/textures every frame. Start with a small effect budget and profile on the intended performance computer at the actual output resolution. Repeated geometry can be instanced when its transparency strategy permits. Throttle hidden/offscreen previews and freeze simulation intentionally when not needed.

Quality tiers should adjust pixel ratio, echo count, ribbon samples, bloom resolution, and optional effects without changing the composition or MIDI contract. Use measured frame time with hysteresis; do not oscillate quality every frame. Precompile shaders and upload assets before a live cue. Record frame time percentiles, draw calls, triangles, and texture/geometry counts; average FPS alone misses hitching. Test repeated preset switches for resource leaks. Have a safe fallback preset that uses only the protected face and inexpensive echoes.

If a catalog is built, the reference site's stated video-preview/live-detail split is a useful pattern. Do not run a separate full realtime scene for every visible card by default. Choose whether the inspector shares a renderer via viewport/scissor or renders to separate targets; both are implementation options, not confirmed site architecture.

### 7. Testable acceptance criteria

1. At zero depth/energy the original artwork is recognizable and geometrically unchanged.
2. Disabling spatial effects removes trails/depth cues while leaving framing and hero artwork comparable.
3. Scrubbing to the same time with the same preset/seed yields the same frame, unless explicitly in live-input mode.
4. Frame stepping is deterministic and does not advance MIDI envelopes unexpectedly while paused.
5. Changing FOV with compensation preserves hero screen size within a documented tolerance over the supported range.
6. Backstage orbit does not change the production camera output.
7. Tail overlap, alpha fringes, and near-plane clipping are inspected at extreme supported controls.
8. Fast MIDI input does not cause camera teleports, NaNs, runaway allocation, or stuck gates.
9. Device disconnect/reconnect is handled visibly; the UI fallback remains usable.
10. Quality fallback preserves visual identity and control continuity.
11. A sustained session at target resolution stays within the agreed frame-time budget and does not accumulate GPU resources after preset switching.
12. Reduced-motion/low-flash settings avoid abrupt camera moves and flashing; performance defaults should be visually restrained.

## Coverage inventory and missing evidence

Verified: public page's high-level technology claim, preview/live policy, control labels, explanatory lab behavior; current Three.js/MIDI capabilities from official documentation.

Not verified: complete item count, full taxonomy, all per-item explanations and recipes, source JS URLs/content, actual equations, shader use, renderer sharing, camera defaults, particle/instance counts, library version, exact GPU budgets, repository availability/license, actual visual quality or responsiveness, and MIDI support in the reference itself.

Do not write “all demos reverse engineered,” “exact implementation reproduced,” “source confirmed,” or “performance tested” on this evidence. A faithful AI handover must preserve the distinction between reference observations and new KAGIXR design choices.
