# Comic Tools — Requirements & Architecture

Scope: `cp_downloads2comics` (the **Organiser**) and `comic_volume_creator` (the
**Volume Builder**), which share one library at `/mnt/extramedia/Comics`.

> **Covers both apps; stored in the `cp_downloads2comics` repo.** That is a storage
> decision, not an ownership one. `comic_volume_creator` is a separate repository and the
> requirements recorded here — V1–V9, and the §8.4 Q5 Metron removal — bind it just as
> much. It lives here because the Phase 1 work and the test harness already do. If the
> shared module in §8.3 is ever extracted into its own repo, this document moves with it.

Status: **reviewed.** Sections 1–7 describe what is true today and are evidence-backed.
Sections 8–10 are proposals. The seven open questions were **answered on 2026-09-10 and
are recorded in §8.4**; three of the seven needed a follow-up, which is stated there with
the measurement that prompted it.

Every number here was measured against the real library on 2026-09-10, not estimated.
Where a previous document or my own earlier statement was wrong, it is corrected
inline and marked.

---

## 0. What this document supersedes

Both repos already ship their own docs. They are **not** deleted by this one; this
document sits above them and is authoritative where they disagree.

| Document | Standing |
|---|---|
| `cp_downloads2comics/DOWNLOADS2COMICS_REQUIREMENTS.md` | Purpose + out-of-scope still valid. Matching rules partly stale (§4.1). |
| `cp_downloads2comics/DOWNLOADS2COMICS_ARCHITECTURE.md` | Largely accurate. CSV column list stale (13 vs 15). |
| `comic_volume_creator/COMIC_VOLUME_CREATOR_REQUIREMENTS.md` | Purpose valid. Port wrong (says 8765, is 8016). "No metadata enrichment" is now **false** (§4.2). |
| `comic_volume_creator/COMIC_VOLUME_CREATOR_ARCHITECTURE.md` | Filenames/version stale (`_v16`, v1.6 → actual v1.7). 8 auto-logic conditions, not 5. |
| `cp_downloads2comics/Claude.md` | "EXACT or FIRST_WORD" is obsolete — FIRST_WORD was deliberately removed. |

**Corrections to my own earlier reports**, recorded so they are not repeated:

- I called the Beausoleil publisher match a *"live file-moving bug."* **Overstated —
  withdrawn.** The mover has `--dry-run` and an interactive confirmation; nothing moves
  unattended.
- I reported 5 of your "Always Exclude" folders were being scanned despite exclusion.
  **Wrong — retracted.** Both sides strip, so all 142 exclusions match. My test did not
  replicate the real code path.
- The plan claimed `Dead Irons v01_(2009)` → `Dead Irons`. Actual output is `Dead Irons _`
  both before and after the Phase 1 fix. Pre-existing, unrelated to the regex anchoring.

---

## 1. Purpose of each app

### 1.1 The Organiser — `cp_downloads2comics`

Takes freshly downloaded comics from `/home/nesha/Downloads/comics_download/`, works out
where each one belongs in an existing 29,836-file library, writes that plan to a CSV for
you to review, and — only after you confirm — moves the files.

**It is a filing clerk.** Its whole value is the decision *"which folder does this go in,
or does it need a new one."*

Explicitly not for (per `DOWNLOADS2COMICS_REQUIREMENTS.md:161-166`): metadata enrichment,
reading comics, cloud/remote destinations, multi-user, or source trees deeper than one
subfolder level.

### 1.2 The Volume Builder — `comic_volume_creator`

Scans the same library for folders holding loose *numbered issues*, judges whether they
form a complete run, and merges them into a single collected `.cbz` volume — deleting the
source issues on success.

**It is a bookbinder.** Its value is *"these 12 issues are a volume; make one file."*

Explicitly not for (per `COMIC_VOLUME_CREATOR_REQUIREMENTS.md:195-201`): manual metadata
editing, cloud storage, multi-user, undo, reader integration, scheduled scans.

### 1.3 The relationship

They are **sequential stages on one shared asset**, not peers:

```
Downloads ──[Organiser]──> Library ──[Volume Builder]──> Library (fewer, larger files)
```

The Organiser produces the input the Volume Builder consumes. Neither knows the other
exists. That is the root of every problem in §4.

---

## 2. The library — measured reality

Both apps encode assumptions about the library that the library does not satisfy.

| Measurement | Value |
|---|---|
| Comic files total (`.cbz .cbr .zip .rar`) | **29,836** |
| Top-level directories | 2,191 |
| Loose comics at library root (depth 0) | 2,944 |
| Comics at depth 1 | 13,063 |
| Comics at depth 2 or deeper | **13,829 (46%)** |
| Deepest nesting observed | **6 levels** |
| Top-level names with leading/trailing whitespace | **70** |
| Multi-series "container" folders | **85**, holding **4,853 files (16%)** |
| Files not visible to the Volume Builder (`.zip`/`.rar`) | 3 |

### 2.1 46% of the library is deeper than either tool looks — by design

Both apps model the library as **root → series folder → files**. Nearly half the
collection is deeper than that. The Organiser's destination scan walks deeper, but its
*loose-file* logic and the Volume Builder's scanner both operate one level down.

