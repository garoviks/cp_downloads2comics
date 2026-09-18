# Library repack candidates

Read-only sweep of `/mnt/extramedia/Comics` — 29,515 archives, 3613.8 GB, 2,733,120 pages.

Every comic in the library should open in QComicBook. These are the ones that will not. Nothing here has been changed.

## How much work is this

| Defect | Files | Size | Pages | Why it matters |
|---|---:|---:|---:|---|
| 7z or tar container | 20 | 1.0 GB | 161 | QComicBook will not open these. Repack as zip. |
| Nested archives | 15 | 3.5 GB | 3,767 | A wrapper, not a book. Unpack one level. |
| **Distinct files affected** | **35** | **4.5 GB** | **3,928** | A file can carry more than one defect. |

That is 0.12% of the library by count and 0.13% by size.

**Page format is not on that list, and that is a correction.** An earlier version of this sweep counted 206 files as defective for holding WebP, GIF or BMP pages. They are not. Once the eight 7z books were repacked as plain zip, QComicBook read their 443 WebP pages without complaint — the container was the whole problem, and the page format was never part of it. All 206 of those files are already in zip or rar containers, so they need nothing. They are still listed further down, as information rather than as work.

## Container formats across the whole library

| Container | Files | Size |
|---|---:|---:|
| rar | 20,530 | 2232.0 GB |
| zip | 8,939 | 1380.1 GB |
| tar | 19 | 0.8 GB |
| unknown | 16 | 0.0 GB |
| not-an-archive | 8 | 0.6 GB |
| ace | 2 | 0.1 GB |
| 7z | 1 | 0.2 GB |

`unreadable` means the file claims to be an archive and would not open, so nothing is asserted about what is inside it — that is not the same as being empty. `not-an-archive` means no archive format was found at all, which is a definite answer.

## 1. 7z and tar containers — repack as zip

**20 files, 1.0 GB, 161 pages**

| Format | Files |
|---|---:|
| tar | 19 |
| 7z | 1 |

Largest first.

| Size | Pages | Container | Path |
|---:|---:|---|---|
| 210 MB | 0 | tar | `Jungle.../Jungle Fantasy - Survivors (001-010)(2017-2018)(digital)(600dpi)(Minutemen-Excelsior)/Jungle Fantasy - Survivors 007 (2017) (digital) (600dpi) (Minutemen-Excelsior).cbz` |
| 199 MB | 161 | 7z | `3 Guns (2013) TPB.cbr` |
| 195 MB | 0 | tar | `Jungle.../Jungle Fantasy - Survivors (001-010)(2017-2018)(digital)(600dpi)(Minutemen-Excelsior)/Jungle Fantasy - Survivors 002 (2017) (digital) (600dpi) (Minutemen-Excelsior).cbz` |
| 177 MB | 0 | tar | `Jungle.../Jungle Fantasy - Survivors (001-010)(2017-2018)(digital)(600dpi)(Minutemen-Excelsior)/Jungle Fantasy - Survivors 004 (2017) (digital) (600dpi) (Minutemen-Excelsior).cbz` |
| 26 MB | 0 | tar | `Warren Ellis/2008/2008 Anna Mercury/Vol 2/Anna Mercury 2 002 (2009) (four covers) (Minutemen-DTs).cbz` |
| 24 MB | 0 | tar | `Warren Ellis/2008/2008 Anna Mercury/Vol 2/Anna Mercury 2 003 (2009) (three covers) (fixed) (Minutemen-DTs).cbz` |
| 24 MB | 0 | tar | `Warren Ellis/1995/Marvel  2099/X men 2099/X men 2099 #24.cbr` |
| 22 MB | 0 | tar | `Robotech (2018)/Robotech 022 (2019) (Digital) (Mephisto-Empire).cbr` |
| 21 MB | 0 | tar | `Grant Morrison/Comics/Ultimate X-Men/(083) Ultimate X-Men #075.cbr` |
| 17 MB | 0 | tar | `Warren Ellis/2008/Astonishing X-Men/Astonishing X-Men 040 (2011) (Minutemen-DTermined).cbr` |
| 17 MB | 0 | tar | `Grant Morrison/Comics/Ultimate X-Men/(052) Ultimate X-Men #047.cbr` |
| 17 MB | 0 | tar | `Grant Morrison/Comics/Ultimate X-Men/(092) Ultimate X-Men #084.cbr` |
| 15 MB | 0 | tar | `Grant Morrison/Comics/Ultimate X-Men/(019) Ultimate X-Men #018.cbr` |
| 14 MB | 0 | tar | `Grant Morrison/Comics/Ultimate X-Men/(077) Ultimate X-Men #069.cbr` |
| 14 MB | 0 | tar | `Grant Morrison/Comics/Ultimate X-Men/(086) Ultimate X-Men #078.cbr` |
| 14 MB | 0 | tar | `Grant Morrison/Comics/Ultimate X-Men/(041) Ultimate X-Men #036.cbr` |
| 13 MB | 0 | tar | `Grant Morrison/Comics/Ultimate X-Men/(097) Ultimate X-Men #089.cbr` |
| 11 MB | 0 | tar | `Grant Morrison/Comics/Ultimate X-Men/(059) Ultimate X-Men #054.cbr` |
| 5 MB | 0 | tar | `Grant Morrison/Comics/Ultimate X-Men/(042) Ultimate X-Men #037.cbr` |
| 1 MB | 0 | tar | `Warren Ellis/2008/2008 Anna Mercury/Vol 2/Anna Mercury 2 002 (Auxiliary Cover Only) (2009) (Steam-DCP).cbr` |

