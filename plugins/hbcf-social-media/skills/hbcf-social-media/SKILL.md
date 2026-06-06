---
name: hbcf-social-media
description: Draft Facebook and Instagram posts, generate branded graphics, process event photos, and prepare Publer CSV bulk uploads for the Hitchin Beer & Cider Festival in the established festival voice. Covers the full visual template library (sponsor thanks, countdown cards, big-number stats, list feature carousels, partner spotlights, launch moments, watermarked event photos), the photo treatment workflow (HEIC conversion, square cropping, hedgehog watermarking), parsing of teammate Word-doc drafts, and the image-vs-video posting strategy. Use this skill whenever asked to write posts for HBCF, thank a sponsor, announce a beer or session, post festival updates, draft countdown posts, prepare event-day carousels, watermark or crop a photo for the festival, parse a draft from Rachel or another teammate, or prepare bulk schedules in Publer. Triggers include "HBCF post", "Hitchin Beer Festival social", "thank [sponsor] for the festival", "countdown post", "Publer CSV", "festival Instagram", "festival photo", "watermark this", "festival video", "festival carousel", "Rachel's draft", "import", "import the batch", "run the import" (the `.import/` folder workflow), or any social media work for the Hitchin Beer & Cider Festival 2026. Use this even if the user just mentions a sponsor name in the context of the festival.
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

## Import command (`.import/` workflow)

The fastest way to turn a teammate's raw drop into ready-to-schedule posts. A teammate puts a base message and the post images into the `.import/` folder at the repo root, then asks to "import". This command runs the whole pipeline end to end: parse the message, brand the images, build the two CSVs, push the images so Publer can fetch them, and hand back short manual Publer steps.

Trigger on: "import", "import the batch", "run the import", or finding content in `.import/`.

`.import/` is gitignored. It is a scratch inbox, not a tracked folder. Its contents are inputs only; the command writes processed outputs into the real asset folders (`community/`, `partners/`, etc.) and `csv/`.

### What the folder holds

- **One base message** — a `.docx`, `.txt`, or `.md` file with the caption text. This is the teammate's voice; treat it as a draft to parse, not to rewrite.
- **One or more images** — `.heic`, `.jpeg`/`.jpg`, or `.png`. Usually real photos that need cropping and the hedgehog watermark. Branded graphics from the design team are the exception (no watermark).

### Steps

1. **Scan `.import/`.** List every document and image. If there is more than one document, ask which is the base message, then read it.
   - Extract `.docx` text with `textutil -convert txt -stdout file.docx` (macOS) or `python-docx`.
2. **Confirm the batch details.** Use `AskUserQuestion` with options for anything not clear from the message:
   - **Batch name** — the `<series>-<batch>` slug for filenames (e.g. `mp-visit`, `day3`).
   - **Target image folder** — `community/`, `partners/`, `sponsors/`, etc. Suggest one from the topic; create a new folder if none fit.
   - **Schedule date and time** — for the `Date` column (`YYYY/MM/DD HH:MM`). Suggest a sensible slot; the user can override.
   - **Single post or carousel** — if a carousel, confirm the slide order.
   - **Photos vs branded graphics** — only real photos get the watermark.
3. **Parse the base message.** Apply the standard fixes from "Parsing drafts from teammates" silently. Preserve the body wording and any urgency. Flag the fixes you made in the final reply.
4. **Draft the FB and IG captions.** Run the voice rules. Add the canonical hashtag block and the partnership line. No `@` mentions in either caption. IG gets the link-in-bio line; FB gets the plain tickets URL.
5. **Brand the images.** For each photo: convert HEIC if needed, centre-crop to 1080×1080, apply the hedgehog watermark (see "Photo treatment workflow"). Skip the watermark for branded graphics. Name files descriptively; number carousel slides in order (`<batch>-1-<subject>.png`). Write them into the chosen folder.
6. **Write alt text** for each image, one per slide, in slide order.
7. **Build the two CSVs.** One Facebook, one Instagram, all 12 columns. `Media URL(s)` is the comma-separated raw URLs in slide order; `Alt text(s)` is the `||`-separated alt texts in the same order. Save as `csv/hbcf-<batch>-facebook.csv` and `csv/hbcf-<batch>-instagram.csv`.
8. **Push to `main`.** Stage the new images and the two CSVs only (never `.import/`). Commit with a `feat(<folder>): ...` message and push, so the raw URLs are live before the user opens Publer.
9. **Verify the raw URLs** return 200 before reporting success.
10. **Present results and short instructions** (see below).
11. **Offer to clear `.import/`** so the next run starts clean. Ask before deleting; these are the teammate's originals.

