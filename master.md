# CLIP CUTTER 01 — MASTER PROJECT INSTRUCTIONS

## 0. PROJECT MISSION

Build a professional AI-powered video clipping and finishing application that turns long-form videos into genuinely engaging, publishable short-form content.

The product must combine:

1. Intelligent clip discovery.
2. Context-aware video cutting.
3. Automatic silence and dead-space removal.
4. Smart face and subject tracking.
5. Intelligent reframing and split-screen layouts.
6. Professional captions and typography.
7. Cinematic effects and motion.
8. Audio enhancement and pacing.
9. Customizable editing presets.
10. Human review and refinement.
11. Reliable video rendering and export.
12. A premium, intuitive user experience.

**Primary objective:** Produce clips that feel deliberately edited by a skilled human, not automatically assembled by generic AI software.

A technically functioning clip generator that produces boring, poorly framed, or unwatchable videos is not a successful product.

---

# PART 1 — MULTI-AGENT SYSTEM

## 1. AVAILABLE AGENTS

The development environment consists of:

- Codex
- Gemini Pro
- Local Ollama model

All agents must collaborate toward the same project objective.

### Agent A — Codex: Engineering & Implementation

Primary responsibilities:

1. Analyze the existing codebase.
2. Implement approved features.
3. Design reliable software components.
4. Handle video-processing logic.
5. Write and maintain tests.
6. Debug runtime and integration errors.
7. Optimize performance.
8. Maintain code quality.
9. Implement rendering and export workflows.
10. Preserve backward compatibility where appropriate.

Codex must not blindly rewrite working functionality.

### Agent B — Gemini Pro: Research, Architecture & Creative Direction

Primary responsibilities:

1. Analyze product requirements.
2. Research appropriate implementation approaches.
3. Design system architecture.
4. Review clip-selection algorithms.
5. Define editing styles and presets.
6. Evaluate UI/UX decisions.
7. Review Codex's proposed implementations.
8. Identify overlooked edge cases.
9. Suggest improvements to video quality.
10. Evaluate results against product goals.

Gemini must distinguish verified findings from assumptions.

### Agent C — Local Ollama: Supporting Analysis & Validation

Primary responsibilities, within the model's actual capabilities:

1. Summarize project documentation.
2. Analyze small, relevant code sections.
3. Review transcripts.
4. Classify content.
5. Evaluate candidate clips using supplied context.
6. Generate structured suggestions.
7. Perform lightweight independent reviews.
8. Assist with documentation.
9. Identify possible inconsistencies.
10. Reduce unnecessary reliance on paid models where reliable.

Do not assign tasks that exceed the local model's available context, hardware, or reasoning capabilities.

## 2. AGENT COLLABORATION RULES

1. All agents must use the same documented requirements.
2. Assign a clear owner to each task.
3. Parallelize independent work when supported by the orchestration environment.
4. Do not allow multiple agents to modify the same files simultaneously without coordination.
5. Maintain one authoritative task board and project status.
6. Share decisions, blockers, and test results through a common workspace.
7. Require independent review for major architectural changes.
8. Resolve disagreements using evidence, experiments, and product requirements.
9. Do not use model voting as proof of correctness.
10. If an agent fails, report the failure instead of pretending the task succeeded.
11. Avoid circular conversations between agents.
12. Use local models for suitable lightweight tasks; use stronger models when complexity justifies them.
13. Never invent successful tool execution or test results.
14. Never allow an agent to overwrite approved work without authorization.

## 3. STANDARD DEVELOPMENT WORKFLOW

For each feature:

1. Understand the requirement.
2. Inspect existing implementation.
3. Identify dependencies and constraints.
4. Produce a concise implementation plan.
5. Review risks and edge cases.
6. Assign implementation ownership.
7. Implement in small, testable changes.
8. Run automated tests.
9. Perform independent review.
10. Test against real media.
11. Inspect actual output.
12. Fix identified problems.
13. Update project documentation.
14. Mark the feature complete only when acceptance criteria pass.

Do not confuse implementation completion with product-quality completion.

---

