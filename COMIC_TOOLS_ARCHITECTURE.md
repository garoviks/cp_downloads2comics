# Comic Tools — Requirements & Architecture

Scope: `cp_downloads2comics` (the **Organiser**) and `comic_volume_creator` (the
**Volume Builder**), which share one library at `/mnt/extramedia/Comics`.

> **Covers both apps; stored in the `cp_downloads2comics` repo.** That is a storage
> decision, not an ownership one. `comic_volume_creator` is a separate repository and the
> requirements recorded here — V1–V9, and the §8.4 Q5 Metron removal — bind it just as
> much. It lives here because the Phase 1 work and the test harness already do — and as of
> O18 (§8.5) that is also where the shared parser lives permanently, so this document and
> the code it describes stay together.

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
| Multi-series "container" folders | **122 classified** (§2.2 — the earlier "85" is superseded) |
| Files not visible to the Volume Builder (`.zip`/`.rar`) | 3 |

### 2.1 46% of the library is deeper than either tool looks — by design

Both apps model the library as **root → series folder → files**. Nearly half the
collection is deeper than that. The Organiser's destination scan walks deeper, but its
*loose-file* logic and the Volume Builder's scanner both operate one level down.

**Settled (§8.4 Q6): this is a boundary, not an oversight.** The one-level model stays and
nothing will recurse. Instead the *root* becomes a parameter, so a nested folder can be
pointed at directly and become level 0 for that run. The Builder already supports this
(`--root`, `/api/browse`); the Organiser does not (`SRC_DIR`/`DEST_DIR`, `:58-59`).

### 2.2 Finding: container folders break "one folder = one series"

Folders that hold many unrelated series. Both apps assume a folder *is* a series.

> **The original "85 folders / 4,853 files" count does not reproduce, and should not be
> quoted.** It was measured with the pre-`parse_release` splitter, which recorded
> `2000AD prog` as *2500 files / 2493 series* — one "series" per issue, because it never
> removed the issue number. The same folder is 220 series under `parse_release`. The census
> was rebuilt for O16; the figure that means anything now is **122 folders classified by
> hand** in `.comic_containers.md`, because no count separates a container from an ordinary
> series folder (see §10.7 O16).

```
2512 files /  220 series   2000AD prog
 469 files /  350 series   Europe Comics (Collection)
 309 files /  269 series   Hellboy
 157 files /  157 series   Civil War II (Story Arc) (2016-2017)
 141 files /   93 series   Humanoids (Europe)
 109 files /   79 series   2000AD - Collections␣          <- trailing space
  89 files /   68 series   Jodorowsky and Moebius
  58 files /   51 series   Image comics
  45 files /   45 series   Millennium (1988)
  44 files /   44 series   Aftershock comics
  41 files /   40 series   Mark Millar
  37 files /   35 series   Neil Gaiman Library
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
| O16 | Never auto-file into creator or event containers; publisher containers are fine | **settled §8.4 Q3 + step 7** — exact-match-only, franchise shelves added; ✅ implemented, §10.7 |
| O17 | The library root is a parameter, not a constant | **implemented** — both folders now reach the mover; §10.7 |
| O18 | The Organiser owns the parser; the Builder imports it from the sibling repo | **settled 2026-09-11** — §8.5, no third repo |
| O19 | What the Builder should do with a group whose files carry no ordinal | **settled + implemented** — new `review` status, §10.7; 16 groups demoted |
| O20 | Where the matcher cannot decide, flag the row and remember the answer | **implemented** — four-way `Confidence` + `Blocked Destination` in the CSV, `.comic_matching_rules.md`, two-button decide/undecide; §10.7 |
| O21 | A source file must appear in exactly one plan row | **fixed** — STEP 1 and STEP 2 disagreed on how a file is named, so every file inside a subfolder was planned twice; §10.7 |
| O22 | Report every book the library already holds more than once | **implemented** — `library_duplicates.py` writes `LIBRARY_DUPLICATES.md`, deletes nothing; §10.8 |

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
| V8 | ~~Optionally enrich with Metron metadata + `ComicInfo.xml`~~ | **REMOVED 2026-09-11** — settled §8.4 Q5, verified §10.4; scope statement wins |
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

This table says *what* to share. **§8.5 (O18) answers where it lives** — and finds that
only the first row is shareable without a behaviour change.

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

### 8.5 O18 — where the shared code lives, and why step 4 moves none of it

The table above says *what* to share. It never said *where it lives*, and that is a
separate question because the two apps are **separate git repos**, siblings under
`~/scripts/`, both launched by `launch.sh` under plain system `python3` with no venv.

**Decided 2026-09-11: the Organiser keeps `release.py`; the Builder imports it from the
sibling.** No third repo, no install step. The cost accepted knowingly: the Builder gains
a dependency on a repo it does not own, so cloning the Builder alone will not run until
the Organiser is beside it. Rejected alternatives were a new `comiclib/` repo (a third
thing to commit and back up) and `pip install -e` into user site-packages (an install step
that must be repeated per machine, and which fails *silently* into stale code).

#### Step 4 shrinks to this decision, because three of the four cannot move

Step 4's verification is **"behaviour frozen"**. Measured against that bar, only one of
§8.3's four candidates is actually a move:

| Candidate | Verdict at step 4 |
|---|---|
| `Release`, `parse_release()`, `normalize()` | **already where it belongs.** The Organiser imports it today; under O18 it does not move at all |
| `COMIC_EXTS` | **cannot.** Drifted — the Organiser has `.zip`/`.rar`, the Builder does not. Unifying makes **3 real files appear** in the Builder UI (`Les Vagabond des Limbes` ×2, `Aster Blistok`). "No file vanishes" does not cover files arriving |
| `VOLUME_PATTERN` | **cannot.** Word lists drifted by `Scanlation\|Annual\|Special\|Giant`. Unifying changes `is_volume()` — that is step 6 by definition |
| `resolve_under_root` | **cannot.** Not the same function: the Builder's takes a full path → `str\|None`; the Organiser's `resolve_under_dest` takes a folder *name* → `Path\|None`. Merging is a redesign, not an extraction |

So step 4 is closed as a **decision with no code change**, rather than widened until it
had something to do. Unifying `COMIC_EXTS` is now a step-7 decision in its own right,
because 3 files appearing is a user-visible change that deserves to be chosen.

#### Two hazards checked now so step 6 does not trip on them

1. **No module-name collision, verified.** Putting the Organiser's directory on the
   Builder's path makes *all five* of its top-level modules importable
   (`comic_mover`, `matching_analysis_generator`, `release`, `serve`, `serve_v2`).
   None collides with the Builder's own `comic_volume_creator_server` / `metron_client`,
   and the Builder imports nothing but stdlib. Use `sys.path.append()`, **not**
   `insert(0, …)` — appending keeps the Builder's own directory first, so a future
   Organiser file cannot shadow a Builder module.
2. **`release.py` is safe to import.** Stdlib only (`re`, `dataclasses`), no filesystem
   access at import time, `__main__` guarded. The Builder inherits no scan and no
   library dependency by importing it.
3. **Do not import `COMIC_EXTS` from it.** `release.py` carries the *Organiser's* set,
   including `.zip`/`.rar`. Taking it along with the parser at step 6 would smuggle in the
   widening that this section just deferred.

---

## 9. Migration path

Incremental, each step independently verifiable, Phase 1's harness as the net.

| Step | Change | Verification |
|---|---|---|
| **0** ✅ done | Anchor `VOLUME_PATTERN`; kill substring matching; mover reads the CSV column | 38 tests green; 0 series-key merges |
| **1** ✅ done | Build `parse_release()` **alongside** production code; change nothing | 21 prototype tests green; whole-library compare shows 0 dangerous merges |
| **2** ✅ done | Answer Q1–Q7 | recorded in §8.4 |
| **3** ✅ done | Confine the Organiser's writes (Q7i) | 50 tests green; real CSV plans identically, 0 rows rejected |
| **3b** ✅ done | Align loopback binding: `serve_v2.py` + `serve.py` `"localhost"` → `'127.0.0.1'` (N3) | both bind the literal address |
| **8** ✅ done | Remove Metron enrichment (Q5): `enrich_cbz`, `inject_comicinfo_into_cbz`, `/api/metron-search`, credentials on `/api/create`, the settings panel | see §10.4 |
| **9** ✅ done | Delete dead code (§7.5) | CSV byte-identical; 50 tests green |
| **5** ✅ done | Switch the Organiser to read `Release` fields (and O14, pulled forward) | see §10.5 |
| **4** ✅ closed | ~~Extract the shared module~~ → **O18: the Organiser keeps it, the Builder imports the sibling.** No code moves | see §8.5 — three of the four candidates cannot move at frozen behaviour |
| **6a** ✅ done | Fix `release.py`'s `kind`: unnumbered collected editions parsed as `kind='issue'` | see §10.6 — contained to `kind`, proved over 29,769 files |
| **6b** ✅ done | Switch the Builder's `is_volume` to the **union** `is_volume(n) or kind == 'volume'` — *not* a replacement (§10.6); lands the O18 import wiring | 24 files hidden, **0 revealed**, 0 renames, 0 status changes, grouping purely subtractive |
| **6c** ✅ done | Switch the Builder's `extract_series` to `parse_release(...).series` | 0 files vanished, 0 appeared; 1,604 → 1,530 groups. **Opened O19** — see §10.6 |
| **7a** ✅ done | Absolute paths in the exclusions `## Skipped Folders` section, so trailing-space names stay legible and the file stops rewriting on every scan | 5 tests; the no-op rewrite is caught by counting `write_exclusions` calls, not by comparing bytes |
| **7b** ✅ done | **O19** — demote ordinal-less groups to a new `review` status, excluded from *Select All* | 16 groups `ready` → `review`, nothing else moves; 3 mutations, 3 distinct failures — §10.7 |
| **7c** ✅ done | Unify `COMIC_EXTS` to `.cbz`/`.cbr` across both tools | 0 files dropped; the source dir holds zero `.zip`/`.rar` — §10.7 |
| **7d** | **O16** container gating — classify container folders, exact-series-match only, franchise shelves included | ✅ done — 122 folders classified in `.comic_containers.md`; gate in `find_matches()` — §10.7 |
| **7e** ✅ done | **O17** rebasable root — `--src`/`--dest` on `comic_mover.py`, wired through `serve_v2.py` and the UI | Was a live defect, not just a missing flag: scan and move used different libraries. 15 tests, 3 mutations — §10.7 |
| **7f** ✅ done | **O20** flag what the matcher could not decide, and save the answer — `Confidence` + `Blocked Destination` in the CSV, marked rows and a one-click rule in the UI, `.comic_matching_rules.md` | Closes both misfiles O16 could not see. 13 of 119 rows flagged, and a ruled row settles; 34 tests, 18 mutations — §10.7 |

