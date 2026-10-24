# NEXUS Research Software

Modular tools for research, technical documents, and knowledge workflows.

**Status: Phase 3 private adapter qualification in progress.** The public AI contract and a separately installable private adapter candidate pass offline checks. Internal and live qualification, application migration, installers, and releases remain ahead. This catalog does not yet offer application downloads. Read the [current status and checkpoints](docs/STATUS.md).

## Start here

- **Using an application:** read [Getting started](docs/GETTING_STARTED.md). Keep using your existing installation during migration.
- **Understanding the design:** read [Architecture](docs/ARCHITECTURE.md).
- **Following development:** read the [staged roadmap](docs/ROADMAP.md) and [current status](docs/STATUS.md).
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
| Content | `nexus-content` | Read-only content extraction and provenance |
| AI contracts | [nexus-ai](https://github.com/nexus-research-software/nexus-ai) | Provider-neutral requests, results, capabilities, and adapter interfaces |
| Review | `nexus-review` | Shared review execution, findings, change plans, and reports |
| Local and compatible providers | `nexus-provider-openai-compatible` | Public connector for qualified compatible endpoints |
| Additional providers | `nexus-provider-asksage` | Candidate future adapter; placement and implementation remain to be decided |
| Optional service | `nexus-ai-gateway` | Consider only when centralized inference has a demonstrated need |

The catalog includes generic source-identity, test-evidence, and private boundary-plan tooling with synthetic CI checks. Three repositories are now established: this catalog, `.github`, and the experimental `nexus-ai` package. Application source extraction and consumer migration are not complete.

## Design commitments

Applications remain independently usable. Shared behavior has one maintained source and is distributed through versioned packages. A compatible release may install that package into more than one application's isolated environment.

Applications depend on the public AI contract. Deployment-specific private adapters are installed separately. A local or hosted backend must be qualified for the requested task; switching backends must not silently send data to another service.

Linux, Windows, and macOS are release targets. Support is established by testing each release, not by this catalog alone.

## Publication and licensing

Public examples use templates and synthetic material. Real documents, their derived evidence, credentials, and private provider implementation do not belong here.

Licensing and attribution decisions must be completed before application source publication. No application source or private integration has been imported into these starter repositories.