# PART 2 — VIDEO INTELLIGENCE

## 4. SOURCE VIDEO ANALYSIS

Before editing, analyze the available source material.

Extract or determine:

1. Video duration.
2. Resolution and frame rate.
3. Audio quality.
4. Spoken language.
5. Transcript with timestamps.
6. Word-level timestamps when reliable.
7. Speaker identities or anonymous speaker labels.
8. Speaker transitions.
9. Silence and speech regions.
10. Major topic changes.
11. Relevant visual events.
12. Scene transitions.
13. Visible faces and important subjects.
14. Emotional changes where reasonably inferable.
15. Important statements and narrative developments.

Preserve the relationship between audio timestamps, transcript segments, and video frames.

Do not invent unavailable metadata.

## 5. INTELLIGENT CLIP DISCOVERY

The application must identify moments that viewers would genuinely want to watch.

Evaluate candidate clips for:

1. Immediate hook strength.
2. Curiosity.
3. Emotional impact.
4. Humor.
5. Surprise.
6. Interesting facts.
7. Educational value.
8. Storytelling.
9. Conflict and resolution.
10. Clear explanations.
11. Strong opinions with sufficient context.
12. Memorable statements.
13. Meaningful reactions.
14. Narrative completeness.
15. Potential audience interest.

Use multiple signals instead of selecting clips from keywords alone.

### Selection principles

- Understand what is being said.
- Understand why the moment matters.
- Examine surrounding context.
- Prefer complete narrative moments.
- Avoid clips that begin or end mid-thought.
- Reject generic or uninteresting segments.
- Never create clips merely to satisfy a target quantity.

### Candidate ranking

Produce explainable candidate scores for:

- Hook
- Context
- Clarity
- Narrative payoff
- Visual suitability
- Audio suitability
- Overall potential

Scores are heuristic estimates, not guarantees of virality.

## 6. YOUTUBE RETENTION SIGNALS

When available and legitimately accessible:

1. Examine audience-retention information.
2. Identify replayed or highly watched segments.
3. Compare these regions with transcript content.
4. Use retention signals to suggest promising candidates.
5. Evaluate whether the moments make sense independently.
6. Avoid blindly copying popular timestamps.
7. Never claim retention data exists when it is unavailable.
8. Respect platform access restrictions and applicable permissions.

Retention is a supporting signal, not the sole selection criterion.

---

# PART 3 — CUTTING & PACING

## 7. SILENCE REMOVAL

The application must distinguish between unnecessary dead space and intentional pauses.

Detect:

1. Extended silence.
2. Unnecessary hesitation.
3. Repeated filler.
4. Unproductive gaps.
5. Long pauses between completed thoughts.
6. Dead space before and after meaningful dialogue.

Preserve:

1. Dramatic pauses.
2. Comedic timing.
3. Emotional reactions.
4. Natural conversational rhythm.
5. Necessary breathing space.
6. Pauses that improve comprehension.

Never remove every silence indiscriminately.

## 8. CONTEXT-AWARE CUTTING

1. Analyze audio and transcript together.
2. Identify meaningful sentence boundaries.
3. Detect complete ideas.
4. Preserve important context.
5. Avoid cutting individual words.
6. Avoid abrupt audio joins.
7. Avoid unnatural sentence combinations.
8. Avoid changing the meaning of speech.
9. Maintain chronological integrity unless a deliberate, non-misleading rearrangement is justified.
10. Ensure every edit improves pacing or clarity.

Provide configurable cutting modes:

- Conservative
- Balanced
- Aggressive

Aggressive mode must still preserve meaning and intelligibility.

## 9. HOOK OPTIMIZATION

The opening 1–2 seconds must provide a compelling reason to continue watching whenever the source supports it.

Potential hook types:

1. Surprising statement.
2. Direct question.
3. Immediate conflict.
4. Unexpected fact.
5. Emotional reaction.
6. Strong visual moment.
7. Unresolved curiosity.
8. Interesting outcome followed by explanation.

Do not manufacture hooks by misleadingly rearranging speech.

Do not use identical hook structures for every video.

## 10. STORY STRUCTURE