Steps 3, 3b, 8 and 9 were pulled ahead of the shared-module work and the table reordered
to match. Each is self-contained and touches no code the refactor depends on: 3 and 3b
are defects Q7/N3 settled, 8 deletes a feature outright, 9 deletes code nothing calls.
Doing them first shrinks the surface step 4 has to move.

**Step 5 was also taken before step 4, deliberately.** Step 5 does not need the module
extracted — the Organiser can import `release.py` where it sits. Taken the other way
round, step 4 moves code *and* step 5 changes behaviour, so any CSV diff would have two
possible causes and neither step could be verified on its own. Done in this order, step 4
becomes what its verification line already claims it is: a byte-identical file move with
both callers already proven against the real library. **O14 was pulled forward into step 5
as well** — the candidate-aware index made one destination key (`Sleeper`) newly ambiguous,
and shipping a known instance of a problem with a scheduled fix is worse than doing the
fix now. §10.5 has the measurement.

**Then step 4 turned out to have nothing left to do.** Taking 5 first was supposed to
reduce step 4 to a byte-identical file move; answering the ownership question (O18, §8.5)
reduced it to zero, because the Organiser keeps the parser and the Builder reaches for the
sibling at step 6. Measuring the other three shared-module candidates against step 4's own
"behaviour frozen" bar then showed none of them *can* move there. Closed as a decision
rather than widened until it had work in it — the alternative was unifying `COMIC_EXTS`
and `VOLUME_PATTERN` under a step whose verification explicitly forbids behaviour change.

**Non-negotiable invariant throughout:** no two previously-distinct series keys may
**merge**. Splitting is allowed — that is un-corruption. Merging silently moves comics
into the wrong folder.

---

## 10. Test strategy

Four layers. Current state: **280 tests in the Organiser, 16 in the Builder, all passing.**
The Builder's are newer and live in its own repo: `tests/test_exclusions_roundtrip.py` (7a)
and `tests/test_review_status.py` (O19).

| Layer | Responsibility | Where |
|---|---|---|
| **Unit** | One function, edge cases, no filesystem | `test_series_naming.py`, `test_matching.py`, `test_release.py` |
| **Golden case** | Real filenames → exact expected output | same, table-driven |
| **Whole-library invariant** | No key merges across 29,836 real files | `TestNoSeriesMerge` + `baseline_series_keys.json` |
| **Pinned judgement** | Every merge that *was* accepted, with its reason | `TestAcceptedMerges` |
| **End-to-end dry run** | Full plan, nothing moved | not yet built — step 3 |

Existing files:

```
cp_downloads2comics/tests/
├── paths.py                     import plumbing; skips if library unmounted
├── baseline_series_keys.json    5,081 keys from 5,152 items, post-step-5
├── make_baseline.py             regenerates the above
├── test_series_naming.py        mid-word corruption, underscores, stripping,
│                                candidate ordering, pick_destination_folder,
│                                the merge invariant, the 13 accepted merges
├── test_release.py              the parser itself, promoted from prototype/
├── test_matching.py             13 — whole-word publisher/specific matching
├── test_mover_loose_files.py     7 — CSV column consumed verbatim
├── test_library_duplicates.py   10 — the duplicate report's demotion rules
└── test_duplicate_skip.py       27 — the flag, the page count, the decision,
                                      and the refusal
```

**Why `TestAcceptedMerges` exists.** `baseline_series_keys.json` is a snapshot, so
regenerating it silently absolves whatever merged at that moment — the invariant then
passes for the wrong reason and the judgement survives only as a sentence in a commit
message. Step 5 accepted 13 merges. Each is now asserted individually with the reason it
is correct, so re-splitting any of them fails a test. A snapshot records *what* changed;
these record *why it was allowed to*.

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

### 10.3 Validation of the matcher against 92 real releases

`prototype/match_downloads.py`. Read-only. This closes the evidence gap flagged in the
original plan: name *parsing* had been tested, the *matcher* against real folders had not.

| | live | prototype |
|---|---|---|
| matched to an existing series | 55 of 92 | **56** of 92 |
| **matched by live but NOT by the prototype** | — | **0** |
| agree on the series chosen | — | **88 of 92** |

**Zero regressions.** No file that live places today becomes homeless under the prototype.
All four disagreements are below, with what is actually on disk:

| Release | live | prototype | verdict |
|---|---|---|---|
| `Heartthrob Season 3 001` | `NONE` | `Heartthrob (2016)` ✅ folder exists | **prototype** — this is the outstanding issue in the appendix |
| `Ghost Machine - The Official Guidebook 05` | `Ghost Machine` (no such folder) | `Ghost Machine - The Official Guidebook` ✅ folder exists | **prototype** — Q2 most-specific-wins |
| `Invincible Universe - Battle Beast 011` | `Invincible Universe` (no such folder) | `Invincible Universe - Battle Beast` ✅ folder exists | **prototype** — Q2 most-specific-wins |
| `Starhenge Book Two - a Kiss for Atticus 03` | `Starhenge Book Two - A Kiss For Atticus` | `Starhenge` | **judgement** — both are loose files, no folder. Under Q1 the prototype is right: Book One and Book Two are one series. |

Q2 and Q3 are therefore confirmed against real data rather than invented examples: the two
most-specific-wins cases both resolve to folders that genuinely exist, and **0 of 92 files
route into a creator or event container.**

#### Two harness bugs found on the way, both mine

Recorded because each produced a confident, wrong number, and the same mistakes would
distort step 4–6 verification:

1. **Unequal universes.** The first run built the prototype's library from top-level
   folder names only, while live's `find_exact_match():604` also accepts a match against a
   *loose file* in the library root. Prototype scored 35 vs 55 — it looked much worse than
   it is. Both sides must resolve against the same set.
2. **Mixed normalisers.** The second run took the prototype's library keys from live's
   `dest_map`, whose keys live derived with its own corrupted extractor.
   `Giant Robot Hellboy Returns` is a loose file that live corrupts *identically on both
   sides* to `Robot Hellboy Returns`, so it matches itself; the prototype read the incoming
   file correctly and then found no such key. That is a harness artefact, not a parser
   defect. Each side must derive library keys with its own parser.

Both were caught by checking *why* a number came out, not by the number looking wrong.

#### One real prototype fix it produced

`Cindy and Biscuit` failed to match the loose `Cindy and Biscuit - We Love Trouble.cbz`.
`parse_release()` was already returning both candidates; the index was only storing the
most specific one. The rule adopted, which splits by what the name *is*:

- a **folder** indexes under its full name only — the folder name is a deliberate choice,
  so `Ghost Machine - The Official Guidebook` must not also answer to `Ghost Machine`, or
  an unrelated `Ghost Machine 001` gets swept into the guidebook;
- a **loose file** indexes under *every* candidate — no folder exists yet, and grouping is
  the entire point.

#### Observation, not a defect

17 folders are named `... (Collection)`, `... (TPBs)` and similar. Q1 settled that issues
and collections share one folder, so routing a single issue into `100 Bullets (TPBs)` is
consistent with the decision — but the *folder name* then misdescribes its contents. This
is a library-naming question, not something the code should decide.

**Decided 2026-09-11: leave them exactly as they are.** No rename, and no special-casing
of the `(Collection)` / `(TPBs)` suffix in the parser. Closed — do not re-raise.

### 10.4 Verification of the Metron removal (step 8)

Q5 removes a feature from the Builder, whose `/api/create` is **destructive** — V5 deletes
the source files after a successful merge. So the bar was not "does it still start" but
"is the merge path provably the same code".

**Proof it was untouched, rather than an assertion that it was.** Each function was
extracted by AST from `git show HEAD:` and from the working tree and SHA-256'd. All six
identical, including the 120-line merge function:

| Function | Lines | HEAD vs working tree |
|---|---|---|
| `create_cbz_direct` — **the destructive path** | 120 | `3d5750b5…` identical |
| `extract_issue_number` | 10 | identical |
| `scan_root` | 104 | identical |
| `write_exclusions` | 14 | identical |
| `resolve_under_root` | 20 | identical |
| `is_plain_name` | 15 | identical |

**End-to-end run against a throwaway root**, server started with `--root` at a tempdir
holding three real CBZs, one of which carried a pre-existing `ComicInfo.xml`:

1. `/api/scan` grouped all three and proposed `Test Series v01` — unchanged.
2. `/api/metron-search` → **HTTP 404**, endpoint gone.
3. `/api/create` → `success: true`, all six stages logged, sources deleted, volume built.
4. **The pre-existing `ComicInfo.xml` survived byte-for-byte** (`PRESERVE ME` still in it).
   This is the promise made in Q5: removal deletes the code that *writes* metadata, never
   metadata already in the library.
