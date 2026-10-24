# Staged roadmap

This public execution outline describes the intended migration. Stages are milestone-based; dates will follow demonstrated readiness.

**Current status:** Stages 0 and 1 retain their acceptance/publication gates. Stage 2 has a public [nexus-ai prototype](https://github.com/nexus-research-software/nexus-ai) with synchronous text/schema completion, explicit selection, capability and schema-qualification controls, bounded accounting, cancellation, safe error receipts, and lazy discovery. Source and clean installed-wheel conformance pass across Linux, Windows, and macOS with Python 3.11–3.13.

An opt-in TRACER compatibility candidate passes 43 focused synthetic checks, including retained findings after later failure, unfinished coverage, cancellation, and retry/repair accounting. Its patch and detailed evidence remain private. Existing application composition and the governed private transport remain unchanged. The bridge cannot replace enforced quota handling, and it does not establish live-provider or native-workflow parity. **Next: implement and qualify the separately installed private adapter while preserving its current admission, qualification, model-policy, credential, and diagnostic protections.**

The catalog and organization foundations provide [baseline tooling](BASELINE.md), a [boundary-plan checker](BOUNDARIES.md), synthetic CI checks, a [capability ledger](CAPABILITY_LEDGER.md), and [AI contract requirements](AI_CONTRACT_REQUIREMENTS.md). Source baselines cover all supplied canonical projects. The repaired TRACER candidate passes its full Linux source suite; ATLAS, Ecosystem Manager, Cartographer, Repository Analyst, and Research Workbench pass their headless suites with skips retained. Foundry and Ledger retain failures requiring a display. The unpublished reconciled Content candidate matches RC4 test-case outcomes across five application consumers. A provisional private map accounts for all 4,133 included source files. Native/live-provider qualification, installation acceptance, application licensing and publication decisions, and detailed boundary review remain open. No application extraction or release qualification is claimed.

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

## Foundry integration across stages

Foundry is an optional coordinator for longer, multistep workflows. TRACER, CLEAR, and SCOPE retain their standalone review paths and domain rules. Applications and Foundry consume the same maintained `nexus-review` capabilities; they do not copy review logic or import another application's GUI. These are planned integrations, not completed capabilities.

### Stage 6 — Prepare the shared interfaces

- Define versioned inputs and results for review requests, findings with source evidence, proposed changes, approval decisions, revision results, and reports. Carry input revision identity and relevant run provenance so findings and approvals remain tied to the document reviewed.
- Preserve existing edit anchors, tracked-change behavior, review dispositions, cancellation, and error reporting through qualified adapters.
- Keep `nexus-review` independent of Foundry. Expose enough information for either a standalone application or a future coordinator to request human approval and apply only approved changes.
- Validate the shared interfaces against existing direct workflows before adding orchestration.

### Stage 7 — Deliver standalone CLEAR and SCOPE

- Build both applications on the shared interfaces while retaining their own rules, settings, and user experiences.
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

## Decisions still required

- Confirm application source licensing and third-party attribution before publication.
- Agree the detailed capability ledger and acceptance thresholds.
- Assign package and application ownership between the two developers.
- Qualify exact OS/CPU combinations and installation methods.
- Finalize additional provider placement when a connector is selected.
- Select the local-model test configuration at Stage 8.

## Working rule

Each stage produces reviewable changes, validation evidence, and a rollback path. Do not remove an existing capability merely because a new architecture cannot yet express it. Keep source movement, behavior changes, and new product work separately reviewable.

