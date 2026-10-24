# Execution status — 2026-10-24

**Current phase: 3 — prove the first private adapter.** A separately installable
offline candidate is implemented and checkpointed. Phase 3 is not accepted for
production selection yet. Existing application defaults and authoritative sources
remain in place. CLEAR with PDF remains the first new application, after shared
review extraction; Foundry remains optional.

| Phase | Current evidence | Remaining exit condition |
| --- | --- | --- |
| 0 — Baselines | Canonical source identities, capability inventory and baseline evidence captured | Native/live checks and joint acceptance of remaining baseline issues |
| 1 — Repository boundaries | Three public repositories, ownership mapping, boundary tooling, and phase/status merge template | Original-source publication/licensing decisions and internal project import |
| 2 — AI contract | `nexus-ai 0.1.0.dev2`; 69 source and installed-wheel tests pass in nine CI environments; private TRACER bridge has 43 focused checks | Consumer acceptance before treating the interface as stable |
| 3 — Private adapter | 242 source tests and the same 242 installed-wheel tests pass offline on Linux/Python 3.12; private import/CI/recovery handoff prepared | Internal/native/live qualification and application parity; no default switch |
| 4 — Consumer migration | Consumer requirements and boundaries identified | Prove one opt-in route, then each remaining application entry point |
| 5 — Installation | Shared public package has cross-platform wheel checks | Novice application install/update/repair/rollback journeys |
| 6 — Shared review | Planned interfaces and ownership | Extract and qualify reusable behavior without a Foundry dependency |
| 7 — CLEAR, then SCOPE | CLEAR PDF requirement retained | Build and jointly accept standalone applications |
| 8 — Another backend | Public connector placement agreed | Select model/runtime/hardware, implement and measure it |
| 9 — Foundry | Optional workflow plan recorded | Qualified shared review and consumer migration, then supervised pilot |
| 10 — Releases | No application release or legacy retirement claimed | All release gates, migration guidance and retained rollback |

## This execution checkpoint

- [Organization PR 1](https://github.com/nexus-research-software/.github/pull/1)
  added the phase/status/checkpoint merge format. Documentation-only validation.
- [AI contract PR 3](https://github.com/nexus-research-software/nexus-ai/pull/3)
  preserved normalized termination reasons when an adapter fails before returning
  a result. All nine CI jobs passed; the merged tree matches the tested tree.
- The private adapter was mechanically separated from the existing runtime and
  tested as an installed package. Its 192 retained characterization tests and 50
  new facade tests cover admission, retries, repairs, concurrency, cancellation,
  qualification scope, strict output validation, safe errors and private receipts.
- A private Git bundle, built candidate, provenance manifest, test evidence and
  internal setup instructions provide a recoverable handoff. They are intentionally
  absent from this public catalog. No internal remote push or registry upload has
  been performed from this workspace.

The public package CI matrix is Linux, Windows and macOS with Python 3.11, 3.12 and
3.13. Its results do not establish native application support or private adapter
support on all those systems. The private candidate's evidence is currently Linux
and Python 3.12 only. No actual provider request was made during this checkpoint.

## Recovery and merge records

Public recovery branches named `checkpoint/20261024-phase2` retain these pre-change
revisions:

| Repository | Recovery revision |
| --- | --- |
| `.github` | `3906a30eebe0a02101f11757c9a9a641edc8c387` |
| `nexus-ai` | `c455da0b392f76eb86cba5f0383aa1e41c711fce` |
| `nexus-ecosystem` | `3649868758220b0e3cbc4ddc3d4031363e2f5d16` |

Private C00 retains the complete pre-change TRACER copy. Private C01 retains the
Phase 3 adapter history and validated package. Restore into a new checkout and
verify the bundle and manifest. Use reviewed revert commits for shared branches;
do not erase checkpoint refs or rewrite shared main history.

Every merge includes the phase, status, validation, remaining gates, next step,
checkpoint and rollback instructions. Exact tested heads and merged trees are
recorded in the corresponding merge commits. There is no application-default
rollback needed at this checkpoint because the existing route is still active.

## Next execution gate

Import the prepared candidate into the approved private Git service and configure
its internal package source and runner. Run the offline checks there, then native
and approved live synthetic qualification. Prove one opt-in application route with
the existing quota protections and full diagnostic parity before migrating all
consumers. Retain unqualified functionality on the original route until accepted.

Outstanding decisions remain application licensing/attribution, developer ownership,
native installation combinations and joint acceptance thresholds. The first local
model and its hardware can still be chosen at Phase 8.
