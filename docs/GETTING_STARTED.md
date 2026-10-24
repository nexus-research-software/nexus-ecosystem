# Getting started

## Current availability

NEXUS now includes a [standalone CLEAR development candidate](https://github.com/nexus-research-software/nexus-clear). Clone only that repository and follow its pinned bootstrap instructions to try the desktop or CLI on fabricated PDFs. Python 3.11–3.13 and Git are required; the desktop additionally needs Tk and a graphical display. Base wording checks need no AI or private service.

Qualified native application installers, update/repair/rollback journeys and an accepted application compatibility set remain pending. Package-level walkthroughs are linked below.

Developers can use the [public AI walkthrough](https://github.com/nexus-research-software/nexus-ai/blob/main/docs/PUBLIC_DEVELOPMENT.md)
to install the shared contract and an optional synthetic adapter, then switch
between two fabricated backends. It needs no API key or internal service. It is
a development example, not TRACER, CLEAR, SCOPE, or a real LLM. Public development
now follows the [public-first execution order](PUBLIC_FIRST.md).

The [public compatible connector](https://github.com/nexus-research-software/nexus-provider-openai-compatible)
also includes an offline example that exercises its actual HTTP mapping through
fabricated responses. It is separately installable and needs no private package.
It does not yet establish compatibility or review quality with an actual model.

The [PDF content walkthrough](https://github.com/nexus-research-software/nexus-content)
and [shared review walkthrough](https://github.com/nexus-research-software/nexus-review)
now demonstrate read-only text extraction, page evidence, a deterministic fabricated
review rule, explicit coverage gaps, and an approval record that applies no edits.
They need no model or private package. Use fresh isolated environments and the
exact shared revision recorded in the review repository. The new public content
package does not replace the original Content/RC4 package in existing applications.

The optional [AI review walkthrough](https://github.com/nexus-research-software/nexus-review/blob/main/docs/AI_REVIEW.md)
now switches between fabricated providers while preserving exact page quotes, native/OCR
origin, explicit qualification, budgets and partial results. It needs the pinned
public AI contract but no private package or key. Base deterministic review remains
available without AI installed. The recorded usage and errors support inspection;
this is still a developer example, not a CLEAR installer or proof of model quality.

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

CLEAR is the first new application. Its [P4a candidate](https://github.com/nexus-research-software/nexus-clear) provides a desktop window, CLI, three narrow wording topics, exact page quotes and new-folder JSON/HTML reports. Save and reopen returned results without inference; optionally verify the current PDF bytes. No PDF edits or legal-risk ratings are applied. Human review remains required even with zero findings.

Its first accepted release still requires qualification for text, scanned and mixed PDFs, page-based evidence, useful checklist coverage and review quality.

P3a establishes shared text-layer and review contracts. P3b adds an optional
[local OCR walkthrough](https://github.com/nexus-research-software/nexus-content/blob/main/docs/OCR.md)
and a [fabricated OCR-to-review example](https://github.com/nexus-research-software/nexus-review/blob/main/examples/ocr_review.py).
A fresh environment and explicitly selected Tesseract executable/language model
are required. OCR is never silently invoked; reports distinguish native and
recognized text, retain gaps and label OCR as unverified transcription. Synthetic
native checks pass, while representative document accuracy and joint acceptance
remain open. P3c now connects shared review to the public AI contract and retains
usage even for discarded outputs. P4a composes these packages in CLEAR, with optional
explicit CLI OCR and two fabricated AI demonstrations. Real-provider configuration
is currently a Python host boundary; the desktop runs offline wording checks.
P4b will improve PDF preview, reviewer controls and explicit OCR/provider setup.
CLEAR is available as a development candidate, not an accepted application release.

PDF review does not imply arbitrary rewriting of a PDF's layout or content. Supported outputs will be stated in the release documentation.

## Help

Report catalog or documentation problems through this repository's issues. Use synthetic reproductions and follow the [contribution guide](https://github.com/nexus-research-software/.github/blob/main/CONTRIBUTING.md).