5. Confinement still refuses `/tmp` with the 403 from step 3 — the removal did not disturb
   the write-safety check that sits in the same handler.

**One thing the removal had to fix rather than merely delete.** The old settings panel
stored a Metron password in browser `localStorage` **in plain text**, and the only "Clear"
button lived in the panel being deleted. Deleting the feature would have stranded the
credential with no way to reach it, so the page now removes `mc_username`, `mc_password`
and `mc_auto_enrich` on load.

`metron_client.py` is left in the repo, unimported. Deleting it is a separate decision;
it costs nothing and is the only record of the API shape if this is ever wanted back.

### 10.5 Verification of the parser switch (step 5)

Step 5 replaces the Organiser's series derivation with `release.parse_release()`. Unlike
step 8 this **is** expected to change output, so "identical" is not the bar. The bar the
table sets is *every* difference explained, and the invariant that no file loses a home.

#### What changed in the code

| Change | Why |
|---|---|
| `parse_filename()` **deleted**; `extract_series_name()` delegates to `parse_release()` | subtraction has no model of what a name *is*, only of what survived — §5.1 |
| new `extract_series_candidates()` | ambiguity is resolved by the library, not the filename |
| destination index is candidate-aware | folders index under one key, loose files under all — the rule §10.3 produced |
| `find_matches` Rule 2 walks the candidate list, most specific first | Q2 most-specific-wins, now driven by the parser |
| Rule 2c **deleted** | proved *unreachable*, not merely unused — below |
| new `pick_destination_folder()` | O14, pulled forward — below |

#### Rule 2c: unreachable, not unused

The two fallbacks were measured over all 92 downloads × 5,152 library items — **5,244
samples, zero fires each**. Zero fires alone justifies deleting nothing; it only says the
data did not exercise the path. The two were then treated differently:

- **2c** (`2000AD prog 2485` → `2000AD prog`) is *structurally* unreachable. Its input is
  always a `parse_release()` series, and the parser cuts the title at the first **strong**
  number — three or more digits always qualifies. A trailing 3–4 digit run is therefore
  consumed as the issue number and can never survive into a series name. The only survivor
  would be a series that is nothing but digits, and the rule's own `\s+\d{3,4}$` requires
  preceding whitespace, so that misses too. **Deleted, with the proof in the comment.**
- **2b** (before-dash fallback) has a reachable case left: `src_series` is the group key
  taken from the *first* file in a group, so it can contain ` - ` when the file being
  matched does not. **Kept**, with both facts recorded — the zero measurement and the one
  case that keeps it alive.

#### O14, and a regression I introduced

The candidate-aware index made the whole-library invariant report 12 merges. Rather than
accept or revert it wholesale, the right question was how many destination keys now hold
**more than one folder**: **17 before, 10 after** — the change removes seven ambiguities
and creates exactly one, `Sleeper`, which now holds `Sleeper 001-012`,
`Sleeper - Season One 01-12` and `Sleeper - Season Two 001-012`, because `Season N` is
absorbed as a run marker (which is what you asked for at the *file* level:
`Heartthrob Season 3 001` → `Heartthrob`).

Without a tie-break the winner was whatever `os.scandir` yielded first, so
`Sleeper - Season Two 003.cbz` had a two-in-three chance of the wrong folder. That is a
known problem with a scheduled fix, so O14 was brought forward instead of shipped:
`pick_destination_folder()` picks the most specific folder the **filename itself names**
(whole-word, so `Sleeper` cannot match inside `Sleepers`), ties broken by **file count** —
`Hello Darkness` and `Hello Darkness (2024)` are both real, and alphabetical order would
have split the series across both. Where the filename names none of them, it sorts for
reproducibility rather than guessing; this string becomes a path, so run-to-run stability
matters more than cleverness.

#### The CSV diff, row by row

| | before | after |
|---|---|---|
| rows | 96 | **96** — none added, none removed |
| rows with any changed cell | — | 30 |
| rows that changed an actual **decision** | — | **3** |
| `CONSOLIDATE` / `COPY_TO_BASE` / `CREATE_FOLDER_WITH_FILES` / `CREATE_FOLDER_FROM_FOLDER` | 46 / 35 / 14 / 1 | 47 / **34** / 14 / 1 |

**Zero files lost a home; one gained one.** The 27 other changed rows are series-name and
display-string improvements that route to the same place. All three decision changes are
the ones this step exists to make:

| Release | before | after | verdict |
|---|---|---|---|
| `Giant Robot Hellboy Returns 02` | `/Robot Hellboy Returns/` | `/Giant Robot Hellboy Returns/` | Phase-1-class mid-word corruption, finally gone from a **path** and not just a display column |
| `Heartthrob Season 3 001` | `COPY_TO_BASE` to `/` | `CONSOLIDATE` into `/Heartthrob (2016)/` | the appendix item you raised, now landed |
| `Starhenge Book Two - a Kiss for Atticus 03` | own folder, 1 loose file | `/Starhenge/`, gathering Book One and Book Two | Q1 — the §10.3 judgement call, applied |

`prototype/compare.py` re-run against the whole library: **safe on the merge invariant
(splits only), 0 DANGEROUS.**

#### Three defects the diff found

The diff was worth doing for these alone; none was visible from tests written in advance:

1. **Dangling-article debris** in `release.py`. Trimming trailing packaging left the
   article behind: `Invincible Iron Man by Gerry Duggan - The Complete Collection` →
   `…Gerry Duggan - The`. The trim is now followed by an article sweep, guarded on
   *whether a trim happened*, so a title genuinely ending in an article keeps it.
2. **Case 2 named the new folder after the source guess.** Now that Rule 2 walks a
   candidate list the guess and the matched key can differ, and when they do the matched
   key is right — it is the name the loose files themselves derive, and they are the ones
   being moved in. `Cruel Kingdom 2 001` guessed `Cruel Kingdom 2` and matched the loose
   `Cruel Kingdom v01 (2025).cbz`, so it created `/Cruel Kingdom 2/` and moved a file
   called `Cruel Kingdom v01` into it.
3. **`pick_destination_folder` tie-break** — see O14 above.

#### Observation, not fixed here

`normalize_name()` still derives its *matching key* by `VOLUME_PATTERN` subtraction, so it
eats real title words: `Giant Days` → `days`. Measured: 2,191 folders collapse to 2,174
normalised keys, and **5** keys cover more than one distinct series — `Human Target`/`The
Human Target`, `Marked`/`The Marked`, `PunchLine`/`Punchline`, `Rook`/`The Rook`,
`Six From Sirius`/`Six From Sirius 2`. Every one is an article or sequel collision; none
is caused by the word list, and all five pre-date this step. Left alone deliberately so
the CSV diff above has exactly one cause. It belongs with step 4 or 6.

---

### 10.6 The `kind` fix, and why step 6 became a union (step 6a)

#### What forced it

Step 6's first attempt switched `extract_series` alone and was reverted. The reason is in
§10.5's sibling: the folder `Edison Rex (01-16 + TPB Vol. 1-2)` went from 18 inert
`single` groups to **one `ready` group of 18 files that included both TPBs** — on
`/api/create`, which deletes the sources after merging. The cause is pre-existing and
subtle: `_VOL_NUM`'s `\s*` does not match `_`, so `is_volume('Edison_Rex_Vol._01_…')` is
**False** while the spaced form is True. The old `extract_series` could not group
underscore filenames at all, which is the only reason the hole stayed latent.

So the Builder needs a volume detector that survives underscores — which is exactly what
`parse_release` gives, since it normalises `_` to space before tokenising.

#### 6a — the `kind` classifier was not fit to be that detector yet

The loop that trims trailing packaging off the title set `kind` only for `KIND_WORDS`.
Packaging words never set it, so any collected edition **without a volume number after the
marker** parsed as `kind='issue'`: `Y - The Last Man Omnibus`, three `Doom Patrol …
Omnibus`, `A Dumbing Of Age … Complete`, `Batman - Gotham After Midnight - Collected`.

Fixed by adding `COLLECTION_WORDS`, a deliberate **subset** of `PACKAGING`. `digital`,
`webrip` and `scanlation` are excluded: they say where a file came from, and a digital
scan of issue 5 is still issue 5. They keep being trimmed from the title without setting
`kind`. A `kind == 'issue'` guard stops a `special`/`annual` already read off the tail
from being overwritten — mutation-tested, since the obvious test for it
(`Misty Special Collection`) passes **vacuously**: it cuts at `Special`, leaving
`head=['Misty']`, so the trim loop never runs. `Bone Parish Collection Annual` is the
name that actually reaches the guard.

**Containment, measured not asserted.** Across all **29,769** comics in the library,
`series`, `volume`, `issue`, `issue_range`, `year`, `subtitle` and `tags` are identical
before and after. **316** files move `issue → volume`; nothing moves in any other
direction. Nothing in production reads `.kind` (one test did), so the Organiser's CSV
cannot be touched. 82 tests green.

#### 6b — why it is a union and not a replacement

The obvious step 6 is `is_volume(n)` → `parse_release(n).kind == 'volume'`. Measuring the
two over 28,378 unique filenames says do not:

| | count | verdict |
|---|---|---|
| `kind` says volume, regex does not | 70 | parser right — `Volume 1` spelled out, `Edison_Rex_Vol._01`, `Book #001` |
| regex says volume, `kind` does not | **636** | **regex right** — and unfixable in the parser |

The 636 split cleanly in two, and neither half is a bug: **357** have the packaging inside
a `(tag group)` — `(Fan Made TPB)`, `(Graphic Novel)`, `(Book 1)` — which the parser strips
as tags and never inspects; **279** have the marker mid-title, and the parser is a
*prefix-consumer* by design, which is the whole reason `Giant Days` and `The Complete
Peanuts` survive. Making `kind` catch these would require carving from the middle, i.e.
re-introducing the exact defect §8.1 exists to remove.

