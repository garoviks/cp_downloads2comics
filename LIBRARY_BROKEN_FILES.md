# Damaged or non-comic files in the library

Found by counting the images inside all 29,515 archives.

**Three rounds of false alarms have been removed from this list, all the same
shape:** a tool was asked a question it could not answer, and its shrug was
recorded as a verdict against the file.

1. The `.jpe` page extension — 159 KissManga files, pages the counter did not
   recognise as pages.
2. The 7z, tar and ACE containers — formats the counter could not name, read as
   files holding nothing.
3. `is_zipfile` asked before byte 0, `unrar` asked as the only RAR reader, and a
   page count believed from a lister that had stopped at the damage —
   16 files, detailed below.

Since the first version of this report, 37 of the 66 files listed have left it:
nine were repacked and are now readable, fourteen were error pages and have been
moved out of the library, four were deleted by the user, two — `Luis Royo -
Subversive Beauty` and `Metal Hurlant v02` — turned out never to have been
damaged at all, two were intact ACE archives, and seven were truncated downloads
now rescued and short one page each.

One correction ran the other way, and it is the only one that has. Seven files
this report called "missing their last page" are in fact **overwritten**, holding
a fragment of the comic and megabytes of zeros. The number I read them by came
from a lister that had stopped at the damage, and I took how far it got for how
much was there. That section is rewritten below.

Every other correction moved files *out* of this list, and not one of them came
from a test — each came from someone noticing the report was wrong. Treat a row
here as a lead, not a conviction.

## 9 were never broken, and have been repacked — see `LIBRARY_REPACK_REPORT.md`

Eight were ordinary comics in the wrong container (7z or tar wearing a `.cbr`
or `.cbz` name); the ninth, `Patience! Conviction! Revenge!`, was a zip holding
five RAR issues rather than pages. The old counter knew only zip and rar, so it
called all nine junk.

They now exist as plain stored zips that QComicBook opens — confirmed by the
user on all nine. No page was re-encoded, including the 443 WebP pages: the
container was the entire objection, not the image format. The originals are in
`/mnt/extramedia/_quarantine/`.

## 14 were `429 Too Many Requests` HTML — see `LIBRARY_REDOWNLOAD.md`

1651 MB of error pages carrying comic filenames. Moved to
`/mnt/extramedia/_quarantine/`; the names are accurate, so the list doubles as
the re-download list.

## 2 were never damaged — nothing to do

| pages | file |
|---|---|
| 97 | `Luis Royo/Luis Royo - Subversive Beauty & Portfolio.cbr` |
| 73 | `Metal Hurlant Collection/Metal Hurlant Collection v02 p003 (2011) GetComics.INFO.cbr` |

Both are perfectly good RARs that `unrar` reads without complaint. They were
accused because the counter asked `zipfile.is_zipfile()` *before* looking at
byte 0.

That function does not read the start of a file. It scans **backwards from the
end** for a central directory, because a zip is allowed to carry a prefix. Luis
Royo carries a nested `.zip` holding a DOS utility — `PICCHECK.exe` and friends
— so is_zipfile said yes, the counter listed those five members, found no images
among them, and filed a 97-page art book as empty. Metal Hurlant tripped the
same wire and failed one step later: is_zipfile said yes, actually parsing it as
a zip then threw, and the file was recorded as "will not open".

Fixed: the format is now decided by the magic bytes at byte 0, and is_zipfile is
consulted only when no signature matched. Both now count correctly, 97 and 73.
Regression tests in `tests/test_page_count.py`.

**A library-wide scan found exactly these two.** All 29,483 archives were
checked for the shape that causes it — a file whose byte 0 says RAR, 7z or ACE
while `is_zipfile()` claims it anyway. Two hits, both listed above, both now
correct. The bug is fully accounted for.

## 25 hold no pages

Opened, or proved not to be an archive at all, and there is no image inside.
`unar` was tried on every one of these and rescued nothing — the damage in this
section is at byte 0, so there is no header left for a tolerant reader to use.