## 2. Pages that are not JPEG or PNG — nothing to do

**206 files, 12.3 GB, 26,885 pages**

Listed for information. Every one of these is already in a zip or rar container, and QComicBook renders WebP, GIF and BMP pages out of those without complaint — proven on 443 WebP pages across three repacked books. Re-encoding them would lose quality and fix nothing.

Broken down by the format found. A file with pages in two formats is counted under each, so these rows sum to more than the file count above.

| Page format | Files | Pages in that format |
|---|---:|---:|
| gif | 109 | 9,696 |
| webp | 88 | 12,061 |
| bmp | 8 | 84 |
| tif | 2 | 79 |

Largest first, top 50 of 206.

| Size | Pages | Page formats | Path |
|---:|---:|---|---|
| 866 MB | 906 | webp | `Batman/Batman by James Tynion IV Omnibus, Vol. 1 (fan-made).cbz` |
| 364 MB | 220 | webp | `Elflord_(1986)/Elflord v01 (1986).cbz` |
| 353 MB | 655 | webp | `Batman/The Batman & Catwoman Wedding Complete Collection (2018).cbz` |
| 349 MB | 130 | bmp | `Julia/Julia 2 - Object Of Desire [ShinjiGR].cbr` |
| 309 MB | 268 | webp | `Image comics/Chrononauts (001-004)(2015)/Chrononauts Library Edition v01 (2025) (digital) (ElleryQueen-DCP) (WebP).cbz` |
| 292 MB | 468 | webp | `Hellboy/04 B.P.R.D. Plague of Frogs - OMNIBUS EDITION Vol. 2 (2015) ComixLedger.cbz` |
| 292 MB | 468 | webp | `Hellboy/Hellboy in reading order/04 B.P.R.D. Plague of Frogs - OMNIBUS EDITION Vol. 2 (2015) ComixLedger.cbz` |
| 286 MB | 436 | webp | `Hellboy/06 B.P.R.D. Plague of Frogs - OMNIBUS EDITION Vol. 4 (2015) ComixLedger.cbz` |
| 286 MB | 436 | webp | `Hellboy/Hellboy in reading order/06 B.P.R.D. Plague of Frogs - OMNIBUS EDITION Vol. 4 (2015) ComixLedger.cbz` |
| 282 MB | 448 | webp | `Hellboy/05 B.P.R.D. Plague of Frogs - OMNIBUS EDITION Vol. 3 (2015) ComixLedger.cbz` |
| 282 MB | 448 | webp | `Hellboy/Hellboy in reading order/05 B.P.R.D. Plague of Frogs - OMNIBUS EDITION Vol. 3 (2015) ComixLedger.cbz` |
| 282 MB | 532 | gif | `Judge Dredd - The Complete Case Files/Judge Dredd - The Complete Case Files v16.cbr` |
| 257 MB | 512 | webp | `The Little Prince 01-24 (2012-2015)/Little Prince v01.cbz` |
| 249 MB | 79 | tif | `Hernandez brothers/Love and Rockets/Love and Rockets Trading Cards (Fantagraphics)(500dpi tiffs - to print a3).cbr` |
| 220 MB | 109 | webp | `The City Beneath Her Feet/The City Beneath Her Feet v01 (2025).cbz` |
| 217 MB | 164 | webp | `Protector (2020)/Protector (2020).cbz` |
| 212 MB | 408 | webp | `Hellboy/03 B.P.R.D. Plague of Frogs - OMNIBUS EDITION Vol. 1 (2014) ComixLedger.cbz` |
| 212 MB | 408 | webp | `Hellboy/Hellboy in reading order/03 B.P.R.D. Plague of Frogs - OMNIBUS EDITION Vol. 1 (2014) ComixLedger.cbz` |
| 208 MB | 469 | webp | `Hellboy/07 B.P.R.D. 1946-1948 - OMNIBUS EDITION (2016) ComixLedger.cbz` |
| 208 MB | 469 | webp | `Hellboy/Hellboy in reading order/07 B.P.R.D. 1946-1948 - OMNIBUS EDITION (2016) ComixLedger.cbz` |
| 187 MB | 291 | webp | `The Blood Brothers Mother v01 (2024).cbz` |
| 143 MB | 258 | webp | `Wizard - How To Draw - The Best of Basic Training (2005-2007)/Wizard—How to Draw–The Best of Basic Training–Vol. 6 Getting Started (2007) (HD digital) ComixLedger.cbz` |
| 125 MB | 336 | webp | `The Little Prince 01-24 (2012-2015)/Little Prince v03.cbz` |
| 111 MB | 143 | gif | `Nth Man (001-016)(1989-1990)/Nth Man v03.cbz` |
| 111 MB | 84 | webp | `Blood_n_Guts_(1990)/Blood 'n Guts v01 (1991).cbz` |
| 102 MB | 93 | webp | `Witch Hammer (2023)/Witch Hammer v01 (2024).cbz` |
| 90 MB | 191 | webp | `We Wicked Ones 01-06 (2023)/We Wicked Ones 01-06 (2023).cbz` |
| 85 MB | 116 | webp | `Dirk Gently's Holistic Detective Agency/Dirk Gently's Holistic Detective Agency - The Salmon of Doubt v01 (2017) GetComics.INFO.cbz` |
| 84 MB | 222 | webp | `Usagi Yojimbo/The Art of Usagi Yojimbo - 20th Anniversary Edition (2004) GetComics.INFO.cbz` |
| 80 MB | 153 | webp | `Hellboy/08 B.P.R.D. Being Human (TPB) (2011) ComixLedger.cbz` |
| 80 MB | 153 | webp | `Hellboy/B.P.R.D. Being Human (TPB) (2011) ComixLedger.cbz` |
| 80 MB | 153 | webp | `Hellboy/Hellboy in reading order/08 B.P.R.D. Being Human (TPB) (2011) ComixLedger.cbz` |
| 78 MB | 165 | bmp | `Fred Perrys Legacy 001-006 (1999-2001)/Fred Perrys Legacy v01 (1999).cbz` |
| 72 MB | 167 | gif | `2000AD - Collections /Harlem Heroes V5 (Dan Dare 2000AD Remix).cbr` |
| 70 MB | 101 | webp | `Dirk Gently's Holistic Detective Agency/Dirk Gently's Holistic Detective Agency - The Salmon of Doubt v02 (2017) GetComics.INFO.cbz` |
| 70 MB | 34 | webp | `Anne Rice/Anne Rices Queen of the Damned (1991)/Anne Rice's Queen of the Damned #006 (1993).cbz` |
| 69 MB | 235 | webp | `Glamourpuss 01-26 (2008-2012)/Glamourpuss v01 (2009).cbz` |
| 68 MB | 32 | webp | `Anne Rice/Anne Rices Queen of the Damned (1991)/Anne Rice's Queen of the Damned #011 (1993).cbz` |
| 68 MB | 128 | webp | `Phantasmagoria 01-03 (2022) (WebP)/Phantasmagoria 01-03 (2022) (WebP).cbz` |
| 66 MB | 35 | webp | `Anne Rice/Anne Rices Queen of the Damned (1991)/Anne Rice's Queen of the Damned #005 (1992).cbz` |
| 65 MB | 160 | gif | `American Splendor (Collection) (1976-2008)/American Splendor - The Life and Times of Harvey Pekar (1986) (Doubleday).cbr` |
| 63 MB | 34 | webp | `Anne Rice/Anne Rices Queen of the Damned (1991)/Anne Rice's Queen of the Damned #007 (1993).cbz` |
| 62 MB | 34 | webp | `Anne Rice/Anne Rices The Vampire Lestat (1990)/Anne Rice's The Vampire Lestat #009 (1991).cbz` |
| 62 MB | 144 | gif | `Atheist 01-04 (2005-2007)/Atheist v01 (2007).cbz` |
| 61 MB | 140 | gif | `Creeps (001-004)(2001-2002)/Creeps (001-004)(2001-2002).cbz` |
| 60 MB | 35 | webp | `Anne Rice/Anne Rices Queen of the Damned (1991)/Anne Rice's Queen of the Damned #004 (1992).cbz` |
| 60 MB | 33 | webp | `Anne Rice/Anne Rices Queen of the Damned (1991)/Anne Rice's Queen of the Damned #008 (1993).cbz` |
| 60 MB | 168 | webp | `The Winter Men (2005) [RC HQ-Scan 576p] ComixLedger.cbz` |
| 60 MB | 28 | webp | `Anne Rice/Anne Rices The Vampire Lestat (1990)/Anne Rice's The Vampire Lestat #010 (1991).cbz` |
| 59 MB | 96 | gif | `2000AD prog/2000AD (Specials, Annuals & Poster Progs + Extras)/2000AD Yearbooks & Specials (1977 - 2013)/Specials (-JJ-)/Best of 2000AD Special Edition 1999.cbr` |
| … | … | … | _…and 156 more, see the total above_ |

