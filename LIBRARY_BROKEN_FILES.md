# Damaged or non-comic files in the library

Found by counting the images inside all 29,515 archives.

Two rounds of false alarms have been removed from this list, both caused by the
same mistake — a format the counter could not name read as a file holding no
pages, which accuses a good comic instead of admitting ignorance. First the
`.jpe` page extension (159 KissManga files), then the 7z, tar and ACE
containers. Counts here are from the fixed counter.

Since the first version of this report, 23 of the 66 files listed have left it:
nine were repacked and are now readable, fourteen were error pages and have
been moved out of the library. The two sections below are what is left.

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

## 29 hold no pages

Opened, or proved not to be an archive at all, and there is no image inside.

| size | why | file |
|---|---|---|
| 392 MB | unrecognisable data from byte 0 — no archive signature anywhere | `Americatown (2016) (digital) (d'argh-Empire).cbr` |
| 210 MB | first 51 MB is NUL, 158 MB of data survives after it | `Jungle.../Jungle Fantasy - Survivors (001-010)(2017-2018)(digital)(600dpi)(Minutemen-Excelsior)/Jungle Fantasy - Survivors 007 (2017) (digital) (600dpi) (Minutemen-Excelsior).cbz` |
| 195 MB | first 9 MB is NUL, 187 MB of data survives after it | `Jungle.../Jungle Fantasy - Survivors (001-010)(2017-2018)(digital)(600dpi)(Minutemen-Excelsior)/Jungle Fantasy - Survivors 002 (2017) (digital) (600dpi) (Minutemen-Excelsior).cbz` |
| 177 MB | first 149 MB is NUL, 28 MB of data survives after it | `Jungle.../Jungle Fantasy - Survivors (001-010)(2017-2018)(digital)(600dpi)(Minutemen-Excelsior)/Jungle Fantasy - Survivors 004 (2017) (digital) (600dpi) (Minutemen-Excelsior).cbz` |
| 115 MB | unrecognisable data from byte 0 — no archive signature anywhere | `Marvel Noir (2009-2011)(digital)/X-Men Noir (2009) (Digital) (Kileko-Empire).cbr` |
| 109 MB | zip archive opens, holds no images | `Luis Royo/Luis Royo - Subversive Beauty & Portfolio.cbr` |
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

## 22 could not be read

These claim to be archives and will not open, so nothing is asserted about
what is inside them. A truncated download looks like this.

| size | why | file |
|---|---|---|
| 589 MB | archive header present, will not open | `Trigan Empire /The Rise and Fall of the Trigan Empire v02 (2020) (digital) (Mr Norrell-Empire).cbr` |
| 457 MB | archive header present, will not open | `Image comics/Carbon Grey/Carbon Grey - Omnibus (2016) GetComics.INFO.cbr` |
| 438 MB | archive header present, will not open | `Image comics/Lake of Fire (2017) (Digital) (XRA-Empire).cbz` |
| 214 MB | archive header present, will not open | `Jungle.../Jungle Fantasy - Survivors (001-010)(2017-2018)(digital)(600dpi)(Minutemen-Excelsior)/Jungle Fantasy - Survivors 001 (2017) (digital) (600dpi) (Minutemen-Excelsior).cbz` |
| 103 MB | archive header present, will not open | `Metal Hurlant Collection/Metal Hurlant Collection v02 p003 (2011) GetComics.INFO.cbr` |
| 91 MB | archive header present, will not open | `The Celestial Bibendum/The Celestial Bibendum 2 (Digital) (Humanoids).cbr` |
| 71 MB | archive header present, will not open | `Europe Comics (Collection)/Stern/Stern 02 - City of Savages _2018_ _Europe Comics_ _Digital-Empire_ (newcomic.info).cbr` |
| 54 MB | ACE archive — no reader installed, so nothing is claimed | `Spirou & Fantasio/Spirou & Fantasio 19 - Baby Fever in Champignac.cbr` |
| 29 MB | archive header present, will not open | `Warren Ellis/2008/2008 Anna Mercury/Vol 2/Anna Mercury 2 001 (2009) (Three Covers) (Minutemen-Shamil).cbr` |
| 23 MB | archive header present, will not open | `Grant Morrison/Comics/Doom Patrol/Doom Patrol 04.cbr` |
| 17 MB | archive header present, will not open | `Grant Morrison/Comics/Ultimate X-Men/(093) Ultimate X-Men #085.cbr` |
| 15 MB | archive header present, will not open | `Enders Game/2    Mazer in Prison/Mazer in Prison (Comic).cbr` |
| 15 MB | ACE archive — no reader installed, so nothing is claimed | `Aria (Collection) GetComics.INFO/Aria 07 - A Murder of Crows (Ringoscann).cbr` |
| 14 MB | archive header present, will not open | `The Celestial Bibendum/The Celestial Bibendum 3 (Digital) (Humanoids).cbr` |
| 13 MB | archive header present, will not open | `Grant Morrison/Comics/Ultimate X-Men/(098) Ultimate X-Men #090.cbr` |
| 12 MB | archive header present, will not open | `Grant Morrison/Comics/Ultimate X-Men/(087) Ultimate X-Men #079.cbr` |
| 11 MB | archive header present, will not open | `Ted McKeever (Collection) (1987-2007)/1995 - Engines (DC Legends of the Dark Knight 74-75)/Legends of the Dark Knight 074.cbz` |
| 10 MB | archive header present, will not open | `Grant Morrison/Comics/Ultimate X-Men/(078) Ultimate X-Men #070.cbr` |
| 5 MB | archive header present, will not open | `Grant Morrison/Comics/Ultimate X-Men/(043) Ultimate X-Men #038.cbr` |
| 5 MB | archive header present, will not open | `Grant Morrison/Comics/Ultimate X-Men/(020) Ultimate X-Men #019.cbr` |
| 3 MB | archive header present, will not open | `Grant Morrison/Comics/Ultimate X-Men/(001) Ultimate X-Men #00½.cbr` |
| 2 MB | archive header present, will not open | `Europe Comics (Collection)/Where is Kiki (Europe Comics 2020) (webrip) (MagicMan-DCP).cbr` |

---

**3.7 GB** across 51 files that are actually broken — down from 5.6 GB and 66.

### On the three files that are data all the way through

`Americatown`, `X-Men Noir` and `James Bond - 007 005` are not truncated and
not NUL-padded. Searching the first 64 MB and the last 4 KB of each turns up no
zip, rar or 7z signature at any offset, and the bytes look random from position
zero. There is nothing to carve out; re-download is the only fix. They are a
different failure from the NUL group below, which still holds real data.

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
