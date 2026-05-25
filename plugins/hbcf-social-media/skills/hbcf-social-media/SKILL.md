---
name: hbcf-social-media
description: Draft Facebook and Instagram posts and Publer CSV bulk uploads for the Hitchin Beer & Cider Festival in the established festival voice. Use this skill whenever asked to write posts for HBCF, thank a sponsor, announce a beer or session, post festival updates, draft countdown posts, or prepare bulk schedules in Publer. Triggers include "HBCF post", "Hitchin Beer Festival social", "thank [sponsor] for the festival", "countdown post", "Publer CSV", "festival Instagram", or any social media work for the Hitchin Beer & Cider Festival 2026. Use this even if the user just mentions a sponsor name in the context of the festival.
---

# HBCF Social Media Manager

Voice, post templates, hashtag and tag library, and Publer CSV workflow for the Hitchin Beer & Cider Festival's Facebook and Instagram accounts.

This skill does NOT contain Publer credentials or account passwords. Those live in the team's shared password manager. This skill is the operational playbook only.

---

## Festival facts

| Item | Value |
|---|---|
| Event | Hitchin Beer & Cider Festival 2026 |
| Dates | 4th to 6th June 2026 |
| Venue | Hitchin Rugby Club |
| Full address | King George V Playing Fields, Old Hale Way, Hitchin, SG5 1XL |
| Opening (Thursday) | 5pm to 11pm |
| Opening (Friday) | 12pm to 11pm |
| Opening (Saturday) | 12pm to 10pm |
| Scale | Around 200 beers, ciders, perries and meads |
| Token and glass policy | Entry includes a festival glass and a starter set of tokens to use at the bar. Additional token cards available throughout the festival. Unused tokens and the glass can be refunded on exit. |
| Tickets | https://hitchinbeerciderfestival.org.uk/ |
| Tickets (CAMRA direct) | https://tckty.camra.org.uk/e/499/hitchin-beer-cider-festival-2026 |
| New for 2026 | Free entry for CAMRA and Hitchin Rugby Club members |
| Organisers | CAMRA North Hertfordshire and Hitchin Rugby Club |
| Sponsorship contact | sponsorship@northherts.camra.org.uk |
| Facebook | facebook.com/HitchinBeerCiderFestival |
| Instagram | @hitchinbeerciderfestival |
| Brand pink | `#EC008C` (process magenta, from the hedgehog logo) |
| Brand font | Bebas Regular (Ryoichi Tsunekawa) |

The full address must appear on every post's footer block. `Hitchin Rugby Club` alone is not enough.

---

## Voice rules

These are the exact rules configured in Publer's brand voice. Use them whenever drafting a post, whether for the AI to generate or for a human to write.

**Always:**
- British English throughout (`-ise`, `-our`, `-re` spellings: organise, colour, centre)
- Sentence case body text
- 80 to 150 words of body text before hashtags
- Specific facts: brewery names, sponsor descriptions, opening times, prices
- One clear call to action with a link, where relevant
- The festival's standard footer block (dates, venue, tickets)

**Never:**
- Emojis of any kind, in any position
- Em-dashes (`—`); use commas, semicolons, colons or single hyphens instead
- American spellings
- More than one exclamation mark per post; prefer none
- Hype phrases: "don't miss out", "act fast", "limited time", "you won't believe"
- Corporate jargon: synergy, leverage, stakeholder, unlock, deep dive
- Generic AI phrases: "dive into", "unpack", "in today's world", "let's explore", "elevate"
- Rhetorical-question openers ("Ever wondered...?", "Want to know...?")
- Made-up facts. If a beer name, sponsor description, ABV or detail is unknown, leave a placeholder in square brackets such as `[BEER NAME]` for human review. Never invent.

**CAMRA terminology used correctly:** cask, real ale, perry, mead. Do not call cask ale "craft" unless referring specifically to keg craft beer.

---

## Post structure template

```
1. One-line hook or announcement
2. Two or three sentences of detail
3. Call to action with link (if relevant)
4. Dates and venue block
5. Tickets line and URL
6. Hashtag block
7. Partnership line
```

Caption ends at the partnership line. Facebook `@` mentions are added in the Publer composer after CSV import, not in the caption text (see Account tag library).

### Instagram differences