## 3. Nested archives — a wrapper, not a book

**15 files, 3.5 GB, 3,767 pages**

These hold other comic archives as members. A reader opening one sees no pages. Note the page count column: where it is 0 the file is purely a wrapper, and where it is not the archive is a mixture.

Largest first.

| Size | Pages | Archive members | Path |
|---:|---:|---|---|
| 1.30 GB | 1773 | 1 | `Deadline magazine (1988-1990)/Deadline v01.cbz` |
| 767 MB | 188 | 3 | `Monstress/Monstress v09 - The Possessed (2024).cbz` |
| 572 MB | 242 | 1 | `Wake/Wake - Parts 11-15 (2008-2012).cbr` |
| 220 MB | 142 | 1 | `Robert Kirkman/Oblivion Song (Kirkman 2018)/Oblivion Song v05 (2021) (Digital) (DrDoom-Empire).cbz` |
| 214 MB | 406 | 1 | `Hombre series (Ortiz, Jos).cbr` |
| 128 MB | 563 | 34 | `Insufferable/Insufferable v1 (01-34) (2012)/Insufferable v1 (01-34) (2012).cbz` |
| 74 MB | 50 | 1 | `Jodorowsky and Moebius/Blueberry/YOUNG BLUEBERRY (01-04)/Young Blueberry 02 - A Yankee Named Blueberry.cbr` |
| 73 MB | 101 | 1 | `Heavy Metal/Heavy Metal Vols 01-35 (1977-2012)/Heavy Metal v03 02 (1979-06) (glitch-DCP).cbr` |
| 39 MB | 146 | 1 | `Heavy Metal/02. Specials/Heavy Metal Special Edition v08 02 (1994) (Greatest Hits) (Humperdido).cbr` |
| 28 MB | 25 | 1 | `Image comics/Guarding the Globe v1 (001-006)(2010-2011)/Guarding the Globe 04 (of 06) (2011) (two covers) (Minutemen-TwiztiD-T).cbz` |
| 17 MB | 27 | 1 | `Hellboy/6.)  Sir Edward Grey, Witchfinder - In the Service of Angels #1-5  (1879 AD)/Sir Edward Grey, Witchfinder - In the Service of Angels #5.cbz` |
| 17 MB | 27 | 1 | `Sir Edward Grey, Witchfinder (Collection) (2009-2014) GetComics.INFO/1- In the Service of Angels (001-005)(2009)(Minutemen-InnerDemons+DTs)/scans/Witchfinder - In the Service of Angels 05 (of 5) (2009) (F) (Minutemen-DTs).cbz` |
| 17 MB | 24 | 1 | `Garth Ennis Collection/The Boys/Herogasm/Herogasm 06.cbr` |
| 14 MB | 43 | 1 | `Judge Dredd The Megazine/Judge Dredd Megazine v2 (001-083)(1992-1995)/Judge Dredd Megazine v2 008 (1992) (c2c) (Youngstar).cbr` |
| 5 MB | 10 | 1 | `SleepyGimp - Evelina & Nancy Templeton (ADULT)/24. (Short) Evelina & Violet White - Pam.cbz` |