### Output to present

Keep it short. Most users run this often and do not need the full Publer guide re-explained each time.

- One line per artifact created (images, the two CSV paths, the commit hash).
- Confirmation that the raw URLs resolve.
- The manual Publer steps, condensed:
  1. Publer → Create → Bulk Options → Import CSV → select the **Facebook** CSV.
  2. Load drafts, confirm images attached, select the Facebook page, add `@CAMRA North Hertfordshire` and `@Hitchin Rugby Club` (plus any relevant) via the composer, set the schedule, submit.
  3. Repeat with the **Instagram** CSV (no `@` mentions; set in-image tags if needed).
- A closing line offering more: full Publer walkthrough, a different schedule, or caption edits.

### When to ask vs proceed

- **Ask** when: the batch name or target folder is ambiguous, the schedule is unstated, the carousel order is unclear, or it is uncertain whether an image is a photo or a branded graphic.
- **Proceed without asking** when: there is one document and one or more photos, the topic maps cleanly to a folder, and the message states the date and time. Note the assumptions in the final reply so the user can correct them.

---

## Parsing drafts from teammates

Rachel and other team members often provide draft captions in Word documents (`.docx`) or pasted text. These drafts are good source material but need standard fixes before they are ready for Publer. Apply the fixes silently and flag them in the response when delivering the CSV.

### Standard fixes (apply silently, flag in the reply)

| In the draft | Replace with | Reason |
|---|---|---|
| ` - ` (space-hyphen-space) joiner | `,` (comma) | Reads cleaner; em-dash-adjacent punctuation breaks the voice rules across a campaign |
| `Hitchin Rugby Club` (alone in footer) | `King George V Playing Fields, Old Hale Way, Hitchin, SG5 1XL` | Canonical venue line, includes postcode for travel |
| `@HitchinBeerCiderFestival @camranorthherts ...` block | Drop entirely from the caption | Won't resolve via CSV import; FB mentions are added in composer after import |
| (no partnership line) | Add `In partnership with CAMRA North Hertfordshire and Hitchin Rugby Club.` at the end | Consistent footer across the campaign |
| `Advance tickets still available` on the last day of the festival | `Tickets at the door, no need to book in advance` | Last day; no advance ticket sales |

### Preserve the original

- **Body wording** — the body of the caption is the teammate's voice. Do not paraphrase or "improve" it. Only apply the fixes in the table above.
- **Urgency and tone** — if the draft has urgency ("Today is our last day", "Doors close at 10pm"), keep it intact. Rachel's notes sometimes say "do not soften it"; even when they don't, urgency is intentional.
- **Specific facts** — beer counts, opening times, sponsor names. If anything looks wrong, flag and ask rather than silently changing.

### When to flag and ask

- Ticket framing on the last day (advance vs door) if it's ambiguous
- Photo selection or order if the draft references images you don't have or in an order that doesn't match what was uploaded
- Any factual claim that contradicts known festival facts (dates, address, opening times, scale)
- Anything that affects branding tone (e.g. a draft using emojis or em-dashes — flag rather than rewrite)

### Posting notes from the draft

Drafts often include posting notes at the bottom (e.g. "post before midday", "use alongside your video", "change 11pm to 10pm if posting Saturday"). Treat these as instructions and:
- Schedule the CSV to the time indicated
- Surface any conditional instructions in the response so the human knows what to adjust if circumstances change
- If the notes say "do not soften it", do not soften the urgency

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

## Big number stat post recipe

A single arresting number can carry an entire post. Used during the campaign for:
- `47` ciders, perries and meads at the Cider Bar
- `80` world beers at the International Beer Bar

The shape is one number, one descriptor, framed by festival branding.

### Post template