| size | why | file |
|---|---|---|
| 392 MB | unrecognisable data from byte 0 — no archive signature anywhere | `Americatown (2016) (digital) (d'argh-Empire).cbr` |
| 115 MB | unrecognisable data from byte 0 — no archive signature anywhere | `Marvel Noir (2009-2011)(digital)/X-Men Noir (2009) (Digital) (Kileko-Empire).cbr` |
| 31 MB | unrecognisable data from byte 0 — no archive signature anywhere | `James Bond (2016)/James Bond - 007 005 (2022) (4 covers) (digital) (Son of Ultron-Empire).cbr` |
| 26 MB | first 11 MB is NUL, 14 MB of data survives after it | `Warren Ellis/2008/2008 Anna Mercury/Vol 2/Anna Mercury 2 002 (2009) (four covers) (Minutemen-DTs).cbz` |
| 24 MB | first 15 MB is NUL, 9 MB of data survives after it | `Warren Ellis/2008/2008 Anna Mercury/Vol 2/Anna Mercury 2 003 (2009) (three covers) (fixed) (Minutemen-DTs).cbz` |
| 24 MB | first 4 MB is NUL, 20 MB of data survives after it | `Warren Ellis/1995/Marvel  2099/X men 2099/X men 2099 #24.cbr` |
| 22 MB | first 22 MB is NUL, 0 MB of data survives after it | `Robotech (2018)/Robotech 022 (2019) (Digital) (Mephisto-Empire).cbr` |
| 21 MB | first 8 MB is NUL, 13 MB of data survives after it | `Grant Morrison/Comics/Ultimate X-Men/(083) Ultimate X-Men #075.cbr` |
| 17 MB | first 3 MB is NUL, 15 MB of data survives after it | `Warren Ellis/2008/Astonishing X-Men/Astonishing X-Men 040 (2011) (Minutemen-DTermined).cbr` |
| 17 MB | first 10 MB is NUL, 7 MB of data survives after it | `Grant Morrison/Comics/Ultimate X-Men/(052) Ultimate X-Men #047.cbr` |
| 17 MB | first 14 MB is NUL, 2 MB of data survives after it | `Grant Morrison/Comics/Ultimate X-Men/(092) Ultimate X-Men #084.cbr` |
| 15 MB | first 10 MB is NUL, 4 MB of data survives after it | `Grant Morrison/Comics/Ultimate X-Men/(019) Ultimate X-Men #018.cbr` |
| 14 MB | first 11 MB is NUL, 4 MB of data survives after it | `Grant Morrison/Comics/Ultimate X-Men/(077) Ultimate X-Men #069.cbr` |
| 14 MB | first 12 MB is NUL, 1 MB of data survives after it | `Grant Morrison/Comics/Ultimate X-Men/(086) Ultimate X-Men #078.cbr` |
| 14 MB | first 1 MB is NUL, 13 MB of data survives after it | `Grant Morrison/Comics/Ultimate X-Men/(041) Ultimate X-Men #036.cbr` |
| 13 MB | first 13 MB is NUL, 0 MB of data survives after it | `Grant Morrison/Comics/Ultimate X-Men/(097) Ultimate X-Men #089.cbr` |
| 11 MB | first 4 MB is NUL, 7 MB of data survives after it | `Grant Morrison/Comics/Ultimate X-Men/(059) Ultimate X-Men #054.cbr` |
| 5 MB | first 4 MB is NUL, 1 MB of data survives after it | `Grant Morrison/Comics/Ultimate X-Men/(042) Ultimate X-Men #037.cbr` |
| 1 MB | first 1 MB is NUL, 0 MB of data survives after it | `Warren Ellis/2008/2008 Anna Mercury/Vol 2/Anna Mercury 2 002 (Auxiliary Cover Only) (2009) (Steam-DCP).cbr` |
| 0 MB | zip archive opens, holds no images | `Sergio Aragones Funnies 01-12 (2011-2014)/Sergio Aragones Funnies v01.cbz` |
| 0 MB | zip archive opens, holds no images | `Cheval Noir magazine/Cheval Noir v03.cbz` |
| 0 MB | zero bytes — the file is empty | `Something is Killing the Children/Fall of the House of Slaughter 03 (of 04) (2026) (Digital) (Mephisto-Empire).cbr` |
| 0 MB | zero bytes — the file is empty | `I'm a Lost Angel/I'm a Lost Angel (2026) (Digital) (Dipole-Empire).cbz` |
| 0 MB | zero bytes — the file is empty | `Greg Rucka/The Death of Stalin 001 - Agony (2016) (Europe Comics) (digital) (Lynx-Empire).cbr` |
| 0 MB | zero bytes — the file is empty | `Floyd_Farland_Citizen_of_the_Future/Floyd_Farland_Citizen_of_the_Future.cbz` |

## 14 would not open, and `unar` reads them anyway — but only 7 are comics