Prefer a natural progression:

**Hook → Context → Development → Payoff**

This is a guiding framework, not a mandatory rigid template.

A good clip must:

1. Establish interest quickly.
2. Provide sufficient context.
3. Maintain logical continuity.
4. Avoid unnecessary repetition.
5. Reach a meaningful conclusion.
6. End intentionally.

If a candidate lacks a meaningful payoff, reject it or recommend manual review.

---

# PART 4 — SMART CROP & CAMERA

## 11. FACE-AWARE REFRAMING

1. Detect visible faces.
2. Identify the active speaker when possible.
3. Track face positions over time.
4. Maintain appropriate headroom.
5. Avoid cutting foreheads, chins, or important expressions.
6. Keep the main subject within safe framing boundaries.
7. Avoid unnecessary camera movement.
8. Smooth tracking movements.
9. Handle temporary occlusion.
10. Handle subjects leaving the frame.
11. Handle multiple visible faces.
12. Handle speaker transitions.
13. Preserve important gestures where practical.
14. Avoid zooming so far that image quality becomes unacceptable.

**Critical rule: Never accept a crop that destroys the primary visual subject.**

## 12. MULTI-SPEAKER LAYOUTS

When two or more people are visible or speaking, consider:

1. Split-screen.
2. Side-by-side.
3. Stacked layouts.
4. Active-speaker switching.
5. Wider framing.
6. Reaction-aware composition.

Choose layouts according to:

- Number of visible subjects.
- Speaker activity.
- Original framing.
- Screen space.
- Facial expressions.
- Visual importance.
- Target aspect ratio.

Do not use split-screen automatically if it creates poor framing.

## 13. SUBJECT-AWARE CROPPING

When no face is visible, prioritize:

1. Main objects.
2. Demonstrations.
3. Screen recordings.
4. Gameplay.
5. Relevant text.
6. Diagrams.
7. Important visual actions.

The crop must preserve what viewers need to understand the content.

## 14. ASPECT RATIOS

Support:

- 9:16 vertical.
- 16:9 landscape.
- 1:1 square.

Allow custom output dimensions later.

Reframing must be evaluated independently for each output format.

---

# PART 5 — CAPTIONS & TYPOGRAPHY

## 15. CAPTION GENERATION

1. Generate captions from verified speech transcription.
2. Align captions accurately with audio.
3. Use word-level timing when sufficiently reliable.
4. Preserve punctuation.
5. Correct obvious transcription errors through verification.
6. Handle names and technical terminology carefully.
7. Support multiple languages where available.
8. Prevent captions from overlapping important visual elements.
9. Avoid excessively long caption lines.
10. Respect platform-safe areas.

## 16. TYPOGRAPHY CONTROLS

Provide customizable:

1. Font family.
2. Font weight.
3. Font size.
4. Text alignment.
5. Horizontal position.
6. Vertical position.
7. Line spacing.
8. Letter spacing.
9. Text color.
10. Highlight color.
11. Stroke.
12. Shadow.
13. Background box.
14. Background opacity.
15. Rounded corners.
16. Maximum words per caption.
17. Caption animation.
18. Animation duration.

## 17. CAPTION PRESETS

Initial presets:

### Clean Minimal
- Restrained typography.
- High readability.
- Subtle animation.
- Suitable for interviews and professional content.

### Bold Creator
- Large readable captions.
- Selective keyword emphasis.
- Controlled scale animation.
- Suitable for energetic short-form content.

### Documentary
- Refined typography.
- Balanced spacing.
- Minimal animation.
- Cinematic visual consistency.

### Dynamic Highlight
- Word-level emphasis.
- Carefully timed motion.
- Strong visual hierarchy.
- No unnecessary animation.

### Custom
- User-defined settings.
- Save and reuse configurations.

## 18. CAPTION QUALITY RULES

1. Never animate every word unnecessarily.
2. Never use the same font treatment for every content type.
3. Avoid excessive colors.
4. Maintain contrast.
5. Preserve readability on small screens.
6. Avoid distracting animation.
7. Ensure captions match the spoken content.
8. Never place captions over faces when avoidable.
9. Keep animations synchronized with speech.
10. Allow users to override automatic decisions.

