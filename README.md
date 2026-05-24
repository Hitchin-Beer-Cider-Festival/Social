# hbcf-social

Hitchin Beer & Cider Festival social media assets and Claude skill.

This repository serves two functions:

1. **Claude Code plugin marketplace** publishing the `hbcf-social-media` skill.
2. **Image host** for festival post graphics, served via GitHub's raw URLs and consumed by Publer's bulk CSV uploader.

## Repository structure

```
hbcf-social/
├── .claude-plugin/
│   └── marketplace.json              # Marketplace catalog
├── plugins/
│   └── hbcf-social-media/
│       ├── .claude-plugin/
│       │   └── plugin.json           # Plugin manifest
│       └── skills/
│           └── hbcf-social-media/
│               └── SKILL.md          # The skill itself
├── dist/
│   └── hbcf-social-media.skill       # Packaged bundle for direct download
├── countdown/                        # Daily countdown PNGs
├── sponsors/                         # Sponsor thank-you PNGs (planned)
├── build-up/                         # Setup-week photos (planned)
└── on-site/                          # Live festival photos (planned)
```

## Installing the skill

### Claude Code users

Add the marketplace and install:

```
/plugin marketplace add lekman/hbcf-social
/plugin install hbcf-social-media@hbcf-social
```

Claude Code fetches `marketplace.json` from this repository, discovers the `hbcf-social-media` plugin, and installs the skill into your local environment.

### Claude.ai web or desktop users

Download `dist/hbcf-social-media.skill` from this repository, then upload it via Claude's settings under Skills. The skill will trigger automatically when you ask Claude to draft festival content, thank a sponsor, or prepare a Publer CSV.

## Image hosting convention

Images referenced from Publer CSVs use the GitHub raw URL pattern:

```
https://raw.githubusercontent.com/lekman/hbcf-social/main/<folder>/<filename>
```

Folder convention by content type:

| Folder | Purpose |
|---|---|
| `countdown/` | Daily countdown graphics (`countdown-1.png` through `countdown-launch.png`) |
| `sponsors/` | Sponsor thank-you graphics |
| `build-up/` | Setup-week and pre-festival photos |
| `on-site/` | Live photos from the festival days |

To add a new image:

1. Push the file to the appropriate folder on `main`
2. Verify by opening the raw URL in a browser
3. Reference in the `Media URL(s)` column of the CSV

Publer fetches at CSV import time, so the file must be on `main` and publicly accessible before the CSV is uploaded.

## Updating the skill

1. Edit `plugins/hbcf-social-media/skills/hbcf-social-media/SKILL.md`
2. Bump the version in both `.claude-plugin/marketplace.json` and `plugins/hbcf-social-media/.claude-plugin/plugin.json`
3. Repackage the bundle:
   ```bash
   # From a checkout of anthropics/skill-creator
   python -m scripts.package_skill /path/to/hbcf-social/plugins/hbcf-social-media/skills/hbcf-social-media \
       /path/to/hbcf-social/dist
   ```
4. Commit the SKILL.md change, the version bumps, and the new `.skill` bundle
5. Push to `main`
6. Claude Code users refresh with `/plugin marketplace update hbcf-social`
7. Claude.ai users re-download the `.skill` from `dist/` and re-install

## Festival operations

Operational guidance for the team (voice rules, post templates, hashtag library, Publer workflow, quality checks) lives inside the skill itself. Install the skill and ask Claude for a sponsor thank-you, a countdown post, or a CSV batch.

Publer credentials are stored separately in the team's shared password manager, not in this repository.

## Contact

Maintained by Lekman Consulting Ltd in support of CAMRA North Hertfordshire and Hitchin Rugby Club.
