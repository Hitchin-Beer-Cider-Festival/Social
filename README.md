# hbcf-social

Hitchin Beer & Cider Festival social media assets and Claude skill.

This repository serves two functions:

1. **Claude Code plugin marketplace** publishing the `hbcf-social-media` skill.
2. **Image host** for festival post graphics, served via GitHub's raw URLs and consumed by Publer's bulk CSV uploader.

## Repository structure

```ini
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
├── brewery-spotlights/               # Brewery debut and Craft Bar pick PNGs
├── cider/                            # Cider Bar lineup PNGs
├── beers/                            # Dark ales and other beer feature PNGs
├── sponsors/                         # Sponsor thank-you PNGs (planned)
├── partners/                         # Partner feature PNGs (e.g. Feed Up Warm Up)
├── community/                        # Community/festival update PNGs (volunteers, weather, opening)
├── build-up/                         # Setup-week photos (planned)
├── on-site/                          # Live festival photos (planned)
├── copy/                             # Hand-written post copy (md) for video/manual posts that bypass the CSV pipeline
├── csv/                              # Publer bulk-import CSVs (one per platform per batch)
├── charity/                          # Charity beneficiary post PNGs (e.g. MP visit, Feed Up Warm Up)
└── .import/                          # Scratch inbox for the import command (gitignored); base message + raw images dropped in here
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

## Using the skill

Once installed, the skill handles all festival social work. There are two ways to drive it.

### Conversational (everyday)

Ask Claude in plain language. The skill applies the festival voice, the hashtag and tag libraries, and the Publer CSV rules. What you can ask for:

| Request | Example |
|---|---|
| Sponsor thank-you | "thank Modern Networks for sponsoring the festival" |
| Countdown post or series | a single day, or the full countdown with the countdown card graphics |
| Beer, cider, or bar feature | "announce the ciders on the Cider Bar", dark ales, world beer |
| Big-number stat post | a single dominant number on a branded card (e.g. 80 world beers) |
| List feature carousel | grouped picks across multiple slides |
| Partner or charity spotlight | a community partner or beneficiary (e.g. Feed Up Warm Up) |
| Launch moment | "we are open" style posts |
| Event-day photo carousel | crop and watermark photos, write captions and CSVs |
| Photo treatment | "watermark and crop this photo for the festival" |
| Parse a teammate draft | paste or point at a Word-doc draft; the skill applies the standard fixes |
| Publer CSV batch | produce the two platform CSVs (Facebook and Instagram) ready to upload |

Every post is drafted for human review before scheduling. Publer is always the final, manual step.

### Import flow (batch from a teammate drop)

For a ready-made batch, use the `.import/` folder instead of describing each post:

1. Drop a base message (`.docx`, `.txt`, or `.md`) and the post images into `.import/`.
2. Ask Claude to "import".
3. The skill parses the message, brands the images (square crop plus hedgehog watermark), writes the two platform CSVs into `csv/`, pushes the images to `main` so Publer can fetch them, and returns short manual Publer steps. It asks for the batch name, target folder, schedule, and carousel order when these are not obvious.

`.import/` is gitignored and holds inputs only; processed outputs land in the tracked asset folders (`community/`, `charity/`, etc.) and `csv/`. See the skill's "Import command" section for the full flow.

## Image hosting convention

Images referenced from Publer CSVs use the GitHub raw URL pattern:

```text
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

For the CSV column schema and import workflow, see Publer's guide: [Ultimate CSV Bulk Scheduler for Social Media](https://publer.com/blog/ultimate-csv-bulk-scheduler-social-media/).

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

Operational guidance for the team (voice rules, post templates, hashtag library, Publer workflow, quality checks) lives inside the skill itself. See "Using the skill" above for how to drive it.

Publer credentials are stored separately in the team's shared password manager, not in this repository.

## Contact

Maintained by Lekman Consulting Ltd in support of CAMRA North Hertfordshire and Hitchin Rugby Club.