---

# PART 6 — VISUAL STYLES & EFFECTS

## 19. STYLE PRESETS

Support distinct visual identities.

### A. Clean Podcast
- Natural colors.
- Stable framing.
- Readable captions.
- Minimal effects.
- Speaker-focused editing.

### B. Cinematic Documentary
- Controlled contrast.
- Subtle motion.
- Refined typography.
- Intentional pacing.
- Restrained transitions.

### C. High-Energy Creator
- Faster pacing.
- Selective punch-ins.
- Dynamic captions.
- Strong emphasis.
- Beat-aware transitions when appropriate.

### D. Phonk / Dramatic
- Beat-synchronized cuts.
- Black-screen transitions.
- High-impact typography.
- Controlled zooms.
- Dramatic pauses.
- Optional flashes and shakes with intensity and accessibility limits.

### E. Educational
- Clear typography.
- Highlighted information.
- Contextual overlays.
- Diagrams when appropriate.
- Minimal distraction.

### F. Custom
- User-defined effects and settings.

## 20. EFFECTS LIBRARY

Support suitable combinations of:

1. Zoom-in.
2. Zoom-out.
3. Punch-in.
4. Pan.
5. Smooth reframing.
6. Fade.
7. Hard cut.
8. Black-frame transition.
9. Motion blur.
10. Speed ramp.
11. Freeze frame.
12. Text emphasis.
13. Controlled shake.
14. Highlight overlay.
15. Blur background.
16. Color adjustments.
17. Contrast changes.
18. Vignette.
19. Beat-synchronized transitions.
20. Picture-in-picture.

Not every effect belongs in every clip.

## 21. EFFECT INTELLIGENCE

Effects must be chosen based on:

1. Content type.
2. Emotional tone.
3. Narrative importance.
4. Speaker movement.
5. Audio rhythm.
6. Visual composition.
7. User-selected style.
8. Accessibility and viewing comfort.

Avoid:

- Random zooms.
- Constant shaking.
- Unnecessary flashes.
- Excessive transitions.
- Repetitive animation.
- Distracting overlays.
- Visual effects that obscure the subject.

## 22. BLACK-SCREEN / PHONK EFFECTS

Provide an optional dramatic editing preset supporting:

1. Brief black-frame interruptions.
2. Beat-aligned transitions.
3. High-impact text.
4. Contrast shifts.
5. Controlled motion effects.
6. Intentional audio synchronization.

Do not apply this style to unrelated documentary, educational, or professional content unless explicitly selected.

Avoid dangerous or uncomfortable flashing patterns.

---

# PART 7 — AUDIO ENGINE

## 23. AUDIO PROCESSING

1. Detect speech regions.
2. Identify silence.
3. Preserve natural speech.
4. Reduce unwanted background noise where practical.
5. Normalize dialogue levels.
6. Prevent clipping.
7. Avoid harsh audio joins.
8. Apply appropriate crossfades.
9. Maintain audio-video synchronization.
10. Preserve emotional delivery.

## 24. MUSIC & SOUND EFFECTS

1. Support optional background music.
2. Support user-provided licensed tracks.
3. Apply automatic music ducking.
4. Detect beats when appropriate.
5. Synchronize selected effects.
6. Preserve dialogue intelligibility.
7. Avoid excessive sound effects.
8. Prevent abrupt music endings.
9. Support music-free exports.
10. Respect music licensing requirements.

Do not add music simply because the feature exists.

---

# PART 8 — EDITING STUDIO

## 25. PRODUCT MODES

Provide two distinct workflows.

### Mode A — AI Clip Finder & Finishing Studio

This is the default product experience.

Workflow:

1. Import video.
2. Analyze content.
3. Generate ranked clip candidates.
4. Preview selected moments.
5. Choose clips.
6. Apply editing presets.
7. Adjust crop and captions.
8. Refine effects.
9. Preview finished clips.
10. Export approved results.

The user should not need professional editing knowledge.

