# Staged roadmap

This public execution outline describes the intended migration. Stages are milestone-based; dates will follow demonstrated readiness. Phase numbers identify outcomes, not a requirement to finish every private gate before advancing unrelated public work.

**Execution order changed on 2026-10-24: complete feasible public work first.**
Private adapter integration is deferred at its existing checkpoint. Public
contracts, synthetic/injected-transport testing, public connectors, content and
review components, applications, and installation tooling may proceed in dependency
order without waiting for internal access. Source-publication decisions, model
selection, and actual acceptance evidence still apply. See the detailed
[public-first work sequence and gates](PUBLIC_FIRST.md).

**Current focus: public P4b CLEAR usability and acceptance preparation, following the P4a standalone candidate.** Public P1/P2 and the P3a/P3b/P3c contract, OCR and optional AI review increments are implemented; Phase 8's actual model qualification remains open. Phase 3 has an offline candidate; acceptance remains open and its internal work is deferred. Stages 0 and 1 retain their acceptance/publication gates. Stage 2 has a public [nexus-ai prototype](https://github.com/nexus-research-software/nexus-ai), version `0.1.0.dev2`, with synchronous text/schema completion, explicit selection, capability and schema-qualification controls, bounded accounting, cancellation, safe error receipts, and lazy discovery. All 69 source and clean installed-wheel tests pass across Linux, Windows, and macOS with Python 3.11–3.13. Adapter failures retain normalized termination evidence as well as usage and call counts. A separate public synthetic adapter example exercises installation, explicit selection between two fabricated backends, and removal; it does not qualify a real model.