```
[Kicker:] ON THE CIDER BAR / ON THE INTERNATIONAL BEER BAR
[Hero number:] 47 / 80 (very large, dominant)
[Descriptor:] CIDERS, PERRIES & MEADS / WORLD BEERS

[Body, 80-120 words explaining what attendees will find]

[Standard footer block: dates, venue, hashtags, partnership line]
```

### When to use this template

- A bar or category has a single headline number worth promoting (count, percentage, years)
- The number is between 10 and 999 (single-digit numbers feel small; four-digit numbers crowd the canvas)
- You can write 80-150 words of body content explaining what the number represents

### Graphic specification

See "Visual template library" below for the big-number stat graphic spec.

---

## List feature post recipe

A list of items grouped under one theme works as a multi-slide carousel. Used during the campaign for:
- Dark ales feature: title card + brewery slides (Moor, Kernel, Abbeydale)
- World beer feature: big-`80` card + Belgium list + Germany list (within the same big-number post)

The shape is a title slide followed by 2-4 detail slides, each focused on one item.

### Post template

```
Carousel structure:
- Slide 1: List title card (e.g. "DARK ALES TO TRY")
- Slides 2-4: One item per slide (brewery logo + beer name, or country + beer list)

Caption:
[2-3 sentence intro to the theme]
[Quick list of what's featured in the carousel, plain text]
[Standard footer: dates, venue, hashtags, partnership line]
```

### When to use this template