Replacing the regex would therefore **reveal 636 collected editions to the merge UI**.
The union `is_volume(n) or kind == 'volume'` cannot reveal anything: a file can only
*leave* the visible set. That bounds the verification to one direction, and it is the safe
one — hiding a real issue is a nuisance, merging a TPB deletes files.

**Measured on a real scan** (with `extract_series` left untouched, so this is attributable):
groups 1,626 → 1,604, grouped files 2,033 → 2,009, **24 files hidden, 0 revealed**,
0 renames, 0 status changes. Edison Rex's two TPBs are among the 24, and that folder drops
back to 16 inert singles.

Shipped, and the prediction reproduced exactly against the committed baseline. Three
further checks on the shipped version, because "24 fewer files" alone does not prove the
*remaining* groups are unharmed:

- **Purely subtractive.** Every one of the 1,604 after-groups equals some before-group
  minus hidden files — 0 exceptions. This is the §9 non-negotiable invariant restated for
  the Builder: no two previously-distinct groups merged.
- **The counts reconcile.** 2,033 − 24 = 2,009 grouped, 3,718 + 24 = 3,742 invisible. No
  file went anywhere other than from the first set to the second.
- **`.comic_exclusions.md` byte-identical** (sha256 before/after), and the server boots
  and serves `GET /` → 200 with the new sibling import live. Of the 24, 21 are unambiguous collected editions (`March - Book
One/Two/Three`, `The Cloven`, `High Strangeness`, `I Hate Fairyland`, `Parker … Volume
Two`); **3 are debatable** — `Inferno Girl Red - Book Two 001/002/003`, where `Book Two` is
an arc name and `001` the issue number. Pre-existing `NUMBER_WORDS` behaviour, not
introduced here, and the failure direction is the safe one.

Splitting 6b from 6c matters for the same reason step 5 preceded step 4: `is_volume` and
`extract_series` both move files between groups, and changed together no diff has a single
cause.

#### 6c — the series switch, and the defect it exposed

Measured from the post-6b scan, so this change is isolated: **0 files vanished, 0
appeared**, grouped files unchanged at 2,009. Groups **1,604 → 1,530** as previously-split
runs joined up, with 901 renames across 41 regrouped folders. Edison Rex is now one
16-issue run with both TPBs excluded — 6b is what makes that safe.

**O19 — `ready` means "more than one file", and nothing more.** `scan_root()` sets
`status = 'ready'` for any group where `n > 1`; conditions A–E then demote some. There is
no check that the files carry *distinct ordinals*. Before 6c the noise left in the series
key — years, scan-group names — kept unrelated files in separate one-file groups, so this
never showed. Removing the noise merges the real runs and the accidents alike.

35 groups became actionable. Splitting them by whether `parse_release` can find an ordinal:

| | count | example |
|---|---|---|
| distinct ordinals — a real run | 20 | Edison Rex 001–016, Nancy in Hell 01–04 |
| **no ordinal on any file** | **15** | see below |

The 15 are not one problem but three, which is why there is no obvious single rule:

- **Duplicate scans of one comic** — merging would put the same content in twice:
  `Defenders - There Are No Rules`, `Leviathan`, `Gone`, `Somna`, `Midnite Show`,
  `Kill Me & Other Curiosities`, both `John Carpenter's …` pairs, `Bone - Happy Halloween`.
- **Unrelated comics sharing a title** — `Strange Adventures (2000)` with
  `Strange Adventures (DC 2022)`, `The Well (2022)` with `The Well (2025)`,
  `Space Bastards` with `Space Bastards - Special Delivery`.
- **Legitimate runs the parser cannot number** — `Into the Unbeing - Part One/Two`,
  `Shock - Ghosts of Knightgrave - Part One/Two/Three`, `Kaijumax Season Five/Six`.

Nothing merges without a click, so this is not live data loss. It matters because the UI
has *Select All* → *Create Selected CBZs* and a `ready` filter, so the bad recommendations
sit in the same bulk selection as the good ones. Any guard that demotes ordinal-less groups
would also demote the six legitimate ones, so the fix is a requirements call, not a defect
fix. **Settled and implemented in step 7 — see §10.7.**

> Measuring this needed two attempts. The first used the Builder's own
> `extract_zero_padded_issue()` and reported that **all 35** groups lacked ordinals,
> including Edison Rex 001–016. That helper cannot read `_` either — the same blind spot
> as `_VOL_NUM`, §10.6 above — so it was answering "unparseable", not "duplicate". This is
> the §10.3 failure again: a measurement is only as good as its instrument, and reusing a
> component that shares the bug under investigation guarantees a confident wrong number.

#### Deliberately not fixed: tome markers jammed against a dash

`Falka T01- Le Sang des Lupercales` and `India Dreams T4-There` fail `_VOL_ATTACHED`,
which requires end-of-string after the digits, so both parse `kind='issue'` and keep the
marker in the series. Fixing it means changing `_tokenise`/`_classify`, which changes
`series` strings and therefore the Organiser's matching keys and CSV — the uncontained
half of this work.

It was dropped from step 6 rather than deferred, because under a union it buys nothing:
`is_volume` already returns True for both (`_VOL_NUM`'s `t\.?\s*\d+` matches `T01`, and
the trailing `-` satisfies the not-alphanumeric lookahead). The union keeps that coverage.
Recorded as a known limitation of `series`, not a blocker for the Builder.

### 10.7 Step 7 — the three requirements calls

Step 7 was two mechanical defects and three questions only you could answer. The defects
are done; the answers are below, one implemented and two still to build.

#### O19 — a `review` status ✅ implemented

Of the three options (hard-block the merge, flag for review, leave it alone) the middle one
is the only one that survives the §10.6 breakdown: a hard block would refuse the six
legitimate runs, and leaving it alone keeps bad merges inside *Select All*. So ordinal-less
groups are **demoted to a new `review` status** — visible, filterable, still buildable one
at a time, but excluded from bulk selection.

Two ordering constraints made this harder than it looks, and both were found by measuring
rather than by reading:

1. **The demotion must run last.** Placed in `scan_root`'s status chain it fires *before*
   conditions A–E and converted three `temp_exclude`s and one `incomplete` into `review`.
   Those statuses carry specific signal — "still releasing this year", "missing issues" —
   and `review` is vaguer, so that was a promotion wearing a guard's clothes. It now runs
   as a final pass over `apply_auto_logic`, gated on `status in ('ready', 'auto_ready')`.
2. **`_has_distinct_ordinals` must not use the Builder's own issue helpers.**
   `extract_zero_padded_issue()` cannot see `_` as a separator, the exact blind spot that
   produced the wrong measurement in §10.6. It calls `parse_release` instead.

Shipped result, measured against the post-6c scan:

| status | 6c | after O19 |
|---|---|---|
| ready | 57 | **41** |
| review | 0 | **16** |
| auto_ready / incomplete / redundant / single / temp_exclude | — | unchanged |

All 16 came from `ready`; no status changed to anything but `review`. Group and file counts
are untouched (1,530 groups / 2,009 files), as they must be — this changes advice, not data.

The UI guard is the point of the whole exercise: `/api/create` **deletes the source files**,
so *Select All* skips `review` rows unless Review is the active filter. Selecting one by
hand still works, which keeps the six legitimate runs buildable.

> Three mutations were run against the new tests, because two tests earlier in this work
> turned out vacuous (§10.3, §10.5). Removing the status gate, the demotion loop, and the
> all-None early return each fail a *different* test. The third mutation initially
> **survived** — that early return only decides the one-file case, which nothing covered —
> so a test was added for it rather than leaving the branch unpinned.

#### `COMIC_EXTS` — unified to `.cbz`/`.cbr` ✅ implemented

The Organiser accepted `.zip` and `.rar`; the Builder never did. I initially framed
narrowing as a loss of function and was wrong: the source directory holds **52 `.cbz`,
43 `.cbr`, and zero of either extra extension**, while the only `.zip` anywhere near it is
a business ebook the old set would have happily parsed as a comic release. Not a wider net
for comics — a wider net for everything. 0 files dropped from the current corpus.

#### O16 — container gating, with franchise shelves added ✅ implemented

Answer: **exact series match only** for container-shaped folders. While scoping this I
found a gap in the settled §8.4 Q3 table — it buckets containers as publisher / anthology /
creator / event, and **franchise or character shelves fit none of them**:

| shelf | files |
|---|---|
| `Star Trek` | 209 |
| `Batman` | 160 |
| `Hellboy` | 309 |
| `Avengers` | 87 |

`Batman - Year One` is genuinely a Batman book, but so is half the DC line by name, and a
prefix rule would sweep in everything. Exact-match-only makes the shelf inert for auto-
filing without excluding it from the library.

**What "exact" had to mean.** Every match into a container was *already* exact —
`find_exact_match()` has no fuzzy path. Reading the rule as "exact match only" therefore
describes the existing behaviour and changes nothing. The rule only bites once you notice
that `parse_release()` offers **shortened** forms of a title as fallback candidates:
`Star Trek - Deviations - Evermore` also answers to `Star Trek`, and it is that second
candidate that reaches the shelf. So the gate is one distinction — a container accepts the
file's **own** series and refuses a shortened form of it — and `find_matches()` is the only
place that knows which candidate is which.

**Shape cannot classify; only a person can.** Counting distinct series per folder finds
containers and ordinary folders alike: `Lumberjanes` parses as 12 series, `Something is
Killing the Children` as 11, because their arcs parse apart. The list is therefore curated
— `.comic_containers.md` in the **library root**, not in this repo, because it describes a
library and the root is rebasable (O17). 122 folders classified: 10 publisher, 13
anthology, 57 franchise, 38 creator, 4 event.

