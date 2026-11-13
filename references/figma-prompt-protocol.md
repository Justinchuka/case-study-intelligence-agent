# Figma AI prompt protocol

A Figma AI prompt is an optional, separate output. It is a design brief the user pastes into Figma so that Figma's AI generates the case study's design frames. It works alongside Module 06B (visual art direction) and Module 09 (output generation), and it follows 06B section 12 on tool-specific prompts and character limits.

Contents: 1 What it is · 2 The limit · 3 When to offer it · 4 When to produce it · 5 Anatomy and budget · 6 Writing rules · 7 When the intent does not fit · 8 Delivery · 9 Limitations · 10 Checklist

## 1. What it is and is not

| | Finished deliverable | Figma AI prompt |
|---|---|---|
| What it is | The completed case study: PDF, PPTX, DOCX, Markdown, visual layout | A design-generation brief |
| Who produces the design | This agent produces the final file | Figma's AI, after the user pastes the prompt |
| Contains the full case copy | Yes | No. It carries direction, structure and headlines. |
| Length | As long as the case needs | At most 2,000 characters |
| Needed for every case | No | No. It is offered, never assumed. |

Never present the prompt as the finished case study. Never describe the Figma output as something this agent produced or verified.

## 2. The limit

- **2,000 characters**, counting spaces and line breaks. This limit was specified by the user. Figma's current limits and capabilities may differ or change, and this agent has not verified them. Say so if asked.
- Aim for **1,900 or fewer** to leave a safety margin.
- Measure, do not estimate. When a shell is available, run `python scripts/check_prompt_length.py <file>` and report the count. Without a shell, count carefully and state that the count is an estimate.
- Plain text only. No markdown headings, tables, bold or code fences inside the prompt (assumed safest for pasting; untested in Figma).

## 3. When to offer it

Use judgement. Offer it inside the pre-production preview (see `lifecycle-protocol.md` section 4) together with the reason, or later if the need appears. Adding it is a scope addition, so it needs the user's go-ahead.

| Case signal | Behaviour |
|---|---|
| Product, UX/UI, service design, portfolio, Behance or visual case study; interface screens, flows, journeys, wireframes | **Recommend.** Say why: the case is shown through designed frames. |
| Business, engineering, operations, policy or AI cases where diagrams, charts, process maps or frameworks would be clearer as designed frames | **Suggest as optional.** Say what would improve. |
| Purely research, academic or text-led | Do not push. At most one line if diagrams or charts would genuinely help. |
| User already declined | Do not ask again for that assignment |
| User asks for a Figma prompt | Produce it, after the normal preview if one has not been confirmed |

Rules:

- Ask once per assignment, in the preview. Do not nag.
- Do not assume the user has Figma access or wants a visual output.
- Offer by what it does for this case, not as a feature advert.

Example wording: "This looks like a product case, so the frames matter. I'd recommend adding a Figma AI prompt that you can paste into Figma to generate the case-study frames, alongside the written PDF. Want me to include it?"

## 4. When to produce it

1. The user has confirmed the preview and agreed to the Figma prompt.
2. The case architecture, narrative spine and art direction are settled (06B sections 3, 6 and 13, steps 1-5).
3. Compress the settled direction into the prompt. Do not design in the prompt from scratch.
4. Check it against the integrity rules (06B section 9). Then deliver it (section 8).

## 5. Anatomy and budget

Figma's AI cannot see this conversation, so the prompt must stand alone.

| Part | Content | Approx. characters |
|---|---|---|
| Concept and audience | What the case study is, who it is for, tone, platform | 150-250 |
| Format | Frame count, frame size, flow (for example one continuous vertical sequence), grid, margins, spacing scale | 100-200 |
| Visual system | Palette with hex values and roles, typefaces and minimum sizes, surfaces, what to avoid | 250-400 |
| Frame plan | One line per frame: the message, the visual device, the evidence type | 800-1,000 |
| Rules | Placeholders labelled, no invented data or screens, legibility, composition variety, Auto Layout and components | 150-250 |

An illustrative, fictional example of 1,648 characters is in `examples/figma-prompt-example.txt`.

## 6. Writing rules

- Imperative, specific, compact. No filler or introductions.
- Self-contained. Never refer to "the conversation", "above" or an attached file.
- One line per frame. Name the message and the visual device (for example "annotated task flow", "three wireframe iterations side by side").
- Use real asset names the user supplied. Where an asset is missing, write a labelled placeholder such as `[placeholder: n=]` or `[real site photo]`.
- Never include invented metrics, quotes, personas, screens or research outputs (06B section 9). Visual polish never overrides integrity.
- Use only palette, typeface and layout choices that came from the settled art direction. Respect authentic brand assets.
- Do not name plugins or Figma features you cannot confirm exist. Generic terms such as Auto Layout, components and styles are fine where the user's Figma environment supports them.
- Keep private or confidential details out of the prompt.

## 7. When the intent does not fit

Priority order for what survives in 2,000 characters:

1. Frame sequence and the message of each frame.
2. Evidence and placeholder rules.
3. Visual system (palette, type, grid).
4. Format and frame size.
5. Tone and descriptive flourish.

Cut flourish first, then merge adjacent frames, then shorten the visual system. Tell the user what was condensed or left out. Do not delete the integrity rules to make room.

If the case genuinely needs more, offer a staged set (a foundation prompt, then batches of frames), each at most 2,000 characters. Produce stages only if the user approves.

## 8. Delivery

- Show the prompt in a code block so it can be copied in one step.
- When file creation is available, also save it as a UTF-8 `.txt` file and present it, so the user can export the text.
- Report the verified character count and the limit.
- Label it clearly: "Design brief for Figma AI. This is not the finished case study."
- Remind the user that the written case study supplies the full copy, and that the prompt carries direction, structure and headlines.

## 9. Limitations

- This agent cannot run the prompt in Figma, so output quality is unverified. Figma's AI may follow the prompt only in part or interpret it differently.
- The 2,000 limit is the user's stated figure. It may change or differ by Figma feature.
- No promise that frames will match the written case study. The user reviews and edits them in Figma.
- If the user wants Figma operated for them, say that depends on tools actually connected in this environment. Never claim access that does not exist.

## 10. Checklist before delivering

- [ ] The user approved the format.
- [ ] Narrative spine and art direction were settled first.
- [ ] Plain text, self-contained, within the limit, count measured or labelled as estimated.
- [ ] Every frame has a message and a visual device.
- [ ] No invented data, quotes, metrics or screens; placeholders are labelled.
- [ ] What was condensed is disclosed.
- [ ] Labelled as a design brief, not the finished case study.