The user reported that **MComix opens `The Rise and Fall of the Trigan Empire
v02`**, which this report had called unreadable. That was correct, and it
exposed the second tooling fault.

MComix uses `unar` (The Unarchiver). Our counter only ever asked `unrar`. On
damaged RARs the two disagree badly: `unrar` refuses Trigan Empire outright and
`7z` lists 189 members but extracts **zero** decodable images, while `unar`
extracts **188 real JPEGs, 590 MB**. Every page of that book except the last one
was sitting there the whole time.

This section originally reported all 14 as the same fault — a download cut short,
each losing exactly its last page. **That was wrong for half of them,** and the
error was mine: I trusted a page count that no tool here can actually produce
for these files.

A lister stops at the first damage it meets and reports what it reached. On a
file with three readable pages it says "3 pages", whether the comic had 3 or 24.
Both shapes therefore look identical in a listing, and I read the number as the
truth. What separates them is not the listing but **what follows the damage**:

* **Truncated** — the file ends in real bytes. The last page's data was cut
  mid-write and about a megabyte of it sits past the archive's last indexed
  member. Everything before the cut is a complete comic. **These lose exactly
  one page, always the last.**
* **Overwritten** — the file ends in *megabytes of NUL*. This is the same
  storage damage as the 25 below, differing only in where the zeros landed:
  at the tail here, so the archive header survives and the pages before the
  zeros still read. **What comes out is a fragment**, and its true page count is
  unknowable, because the only tool that could count them is reading zeros.

The measured split is absolute — the truncated files end in under a dozen NUL
bytes, the overwritten ones in 1.1 MB to 26 MB. Nothing sits between.

### 7 truncated — real comics, one page short each

| pages | size | file |
|---|---|---|
| 188 of 189 | 562 MB | `Trigan Empire /The Rise and Fall of the Trigan Empire v02 (2020) (digital) (Mr Norrell-Empire).cbr` |
| 122 of 123 | 435 MB | `Image comics/Carbon Grey/Carbon Grey - Omnibus (2016) GetComics.INFO.cbr` |
| 105 of 106 | 418 MB | `Image comics/Lake of Fire (2017) (Digital) (XRA-Empire).cbz` |
| 42 of 43 | 86 MB | `The Celestial Bibendum/The Celestial Bibendum 2 (Digital) (Humanoids).cbr` |
| 49 of 50 | 67 MB | `Europe Comics (Collection)/Stern/Stern 02 - City of Savages _2018_ _Europe Comics_ _Digital-Empire_ (newcomic.info).cbr` |
| 7 of 8 | 12 MB | `The Celestial Bibendum/The Celestial Bibendum 3 (Digital) (Humanoids).cbr` |
| 2 of 3 | 1 MB | `Europe Comics (Collection)/Where is Kiki (Europe Comics 2020) (webrip) (MagicMan-DCP).cbr` |

**All seven are done** — rescued, repacked as `.cbz`, originals in quarantine.
**515 pages recovered, 7 lost.**

### 7 overwritten — fragments, not comics

`readable` is what decodes; `of about` is the original size divided by the mean
compressed page size, so it is an estimate and not a count.

| readable | of about | size | ends in | file |
|---|---|---|---|---|
| 3 | ~32 | 29 MB | 26 MB NUL | `Warren Ellis/2008/2008 Anna Mercury/Vol 2/Anna Mercury 2 001 (2009) (Three Covers) (Minutemen-Shamil).cbr` |
| 3 | ~35 | 17 MB | 15 MB NUL | `Grant Morrison/Comics/Ultimate X-Men/(093) Ultimate X-Men #085.cbr` |
| 9 | ~29 | 13 MB | 9 MB NUL | `Grant Morrison/Comics/Ultimate X-Men/(098) Ultimate X-Men #090.cbr` |
| 6 | ~27 | 12 MB | 9 MB NUL | `Grant Morrison/Comics/Ultimate X-Men/(087) Ultimate X-Men #079.cbr` |
| 17 | ~27 | 11 MB | 4 MB NUL | `Ted McKeever (Collection) (1987-2007)/1995 - Engines (DC Legends of the Dark Knight 74-75)/Legends of the Dark Knight 074.cbz` |
| 11 | ~22 | 5 MB | 2 MB NUL | `Grant Morrison/Comics/Ultimate X-Men/(043) Ultimate X-Men #038.cbr` |
| 11 | ~18 | 3 MB | 1 MB NUL | `Grant Morrison/Comics/Ultimate X-Men/(001) Ultimate X-Men #00½.cbr` |