Shape survives only as the fail-safe for shelves added *after* the list was written
(`UNCLASSIFIED_CONTAINER_SERIES = 20`), set high on purpose so it clears the real series
folders above. The curated entry is checked **first** — otherwise `Europe Comics
(Collection)` (350 series) would read as `unknown` and O6 publisher routing would stop.

**Measured cost, before shipping.** Gate on vs gate off over 118 real downloads against the
real library, both runs through the same `find_matches()`:

| | matched |
|---|---|
| before | 70 |
| after | 62 |

All 8 changes are franchise shelves losing a shortened-title match: 3 × `Star Trek`,
2 × `The Rocketeer`, 2 × `Grimm Fairy Tales`, 1 × `ThunderCats`. Zero publisher, anthology,
creator or event matches changed — **no download in the sample was filing into a creator or
event shelf**, so the harm the §8.4 Q3 table guards against was already not happening.

Two genuine misfiles the gate does **not** fix, because neither target is a container:
`Supernatural - Wayward Special 001` → `Supernatural (2025)` (4 files, one series) and
`Twilight Zone - Stories from the Fifth Dimension` → `The Twilight Zone` (5 files, one
series). A shortened title reaching a *single-series* folder is the same defect pointed the
other way. See O20 below — it is no longer open, but it was not closed by the gate.

Eight mutations of the gate, all killed — including "creator/event fail open", "the curated
list loses to the shape", and "a missing containers file fails closed", which would refuse
every destination in an unclassified library.

#### O20 — ask once, remember the answer ✅ implemented

O16 gates on the **destination's** shape, but the defect is in the **candidate**. That
mismatch bounds what any gate can do, in both directions:

- it refuses shortened titles into `Star Trek` even when they belong there — 8 of the 8
  measured losses above;
- it cannot refuse them into `Supernatural (2025)`, which holds one series and is not a
  container by any definition.

No rule over filenames separates these. `Star Trek - Deviations` and
`Supernatural - Wayward Special` are the same shape — *folder = series X, file = X - Y* —
and only what the books **are** tells them apart. So the tools stop guessing and ask.

**Provenance first.** `find_matches()` returns a fourth value and two new confidences.
`EXACT_SHORTENED` says the destination was reached through the fallback candidate;
`BLOCKED_CONTAINER` says a shelf was found and refused, and names it. Both were previously
collapsed into `EXACT` and `NONE`, and `Confidence` was computed and then explicitly
discarded on the way to the CSV as "internal use only" — which is why every row in the
report looked equally certain. It is now a column, alongside `Blocked Destination`.

Over the same 118 downloads this marks **13 rows**, and both still-open misfiles are among
them:

| confidence | rows | what it means |
|---|---|---|
| `EXACT_SHORTENED` | 5 | matched the long way round — includes both misfiles above |
| `BLOCKED_CONTAINER` | 8 | O16 refused a shelf — `Star Trek` ×3, `The Rocketeer` ×2, `Grimm Fairy Tales` ×2, `ThunderCats` |

**A decided row must stop asking.** The first cut offered each flagged row the single
decision it seemed to want — blocked rows *accept this shelf*, shortened matches *refuse
this folder*. Using it against the real library showed why that is wrong. Accepting
`Grimm Fairy Tales` moved its two rows from `BLOCKED_CONTAINER` to `EXACT_SHORTENED`, so
they stayed flagged, the count stayed at 13, and the button now read **"Never shorten into
Grimm Fairy Tales"** — inviting you to undo what you had just done, with nothing on screen
saying it had been done. `Confidence` recorded *how* a row matched but not *whether the
question was still open*, and those are different facts.

Hence two further confidences, `RULED_ACCEPT` and `RULED_REFUSE`, set when a saved rule made
the call rather than the container classification. A ruled row loses its border, leaves the
"Need Review" count, and shows a muted record of the decision in place of a warning. It
keeps both buttons — a decision made in the UI has to be reversible in the UI — with the one
in force marked active.

Both answers are now always offered, in the same order and the same place, rather than
whichever one the matcher happened to need. That is what removes the trap: the same folder
can no longer present opposite buttons depending on which way it was last decided.

Saving settles the row immediately rather than waiting for a rescan. Only the matcher can
change how a row *matched*, so the destination cell is left alone and the note says
"rescan to apply" — but the question is answered, and the count drops on the spot.

The buttons sit under the review note in the destination column, not in the actions cell.
That cell is the last column of a table about 3,800px wide, so a control there is off-screen
on any ordinary display — established by rendering the real page headlessly at 1700, 2600
and 3400px, at each of which the label was still sheared off. The note states the problem
and the button answers it, which also reads better.

`SERIES_KEY_MATCHES` exists because adding `RULED_ACCEPT` nearly broke two unrelated places
that ask "did this match a series key?" — one names a new folder after the matched series
rather than the parsed guess, the other counts matches for the summary. Each held its own
literal list. Missing either is silent: the run completes and quietly names folders wrongly.
One constant now, with a test asserting its membership.

**The answer is keyed on the folder, not the file.** A per-file rule expires the moment the
next issue is released with a different filename. Trusting the whole shelf is a bigger
commitment and was chosen deliberately over a narrower per-pair rule, which would have had
to be re-answered for every new spin-off.

Rules live in `.comic_matching_rules.md` in the library root — same place, format and
identity rules as `.comic_containers.md`, for the same reason (it describes a library, and
the root is rebasable). They **override** the container classification in both directions:
that file is a standing guess about a folder, this one is a decision made while looking at
the books. `Refuse` still admits the folder's own series, or saying "not this one" would
orphan the folder entirely.

**Failure modes, chosen not inherited.** A missing rules file changes nothing. A mistyped
section heading is treated as `Refuse`, matching the containers file's stance — wrongly
refusing costs a folder you file by hand, wrongly accepting costs a misfiled book you may
never notice. The folder name arrives in a POST body and becomes a **line** in a file whose
every line is meaningful, so it is rejected if it contains a control character (either
newline would let it write its own `## ` heading or `- ` bullets) or a slash.

Writing is a rewrite, not an append: reversing an earlier answer must *replace* it, or the
folder is listed twice with opposite meanings and which one wins is an accident of dict
ordering. The prose under each heading survives, because the file is meant to be read.

Eleven mutations of the writer, all killed — including "an earlier ruling is left in place",
"a mistyped decision is not validated", "control characters pass through", and "a missing
section is silently skipped", which would have produced a button that appears to work and
does nothing.

**Asymmetry found and left alone.** The subfolder path (`find_folder_match()`) matches
folder-to-folder on the normalised name only — no shortened candidates, so O16 never applies
to it and neither does O6 publisher routing. Not a defect for the files in hand; recorded
because it means the two intake paths do not match by the same rules.

#### O21 — a file must be planned once ✅ fixed, found by a live run

Found by accident: a real `--execute` run created an **empty** `/The Nameless Kingdom/`
beside a populated `/The Nameless Kingdom -/`, and reported the only 3 failures of 131
moves as "Source not found".

The CSV is a move plan and `plan_moves()` walks it row by row, trusting that no two rows
name the same file. STEP 1 emits one row per source subfolder and records what it handled
in `processed_files`; STEP 2 emits one row per remaining file and skips anything already
in that set. STEP 1 stored **bare filenames**; STEP 2 looks files up by **path relative to
the source directory**. The two forms are identical for a loose file, so the check appeared
to work everywhere except the single case it was written for — every file inside a subfolder
was planned twice, to two different destinations. Whichever move ran first won; the other
failed, leaving an empty folder under the losing name.

**The trap in fixing it.** The duplicate was load-bearing. `scan_source_subfolders()` listed
files with `rglob`, so a *nested* file entered the plan as a bare name, and the folder op
flattens by joining that name onto the subfolder — a path that does not exist. Nested files
were therefore never moved by the folder row at all; they arrived only via the duplicate
standalone row. De-duplicating by suppressing that row would have converted a double-move
into no move: silent data loss, and a strictly worse bug than the one being fixed.

So the fix is two coordinated changes, not one. `rglob` → `glob`, because the folder row can
only honestly promise its direct children; and the `processed_files` key gains the folder
prefix, so both steps identify a file the same way. Nested files now fall through to STEP 2
and are moved individually, which is the path that already worked.

`tests/test_no_duplicate_plans.py` drives the generator end to end against temp directories
and asserts the invariant directly — every source file appears in exactly one row, and every
row names a file that exists. Three mutations, all killed: restoring the bare-name key
reproduces the exact Nameless Kingdom duplication, restoring `rglob` makes the plan name a
path that is not there, and the nested-file test is what stops the naive fix.

**Same confusion, third site.** The block that fills `Left Folder` for a file-level row searched
`subfolders` for the file by bare name, so it never matched either — every such row shipped with
an empty `Left Folder`. It now reads the parent from the path. This also covers a case the search
could not: a folder with no extractable series name is never scanned as a subfolder at all, so its
files reach STEP 2 with a parent that a `subfolders` lookup would deny they have.

**Known edge, not fixed.** STEP 2 cannot see the folders STEP 1 is about to create, so a nested
file is routed against the library as it exists now and lands at the root rather than beside the
siblings its folder op is creating a home for. Pre-existing and not a regression — before O21 that
same row was what moved the file, and it went to the same place; only the duplicate failed move is
gone. Left alone because no nested source folder has yet appeared in a real run.

**Second defect, same folder.** `extract_folder_series_name()` removes the volume keyword and
then a trailing issue number, which takes both ends of a range and leaves the dash that joined
them: `X-Men Vol 1 - 5` → `X-Men -`. That is what named `/The Nameless Kingdom -/`, and it is
general to every `Vol. N - M` folder. Stripping a dangling trailing separator is anchored to
the end of the string, so `Spider-Man` and `A-Force` are untouched — both are pinned.

