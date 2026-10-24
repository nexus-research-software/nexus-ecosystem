# Repository boundary plans

Stage 1 turns the frozen source inventory into proposed ownership and publication boundaries. The public tool checks a private plan against that inventory. It does not move files, inspect their contents, resolve imports, scan for secrets, approve licensing, or authorize publication.

## Current checkpoint

A provisional private plan accounts for all 4,133 included files across nine canonical source trees. Every entry retains its source hash, size, reason, proposed disposition, and review requirement. Historical copies, embedded archives, documents, operational evidence, and mixed provider/application files remain visible in the plan. Original inputs remain preserved.

The map is a review draft. Mechanical signals and selected architectural inspection help route review; they do not establish that a file is safe to publish. Application licensing, attribution, fixture provenance, exact extraction boundaries, and behavioral acceptance remain open. The map describes the original snapshot; working-copy repairs require an updated snapshot and plan before migration.

## Responsibilities

| Responsibility | Proposed owner |
| --- | --- |
| Application workflows, domain prompts, approvals, evidence, durable data, and GUI state | Owning public application repository |
| Generic document parsing and provenance | Public `nexus-content` |
| Provider-neutral requests, results, capabilities, errors, and registration | Public `nexus-ai` |
| Generic local or compatible model transport | Public connector, once its contract and consumers qualify extraction |
| Service-specific authentication, endpoint configuration, model policy, response parsing, and qualification | Private provider adapter |
| Agent execution, tool permissions, and orchestration | Foundry; independent of model-provider selection |
| Acquisition, environments, compatibility, installation, and rollback | Public Ecosystem Manager |

An HTTP client, an OpenAI-compatible SDK call, or a credential interface does not by itself make code private. Likewise, application prompts and business rules should not move into a provider adapter merely because they are sent to a model. Mixed modules need a deliberate split that preserves both responsibilities.

Keep existing generic transports with their owning applications until a shared implementation preserves their differences: context planning, cancellation, streaming semantics, callbacks, credential precedence, and application approvals. Avoid creating a second maintained copy merely to populate a proposed repository.

Repository hierarchy is logical. Applications retain their existing import namespaces, entry points, state directories, and artifact identifiers. Ecosystem Manager's current local discovery expects direct child application directories; a repository grouping should not silently change that layout. Optional private packages need deployment-level installation policy without becoming required public application dependencies.

## Draft and validate a plan

First follow the [baseline example](BASELINE.md#try-the-synthetic-example). Then run from this repository root:

```console
python tools/nexus_boundaries.py draft --baseline ../nexus-baseline-example-before.private.json --output ../nexus-boundaries-example.private.json
python tools/nexus_boundaries.py validate --baseline ../nexus-baseline-example-before.private.json --plan ../nexus-boundaries-example.private.json --output ../nexus-boundaries-validation.private.json
```

`draft` creates one `review_required` entry for every included source file. It does not guess ownership or classify content. Edit a copy to record proposed repository targets, dispositions, and reasons, then validate that copy. Choose a new output filename for each run. Outputs cannot replace existing evidence or write into recorded input paths.

The plan is bound to the complete snapshot, including its exclusion policy and artifact identities. Coverage applies to included regular source files; it does not inspect members of embedded archives or claim coverage of excluded files. Original archives remain preservation inputs. Repaired or newly generated source needs a fresh snapshot and a reviewed plan for that revision.

| Disposition | Meaning | Required targets |
| --- | --- | --- |
| `public_candidate` | Proposed public ownership, pending content and licensing review | One or more public repositories |
| `private_provider` | Proposed private provider implementation or supporting material | One or more private repositories |
| `split_required` | Public and private concerns share the file | Both public and private repositories |
| `private_evidence` | Documents, traces, or historical evidence retained privately | None |
| `generated_exclude` | Generated output or copied implementation preserved outside maintained source | None |
| `review_required` | No destination assigned yet | None |

Every entry retains `review_required: true`; even a `public_candidate` is unapproved. The plan's `publication_authorized` field must remain `false`. A separate reviewed export/release process must eventually establish what can be published; this tool deliberately cannot perform that step.

The validator rejects missing or duplicate files, unknown paths, stale identities, changed snapshots, unknown targets, and dispositions inconsistent with target visibility. JSON with duplicate keys is rejected. CLI exit code `0` means the draft or structural check succeeded; `2` means invalid input or an operational error. A structurally valid plan can still contain unresolved decisions or incorrect content classifications.

Real plans, paths, hashes, reasons, and reports stay private. Public CI uses fabricated files only, on Linux, Windows, and macOS with Python 3.11–3.13.

## Review and extraction sequence

1. Review proposed ownership against current code and the capability ledger. Confirm licenses, attribution, document/template provenance, and artwork rights. Preserve documents and evidence until a separate synthetic replacement is verified.
2. Define and test the public AI contract without importing private adapters. Keep inference capabilities separate from execution authority. Preserve unsupported/unknown states and forbid silent provider fallback.
3. Split mixed modules in working copies. Keep application policy and generic interfaces public; implement service-specific behavior and its operational tests privately. Replace concrete-client coupling with qualified interfaces without weakening existing safeguards.
4. Regenerate bundled authoring packets, examples, and build artifacts from reviewed canonical sources. Inspect embedded contents before release; moving the live module alone does not remove historical copies.
5. Compare capability and installation evidence against the baseline. Retain native desktop, live-provider, and installer gates separately from source tests. Preserve rollback artifacts and migration behavior.
6. Publish only the reviewed revision after the application publication decisions are complete. Consume versioned public packages internally and install private adapters separately. Require public imports, synthetic tests, and installation to work without internal credentials or registry access.

The two developers will assign ownership before extraction. Application acceptance remains a joint decision with the project owner. Completing inventory coverage does not close Stage 1.