- A bar has a defined sub-theme worth its own post (dark ales, vegan ales, GF/vegan, light sessions, a specific country's beers)
- 3-4 items make the list (2 is too thin; 5+ overcrowds the carousel and individual slides feel rushed)
- The items are visually distinguishable (different breweries' pump clips, country names, style classifications)

### Graphic specification

See "Visual template library" below for list feature graphic specs.

---

## Partner spotlight recipe

A partner or chosen charity beneficiary post recognises an organisation that is supported by, or supports, the festival. Used during the campaign for:
- Feed Up Warm Up (chosen charity beneficiary, returning for the third year)

### Post template

```
[Kicker:] PROUDLY SUPPORTING
[Centre:] Partner logo (preserved in native colours where possible)
[Festival branding at the bottom]

Caption:
The Hitchin Beer & Cider Festival is delighted to welcome [PARTNER] 
[back for their Nth year with us / to the festival for the first time].

[2-3 sentences on what the partner does, in factual terms]

[Practical call to action: where to find them on site, what they're doing]

[Standard footer + hashtags including #Charity if applicable]
```

### When to use this template

- A charity, community organisation, or non-sponsor partner is associated with the festival
- The partner has a recognisable logo or visual identity
- The relationship is supportive rather than transactional (a sponsor uses the sponsor template instead)

### When NOT to use this template

- Sponsor relationships — use the sponsor thank-you recipe instead
- Suppliers, vendors, contractors — these don't typically get a spotlight unless there's a community angle

### A specific note on Feed Up Warm Up

Feed Up Warm Up is the festival's chosen charity beneficiary, not a partner in the technical sense. Token cards left without refunds, plus any additional money donated by visitors, go directly to the charity. They do not receive funds from the overall festival budget. **This funding mechanism is intentionally not mentioned on social media** — public-facing posts use "supporting" language, not financial detail.

### Graphic specification

See "Visual template library" below for partner spotlight graphic spec.

---

## Launch moment recipe

A celebratory milestone post when doors open. Used during the campaign for:
- "WE ARE OPEN / COME ON IN" at 5pm Thursday

### Post template

```
[Top:] WE ARE OPEN
[Centre:] Pink hedgehog (large, hero)
[Below:] COME ON IN
[Bottom:] HITCHIN BEER & CIDER FESTIVAL 2026

Caption:
We are open. Come on in.

Walk-up tickets are available at the door, no need to book in advance. 
Everyone is welcome.

If you are not drinking, you do not pay to come in. Free entry for 
under-18s, non-drinkers and designated drivers, so bring the family along. 
The marquee is dry, comfortable and stocked with around 200 real ales, 
ciders, perries and meads.

Open until [11pm Thursday and Friday / 10pm Saturday] tonight. See you in there.

[Standard footer + hashtags including #FamilyFriendly]
```

### When to use this template

- A milestone moment that deserves its own post (doors open, daily opening, last day morning)
- Not for general updates — a launch moment is a single-purpose celebratory beat

### Critical messaging points

- **Tickets at the door** — every launch moment should mention door tickets, not push advance sales
- **Family welcome, free non-drinker entry** — distinguishes HBCF from drinks-only events; high-value information for waverers
- **Closing time only, not opening time** — if posted at the moment doors open, "we are open until 11pm" reads as a present statement; including "doors open at 5pm" reads as future tense and confuses

### Graphic specification

See "Visual template library" below for launch moment graphic spec.

---

## Event-day photo recipe

Posts featuring real festival photos taken on the day (or yesterday). Used during the campaign for:
- Volunteer briefing thank-you (Thursday)
- Weather reassurance (Friday, with archival photo)
- Day 2 opening carousel (Friday — glass, customers, queue, bar)
- Day 3 last day carousel (Saturday — welcome desk, attendees, bar, outdoor crowd)

### Post template

```
Carousel:
- 1 to 4 square-cropped photos with hedgehog watermark lower-right
- Slide order tells a story (e.g. welcome → enjoying → action → scale)

Caption:
[Opening line tied to the day or event]

[2-3 sentences of context. If using archival photo, do not claim it's current]

[Practical call to action: what's still available, opening hours, ticket info]

[Standard footer]
```

### When to use this template

- Festival is live or about to open
- You have real photos taken on-site (or archival photos for illustrative purposes)
- The photo itself carries the message; minimal templating

### Photo handling

All photos in this recipe get the standard treatment: HEIC conversion if needed, centre crop to 1080x1080, hedgehog watermark in white box lower-right. See "Photo treatment workflow" below.

### Slide ordering for carousels

A 3-4 slide carousel reads better when slides build a narrative arc rather than appearing in random order. Established patterns:
- Welcome (people/volunteers) → Experience (attendees enjoying) → Action (bar, serving) → Scale (crowd or outdoor shot)
- Product (the glass) → People (attendees) → Demand (queue or busy bar) → Operation (the team running it)

Lead with the most visually distinctive frame; that determines the carousel thumbnail.

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

## Visual template library

The festival's visual identity rests on three things: festival pink `#EC008C`, Bebas Regular typography, and the pink hedgehog mark. Every branded graphic uses these. Photos use the hedgehog as a watermark only (see "Photo treatment workflow" below).

### Brand identity (canonical)

| Element | Value |
|---|---|
| Canvas | 1080 × 1080 PNG (square) for feed posts |
| Background | White (`#FFFFFF`) for branded graphics; photo content for photo posts |
| Brand colour | Pink `#EC008C` (process magenta) |
| Typography | Bebas Regular, all-caps, by Ryoichi Tsunekawa (free for commercial use) |
| Logo | Pink hedgehog (`pink-hedgehog_png.webp`), white pixels treated as transparent before compositing |

Files are saved as PNG with `optimize=True`. Publer accepts JPG, PNG, GIF, MP4. Do not upload Affinity Photo (`.afphoto`), PSD, or other proprietary formats; export to PNG first.

### Template: Sponsor thank-you graphic

The festival uses a consistent sponsor thank-you template, produced by the design team (not this skill):
- Square format (1024×1024 or larger), suitable for both FB and IG
- White background
- `THANK YOU TO OUR SPONSOR` in dark red across the top
- Sponsor logo centred
- `HITCHIN BEER & CIDER FESTIVAL` in dark red across the bottom

### Template: Brewery / cask spotlight

Used for individual brewery features and brewery carousels (e.g. cask brewery curation, craft brewery curation). One slide per brewery.

**Specification:**
- 1080×1080 white canvas
- Top kicker text in pink Bebas: `NEW TO THE FESTIVAL`, `BREWERY SPOTLIGHT`, `CASK BAR PICK`, `CRAFT BAR PICK`, or similar at ~90pt
- Brewery logo centred at approximately 800×400 (scale to fit aspect ratio, keep native colours)
- Bottom-left: `HITCHIN BEER & CIDER` over `FESTIVAL 2026` in pink Bebas ~56pt
- Bottom-right: small pink hedgehog ~130×130

**Logo treatment:**
- If the logo has its own dark/black background, keep it as a dark tile rather than trying to extract — looks like a deliberate design choice (Bishop Nick, Pretty Decent)
- If the logo is on white or transparent, place directly
- Never invert or recolour the logo to match the festival's pink

### Template: Countdown card

Used for the daily countdown posts (days 10 down to 1) and the launch day post. Generated programmatically by this skill.

**Specification:**
- 1080×1080 white canvas
- Top text band: countdown line in pink Bebas ~130pt
  - Days 10 to 2: `X DAYS LEFT`
  - Day 1: `1 DAY LEFT` (singular)
  - Launch day: `OPENS TODAY` (or equivalent short phrase)
- Centre: pink hedgehog ~520×520, transparent background composited over white
- Bottom text band: two lines in pink Bebas ~78pt
  - Line 1: `HITCHIN BEER & CIDER`
  - Line 2: `FESTIVAL 2026`

**File naming convention:**
- `countdown-10.png` through `countdown-1.png` for daily countdown
- `countdown-launch.png` for the Thursday morning launch graphic

### Template: Big number stat post

A single dominant number framed by festival branding.

**Specification:**
- 1080×1080 white canvas
- Top kicker in pink Bebas ~70-80pt: context line (e.g. `ON THE CIDER BAR`)
- Centre: the number itself in pink Bebas at very large size (~480-500pt for two-digit numbers like `47`, `80`)
- Below centre: descriptor in pink Bebas ~70pt (e.g. `CIDERS, PERRIES & MEADS`)
- Bottom-left: `HITCHIN BEER & CIDER` over `FESTIVAL 2026` ~56pt
- Bottom-right: small pink hedgehog ~130×130

**Used in campaign:** Cider Bar `47`, World Beer Bar `80`.

### Template: List feature carousel

Multi-slide carousel for grouped content.

**Slide 1 (title card) specification:**
- 1080×1080 white canvas
- Top kicker in pink Bebas ~85pt: theme name (e.g. `DARK ALES TO TRY`)
- Centre: 3-5 list items in pink Bebas ~70-90pt, each line a brewery name + beer name
- Bottom-left: `HITCHIN BEER & CIDER` over `FESTIVAL 2026` ~56pt
- Bottom-right: small pink hedgehog ~130×130

**Subsequent slides (one per item):**
- Use the brewery / cask spotlight template (above)
- Or a country-list card for international beer carousels (kicker + country name + beer list + branding)

**Used in campaign:** Dark Ales (4 slides), World Beer Bar (3 slides: big-`80` + Belgium list + Germany list).

### Template: Partner spotlight

For charity beneficiaries and community partners.

**Specification:**
- 1080×1080 white canvas
- Top kicker in pink Bebas ~110pt: `PROUDLY SUPPORTING`
- Centre: partner logo in native colours, scaled to ~800×400 box
- Bottom-left: `HITCHIN BEER & CIDER` over `FESTIVAL 2026` ~56pt
- Bottom-right: small pink hedgehog ~130×130

**Logo treatment:**
- Use the partner's native colours, even if they clash with festival pink. The partner's brand identity matters more than visual harmony with the festival
- If the partner logo is supplied on a black background, replace the dark pixels with white before placing (use threshold-based flatten, not transparency, to avoid haloing)

**Used in campaign:** Feed Up Warm Up (orange + blue logo on white festival canvas).

### Template: Launch moment card

A milestone-marker graphic for the moment doors open.

**Specification:**
- 1080×1080 white canvas
- Top in pink Bebas ~160pt: `WE ARE OPEN` (dominant message)
- Centre: pink hedgehog ~460×460
- Below hedgehog in pink Bebas ~100pt: `COME ON IN`
- Bottom centred in pink Bebas ~52pt: `HITCHIN BEER & CIDER FESTIVAL 2026`

**Used in campaign:** Thursday 5pm "we are open" launch moment.

### Template: Photo with hedgehog watermark

Real event-day photos cropped to square with the hedgehog watermark applied lower-right. See "Photo treatment workflow" below for the full procedure.

**Visual specification:**
- 1080×1080 (square crop of the original photo)
- Hedgehog watermark in white rounded box, lower-right, 30px margin
- White box: 180×180, slight rounded corners (radius 12), 235 alpha (slightly translucent)
- Hedgehog: 130×130, pink, centred inside the white box

**Used in campaign:** volunteer briefing thank-you, weather reassurance, Day 2 carousel (4 slides), Day 3 carousel (4 slides).

---

## Photo treatment workflow

When teammates share photos for an event-day post, the photo needs square cropping plus the hedgehog watermark. Photos arrive as iPhone HEIC, WhatsApp JPEG, or DSLR JPEG.

### Step 1: Convert HEIC if needed

iPhone photos arrive as `.HEIC` which PIL doesn't read natively. Install and register the HEIC opener once per session:

```python
import pillow_heif
pillow_heif.register_heif_opener()
# After this, PIL.Image.open() handles .HEIC files transparently
```

Install with `pip install pillow-heif --break-system-packages` if not present.

### Step 2: Centre crop to square

Default to a centre crop. Most festival photos have the main subject central, and centre crop is predictable. The original aspect ratio is usually 4:3 (1.33) landscape or 3:4 portrait; for either, crop to a square by removing equal amounts from the longer dimension.

```python
w, h = photo.size
crop_size = min(w, h)
left = (w - crop_size) // 2
top = (h - crop_size) // 2
photo_sq = photo.crop((left, top, left + crop_size, top + crop_size))
photo_sq = photo_sq.resize((1080, 1080), Image.LANCZOS)
```

**When centre crop is wrong:**
- Subject is significantly off-centre (rare for posed event photos)
- Bar signage or branding is at one edge and you want to preserve it
- Faces or named individuals would be cut off

For those cases, compute a weighted crop manually. Do not write a "smart crop" routine; the photos are too varied for it to be reliable.

### Step 3: Apply the hedgehog watermark

White rounded box in the lower-right corner, with the pink hedgehog centred inside it.

```python
from PIL import Image, ImageDraw

def load_hedgehog(target_size):
    """Load the pink hedgehog and make white pixels transparent."""
    h = Image.open(HEDGEHOG_PATH).convert("RGBA")
    data = [(255, 255, 255, 0) if (r > 240 and g > 240 and b > 240) else (r, g, b, a)
            for (r, g, b, a) in h.getdata()]
    h.putdata(data)
    return h.resize((target_size, target_size), Image.LANCZOS)

def apply_watermark(photo_sq):
    """Composite the hedgehog watermark in lower-right white box."""
    margin = 30
    box_size = 180
    hedge_size = 130

    photo_sq = photo_sq.convert("RGBA")
    overlay = Image.new("RGBA", photo_sq.size, (0, 0, 0, 0))
    draw = ImageDraw.Draw(overlay)
    box_x = photo_sq.width - box_size - margin
    box_y = photo_sq.height - box_size - margin
    draw.rounded_rectangle(
        [(box_x, box_y), (box_x + box_size, box_y + box_size)],
        radius=12, fill=(255, 255, 255, 235)
    )
    photo_sq = Image.alpha_composite(photo_sq, overlay)
    hedgehog = load_hedgehog(hedge_size)
    photo_sq.paste(hedgehog,
                   (box_x + (box_size - hedge_size) // 2,
                    box_y + (box_size - hedge_size) // 2),
                   hedgehog)
    return photo_sq.convert("RGB")
```

### When to apply the watermark (and when not to)

**Apply watermark:** real photographs (HEIC, JPEG from event days, archival photos used in current posts).

**Do not apply watermark:** branded graphics that already include festival branding (sponsor cards, countdown cards, stat cards, partner cards, launch cards). These have the hedgehog and festival name built into the layout already; adding a watermark double-brands them and looks amateur.

### File naming for photos

Use descriptive snake-case names tied to the post or moment:
- `volunteer-briefing.png`
- `weather-marquee.png`
- `day2-1-glass.png`, `day2-2-customers.png`, `day2-3-queue.png`, `day2-4-bar.png`
- `day3-1-welcome.png`, `day3-2-goers.png`, `day3-3-bar.png`, `day3-4-crowd.png`

For carousels, number the slides in the filename so the order is unambiguous when uploaded.

---

## Mixed media: images and videos

Different content types need different treatment. The temptation to mix image and video in one carousel is real; the reliability of doing it via Publer CSV is low. The pattern below favours reliability over feature-completeness.

### Image-only carousels via CSV: reliable

CSV bulk import handles multiple images cleanly:
- Comma-separated URLs in the `Media URL(s)` column
- Matching alt texts in `Alt text(s)` separated by `||`
- Works for both Facebook and Instagram
- Carousel slide order matches URL order in the CSV

This is the default for event-day photo posts.

### Video posts: post separately, native upload

Videos work best as **standalone posts**, not as slides in a carousel:

- **On Instagram:** post as a Reel. Reels get significantly more reach than feed slides or video posts in a carousel
- **On Facebook:** post as a native video post (not a link share)
- **Upload natively** via the FB/IG mobile apps or via Publer's UI; not via CSV
- Posting natively lets the platforms transcode and handle the format conversion automatically

### Codec considerations

iPhone videos default to HEVC (H.265). Facebook and Instagram **prefer H.264** and may transcode HEVC poorly or refuse to upload it. If a video fails to upload:
- Check the codec with `ffprobe`
- If HEVC, convert to H.264 with HandBrake (Mac, free) or ffmpeg one-liner
- MP4 container is more universal than MOV

### Mixed image + video carousels

Both Instagram and Facebook support mixed-media carousels (since 2022 for IG). But **doing this via Publer CSV is unreliable** for two reasons:
- GitHub raw URLs work for images but are not designed for video streaming. Video files load slowly and may time out during Publer's CSV import
- Aspect ratios usually don't match between square photos and landscape video

**Workaround if you really need a mixed-media carousel:**
1. Upload via Publer's UI (not CSV), attaching the video file directly
2. Or pre-convert the video to a square 1080×1080 export with H.264 codec
3. Or — usually best — split into separate posts: one image carousel, one standalone video Reel/post

### Default recommendation

For event-day content, treat images and videos as separate posts. Image carousels via CSV, videos as native Reels/posts. The video gets better engagement on its own anyway.

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

Images for posts are hosted in the `Hitchin-Beer-Cider-Festival/Social` repository on GitHub. The raw URL pattern is:

```
https://raw.githubusercontent.com/Hitchin-Beer-Cider-Festival/Social/main/<folder>/<filename>
```

Folder convention (as established during the 2026 campaign):
- `countdown/` for countdown graphics (`countdown-1.png` through `countdown-launch.png`)
- `brewery-spotlights/` for individual brewery feature graphics (one PNG per brewery)
- `cider/` for Cider Bar feature posts (`cider-bar-47.png` etc.)
- `beers/` for beer style or category feature posts (dark ales, world beer slides, etc.)
- `partners/` for charity beneficiary and community partner posts (Feed Up Warm Up etc.)
- `community/` for event-day photos with watermarks (volunteers, weather, day 2/3 carousels, launch moment)
- `sponsors/` for sponsor thank-you graphics from the design team

When in doubt, choose a folder by topic; create a new folder if the existing ones don't fit. Topic-based folder organisation keeps the repo browsable as the asset library grows year on year.

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
- [ ] Image files actually pushed to `main` of `Hitchin-Beer-Cider-Festival/Social` before CSV upload
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

If the work starts from a drop in `.import/`, follow the "Import command (`.import/` workflow)" section instead; it orchestrates the steps below end to end. The numbered flow here is the manual path for work that does not come through `.import/`.

1. **Understand the brief.** Sponsor thank-you, countdown series, single countdown post, beer announcement, volunteer call-out, big-number stat, list feature, partner spotlight, launch moment, event-day photo carousel, or something else?
2. **If a teammate draft is supplied** (Word doc or pasted text), apply the standard fixes silently (see "Parsing drafts from teammates"). Preserve the original body wording and any urgency.
3. **Gather facts.** Use the research checklist for sponsor posts. For other categories, gather the specific factual content first.
4. **Process photos if needed.** Convert HEIC, centre crop to 1080×1080, apply hedgehog watermark for real photos (not branded graphics). See "Photo treatment workflow".
5. **Decide image vs video strategy.** Image-only carousels go via CSV. Videos go as separate native posts (Reels/native video). Do not mix in a CSV carousel.
6. **Draft the post body.** Follow the appropriate recipe (sponsor, countdown, big number stat, list feature, partner spotlight, launch moment, event-day photo). Run the voice rules in your head as you write.
7. **Produce platform variants.** Facebook and Instagram each need their own version.
8. **Add hashtags and tags.** Pull from the libraries above.
9. **For countdown series, vary the joiners.** Don't let every opener use the same construction.
10. **Run both quality checklists.**
11. **Output:**
    - For a single post: present as two text blocks (FB and IG) for the user to copy into Publer
    - For a batch: produce **two CSV files, one per platform**, named `hbcf-<series>-<batch>-facebook.csv` and `hbcf-<series>-<batch>-instagram.csv`, each containing all 12 Publer columns
    - For a countdown series: produce both CSVs and the PNG graphics
    - For an event-day photo carousel: produce both CSVs plus a zipped folder bundle with the processed photos under the right `community/` (or other) folder for direct unzip into the repo
12. **Note any TBC handles or facts** the user needs to verify before scheduling.

---

## Things this skill does not do

- Generate sponsor thank-you graphics; those come from the design team
- Hold Publer login credentials; those are in the shared password manager
- Schedule posts directly; Publer's UI is used for the final step
- Replace human review; every generated post is reviewed by a human before publishing
- Transcode video; if a video needs codec conversion (HEVC → H.264), use HandBrake or ffmpeg externally
- Generate animated content (Stories, Reels with motion graphics)

---

## Changelog

### v1.4.0 (post-2026 festival)

- **Import command (`.import/` workflow)** — one end-to-end command that turns a teammate's raw drop (base message plus images in the gitignored `.import/` folder) into branded images, two platform CSVs, a push to `main`, and short manual Publer steps. Orchestrates the existing draft-parsing, photo-treatment, CSV, and push sub-workflows. Interactive: asks for batch name, target folder, schedule, and carousel order when not obvious; proceeds with stated assumptions otherwise.
- **`.gitignore` added** — excludes `.import/` (scratch inbox) and `.DS_Store`.

### v1.3.0 (post-2026 festival)

Added based on patterns that emerged during the live 2026 campaign:

- **Parsing drafts from teammates** — the four standard fixes for Rachel's Word-doc drafts ( - joiner → comma, venue line, drop @-block, add partnership line), preservation of body wording and urgency, posting-notes handling.
- **Five new post recipes:**
  - Big number stat post (used for cider 47, world beer 80)
  - List feature carousel (used for dark ales, world beer carousels)
  - Partner spotlight (used for Feed Up Warm Up)
  - Launch moment card (used for the "we are open" 5pm Thursday moment)
  - Event-day photo carousel (used for volunteer briefing, weather, day 2 and day 3)
- **Visual template library** — replaces and expands the previous "Image conventions" section. Documents all seven templates (sponsor, countdown, big number stat, list feature, partner spotlight, launch moment, photo with watermark) with concrete sizing.
- **Photo treatment workflow** — HEIC conversion, centre crop to square, hedgehog watermark in white box lower-right. Includes PIL code references for the watermark and crop routines. Rule about when to apply the watermark (real photos yes, branded graphics no).
- **Mixed media: images and videos** — image-only carousels via CSV (reliable), videos as separate native Reels/posts (better engagement, avoids HEVC codec and GitHub-raw streaming issues), guidance on mixed carousels.
- **Folder convention updated** — `partners/`, `community/`, `cider/`, `beers/`, `brewery-spotlights/` added; topic-based naming for year-on-year repo growth.
- **Workflow steps expanded** — explicit photo processing step, draft parsing step, image/video strategy decision, event-day carousel bundle output.

### v1.1.0 (pre-2026 festival)

Initial published version. Core sponsor and countdown recipes, hashtag and account tag libraries, Publer CSV bulk upload workflow with the confirmed CSV mention-resolution constraint.