`Anna Mercury 2 001` is the worst of them and the one that exposed the fault. Its
first surviving page is named `pg014`, so it is missing the *front* of the comic
as well as the back: two readable pages, numbered 14 and 15, out of roughly 32.
It was rescued before the check existed, which put a 2-page file into the library
under the full issue's name — worse than the broken original, which at least
failed openly. **It has been reverted**; the original is back in place and the
fragment is parked at `/tmp/anna_mercury_001_fragment.cbz`.

`repack_comics.py` now refuses these by default, naming the damage as the
reason, and `--salvage-fragments` overrides it for a caller who wants the pages
anyway. Even under the override it reports `pages_lost` as unknown rather than
computing `claimed - recovered`, which would measure how far the lister read and
not how many pages the comic had.

**A later sweep of all 20,569 RARs found a fragment this table's test would have
missed.** `Doom Patrol 04.cbr` ends in exactly *one* zero byte, so the NUL
measure cleared it as an ordinary truncation — but 7z can account for only
1.6 MB of its 22.5 MB, and the remaining 20.9 MB is real bytes no reader can
reach. Same outcome, different damage. The check now asks both questions: how
much NUL the file ends in, and what share of it no lister can reach. Truncated
files leave 0%–18.6% unreached, fragments 39.7% or more.

Three more turned up with it — `Mazer in Prison (Comic).cbr`,
`(078) Ultimate X-Men #070.cbr` and `(020) Ultimate X-Men #019.cbr`. All four are
already listed under *4 no tool here can read* below, which prescribes the same
fix, so nothing moves; they are named here because they are the same failure and
a later sweep should not have to work that out twice.

**Decided: re-download, do not salvage.** The originals stay where they are and
all seven are on `LIBRARY_REDOWNLOAD.md`. A file that refuses to open is honest
about its state; a two-page `.cbz` wearing a full issue's name is not, and the
shelf is the place you are least able to check.

## 2 ACE archives — intact, and now readable — 86 pages

`unace-nonfree` was installed, and both turn out to be **completely undamaged**.
Every page decodes; nothing is missing.

| pages | size | file |
|---|---|---|
| 38 of 38 | 51 MB | `Spirou & Fantasio/Spirou & Fantasio 19 - Baby Fever in Champignac.cbr` |
| 48 of 48 | 13 MB | `Aria (Collection) GetComics.INFO/Aria 07 - A Murder of Crows (Ringoscann).cbr` |

They were never broken — ACE is simply a format from 1998 that nothing here
could open. QComicBook still cannot read ACE, so these want **repacking** into
plain `.cbz`, not re-downloading.

Extraction was done inside a sandbox and every output path checked, because ACE
parsers have a path-traversal history (CVE-2018-20250, severe enough that WinRAR
dropped the format in 2019). Nothing escaped; all 86 files landed where they
should.

## 4 no tool here can read

| size | why | file |
|---|---|---|
| 21 MB | RAR, parsing fails after 2 members — "Data is corrupted" | `Grant Morrison/Comics/Doom Patrol/Doom Patrol 04.cbr` |
| 14 MB | RAR, parsing fails after 1 member — "Data is corrupted" | `Enders Game/2    Mazer in Prison/Mazer in Prison (Comic).cbr` |
| 9 MB | RAR, parsing fails after 1 member — "Data is corrupted" | `Grant Morrison/Comics/Ultimate X-Men/(078) Ultimate X-Men #070.cbr` |
| 4 MB | RAR, parsing fails after 1 member — "Data is corrupted" | `Grant Morrison/Comics/Ultimate X-Men/(020) Ultimate X-Men #019.cbr` |

All four are damaged near the front, so `unar` gets one or two filenames out and
then loses the structure. Unlike the truncated seven above, there is no surviving
tail to rescue. Re-download.

---

**36 files want re-downloading** — the 25 that hold no pages, the 4 corrupt RARs,
and the 7 overwritten fragments, which are the same storage damage as the 25 and
belong with them.

| | files | pages | what it needs |
|---|---|---|---|
| never damaged | 2 | 170 | nothing — counter was wrong |
| ACE, intact | 2 | 86 | **done** — repacked to `.cbz` |
| truncated | 7 | 515 | **done** — rescued, one page lost each |
| already repacked | 9 | 970 | done |
| overwritten fragments | 7 | ~60 of ~190 | re-download; salvageable only as fragments |
| **beyond recovery** | **29** | — | **re-download** |