Use the same body as Facebook, with these adjustments:
- Add `or visit the link in our bio.` immediately after the tickets URL
- No `@` mentions in the caption (Instagram discovery runs on hashtags)
- For sponsor posts, mention the sponsor by name in the body copy. In-image account tags can be set in Publer's per-post UI if the sponsor has an active IG.

---

## Sponsor post recipe

Sponsor thank-you posts follow a stable shape. Use it for every sponsor.

```
We're delighted to have [SPONSOR NAME] supporting the Hitchin Beer 
& Cider Festival 2026 as [TIER PHRASE].

[2-3 sentence company description with one or two verifiable facts: 
location, year established, services or products, local angle if any.]

To learn more, visit their website:
[SPONSOR URL]

We are grateful for their [continued] support of [community events 
in Hitchin / the festival] and proud to have them backing the festival 
this year. [TIER PAYOFF LINE: where attendees will see the sponsor at 
the festival.]

4th to 6th June 2026
King George V Playing Fields, Old Hale Way, Hitchin, SG5 1XL

Advance tickets are on sale now:
https://hitchinbeerciderfestival.org.uk/
[or visit the link in our bio.       <- Instagram only]

[HASHTAG BLOCK]

In partnership with CAMRA North Hertfordshire and Hitchin Rugby Club.
```

For Facebook, `@` mention the sponsor's Page in the composer after CSV import. Use the sponsor's actual Facebook Page name (not their handle from another platform).

### Tier phrases and payoff lines

| Tier | Tier phrase | Payoff line example |
|---|---|---|
| T-shirt sponsor | `one of our t-shirt sponsors` | `Look out for their logo on the volunteer and crew t-shirts across all three days.` |
| Programme sponsor | `our programme sponsor` | `Look out for their branding throughout the festival programme.` |
| Cider Bar sponsor | `sponsors of the Cider Bar` | `Raise a glass at the Cider Bar and you'll see their logo nearby.` |
| International Beer Bar sponsor | `sponsors of the International Beer Bar` | `Raise a glass at the International Beer Bar and you'll see their logo nearby.` |
| Cask sponsor | `one of our cask sponsors` | `Look out for the cask carrying their name on the bar.` |
| General sponsor | `one of our festival sponsors` | (omit a specific payoff line; generic gratitude is enough) |

### "Continued" vs plain support

Use `continued support of community events in Hitchin` only when there is verifiable evidence the sponsor has supported community events before (their own website, news articles, prior sponsorships). Otherwise use `support of the festival`.

### Research checklist for a new sponsor

Before drafting, gather:
1. Verified company name and primary website
2. Year established or years in operation
3. Location and any local angle (Hitchin, North Herts, Hertfordshire)
4. One or two factual products, services, or recognitions
5. Facebook page URL
6. Instagram handle (or confirmation they have none)
7. Sponsorship tier (so the tier phrase and payoff line are correct)
8. Image asset (the sponsor thank-you graphic provided by the festival design team)

Do not draft without these. If something is missing, ask the user or leave a placeholder.

---

## Countdown post recipe

A 10-day daily countdown plus a Thursday-morning launch post is the standard run-up to the festival. Countdown posts publish at 10:00 daily; the launch post publishes earlier at 09:00 to differentiate from the countdown rhythm and to catch the morning scroll before people commit to evening plans elsewhere.

### Daily theme rotation

| Day | Theme | Notes |
|---|---|---|
| 10 | Welcome and scale | Set up the festival, lead with the 200-drinks headline |
| 9 | CAMRA curation | Who chose the range and why it matters |
| 8 | Member free-entry | Catches CAMRA and Hitchin Rugby Club members early |
| 7 | One week to go | Practical, include the session times grid |
| 6 | Cider Bar focus | Differentiates from beer-only festivals |
| 5 | First-time visitor guide | Glass, starter tokens, top-ups, refund on exit |
| 4 | International Beer Bar | Range across cask, cider, international |
| 3 | Volunteer-led ethos | Add `#VolunteerLed #CAMRAVolunteers` to the hashtag block |
| 2 | Logistics and travel | Full address, parking, train station |
| 1 | Eve of opening | Anticipation, last advance ticket nudge |
| 0 (launch) | "It begins tonight" | Schedule 09:00 Thursday; opens at 5pm |

