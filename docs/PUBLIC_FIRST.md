# Public-first execution order

**Decision — 2026-10-24:** complete all feasible public work before resuming
private-repository integration. The architecture and no-loss requirement remain
the same; the dependency order changes. An internal adapter acceptance gate is
not a prerequisite for building independent public components.

The existing Phase 3 candidate remains at its private checkpoint. No internal
software installation, repository import, credential, runner setup, or private
merge is needed for the public milestones below. The existing private candidate
can retain its tested dependency pin while the public work proceeds.

## Ordered public milestones

Phase references preserve the original [roadmap](ROADMAP.md). The milestones
below describe execution order, not additional product versions or acceptance
claims. Work can advance past a blocked item when its actual dependencies permit.

| Order | Work and owning repository | Public exit evidence | Dependency or remaining decision |
| --- | --- | --- | --- |
| P1 — complete | `nexus-ai`: developer path with separately installed synthetic providers, explicit selection, metadata-only discovery, strict receipts and schemas | [PR 4](https://github.com/nexus-research-software/nexus-ai/pull/4): clean shared/provider wheel installs, switching and removal checks pass in all nine CI environments | Synthetic walkthrough only; no real model or private service qualified |
| P2 | Public compatible connector: explicit configuration, injected transport tests, errors, cancellation, deadlines, bounded attempts, scoped qualification and model identity | Installable connector passing transport/contract tests without a real endpoint; no hidden retries or service fallback | A real runtime/model and hardware are needed only for live qualification; connector repository and tested protocol scope must be established |
| P3 | `nexus-content` and `nexus-review`: content/provenance and review/findings/proposed-change/approval interfaces, then reusable implementations | Synthetic text/scanned/mixed PDF fixtures; page evidence and extraction/OCR checks; versioned review interfaces; independent wheel checks | Extracted original source needs publication/licensing/attribution review; preserve consumer behavior and compare existing tests |
| P4 | CLEAR: standalone PDF review built on the shared interfaces | A synthetic end-to-end workflow and a separately qualified real public-backend workflow; page-grounded findings, explicit incomplete coverage and reports | P3, qualified backend, joint review criteria; arbitrary PDF rewriting is outside the first release |
| P5 | Installation and catalog: acquire, install, launch, update, repair and roll back selected applications | Novice journeys on Linux, Windows and macOS; pinned compatibility records and synthetic first-run checks | Test actual OS/CPU/package combinations; original Ecosystem Manager source publication remains gated |
| P6 | Existing consumers and SCOPE: opt-in shared interfaces and backend selection, then SCOPE on accepted review components | Public routes retain domain behavior, evidence, saved results and approvals; SCOPE follows CLEAR acceptance | Publication decisions for extracted sources, consumer-specific parity, qualified backend; retain private/legacy routes until separately accepted |
| P7 | Optional Foundry workflows: shared review/revision interfaces and a supervised public-backend pilot | Explicit approvals, artifact identity, interruption/resume and measured value against the direct workflow | Qualified review components and Foundry's public provider route; execution authority remains with Foundry |
| P8 | Public release preparation | Reproducible packages, installation evidence, release/compatibility notes, synthetic examples, recovery checkpoints and an exact supported-workflow list | Licensing, native acceptance, actual model results and joint acceptance; publish only the subset whose gates are met |

Installation work can start alongside component development; end-to-end novice
qualification requires a usable application. Consumer migration can proceed as
each needed interface becomes qualified. SCOPE waits for CLEAR acceptance, while
Foundry stays optional and cannot delay CLEAR. A fabricated model response is
useful for interface testing but is not evidence of useful review quality.

## What remains private

Provider-specific GenAI integration, protected configuration, private tests and
diagnostics remain in the private deliverable. Public code contains provider-neutral
contracts, application behavior approved for publication, synthetic fixtures,
and permitted public connectors. It must not embed private transport behavior,
connection details, actual documents, or their derived evidence.

When public development reaches a dependency that requires private integration,
resume the preserved candidate through the approved internal handoff: internal
package/CI validation, native and live qualification, and application parity.
Those gates remain explicitly pending until supported by internal results. No
remote access to the private machine is assumed by this execution plan.

## Keep interface drift visible

- Keep exact contract package, interface generation, connector version and
  configuration/evidence identity in compatibility records. The current contract
  remains experimental; public development does not declare it stable.
- Use synthetic negative cases for unknown/unsupported capabilities, changed
  configuration or schema, missing providers, cancellation, partial workflows,
  timeout, usage/accounting, and mismatched model identity.
- Keep reusable behavior in its owning package. A separately packaged example
  may demonstrate a boundary without creating another production repository.
- Record private compatibility as pending when a public interface changes. Do not
  infer a private pass from a public fake or silently advance its dependency pin.
- Preserve the original application route and saved data until the applicable
  consumer acceptance gate passes. New public routes are opt-in during migration.

## Checkpoints and completion criteria

Every merge retains the established phase/status format: completed behavior,
validation and environment, remaining gates, next step, recoverable base, tested
head, and rollback procedure. Verify the merged tree matches the tested tree.
Keep checkpoint refs immutable and revert shared changes through reviewed commits.

The public-first starting checkpoints are:

| Repository | `checkpoint/20261024-public-first-start` |
| --- | --- |
| `nexus-ai` | `0a302724d1bffd9af3daaa8e0f5f700ccd309fb1` |
| `nexus-ecosystem` | `4e40ccb9e1aa675083ef21cf26b061197bfb87a2` |

Private C00 and C01 remain retained. They are not copied into public history.

Public development is complete for a milestone only when its implementation,
tests, installation evidence, documentation, and recovery path are present.
Application acceptance additionally requires the agreed capability/quality and
platform evidence. Whole-ecosystem completion still requires the deferred private
and cross-provider gates. These are different claims and must be reported separately.

The next decisions should be requested only when they block concrete work:
publication/licensing for existing sources, a runtime/model/hardware for actual
public inference, and joint quality thresholds. Until then, continue independent
public work using new code and fabricated fixtures.