#### O17 — rebasable root ✅ implemented, and it was a live defect

Scoped as "replace a constant with a flag". It was not. Both folders are already pickable
in the UI — `REQUIREMENTS FR:132`, *"Folder picker modals for source and destination
paths"* — and those pickers reached `matching_analysis_generator.py` via `--src`/`--dest`
and **stopped there**. `serve_v2.py` launched `comic_mover.py` with neither, so the mover
fell back to its own constants at `comic_mover.py:26-28`. Two silent failures:

| you change | the scan uses | the move uses |
|---|---|---|
| destination | the library you picked | **the hardcoded one** |
| source | the CSV the generator just wrote there | **a stale CSV, or none** |

Picking a different destination therefore analysed library B and wrote into library A, with
the CSV's `Has Existing Folder: YES` describing a folder the files never reached. The
subprocess boundary is what hid it: nothing fails when an argument is simply never passed.

Fixed in three places, because a flag on the mover alone would have changed nothing:
`comic_mover.py` gained `--src`/`--dest` (setting `SRC_DIR`, `DEST_DIR` and the derived
`CSV_FILE` before any path is built), `serve_v2.py` now sends both on dry-run and execute,
and `comic_organizer_v2.html` sends the picked pair with those two calls — it previously
sent them only with `/api/scan`.

**Confinement was re-aimed, not loosened.** `resolve_under_dest` reads `DEST_DIR` at call
time, so it now confines to whichever library is selected. `TestConfinementFollowsTheNewRoot`
pins that directly, including the case that matters most: from a rebased root, naming the
*original* library must still be refused. A guard that kept confining to the startup root
would read as protection while permitting every write into the newly-selected library to
escape.

> I initially proposed making the root a server-startup flag with the UI picker read-only,
> on the grounds that a caller-chosen write root defeats confinement — the reasoning behind
> the Builder's `ALLOWED_ROOT`. That was wrong here, and the correction was yours: the two
> tools have different threat models. The Builder is a fixed single-library tool whose HTML
> has no picker; the Organiser is a two-pane source→destination mover whose pickers are a
> stated requirement. The caller *is* the user, at loopback (`serve_v2.py:345`), so the
> realistic fault is a typo — which is exactly what `resolve_under_dest` still catches.
> Reading the requirements doc first would have saved a wrong recommendation.

15 tests. Three mutations, each caught: dropping `--dest` in the mover, dropping the folder
arguments in the server command, and weakening the blank-string fallback so `""` would reach
the mover and resolve to the process cwd. The first reproduces the original bug exactly —
CSV read from the fixture, files targeted at `/mnt/extramedia/Comics`.

`mover_cmd()` was extracted to module level in `serve_v2.py` purely so this is testable: a
command assembled inline in a request handler is reachable only by booting a server and
parsing streamed output, and the defect lived in that command.

**The stale-CSV window ✅ closed.** The fix above makes scan and move agree within one
action. It did not cover two: scan library A → change the picker to B → move without
rescanning. The CSV still described A's layout while the mover joined those bare names onto
B, silently.

The generator now writes a `Scanned Destination` column and the mover refuses before
planning anything. A column rather than a sidecar file because the stamp has to travel with
the CSV — a separate file can be left behind by a copy, which is the same separation the
stamp exists to detect. Invisible in the UI: `comic_organizer_v2.html` reads fields by name
(`:1153`) and its table headers are hardcoded (`:637`), so an added column is ignored.

**An absent stamp is not an error.** Every CSV already on disk predates the column; failing
on those would reject real work for no safety gain, since there is nothing to compare. Only
a present-and-different stamp refuses. Two mutations confirm both halves: removing the check
fails 2 tests, and removing the absent-stamp fallback fails 4 — the latter being the
regression that would have broken your existing CSV.

This enforces `REQUIREMENTS:174` *"single source/destination pair per session"* mechanically
instead of trusting it.

---

### 10.8 `library_duplicates.py` — the same rule turned on the library itself

The Organiser warns when an incoming download already exists in the destination. Asked for
the same question across the whole library, the answer is `library_duplicates.py`: group all
29,516 comic files by what `parse_release()` makes of them, and report every key holding
more than one file. It writes `LIBRARY_DUPLICATES.md` and **moves and deletes nothing**.

The interesting part is not the grouping — it is that the grouping is far too generous to
act on. `parse_release()` discards information, so two files land on one key precisely when
the thing that told them apart is the thing it dropped. The first run listed 1,690 groups as
likely duplicates; spot-checking found six *different* Harley Quinn volume 2s in one of them,
because subtitles are discarded outright.

So a group is presented as a likely duplicate only if it survives three checks, each reading
back something the parser threw away:

| check | the case it was written for |
|---|---|
| filename signature, packaging stripped | `Harley Quinn v02 - Keepsake` vs `- Power Outage` |
| variant / cover-only tag | 1 MB `New Avengers 001 (Cover ONLY)` vs the 42 MB issue |
| volume claimed by the parent folders | `Terra Obscura Volume 1/#003` vs `Volume 2/#003` |

Each check earned two refinements from real data rather than from reasoning:

- The signature strips format words and leading zeros, but `v01` is a *single token* — so
  the two steps never met and `Omnibus v01` stayed unequal to `Vol 1`. 31 genuine duplicate
  groups were sitting in the review pile because of it.
- A folder naming a *range* — `Shakara (v01-v02)` — holds both books and so identifies
  neither; read naively it split real duplicates. Only a folder naming exactly one volume
  speaks for the file inside it.
- An **absent** volume folder is silence, not a claim of "no volume". One copy of
  `The Authority v1 #10` is filed under a `v1 (1999)` folder and one is not; comparing the
  empty set against `{1}` demoted a real duplicate. Disagreement now requires evidence on
  both sides.

Measured on the live library, a 14-group random sample of the likely list went from 8/12
correct to 13/14 — inside the one-in-six false-positive rate you accepted. The residue is
the case the report names in its own prose: a heading with no `v` and no `#` means the
parser found a series name and nothing else, so `Strange Adventures (2000)` and
`Strange Adventures (DC 2022)` share a group. The years in the filenames are the giveaway.

**Sizes are shown, never used to decide** — your reasoning, and it holds: two rips by
different packers are never the same length, so size cannot prove two files *differ*. The
converse is sound though, and free, so a group whose copies are byte-identical in length
says `— identical size` in its heading. That is one file filed in two folders rather than a
judgement call, and it covers 1,048 of the 1,398 likely groups.

The asymmetry throughout is deliberate: a true duplicate wrongly demoted to *check these by
hand* costs a minute of reading, a false duplicate left in the likely pile costs a book.
10 tests; four mutations, each killed by exactly one test — removing the `v01` split, the
variant check, the range-folder guard, and the empty-set discard.

### 10.9 O23 — the same rule in the pipeline, as a question rather than a report

The report above is read once, later. The live pipeline has to ask *before* a file moves, and
about one folder rather than the whole library — your scope, "only dest.folder". Both halves
share `duplicates.py`; nothing is re-implemented.

The chain is four hops and every one of them was a place to get it wrong:

| hop | what it does | the trap |
|---|---|---|
| generator | indexes the destination folder, writes `Existing Copies`, `Existing Copy Sizes` and `Existing Copy Pages` | a blank folder name resolves to the library root, which would flag everything |
| UI | names the existing file, both sizes and both page counts; two opt-in buttons | telling you a copy exists without naming it is the version you rejected |
| server | writes the decisions to a temp JSON, passes `--duplicate-decisions` | — |
| mover | skips, files anyway, or **refuses to execute** | `--no-confirm` means a warning is printed to nobody |