### Mode B — Full Video Editor

This mode is available only when explicitly selected.

Do not turn the default interface into a complicated professional editor.

Full editor capabilities may include:

1. Multi-track timeline.
2. Manual trimming.
3. Clip splitting.
4. Audio tracks.
5. Text layers.
6. Effect layers.
7. Transitions.
8. Keyframes.
9. Manual cropping.
10. Export controls.

Implement this progressively, not as a prerequisite for the core product.

## 26. USER CONTROL

Users must be able to:

1. Approve or reject clips.
2. Adjust start and end times.
3. Restore removed segments.
4. Modify captions.
5. Change crop positions.
6. Select alternate layouts.
7. Enable or disable effects.
8. Change editing presets.
9. Adjust music levels.
10. Preview modifications.
11. Undo and redo changes.
12. Export without destructive modifications.

Automatic editing must remain reversible.

---

# PART 9 — USER INTERFACE & EXPERIENCE

## 27. DESIGN DIRECTION

Create a premium, modern, practical interface.

Visual principles:

1. Clean.
2. Minimal.
3. Professional.
4. Consistent.
5. Responsive.
6. Intuitive.
7. Visually polished.
8. Efficient for frequent use.

Avoid generic AI-generated dashboards.

Avoid unnecessary gradients, excessive cards, oversized spacing, and decorative elements that do not serve the workflow.

## 28. MAIN APPLICATION SECTIONS

### Project Library
- Existing projects.
- Import new video.
- Recent work.
- Project status.

### Analysis Workspace
- Video preview.
- Processing progress.
- Transcript.
- Detected speakers.
- Candidate clips.

### Clip Selection
- Ranked candidates.
- Clip previews.
- Scores and explanations.
- Duration.
- Approval controls.

### Finishing Studio
- Video preview.
- Crop settings.
- Caption settings.
- Style presets.
- Effects.
- Audio controls.

### Export
- Format.
- Resolution.
- Quality.
- Output location.
- Export progress.
- Final preview.

## 29. UX REQUIREMENTS

1. Keep the main workflow simple.
2. Avoid exposing unnecessary technical settings.
3. Provide advanced controls when requested.
4. Show real processing progress.
5. Explain errors clearly.
6. Allow users to cancel operations safely.
7. Preserve unfinished work.
8. Make previews responsive.
9. Avoid blocking the interface during processing.
10. Never claim processing is complete before the output is ready.

---

# PART 10 — ENGINEERING & PERFORMANCE

## 30. DEVELOPMENT ENVIRONMENT

The current development machine uses:

- Arch Linux.
- NVIDIA RTX 4050 Laptop GPU with 6 GB VRAM.
- Approximately 16 GB system RAM.
- Intel Core i5 13th-generation CPU.

Verify the actual runtime environment before choosing dependencies or execution strategies.

## 31. PERFORMANCE REQUIREMENTS

1. Prioritize efficient processing.
2. Avoid unnecessary model loading.
3. Reuse cached intermediate results.
4. Process long videos in manageable segments.
5. Avoid loading entire videos into memory.
6. Use GPU acceleration where supported.
7. Provide CPU fallbacks.
8. Monitor memory and VRAM consumption.
9. Prevent simultaneous heavy tasks from exhausting hardware.
10. Keep the interface responsive.
11. Support task cancellation.
12. Handle failed jobs safely.
13. Avoid redundant rendering.
14. Prefer preview-quality rendering during editing.
15. Render full quality only when required.

## 32. TECHNICAL DECISION RULES

1. Inspect the existing stack before proposing changes.
2. Prefer proven libraries and maintainable components.
3. Do not add dependencies without justification.
4. Avoid premature microservices.
5. Keep modules independently testable.
6. Separate analysis from rendering.
7. Separate editing decisions from media files.
8. Store edits as structured, reversible project data.
9. Maintain reproducible exports.
10. Use appropriate background job processing.
11. Log meaningful errors.
12. Avoid excessive complexity.
13. Do not rewrite stable modules without evidence.
14. Design interfaces that can support future improvements.
15. Document important architectural decisions.

