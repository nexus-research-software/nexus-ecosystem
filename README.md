# NEXUS Research Software

Modular tools for research, technical documents, and knowledge workflows.

**Status: public work takes priority; private integration is deferred.** We are advancing the shared contracts, synthetic backend tests, public connectors, reusable components, and application/installation work that can proceed without an internal service. The private candidate remains checkpointed. This catalog does not yet offer application downloads. Read the [public-first execution order](docs/PUBLIC_FIRST.md) and [current status and checkpoints](docs/STATUS.md).

## Start here

- **Using an application:** read [Getting started](docs/GETTING_STARTED.md). Keep using your existing installation during migration.
- **Understanding the design:** read [Architecture](docs/ARCHITECTURE.md).
- **Following development:** read the [staged roadmap](docs/ROADMAP.md) and [current status](docs/STATUS.md).
- **Developing without a private service:** try the [separately installed synthetic backends](https://github.com/nexus-research-software/nexus-ai/blob/main/docs/PUBLIC_DEVELOPMENT.md).
- **Building a public backend:** use the [compatible connector and offline demo](https://github.com/nexus-research-software/nexus-provider-openai-compatible). Actual model qualification remains pending.
- **Reviewing a fabricated PDF:** try the [shared review walkthrough](https://github.com/nexus-research-software/nexus-review), built on [read-only content evidence](https://github.com/nexus-research-software/nexus-content). Scanned pages remain explicit gaps until OCR is qualified.
- **Establishing the baseline:** use the [baseline tools](docs/BASELINE.md) and [capability ledger](docs/CAPABILITY_LEDGER.md).
- **Planning repository ownership:** use the [boundary-plan checker](docs/BOUNDARIES.md).
- **Contributing:** read the [shared contribution guide](https://github.com/nexus-research-software/.github/blob/main/CONTRIBUTING.md).

## Application catalog

These are intended repository names. Entries without links have not yet been established as application repositories in this organization.

| Application | Intended repository | Migration or release status |
| --- | --- | --- |
| TRACER | `nexus-tracer` | Existing application; public migration pending |
| ATLAS | `nexus-atlas` | Existing application; public migration pending |
| Foundry | `nexus-foundry` | Existing application; public migration pending |
| Cartographer | `nexus-cartographer` | Existing application; public migration pending |
| Ledger | `nexus-ledger` | Existing application; public migration pending |
| Repository Analyst | `nexus-repository-analyst` | Existing application; public migration pending |
| Research Workbench | `nexus-research-workbench` | Existing application; public migration pending |
| CLEAR | `nexus-clear` | First new application; PDF required in its first release |
| SCOPE | `nexus-scope` | Planned after CLEAR |

## Shared components

| Layer | Intended repository | Responsibility |
| --- | --- | --- |
| Entry point | [nexus-ecosystem](https://github.com/nexus-research-software/nexus-ecosystem) | Catalog, documentation, and future compatibility records |
| Organization | [.github](https://github.com/nexus-research-software/.github) | Public profile and shared contribution guidance |
| Installation | `ecosystem-manager` | Acquire, install, repair, launch, and roll back selected applications |
| Content | [nexus-content](https://github.com/nexus-research-software/nexus-content) | Experimental PDF text-layer extraction, source identity, page gaps and exact quote anchors |
| AI contracts | [nexus-ai](https://github.com/nexus-research-software/nexus-ai) | Provider-neutral requests, results, capabilities, and adapter interfaces |
| Review | [nexus-review](https://github.com/nexus-research-software/nexus-review) | Experimental shared review, findings, coverage reports, change plans and explicit approval contracts |
| Local and compatible providers | [nexus-provider-openai-compatible](https://github.com/nexus-research-software/nexus-provider-openai-compatible) | Experimental compatible chat connector with explicit scoped qualification; offline candidate |
| Additional providers | `nexus-provider-asksage` | Candidate future adapter; placement and implementation remain to be decided |
| Optional service | `nexus-ai-gateway` | Consider only when centralized inference has a demonstrated need |

The catalog includes generic source-identity, test-evidence, and private boundary-plan tooling with synthetic CI checks. Six repositories are now established: this catalog, `.github`, `nexus-ai`, `nexus-provider-openai-compatible`, `nexus-content`, and `nexus-review`. Public package evidence covers synthetic workflows. Actual model quality, OCR, application acceptance and consumer migration remain open. Use separate development environments; the new content prototype is not an upgrade of the retained original Content/RC4 implementation.

## Design commitments

Applications remain independently usable. Shared behavior has one maintained source and is distributed through versioned packages. A compatible release may install that package into more than one application's isolated environment.

Applications depend on the public AI contract. Deployment-specific private adapters are installed separately. A local or hosted backend must be qualified for the requested task; switching backends must not silently send data to another service.

Linux, Windows, and macOS are release targets. Support is established by testing each release, not by this catalog alone.

## Publication and licensing

Public examples use templates and synthetic material. Real documents, their derived evidence, credentials, and private provider implementation do not belong here.

Licensing and attribution decisions must be completed before application source publication. No application source or private integration has been imported into these starter repositories.

