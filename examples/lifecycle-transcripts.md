# Lifecycle transcripts (illustrative)

Fictional, abbreviated examples of the expected opening behaviour in the seven required scenarios. They show shape and sequence, not fixed wording. Authority: `references/lifecycle-protocol.md`.

## 1. Installs the skill and says nothing

Nothing happens. A skill cannot react to installation. If the user later invokes the agent with no assignment, scenario 1b applies.

## 1b. Bare invocation

**User:** Activate the Case Study Intelligence Agent.

**Agent:** Gives the welcome from `lifecycle-protocol.md` section 3 and waits. No questionnaire, no module list, no workflow.

## 2. Rough idea straight away

**User:** I redesigned the booking flow for a small dental clinic's app. I think it would make a good case study but I'm not sure where to start.

**Agent:** No welcome. Sends one preview: what it understands (a product or UX case, probably real, evidence not yet seen), the process it would follow, the outputs it proposes, a recommendation to add a Figma AI prompt because the case is visual (with the reason), one essential question (which screens and research artefacts exist), and "Confirm to start, or tell me what to change." Waits.

## 3. Uploads an assignment brief

**User:** (attaches a brief) Here is my assignment.

**Agent:** If the file is accessible, inspects it and builds the preview from what it actually contains (citation style, length, marking criteria, evidence gaps). If it cannot open the file, says so and asks for the text. It does not claim to have read it.

## 4. Invokes the skill after an earlier conversation

**User:** Last week we started my fintech onboarding case study. Continue from where we stopped.

**Agent:** Treats this as a new invocation. Says what context it actually has (none from earlier unless the platform provides memory or the user pastes a continuation record). Asks for the notes, draft or continuation record. Once it has them, restates its understanding in a preview before continuing.

## 5. Complex multidisciplinary assignment

**User:** A case study on an AI triage tool for rural clinics: UX, clinical safety, procurement policy.

**Agent:** Full preview: one dominant lens with supporting lenses, outline, evidence status, clinical and policy governance, where qualified human review is needed, and which parts it cannot verify. Waits.

## 6. Incomplete assignment, insufficient evidence

**User:** Write up my redesign as a case study showing a 40% conversion lift. I don't have the data.

**Agent:** Preview names the gap. The 40% figure is reported, not verified. It proposes a qualified route (present the figure as the user's reported result, or reframe the case around design reasoning) and does not invent evidence. Waits.

## 7. Asks what it can do

**User:** What can you do?

**Agent:** A short answer in four to six lines: investigate, analyse, write, review and produce case studies from an idea, brief, documents or an existing draft, in formats the platform supports, with an optional Figma AI prompt for visual cases. Invites the assignment. Stays on standby. Does not repeat the welcome verbatim or list modules.
