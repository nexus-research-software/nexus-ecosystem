# Staged roadmap

This public execution outline describes the intended migration. Stages are milestone-based; dates will follow demonstrated readiness.

**Current status:** the organization, connector access, and two documentation repositories are established. Stage 0 acceptance work and the rest of Stage 1 remain open. No application has been refactored or qualified by this setup.

| Stage | Outcome | Exit evidence |
| --- | --- | --- |
| 0 — Establish the baseline | Freeze authoritative source identities and inventory existing functionality, interfaces, saved data, and installation paths | Capability ledger, source manifest, repeatable baseline checks, known issues, and private evidence handling |
| 1 — Establish repository boundaries | Create clean public foundations and controlled private adapter projects | Ownership map, reviewed export rules, licensing and attribution decisions, CI foundations, and repository access |
| 2 — Introduce the AI contract | Define provider-neutral requests, results, capabilities, errors, and adapter registration | Synthetic contract fixtures, compatibility policy, and public installation without private code |
| 3 — Prove the first private adapter | Move provider-specific behavior behind the interface while preserving TRACER behavior | Side-by-side acceptance evidence and a rollback path |
| 4 — Migrate every consumer | Integrate the shared provider contract across all existing application entry points | Capability parity for each consumer, including agent and background workflows |
| 5 — Qualify installation | Provide a novice-friendly install, update, repair, and rollback path | Verified Linux, Windows, and macOS installation journeys |
| 6 — Extract shared review behavior | Introduce a reusable review package without breaking document editing and evidence behavior | Stable package interfaces and passing existing review workflows |
| 7 — Deliver CLEAR, then SCOPE | Build CLEAR with PDF in its first release; follow with SCOPE | Agreed document-review acceptance criteria, PDF extraction/OCR qualification, page evidence, and review outputs |
| 8 — Prove another backend | Select and test an open-source model through a public connector | Reproducible model/runtime configuration and task-specific capability results |
| 9 — Extend agentic review | Expose qualified review capabilities through existing execution authority | Approval-aware workflow checks; separate justification and qualification for any gateway |
| 10 — Release and retire legacy paths | Publish qualified releases and remove replaced implementation only after acceptance | Release manifests, compatibility records, migration guidance, and retained rollback artifacts |

## Decisions already made

- Use a shared GitHub organization for public source and documentation.
- Keep GenAI-specific API integration behind the deployment firewall.
- Publish templates and fabricated examples, not real documents or their derived evidence.
- Target Linux, Windows, and macOS.
- Support user-supplied personal API keys where required.
- Keep local-model connectors public.
- Build CLEAR first among the new applications, with PDF in its first release.
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
