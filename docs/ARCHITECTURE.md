# Architecture and repository boundaries

This is the target architecture. Public experimental packages now implement AI
contracts, a compatible connector, read-only PDF evidence, and shared review/approval
contracts. New `nexus-clear` composes these packages as a standalone experimental
PDF wording-review application. Original application/source extraction and consumer migration remain
open. The [execution status](STATUS.md) distinguishes synthetic package evidence
from representative OCR quality, model and application acceptance.

## Logical hierarchy

GitHub repositories live under one organization. The hierarchy is expressed through responsibilities and package dependencies.

| Layer | Owns | Depends on |
| --- | --- | --- |
| Catalog and installation | Application discovery, compatible release records, install and repair flows | Published application and package artifacts |
| Applications | User workflows, domain policy, settings, and product-specific outputs | Public shared-package interfaces |
| Review package | Shared review execution, findings, change plans, and reports | Content and AI contracts where needed |
| Content package | Read-only extraction, optional rendering/OCR and provenance | Format parsers; explicit local OCR runtime when selected |
| AI contract | Normalized requests, results, capabilities, errors, and provider registration | No private provider implementation |
| Provider adapters | Protocol transport and provider-specific behavior | The public AI contract |

Applications do not import one another to reuse review behavior. Shared packages are extracted where multiple real consumers and a stable responsibility justify them.

Foundry retains authority over its agent workflows. An AI connector transports model interactions; it does not gain authority to approve tools, access arbitrary files, or execute actions.

### Optional Foundry orchestration

TRACER, CLEAR, and SCOPE keep their standalone review paths. Foundry may coordinate longer workflows through the same versioned `nexus-review` interfaces used by those applications. The review package does not depend on Foundry; application-specific rules remain with each application, and orchestration remains with Foundry.

Shared interfaces describe review requests, evidence-backed findings, proposed changes, human approvals, revision results, and reports. Preserve source revision identity, edit semantics, and provenance. Foundry integration must use its supported public API and qualified execution capabilities; no private runtime imports or implicit authority grants.

P3a implements new generation-one source/snapshot/quote anchors in `nexus-content`
and review requests, findings, coverage, proposed changes, approval records and
JSON/HTML reports in `nexus-review`. Review depends on content; neither depends on
Foundry or a private provider. The current review callback is deterministic in the
base example. P3c adds the optional AI reviewer described below; revision
execution/results remain an open consumer-specific gate.
Approval records bind exact plans and fresh source bytes; the host still owns human
authentication, decision capture, source locking and execution authority.

P3b adds optional raster/OCR execution to `nexus-content`, keeping the base package
usable without native OCR tools. Text-only generation-one wire identities remain
unchanged; generation-two OCR snapshots bind the base, scope, settings, runtime,
raster and recognized text. Explicit page selection, processing limits and gaps
prevent hidden fallback or a false complete-review claim. `nexus-review` consumes
the same immutable snapshot boundary, labels evidence origin and rejects stale
OCR reports/decisions. OCR runtime selection is separate from GenAI provider
selection and does not require another application or Foundry.

P3c adds optional `nexus_review.ai` on `nexus-ai==0.1.0.dev2`; base review still
requires only `nexus-content`. The host explicitly chooses and qualifies a provider,
model, configuration and exact output schema. Whole-page findings must resolve to
exact quote occurrences. Shared execution retains coverage and prior findings;
immutable AI receipts record usage, admitted budgets, errors and interruptions,
including discarded responses. Unknown usage remains unknown and stops further
dispatch by default. The report identity binds the selected backend and call ledger
so earlier approvals cannot move to a new run. No hidden retry, fallback, provider
probe, editing or execution authority is introduced. Compatible connectors stay
independent; GenAI-specific code remains private. This API does not claim monetary
quotas, durable in-flight recovery, cross-page reasoning or actual model quality.

P4a makes CLEAR the first new application consumer. Its desktop and CLI share one
application service; versioned JSON owns the wording checklist, while extraction,
OCR, evidence, review execution and AI receipts stay in their existing packages.
Base use requires no AI, private service or Foundry. An explicit Python host supplies
AI configuration; fabricated CLI backends only accept bundled synthetic PDFs.
Checklist identity binds every shared rule. New-folder exports retain validated
returned results without copying the source PDF; restoration performs no inference.
These folders do not provide durable in-flight recovery or authenticated approvals.
The developer bootstrap pins exact public revisions and refuses existing environments;
full native installation/update/repair acceptance remains P5 work.

Prepare these interfaces in Stage 6, deliver standalone CLEAR and SCOPE in Stage 7, and pilot TRACER review/approve/revise/re-review in Stage 9. Qualify CLEAR and SCOPE integration separately after demonstrating value. Enabling or disabling Foundry must preserve existing direct review capabilities, evidence, approval rules, and saved results. Backend selection through `nexus-ai` remains independent of orchestration. See the [staged roadmap](ROADMAP.md#foundry-integration-across-stages) for acceptance gates.

## Public and private boundary

Application source, reusable libraries, generic deployment tooling, templates, synthetic examples, and local-model connectors belong in public repositories.

GenAI-specific API integration is maintained separately behind the deployment firewall. Private adapters implement the public contract and are installed through controlled distribution. Private endpoint values, credentials, operational traces, and protected evaluation material stay in that environment.

Public packages must install and run their synthetic tests without a private adapter or live service key. Importing or discovering a provider must not trigger network requests or credential access.

A private repository does not by itself create a remote service boundary. Public-source applications may run inside a firewall and load a private adapter locally. A separate gateway is optional future work.

## Interchangeable providers

Represent text generation, structured output, streaming, tool calls, vision, and embeddings as distinct capabilities. Record supported, unsupported, and unknown states separately.

Select a provider and model explicitly. Unsupported tasks should produce a clear result; they must not silently fall back to a different service. Qualify each backend using common synthetic fixtures and application-level acceptance checks.

Preserve cancellation, error handling, usage accounting, and existing compatibility behavior during migration.

## One maintained implementation

Each application and package has a canonical source repository. Internal builds consume versioned public packages or verified mirrors of their artifacts.

Separate application environments may install the same released package. This is compatible with maintaining shared source once.

Preserve existing import paths, commands, saved projects, and settings through adapters and reviewed migrations. Keep rollback artifacts until the replacement passes acceptance.

## Evidence and release gates

Separate source movement from behavior changes. Compare old and new behavior with repeatable fixtures and user journeys. Keep real-document evidence private, and publish only synthetic examples and appropriate aggregate qualification results.

Linux, Windows, and macOS each require validation. Release notes must state tested environments, supported capabilities, and remaining limitations.