This rotation is illustrative, not fixed. Substitute themes as the year warrants (charity partner highlight, music or entertainment teaser, key sponsor recognition).

### Countdown post template

```
[X days to go opener; see joiner variation rule below]

[2-3 sentences on the day's theme]

Advance tickets are on sale now:
https://hitchinbeerciderfestival.org.uk/
[or visit the link in our bio.       <- Instagram only]

4th to 6th June 2026
[Optional: session times line for the Day 7 logistics post]
King George V Playing Fields, Old Hale Way, Hitchin, SG5 1XL

[HASHTAG BLOCK]

In partnership with CAMRA North Hertfordshire and Hitchin Rugby Club.
```

For Facebook, `@` mention CAMRA North Hertfordshire and Hitchin Rugby Club (always), plus CAMRA national and Hitchin Nub News when relevant, in the Publer composer after CSV import.

### Joiner variation rule

Across a 10+ post series the same opener pattern reads as automated. Vary the sentence joiner across the run:

- Full stop: `"9 days to go. Here is what is waiting..."`
- Colon: `"7 days to go: one week until..."`
- Comma: `"6 days to go, and cider is very much on the menu..."`
- Single hyphen: permitted but use at most once or twice across the series

Single hyphens pass the voice rules per post, but become a tell when overused across a campaign. Each individual post is fine with a dash; the cumulative effect across the series needs variety.

### Launch day (day 0)

The Thursday morning post breaks the `"X days to go"` pattern. Use an opener that signals the moment:

- `"It begins tonight. The Hitchin Beer & Cider Festival 2026 opens at 5pm."`
- `"Today's the day. Doors open at 5pm at Hitchin Rugby Club."`
- `"The festival opens tonight at 5pm."`

Body should cover: scale (200 drinks), session times, member free entry, advance vs gate tickets. Keep to 80-150 words.

---

## Hashtag library

### Canonical block (every sponsor post)

```
#HitchinBeerFestival #HBCF2026 #RealAle #RealCider #CAMRA #Hitchin #NorthHerts #Hertfordshire #SupportLocal #CommunityEvent
```

### Brewery or cask-relevant posts

Add `#CaskAle` between `#CAMRA` and `#Hitchin`:

```
#HitchinBeerFestival #HBCF2026 #RealAle #RealCider #CAMRA #CaskAle #Hitchin #NorthHerts #Hertfordshire #SupportLocal #CommunityEvent
```

### Cider-relevant posts

Add `#Perry` or `#BritishCider` as appropriate.

### Volunteer-related posts

Add `#VolunteerLed` and `#CAMRAVolunteers`.

### Rules

- Cap at 10 hashtags per post unless there is a strong reason to add more
- Keep canonical block intact; add topical tags rather than substituting

---

## Account tag library

### Confirmed: Publer CSV imports do not resolve Facebook mentions in any syntax

Confirmed by Publer support on 2026-05-24. Every attempted CSV-side syntax fails to produce a real Facebook mention:

| Attempted CSV syntax | Behaviour at publish |
|---|---|
| `@camranorthherts` (plain handle) | Publishes as literal text |
| `[Name](https://facebook.com/handle)` (markdown link) | Publishes as literal text |
| Page URL on its own | Publishes as literal text or a link preview |
| Page ID inserted in the caption | Publishes as literal text |

The Facebook API requires the mention to be resolved by selecting a suggestion returned by Publer's composer autocomplete. This is enforced by Facebook (not chosen by Publer), and Publer has stated there are no plans to change CSV import to do this server-side. Reference: https://publer.com/help/en/article/how-to-tagmention-people-or-social-accounts-12vywhs/

**The practical consequence:** Facebook post mentions must be added in the Publer composer after CSV import, every time. Plan for this in the workflow rather than fighting it.

### Facebook tag block (canonical)

```
In partnership with CAMRA North Hertfordshire and Hitchin Rugby Club.
```

No `@` mentions in the CSV caption. The partnership line names the two core partner accounts (CAMRA North Hertfordshire and Hitchin Rugby Club) as plain text. During the post-import review step, the reviewer converts those names to real `@` tags using composer autocomplete, and adds any further tags (sponsor handle, Campaign for Real Ale, Hitchin Nub News) at their discretion.