## 33. SECURITY & PRIVACY

1. Treat uploaded videos as untrusted files.
2. Validate file formats and metadata.
3. Protect against unsafe file paths.
4. Prevent command injection in media-processing pipelines.
5. Avoid exposing private user files.
6. Protect API credentials.
7. Never hardcode secrets.
8. Apply reasonable processing limits.
9. Prevent unauthorized access to projects.
10. Keep temporary files controlled.
11. Clean up safely after failed operations.
12. Never transmit private videos to external services without explicit user authorization.
13. Preserve local processing where supported and selected.
14. Avoid logging sensitive content unnecessarily.
15. Design for future authentication and usage limits without prematurely implementing billing.

---

# PART 11 — QUALITY ASSURANCE

## 34. AUTOMATED TESTING

Test:

1. Video import.
2. Unsupported formats.
3. Corrupted media.
4. Audio extraction.
5. Transcription alignment.
6. Silence detection.
7. Cut boundary accuracy.
8. Speaker changes.
9. Face detection.
10. Crop stability.
11. Split-screen layouts.
12. Caption synchronization.
13. Effect rendering.
14. Audio synchronization.
15. Export integrity.
16. Cancellation.
17. Project recovery.
18. Low-memory conditions.
19. Missing GPU support.
20. Regression scenarios.

## 35. REAL VIDEO TESTING

Use a representative test collection containing:

1. Single-speaker podcasts.
2. Two-person interviews.
3. Multi-speaker conversations.
4. Educational lectures.
5. Documentary footage.
6. Videos without visible faces.
7. Screen recordings.
8. Noisy audio.
9. Low-quality footage.
10. Long-form source material.

Evaluate actual rendered outputs, not just metadata or successful process exit codes.

## 36. VIDEO QUALITY SCORECARD

Evaluate each candidate and final export on:

1. Hook effectiveness.
2. Narrative coherence.
3. Context preservation.
4. Pacing.
5. Framing.
6. Caption accuracy.
7. Typography.
8. Audio quality.
9. Effect appropriateness.
10. Overall publishability.

Use configurable, explainable scoring criteria.

A high automated score does not replace human judgment.

## 37. RELEASE-BLOCKING FAILURES

Reject or flag clips containing:

1. Missing or clipped speech.
2. Misleading sentence combinations.
3. Incomplete narratives.
4. Important faces cut off.
5. Severe crop jitter.
6. Unreadable captions.
7. Incorrect caption timing.
8. Audio distortion.
9. Broken transitions.
10. Unintentional black frames.
11. Missing visual content.
12. Failed rendering.
13. Corrupted output.
14. Unsupported factual claims presented as verified.
15. Serious synchronization errors.

Human approval is mandatory before publishing.

---

# PART 12 — PRODUCT STRATEGY

## 38. PRIMARY TARGET USERS

1. YouTube creators.
2. Podcast creators.
3. Interview channels.
4. Educational creators.
5. Documentary creators.
6. Social media editors.
7. Agencies managing short-form content.

## 39. PRODUCT DIFFERENTIATION

Compete through:

1. Better clip understanding.
2. Context-preserving cuts.
3. More intelligent cropping.
4. Professional caption styles.
5. Deliberate effects.
6. Customizable presets.
7. Reliable rendering.
8. Human-in-the-loop editing.
9. Consistent output quality.
10. Transparent editing decisions.

Do not compete merely by generating more clips.

## 40. BUSINESS MODEL — LATER PHASE

The eventual product may use:

- Paid subscriptions.
- Limited free usage.
- Processing quotas.
- Export limits.
- Premium presets.
- Higher processing allowances.

Do not implement billing until the core product reliably produces desirable results.

---

# PART 13 — DEVELOPMENT PRIORITIES

## 41. PHASE 1 — RELIABLE CLIP ENGINE

Deliver:

1. Video import.
2. Audio extraction.
3. Timestamped transcript.
4. Silence detection.
5. Context-aware clip discovery.
6. Candidate ranking.
7. Non-destructive cutting.
8. Basic clip preview.
9. Reliable export.

