# Roundhouse Account and Repository Safety SOP

**Document ID:** CIPHER-SEC-001-PUBLIC  
**Version:** 0.1.0  
**Status:** Community contribution baseline  
**Maintainer:** Roundhouse SOP maintainers  
**Last reviewed:** 2026-11-09  
**License:** Creative Commons Attribution 4.0 International (CC BY 4.0). See [LICENSES/CC-BY-4.0-NOTICE.md](../LICENSES/CC-BY-4.0-NOTICE.md).

## 1. Purpose and scope

This standard provides a repeatable, non-destructive checklist for reviewing the safety of a software project, source-code hosting account, or repository collection. It is a practical baseline, not a certification, legal opinion, penetration test, or guarantee that a system is secure.

Apply controls proportionately to the project's sensitivity, threat model, deployment model, and risk. A checklist item is not complete merely because a policy document says it is complete: record evidence, scope, reviewer, date, result, and exceptions.

### Evidence labels

Use consistent labels in every review:

- **Verified:** directly observed in authoritative configuration, source, or evidence.
- **Tested:** exercised by a reproducible scan, test, or controlled verification.
- **Documented:** stated in project documentation but not independently verified.
- **Inferred:** reasoned conclusion from observed evidence.
- **Unknown:** evidence is unavailable, incomplete, or inaccessible.

Never claim a project is secure, compliant, production-ready, or free of secrets based only on a README, one search query, or a green CI run.

### Stop-publication conditions

Pause releases and public distribution when there is:
- A live or potentially live credential, private key, recovery code, session token, or signing secret in source, history, logs, artifacts, or documentation.
- A critical/high vulnerability with a credible exploit path and no accepted mitigation.
- An unexplained exposure of private, regulated, restricted, or personal data.
- An unsafe privileged workflow that executes untrusted code with write-capable credentials.
- An unresolved rights or licensing concern affecting the material being distributed.
- A release artifact without traceable source commit and build provenance appropriate to its risk.

Do not reproduce secret values in tickets or reports. Record only the affected location, credential class, exposure window, and remediation status.

## 2. Inventory and authority

- [ ] Enumerate repositories, forks, mirrors, packages, deployments, pages, submodules, and external integrations in scope.
- [ ] Record owner, visibility, purpose, default branch, maintainers, canonical URL, and review date.
- [ ] Identify authoritative sources for code, schemas, policies, protocols, and decisions.
- [ ] Distinguish active projects, archives, experiments, mirrors, and indexes.
- [ ] Ensure indexes describe projects without claiming authority over their code or security posture.
- [ ] Verify public indexes expose only intentionally public metadata.
- [ ] Record excluded or inaccessible resources; do not imply they were reviewed.

## 3. Secrets, credentials, and private data

### Tracked content
- [ ] Scan tracked text and binary files for credential patterns and sensitive material.
- [ ] Inspect filenames and paths for environment files, keys, certificates, database dumps, backups, cookies, credential exports, and local configuration.
- [ ] Review examples, tests, notebooks, fixtures, screenshots, logs, and generated artifacts.
- [ ] Maintain ignore rules for local secrets and data, while verifying ignored files are not already tracked.
- [ ] Use obviously fake placeholders in examples.

### History and distribution
- [ ] Scan all reachable branches and tags, not only the default branch.
- [ ] Check deleted or rewritten content in Git history where feasible.
- [ ] Consider forks, clones, caches, releases, packages, CI logs, and external copies.
- [ ] Treat a deleted credential as exposed until its issuer confirms revocation or rotation.
- [ ] Revoke/rotate first; history rewriting is not a substitute for credential revocation.

### Hosting and external services
- [ ] Review secret-scanning alerts and push protection where available.
- [ ] Review repository/environment secrets, variables, deploy keys, app grants, webhooks, and token permissions where authorized.
- [ ] Review MFA, recovery methods, authorized applications, and least-privilege access.
- [ ] Review cloud, deployment, package, and data-provider credentials independently; source scans cannot inspect external secret stores.
- [ ] Separate development, staging, and production credentials.

### Incident response
1. Revoke or rotate the exposed credential at its issuer.
2. Determine permissions, affected resources, and exposure window.
3. Review provider audit logs and downstream access.
4. Remove the secret from active content and address history and derived copies as appropriate.
5. Record the incident without reproducing the value.
6. Add preventive scanning or regression tests.
7. Verify the fix and close out the incident with evidence.

## 4. Repository configuration and supply chain

- [ ] Review branch protection/rulesets and required checks.
- [ ] Restrict write permissions and workflow token permissions to the minimum needed.
- [ ] Pin third-party CI actions to reviewed immutable commit SHAs where supported.
- [ ] Review action provenance, maintainers, permissions, and transitive dependencies.
- [ ] Lock or pin dependencies where practical; triage vulnerability alerts.
- [ ] Remove unsupported runtimes and unmaintained build dependencies.
- [ ] Avoid running untrusted pull-request code with privileged secrets.
- [ ] Review workflow triggers, artifact retention, cache trust boundaries, and downloads.
- [ ] Generate an SBOM and provenance for distributable software where appropriate.
- [ ] Ensure release artifacts map to reviewed source commits and publish checksums where useful.

## 5. Code, data, and trust boundaries

