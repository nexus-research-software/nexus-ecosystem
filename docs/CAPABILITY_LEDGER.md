# Capability retention ledger

This is the initial Stage 0 checklist. Each row needs linked private evidence, a responsible developer, and agreed acceptance criteria before it can close. Source inspection or historical test records are not current acceptance evidence.

| Owner | Capability families to retain | Required evidence | Gate |
| --- | --- | --- | --- |
| TRACER | GUI/CLI/batch entry points; DOCX and LaTeX review; citation evidence; tracked edits and comments; reviewed clean export; publication and converter outputs; request qualification, quotas, cancellation and partial results | Existing regressions, synthetic document journeys, installed resources, native Word/desktop checks, private live-provider checks | Open |
| ATLAS | Workbench, modes, Agent Skills, document context, Help, custom and visual workflows, Plugin Designer, Summary Artifact, optional Foundry integration, distribution | Existing regressions, source-currentness and request-budget checks, standalone/optional integration runs, platform installation journeys | Open |
| Foundry | Work, Forge, and Legacy Code Modernization as distinct surfaces; durable runs, approvals, recovery, Native outputs, public API, inference bridge | Existing regressions per surface, artifact and approval evidence, independent production execution qualification | Open |
| Cartographer | Inventory, semantic exploration, provenance, organization proposals, dry run/apply/undo/recovery | Deterministic filesystem fixtures, approved plan identity, no-overwrite and rollback evidence | Open |
| Ledger | Durable knowledge and legacy identifiers, retained sources, review-gated updates, search, Document Review, Context currentness and external handoffs | Persistence/migration, source refresh, approval, transactional and artifact-contract regressions | Open |
| Repository Analyst | Non-executing repository inspection, snapshots, dossier, source currentness, history, investigations, evidence and conflicts | Repository boundary, identity, persistence, cancellation, history and provenance regressions | Open |
| Research Workbench | Literature/evidence workflow, source-aware approvals, synthesis, outline approval, drafting, publication, budgets and recovery | Existing regressions plus source changes, approval invalidation, Word output and publication provenance checks | Open |
| NEXUS Content | Read-only parsing, canonical evidence, completeness, provenance, profiles, bounded processing, optional backends and public contract | Source/wheel reconciliation, contract comparison, parser fixtures and consumer acceptance at exact versions | Open |
| Ecosystem Manager | Discovery, manifest/launch compatibility, environments, shared packages, installation/export/repair | Existing regressions and complete per-application installation/update/rollback journeys | Open |

CLEAR and SCOPE are new products. Their acceptance sets must be created in Stage 7; they are not existing functionality to claim preserved. Foundry integration remains optional and follows the [roadmap](ROADMAP.md#foundry-integration-across-stages).

For each tested capability, record: stable ID, owning package, source identity, test or user journey, environment/dependencies, result (pass/fail/skip/blocked/not-run), evidence location, baseline issue, acceptance owner, and rollback path. Keep evidence locations and real-document results in private records.
