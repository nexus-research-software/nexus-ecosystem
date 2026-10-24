# Requirements for the first shared AI contract

This document remains the acceptance target for Stage 2. The first [nexus-ai implementation](https://github.com/nexus-research-software/nexus-ai) is an experimental `0.1.0.dev2` prototype, not an approved stable API. Characterization comes before moving consumers. Its 69 tests pass from source and a clean installed wheel in all nine supported OS/Python CI combinations. Failure receipts preserve normalized termination evidence without an extra inference call.

The first slice implements synchronous text and local JSON-schema completion, immutable request/selection types, capability checks, normalized results/errors/usage, bounded attempt and repair accounting, cancellation/deadline checks, and metadata-only provider discovery. Synthetic conformance and clean installed-wheel checks exercise these contracts. There is no live adapter or migrated application. Streaming, tools, vision, and embeddings have separate capability identifiers but no execution methods yet.

The prototype reports incomplete output without returning partial text. An opt-in TRACER compatibility candidate now preserves completed findings when later requests fail, with 43 focused synthetic checks. Shared requests carry temperature and schema names, and the bridge requires exact schema-hash qualification plus the expected evidence identity. The existing application runtime remains the default. The candidate patch and detailed evidence stay private pending application publication review.

The separately installed private adapter now has an offline candidate: 242 source tests and the same 242 installed-wheel tests pass on Linux/Python 3.12. Existing runtime behavior remains the compatibility reference. The next gates are internal/native/live qualification and complete consumer parity, including citation protections and per-attempt private diagnostics, before production selection. The bridge deliberately refuses enforced quota mode and does not establish live-service or native installation parity. See the [compatibility notes](https://github.com/nexus-research-software/nexus-ai/blob/main/docs/CONSUMER_COMPATIBILITY.md) and [current status](STATUS.md).

## Preserve existing owners

Applications own prompts, domain rules, review approvals, durable state, and workflow budgets. Foundry owns execution authority. Shared AI code describes requests, capabilities, normalized results, cancellation, errors, and accounting. Provider adapters own authentication and wire translation. Public imports and discovery must perform no network or credential access.

## First contract slice

| Contract | Required semantics |
| --- | --- |
| Request | Explicit provider/profile/model identity, ordered messages, temperature, named response schema, context/output budgets, request identity and cancellation |
| Capability | Supported/unsupported/unknown states; qualification bound to selected configuration/model, optional exact schema hashes and pinned evidence identity; separate text, structured output, streaming, tool, vision and embedding capabilities |
| Response | Requested and observed model identity, structured/text output, termination reason, provenance and normalized receipt |
| Usage | Known versus unknown counts; distinguish logical calls, formatting repair and actual transport attempts; no repeated inference merely because usage lookup failed |
| Error | Typed unavailable/unsupported/authentication/quota/context/transport/schema/cancellation outcomes; safe metadata without credentials or document text |
| Provider registration | Lazy discovery, explicit selection, version compatibility, no automatic fallback to another service |

Begin with the structured-completion path already used by TRACER and keep a compatibility wrapper around its existing port. Do not replace its current schema qualification, accounting, model-selection or citation protections with a weaker generic interface. Additional capabilities are additive and separately qualified.

Before migration, construct synthetic conformance cases covering schema rejection without silent downgrade, explicit unsupported capability, cancellation, unknown usage, retry/admission accounting, provider identity, safe error receipts, and import/discovery without credentials. Keep provider-specific envelope fixtures in the corresponding private project.

Consumer migration requires repeatable baseline results, disposition of baseline failures, and reviewed ownership/publication decisions. New contract code is reviewed in its owning `nexus-ai` repository while those gates remain open. No application or provider implementation is copied into this catalog or the contract prototype.