- [ ] Map network, filesystem, process, parser, deserialization, database, and cryptographic boundaries.
- [ ] Enforce input type, schema, size, depth, and resource limits before expensive processing.
- [ ] Treat user content, external source material, model output, tool output, and registry metadata as untrusted.
- [ ] Never evaluate untrusted content as code, shell, SQL, templates, or privileged instructions.
- [ ] Separate raw observations, normalized records, claims, evidence references, and review conclusions.
- [ ] Preserve source identifiers, retrieval times, digests, transformations, parser versions, and lineage.
- [ ] Do not claim a hash proves truth, authorship, legality, source authenticity, or trusted time.
- [ ] Enforce source authorization and purpose restrictions; do not treat operator assertions as external authorization.
- [ ] Quarantine malformed, unauthorized, suspicious, ambiguous, or over-limit inputs with explicit reason codes.
- [ ] Make multi-output writes atomic or recoverable; test crashes and partial writes.
- [ ] Test replay, duplicate handling, revocation, stale approvals, and fail-closed behavior.
- [ ] Keep secrets and unnecessary personal data out of logs.

## 6. Privacy, licensing, and publication

- [ ] Classify content by sensitivity and intended audience.
- [ ] Minimize personal data and document purpose, access, retention, and deletion.
- [ ] Verify source terms and rights before collection, storage, transformation, redistribution, or model use.
- [ ] Track licenses and attribution for code, dependencies, datasets, documentation, images, and examples.
- [ ] Do not infer reuse rights from public repository visibility.
- [ ] Review examples, issues, screenshots, and release notes for accidental disclosure.
- [ ] Conduct a separate publication review for every public artifact.
- [ ] Keep internal findings, private repository contents, credentials, and restricted datasets out of public templates.
- [ ] State precisely which files a license covers; do not imply a document license licenses an entire repository.

## 7. CI and verification

- [ ] Confirm CI ran on the exact commit being reviewed or released.
- [ ] Investigate recent failed runs; a later green run does not explain earlier failures.
- [ ] Run appropriate unit, integration, schema, lint, type, and security tests.
- [ ] Add negative tests for malformed inputs, boundary cases, authorization failures, duplicates, and partial failures.
- [ ] Verify tests exercise the actual trust boundary.
- [ ] Use synthetic, non-sensitive fixtures.
- [ ] Record commands, versions, environment, commit, date, results, and limitations.
- [ ] Independently reproduce high-severity findings and fixes before closure.

## 8. Release gate

- [ ] Purpose, maturity, limitations, and compatibility claims are accurate.
- [ ] Intended distribution rights and third-party notices are resolved.
- [ ] Secret and private-data checks cover the release commit and relevant history.
- [ ] Critical/high findings are fixed or explicitly accepted by an authorized owner.
- [ ] CI is green on the exact release commit and recent failures are explained.
- [ ] Dependencies and workflows are reviewed.
- [ ] Version, changelog, migration notes, and artifact provenance are accurate.
- [ ] Security reporting path is usable.
- [ ] Release notes distinguish implemented, tested, documented, inferred, and unknown behavior.
- [ ] No private content or credentials are included.
- [ ] Authorized maintainer approval is recorded.

## 9. Findings and severity

Every finding should record a stable ID, date, repository/ref/commit, file or evidence locator, evidence label, severity, confidence, impact, reproduction, remediation, owner, acceptance criteria, verification method, and status. Never include secret values.

- **Critical:** confirmed compromise or severe reachable trust-boundary failure with broad impact.
- **High:** credible exploitable boundary failure, significant exposure, or privilege escalation.
- **Medium:** meaningful weakness with specific conditions or plausible operational impact.
- **Low:** limited-impact hardening or documentation defect.
- **Informational:** observation without direct security impact.

Justify severity by evidence and exploitability, not wording.

## 10. Review cadence and sign-off

Suggested minimum cadence:
- Before every public release: complete the release gate.
- Weekly: review commits, pull requests, dependency alerts, CI failures, and new configuration.
- Monthly: review inventory, access, workflows, and dependencies.
- Quarterly: history-aware secret scan, threat-model refresh, rights review, and backup restoration test.
- After an incident: perform an out-of-cycle review and preserve a non-sensitive timeline.

Review record:

| Field | Record |
|---|---|
| Review ID / window | |
| Repositories and refs covered | |
| Reviewers | |
| Tools and versions | |
| Findings by severity | |
| Excluded/inaccessible resources | |
| Accepted risks and approver | |
| Release decision | |
| Next review date | |

A review may be marked **complete with limitations**. Never mark it clean when material resources, history, settings, or alerts were inaccessible.

## 11. Community extensions

Contributors may propose language-specific controls, CI automation, test fixtures, secret-detection rules, threat models, privacy and rights controls, or measurable release gates. Each proposal must state scope, assumptions, evidence, limitations, compatibility impact, and test method.

Contributions are recommendations until reviewed and adopted by the relevant maintainers. This document is a baseline, not a certification or substitute for professional security review.

## 12. Disclaimer

The SOP is provided as general educational and operational guidance, without warranty. Adapt it to the applicable threat model and legal requirements. Maintainers and adopters remain responsible for their own systems, decisions, and verification.