**Settled (§8.4 Q6): this is a boundary, not an oversight.** The one-level model stays and
nothing will recurse. Instead the *root* becomes a parameter, so a nested folder can be
pointed at directly and become level 0 for that run. The Builder already supports this
(`--root`, `/api/browse`); the Organiser does not (`SRC_DIR`/`DEST_DIR`, `:58-59`).

### 2.2 Finding: 85 container folders break "one folder = one series"

Folders that hold many unrelated series. Both apps assume a folder *is* a series.

```
2500 files / 2493 series   2000AD prog
 469 files /  353 series   Europe Comics (Collection)
 157 files /  157 series   Civil War II (Story Arc) (2016-2017)
 141 files /   95 series   Humanoids (Europe)
 109 files /  103 series   2000AD - Collections␣          <- trailing space
  89 files /   54 series   Jodorowsky and Moebius
  58 files /   51 series   Image comics
  45 files /   45 series   Millennium (1988)
  44 files /   44 series   Aftershock comics
  36 files /   33 series   Mark Millar
  34 files /   32 series   Fantagraphics (Europe)
  33 files /   28 series   Neil Gaiman Library
```

They fall into distinct kinds — publisher, creator, event/crossover, anthology — and they
do not all want the same treatment.

**Settled (§8.4 Q3): leave them as they are, mark them, and gate auto-filing by kind** —
publisher and anthology containers may receive files, creator and event containers may
not. No restructuring, no flattening.

### 2.3 Finding: 70 folder names end in whitespace

Folder identity is stored **stripped** (`.comic_exclusions.md`), but the real path is not
stripped. Today this is harmless because both sides strip consistently. It becomes a
defect the moment any code compares an unstripped path — including the `folder_id()`
helper an earlier draft proposed. Two folders differing only in trailing whitespace are
currently indistinguishable.

---

## 3. Functional requirements

Derived from current behaviour plus your stated intent. Requirements marked **settled** in
the Status column were decided by you, not read off the code — see §8.4 for each.

### 3.1 Organiser

| # | Requirement | Status |
|---|---|---|
| O1 | Scan the download folder, one subfolder level deep | implemented |
| O2 | Derive a series name from each filename | implemented, §4.1 |
| O3 | Match against library folders using ordered rules: specific-series → exact → before-dash → trailing-number → publisher → none | implemented (`find_matches:674`) |
| O4 | Never fuzzy/substring match — false positives are worse than misses | **settled, do not re-open** |
| O5 | Subfolder matching is EXACT-only | settled |
| O6 | A dedicated series folder always beats a publisher folder | settled |
| O7 | Write the plan to CSV before touching anything | implemented |
| O8 | Never move without explicit confirmation; dry-run always available | implemented |
| O9 | Rollback moves files back to origin | implemented — **docs wrongly say "delete"** |
| O10 | 2+ loose files of one series ⇒ create a folder, even with no match | settled |
| O11 | Propose cleaned-up filenames, except for Annual/Special/Giant/one-shot | implemented, **undocumented** |
| O12 | Specials and Annuals route to the parent series folder | implemented, inconsistent — §4.3 |
| O13 | Collected editions and single issues share one series folder | **settled §8.4 Q1** — already implemented |
| O14 | Arcs/spin-offs go to the most specific folder that exists, else the parent | **settled §8.4 Q2** — parent-only today; see §4.3 |
| O15 | Confine all writes to the library root | **implemented** — `resolve_under_dest`/`is_plain_name`, §5.2 |
| O16 | Never auto-file into creator or event containers; publisher containers are fine | **settled §8.4 Q3** — not implemented |
| O17 | The library root is a parameter, not a constant | **settled §8.4 Q6** — Builder yes, Organiser no (`:58-59`) |

### 3.2 Volume Builder

| # | Requirement | Status |
|---|---|---|
| V1 | Scan one level for folders of numbered issues | implemented |
| V2 | Classify readiness via 8 conditions (A, A-gap, A2, B, C, D, E, auto-ready) | implemented — **docs say 5** |
| V3 | Flag thresholds S/Y/M = <4 / 4–6 / >6 | settled |
| V4 | Merge into one `.cbz`, `ZIP_STORED`, zero-padded `NN_stem` subfolders for reading order | settled |
| V5 | Delete sources after a successful merge — irreversible, accepted | settled |
| V6 | Confine all writes to `ALLOWED_ROOT` | implemented |
| V7 | Persist exclusions to `.comic_exclusions.md` | implemented |
| V8 | ~~Optionally enrich with Metron metadata + `ComicInfo.xml`~~ | **to be REMOVED — settled §8.4 Q5**; scope statement wins |
| V9 | Volume year = earliest of the issues | implemented — **docs say highest** |

---

## 4. Where the two apps disagree

This is the core architectural problem: **the same domain concepts are implemented twice
and have drifted.**

| Concept | Organiser | Volume Builder | State |
|---|---|---|---|
| `COMIC_EXTS` | `.cbz .cbr .zip .rar` | `.cbz .cbr` | drifted (3 files affected) |
| `VOLUME_PATTERN` keywords | 11 | 7 | drifted |
| Series extraction | `extract_series_name:172` | `extract_series:74` | two impls |
| Normalisation | `normalize_name:231` | `normalize_series:134` | two impls |
| Issue number | `ISSUE_PATTERN:46` | 3 functions (`:91,:99,:111`) | two impls |
| Year | inside `parse_filename:90` | `extract_year:86` | two impls |
| Path confinement | none | `resolve_under_root:605` | **asymmetric** |

