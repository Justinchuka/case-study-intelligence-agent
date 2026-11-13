#!/usr/bin/env python3
"""Mechanical checks for the skill folder.

Usage: python scripts/validate_skill.py <skill-folder>

Checks: frontmatter (name matches folder, description present and at most 1024
characters), SKILL.md under 500 lines, every referenced path exists, no empty
files, no placeholder text, all twelve modules present, the Figma example fits
its limit, and every eval case has a prompt, a case file and a grader.
Exit code 0 when all checks pass, 1 otherwise.
"""
import os
import re
import sys

MODULES = ["module-01-orchestration", "module-02-classification", "module-03-intent",
           "module-04-evidence-sufficiency", "module-05-research", "module-06-writing",
           "module-06a-adaptive-case-intelligence", "module-06a-discipline-library",
           "module-06b-visual-art-direction", "module-07-quality-assurance",
           "module-08-methodology", "module-09-output-generation",
           "module-10-execution-workflow"]
REQUIRED = ["lifecycle-protocol", "figma-prompt-protocol", "shared-operating-protocols",
            "execution-and-quality-standards", "operational-instructions",
            "appendix-a-taxonomy", "appendix-b-integrity-controls", "appendix-c-checklist"]
PLACEHOLDERS = re.compile(r"\b(TODO|TBD|FIXME|lorem ipsum)\b", re.I)
STALE = ["ten specialist modules", "expose ten stages", "Suggested first response"]
fails, passes = [], []


def check(ok, msg):
    (passes if ok else fails).append(msg)


def main(root):
    root = os.path.abspath(root)
    folder = os.path.basename(root)
    skill = os.path.join(root, "SKILL.md")
    check(os.path.isfile(skill), "SKILL.md exists")
    if not os.path.isfile(skill):
        return report()
    text = open(skill, encoding="utf-8").read()
    m = re.match(r"---\n(.*?)\n---\n", text, re.S)
    check(bool(m), "frontmatter present")
    if m:
        fm = m.group(1)
        name = re.search(r"^name:\s*(.+)$", fm, re.M)
        desc = re.search(r"^description:\s*(.+)$", fm, re.M)
        check(bool(name) and name.group(1).strip() == folder, f"name matches folder ({folder})")
        check(bool(desc) and 0 < len(desc.group(1).strip()) <= 1024,
              f"description present and <= 1024 chars ({len(desc.group(1).strip()) if desc else 0})")
        check(bool(desc) and ": " not in desc.group(1), "description has no colon-space (valid plain YAML)")
    nlines = text.count("\n") + 1
    check(nlines < 500, f"SKILL.md under 500 lines ({nlines})")
    check("13. Never start research" in text, "rule 13 (preview gate) present in SKILL.md")

    for mod in MODULES + REQUIRED:
        check(os.path.isfile(os.path.join(root, "references", mod + ".md")), f"references/{mod}.md exists")

    ref_re = re.compile(r"(?:references|scripts|examples|evals)/[A-Za-z0-9_\-./]*[A-Za-z0-9_\-/]")
    for dp, _, fns in os.walk(root):
        for fn in fns:
            p = os.path.join(dp, fn)
            rel = os.path.relpath(p, root)
            if os.path.getsize(p) == 0:
                check(False, f"{rel} is empty")
            if fn.endswith((".md", ".txt", ".yaml", ".py")):
                t = open(p, encoding="utf-8").read()
                if fn != "validate_skill.py":
                    if PLACEHOLDERS.search(t):
                        check(False, f"{rel} contains placeholder text")
                    for s in STALE:
                        if s in t:
                            check(False, f"{rel} contains stale wording: {s}")
                if fn.endswith(".md") and rel != os.path.join("evals", "validation-report.md") or fn == "validation-report.md":
                    for tok in set(ref_re.findall(t)):
                        if "*" in tok or "case-name" in tok:
                            continue
                        if not os.path.exists(os.path.join(root, tok)):
                            check(False, f"{rel} references missing path: {tok}")
    ex = os.path.join(root, "examples", "figma-prompt-example.txt")
    if os.path.isfile(ex):
        n = len(open(ex, encoding="utf-8").read().replace("\r\n", "\n").rstrip())
        check(n <= 2000, f"Figma example within 2000 characters ({n})")
    ev = os.path.join(root, "evals")
    if os.path.isdir(ev):
        for case in sorted(os.listdir(ev)):
            cp = os.path.join(ev, case)
            if not os.path.isdir(cp):
                continue
            ok = (os.path.isfile(os.path.join(cp, "prompt.md")) and os.path.isfile(os.path.join(cp, "case.yaml"))
                  and os.path.isdir(os.path.join(cp, "graders")) and os.listdir(os.path.join(cp, "graders")))
            check(ok, f"eval case complete: {case}")
    return report()


def report():
    for p in passes:
        print("PASS", p)
    for f in fails:
        print("FAIL", f)
    print(f"\n{len(passes)} passed, {len(fails)} failed")
    return 1 if fails else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1] if len(sys.argv) > 1 else "."))
