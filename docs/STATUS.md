# Execution status — 2026-10-24

**Current focus: public P3c AI review adaptation and accounting.** Public P1/P2
and the P3a/P3b content/review and native OCR increments are implemented. Full P3, actual Phase 8 model
qualification and application acceptance remain open.
The execution order now prioritizes every feasible public milestone before
resuming internal private-repository work. Phase 3 remains at its implemented
offline checkpoint and is not accepted for production selection. Existing
application defaults and authoritative sources remain in place. CLEAR with PDF
remains the first new application, after shared review extraction; Foundry remains
optional. See the [public-first sequence](PUBLIC_FIRST.md) for dependencies and
separate public/private acceptance gates.

| Phase | Current evidence | Remaining exit condition |
| --- | --- | --- |
| 0 — Baselines | Canonical source identities, capability inventory and baseline evidence captured | Native/live checks and joint acceptance of remaining baseline issues |
| 1 — Repository boundaries | Six public repositories, ownership mapping, boundary tooling, and phase/status merge template | Original-source publication/licensing decisions and internal project import |
| 2 — AI contract | `nexus-ai 0.1.0.dev2`; 69 source and installed-wheel tests pass in nine CI environments; private TRACER bridge has 43 focused checks | Consumer acceptance before treating the interface as stable |
| 3 — Private adapter | Deferred at the retained offline checkpoint: 242 source and 242 installed-wheel tests on Linux/Python 3.12; private handoff prepared | Internal/native/live qualification and application parity when private work resumes; no default switch |
| 4 — Consumer migration | Consumer requirements and boundaries identified | Prove one opt-in route, then each remaining application entry point |
| 5 — Installation | AI, compatible provider, content and review packages have cross-platform wheel checks; synthetic-provider selection/removal checks implemented | Novice application install/update/repair/rollback journeys |
| 6 — Shared review | P3a/P3b implemented: exact PDF evidence, optional native rendering/OCR with provenance, explicit gaps, review/approval contracts; 86 content and 49 review source/installed-wheel tests in nine environments | Representative OCR quality, AI review/accounting, original-source publication and consumer/editing parity; authenticated host workflows and revision results |
| 7 — CLEAR, then SCOPE | CLEAR PDF requirement retained | Build and jointly accept standalone applications |
| 8 — Another backend | Public compatible chat connector implemented; 67 source/installed-wheel checks and 69 shared-contract regression checks; explicit profiles and scoped qualification | Actual HTTP/model/runtime/hardware, quality/capacity and application/native qualification; no real model qualified yet |
| 9 — Foundry | Optional workflow plan recorded | Qualified shared review and consumer migration, then supervised pilot |
| 10 — Releases | No application release or legacy retirement claimed | All release gates, migration guidance and retained rollback |

## Public P3b rendering/OCR checkpoint