### 4.1 Measured: how much do they actually disagree?

Running both apps' series derivation over all 16,007 files they can both see:

- **84.5% produce different strings** — but this headline is misleading and I am not going
  to present it as a bug count. The two functions have *different remits*: the Organiser
  strips year/publisher tags to make a matching key; the Builder keeps them to make a
  display name.
- Normalising away that difference in remit, **444 files (2.8%) genuinely disagree.**

The real problem is not the 2.8%. It is that **`extract_series` and `extract_series_name`
have near-identical names and compute different things, and neither name tells you
which.** Anyone editing one will assume it matches the other.

The 444 break down into four causes:

| Cause | Example | Organiser | Builder |
|---|---|---|---|
| Leading article stripped by one side | `A Legacy of Violence v02` | `legacy of violence` | `a legacy of violence v02` |
| Packaging word is a real title word | `Giant Days v02` | `days` | `giant days v02` |
| `Vol. NN` ordering asymmetry | `Giant Days Vol. 05` | `days` | `giant days vol` |
| Decimal volume | `Side-Kicked v01.5` | `side kicked 5` | `side kicked v01 5` |

### 4.2 The Volume Builder does metadata enrichment its own requirements forbid

`COMIC_VOLUME_CREATOR_REQUIREMENTS.md:195-201` lists "no metadata enrichment (no
OMDB/comicvine integration)" as out of scope. The code has `enrich_cbz():785`,
`inject_comicinfo_into_cbz():768`, `/api/metron-search`, and Metron credentials on
`/api/create`.

This is not a bug — it is a **feature that outgrew its stated scope**. Either the
requirement or the scope statement must change.

**Settled (§8.4 Q5): remove the feature, keep the requirement.** You said you had never
seen any metadata; measured, **162 of 398 randomly sampled `.cbz` files (41%) already
contain a `ComicInfo.xml`** — invisible because neither app displays it, not absent. Shown
that, you still chose removal. So the requirements document was right all along and the
code had drifted out of scope; the code comes back into line. Existing `ComicInfo.xml`
files inside archives are not touched. (No Metron credentials are on disk, so the path is
already inert — removal changes no observable behaviour.)

### 4.3 Matcher behaviour worth a decision, not a fix

These were working as coded; whether the code was right was your call. **Two of the four
have since been answered in §8.4** and are recorded here with their outcome.

- **Collections filed with issues — ✅ CORRECT, not a defect.** `Escape v01 (Collection)`
  lands in the same folder as `Escape 008`/`009`. Also `Undiscovered Country v06`,
  `Blood Type v01`, `Free Planet v02`, `The Forged v04`. §8.4 Q1 confirms one folder per
  series across its whole lifecycle, so this is the intended behaviour. → O13, no change.
- **Arcs collapse into the parent — ⚠️ RIGHT BY DEFAULT, WRONG WHEN A SPIN-OFF FOLDER
  EXISTS.** `100 Bullets - The US of ANGER` → `100 Bullets`;
  `The Rocketeer - Infiltrator` → `The Rocketeer`; `ThunderCats - Cheetara` → `ThunderCats`;
  `Star Trek - Deviations - Evermore` → `Star Trek` — all correct per §8.4 Q2. But the
  collapse is unconditional, so `Die - Loaded v01 - Zero Sessions` also derives `die` and
  is filed into `Die` even though a real `Die - Loaded` folder exists. Same for
  `The Umbrella Academy - Plan B v01`. → O14, needs the most-specific-wins refinement.
- **Specials route inconsistently.** `Supernatural - Wayward Special 001` → `Supernatural` ✅,
  but `Supernatural Valentine's Special 2026 001` → no match ❌ (mid-string year defeats it).
- **Truncation from regex subtraction.** `Star Trek - Red Shirts - Ghost of the 21st Century`
  → `Star Trek - Red Shirts - Ghost of the`; `The Wicked + The Divine - Book 02` →
  `The Wicked + The Divine -`; `Heartthrob Season 3` → `Heartthrob Season`.

### 4.4 The protected-title defect — precisely bounded

`Giant Days` derives to `Days`; `Giant-Man` → `-Man`; `The Complete Peanuts` → `The Peanuts`.
**13 top-level folders** have a packaging word as a genuine title word, and **14 derived
keys are shared by two or more distinct folders.**

I initially assumed this misfiles comics. **It mostly does not,** and the reason matters:
`extract_series_name` (files) and `extract_folder_series_name` (folders) corrupt *both
sides identically*, so `Giant Days 015.cbz` still finds the `Giant Days` folder. When a
folder already exists, the CSV shows the **real** folder name (`generate_consolidation_strategy:757`
uses `match_data["folders"][0]`), so the corruption never reaches disk.

The corruption reaches disk in exactly one case: **no existing folder matches**, so the
new folder is named from the corrupted series string. Measured:

```
Giant Robot Warrior 001 (2024).cbz  -> NONE  -> would create folder 'Robot Warrior'
Man-Thing 001 (1974).cbz            -> NONE  -> exists as 'Giant-Size Man-Thing', not found
```

So the real cost is **fragmentation** — new wrongly-named folders and missed matches
against existing ones — not active misfiling. That is a smaller and more accurate claim
than the one in the original plan.

---

## 5. Non-functional requirements