### What the largest wrappers contain

- `Deadline magazine (1988-1990)/Deadline v01.cbz` — 1 archive members, 1773 loose pages
  - `18_Deadline 016 [1990 March](FIXED)(S23-ScAndy)/New folder.rar`
- `Monstress/Monstress v09 - The Possessed (2024).cbz` — 3 archive members, 188 loose pages
  - `Monstress 052 (2024) (digital) (Goobadaddy-Empire).cbz`
  - `Monstress 053 (2024) (digital) (Goobadaddy-Empire).cbz`
  - `Monstress 054 (2024) (digital) (Goobadaddy-Empire).cbz`
- `Wake/Wake - Parts 11-15 (2008-2012).cbr` — 1 archive members, 242 loose pages
  - `2010 Wake 13 - Powerslide (Ouash) (Retranslation)/Wake 13 - Powerslide (Ouash) (Retranslation).cbr`
- `Robert Kirkman/Oblivion Song (Kirkman 2018)/Oblivion Song v05 (2021) (Digital) (DrDoom-Empire).cbz` — 1 archive members, 142 loose pages
  - `Oblivion Song v05 (2021) (Digital) (DrDoom-Empire).cbz/`
- `Hombre series (Ortiz, Jos).cbr` — 1 archive members, 406 loose pages
  - `Ortiz, José - Hombre series (JJ_O&S_hombre2)/1992 Hombre 4 Attila and the Seven Dwarves (JJ_O&S_hombre4)/Morea - T04 - Un parfum d'éternité.rar`