### Mentions to add in the composer (FB)

For every Facebook post during review, type `@` and select from the autocomplete dropdown:

| Always | Type | Then select |
|---|---|---|
| CAMRA North Hertfordshire | `@CAMRA North` | "CAMRA North Hertfordshire" |
| Hitchin Rugby Club | `@Hitchin Rugby` | "Hitchin Rugby Club" |

| When relevant | Type | Then select |
|---|---|---|
| The Campaign for Real Ale (the national body) | `@CAMRA` or `@Campaign` | "CAMRA" or "Campaign for Real Ale" |
| Hitchin Nub News | `@Hitchin Nub` | "Hitchin Nub News" |
| Sponsor (sponsor posts only) | `@<sponsor name>` | The verified Facebook Page |

Important Facebook tagging rules (per Publer docs):
- Search by **Page name**, not handle or username. Facebook's autocomplete matches the page's display name.
- The result must be selected from the autocomplete dropdown for the mention to register.
- Only Facebook **Pages** can be tagged, not personal profiles.

### Instagram tag block (canonical)

```
In partnership with CAMRA North Hertfordshire and Hitchin Rugby Club.
```

No `@` mentions at all. Discovery on Instagram runs on hashtags; the marginal cross-promotion value of `@` tags does not justify the additional manual step. If a specific sponsor post warrants tagging the sponsor's IG, add it in the composer at review time.

### Verified handles (reference only)

These are the actual platform handles for the orgs we deal with. They are NOT used in CSV captions; they are stored here so the team knows what to search for in composer autocomplete.

| Account | Facebook Page name | Instagram handle |
|---|---|---|
| HBCF (self) | Hitchin Beer Cider Festival | @hitchinbeerciderfestival |
| CAMRA North Herts | CAMRA North Hertfordshire | @camranorthherts |
| Campaign for Real Ale | CAMRA (or Campaign for Real Ale) | @campaignforrealale |
| Hitchin Nub News | Hitchin Nub News | @hitchinnubnews |
| Hitchin Rugby Club | Hitchin Rugby Club | (no active IG, verify before tagging) |

### In-image account tags (Instagram only)

Instagram allows tagging accounts on the image itself, separate from the caption. This is a different mechanism, set up in Publer's UI per post. For sponsor posts, add:
- The sponsor's IG handle, if it exists
- `@camranorthherts`
- `@hitchinnubnews`

These in-image tags resolve correctly even when added in Publer's UI.

---

## Content categories and cadence

Roughly six to eight weeks before the festival, post on this rhythm. Adjust for available material.

| Category | Cadence | Notes |
|---|---|---|
| Countdown | Daily for the final 10 days, plus a launch-day post | See Countdown post recipe above for themes per day |
| Sponsor thanks | One per sponsor, mid-week | Use the sponsor thank-you graphic; tag their accounts |
| Beer or cider promotion | 2 to 3 per week from 3 weeks out | Specific brewery, style, or producer |
| Volunteer recruitment | Fortnightly until 2 weeks before | Link to the volunteering page |
| Member benefit | 2 to 3 times | Highlight the new-for-2026 free entry for CAMRA and HRC members |
| Practical info | Weekly | Opening times, transport, accessibility, food vendors |
| Charity partner | One mid-campaign, one during festival | |
| First-time visitor guide | Built into the Day 5 countdown post | Glass, starter tokens, top-ups, refund on exit |
| Build-up photos | Daily during setup week | Marquee going up, casks arriving, signage |
| On-site live | 2 to 3 per session during festival | Crowds, specific beers being tapped, music |
| Post-event thank-you | 3 posts in the week after | Volunteers, sponsors, attendees (separately) |

---

## Image conventions

### Sponsor thank-you graphics

The festival uses a consistent sponsor thank-you template:
- Square format (1024x1024 or larger), suitable for both FB and IG
- White background
- `THANK YOU TO OUR SPONSOR` in dark red across the top
- Sponsor logo centred
- `HITCHIN BEER & CIDER FESTIVAL` in dark red across the bottom

These graphics are produced by the festival design team. The skill does not generate them.

### Countdown graphics

Used for the daily countdown posts (days 10 down to 1) and the launch day post. Generated programmatically by this skill or by the festival design team.