| # | Requirement | Organiser | Volume Builder |
|---|---|---|---|
| N1 | No data loss | dry-run + confirm + rollback | **deletes sources, accepted** |
| N2 | Reversibility | rollback moves files back | none, by design |
| N3 | Bind to loopback only | binds `"localhost"` | binds `'127.0.0.1'` |
| N4 | Confine writes to the library | `resolve_under_dest` + `is_plain_name` (§5.2) | `resolve_under_root` + `is_plain_name` |
| N5 | Stdlib only, Python 3.8+ | yes | yes (+ `unrar`/`unzip` binaries) |
| N6 | Single user, no daemon | yes | yes |

### 5.1 N3 — a small real difference

`serve_v2.py:341` binds the hostname `"localhost"`; the Builder binds the literal
`'127.0.0.1'`. A hostname goes through resolution and can be remapped in `/etc/hosts` or
resolve to `::1`. Low severity, trivially fixed, worth aligning.

### 5.2 N4 — the Organiser had no library confinement ✅ FIXED

Verified, not theorised. The mover built every destination as:

```python
dest_folder_path = DEST_DIR / dest_folder.strip('/')     # comic_mover.py:182, 224, 305
dest_folder.mkdir(parents=True, exist_ok=True)           # :307
```

`.strip('/')` neutralises an absolute path but **does nothing about `..`**:

```
'Sandman'            -> /mnt/extramedia/Comics/Sandman        ✅
'/etc/cron.d'        -> /mnt/extramedia/Comics/etc/cron.d     ✅ neutralised
'../../../tmp/pwned' -> /tmp/pwned                            ❌ escapes
```

And that value is user-supplied: `comic_mover.py:489-492` copies `dest_folder` from the
overrides JSON straight into `Suggested Folder Name` with no validation. `rename` reaches
a filename the same way (`:494`).

**Honest severity.** This is a single-user tool bound to loopback, and the input comes
from your own browser. It is **not** a remote vulnerability, and I am not going to call it
one. It is a **missing integrity guard**: a typo or a bad override silently creates
directories outside the library, and `mkdir(parents=True)` makes that succeed quietly.
The Volume Builder already solved this exact problem. The asymmetry is the point.

**Settled (§8.4 Q7): fix now**, ahead of the migration, because it is a defect rather than
a design question. **Done.** `comic_mover.py` gained `resolve_under_dest()` and
`is_plain_name()`, mirroring the Builder's `resolve_under_root()`/`is_plain_name()`:

- `resolve_under_dest()` replaces all four `DEST_DIR / x.strip('/')` joins (`:125`, `:182`,
  `:224`, `:305`). It calls `realpath()` *before* comparing, so `..` and planted symlinks
  are both collapsed first, and compares against `root + os.sep` so a sibling like
  `/mnt/extramedia/ComicsOld` is not accepted by a bare `startswith()`.
- `is_plain_name()` guards `Proposed Filename` and `Proposed Files Details`, which reached
  a move destination by the same unvalidated route (`:494`).
- The check is repeated at execution time, not merely at plan time, because `:305` is the
  line that actually calls `mkdir(parents=True)`.
- Escaping rows are skipped with a reason rather than silently dropped.

**Verified behaviour-preserving:** planning against the real 47-row CSV produces the same
55 moves, with **0 rows rejected**. 11 new tests (`test_mover_confinement.py`); suite is
now 50, all green.

One thing worth recording, because it nearly produced a worthless test: `plan_moves()`
checks that the *source* file exists before it resolves the destination, so a row naming a
nonexistent file is skipped for that reason and never reaches the guard. The first version
of the test passed without ever executing the code it claimed to cover. It now redirects
`SRC_DIR` at a tempdir with a real file, and asserts on the *reason* for the skip.

---

## 6. Workflows

### 6.1 Organiser: download → library

```
1. Download comics into ~/Downloads/comics_download/
2. launch.sh  ->  serve_v2.py on :8123
3. UI "Scan"  ->  runs matching_analysis_generator.py
                  writes matching_analysis_consolidated.csv (15 cols) INTO the download folder
4. YOU review each row; may override series name, destination folder, or filename
5. "Dry Run"  ->  comic_mover.py --dry-run, prints every planned move
6. "Consolidate" + confirm  ->  moves execute, log written
7. Rollback available: moves files back to origin, skipping occupied paths
```

Currently 47 rows pending: 25 `CONSOLIDATE`, 12 `COPY_TO_BASE`, 9 `CREATE_FOLDER_WITH_FILES`,
1 `CREATE_FOLDER_FROM_FOLDER`.

### 6.2 Volume Builder: loose issues → collected volume

```
1. launch.sh  ->  comic_volume_creator_server.py on :8016, root-locked to /mnt/extramedia/Comics
2. "Scan"     ->  one level deep; each folder classified by the 8 conditions
                  SIDE EFFECT: rewrites '## Skipped Folders' in .comic_exclusions.md
3. YOU review flags (S/Y/M), exclude folders permanently or temporarily
4. Optional: Metron lookup to attach metadata
5. "Create"   ->  builds NN_stem-ordered .cbz, injects ComicInfo.xml, DELETES sources
```

**Note the side effect at step 2:** a nominally read-only scan writes to disk
(`server.py:589-593`). It is how skipped folders persist, but it means "just scanning"
modifies the library.

---

## 7. Ownership and data contracts

### 7.1 Ownership — exactly one writer each