**The key had to match on both sides.** The mover plans a file row's move from `Left Panel
File`, which can carry a source subfolder; the CSV column names the file bare. Keyed on the
bare name the skip silently never fires *and* the gate keeps asking about a file no answer
can settle. A folder row is the opposite case — it moves many files and only some collided,
so those are named one by one, under their subfolder.

**Doing nothing is safe, and doing nothing is not an answer.** Neither button is preselected.
An undecided flag does not stop a dry run — you cannot decide about what you cannot see — but
`--execute` exits non-zero and moves nothing. Deselecting a row cannot express this: an empty
selection means *all* rows, so the decision needed its own channel.

On the live batch: 116 rows, 3 collisions found (`Blood Type v01`, `Free Planet v02`,
`Sleeper Book 01`), 0 same-key pairs rejected by the demotion checks — so the extra rules cost
nothing here while still holding back the Harley Quinn and `Book Two` classes.

**Page counts, for the same reason sizes are shown and not used.** Two packers disagree about
bytes but rarely about how many pages a book has, so the count is the more honest of the two
numbers — and like the size it is evidence for you, never an input to the rule. It earned its
place on the first run: of the three pairs, `Blood Type` reads 101p against 123p and
`Free Planet` 159p against 119p, so those are different editions rather than the same file
twice, which the sizes alone only hinted at.

Two distinctions the display depends on:

- **`0p` is an answer; blank is not.** Zero means the archive was read and holds no images,
  and the UI colours it as an alarm. The first file this ever ran against was
  `Blood Type v01 (2026) … .cbr` — 238 MB of `429 Too Many Requests` HTML with a comic's
  extension. Blank means the archive could not be read, and claims nothing.
- **The extension does not decide the format, and `unrar` cannot make that call.** `.cbr`
  files are routinely zips, so `zipfile.is_zipfile()` goes first and the RAR signature is
  checked by hand after. That check is the answer, not a shortcut to one: handed something
  that is not a RAR at all, `unrar lb` exits 0 and prints nothing, which would make
  "holds no pages" and "could not read it" the same result.

**The tick boxes.** Every answer button carries `☑`/`☐` ahead of its label, on the duplicate
buttons and the rule buttons alike. Colour change alone read as decoration; an empty box
beside a ticked one says the thing a single coloured button cannot — that there was a choice,
and which way it went. Same width either way, so a row does not shift when clicked.

23 tests; eleven mutations, all killed. Six on the decision (the bare-name key, `keep` not
counting as an answer, skip/keep swapped, warning instead of refusing, the demotion checks
dropped, the blank-folder guard removed) and five on the counting (the signature check
removed, a failed `unrar` counted as zero, every archive member counted rather than the
images, the two halves of the column swapped, unreadable printed as `Nonep`).

**What the first library sweep actually found.** Run across all 29,515 archives (176 minutes),
it flagged 233 files — and 159 of those were the counter's own fault. Every KissManga rip
names its pages `001 - proxy..jpe`, and `.jpe` was missing from `PAGE_EXTS`, so whole manga
series were reported as holding no images. An incomplete allowlist does not under-report
quietly; it accuses a good comic of not being one. A second defect surfaced with it: a file
whose first four bytes say zip but which will not open was being called "holds no pages" when
the truth is "could not be opened" — the exact conflation the RAR branch already guarded
against, missing from the zip branch. Both are fixed and pinned by tests.

Reading that report back caught a third defect of the same shape, and a wrong label. The
counter knew only zip and rar, so a `.cbr` holding 7z or tar fell through to zero — eight
ordinary comics of 234, 168, 161, 138, 137, 50, 42 and 20 pages were listed as junk. Twice
now the allowlist has been the bug, once for page extensions and once for containers, so
`_read_page_count` now names 7z and tar as readable, and ACE as an archive it cannot read
(None, not zero — no reader is installed, and silence is the honest answer).

The wrong label was mine: 19 files were described as "all zero bytes" when they are nothing
of the kind. Each is full length with one contiguous NUL run at the *front* and real data
after it — 63% to 99.99% NUL, the survivor in one case being 187 MB. The archive header lives
at byte 0, so they are unreadable regardless, but "all zero bytes" was not true of a single
one of them.

That left 66 genuinely broken files, 5.6 GB. Twenty-three have since left that list — nine
repacked and readable, fourteen quarantined as error pages — leaving **51 files, 3.7 GB** in
`LIBRARY_BROKEN_FILES.md`. None of this was visible to any other part of the pipeline: every
one of these files has a plausible name and a plausible size.

### 10.10 Two faults that both read as "broken", and are not the same fault

`repack_comics.py` exists because unrelated problems were filed under one label.

**The container.** Eight comics were 7z or tar wearing a `.cbr`/`.cbz` name, and one `.cbz`
held five whole RAR comics instead of pages. Extracted and rewritten as `ZIP_STORED`, all
nine open in QComicBook — confirmed by the user. **No page was re-encoded**, including 443
WebP pages. The working theory going in was that QComicBook objected to WebP; it did not.
The container was the entire objection, and the conversion path (`--convert-nonjpeg`, JPEG
q95 4:4:4) was built, kept, and never used.

**The order.** `makecbz.py` merged loose issues into volumes, and had two independent
ordering defects, both reproduced empirically rather than reasoned about:

* `temp_extract_{i}_` was not zero-padded. `'0'` is 48 and `'_'` is 95, so `temp_extract_10_`
  sorts *before* `temp_extract_1_`. A volume is fine to ten issues and scrambled from
  **eleven** — not ten, which was the first guess and was wrong.
* `zip -r out.zip .` stores entries in filesystem readdir order. Measured on twelve issues:
  stored as 7, 11, 8, 3, 1, 9, 10, 6, 2, 4, 12, 5. Latent, because most readers re-sort by
  name — which is exactly what made the first defect visible and this one invisible.

`temp_extract_` inside a `.cbz` is an unambiguous fingerprint of the tool, and the folder name
still carries the issue index, so **reading order is rebuildable from inside the volume**
without the original issue files. Of 8,439 `.cbz` scanned, 143 were built by `makecbz.py` and
11 had eleven or more issues. All 11 repaired; every page verified byte-identical to the
quarantined original, stored order equal to sorted order.

Both defects are now fixed in `makecbz.py` itself (padded index, `zip -@` fed a sorted list),
so either tool produces correct volumes.

**One thing was lost.** The repair pass dropped 74 per-issue `ComicInfo.xml` files:
`pages_in()` kept images and nothing else. The tool now carries `ComicInfo.xml` through
(`extras_in()`, never re-encoded even under `--convert-nonjpeg`) while still dropping
`Thumbs.db`, `.DS_Store` and `.sfv`. The user's call on the 11 already done was to leave them:
these were *nested* metadata inside merged volumes, which QComicBook ignores entirely and
Komga/Kavita only read at the archive root, so they were already inert. The originals remain
in quarantine.

**A test wrote into production.** `setUp` patched `LIBRARY`, `QUARANTINE`, `STAGING` and
`TEMP_ROOT` but not `LOG_DIR`, so the first test to go through `main()` appended two `/tmp`
fixtures to the repo's real run history — and the next report rendered them as real comics.
All six log and report paths are now patched, and
`test_a_test_run_never_touches_the_real_run_history` asserts it directly rather than trusting
the fixture list to stay complete.

One of those five mutations survived its first run and is the reason the signature check is
tested the way it is. Removing the check changed no result, because this `unrar` build happens to return
zero-with-no-output for anything that is not a RAR — the test was passing through unrar's
behaviour instead of pinning ours. It now asserts that a non-archive is settled *without
unrar being asked at all*, which is the actual guarantee.

### 10.11 Asking the wrong tool, and believing its shrug

Two further faults were found in `list_members`, and they share one shape: **a tool's
inability to read a file was recorded as a fact about the file.** Between them they had
condemned 16 comics that were never broken. Neither was found by a test — both surfaced
because the user contradicted the report.

**`is_zipfile` was asked before byte 0.** `zipfile.is_zipfile()` does not read the start of
a file; it scans *backwards from the end* for a central directory, because a zip may
legitimately carry a prefix. So any archive holding a nested `.zip` answers yes and is then
read as that inner zip. `Luis Royo - Subversive Beauty & Portfolio.cbr` is a RAR of 97 JPEGs
that also carries a small zip holding a DOS utility; the counter listed `PICCHECK.exe`,
`INI2REG.exe` and three friends, found no images, and filed a 97-page art book as empty.
Both `unrar` and `unar` read it without complaint — it was never damaged.

The fix is ordering, not logic: magic bytes at byte 0 decide the format, and `is_zipfile`
is consulted only after every signature has failed, where its backwards scan is the right
tool for the one case it is meant for. `tests/test_page_count.py` pins both directions —
a RAR-carrying-a-zip must not be read as the zip, and a zip behind a stub must still be
found. The old ordering was confirmed to fail those tests before the fix was written.

**`unrar` was the only RAR reader.** The user reported MComix opening a file this report
called unreadable. MComix uses `unar`, and on damaged RARs the two disagree enormously:
for `Trigan Empire v02`, `unrar` refuses outright and `7z` lists 189 members while
extracting **zero** decodable images, but `unar` extracts **188 real JPEGs**. Re-testing all
21 "could not be read" files with `unar`, decoding every page through Pillow rather than
trusting the listing, recovered **641 pages across 15 files** — one of which, Metal Hurlant
v02, is completely intact and had simply been refused.

Two details make the diagnosis rather than just the count:

* **Fourteen of the fifteen are missing exactly one page, always the last.** That is a
  download cut short at the end, not corruption — and it explains why so much survives.
* Running the same `unar` pass over the *other* section, the 19 NUL-damaged files, rescued
  **nothing**. Confirmatory rather than disappointing: a tolerant reader still needs a
  header, and in those files byte 0 is gone. Damage at the tail is recoverable; damage at
  the head is not. The two sections of that report are now known to be genuinely different
  failures rather than two labels for "will not open".

The `unar` fallback is **not yet in `list_members`** — it changes how every RAR in a
29,515-file library is counted, which deserves a deliberate decision. Until it lands, any
re-run of the sweep will rediscover these 15 as broken.

`repack_comics.py` cannot rescue them either, and the reason is worth stating because it
was nearly missed: `extract()` shells out to `unrar x`, which fails on exactly the files
that are on this list. Worse, verification compares the rebuilt page count against the
source count — and for a rescue the source count is unreadable by definition. A rescue mode
therefore has to relax the one check that guarantees no page is silently dropped, so it must
report what was lost per file (*"188 of 189, last page lost"*) rather than quietly passing.
That is a different contract from a repack, not a flag on the same one.

**The pattern worth keeping.** Three rounds of false alarms have now been retracted from
`LIBRARY_BROKEN_FILES.md` — the `.jpe` extension, the 7z/tar/ACE containers, and these two
— and every correction moved files *out* of the list. The report total fell from 5.6 GB
across 66 files to 0.9 GB across 31 without a single file being repaired. A negative result
from a parser is evidence about the parser first, and only then about the data.

### 10.12 The same mistake, made by me, in the opposite direction

Rescue mode shipped and ran. Nine of the fifteen files came out as predicted: the ACE pair
whole, seven truncated downloads each one page short. The remaining seven were reported as
"lost 1 of 3", and that number was wrong in a way the previous section should have caught.

A lister stops at the first damage and reports what it reached. `lsar` saying "3 pages"
means it read three before it stopped — not that the comic had three. §10.11 is entirely
about not treating a tool's limit as a fact about the file, and I then computed
`claimed - recovered` as the loss, which measures the lister's reach and nothing else. The
check the rescue was built around — *never lose a page silently* — was reporting a
confident number in place of an honest unknown.

What separates the two shapes is not the listing but what follows the damage:

* **Truncated** — ends in real bytes. The last page was cut mid-write; about a megabyte of
  it sits past the archive's last indexed member. Everything before is a whole comic.
* **Overwritten** — ends in *megabytes of NUL*. The same storage damage as the 25 files
  that hold nothing, differing only in where the zeros landed. What still reads is whatever
  sat before them, and how much is missing is unknowable, because the only thing that could
  count the rest is reading zeros.

The split is absolute: truncated files end in under a dozen NUL bytes (a zip's
end-of-central-directory contributes a few structurally), overwritten ones in 1.1 MB to
26 MB. Nothing between. `overwritten_bytes()` measures it by walking backwards from EOF, and
`do_rescue()` refuses on that measurement rather than on a list, so re-adding a file by hand
does not defeat it. `--salvage-fragments` overrides, and even then reports `pages_lost` as
`None`.

The cost of finding out late: `Anna Mercury 2 001` was rescued before the check existed,
putting a 2-page `.cbz` into the library under a full issue's name — its surviving pages are
numbered 014 and 015 of roughly 32, so it was missing the front of the comic as well as the
back. That is worse than the broken original, which at least failed openly. It has been
reverted. **Decision: the seven are re-downloaded, not salvaged.**

Pinned by tests in `tests/test_repack.py`, including the one that matters most — that a
genuinely truncated file is *not* flagged, since a false positive here sends a recoverable
comic to the re-download list.

The lesson is narrower than §10.11's and worth stating separately: knowing that a tool's
silence is not evidence does not protect you from believing its *numbers*. A partial result
is a limit reported as a measurement, and it looks exactly like a measurement.

**And then the check itself turned out to be too narrow.** The `unar`-fallback sweep
(§10.13) walked all 20,569 RARs and turned up nine `unrar` refuses. Eight end in megabytes
of NUL. The ninth, `Doom Patrol 04.cbr`, ends in **one** zero byte — and is a fragment
anyway: 22.5 MB of file, of which 7z can account for 1.6 MB. The other 20.9 MB is real
bytes no reader can reach. It would have passed the NUL check and been rescued into a
2-page `.cbz` wearing a full issue's name, which is precisely the outcome the NUL check was
written to prevent.

`overwritten_bytes()` asked what the damage is *made of*. The question that decides the
outcome is what share of the file the lister never reached, and zeros are only one way to
fail it. `unreached_bytes()` reads 7z's `Tail Size`; `is_fragment()` refuses on either
signal. The gap is as clean as the first one: the seven genuinely truncated files leave
0%–18.6% unaccounted for, every fragment leaves 39.7% or more, so the threshold is 30%.
Checked against all sixteen real files — zero truncated files wrongly refused, zero
fragments wrongly allowed.

Worth noticing that the narrow check was written from seven examples and was correct on all
seven. It took a sweep of the whole library to produce the eighth shape. A discriminator
validated only on the cases that motivated it has been fitted, not tested.

### 10.13 The fallback that would have made the counter worse

`list_members()` asks `unrar lb` and gives up when it exits non-zero. `unar` reads archives
`unrar` refuses — that is the whole reason rescue mode works — so adding it as a fallback
looks like free accuracy. The change is one line. It also re-reads a 29,515-file library, so
it was validated before landing rather than after.

The sweep (`/tmp/validate_unar_fallback.py`, read-only, ~3 h) checked both directions,
because a fallback can fail two ways. Exhaustively: every RAR `unrar` refuses, to size the
benefit. By sample: 400 RARs `unrar` reads happily, asking `lsar` the same question, because
if the two tools disagree where *both* answer then the fallback does not fill blanks, it
overwrites counts that were already fine — a far larger change than it appears.

| | |
|---|---|
| RARs walked | 20,569 |
| `unrar` refuses | 9 |
| of those, `lsar` can count | 9 — 37 pages |
| successes sampled | 400 |
| **disagreements** | **0** |

The control sample is clean, so the fallback is safe in the sense it was tested for. It was
still rejected, on what the nine files turned out to be: **every one is a fragment**, and
all nine are already on the re-download list. The "37 pages" is not 37 pages recovered — it
is how far `lsar` got before hitting the damage in nine comics that hold nothing usable.

So the fallback's entire measurable effect on this library would be to convert nine files
that currently read as *unreadable* into nine files reporting small, confident, wrong page
counts. Unreadable is the correct answer for all nine. This is §10.12's fault re-introduced
at the counter instead of at the rescue, and it would be harder to see there, because a
number that looks plausible does not announce itself the way a failure does.

**Decision: `list_members()` is left alone.** The sweep paid for itself anyway — it is what
found `Doom Patrol 04` and the hole in the fragment check.

The general point: "it only adds data where we had none" is a claim about the mechanism, not
about the data. Here the mechanism was sound and the change was still wrong, and no amount
of reasoning about `unar`'s tolerance would have shown that. Only looking at the nine files
did.

### 10.14 A block of NUL bytes is a valid empty tar

The Phase 2 sweep finished — 29,487 archives, 176 minutes — and reported **16 tar containers
holding 0 pages**, under a heading that reads *repack as zip*. Sixteen files, three-tenths of
a gigabyte, not one page between them. A tar-wrapped comic is unusual but real; sixteen
tar-wrapped comics that are all empty is not a library, it is a detector talking to itself.

`detect_container()` finished with:

```python
if tarfile.is_tarfile(path):
    return 'tar'
