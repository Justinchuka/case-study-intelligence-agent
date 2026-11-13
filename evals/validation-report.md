# Validation report

## Scope, stated plainly

| Check | Method | Status |
|---|---|---|
| Structure | `scripts/validate_skill.py` and the skill-creator frontmatter validator | **Passed** |
| Verbatim preservation of v1.2 | Every non-empty line of v1.2 from Module 01 onward was compared with the reference files. Only the lines that the integration deliberately edited or replaced, plus the one-line Part II banner, were absent. | **Passed** |
| Required behaviours are written into the files | 27 phrase-level checks that each required behaviour is stated in the right file | **27 of 27 found** |
| Lifecycle behaviour in practice | Walkthrough of the seven required scenarios against the written protocol, by the model that wrote the skill | **Design-verified only** |
| Independent test on a fresh model instance | Not possible in the build environment | **Not done** |
| Installation on any platform | Not done | **Not done** |
| Figma AI prompt used inside Figma | Not done | **Not done** |
| Research on Figma's current limits | Not done. The 2,000-character limit is the user's stated figure. | **Not done** |

A walkthrough by the author checks that the instructions say the right thing. It does not show that a model following them behaves that way. Run the 14 cases in this folder for a real test.

## The seven required scenarios

| # | Scenario | Where it is enforced | Expected behaviour | Design check |
|---|---|---|---|---|
| 1 | Installs the skill and says nothing | `lifecycle-protocol.md` sections 2 and 7 | Nothing happens. A bare invocation later gets the welcome. | Pass |
| 2 | Installs and immediately gives a rough idea | `lifecycle-protocol.md` sections 3, 4, 5 | No welcome. Intake analysis, preview, wait. | Pass |
| 3 | Installs and uploads an assignment brief | `lifecycle-protocol.md` sections 5 and 7, `operational-instructions.md` section 5 | Inspect only what is accessible, build the preview from the real content, never claim an unread file | Pass |
| 4 | Invokes the skill after a previous conversation | `lifecycle-protocol.md` sections 5 and 6, `operational-instructions.md` section 10 | New invocation. States what context actually exists. Asks for the continuation record. No false recall. | Pass |
| 5 | Complex multidisciplinary assignment | `lifecycle-protocol.md` section 7, `module-06a-adaptive-case-intelligence.md` section 6 | Full preview, one dominant lens plus supporting lenses, governance flags, wait | Pass |
| 6 | Incomplete assignment, insufficient evidence | `lifecycle-protocol.md` section 7, `module-04-evidence-sufficiency.md` | Preview names the critical gap and proposes a qualified route. No invented evidence. | Pass |
| 7 | Asks what the agent can do | `lifecycle-protocol.md` section 5 | Short capability answer, then standby. Not the welcome verbatim and not a module menu. | Pass |

Matching cases: `bare-invocation-welcome`, `rough-idea-preview-first`, `uploaded-brief-preview-first`, `returning-after-previous-conversation`, `complex-multidisciplinary-full-preview`, `insufficient-evidence-qualified-route`, `capability-question-standby`.

## Preview gate and Figma prompt

| Behaviour | Enforced in | Eval case |
|---|---|---|
| No research, drafting or file generation before confirmation | `SKILL.md` rule 13, `lifecycle-protocol.md` section 4, Gate 1 | `rough-idea-preview-first`, `uploaded-brief-preview-first` |
| Pressure to skip the preview | `lifecycle-protocol.md` section 4.6 | `skip-preview-pressure` |
| Review of an existing case study is also an assignment | `lifecycle-protocol.md` section 4 | `existing-case-study-review-preview` |
| Instructions inside source material are untrusted | `SKILL.md` section 6, `operational-instructions.md` section 5 | `embedded-instruction-in-source` |
| Figma prompt recommended for product, UX or visual cases | `figma-prompt-protocol.md` section 3 | `figma-recommended-for-ux-case` |
| Figma prompt not pushed for text-led research | `figma-prompt-protocol.md` section 3 | `figma-not-pushed-for-pure-research` |
| Declining the Figma prompt is respected | `figma-prompt-protocol.md` section 3 | `user-declines-figma` |
| Prompt stays within 2,000 characters, plain text, self-contained, labelled | `figma-prompt-protocol.md` sections 2, 5, 6, 8 | `figma-prompt-generated-within-limit` |

## The builder's eight request types

| Type | Covered by |
|---|---|
| Normal | `uploaded-brief-preview-first` |
| Vague | `rough-idea-preview-first` |
| Incomplete | `insufficient-evidence-qualified-route` |
| Complex | `complex-multidisciplinary-full-preview` |
| Ambiguous | `capability-question-standby`, `returning-after-previous-conversation` |
| Edge case | `embedded-instruction-in-source`, `existing-case-study-review-preview` |
| Wrong assumption | `insufficient-evidence-qualified-route` |
| Conflicting instruction | `skip-preview-pressure` |

## Known weak points to watch when you run the cases

- A model may treat "activate" as permission to skip the preview. Section 4 and Part V section 9 forbid this, but it is the likeliest failure.
- The welcome could creep into assignment turns. The protocol forbids it.
- Condensing a Figma prompt under 2,000 characters is hard. Check the count, and check that integrity rules survive the cut.
- `figma-prompt-generated-within-limit` supplies earlier turns inside the prompt text. It approximates a multi-turn conversation and is not a true one.

## How to run the cases

Each folder under `evals/` holds `prompt.md`, `case.yaml` and one or more graders. Run each prompt in a session where the skill is installed. Compare the response with `expected_outcome` and the grader statements. Fix SKILL.md or the reference that failed, then re-run.