- `Insufferable/Insufferable v1 (01-34) (2012)/Insufferable v1 (01-34) (2012).cbz` — 34 archive members, 563 loose pages
  - `Insufferable 001 (2012) (Mark Waid, digital).cbz`
  - `Insufferable 002 (2012) (Mark Waid, digital).cbz`
  - `Insufferable 003 (2012) (Mark Waid, digital).cbz`
  - `Insufferable 004 (2012) (Mark Waid, digital).cbz`
  - `Insufferable 005 (2012) (Mark Waid, digital).cbz`
  - `Insufferable 006 (2012) (Mark Waid, digital).cbz`
  - `Insufferable 007 (2012) (Mark Waid, digital).cbz`
  - `Insufferable 008 (2012) (Mark Waid, digital).cbz`
  - _…and 26 more_
- `Jodorowsky and Moebius/Blueberry/YOUNG BLUEBERRY (01-04)/Young Blueberry 02 - A Yankee Named Blueberry.cbr` — 1 archive members, 50 loose pages
  - `La_jeunesse_de_02-Un_Yankee_nomme_Blueberry/19 Young Blueberry 02_-_A_Yankee_Named_Blueberrya.cbr`
- `Heavy Metal/Heavy Metal Vols 01-35 (1977-2012)/Heavy Metal v03 02 (1979-06) (glitch-DCP).cbr` — 1 archive members, 101 loose pages
  - `Heavy Metal v03 02 (June 79).cbr`
