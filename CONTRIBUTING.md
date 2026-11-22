[![CONTRIBUTING](https://github.com/OstinUA/Promt-AI-Helper/blob/main/Additional%20files/Image/CONTRIBUTING.svg)](https://github.com/adops-tool)

[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-3e80ed?style=for-the-badge&logo=github&logoColor=white)](https://github.com/adops-tool/awesome-header-bidding/pulls)
[![Open Source](https://img.shields.io/badge/Open_Source-Yes-brightgreen?style=for-the-badge&logo=open-source&logoColor=white)](https://github.com/adops-tool/awesome-header-bidding/pulls)

# Contributing to Awesome Header Bidding

First off, thank you for considering contributing to Awesome Header Bidding. We appreciate your time and effort in helping us build the definitive index of the open-source programmatic stack.

The goal of this project is to curate a high-quality list of header bidding engines and wrappers, debugging tools, identity and consent modules, floor and timeout tooling, and the specifications that define them. To maintain the quality of this list, please review the guidelines below before submitting a pull request.

By participating in this project you agree to abide by our [Code of Conduct](CODE_OF_CONDUCT.md).

## Submission Guidelines

Please ensure your submission adheres to the following core criteria:

- **Relevance:** The resource must sit inside the auction path — a wrapper, an auction server, a Prebid module, a debugging or QA tool, a specification, or reference code around them. Vendor features that are not open source belong in the vendor's own documentation, not here.
- **Active Maintenance:** We only accept active projects. Abandoned or unmaintained tools are merged only when they still explain an architecture that people read today, and the entry must then say when it stopped (for example, "Dormant since 2019.").
- **Direct Links Only:** Absolutely no affiliate, tracking, or referral links are allowed. Link directly to the tool's site or repository — never through search engines, URL shorteners, or redirect services.
- **No Duplicates:** Search `README.md` before adding an entry. One URL may appear only once in the list, in the single category where it fits best.

## Description Standards

Descriptions must be concise, objective, and purely informational.

- **Do:** Focus on the exact utility and core features of the tool, and where it sits in the auction.
  > *Example: "Generates Google Ad Manager line items and key-value targeting from a Prebid.js configuration file."*
- **Don't:** Use marketing fluff, superlatives, or subjective claims.
  > *Example: "The world's best header bidding platform that revolutionizes your yield."*
- Do not include pricing or promotional claims in descriptions.
- One sentence, present tense, third person. If the entry needs two sentences, the resource probably needs its own category.

## The Format

The list is organized as `##` categories, each with a one-line italic description, split into `###` subsections. Every entry is one line, one blank line apart from the next:

```markdown
![github](image/alg_R.png) [Tool Name](https://github.com/org/repo) - Short, objective description of what it does.

![web](image/alg_I.png) [Tool Name](https://example.com) - Short, objective description of what it does.
```

Use the `github` icon when the primary link is a GitHub repository and the `web` icon otherwise. The icon files are in `image/` and are not to be replaced or renamed.

## Step-by-Step Submission Process

To add a tool to the list, please follow these steps:

1. **Star the repository:** Show your support and help the community grow.
2. **Locate the file:** Navigate to the `README.md` file in the main branch of this repository.
3. **Edit the document:** Click the "Edit" (pencil) icon to begin making your changes.
4. **Format your entry:** Add your link to the appropriate category using the exact Markdown syntax above.
5. **Run the checks locally:** See [Automated checks](#automated-checks) below.
6. **Create a Pull Request:** Submit your PR with a clear and descriptive title using the following format: `Add [Tool Name]`.

A PR that only adds an entry needs no other changes. If you also open an issue explaining why the resource is canonical enough to outlive the next release cycle, review goes faster.

## Automated checks

CI runs a single validator, and it must pass before a pull request can be merged:

```bash
python3 scripts/validate_readme.py
```

It checks that:

- every entry line matches the documented format, with a known icon and the matching icon file;
- the `github` icon is used only for `github.com` links and `web` for everything else;
- no URL appears twice;
- every `##` category has a Table of Contents entry and every Table of Contents entry resolves to a real heading;
- all links are `https` and carry no tracking or referral parameters;
- descriptions start capitalized, end with a period, stay under 320 characters, and contain no promotional wording.

Run it from the repository root before pushing. Fixing a format error here takes seconds; in review it takes a round trip.

## Ideas for Contribution

- A module, adapter, or tool that is missing from a subsection where it clearly belongs.
- A specification or standard that has moved and needs its link refreshed.
- A dormant project whose entry no longer states that it is unmaintained.
- Descriptions that drifted from what the tool actually does.