**Acceptance condition:** Generate coherent clips with natural cuts and no critical audio or context failures.

## 42. PHASE 2 — SMART FRAMING

Deliver:

1. Face detection.
2. Face tracking.
3. Stable reframing.
4. Speaker-aware framing.
5. Split-screen layouts.
6. Subject-aware fallback.
7. Crop preview and adjustment.

**Acceptance condition:** Main subjects remain appropriately framed throughout tested clips.

## 43. PHASE 3 — PROFESSIONAL FINISHING

Deliver:

1. Accurate captions.
2. Typography presets.
3. Caption animation.
4. Style presets.
5. Selected transitions.
6. Audio balancing.
7. Music ducking.
8. Effect preview.
9. Export customization.

**Acceptance condition:** Results look intentional, readable, synchronized, and professionally finished.

## 44. PHASE 4 — POLISHED PRODUCT

Deliver:

1. Project library.
2. Refined interface.
3. Reliable processing states.
4. Project recovery.
5. Undo and redo.
6. Batch processing where appropriate.
7. Performance improvements.
8. Expanded quality tests.
9. Stable export workflow.

**Acceptance condition:** A user can complete the core workflow without developer assistance.

## 45. PHASE 5 — ADVANCED FEATURES

Only after the core product is stable:

1. Full timeline editor.
2. Advanced keyframes.
3. More sophisticated effects.
4. Additional AI models.
5. Expanded style libraries.
6. Batch workflows.
7. Optional cloud processing.
8. Account management.
9. Subscription billing.
10. Commercial launch infrastructure.

---

# PART 14 — NON-NEGOTIABLE RULES

1. Quality over quantity.
2. Actual results over impressive explanations.
3. Working implementations over mock demonstrations.
4. Research before major architectural decisions.
5. Understand existing code before modifying it.
6. Preserve approved work.
7. Never overwrite source videos.
8. Never fabricate test results.
9. Never invent source material.
10. Never misrepresent spoken content.
11. Never add effects without purpose.
12. Never accept visibly broken framing.
13. Never assume a rendered video is good merely because export succeeded.
14. Never hide known defects.
15. Never introduce unnecessary complexity.
16. Never use generic AI-generated design patterns without considering usability.
17. Never claim a feature is complete without testing it.
18. Never silently change requirements.
19. Never let agents make conflicting edits without coordination.
20. Never prioritize monetization before product quality.

---

# PART 15 — FIRST EXECUTION INSTRUCTIONS

When receiving this document:

1. Read the entire requirements document.
2. Inspect the existing repository.
3. Identify the actual technology stack.
4. Determine which features already exist.
5. Identify incomplete or unreliable implementations.
6. Identify architectural problems.
7. Identify unnecessary complexity.
8. Determine current test coverage.
9. Identify available hardware acceleration.
10. Check the current development environment.
11. Evaluate the existing video-processing pipeline.
12. Determine whether current clips are genuinely publishable.
13. Identify the highest-impact improvements.
14. Create a prioritized development backlog.
15. Divide responsibilities between Codex, Gemini, and Ollama.
16. Define measurable acceptance criteria.
17. Establish safe working practices and non-destructive edits.
18. Begin with the highest-priority verified problem.
19. Implement and test one coherent improvement at a time.
20. Report actual progress and remaining blockers.

## REQUIRED INITIAL REPORT

Provide:

- Current project status.
- Existing working features.
- Broken or incomplete features.
- Major technical risks.
- Video-quality weaknesses.
- Recommended architecture adjustments.
- Prioritized development plan.
- Agent responsibilities.
- Immediate next task.
- Definition of done for that task.

Keep reports precise and evidence-based.

Do not spend excessive time generating planning documents instead of building.

## FINAL INSTRUCTION

You are not building another generic AI clipping demonstration.

You are building a real video production tool intended to compete on the quality of its output.

The system must understand content before cutting, preserve meaning, frame subjects intelligently, apply effects deliberately, and give users meaningful control.

**A smaller product that consistently produces excellent clips is more valuable than a feature-rich application that produces mediocre videos.**

Build accordingly.