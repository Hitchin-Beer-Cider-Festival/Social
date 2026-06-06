# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Use the festival skill

For any Hitchin Beer & Cider Festival social media request — drafting posts, thanking a sponsor, countdown posts, photo watermarking, event-day carousels, the import flow, or Publer CSVs — follow the skill at [plugins/hbcf-social-media/skills/hbcf-social-media/SKILL.md](plugins/hbcf-social-media/skills/hbcf-social-media/SKILL.md). It is the source of truth for voice rules, post recipes, the hashtag and account-tag libraries, the photo treatment workflow, and the Publer CSV contract.

This applies to `@claude` mentions on GitHub issues and pull requests as well as local sessions.

## What this repository is

Two jobs, not a conventional application:

1. **Claude Code plugin marketplace** publishing the `hbcf-social-media` skill (`.claude-plugin/marketplace.json` → `plugins/hbcf-social-media/`).
2. **Image host** for festival graphics. Publer's bulk CSV uploader fetches images by GitHub raw URL at import time.

There is no build, lint, or test suite. Image processing is done with one-off Python (PIL/Pillow) snippets as described in the skill.

## Canonical raw URL

```
https://raw.githubusercontent.com/Hitchin-Beer-Cider-Festival/Social/main/<folder>/<filename>
```

Publer fetches at CSV import time, so an image must be committed and pushed to `main` **before** the CSV referencing it is uploaded. After pushing images, verify they resolve before reporting done:

```bash
curl -s -o /dev/null -w '%{http_code}\n' https://raw.githubusercontent.com/Hitchin-Beer-Cider-Festival/Social/main/<folder>/<file>.png
```

Asset folders are organised by topic (`countdown/`, `community/`, `charity/`, `cider/`, `beers/`, `partners/`, `brewery-spotlights/`, `sponsors/`). Create a new topic folder when none fit.

## Editing the skill (version + bundle must move together)

The skill ships three coupled artifacts. A change to the skill is incomplete unless all three move:

1. Edit `plugins/hbcf-social-media/skills/hbcf-social-media/SKILL.md`.
2. Bump the version in **both** `.claude-plugin/marketplace.json` and `plugins/hbcf-social-media/.claude-plugin/plugin.json` (semver: new capability → minor, fix/doc → patch). Reusing a published version stops `/plugin marketplace update` from refreshing for anyone who cached it.
3. Repackage `dist/hbcf-social-media.skill` — a zip whose single entry keeps the `hbcf-social-media/SKILL.md` path:

```bash
cd /tmp && rm -rf skillpack && mkdir -p skillpack/hbcf-social-media
cp <repo>/plugins/hbcf-social-media/skills/hbcf-social-media/SKILL.md skillpack/hbcf-social-media/SKILL.md
cd skillpack && zip -r -X <repo>/dist/hbcf-social-media.skill hbcf-social-media/SKILL.md
```

4. Add a changelog entry in SKILL.md.

The marketplace name `hbcf-social` (in `marketplace.json`, used by `/plugin marketplace update hbcf-social` and `/plugin install hbcf-social-media@hbcf-social`) is an ID, not a path — do not change it when the repo path changes.

## Publer CSV contract (non-obvious rules)

- **One CSV per platform.** Produce `csv/hbcf-<batch>-facebook.csv` and `csv/hbcf-<batch>-instagram.csv`; never mix platforms in one file.
- **All 12 columns** in the header even when blank; the structure is part of the import contract.
- **No `@` mentions in captions** on either platform — Publer CSV import does not resolve them. Facebook mentions are added in the composer after import; Instagram uses in-image tags. The skill's account-tag library lists which to add.
- Carousel: `Media URL(s)` is comma-separated in slide order; `Alt text(s)` is `||`-separated in the same order. `Link(s)` stays blank for image-led posts (it converts Facebook to a link-share).

## Import flow (`.import/`)

`.import/` (gitignored) is a scratch inbox: a teammate drops a base message (`.docx`/`.txt`/`.md`) plus images, then asks to "import". The command parses the message, brands the images, writes the two CSVs, pushes images to `main`, and returns manual Publer steps. Inputs only — processed outputs go to the tracked asset folders. Full flow in the skill's "Import command" section.

## Hedgehog watermark asset

The brand hedgehog (`pink-hedgehog_png.webp`) referenced by the skill's watermark code is **not committed**. To watermark photos, extract a clean transparent hedgehog from any `countdown/countdown-*.png` (pink logo centred on pure white; treat white pixels as transparent). The applied watermark is a white rounded box, lower-right, 1080-canvas params: box 180, hedgehog 130, margin 30, radius 12.

## Always manual

Publer is the final step and is never automated from here. Claude prepares captions, images, and CSVs; a person uploads and schedules. Publer credentials live in the team's shared password manager, not this repo.
