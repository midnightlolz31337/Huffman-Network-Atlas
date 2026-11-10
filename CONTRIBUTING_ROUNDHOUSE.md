# Contributing to the Roundhouse SOP

Thank you for helping improve the Roundhouse safety checklist.

## What is in scope

Useful contributions include:
- Concrete, testable security controls.
- Framework- or language-specific checklists.
- Reproducible CI checks and synthetic test fixtures.
- Threat models and abuse-case analysis.
- Secret-scanning patterns with false-positive guidance.
- Privacy, licensing, data provenance, and supply-chain controls.
- Clearer evidence labels, review records, and release gates.

## Contribution requirements

Every proposal should include:
1. The risk or gap being addressed.
2. Affected systems and trust boundaries.
3. Assumptions and prerequisites.
4. Evidence supporting the recommendation.
5. A practical verification or test method.
6. Limitations, false-positive risks, and compatibility impact.
7. References and attribution for third-party material.

Prefer small, focused pull requests. Explain whether a change is normative (“must”), recommended (“should”), or optional (“may”). Avoid vague requirements that cannot be verified.

## Safety and privacy rules

- Never submit credentials, private keys, recovery codes, session tokens, personal data, private repository contents, or restricted datasets.
- Use synthetic fixtures and clearly fake placeholders.
- Do not include exploit payloads or operational details beyond what is necessary to explain and safely verify a defensive control.
- Report suspected vulnerabilities through the affected project's published private reporting channel, not a public issue.
- Do not assume a contributor has authority to change the policy of a project indexed by this Atlas.

## Review and adoption

A pull request is a proposal, not an automatic policy change. Maintainers review technical accuracy, scope, evidence, licensing, privacy, and compatibility before adoption. Contributors should identify material changes and tests. Maintainers may request revisions or decline proposals that are unsubstantiated, unsafe, or out of scope.

## Licensing

Contributions to the public Roundhouse SOP document are offered under CC BY 4.0, consistent with the document's license notice. This does not change the license status of the rest of this repository. By submitting a contribution, you confirm that you have the right to contribute it under those terms and that third-party material is properly attributed and compatible.