| Asset | Owner (writes) | Readers |
|---|---|---|
| `/mnt/extramedia/Comics` contents | **both** — Organiser adds, Builder merges/deletes | — |
| `.comic_exclusions.md` | Volume Builder | nobody else — **the Organiser never reads it** |
| `matching_analysis_consolidated.csv` | Organiser generator | `comic_mover.py`, `serve_v2.py` |
| Series-name derivation | *currently nobody — duplicated* | both |
| Volume detection | *currently nobody — duplicated* | both |

Two rows have no single owner. That is the defect §8 addresses.

**Correction to an earlier assumption of mine:** exclusions are purely a Volume Builder
concept. Neither `comic_mover.py` nor `matching_analysis_generator.py` reads
`.comic_exclusions.md` at all. Excluding a folder does **not** stop the Organiser filing
into it.

### 7.2 CSV contract — 15 columns

Live file: `/home/nesha/Downloads/comics_download/matching_analysis_consolidated.csv`.
Written by `matching_analysis_generator.py:1076-1089`.

| # | Column | Kind | Becomes a path? |
|---|---|---|---|
| 1 | `Left Folder` | raw | no |
| 2 | `File Count` | derived | no |
| 3 | `Left Panel File` | raw — **row key** | source path |
| 4 | `Series Name` | **derived** | no |
| 5 | `Action Type` | derived | no |
| 6 | `Suggested Folder Name` | **derived, user-editable** | **YES — §5.2** |
| 7 | `Right Panel Matches (Count)` | derived | no |
| 8 | `Has Existing Folder` | derived | no |
| 9 | `Has Existing Files` | derived | no |
| 10 | `Consolidation Strategy` | derived | no |
| 11 | `Move Source` | derived | no |
| 12 | `Files Details` | raw, `|`-separated | yes |
| 13 | `Right Loose Files` | **derived**, `|`-separated | **YES** |
| 14 | `Proposed Filename` | derived, user-editable | **YES — filename** |
| 15 | `Proposed Files Details` | derived, `|`-separated | yes |

Four columns become filesystem paths. Two of those are user-editable and unvalidated.

**Known format limitation:** `|` is the separator, so a filename containing `|` would
split. No such file exists in the library today; the test suite documents the behaviour
rather than fixing it.

**Housekeeping:** `cp_downloads2comics/matching_analysis.csv` (6 cols, 7 Apr) and
`matching_analysis_consolidated.csv` (9 cols, 8 Apr) inside the repo are **both dead
leftovers** — the live file is in the download folder. Earlier notes said only the first
was stale; both are.

### 7.3 `.comic_exclusions.md` contract

Written by `write_exclusions:273`, read by `read_exclusions:247`.

```markdown
# Comic Volume Creator — Exclusions
## Always Exclude
- /mnt/extramedia/Comics/Some Folder     <- full path
## Temp Exclude
- /mnt/extramedia/Comics/Another         <- full path
## Skipped Folders
- Another                                <- BASENAME ONLY  <- inconsistent
```

**Defect (deferred, not scheduled):** `## Skipped Folders` stores bare basenames while
the other two store absolute paths (`server.py:589`). This is the only place identity is
downgraded, and it is why 2 skipped entries looked stale — their real folders end in a
space (§2.3).

### 7.4 HTTP endpoints

**Organiser** (`serve_v2.py`, port 8123): `GET /`, `GET /api/csv`, `POST /api/scan`,
`POST /api/dry-run`, `POST /api/consolidate`, `POST /api/rescan-series`. Undocumented
body field `selected_ids` on dry-run/consolidate.

**Volume Builder** (`server.py`, port 8016): `GET /`, `GET /api/browse?path=`,
`GET /api/exclusions?path=`, `POST /api/scan`, `POST /api/exclusions`, `POST /api/create`,
`POST /api/metron-search`.

Docs are stale on both: they omit both Builder GETs, list a nonexistent
`/api/comicvine-search`, and give the Builder's port as 8765.

### 7.5 Dead code confirmed

- `serve.py` + `comic_organizer.html` — v1, superseded by v2, nothing references them.
- `find_fuzzy_match():632` — defined, never called; the `FUZZY` branches at `:776,:804,:1048` are unreachable.
- `PUBLISHER_FOLDERS:77` — declared, never read. `find_publisher_match` uses a different inline set at `:558` that has already drifted from it.

I have not deleted any of these — per your standing instruction I report dead code rather
than removing it.

---

## 8. Target architecture — proposal

### 8.1 The one structural change: parse once, into a record

Today both apps derive names by **subtraction** — take the filename, `.sub('')` away
everything that looks like packaging, and hope what remains is a series name. That is why
`Star Trek - Red Shirts - Ghost of the 21st Century` ends as `...Ghost of the`, why
`The Wicked + The Divine - Book 02` keeps a trailing dash, and why `Giant Days` becomes
`Days`. Subtraction leaves debris and has no representation of what the name *is* — only
what survived.

You said it directly: *"far too much reliance on regex for such complex patterns."* I
agree, and I measured it — **37 regex operations** across the two apps (18 Organiser,
19 Builder; the mover has none).

The proposal is to **parse each filename once into a structured record**, and let both
apps read fields off that record instead of each running its own subtraction:

```python
@dataclass(frozen=True)
class Release:
    series: str           # 'Giant Days'   — the actual title, not the leftovers
    volume: int | None    # 5
    issue: str | None     # '015'  (string: preserves zero-padding, allows '1.5')
    year: int | None      # 2016
    tags: tuple[str,...]  # ('digital', 'Son of Ultron-Empire')
    kind: str             # 'issue' | 'volume' | 'special' | 'annual' | 'one-shot'
    original: str         # the untouched filename
```

Then:
- Organiser matching key = `normalize(r.series)`
- Organiser "is this a collected edition" = `r.kind == 'volume'`
- Builder `is_volume()` = `r.kind == 'volume'`
- Builder display name = rebuilt from fields, not from a residue
- `Special`/`Annual` routing = `r.kind`, with `r.series` **intact** — which resolves the
  stripper-vs-detector conflict below

This works by **tokenising then classifying** rather than by boundary regex. It sidesteps
the entire class of bug Phase 1 fixed: there are no `\b` semantics to get wrong, because
words are split once and compared as words. The `contains_words()` helper already added
to the Organiser is the same technique, proven on the publisher matcher.

### 8.2 It resolves the stripper/detector conflict

The plan flagged this as an open question. It has an answer.

`VOLUME_PATTERN` is used two incompatible ways: the Organiser uses it as a **stripper**
(`.sub('')` to get a series name) and the Builder as a **detector** (`.search()` for a
boolean). Sharing one constant between those jobs is what created today's mess, and a
naive shared constant would recreate it.

A record has no such conflict: stripping and detecting are the *same operation* —
parse — and the two apps read *different fields* of the result. There is one producer and
two consumers, which is the pattern that worked for `Right Loose Files`.

### 8.3 What should be shared, and what should not

| Shared module | Rationale |
|---|---|
| `Release` + `parse_release()` | one derivation, two readers |
| `normalize()` | matching keys must be identical or matching is meaningless |
| `COMIC_EXTS` | disagreement means one app cannot see files the other files |
| `resolve_under_root()` | both write to the library; both need the guard |

| Stays private | Rationale |
|---|---|
| Match rule ordering | Organiser-only policy |
| The 8 readiness conditions | Builder-only policy |
| Rename proposals | Organiser-only |
| Exclusions | Builder-only |
| Metron | Builder-only |

The boundary is: **share what a filename *means*; keep private what each app *does about it*.**

### 8.4 Decisions — answered 2026-09-10

**All seven are now settled.** Four were settled on the first answer. Three needed a
follow-up, because the answer as given either contradicted what is already on disk (Q2,
Q3) or rested on a premise I measured and found wrong (Q5). In each case I put the
evidence in front of you rather than quietly reinterpreting your answer — Q2 and Q3 were
then confirmed as refined, and Q5 you decided against my recommendation, which is recorded
as such.

#### Q1 — Collections vs issues ✅ SETTLED

> *"Folders first contain individual issues (accumulated over time) and then I use
> ComicCreator to zip them."*

**One folder per series, across the whole lifecycle.** A series folder holds loose issues
*and* the volumes built from them; they are two states of the same shelf, not two shelves.

Consequences:
- `Escape v01 (Collection)` beside `Escape 008` is **correct**. §4.3 listed this as a
  defect; it is not, and I have removed it from that list.
- Matching needs no collection/issue distinction — `r.kind` becomes display and Builder
  policy only, never a routing key.
- This confirms the Builder's existing model: `get_next_volume_number()` and
  `has_any_volume()` both assume volumes accumulate in the series folder alongside
  whatever else is there.
- **No code change required.** This decision ratifies current behaviour.

#### Q2 — Arcs and spin-offs ✅ SETTLED (refined, then confirmed by you)

> *"Keep arcs/spin-offs in the base series folder."*

I cannot implement that literally, because it would move files you have already filed
deliberately. Two measured problems:

**A. You already keep some spin-offs separate.** Real adjacent folder pairs in the library:

| Parent folder | Separate spin-off folder |
|---|---|
| `Die` | `Die - Loaded` |
| `Criminal` | `Criminal Macabre` |
| `Coins of Judas` | `Coins of Judas - The Gambler` |
| `By the Horns` | `By The Horns Dark Earth` |

A literal collapse rule would file `Die - Loaded v01 - Zero Sessions` into `Die`, emptying
a folder you created on purpose.

**B. "Starts with the same words" ≠ "is a spin-off."** The same detector that found the
table above also produced `Ghost` → `Ghost Pepper` and `Ghost` → `Ghost Projekt`, which
are unrelated series. A prefix rule cannot tell the two cases apart — that is precisely
the substring-reasoning bug class Phase 1 removed.

**Refinement, which you confirmed:**

> **The most specific folder that already exists wins; fall back to the parent when no
> more specific folder exists.**

- `Die - Loaded v01` → `Die - Loaded` exists → files there.
- `Die - Loaded v01` in a library with only `Die` → files into `Die`.
- No new folder is ever invented for an arc; arcs land in the parent by default, which is
  your stated intent.

`parse_release()` already implements this: it returns ordered `series_candidates`
(most specific first) and `resolve()` picks the first that the library actually contains.
This also **fixes a live bug** — today the Organiser derives `die` for
`Die - Loaded v01 - Zero Sessions` and misfiles the spin-off into the parent.

#### Q3 — Container folders ✅ SETTLED (one clause corrected, then confirmed by you)

> *"(a) LEAVE THEM."*