The new public [compatible chat connector](https://github.com/nexus-research-software/nexus-provider-openai-compatible)
implements explicit immutable profiles, expiring instance-bound qualification,
text/schema mapping, single-attempt HTTP dispatch, strict model/output validation,
safe receipts, bounded bodies, and cooperative cancellation/deadlines. Its offline
tests and installable package complete the P2 implementation scope. Real HTTP/model,
task-quality, context-capacity and application/native acceptance remain separate.
The existing shared runtime and private candidate pins are unchanged.

P3a introduces [nexus-content](https://github.com/nexus-research-software/nexus-content)
and [nexus-review](https://github.com/nexus-research-software/nexus-review), both
`0.1.0.dev0`. New read-only PDF extraction binds source bytes, processing settings,
page text and exact quotes; scanned/mixed/failed coverage stays explicit. Shared
review contracts retain completed findings, bounded reports and explicit change
plans/approval records, with strict JSON and escaped HTML. The synthetic example
uses a deterministic rule and performs no edits. P3a does not replace the original
Content/RC4 candidate, qualify OCR, invoke a model, or establish existing-consumer
parity. P3b advances both packages to `0.1.0.dev1`, adding explicit local
PDFium/Tesseract rendering and OCR with source/raster/runtime/text provenance,
controlled subprocesses, limits, cancellation and retained progress. Generation-one
text-only snapshots are preserved; generation-two OCR text remains unverified and
visible in review reports. The synthetic native baseline passes on all nine
OS/Python combinations; representative OCR accuracy is a separate acceptance gate.
P3c advances review to `0.1.0.dev2` with optional `nexus_review.ai`. Explicit provider,
model/configuration and schema qualification govern whole-page reviews. Exact quote
occurrences bind findings to evidence; bounded calls, attempts, repairs and timeouts
retain usage and prior findings through interruption. Unknown usage remains unknown.
Strict AI reports bind backend/run receipts to change plans and approvals. The
53 base-only and 100 combined source/installed-wheel tests pass in nine environments;
69 AI and 67 connector regressions also pass. Actual review/model quality remains
open. P4a now adds [standalone CLEAR](https://github.com/nexus-research-software/nexus-clear),
`0.1.0.dev0`: a desktop/CLI PDF wording-review candidate with 45 base / 52 combined
application tests, exact page findings, explicit local OCR, saved evidence and two
fabricated backend examples. The application composes the shared packages without
copying parsers, transports or review loops. Its narrow starter checklist makes no
legal-risk or contract-clearance claim. P4b next improves PDF preview, review
controls and explicit OCR/provider setup. Joint criteria, real-model qualification,
representative OCR and full native application acceptance remain open, while
consumer/revision qualification proceeds as publication decisions permit.

An opt-in TRACER compatibility candidate passes 43 focused synthetic checks, including retained findings after later failure, unfinished coverage, cancellation, and retry/repair accounting. Its patch and detailed evidence remain private. Existing application composition and the governed private transport remain unchanged. The bridge cannot replace enforced quota handling, and it does not establish live-provider or native-workflow parity.

The separately installable private adapter candidate passes 242 offline source tests and the same 242 tests from a clean installed wheel on Linux/Python 3.12, without an application installation. Those checks include 192 retained runtime cases and 50 new adapter cases. Private code, configuration, diagnostic evidence and recovery bundles remain outside public repositories. **Deferred private gate:** internal import, internal/native/live qualification, and one opt-in consumer route remain required before changing private application defaults. They no longer block unrelated public implementation. See [status and recovery checkpoints](STATUS.md) for completed work and remaining gates.

The catalog and organization foundations provide [baseline tooling](BASELINE.md), a [boundary-plan checker](BOUNDARIES.md), synthetic CI checks, a [capability ledger](CAPABILITY_LEDGER.md), and [AI contract requirements](AI_CONTRACT_REQUIREMENTS.md). Source baselines cover all supplied canonical projects. The repaired TRACER candidate passes its full Linux source suite; ATLAS, Ecosystem Manager, Cartographer, Repository Analyst, and Research Workbench pass their headless suites with skips retained. Foundry and Ledger retain failures requiring a display. The unpublished reconciled Content candidate matches RC4 test-case outcomes across five application consumers. A provisional private map accounts for all 4,133 included source files. Native/live-provider qualification, installation acceptance, application licensing and publication decisions, and detailed boundary review remain open. No original-application extraction or release qualification is claimed; CLEAR is newly authored public candidate code.

| Stage | Outcome | Exit evidence |
| --- | --- | --- |
| 0 — Establish the baseline | Freeze authoritative source identities and inventory existing functionality, interfaces, saved data, and installation paths | Capability ledger, source manifest, repeatable baseline checks, known issues, and private evidence handling |
| 1 — Establish repository boundaries | Create clean public foundations and controlled private adapter projects | Ownership map, reviewed export rules, licensing and attribution decisions, CI foundations, and repository access |
| 2 — Introduce the AI contract | Define provider-neutral requests, results, capabilities, errors, and adapter registration | Synthetic contract fixtures, compatibility policy, and public installation without private code |
| 3 — Prove the first private adapter | Move provider-specific behavior behind the interface while preserving TRACER behavior | Side-by-side acceptance evidence and a rollback path |
| 4 — Migrate every consumer | Integrate the shared provider contract across all existing application entry points | Capability parity for each consumer, including agent and background workflows |
| 5 — Qualify installation | Provide a novice-friendly install, update, repair, and rollback path | Verified Linux, Windows, and macOS installation journeys |
| 6 — Extract shared review behavior | Introduce reusable review, findings, proposed-change, and approval interfaces for applications and future Foundry workflows | Versioned interfaces with no Foundry dependency; passing existing editing, evidence, and approval workflows |
| 7 — Deliver CLEAR, then SCOPE | Build standalone applications on the shared review interfaces; CLEAR with PDF first, then SCOPE | Agreed review acceptance criteria, PDF extraction/OCR qualification, page evidence, and review outputs; installation and use without Foundry |
| 8 — Prove another backend | Select and test an open-source model through a public connector | Reproducible model/runtime configuration and task-specific capability results |
| 9 — Add optional Foundry workflows | Pilot supervised TRACER review and revision, then extend to CLEAR and SCOPE where demonstrated value justifies it | Preserved direct reviews, evidence, and approvals; measured quality, manual effort, latency, and model usage; separate qualification for any gateway |
| 10 — Release and retire legacy paths | Publish qualified releases and remove replaced implementation only after acceptance | Release manifests, compatibility records, migration guidance, and retained rollback artifacts |

Public-only workflows may reach release readiness independently of the private
adapter when all of their own gates pass. A public release must state its tested
providers and unsupported workflows explicitly. It must not replace an existing
installation or retire its legacy path on the strength of synthetic checks alone.

## Foundry integration across stages

Foundry is an optional coordinator for longer, multistep workflows. TRACER, CLEAR, and SCOPE retain their standalone review paths and domain rules. Applications and Foundry consume the same maintained `nexus-review` capabilities; they do not copy review logic or import another application's GUI. These are planned integrations, not completed capabilities.

### Stage 6 — Prepare the shared interfaces

- Define versioned inputs and results for review requests, findings with source evidence, proposed changes, approval decisions, revision results, and reports. Carry input revision identity and relevant run provenance so findings and approvals remain tied to the document reviewed.
- Preserve existing edit anchors, tracked-change behavior, review dispositions, cancellation, and error reporting through qualified adapters.
- Keep `nexus-review` independent of Foundry. Expose enough information for either a standalone application or a future coordinator to request human approval and apply only approved changes.
- Validate the shared interfaces against existing direct workflows before adding orchestration.

### Stage 7 — Deliver standalone CLEAR and SCOPE

- Build both applications on the shared interfaces while retaining their own rules, settings, and user experiences. P4a delivers the first CLEAR candidate; P4b prepares usable reviewer controls and acceptance evidence.
- Verify installation and normal reviews without Foundry on Linux, Windows, and macOS.
- Keep CLEAR's first PDF release independent of Stage 9. Qualify extraction/OCR, page evidence, and review reports; arbitrary PDF rewriting is outside this initial commitment.
- Follow with SCOPE after CLEAR's acceptance gates pass.

### Stage 9 — Pilot, measure, and expand

Prerequisites are qualified shared review behavior and Foundry's provider migration. Planning the interfaces earlier must not turn Foundry integration into a release dependency for Stage 7.

1. Add `document.review` and `document.revise` through Foundry's supported public API and trusted execution boundaries, using `nexus-review`. Qualify any new API capabilities explicitly. Validate staged inputs, output schemas, approved changes, and artifact paths; retain Foundry's control of execution authority.
2. Pilot TRACER on synthetic documents: review → propose revisions → obtain human approval → apply approved changes → re-review → export findings and revision evidence.
3. Compare the pilot with TRACER's direct workflow using the same fixtures and a recorded provider/model configuration. Agree acceptance thresholds jointly for finding quality, evidence fidelity, manual effort, end-to-end latency, and model usage. Check interruption, resume, cancellation, and rollback.
4. Extend to CLEAR where coordinating PDF extraction/OCR, related contract checks, and uncertain findings helps reviewers. Extend to SCOPE where coordinating checks of objectives, tasks, deliverables, and acceptance criteria improves the workflow. Qualify each application separately.
5. Release these workflows as optional features only after acceptance. If a workflow does not demonstrate sufficient value, retain direct reviews and defer that integration.

**Acceptance requirement:** enabling or disabling Foundry must preserve each application's existing direct review capabilities, evidence, approval rules, and saved results. Disabling integration must not silently discard an in-progress run; preserve its state and artifacts and make the status explicit. Model-generated findings may vary; assess them against agreed quality criteria rather than requiring identical text.

Backend selection remains independent of orchestration. Generic AI interactions use the public `nexus-ai` contract; GenAI-specific integration remains private, and local-model connectors remain public. Foundry's execution authority is separate from model-provider selection. Any new host controls, remote gateway, or production Hermes execution requires its own justified scope and qualification.

No additional repository is required solely for this integration. Keep reusable review behavior in `nexus-review`, orchestration in Foundry, and application-specific policy in each application.

## Decisions already made

- Use a shared GitHub organization for public source and documentation.
- Keep GenAI-specific API integration behind the deployment firewall.
- Publish templates and fabricated examples, not real documents or their derived evidence.
- Target Linux, Windows, and macOS.
- Support user-supplied personal API keys where required.
- Keep local-model connectors public.
- Build CLEAR first among the new applications, with PDF in its first release.
- Keep Foundry optional for TRACER, CLEAR, and SCOPE; prepare shared interfaces in Stage 6 and pilot orchestration in Stage 9 without delaying CLEAR.
- Select the first local model and hardware later.
- Complete feasible public work before resuming internal private-repository work; retain separate public, private, and application acceptance evidence.

## Decisions still required

- Confirm original application-source licensing and third-party attribution before source publication, and licensing before any package/application release.
- Agree the detailed capability ledger and acceptance thresholds.
- Assign package and application ownership between the two developers.
- Qualify exact OS/CPU combinations and installation methods.
- Finalize additional provider placement when a connector is selected.
- Select the local-model test configuration at Stage 8.

## Working rule

Each stage produces reviewable changes, validation evidence, and a rollback path. Do not remove an existing capability merely because a new architecture cannot yet express it. Keep source movement, behavior changes, and new product work separately reviewable.

Every merge must record its phase, completed behavior, validation environment and results, remaining gates, next step, checkpoint, tested revision and rollback procedure in both the review description and merge commit. Retain recovery refs; verify the merged tree against the tested tree. A passing package test suite does not close application acceptance gates.