Down from 66 files and 5.6 GB, and **not one file was repaired to get there.**
Every reduction came from correcting a tool that had been mistaking its own
inability to read a file for evidence about the file.

### On the two tooling faults behind the false alarms

Both had the same shape — a negative answer from a tool being recorded as a fact
about the comic — and between them they account for 16 of the files this report
once condemned.

1. **`is_zipfile` before byte 0.** It scans backwards from the end of the file,
   so a RAR carrying a nested zip was read as that inner zip. Cost: `Luis Royo -
   Subversive Beauty`, a healthy 97-page book. Fixed in `list_members`; pinned
   by `tests/test_page_count.py`.
2. **`unrar` as the only RAR reader.** It refuses damaged archives that `unar`
   reads happily, and it refused one — Metal Hurlant v02 — that is not damaged
   at all. Cost: 515 readable pages across 7 files declared unreadable, plus 73
   in a file that was never damaged. This is why MComix could open a file this
   report said was broken. **Not yet fixed in the counter** — see below.

There was a third fault, and it was mine rather than the code's:

3. **A page count read off a tool that had already stopped.** `lsar` reports
   what it reached before the damage, which on an overwritten file is a fragment
   count, and I reported `claimed - recovered` as the loss. For seven files that
   produced a confident number — "lost 1 of 3" — where the honest answer was
   "lost about 29 of 32, and no tool here can tell you exactly". Fixed by
   `overwritten_bytes()`, which measures the NUL run the listers cannot see past;
   pinned by four tests in `tests/test_repack.py`.

### ~~Recommended: teach the counter to fall back to `unar`~~ — measured, and rejected

`list_members` calls `unrar lb` and treats a non-zero exit as "cannot read
this". The obvious fix was to try `lsar` next, since it answers for files
`unrar` gives up on. Rather than land a one-line change that re-reads every RAR
in the library, it was measured first — all **20,569** RARs, both directions:

| | |
|---|---|
| `unrar` refuses | 9 |
| of those, `lsar` can count | 9 — 37 pages |
| RARs `unrar` reads, sampled as a control | 400 |
| **counts the two tools disagree on** | **0** |

The control sample is clean, so the fallback would never overwrite a count that
was already right. It was still rejected, on what the nine files are: **every
one of them is a fragment**, and all nine are on the re-download list already.
The 37 pages are not 37 pages recovered — they are how far `lsar` reads into
nine comics before hitting the damage.

The fallback's whole effect here would be to turn nine honest "unreadable"
results into nine small, confident, wrong page counts. Unreadable is the right
answer for all nine, and a wrong number is harder to notice than a failure.
**Decision: leave `list_members` as it is.**

The sweep was still worth its three hours. It is what found `Doom Patrol 04` —
a fragment that ends in a single zero byte, which the NUL-based check called
truncated and would have rescued into a 2-page file under a full issue's name.
The check now also measures how much of the file no lister can reach.

### On the three files that are data all the way through

`Americatown`, `X-Men Noir` and `James Bond - 007 005` are not truncated and
not NUL-padded. Searching the first 64 MB and the last 4 KB of each turns up no
zip, rar or 7z signature at any offset, and the bytes look random from position
zero. There is nothing to carve out; re-download is the only fix. They are a
different failure from the NUL group below, which still holds real data.

`unar` was tried on all three and, as expected, found no archive to open.

### On the NUL damage

The 19 files marked as NUL are not empty, and not zero-length — they are the
size they should be. Each has one contiguous run of NUL bytes at the *front*,
then genuine data after it: the tail of the archive survived and the head did
not. Since the archive header lives at byte 0, the file is unreadable even
though most of a book is still sitting in it.

Their modification times fall into four episodes rather than spreading evenly:
ten files on 2022-10-23 inside a single 52-minute window, five on 2022-07-06,
three in July 2018 and one in May 2020. That shape says a handful of bad write
sessions, not gradual decay of the disk. Re-download is the practical fix;
carving the surviving tail out is possible but not worth it.

`unar` was tried on all 19 and rescued nothing from any of them. This is the
expected result and worth stating plainly: a tolerant reader still needs a
header to start from, and in these files byte 0 is gone. The contrast with the
15 above is the whole point — those were damaged at the *end*, where everything
before the cut survives.