- [Content PR 2](https://github.com/nexus-research-software/nexus-content/pull/2)
  advances `nexus-content` to `0.1.0.dev1`. Optional PDFium/Pillow rendering and
  explicit local Tesseract 5 OCR bind exact source, base snapshot, selected pages,
  settings, native runtime/model hashes, rasters and recognized text. Controlled
  direct subprocesses enforce admission/output limits and interruption; completed
  page results survive later failures. Failed requested OCR cannot silently fall
  back to native text. Generation-one text-only JSON remains unchanged; OCR uses
  generation two and explicitly unverified transcription.
- [Review PR 2](https://github.com/nexus-research-software/nexus-review/pull/2)
  advances `nexus-review` to `0.1.0.dev1`, pinned to content source
  `b4bf978a16fb7a67b3d8628d5efd303a39d4ba9b`. Reports label native/OCR evidence and
  expose OCR settings/limitations. Changed OCR evidence invalidates earlier
  findings, reports, plans and approval records. A fabricated local OCR-to-review
  example finds the pixel-only wording while retaining incomplete visual coverage.
- [Content CI 40128706810](https://github.com/nexus-research-software/nexus-content/actions/runs/40128706810)
  passes 86 source and 86 clean installed-wheel checks in all nine Linux/Windows/
  macOS x Python 3.11/3.12/3.13 environments, with actual native OCR required.
  The wheel check also verifies base-only text extraction before adding the OCR
  extra. Native runtime versions and executable/model hashes are recorded in CI.
- [Review CI 40128754505](https://github.com/nexus-research-software/nexus-review/actions/runs/40128754505)
  passes 49 source and 49 clean installed-wheel checks per environment, plus 75
  shared-content checks. Its base-only environment intentionally skips 11 optional
  native content cases; those are required in the content matrix above. Local
  actual OCR-to-review, wheel/sdist, static/link and visual raster checks pass.
- Windows CI exposed a Tesseract `v5` version prefix and a local hostname query
  used by PDFium's platform detection. The fixes retain full version provenance
  and permit only that local query while continuing to block socket creation and
  network operations. Regression checks precede acceptance.
- Content merge: `4052e6e4dc865abfdcd84f816de228cec3ed61c0`.
  Review merge: `a64a33cc44db3fc900965893afbe2f968c4b96f9`.
  Both merged trees equal their tested trees and are retained at
  `checkpoint/20261024-public-p3b` in their respective repositories.
- This is an implemented native synthetic baseline, not general OCR accuracy,
  full visual/layout/form/table coverage, real-model review or application release
  acceptance. OCR processes are not an OS sandbox or hard memory/disk quota.
  Existing applications, original Content/RC4, saved data, private C00/C01 and
  private dependency pins remain unchanged. No real documents were published.

## Retained public P3a content/review checkpoint

- [Content PR 1](https://github.com/nexus-research-software/nexus-content/pull/1)
  introduces `nexus-content 0.1.0.dev0`: immutable source/snapshot/page/quote
  contracts, strict JSON, read-only PDF text-layer extraction, an interruptible
  worker with retained page progress, explicit coverage gaps and shared fabricated
  text/scanned/mixed fixtures. Binary checkout attributes and fixture hash checks
  preserve the exact PDF bytes on Windows.
- [Review PR 1](https://github.com/nexus-research-software/nexus-review/pull/1)
  introduces `nexus-review 0.1.0.dev0`: scoped review callbacks, validated findings,
  explicit coverage and partial results, bounded JSON/HTML reports, exact change
  plans and explicit human-decision records. It depends on the reviewed content
  source `e7ffc58901837f1d40b1f924480fefeb94ace8ea`; it imports no application,
  AI provider or Foundry. The example applies a fabricated deterministic rule.
- All nine Linux/Windows/macOS × Python 3.11/3.12/3.13 environments pass.
  [Content CI 40118179276](https://github.com/nexus-research-software/nexus-content/actions/runs/40118179276)
  runs 44 source and 44 clean installed-wheel tests per environment.
  [Review CI 40118218361](https://github.com/nexus-research-software/nexus-review/actions/runs/40118218361)
  runs 42 source and 42 clean installed-wheel tests plus 44 shared-content
  regressions per environment. Distributions build, local static/relative-link
  checks pass, and fabricated PDF pages were visually inspected.
- Content merge: `e710423f1b6ca4d0dfc73eb7562118ebbe797172`.
  Review merge: `392348ef4fde1d8800b0db2bdcb4f2eaa6668f29`.
  Both merged trees equal their tested trees and are retained at
  `checkpoint/20261024-public-p3a` in their respective repositories.
- **P3a was the first P3 increment, not full P3 acceptance.** At that checkpoint,
  scanned pages reported missing text; OCR had not yet been implemented. Visual/layout coverage,
  real-model review, authenticated host approval workflows, revision execution,
  existing consumer parity and native application acceptance remain open. Approval
  records are not authentication or execution grants, and no PDF edits are applied.
- New public code and fabricated documents only. The original Content/RC4
  candidate remains authoritative for existing consumers; this prototype belongs
  in a fresh development environment. Existing application routes, saved data,
  AI contract and private C00/C01/dependency pins remain unchanged.

## Public P2 connector checkpoint

- [Connector PR 1](https://github.com/nexus-research-software/nexus-provider-openai-compatible/pull/1)
  introduces `nexus-provider-openai-compatible 0.1.0.dev0`, its offline example,
  protocol/qualification documentation, and independent package checks. The
  shared dependency remains `nexus-ai==0.1.0.dev2` at the reviewed public commit.
- Local Linux/Python 3.12 validation passed 67 connector source tests, the same
  67 clean installed-wheel tests, and 69 shared-contract regression tests with
  the connector installed. Socket operations are blocked in the offline suite.
  Both wheel and source distribution build; static checks and relative links pass.
  [CI run 40113685963](https://github.com/nexus-research-software/nexus-provider-openai-compatible/actions/runs/40113685963)
  passed all nine Linux/Windows/macOS and Python 3.11–3.13 environments, including
  source, shared-contract regression, builds and clean installed-wheel checks.
  The merge is `8bb09e0c4a917ef0207c91faa24a19fc32af3375`, retained at
  `checkpoint/20261024-public-p2`; its tree matches the tested tree recorded in
  the PR.
- This is public P2's offline implementation evidence, not actual endpoint/model
  or application qualification. No original application/private source was copied.
  Existing application defaults, private C00/C01 and private dependency pins are
  unchanged. No live inference or key was used.

## Retained public P1 checkpoint

- [AI contract PR 4](https://github.com/nexus-research-software/nexus-ai/pull/4)
  adds an optional, separately packaged synthetic provider example, an explicit
  backend-selection command, developer instructions, and eleven installed-provider
  checks. It preserves the core runtime and version `0.1.0.dev2`.
- All nine CI jobs passed 69 source tests, 69 installed-wheel contract tests,
  and 11 installed-provider checks on Linux, Windows and macOS with Python
  3.11–3.13. Both distributions build as wheel and sdist. The
  [CI run](https://github.com/nexus-research-software/nexus-ai/actions/runs/40110357596)
  covers the tested head recorded in the PR; the merged tree was verified equal.
  Public milestone P1 is complete. The merge is
  `b9029c2e73499771be718718c3452fbc17bf6c85`, retained at
  `checkpoint/20261024-public-p1`.
- The public-first roadmap removes internal import/qualification from the next
  mandatory step for unrelated public work. It retains original-source publication,
  real-model quality, native workflow, and joint acceptance requirements.
- Private C00/C01 and the private dependency pin remain unchanged. No internal
  action or credential is required to use the public development example.

## Retained Phase 3 checkpoint

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

`checkpoint/20261024-public-p3b-start` preserves the pre-P3b revisions:

| Repository | P3b recovery revision |
| --- | --- |
| `nexus-content` | `e710423f1b6ca4d0dfc73eb7562118ebbe797172` |
| `nexus-review` | `392348ef4fde1d8800b0db2bdcb4f2eaa6668f29` |
| `nexus-ecosystem` | `d9bd2480270a5130e4c04202fab0c842258be5bb` |

Completed P3b checkpoint refs and tested/merged revisions are recorded in all
three PRs. Retain P3a and earlier public/private recovery points.

`checkpoint/20261024-public-p3a-start` preserves the pre-increment revisions:

| Repository | P3a recovery revision |
| --- | --- |
| `nexus-content` | `a81d6bec789f4c6cc95fbeabcc6c1e136915ebf0` |
| `nexus-review` | `6fa1a35d61af7392f6fd095299629d552a4d6885` |
| `nexus-ecosystem` | `5172290b95da422ecdff421054adf3f235d97253` |

Completed P3a checkpoint refs and exact tested/merged revisions are recorded in
all three PRs. Retain the previous P1/P2 and private recovery points as well.

`checkpoint/20261024-public-p2-start` retains the initial connector scaffold
`30e190f7db83fbcf978521b39d13321caa5dd1b2` and the catalog's pre-P2 revision
`ae22a6ff70727913653242c35724f58cd82664df` in their respective repositories.
The corresponding completed P2 refs and tested/merged revisions are recorded with
the implementation and catalog PRs. Keep earlier recovery points as well.

The retained `checkpoint/20261024-public-first-start` branches preserve the
starting revisions for the earlier public P1 increment:

| Repository | Public-first recovery revision |
| --- | --- |
| `nexus-ai` | `0a302724d1bffd9af3daaa8e0f5f700ccd309fb1` |
| `nexus-ecosystem` | `4e40ccb9e1aa675083ef21cf26b061197bfb87a2` |

The corresponding completed milestone refs and exact tested/merged revisions
are recorded with each PR. Preserve the earlier checkpoints below as well.

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

Continue public P3c: adapt the review boundary to the public AI contract with
complete usage, budget and interruption receipts. Keep explicit native/OCR origins
and incomplete coverage through the model boundary; use fabricated responses for
contract checks while actual-model quality remains a separate gate. Original-source
extraction and consumer/revision parity retain their publication/licensing gates;
actual inference awaits a chosen model/runtime and hardware. These independent
public increments prepare CLEAR's first PDF workflow without requiring internal
access or changing existing application routes.

Internal import/CI, native/live private qualification, and one governed opt-in
consumer route are deferred acceptance gates. Resume them after feasible public
work or when a specific remaining dependency requires private evidence. Keep all
unqualified functionality on its original route until accepted.

Outstanding decisions remain application licensing/attribution, developer ownership,
native installation combinations and joint acceptance thresholds. The first local
model and its hardware can still be chosen at Phase 8.
