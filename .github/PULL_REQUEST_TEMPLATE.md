<!-- Node docs live in comfyui_embedded_docs/docs/<NodeName>/. -->

## What changed

<!-- Which node(s), and which behaviour, parameter or wording. -->

## Localization

`en.md` is the source of truth. The other locales in the folder are generated from `en.md` by the pipeline
in [`docs-generation/`](https://github.com/Comfy-Org/embedded-docs/blob/main/docs-generation/README.md), so
**you are not expected to review translations you did not write**. Fill in what applies so a native speaker
knows what is left.

- Locales touched: <!-- e.g. en -->
- Locales reviewed by me: <!-- e.g. en, ja -->
- Locales left for native-speaker review: <!-- the other locales changed in this PR, or "none" -->

Rules (details in [`AGENTS.md`](https://github.com/Comfy-Org/embedded-docs/blob/main/AGENTS.md)):

- [ ] A content fix went into `en.md` only, and I did not hand-translate the other locales
- [ ] If this touches a value repeated in every locale (parameter name, default, command, URL), I searched
      for the same string and fixed it in each locale, leaving the prose alone
- [ ] Data types stay in English, and parameter names follow the ComfyUI frontend `nodeDefs` translations
- [ ] Section headings use the Inputs/Outputs wording that `AGENTS.md` lists for that language (its table
      covers en, es, fr, ja, ko, zh, ru, fa; locales not in the table are left to the pipeline)

## Checks

- [ ] `bash fix_markdown.sh <NodeName>` reports no errors for the files I changed
- [ ] Optional: previewed the page in ComfyUI after `pip install -e .` (see README)
