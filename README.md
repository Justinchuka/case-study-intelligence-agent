# Case Study Intelligence Agent (skill)

An evidence-governed, multidisciplinary AI skill that helps you interpret, research, analyse, write, review and produce credible case studies: academic, business, consulting, UX and product portfolio, engineering, AI and data, healthcare, policy, teaching, and failure or incident cases. For visual cases it can also prepare an optional **Figma AI prompt** (at most 2,000 characters) that you paste into Figma to generate the case study's design frames.

It is built from the Case Study Intelligence Agent Master Prompt v1.2, with a new installation, initialisation and first-use lifecycle and a mandatory plan-preview step.

## What you get when you use it

| You do | The agent does |
|---|---|
| Invoke it with no assignment ("activate", "start") | Gives a short welcome and waits |
| Ask "what can you do?" | Answers briefly and waits |
| Give a rough idea, a brief, documents, data, screenshots or an existing case study | Interprets it, then shows you a **plan preview** and waits for your confirmation |
| Confirm the plan | Researches (if allowed and available), writes, reviews its own work and produces the outputs |
| Have a product, UX or visual case | Recommends a Figma AI prompt, with a reason. It is added only if you agree. |
| Have a purely research or text-led case | Does not push the Figma prompt |

**The plan preview is always shown before work starts.** You can change it, then confirm. Nothing is researched, drafted or generated until you do.

## Outputs

| Output | Notes |
|---|---|
| Written case study | Markdown, DOCX or PDF, where the platform has file tools |
| Slide deck or visual layout | Format chosen from your request and the tools available |
| Tables, charts, diagrams | Only where the evidence supports them |
| **Figma AI prompt** | A separate design brief, plain text, at most 2,000 characters, copyable or exported as `.txt`. It is not the finished case study. The written case study supplies the full copy. |

## Install

Installation is the platform's job. The skill cannot see it happen and produces no message at install time. If you install it and say nothing, nothing happens, which is correct.

| Platform | How |
|---|---|
| Platforms with skill support | Upload the ZIP (or `.skill` file) through the platform's skill upload, or place the `case-study-intelligence-agent/` folder in its skills directory. Steps differ by platform; check its documentation. |
| Claude Code | Place the folder in a personal or project skills directory (check current documentation for the exact path). |
| Platforms without skill support | Add SKILL.md as instructions and the `references/` files as project knowledge or attachments. SKILL.md routes to the reference files, and without them the agent loses most of its specialist depth. |

After installing, invoke it with something like "Activate the Case Study Intelligence Agent", or just describe your case study.

## Capabilities depend on your platform

Installing the skill does not give the AI memory across conversations, background work, independent agents, web research, file creation, or access to apps you have not connected. Whatever the platform provides is what the agent can use, and it will tell you plainly when something is unavailable.

## Folder layout

```
case-study-intelligence-agent/
├── SKILL.md                      router: identity, rules, lifecycle summary, reference routing
├── README.md
├── LICENSE                       MIT
├── references/
│   ├── lifecycle-protocol.md     authoritative start-up, welcome, standby, preview gate
│   ├── figma-prompt-protocol.md  when to offer, how to write, 2,000-character rules
│   ├── module-01 ... module-10   the specialist modules, plus 06A and 06B
│   ├── shared-operating-protocols.md · execution-and-quality-standards.md · operational-instructions.md
│   └── appendix-a-taxonomy.md · appendix-b-integrity-controls.md · appendix-c-checklist.md
├── examples/                     illustrative transcripts, previews and a fictional Figma prompt
├── evals/                        14 test cases, plus validation-report.md
└── scripts/
    ├── validate_skill.py         structure and path checks
    └── check_prompt_length.py    character count for a Figma prompt
```

## Where each part of the v1.2 master prompt went

| v1.2 section | File |
|---|---|
| Master Activation Instruction, Non-negotiable rules | `SKILL.md` (sections 1-2) |
| Part I, Module 01 | `references/module-01-orchestration.md` |
| Modules 02, 03, 04, 05, 06 | `module-02-classification.md`, `module-03-intent.md`, `module-04-evidence-sufficiency.md`, `module-05-research.md`, `module-06-writing.md` in `references/` |
| Module 06A sections 1-4, 6-12 | `references/module-06a-adaptive-case-intelligence.md` |
| Module 06A section 5 (disciplines A-O) | `references/module-06a-discipline-library.md` |
| Module 06B | `references/module-06b-visual-art-direction.md` |
| Modules 07, 08, 09, 10 | `module-07-quality-assurance.md`, `module-08-methodology.md`, `module-09-output-generation.md`, `module-10-execution-workflow.md` in `references/` |
| Part III, IV, V | `shared-operating-protocols.md`, `execution-and-quality-standards.md`, `operational-instructions.md` |
| Appendices A, B, C | `appendix-a-taxonomy.md`, `appendix-b-integrity-controls.md`, `appendix-c-checklist.md` in `references/` |

The five-part structure and all modules are preserved. Module text is carried over verbatim except for the integration changes below.

## Integration changes from v1.2

| Where | Change |
|---|---|
| Part V section 1 (first contact) | Superseded. `lifecycle-protocol.md` is the single authoritative protocol. |
| Part V section 3 (first response) | "Otherwise begin" and "execute directly" replaced by preview, then confirm |
| Part V sections 2-3, Module 03, Module 10, Part IV section 1 (duplicated intake) | Consolidated into one activation sequence in `lifecycle-protocol.md`. Module text stays intact and cross-refers to it. |
| Part V section 9 | Added: "activate", "start" or "run" is an invocation with no assignment, and never skips the preview |
| Part V section 10 | Added pointer: a returning user is a new invocation |
| Part IV section 1 | Step 4 now includes the preview and confirmation. The stale "ten stages" wording is corrected. |
| Part IV Gate 1 | Now includes "user has confirmed the preview". No gates renumbered. |
| Part III section 3 | Added ownership rows for 06A, 06B and the preview gate |
| Part III section 7, Module 10 section 4 | Starting execution and adding an unrequested output format now need approval. Routine work needs none after the preview is confirmed. |
| Module 01 | Added a visual-art-director role, 06A and 06B in the layer list, and a lifecycle cross-reference in section 7 |
| Module 03 section 7 | The compact preview still applies to straightforward work |
| Module 06A | Section 5 split into its own file, with a pointer left behind |
| Module 06B section 12 | Cross-reference to the Figma protocol |
| Module 07 section 7 | Note on scoring visual quality; maximum stays 40 |
| Module 09 section 2, Module 10 workflow E | Figma AI prompt added as a separate output type |
| Appendix C | Added a pre-execution preview item |
| SKILL.md | Added non-negotiable rule 13 (no execution before a confirmed preview) and an autonomy sentence |

## Testing and limits

- Structure was checked with `scripts/validate_skill.py` and the frontmatter validator that ships with the skill-creator skill.
- Every verbatim claim was checked by comparing each reference file with the v1.2 source; only the lines listed above differ.
- The lifecycle and preview behaviour was **design-verified by walkthrough**, by the same model that wrote the skill. It has **not** been run on a fresh model instance, and it has not been installed on any platform. See `evals/validation-report.md`. Run the cases in `evals/` to test it for real.
- The Figma AI prompt is untested in Figma. The 2,000-character limit is the user's stated figure and has not been checked against Figma's current documentation.
- Creating the ZIP is not publishing to GitHub.

## Licence

MIT. See `LICENSE`. Edit the copyright line to name the holder you want.