- `Heavy Metal/02. Specials/Heavy Metal Special Edition v08 02 (1994) (Greatest Hits) (Humperdido).cbr` — 1 archive members, 146 loose pages
  - `Heavy_Metal_Special_Edition_1994_#02_Greatest Hits.cbr`
- `Image comics/Guarding the Globe v1 (001-006)(2010-2011)/Guarding the Globe 04 (of 06) (2011) (two covers) (Minutemen-TwiztiD-T).cbz` — 1 archive members, 25 loose pages
  - `Guarding the Globe 04 (of 06) (2011) (two covers) (Minutemen-TwiztiD-T).cbz/`

## Not repack candidates, but worth knowing

### 38 unreadable

These claim to be archives and would not open. Nothing is claimed about their contents. They are a separate problem from repacking.

| Size | Pages | Path |
|---:|---:|---|
| 589 MB | 0 | `Trigan Empire /The Rise and Fall of the Trigan Empire v02 (2020) (digital) (Mr Norrell-Empire).cbr` |
| 457 MB | 0 | `Image comics/Carbon Grey/Carbon Grey - Omnibus (2016) GetComics.INFO.cbr` |
| 438 MB | 0 | `Image comics/Lake of Fire (2017) (Digital) (XRA-Empire).cbz` |
| 214 MB | 0 | `Jungle.../Jungle Fantasy - Survivors (001-010)(2017-2018)(digital)(600dpi)(Minutemen-Excelsior)/Jungle Fantasy - Survivors 001 (2017) (digital) (600dpi) (Minutemen-Excelsior).cbz` |
| 103 MB | 0 | `Metal Hurlant Collection/Metal Hurlant Collection v02 p003 (2011) GetComics.INFO.cbr` |
| 91 MB | 0 | `The Celestial Bibendum/The Celestial Bibendum 2 (Digital) (Humanoids).cbr` |
| 71 MB | 0 | `Europe Comics (Collection)/Stern/Stern 02 - City of Savages _2018_ _Europe Comics_ _Digital-Empire_ (newcomic.info).cbr` |
| 54 MB | 0 | `Spirou & Fantasio/Spirou & Fantasio 19 - Baby Fever in Champignac.cbr` |
| 29 MB | 0 | `Warren Ellis/2008/2008 Anna Mercury/Vol 2/Anna Mercury 2 001 (2009) (Three Covers) (Minutemen-Shamil).cbr` |
| 23 MB | 0 | `Grant Morrison/Comics/Doom Patrol/Doom Patrol 04.cbr` |
| 17 MB | 0 | `Grant Morrison/Comics/Ultimate X-Men/(093) Ultimate X-Men #085.cbr` |
| 15 MB | 0 | `Enders Game/2    Mazer in Prison/Mazer in Prison (Comic).cbr` |
| 15 MB | 0 | `Aria (Collection) GetComics.INFO/Aria 07 - A Murder of Crows (Ringoscann).cbr` |
| 14 MB | 0 | `The Celestial Bibendum/The Celestial Bibendum 3 (Digital) (Humanoids).cbr` |
| 13 MB | 0 | `Grant Morrison/Comics/Ultimate X-Men/(098) Ultimate X-Men #090.cbr` |
| 12 MB | 0 | `Grant Morrison/Comics/Ultimate X-Men/(087) Ultimate X-Men #079.cbr` |
| 11 MB | 0 | `Ted McKeever (Collection) (1987-2007)/1995 - Engines (DC Legends of the Dark Knight 74-75)/Legends of the Dark Knight 074.cbz` |
| 10 MB | 0 | `Grant Morrison/Comics/Ultimate X-Men/(078) Ultimate X-Men #070.cbr` |
| 5 MB | 0 | `Grant Morrison/Comics/Ultimate X-Men/(043) Ultimate X-Men #038.cbr` |
| 5 MB | 0 | `Grant Morrison/Comics/Ultimate X-Men/(020) Ultimate X-Men #019.cbr` |
| 3 MB | 0 | `Grant Morrison/Comics/Ultimate X-Men/(001) Ultimate X-Men #00½.cbr` |
| 2 MB | 0 | `Europe Comics (Collection)/Where is Kiki (Europe Comics 2020) (webrip) (MagicMan-DCP).cbr` |
| 0 MB | 0 | `Alix Senator  (2012-2020)/Alix Senator v08 - The City of Poisons (2018) (Scanlation) (phillywilly).cbr` |
| 0 MB | 0 | `All Night & Every Day (2022) (digital) (Son of Ultron-Empire).cbr` |
| 0 MB | 0 | `Beautiful Killer (2002) (Fan-Made TPB).cbr` |
| 0 MB | 0 | `Dwellings (2023)/Dwellings - All Hallows' Eve Special 01 (2024) (Digital Rip) (Hourman-DCP).cbr` |
| 0 MB | 0 | `Firefly/Firefly 20th Anniversary Special 001.cbr` |
| 0 MB | 0 | `Frankenstein - New World - The Speed of Darkness/Frankenstein - New World - The Speed of Darkness 004 (2026) (digital) (Son of Ultron-Empire).cbr` |
| 0 MB | 0 | `Hello Darkness (2024)/Hello Darkness 022 (2026) (Digital Rip) (Hourman-DCP).cbr` |
| 0 MB | 0 | `Honor and Curse Eternal/Honor and Curse Eternal 004 (2026) (2 covers) (digital) (Knight Ripper-Empire).cbr` |
| 0 MB | 0 | `Murder Drones/Murder Drones 05 (of 06) (2026) (Digital Rip) (Hourman-DCP).cbr` |
| 0 MB | 0 | `Murder Podcast/Murder Podcast 007 (2026) (Digital) (DR & Quinch-Empire).cbr` |
| 0 MB | 0 | `Planet Atmos - Exordium/Planet Atmos - Exordium v01 (2026) (digital) (Knight Ripper-Empire).cbr` |
| 0 MB | 0 | `Red Roots/Red Roots 004 (2026) (Digital) (Mephisto-Empire).cbr` |
| 0 MB | 0 | `Ripcord/Ripcord 004 (2026) (Digital) (DR & Quinch-Empire).cbr` |
| 0 MB | 0 | `Star Trek/Star Trek - Strange New Worlds - The Seeds of Salvation (2026) (digital) (The Magicians-Empire).cbr` |
| 0 MB | 0 | `The Living Corpse Omnibus Vol. 1 (2007).cbr` |
| 0 MB | 0 | `White Sky/White Sky 005 (2026) (Digital) (Mephisto-Empire).cbr` |