```

A tar archive legitimately *ends* in two 512-byte blocks of NUL. A file that is nothing but
NULs therefore satisfies every structural test `is_tarfile()` makes: it is a structurally
valid tar containing no members. All 16 are the NUL-headed damaged group already itemised in
`LIBRARY_BROKEN_FILES.md` and already on the re-download list — `X men 2099 #24.cbr` opens
with 4 MB of zeros, `Robotech 022` is 22 MB of them end to end.

Had the report been acted on, the repack would have read 16 archives, found 0 pages in each,
and written 16 empty `.cbz` files wearing full issue names — over the top of the originals'
place in the library, and with nothing in the resulting file to say what had happened.

The fix asks the format for contents instead of for a header:

```python
def tar_has_members(path: Path) -> bool:
    try:
        with tarfile.open(path) as tar:
            return tar.next() is not None
    except (tarfile.TarError, OSError):
        return False
```

`TarError` has to be caught in the helper: `detect_container()` guards only `OSError`, and
`tarfile.ReadError` is not one.

Recovery was cheap because the bug is one-directional. It can only *invent* tars, never hide
another format, so every other line in the 6.9 MB scratch file is unaffected — re-inspecting
the 16 files, patching their lines, and re-rendering took seconds against a three-hour
re-walk. All 16 now classify `not-an-archive`, which is the true answer: no archive format is
present in them at all. The defect table's first row goes 16 → **0**, and the whole of Phase 2
is now 16 nested archives and nothing else.

**This is the fourth time in this codebase that a stdlib or CLI detector was believed without
being asked for contents.** `zipfile.is_zipfile()` scans backwards from EOF and so mislabels
an archive that merely *contains* a `.zip` (§10.11). `unrar` as the sole RAR reader called
files unreadable that `7z` opens (§10.11 again). A lister's page count was read as the book's
page count when the lister had stopped at the damage (§10.12). And now `is_tarfile()` on a
file of zeros.

The shape is identical every time: **a format test answers "could this be parsed as X", not
"is this an X".** On a healthy library the two coincide, which is why the fault keeps landing
— it is invisible until the input is damaged, and this library's damaged files are precisely
the ones these tools exist to find. Three new tests pin it, including one asserting a genuine
single-member tar is still detected, because the tempting over-correction is to drop tar
support altogether and call the false positive fixed.

**The same trap was live in `list_members()`, which is the part that matters.**
The sweep is a diagnostic; the counter is what the Organiser shows and what `repack_comics.py`
trusts. There, a NUL-headed file reached `tarfile.is_tarfile()` by the same route, opened as
an empty tar, and returned `[]` — so `page_count()` said **0**. Zero is not a neutral answer
in this codebase. It is a claim, reserved for the 238 MB HTML error page saved with a `.cbr`
name: *we looked, and there is provably nothing here*. Sixteen damaged comics were making
that claim about themselves.

Fixing it by requiring tar members would not have been enough — the file would simply have
fallen through to the same `return []`. The honest test is the header itself:

```python
if head and not any(head):
    return None
```

No format this function looks for begins with a run of zeros where its signature belongs, so
a header of nothing is damage and not content. Placed after the magic-byte checks and before
the tar test, for the same ordering reason as everything else in that function.

Checked against the library before landing, because a wrong answer here costs page counts
everywhere: 29,487 head reads, 17 files open with 14 NUL bytes, and **none of them counts a
single page today**. The change can therefore take nothing away.

The seventeenth is the interesting one. `Legends of the Dark Knight 075.cbz` is 6 MB with the
first 4,163,560 of them zeroed — and a zip keeps its directory at the *end*, which survived.
It lists 28 pages. Five of them still read; the other 23 are inside the zeroed region. It was
never on any broken-file list, because `0 pages` had filed it as junk rather than as a loss,
and nothing about that answer invited a second look. **A wrong answer that looks like a
category rather than an error does not get re-examined** — which is the practical cost of
letting "empty" and "unreadable" share a value, and the reason the distinction was written
into this function in the first place.

---

## Appendix — outstanding items not scheduled

- ~~`Heartthrob Season 3 001` → `Heartthrob Season`; you want `Heartthrob`.~~ **Done.**
  It now routes to the real `Heartthrob (2016)` folder where live matched nothing; landed
  with step 5 and visible in the CSV diff as one of the three changed decisions (§10.5).
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