**Specification:**
- Square format, 1080x1080 PNG
- White background
- Top text band: countdown line in Bebas Regular, approximately 130pt, in festival pink `#EC008C`
  - Days 10 to 2: `X DAYS LEFT`
  - Day 1: `1 DAY LEFT` (singular)
  - Launch day: `OPENS TODAY` (or equivalent short phrase)
- Centre: the pink hedgehog logo at 520x520 px, transparent background composited over the white canvas
- Bottom text band: two lines, both in Bebas Regular, approximately 78pt, also in `#EC008C`
  - Line 1: `HITCHIN BEER & CIDER`
  - Line 2: `FESTIVAL 2026`

**File naming convention:**
- `countdown-10.png` through `countdown-1.png` for daily countdown
- `countdown-launch.png` for the Thursday morning launch graphic

**Assets used:**
- Logo: festival pink hedgehog (same as the website favicon and primary brand mark)
- Font: Bebas Regular by Ryoichi Tsunekawa (free for commercial use)
- Pink: `#EC008C` (process magenta, extracted from the hedgehog logo)

### Improvements being considered for future sponsor graphics

These are not yet implemented for sponsor thank-you templates. Use the current sponsor template until updated:
- Festival hedgehog logo top-left for brand recognition (now in place on countdown graphics)
- Footer strip with dates, venue, and URL
- Tier badge differentiating t-shirt, programme, bar, and cask sponsors
- T-shirt mockup specifically for t-shirt-tier sponsors

### File format

Publer accepts JPG, PNG, GIF, MP4. Do not upload Affinity Photo (`.afphoto`), PSD, or other proprietary formats; export to PNG first.

---

## Publer CSV bulk upload

Reference: https://publer.com/help/en/article/how-to-schedule-in-bulk-using-a-csv-file-3yvwt/

### CSV columns

Publer's template has 12 columns. Keep all 12 in every CSV, even when most are blank; the column structure is part of the import contract. Reference: https://publer.com/blog/ultimate-csv-bulk-scheduler-social-media/

| # | Column | HBCF use | Notes |
|---|---|---|---|
| 1 | Date | Yes | `YYYY/MM/DD HH:MM` (24-hour). Leave blank to auto-schedule via labels. |
| 2 | Text | Yes | The post caption. Newlines preserved when field is quoted. |
| 3 | Link(s) | **No** | Leave blank for countdown and sponsor posts. If populated on Facebook, the post converts to a link-preview share and the image loses prominence. Tickets URL stays inside the Text field. |
| 4 | Media URL(s) | Yes | Publicly accessible image URL. Use the GitHub raw URL pattern below. |
| 5 | Title | No | For videos, LinkedIn PDFs, Pinterest pins only. |
| 6 | Label(s) | Yes | `countdown-fb`, `countdown-ig`, `sponsor-thanks-fb`, `sponsor-thanks-ig`, etc. Used for grouping and auto-schedule. |
| 7 | Alt text(s) | Yes | Accessibility text describing the image. Separate multiples with `\|\|`. |
| 8 | Comment(s) | Optional | First comment text. Published as a visible comment by the same account immediately after the main post. Useful for engagement questions, follow-up CTAs, or moving hashtags out of the caption. Does NOT support `@` mentions (same constraint as the main caption). Multiples separated with `\|\|`. |
| 9 | Board, Album, or Category | No | Pinterest boards, Facebook albums, Google categories. Not used. |
| 10 | Post Subtype | No | `short`, `reel`, `story`, `pdf`, etc. Use when scheduling Instagram Stories or Reels in future; not for countdown feed posts. |
| 11 | CTA | Conditional | Facebook and Google only. **Requires the Link(s) column to be populated**, which conflicts with native image posts. Do not use on countdown or sponsor posts. Useful for dedicated text-led "buy tickets" or "tickets running low" Facebook reminders, where `BUY_TICKETS` is the relevant value. Available CTAs include `BUY_TICKETS`, `LEARN_MORE`, `SIGN_UP`, `DONATE_NOW`, `CONTACT_US`. |
| 12 | Reminder | No | For push-notification reminders. We auto-publish. |

### Critical rule: one CSV per platform

Split posts into two separate CSVs, one for Facebook and one for Instagram. Do not mix platforms in a single CSV.

