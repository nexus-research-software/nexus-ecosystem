# Baseline tooling

Stage 0 establishes what exists before extracting shared packages. The tools in this repository capture source identities and summarize test evidence. They do not run application code, install applications, call a model, or establish release qualification.

Use Python 3.11–3.13. The tools and their synthetic tests use only the standard library.

## Try the synthetic example

From the repository root:

```console
python -m unittest discover -s tests -v
python tools/nexus_baseline.py snapshot --config examples/baseline/inputs.example.json --output ../nexus-baseline-example-before.private.json
python tools/nexus_baseline.py snapshot --config examples/baseline/inputs.example.json --output ../nexus-baseline-example-after.private.json
python tools/nexus_baseline.py compare ../nexus-baseline-example-before.private.json ../nexus-baseline-example-after.private.json --output ../nexus-baseline-example-diff.private.json
```

Choose new output names on subsequent runs. Reports are created once; the tool refuses to overwrite a previous baseline or write inside an input source tree.

## Capture the authoritative inputs privately

Create an input JSON file outside this repository using the example's schema. Map stable labels under `sources` to extracted source directories and labels under `artifacts` to original archives or other files. Relative paths resolve from that configuration file, not the shell's working directory.

Run `snapshot` before making changes. Preserve both the original archives and the resulting report in approved private storage. A digest records identity; it is not a backup. Run tests and migrations in separate working copies, then capture another snapshot and compare the originals to confirm preservation.

The tool hashes every included regular file, including wheels and documents, without copying contents into the report. It skips only its documented VCS/environment/cache directories and Python bytecode; the exact exclusion policy is recorded in every snapshot. It records symbolic links and special files as omitted and marks the snapshot incomplete. Missing inputs, empty source trees, unreadable files, observed changes during hashing, and inconsistent manifests cannot produce a successful comparison.

Keep input trees quiescent while capturing. This is a filesystem inventory, not an atomic filesystem snapshot or an adversarial sandbox. File paths, hashes, package metadata, and omitted-entry names can themselves be sensitive. Treat every real-source report as private; `.gitignore` is an aid, not a publication approval mechanism.

Root relocation is allowed when comparing snapshots. Added/removed sources or artifacts, changed file contents, and added/removed files are differences. Changing the exclusion policy requires a deliberately established new baseline.

## Record tests without concealing failures

Provision each application in a separate environment using its declared dependencies and lockfile where supplied. Record the exact dependency versions, source identity, interpreter, OS, command, and process exit code. Do not assume that different applications' dependency constraints can share an environment.

Run the selected existing suite with JUnit output in private storage, for example:

```console
python -m pytest tests --junitxml=../baseline-tests.private.xml
python tools/nexus_baseline.py junit ../baseline-tests.private.xml --exit-code ACTUAL_EXIT_CODE --output ../baseline-tests-summary.private.json
```

The first command is illustrative: execute it from the owning application with that application's approved test setup. Run the second from this repository, replacing `ACTUAL_EXIT_CODE` with the observed process result. Collection failures, timeouts, incomplete runs, and skipped GUI checks must remain explicit. Never pass a fabricated zero to turn a failed run green.

JUnit summaries retain aggregate counts and the report hash, without copying test names, assertions, document excerpts, or logs. A nonzero process result, recorded failure/error, or an empty/all-skipped report cannot count as success. Mixed passed/skipped results retain their skips and do not qualify the skipped capabilities.

CLI exit codes: `0` means a complete snapshot, equal comparison, or successful test process with passing cases; `1` means incomplete/different/unsuccessful evidence; `2` means invalid input or an operational error. A tool success does not close a roadmap stage.

## Stage 0 completion criteria

- Original archives remain preserved with verified identities.
- Each application has an agreed capability ledger, including entry points, saved state, outputs, and integration boundaries.
- Existing regression checks run repeatably in identified environments; failures are reproduced and either fixed separately or explicitly accepted as baseline debt with owners.
- Native desktop, installation, Word rendering, and live-provider checks remain separate from headless tests.
- Content source/wheel differences are reconciled before selecting a shared release.
- Public export and licensing decisions are recorded before application source is published.
- The two developers and project owner agree the acceptance and rollback evidence.

The public CI workflow validates this tool using fabricated temporary files on Linux, Windows, and macOS with Python 3.11, 3.12, and 3.13. It does not upload or test supplied application archives, private integrations, or real documents.
