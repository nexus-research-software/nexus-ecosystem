# Getting started

## Current availability

NEXUS is establishing its public repository foundations. This catalog does not yet provide application installers, package installation commands, or a qualified compatibility set.

Developers can use the [public AI walkthrough](https://github.com/nexus-research-software/nexus-ai/blob/main/docs/PUBLIC_DEVELOPMENT.md)
to install the shared contract and an optional synthetic adapter, then switch
between two fabricated backends. It needs no API key or internal service. It is
a development example, not TRACER, CLEAR, SCOPE, or a real LLM. Public development
now follows the [public-first execution order](PUBLIC_FIRST.md).

If you already use a NEXUS application, continue using your existing installation during migration. Moving the public repositories is not an instruction to uninstall or replace a working application.

## Planned installation experience

1. Select the application you want from the [catalog](../README.md#application-catalog).
2. Choose a release qualified for your operating system.
3. Use its installer or the qualified Ecosystem Manager installation path.
4. Configure a supported AI provider only if the selected workflow needs one.
5. Follow the application's first-run check using a synthetic example.

Users will not need to clone every repository or manually assemble shared library source.

## AI providers

Provider selection will be explicit. The application will identify which capabilities a selected backend supports and report when a task is unavailable.

For deployments using personal API keys, each user supplies their own key through the application's credential setup. Keys must not be committed to Git or included in public issue reports.

Some deployments require a separately distributed private adapter and an internal installation profile. Local-model connectors can be public. The first local model and its hardware requirements have not been selected.

## CLEAR and PDF

CLEAR is the first planned new application. Its first release must support PDF review, including qualification for text, scanned, and mixed PDFs, page-based evidence, and review reports.

PDF review does not imply arbitrary rewriting of a PDF's layout or content. Supported outputs will be stated in the release documentation.

## Help

Report catalog or documentation problems through this repository's issues. Use synthetic reproductions and follow the [contribution guide](https://github.com/nexus-research-software/.github/blob/main/CONTRIBUTING.md).