**Why:**
- Cleaner account assignment in Publer (whole CSV maps to one account)
- Per-platform scheduling can be applied to all rows at once via Publer's "apply to all" UI
- Per-platform differences (link-in-bio line, tag block, future CTA usage) stay encapsulated
- Easier to troubleshoot and edit
- Aligned with Publer's own recommendation when platform-specific columns differ

**Naming convention:**
- `hbcf-<series>-<batch>-facebook.csv` for the Facebook CSV
- `hbcf-<series>-<batch>-instagram.csv` for the Instagram CSV

For example: `hbcf-countdown-day-9-to-launch-facebook.csv` and the matching `-instagram.csv`.

### Other rules

- **Use Google Sheets, not Excel,** when editing CSVs by hand. Publer's documentation is explicit that special characters and styled text only round-trip correctly via Sheets.
- **Keep all 12 columns in the CSV header,** even when most are blank. The structure is part of the contract.

### Image hosting via GitHub

Images for posts are hosted in the `lekman/hbcf-social` repository on GitHub. The raw URL pattern is:

```
https://raw.githubusercontent.com/lekman/hbcf-social/main/<folder>/<filename>
```

Folder convention:
- `countdown/` for countdown graphics (`countdown-1.png` through `countdown-launch.png`)
- `sponsors/` for sponsor thank-you graphics
- `build-up/` for setup-week photos
- `on-site/` for live photos from the festival

To add new images:
1. Push the file to the appropriate folder on `main`
2. Verify by opening the raw URL in a browser
3. Reference in the `Media URL(s)` column of the CSV

Publer fetches the image at CSV import time, so the file must be on `main` and publicly accessible before the CSV is uploaded.

### Upload workflow

Repeat this sequence twice: once for the Facebook CSV, once for the Instagram CSV.

1. **Prepare both CSVs** (Facebook and Instagram) with assembled captions, hashtags, and the plain-text partnership line. Do NOT include `@` mentions in the caption.
2. **Confirm images are pushed to GitHub** and the raw URLs resolve in a browser
3. In Publer: **Create → Bulk Options → Import CSV** and select one CSV
4. Click the upload notification to **load the draft posts**
5. **Verify images attached** automatically from the URLs. If any post shows missing media, wait a minute for GitHub raw to propagate, then retry, or attach manually
6. **Select the social account** for this CSV (Facebook page for the FB CSV, Instagram account for the IG CSV). With one CSV per platform, you can select-all rather than filtering by label
7. **For the Facebook CSV:** open each draft and add `@` mentions via composer autocomplete. Always add `@CAMRA North Hertfordshire` and `@Hitchin Rugby Club`. Add `@CAMRA` (national) and `@Hitchin Nub News` when relevant. For sponsor posts, also add the sponsor's Facebook Page. See Account tag library for the autocomplete trigger strings.
8. **For the Instagram CSV:** no `@` mentions needed in the caption. For sponsor posts, set in-image account tags via Publer's per-post UI rather than typing in the caption.
9. Review every post individually
10. Set scheduling and submit
11. Repeat steps 3 to 10 for the other CSV

### Account assignment

Publer does NOT assign posts to accounts automatically from the CSV. With the two-CSV split, each CSV represents one platform, and you can apply the account to all rows at once. The `Label(s)` column is still useful for organisation and any future auto-schedule rules.

---

## Quality checks before publishing

Run both checklists before scheduling a batch.