Adopted: the 85 container folders (4,853 files) stay as they are and get marked, not
restructured. But option (a) as I wrote it said *"never auto-file into them"*, and that
clause contradicts a rule you already settled.

**The conflict:** publisher matching (requirement O6) is *supposed* to file into
containers. `Humanoids (Europe)` and `Fantagraphics (Europe)` are both on the 85-folder
container list — they are publisher shelves, and routing a Humanoids release there is the
feature working, not a mistake.

**Recorded rule, splitting by container type:**

| Container type | Example | Auto-file into it? |
|---|---|---|
| Publisher shelf | `Humanoids (Europe)` | **Yes** — this is requirement O6 |
| Anthology | `2000AD prog` | Yes, on exact series match only |
| Creator shelf | `Mark Millar` | **No** — never inferred from a filename |
| Event | `Civil War II` | **No** — crossover membership is not derivable |

#### Q4 — Protected titles ✅ SETTLED

> *"Why txt instead of md? — No good reason; `.md` is better and I have changed it."*

Agreed, and you are right that there was no reason. `.md` is consistent with
`.comic_exclusions.md`, permits a header explaining what the file is for and a comment per
entry, and renders on GitHub. Parsing cost is identical — both are read line by line.

Unchanged from the recommendation: it must **not** live inside `.comic_exclusions.md`,
which the Builder rewrites on every scan.

**Caveat worth stating plainly:** if `parse_release()` is adopted, this file may not be
needed at all. Protected titles exist to stop `Giant Days` becoming `Days` — a subtraction
artefact. A parser that consumes packaging only as a *suffix* never makes that mistake, so
the list becomes an escape hatch for genuine oddities rather than a required input. I would
not populate it eagerly.

#### Q5 — Metron scope ✅ SETTLED: REMOVE, after correcting the premise

> *"Not sure that I ever seen any metadata anywhere? So not needed."*

I challenged the premise before acting on it, because it was wrong on the facts:

**Measured:** of 398 `.cbz` files sampled at random across the library, **162 (41%)
already contain a `ComicInfo.xml`** inside the archive. That is the standard comic metadata
sidecar; readers such as Komga, Kavita and ComicRack read it for series, issue, year,
publisher and credits. The metadata was never absent — it was invisible, because nothing
in either app displays it.

Shown that number, you chose removal anyway. That is a legitimate scope decision rather
than a mistaken one, so it is recorded as settled:

**Remove the Metron enrichment feature.** `enrich_cbz():785`,
`inject_comicinfo_into_cbz():768`, `/api/metron-search`, and the Metron credential
parameters on `/api/create`.

Two things this decision explicitly does **not** do, so nobody later reads it as broader
than it is:

- **Existing `ComicInfo.xml` files inside archives are untouched.** Removal deletes the
  code that *writes* metadata, not any metadata already in your library. The 41% keep
  working in Komga/Kavita exactly as before.
- **It does not merge into the volume-building path.** `inject_comicinfo_into_cbz()` must
  be unwired carefully — the merge step is destructive (V5 deletes sources), and removal
  must not perturb it.

This also resolves §4.2 in the *other* direction from what I recommended: the requirements
document was right and the code had outgrown it, so the code comes back into line rather
than the document being widened.

Ancillary fact, now moot: no Metron credentials are present on disk, so the feature is
already inert in practice. Removal carries no behavioural risk today.

#### Q6 — Depth ✅ SETTLED

> *"Limit to level 1, as in the future I might start consolidating/zipping from another
> (nested) folder."*

Two separate things in one answer, both adopted:

1. **The one-level model stays.** No recursive descent, no nesting model. The 46% of the
   library deeper than level 1 is out of scope by design, not by oversight. §2.1 is
   re-labelled from a finding to a stated boundary.
2. **The root becomes rebasable** so you can point either tool at a nested folder and have
   *that* be level 0. This is the "consolidate from another folder" case.

Current state of (2): the Builder already supports it via `--root` and `/api/browse`. The
**Organiser does not** — `SRC_DIR` and `DEST_DIR` are module constants (`:58-59`). Making
them parameters is the whole of the work.

#### Q7 — Path confinement ✅ SETTLED (it was two questions)

> *"Explain — I would prefer full path everywhere (but I don't have a strong reason)."*

Fair, because I had conflated two unrelated things under one heading. They are:

**(i) Path confinement — a write-safety check.** Before writing, verify the resolved
destination is still inside the library root. Demonstrated on the real code:

```
'Sandman'            -> /mnt/extramedia/Comics/Sandman      ok
'/etc/cron.d'        -> /mnt/extramedia/Comics/etc/cron.d   ok — neutralised by .strip('/')
'../../../tmp/pwned' -> /tmp/pwned                          ESCAPES THE LIBRARY
```

The third escapes because `..` is not stripped and `mkdir(parents=True)` creates whatever
it is handed. This is a **single-user loopback tool**, so it is an integrity guard against
a malformed CSV cell or a typo — not a remote vulnerability, and I am not going to inflate
it into one. The fix is ~10 lines reusing `resolve_under_root()`, which the Builder already
has. **Do it now** — it is a defect, not a design question.

