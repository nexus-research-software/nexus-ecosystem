# Requirements for the first shared AI contract

This is a Stage 2 design input, not an implemented runtime or approved stable API. Characterization comes before moving consumers.

## Preserve existing owners

Applications own prompts, domain rules, review approvals, durable state, and workflow budgets. Foundry owns execution authority. Shared AI code describes requests, capabilities, normalized results, cancellation, errors, and accounting. Provider adapters own authentication and wire translation. Public imports and discovery must perform no network or credential access.

## First contract slice

| Contract | Required semantics |
| --- | --- |
| Request | Explicit provider/profile/model identity, ordered messages, requested response contract, context/output budgets, request identity and cancellation |
| Capability | Supported/unsupported/unknown states; qualification bound to selected configuration/model; separate text, structured output, streaming, tool, vision and embedding capabilities |
| Response | Requested and observed model identity, structured/text output, termination reason, provenance and normalized receipt |
| Usage | Known versus unknown counts; distinguish logical calls, formatting repair and actual transport attempts; no repeated inference merely because usage lookup failed |
| Error | Typed unavailable/unsupported/authentication/quota/context/transport/schema/cancellation outcomes; safe metadata without credentials or document text |
| Provider registration | Lazy discovery, explicit selection, version compatibility, no automatic fallback to another service |

Begin with the structured-completion path already used by TRACER and keep a compatibility wrapper around its existing port. Do not replace its current schema qualification, accounting, model-selection or citation protections with a weaker generic interface. Additional capabilities are additive and separately qualified.

Before migration, construct synthetic conformance cases covering schema rejection without silent downgrade, explicit unsupported capability, cancellation, unknown usage, retry/admission accounting, provider identity, safe error receipts, and import/discovery without credentials. Keep provider-specific envelope fixtures in the corresponding private project.

Stage 0 must first establish repeatable results and disposition baseline failures. Stage 1 must settle source publication and ownership. New public contract code can then be reviewed in its owning `nexus-ai` repository without copying application or provider implementations into this catalog.