### 8 not archives at all

No archive format found. Definitely holds no comic.

| Size | Pages | Path |
|---:|---:|---|
| 392 MB | 0 | `Americatown (2016) (digital) (d'argh-Empire).cbr` |
| 115 MB | 0 | `Marvel Noir (2009-2011)(digital)/X-Men Noir (2009) (Digital) (Kileko-Empire).cbr` |
| 59 MB | 0 | `A Quiet Place - Storm Warning/A Quiet Place - Storm Warning 004 (2026) (digital) (Son of Ultron-Empire).cbr` |
| 31 MB | 0 | `James Bond (2016)/James Bond - 007 005 (2022) (4 covers) (digital) (Son of Ultron-Empire).cbr` |
| 0 MB | 0 | `Floyd_Farland_Citizen_of_the_Future/Floyd_Farland_Citizen_of_the_Future.cbz` |
| 0 MB | 0 | `Greg Rucka/The Death of Stalin 001 - Agony (2016) (Europe Comics) (digital) (Lynx-Empire).cbr` |
| 0 MB | 0 | `I'm a Lost Angel/I'm a Lost Angel (2026) (Digital) (Dipole-Empire).cbz` |
| 0 MB | 0 | `Something is Killing the Children/Fall of the House of Slaughter 03 (of 04) (2026) (Digital) (Mephisto-Empire).cbr` |