**(ii) "Full paths everywhere" — the folder-identity question (§2.3, §7.3).** Separate
issue: `.comic_exclusions.md` stores absolute paths in two sections and bare basenames in
`## Skipped Folders`. Combined with the 70 folder names ending in whitespace, a basename is
not a reliable identity. **Adopted: absolute paths in all three sections**, with a one-time
migration converting existing basename entries. Your preference and the evidence agree.

---

## 9. Migration path

Incremental, each step independently verifiable, Phase 1's harness as the net. **Nothing
below is started.**

| Step | Change | Verification |
|---|---|---|
| **0** ✅ done | Anchor `VOLUME_PATTERN`; kill substring matching; mover reads the CSV column | 38 tests green; 0 series-key merges |
| **1** ✅ done | Build `parse_release()` **alongside** production code; change nothing | 21 prototype tests green; whole-library compare shows 0 dangerous merges |
| **2** ✅ done | Answer Q1–Q7 | recorded in §8.4 |
| **3** ✅ done | Confine the Organiser's writes (Q7i) | 50 tests green; real CSV plans identically, 0 rows rejected |
| **3b** | Align loopback binding: `serve_v2.py:341` `"localhost"` → `'127.0.0.1'` (N3) | one line |
| **4** | Extract the shared module; both apps import it, behaviour frozen | Byte-identical CSV; no file vanishes from the Builder UI |
| **5** | Switch the Organiser to read `Release` fields | CSV diff explained row by row |
| **6** | Switch the Builder's `is_volume`/`extract_series` | Visible-file count before/after |
| **7** | Apply the remaining decisions: O14 most-specific-wins, O16 container gating, O17 rebasable root, absolute paths in all three exclusions sections | Per-decision test cases + one-time migration |
| **8** | Remove Metron enrichment (Q5): `enrich_cbz`, `inject_comicinfo_into_cbz`, `/api/metron-search`, credentials on `/api/create` | Merge path unchanged; existing `ComicInfo.xml` in archives untouched |
| **9** | Delete dead code (§7.5) | Test suite green |

Step 3 moved ahead of the shared-module work because Q7 settled it as a defect, and it
touches no code the refactor depends on.

**Non-negotiable invariant throughout:** no two previously-distinct series keys may
**merge**. Splitting is allowed — that is un-corruption. Merging silently moves comics
into the wrong folder.

---

## 10. Test strategy

Four layers. Current state: **38 tests, all passing.**

| Layer | Responsibility | Where |
|---|---|---|
| **Unit** | One function, edge cases, no filesystem | `test_series_naming.py`, `test_matching.py` |
| **Golden case** | Real filenames → exact expected output | same, table-driven |
| **Whole-library invariant** | No key merges across 29,836 real files | `TestNoSeriesMerge` + `baseline_series_keys.json` |
| **End-to-end dry run** | Full plan, nothing moved | not yet built — step 3 |

Existing files:

```
cp_downloads2comics/tests/
├── paths.py                     import plumbing; skips if library unmounted
├── baseline_series_keys.json    5,052 keys from 5,152 items, post-Phase-1
├── make_baseline.py             regenerates the above
├── test_series_naming.py        18 — mid-word corruption, underscores, stripping
├── test_matching.py             13 — whole-word publisher/specific matching
└── test_mover_loose_files.py     7 — CSV column consumed verbatim
```

### 10.1 What must never regress

1. `find_loose_right_files()` stays deleted — asserted directly by test.
2. Substring matching never returns — `Soleil` must not match `Beausoleil`.
3. Mid-word stripping never returns — `Signal` must not become `Sial`.
4. Packaging words still strip where they should — `Misty Special` → `Misty`.
5. Zero series-key merges against the real library.

### 10.2 Validation of Phase 1 against the returned files

You moved the 18 previously-misfiled comics into the download folder specifically as a
test. Re-matching all 18 with the fixed logic:

- **16 → `NONE`** — correctly no home, so they become `COPY_TO_BASE` back to the library
  root. Under the old code these were dragged into `Sleep`, `Flow`, `Odin`, `RED`,
  `Vanish`, `Solo`, `Wynd`, `Grit`, `Capes`, `Goblin`, `Nights`.
- **2 → `EXACT`** — `D4VEocracy 001` → `D4VEocracy`, `Sleeper Book 01` → `Sleeper`, both
  their own genuine folders.
- **0 regressions.**

The fix is confirmed against the exact data that exposed the bug.

---

## Appendix — outstanding items not scheduled

- `Heartthrob Season 3 001` → `Heartthrob Season`; you want `Heartthrob`. `ISSUE_PATTERN` question.
- `2000AD` and `2000AD - Collections␣` already share a `series_map` key today, independent
  of any regex change. Your `2000AD_Collections` rename fixes it with no code change — but
  the rename must also update the `## Skipped Folders` entry, whose real folder name ends
  in a space.
- `scan_root()` is annotated `tuple[list, list]` but returns three values (`server.py:497`).
- Folder renames you mentioned: `2000AD_Collections`, `Asterix`, `Nancy In Hell`.
- The 20 `SAME_FRANCHISE` files from the audit are correctly filed — possessives
  (`Clive Barker` → `Clive Barkers`), sequels (`D4VE` → `D4VE2`), a missing space
  (`The Empty Man` → `The Empty Manv02`). **No action proposed**; listed so they are not
  re-flagged next time.
- `shred -u ~/scripts/cp_downloads2comics/github_key_4cp` — **for you to run.** Dead key,
  untracked, gitignored. I have deliberately not read or moved it.
