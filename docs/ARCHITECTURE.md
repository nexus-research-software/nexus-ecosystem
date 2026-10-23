# Architecture and repository boundaries

This is the target architecture. The public repositories currently contain documentation foundations; the package extraction has not yet been implemented.

## Logical hierarchy

GitHub repositories live under one organization. The hierarchy is expressed through responsibilities and package dependencies.

| Layer | Owns | Depends on |
| --- | --- | --- |
| Catalog and installation | Application discovery, compatible release records, install and repair flows | Published application and package artifacts |
| Applications | User workflows, domain policy, settings, and product-specific outputs | Public shared-package interfaces |
| Review package | Shared review execution, findings, change plans, and reports | Content and AI contracts where needed |
| Content package | Read-only extraction and provenance | Format-specific parsers |
| AI contract | Normalized requests, results, capabilities, errors, and provider registration | No private provider implementation |
| Provider adapters | Protocol transport and provider-specific behavior | The public AI contract |

Applications do not import one another to reuse review behavior. Shared packages are extracted where multiple real consumers and a stable responsibility justify them.

Foundry retains authority over its agent workflows. An AI connector transports model interactions; it does not gain authority to approve tools, access arbitrary files, or execute actions.

### Optional Foundry orchestration

TRACER, CLEAR, and SCOPE keep their standalone review paths. Foundry may coordinate longer workflows through the same versioned `nexus-review` interfaces used by those applications. The review package does not depend on Foundry; application-specific rules remain with each application, and orchestration remains with Foundry.

Shared interfaces describe review requests, evidence-backed findings, proposed changes, human approvals, revision results, and reports. Preserve source revision identity, edit semantics, and provenance. Foundry integration must use its supported public API and qualified execution capabilities; no private runtime imports or implicit authority grants.

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