### Voice and content checks
- [ ] British English spelling throughout
- [ ] No emojis anywhere in the post
- [ ] No em-dashes; commas, semicolons or single hyphens used instead
- [ ] At most one exclamation mark; ideally none
- [ ] Body text between 80 and 150 words
- [ ] No invented facts; placeholders flagged in square brackets if needed
- [ ] Sponsor name spelled exactly as the sponsor uses it (check their own website)
- [ ] Sponsor URL works (open it; do not trust autocomplete)
- [ ] Tier phrase matches the actual sponsorship agreement
- [ ] Payoff line is plausible (does the sponsor's logo actually appear where you claim?)
- [ ] Festival dates correct: `4th to 6th June 2026`
- [ ] Venue full address used in footer: `King George V Playing Fields, Old Hale Way, Hitchin, SG5 1XL`

### Tags and accounts
- [ ] Hashtag block matches the canonical (or brewery / volunteer variant)
- [ ] FB caption does NOT contain `@` mentions (those are added in composer after import)
- [ ] IG caption does NOT contain `@` mentions
- [ ] Partnership line present at the end of caption naming CAMRA North Hertfordshire and Hitchin Rugby Club
- [ ] No invented handles; only Page names confirmed against the org's own website
- [ ] In-image account tags planned for Instagram (separate from caption, set in Publer UI)

### CSV checks (if bulk uploading)
- [ ] Two CSVs produced, one for Facebook and one for Instagram (not mixed)
- [ ] All 12 Publer columns present in each CSV header, blanks where not used
- [ ] Labels set to `countdown-fb`/`countdown-ig` or `sponsor-thanks-fb`/`sponsor-thanks-ig` matching the CSV's platform
- [ ] Link(s) column blank for image-led posts (otherwise FB converts to link-share format)
- [ ] CTA column blank for image-led posts (requires Link, conflicts with native image)
- [ ] Media URL(s) populated with the GitHub raw URL pointing at the correct folder and filename
- [ ] Image files actually pushed to `main` of `lekman/hbcf-social` before CSV upload
- [ ] Raw image URL verified by opening it in a browser
- [ ] CSV exported from Google Sheets, not Excel
- [ ] Text field opens with double-quote in Publer preview (newlines preserved)

### Publer post-import checks
- [ ] Images attached automatically; if any are missing, wait for GitHub raw to propagate or attach manually
- [ ] Correct account assigned per label (`-fb` to Facebook, `-ig` to Instagram)
- [ ] **Facebook rows: `@` mentions added via composer autocomplete** (CAMRA North Hertfordshire, Hitchin Rugby Club always; CAMRA national, Hitchin Nub News, sponsor as relevant)
- [ ] Facebook mentions display as friendly page names in cyan, not as `@handle` plain text
- [ ] Instagram rows: in-image account tags set if applicable
- [ ] Each post reviewed individually before scheduling

---

## Confirmed sponsors (rolling list)

Update this when new sponsors are signed.

| Sponsor | Tier | Local? | FB | IG |
|---|---|---|---|---|
| Maish Devitt & Associates (MDA Law) | Cider Bar | Yes (Hitchin) | @mda.law | @mda.law |
| Modern Networks | T-shirt | Yes (Hitchin) | @modernnetworks | None (B2B only) |
| Charles Church | T-shirt | Yes (Gosmore, St Ippolyts) | TBC | TBC |
| Buntingford Brewery | Programme | Yes (North Herts) | TBC | TBC |
| Function Security | International Beer Bar | Yes (Hitchin) | TBC | TBC |

When `TBC`, the team should verify the sponsor's actual Facebook Page name and Instagram handle by checking the sponsor's own website footer for social links. Do not guess handles based on the company name. The verified Page name is used in the Publer composer `@` autocomplete during post-import review.

---

## Workflow

1. **Understand the brief.** Sponsor thank-you, countdown series, single countdown post, beer announcement, volunteer call-out, or something else?
2. **Gather facts.** Use the research checklist for sponsor posts. For other categories, gather the specific factual content first.
3. **Draft the post body.** Follow the appropriate template (sponsor recipe, countdown recipe, or general structure). Run the voice rules in your head as you write.
4. **Produce platform variants.** Facebook and Instagram each need their own version.
5. **Add hashtags and tags.** Pull from the libraries above.
6. **For countdown series, vary the joiners.** Don't let every opener use the same construction.
7. **Run both quality checklists.**
8. **Output:**
   - For a single post: present as two text blocks (FB and IG) for the user to copy into Publer
   - For a batch: produce **two CSV files, one per platform**, named `hbcf-<series>-<batch>-facebook.csv` and `hbcf-<series>-<batch>-instagram.csv`, each containing all 12 Publer columns
   - For a countdown series: produce both CSVs and the PNG graphics (using the countdown graphic specification)
9. **Note any TBC handles or facts** the user needs to verify before scheduling.

---

## Things this skill does not do

- Generate sponsor thank-you graphics; those come from the design team
- Hold Publer login credentials; those are in the shared password manager
- Schedule posts directly; Publer's UI is used for the final step
- Replace human review; every generated post is reviewed by a human before publishing
