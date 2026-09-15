# Duplicate comics in the library

- Library: `/mnt/extramedia/Comics`
- Comic files scanned: **29,516**
- Groups where one book appears more than once: **1,866**
- Extra copies: **2,764**

## How a duplicate was decided

Two files are the same book when they parse to the same series, volume, issue
and kind. Year and packer tags are ignored, so `(2014)` and `(2016)`, or
`(digital-Empire)` and `(DR & Quinch-Empire)`, are treated as the same book —
which is the case this report exists to find. Sizes differ between packers and
are shown so you can judge, not used to decide. Where every copy is the same
length the heading says so: that is one file filed in two folders, not a
judgement call.

Read a heading with no `v` and no `#` more carefully. It means the parser found
a series name and nothing else, so `Strange Adventures (2000)` and
`Strange Adventures (DC 2022)` — different series two decades apart — land in
one group. The years in the filenames are the giveaway.

**Nothing here has been deleted or moved.** Regenerate with
`python3 library_duplicates.py`.

---

## Likely duplicates — 1,398 groups, 124.20 GB recoverable

Every file in these groups agrees on everything the parser discarded: issue
numbers, subtitles, whether it is a variant or cover-only scan, and any volume
number claimed by the folders above it. That leaves only the year and the
packer's tag to tell the copies apart. The largest copy is listed first.

### moonshadow definitive edition expanded  *(issue)*

- ` 4.74 GB`  Moonshadow/Moonshadow - The Definitive Edition - Expanded (2025) (digital) (Son of Ultron-Empire).cbr
- ` 1.55 GB`  Moonshadow/Moonshadow - The Definitive Edition Expanded (2025) (digital) (Prot-DCP).cbz

### batman by grant morrison — v1  *(volume)*

- ` 1.04 GB`  Grant Morrison/Batman by Grant Morrison Vol 1.cbz
- `  986 MB`  Batman/Batman by Grant Morrison Omnibus v01 (2018) (hybrid) (Marika-Empire).cbz
- `  846 MB`  Batman/BATMAN BY GRANT MORRISON, BOOK 1 (DC) (MiracleScans Ltd).cbr

### batman by grant morrison — v2  *(volume)*

- ` 1.12 GB`  Grant Morrison/Batman by Grant Morrison Vol 2.cbz
- `  968 MB`  Batman/Batman by Grant Morrison Omnibus v02 (2019) (hybrid) (Marika-Empire).cbz
- `  640 MB`  Batman/BATMAN BY GRANT MORRISON, BOOK 2 (DC) (MiracleScans Ltd).cbr

### 09 hellboy — v3  — identical size  *(volume)*

- ` 1.20 GB`  Hellboy/Hellboy in reading order/09 Hellboy Omnibus v03 - The Wild Hunt (2018) (digital) (Son of Ultron-Empire).cbr
- ` 1.20 GB`  Hellboy/09 Hellboy Omnibus v03 - The Wild Hunt (2018) (digital) (Son of Ultron-Empire).cbr

### authority — v2  *(volume)*

- ` 1.73 GB`  Warren Ellis/The Authority/The Authority Book 02 (2021) (digital) (Son of Ultron-Empire).cbr
- `  548 MB`  The Authority/The Authority Vol 2 TPB (2013) (Digital) (DR & Quinch-Empire).cbz

### 11 b.p.r.d. hell on earth — v2  — identical size  *(volume)*

- ` 1.12 GB`  Hellboy/Hellboy in reading order/11 B.P.R.D. Hell on Earth v02 (2018) (digital) (Son of Ultron-Empire).cbr
- ` 1.12 GB`  Hellboy/11 B.P.R.D. Hell on Earth v02 (2018) (digital) (Son of Ultron-Empire).cbr

### harley quinn & gotham city sirens  — identical size  *(volume)*

- `  953 MB`  Harley Quinn/Harley Quinn & the Gotham City Sirens Omnibus (Fan Made) (2020).cbz
- `  953 MB`  Gotham/Harley Quinn & the Gotham City Sirens Omnibus (Fan Made) (2020).cbz

### daredevil by brian michael bendis & alex maleev ultimate — v3  — identical size  *(volume)*

- `  880 MB`  Daredevil/Daredevil by Brian Michael Bendis & Alex Maleev Ultimate Collection - Book 3 (2010) (Digital) (F2) (Zone-Empire).cbr
- `  880 MB`  Brian Michael Bendis - Oeming/Daredevil by Brian Michael Bendis & Alex Maleev/Daredevil by Brian Michael Bendis & Alex Maleev Ultimate Collection - Book 3 (2010) (Digital) (F2) (Zone-Empire).cbr

### batman by grant morrison — v3  *(volume)*

- ` 1.16 GB`  Grant Morrison/Batman by Grant Morrison Vol 3.cbz
- `  593 MB`  Batman/BATMAN BY GRANT MORRISON, BOOK 3 (DC) (MiracleScans Ltd).cbr

### strange adventures  *(issue)*

- ` 1.45 GB`  Strange Adventures/Strange Adventures (DC 2022) (Digital) (EJGriffin-Empire).cbz
- `  164 MB`  Strange Adventures/Strange Adventures (2000).cbz

### magic order — v5  *(volume)*

- ` 1.09 GB`  The Magic Order v05 (2025) (digital) (Son of Ultron-Empire).cbr
- `  380 MB`  Mark Millar/The Magic Order (Mark MIllar)/The Magic Order v05 (2025).cbz

### moon prince  *(issue)*

- `  878 MB`  The Moon Prince (2025) (digital) (Mr Norrell-Empire).cbr
- `  590 MB`  Fantagraphics (Europe)/The Moon Prince (2025) (Graphic Novel) (Fantagraphics) (Digital-HD) (LeDuch).cbz

### bitter root — v2  — identical size  *(volume)*

- `  678 MB`  Europe Comics (Collection)/Bitter Root (2021)/Bitter Root v02 - Rage & Redemption (2020) (Digital) (DR & Quinch-Empire).cbr
- `  678 MB`  Bitter Root/Bitter Root v02 - Rage & Redemption (2020) (Digital) (DR & Quinch-Empire).cbr

### 10 b.p.r.d. hell on earth — v1  — identical size  *(volume)*

- `  651 MB`  Hellboy/Hellboy in reading order/10 B.P.R.D. Hell on Earth v01 (2017) (digital) (Son of Ultron-Empire).cbr
- `  651 MB`  Hellboy/10 B.P.R.D. Hell on Earth v01 (2017) (digital) (Son of Ultron-Empire).cbr

### black widow widowmaker  *(issue)*

- `  706 MB`  Black Widow/Black Widow - Widowmaker.cbz
- `  572 MB`  Black Widow/Black Widow - Widowmaker (2020) (Digital) (Zone-Empire).cbr

### defenders by brian michael bendis  — identical size  *(volume)*

- `  622 MB`  Brian Michael Bendis - Oeming/Defenders by Brian Michael Bendis - The Complete Collection.cbz
- `  622 MB`  Ben/Defenders by Brian Michael Bendis - The Complete Collection.cbz

### devil on my shoulder  *(issue)*

- ` 1.04 GB`  Devil on My Shoulder/Devil on My Shoulder (2026) (digital) (Son of Ultron-Empire).cbr
- `  184 MB`  Devil on My Shoulder/Devil on My Shoulder (2026) (Collection) (Dark Horse Comics) (Digital) (LeDuch-DCP).cbz

### author immortal — v1  *(volume)*

- `  723 MB`  Author Immortal/The Author Immortal v01 (2026).cbz
- `  486 MB`  Author Immortal/Author Immortal v01 (2026) (Digital) (DR & Quinch-Empire).cbr

### hornsby & halo — v2  *(volume)*

- `  726 MB`  Hornsby & Halo  (2024)/Hornsby & Halo v02 (2025).cbz
- `  476 MB`  Hornsby & Halo  (2024)/Hornsby & Halo v02 (2026) (Digital) (DR & Quinch-Empire).cbr

### james bond warren ellis  — identical size  *(volume)*

- `  600 MB`  Warren Ellis/James Bond - The Complete Warren Ellis Omnibus (2020) (digital) (The Magicians-Empire).cbr
- `  600 MB`  James Bond (2016)/James Bond - The Complete Warren Ellis Omnibus (2020) (digital) (The Magicians-Empire).cbr

### buddha  *(issue)*

- `  189 MB`  Manga/Osamu Tezuka/Osamu Tezuka's Buddha/Buddha (v07).cbz
- `  159 MB`  Manga/Osamu Tezuka/Osamu Tezuka's Buddha/Buddha (v08).cbz
- `  147 MB`  Manga/Osamu Tezuka/Osamu Tezuka's Buddha/Buddha (v05).cbz
- `  141 MB`  Manga/Osamu Tezuka/Osamu Tezuka's Buddha/Buddha (v06).cbz
- `  138 MB`  Manga/Osamu Tezuka/Osamu Tezuka's Buddha/Buddha (v04).cbz
- `  134 MB`  Manga/Osamu Tezuka/Osamu Tezuka's Buddha/Buddha (v02).cbz
- `  125 MB`  Manga/Osamu Tezuka/Osamu Tezuka's Buddha/Buddha (v01).cbz
- `  111 MB`  Manga/Osamu Tezuka/Osamu Tezuka's Buddha/Buddha (v03).cbz

### phantom road — v2  — identical size  *(volume)*

- `  572 MB`  Phantom Road (2025)/Phantom Road v02 (2024) (Digital) (DR & Quinch-Empire).cbr
- `  572 MB`  Jeff Lemire/Phantom Road  (2025)/Phantom Road v02 (2024) (Digital) (DR & Quinch-Empire).cbr

### finder library — v1  *(volume)*

- `  751 MB`  Finder/The Finder Library v01 (2011) (digital) (Son of Ultron-Empire).cbr
- `  348 MB`  Finder/The Finder Library Vol 1 (001-022) (2011) (Digital-Empire).cbr

### gilt frame  *(issue)*

- `  875 MB`  Matt Kindt/Gilt Frame (2025) (digital) (Son of Ultron-Empire).cbr
- `  191 MB`  Gilt Frame (2025) (digital) (Li'l Ultron-Empire).cbr

### 16 b.p.r.d. hell on earth — v5  — identical size  *(volume)*

- `  530 MB`  Hellboy/Hellboy in reading order/16 B.P.R.D. Hell on Earth Omnibus v05 (2019) (digital) (Son of Ultron-Empire).cbr
- `  530 MB`  Hellboy/16 B.P.R.D. Hell on Earth Omnibus v05 (2019) (digital) (Son of Ultron-Empire).cbr

### 13 b.p.r.d. hell on earth — v3  — identical size  *(volume)*

- `  527 MB`  Hellboy/Hellboy in reading order/13 B.P.R.D. Hell on Earth v03 (2018) (digital) (Son of Ultron-Empire).cbr
- `  527 MB`  Hellboy/13 B.P.R.D. Hell on Earth v03 (2018) (digital) (Son of Ultron-Empire).cbr

### 14 b.p.r.d. hell on earth — v4  — identical size  *(volume)*

- `  523 MB`  Hellboy/Hellboy in reading order/14 B.P.R.D. Hell on Earth v04 (2018) (digital) (Son of Ultron-Empire).cbr
- `  523 MB`  Hellboy/14 B.P.R.D. Hell on Earth v04 (2018) (digital) (Son of Ultron-Empire).cbr

### texarcanum  *(issue)*

- `  741 MB`  TexArcanum/TexArcanum (2026) (digital) (Son of Ultron-Empire).cbr
- `  296 MB`  TexArcanum/TexArcanum (2025).cbz

### her infernal descent  — identical size  *(issue)*

- `  334 MB`  Her Infernal Descent (2018).cbz
- `  334 MB`  Her Infernal Descent (2018)/Her Infernal Descent (2018).cbz
- `  334 MB`  Aftershock comics/Her Infernal Descent (2018).cbz

### manifest destiny — v5  — identical size  *(volume)*

- `  326 MB`  Manifest Destiny/Manifest Destiny v05 - Mnemophobia _ Chronophobia (2016) (digital) (Minutemen-Newt+Geist) (RC).cbz
- `  326 MB`  Manifest Destiny/Manifest Destiny v05 - Mnemophobia _ Chronophobia (2016) (digital) (Minutemen-Newt Geist) (RC).cbz
- `  326 MB`  Manifest Destiny/Manifest Destiny v05 - Mnemophobia & Chronophobia (2016) (digital) (Minutemen-Newt Geist) (RC).cbz

### chrononauts library edition — v1  *(volume)*

- `  660 MB`  Mark Millar/Chrononauts Library Edition v01 (2025) (ElleryQueen-DCP) (AI-enhanced juvecube).cbz
- `  309 MB`  Image comics/Chrononauts (001-004)(2015)/Chrononauts Library Edition v01 (2025) (digital) (ElleryQueen-DCP) (WebP).cbz

### checkmate by greg rucka — v2  — identical size  *(volume)*

- `  481 MB`  Greg Rucka/Checkmate by Greg Rucka Book 02 (2018) (digital) (Son of Ultron-Empire).cbr
- `  481 MB`  Checkmate by Greg Rucka (Books 01-02)(2017-2018)(digital)(Son of Ultron-Empire)/Checkmate by Greg Rucka Book 02 (2018) (digital) (Son of Ultron-Empire).cbr

### tithe — v3  — identical size  *(volume)*

- `  481 MB`  Image comics/Postal/Postal - The Tithe/The Tithe v03 - Samaritan (2017) (Digital) (DR _ Quinch-Empire).cbr
- `  481 MB`  Image comics/Postal/Postal - The Tithe/The Tithe v03 - Samaritan (2017) (Digital) (DR & Quinch-Empire).cbr

### ghost — v4  *(volume)*

- `  574 MB`  Ghost/Ghost v04 (2013-2015) .cbz
- `  386 MB`  Ghost/Ghost Omnibus v04 (2013) (digital) (Son of Ultron II-Empire).cbr

### folklords  — identical size  *(issue)*

- `  469 MB`  Matt Kindt/Folklords (2020) (digital) (Son of Ultron-Empire).cbr
- `  469 MB`  Folklords (2020) (digital) (Son of Ultron-Empire).cbr

### authority — v1  *(volume)*

- `  503 MB`  Warren Ellis/The Authority/The Authority Book 01 (2020) (digital) (Son of Ultron-Empire).cbr
- `  430 MB`  The Authority/The Authority Vol 1 TPB (2013) (Digital) (DR & Quinch-Empire).cbr

### henchgirl  *(issue)*

- `  551 MB`  Henchgirl (2017) (digital) (Son of Ultron-Empire).cbr
- `  379 MB`  Henchgirl (Expanded Edition) (2020) (digital) (Son of Ultron-Empire).cbr

### sacrificers — v4  *(volume)*

- `  574 MB`  The Sacrificers/The Sacrificers v04 (2026) (Digital) (DR & Quinch-Empire).cbr
- `  353 MB`  The Sacrificers/The Sacrificers v04.cbz

### hot lunch  — identical size  *(special)*

- `  457 MB`  Hot Lunch Special (001-005)(2018-2019)(digital)(Mephisto-Empire).cbz
- `  457 MB`  Aftershock comics/Hot Lunch Special (001-005)(2018-2019)(digital)(Mephisto-Empire).cbz

### george herriman library — v4  — identical size  *(volume)*

- `  456 MB`  The George Herriman Library - Krazy and Ignatz 1916-1918/The George Herriman Library v04 - Krazy & Ignatz 1925-1927 (2023) (Digital) (Dipole-Empire).cbz
- `  456 MB`  Krazy & Ignatz /The George Herriman Library v04 - Krazy & Ignatz 1925-1927 (2023) (Digital) (Dipole-Empire).cbz

### mothballs  *(issue)*

- `  598 MB`  Mothballs (2024) (Digital-Empire).cbz
- `  295 MB`  Mothballs (2024) (digital) (DrVink-DCP).cbz

### 05a hellboy weird tales 2014  — identical size  *(issue)*

- `  446 MB`  Hellboy/Hellboy in reading order/05a Hellboy - Weird Tales 2014.cbr
- `  446 MB`  Hellboy/05a Hellboy - Weird Tales 2014.cbr

### hellboy artists richard corben  — identical size  *(issue)*

- `  445 MB`  Richard Corben/Hellboy Artists Collection - Richard Corben (2024) (digital) (DrVink-HD-DCP).cbz
- `  445 MB`  Hellboy/Hellboy Artists Collection - Richard Corben (2024) (digital) (DrVink-HD-DCP).cbz

### total thb — v2  *(volume)*

- `  394 MB`  Total_THB_v2.cbz
- `  394 MB`  Total THB/Total THB v02.cbz
- `   96 MB`  Total THB/Total THB v02 (2026) (Digital) (XRA-Empire).cbz

### ring of nibelung  *(issue)*

- `  758 MB`  The Ring of Nibelung (1991-2014)/The Ring of the Nibelung (2014) (digital) (Son of Ultron II-Empire).cbr
- `  113 MB`  The Ring of Nibelung (1991-2014)/The Ring of the Nibelung (1991).cbr

### deviant — v2  *(volume)*

- `  636 MB`  The Deviant (2023)/The Deviant v02 (2025) (Digital) (DR & Quinch-Empire).cbr
- `  225 MB`  The Deviant (2023)/The Deviant v02 (2024).cbz

### rompepistas  *(issue)*

- `  616 MB`  Rompepistas (Ablaze) (2024) (Digital) (XRA-Empire).cbz
- `  245 MB`  Rompepistas (2024) (Graphic Novel) (Ablaze) (Digital-HD) (LeDuch).cbz

### hyde street — v2  *(volume)*

- `  749 MB`  Hyde Street/Hyde Street v02 (2026) (Digital) (DR & Quinch-Empire).cbr
- `  108 MB`  Hyde Street/Hyde Street v02 (2025).cbz

### bitter root — v1  *(volume)*

- `  539 MB`  Europe Comics (Collection)/Bitter Root (2021)/Bitter Root v01 - Family Business (2019) (Digital) (DR & Quinch-Empire).cbr
- `  313 MB`  Bitter Root/Bitter Root v01 - Family Business (2019) (Digital) (LuCaZ).cbz

### dust to dust  *(issue)*

- `  578 MB`  Dust to Dust/Dust to Dust (2026) (Digital) (DR & Quinch-Empire).cbr
- `  265 MB`  Dust to Dust/Dust to Dust (2026) (Collection) (Image) (Digital) (LeDuch-DCP).cbz

### kill me & other curiosities  *(issue)*

- `  764 MB`  Kill Me & Other Curiosities/Kill Me & Other Curiosities (2024) (digital) (Son of Ultron-Empire).cbr
- `   62 MB`  Kill Me & Other Curiosities/Kill Me & Other Curiosities (2024) (digital) (Li'l Ultron-Empire).cbr

### 15 hellboy universe secret histories  — identical size  *(issue)*

- `  410 MB`  Hellboy/Hellboy in reading order/15 Hellboy Universe - The Secret Histories (2021) (digital) (Son of Ultron-Empire).cbr
- `  410 MB`  Hellboy/15 Hellboy Universe - The Secret Histories (2021) (digital) (Son of Ultron-Empire).cbr

### past aways facedown in timestream  — identical size  *(issue)*

- `  398 MB`  Past Aways - Facedown in the Timestream (2016) (digital) (Son of Ultron-Empire).cbr
- `  398 MB`  Matt Kindt/Past Aways - Facedown in the Timestream (2016) (digital) (Son of Ultron-Empire).cbr

### riptide  *(issue)*

- `  669 MB`  Riptide (2025) (digital) (Son of Ultron-Empire).cbr
- `  123 MB`  Riptide (001-004)(2018)(digital)(Minutemen-Excelsior)/Riptide (001-004)(2018)(digital)(Minutemen-Excelsior).cbz

### george herriman library — v3  — identical size  *(volume)*

- `  394 MB`  The George Herriman Library - Krazy and Ignatz 1916-1918/The George Herriman Library v03 - Krazy & Ignatz 1922-1924 (2022) (Digital) (Dipole-Empire).cbz
- `  394 MB`  Krazy & Ignatz /The George Herriman Library v03 - Krazy & Ignatz 1922-1924 (2022) (Digital) (Dipole-Empire).cbz

### checkmate by greg rucka — v1  — identical size  *(volume)*

- `  392 MB`  Greg Rucka/Checkmate by Greg Rucka Book 01 (2017) (digital) (Son of Ultron-Empire).cbr
- `  392 MB`  Checkmate by Greg Rucka (Books 01-02)(2017-2018)(digital)(Son of Ultron-Empire)/Checkmate by Greg Rucka Book 01 (2017) (digital) (Son of Ultron-Empire).cbr

### 02 hellboy — v2  — identical size  *(volume)*

- `  388 MB`  Hellboy/Hellboy in reading order/02 Hellboy Omnibus v02 - Strange Places (2018) (digital) (Son of Ultron-Empire).cbr
- `  388 MB`  Hellboy/02 Hellboy Omnibus v02 - Strange Places (2018) (digital) (Son of Ultron-Empire).cbr

### beauty — v1  *(volume)*

- `  567 MB`  The Beauty (2016)/The Beauty - Book 01 (2026) (Digital) (DR & Quinch-Empire).cbr
- `  205 MB`  The Beauty (2016)/The Beauty v01 (2016) (Digital) (Zone-Empire).cbr

### airtight garage  — identical size  *(issue)*

- `  380 MB`  Jodorowsky and Moebius/AIRTIGHT GARAGE (1976-80) (Heavy Metal collection) [HD 2564] (Hoyeru).cbr
- `  380 MB`  Heavy Metal/02. Specials/AIRTIGHT GARAGE (1976-80) (Heavy Metal collection) [HD 2564] (Hoyeru).cbr

### rocketfellers — v2  *(volume)*

- `  495 MB`  The Rocketfellers (2024)/The Rocketfellers v02 (2026) (Digital) (DR & Quinch-Empire).cbr
- `  262 MB`  The Rocketfellers (2024)/The Rocketfellers v02 (2025).cbz

### babs — v1  *(volume)*

- `  453 MB`  Babs v01 (2025) (Digital) (EricJGriffin-Empire).cbz
- `  287 MB`  Babs v01 (2025).cbz

### cosmic detective  *(issue)*

- `  556 MB`  Cosmic Detective (2023) (digital) (Son of Ultron-Empire).cbr
- `  184 MB`  Cosmic Detective.cbz

### brothers dracul  — identical size  *(issue)*

- `  367 MB`  Dracula comics/Brothers Dracul (2018).cbz
- `  367 MB`  Aftershock comics/Brothers Dracul (2018).cbz

### deconstructing incal  — identical size  *(issue)*

- `  367 MB`  Jodorowsky and Moebius/Incal/04 Final Incal (v01-v03) (2008-2014) (digital) (Minutemen-Excelsior)/Deconstructing The Incal (Annestay and Quillien) (2017) (c2c) (fylgja).cbz
- `  367 MB`  Jodorowsky and Moebius/Deconstructing The Incal (Annestay and Quillien) (2017) (c2c) (fylgja).cbz

### midnite show  *(issue)*

- `  582 MB`  The Midnite Show/The Midnite Show (2024) (digital) (Son of Ultron-Empire).cbr
- `  147 MB`  The Midnite Show/The Midnite Show (2024) (digital) (DrVink-HD-DCP).cbz

### george herriman library krazy & ignatz  — identical size  *(issue)*

- `  364 MB`  The George Herriman Library - Krazy and Ignatz 1916-1918/The George Herriman Library - Krazy & Ignatz 1916-1918 (2019) (Digital-Empire).cbr
- `  364 MB`  Krazy & Ignatz /The George Herriman Library - Krazy & Ignatz 1916-1918 (2019) (Digital-Empire).cbr

### essential judge dredd necropolis  — identical size  *(issue)*

- `  361 MB`  Judge Dredd - Collections/Essential Judge Dredd - Necropolis (2022) (digital) (Torquemada).cbr
- `  361 MB`  Judge Dredd - Collections/Essential Judge Dredd/Essential Judge Dredd - Necropolis (2022) (digital) (Torquemada).cbr

### roughneck  — identical size  *(issue)*

- `  360 MB`  Roughneck (2017) (digital) (apocalyp7e).cbr
- `  360 MB`  Jeff Lemire/Roughneck (2017) (digital) (apocalyp7e).cbr

### clive barkers nightbreed — v1  — identical size  *(volume)*

- `  237 MB`  Clive Barker/Clive Barkers Nightbreed Vol. 01 (2015) (digital) (Minutemen-Slayer).cbr
- `  237 MB`  Clive Barker/Clive Barker s Nightbreed v2 (001-012+)(2014-2017)(digital)(Minutemen-Slayer)/Clive Barkers Nightbreed Vol. 01 (2015) (digital) (Minutemen-Slayer).cbr
- `  237 MB`  Clive Barker/Clive Barker s Nightbreed 001-012 (2014-2015)/Clive Barkers Nightbreed Vol. 01 (2015) (digital) (Minutemen-Slayer).cbr

### lawless — v1  *(volume)*

- `  563 MB`  Dan Abnett/Lawless v01 - Welcome to Badrock (2017) (digital) (Ampersand).cbr
- `  145 MB`  2000AD - Collections /Lawless/Lawless v01 - Welcome to Badrock (F) (2017) (digital) (Torquemada).cbr

### death deluxe edition  — identical size  *(issue)*

- `  354 MB`  The Sandman/The Sandman - Extras/Death (Sandman)/Death - The Deluxe Edition (2012) (Digital) (Zone-Empire).cbr
- `  354 MB`  Neil Gaiman Library/Death - The Deluxe Edition (2012) (Digital) (Zone-Empire).cbr

### king of moths  *(issue)*

- `  420 MB`  The King of Moths (2023) (Digital-Empire).cbz
- `  287 MB`  The King Of Moths (Ablaze 2023) (webrip) (MagicMan-DCP).cbr

### blood stain — v1  — identical size  *(volume)*

- `  352 MB`  Blood Stain/Blood Stain v01 (2016) GetComics.INFO.cbr
- `  352 MB`  Bllod Stain/Blood Stain v01 (2016) GetComics.INFO.cbr

### john carpenter's tales of science fiction twitch  *(issue)*

- `  390 MB`  John Carpenter's Tales of Science Fiction/John Carpenter's Tales of Science Fiction - Twitch (2019).cbz
- `  301 MB`  John Carpenter's Tales of Science Fiction/John Carpenter's Tales of Science Fiction - TWITCH (2019) (digital) (DrVink-HD-DCP).cbz

### james bond agent of spectre  *(issue)*

- `  512 MB`  James Bond (2016)/James Bond - Agent of Spectre (2023) (digital) (The Magicians-Empire).cbr
- `  173 MB`  James Bond (2016)/James Bond - Agent of Spectre (2021) .cbz

### human target — v1  *(volume)*

- `  625 MB`  The Human Target/The Human Target v01 (2022) (digital) (Son of Ultron-Empire).cbr
- `   55 MB`  The Human Target/Human Target v01 (2003).cbz

### coven  — identical size  *(issue)*

- `  337 MB`  Europe Comics (Collection)/Coven (2023) (digital) (Mr Norrell-Empire).cbr
- `  337 MB`  Coven (2023) (digital) (Mr Norrell-Empire).cbr

### dead kings  — identical size  *(issue)*

- `  337 MB`  Dead Kings (2018)/Dead Kings (2018).cbz
- `  337 MB`  Aftershock comics/Dead Kings (2018).cbz

### superman by mark millar  — identical size  *(issue)*

- `  333 MB`  Superman/Superman by Mark Millar (2018) (Digital) (Zone-Empire).cbr
- `  333 MB`  Mark Millar/Superman by Mark Millar (2018) (Digital) (Zone-Empire).cbr

### shadow roads — v1  *(volume)*

- `  554 MB`  Shadow Roads (2018)/Shadow Roads v01 (2020).cbz
- `  108 MB`  Cullen Bunn/Shadow Roads v01 (2019) (digital) (DrVink).cbz

### shade — v1  *(volume)*

- `  600 MB`  The Shade 01-04/The Shade v01 (2013) (digital) (Marika-Empire).cbz
- `   41 MB`  The Shade 01-04/The Shade v01.cbz

### message to adolf — v2  — identical size  *(volume)*

- `  316 MB`  Manga/Osamu Tezuka/Message to Adolf v02 (Osamu Tezuka )(2012) .cbr
- `  316 MB`  Manga/Message to Adolf v01-02 (2012) (Digital) (XRA-Empire)/Message to Adolf v02 (2012) (Digital) (XRA-Empire).cbr

### blood stain — v2  — identical size  *(volume)*

- `  315 MB`  Blood Stain/Blood Stain v02 (2017) (Digital-uHD) (Dogmatix-Empire).cbr
- `  315 MB`  Bllod Stain/Blood Stain v02 (2017) (Digital-uHD) (Dogmatix-Empire).cbr

### 01 hellboy — v1  — identical size  *(volume)*

- `  312 MB`  Hellboy/Hellboy in reading order/01 Hellboy Omnibus v01 - Seed of Destruction (2018) (digital) (Son of Ultron-Empire).cbr
- `  312 MB`  Hellboy/01 Hellboy Omnibus v01 - Seed of Destruction (2018) (digital) (Son of Ultron-Empire).cbr

### brilliant trash  — identical size  *(issue)*

- `  311 MB`  Brilliant Trash (2017)/Brilliant Trash (2017).cbz
- `  311 MB`  Aftershock comics/Brilliant Trash (2017).cbz

### thundercats cheetara — v1  *(volume)*

- `  322 MB`  ThunderCats/Thundercats - Cheetara v01.cbz
- `  297 MB`  ThunderCats/ThunderCats - Cheetara v01 (2026) (Digital) (Shan-Empire).cbz

### ghost in shell  *(issue)*

- `  423 MB`  Manga/Ghost in the Shell/Ghost in the Shell (1995) (null-DCP).cbz
- `  196 MB`  Manga/Ghost in the Shell/Ghost in the shell.cbr

### red seas — v2  — identical size  *(volume)*

- `  309 MB`  The Red Seas (v01-v02) (2015) (digital) (Ampersand)/The Red Seas v02 - Fire Across the Deep (2015) (digital) (Ampersand).cbr
- `  309 MB`  2000AD - Collections /The Red Seas/The Red Seas v02 - Fire Across the Deep (2015) (digital) (Ampersand).cbr

### judge dredd  *(issue)*

- `  571 MB`  Judge Dredd - Collections/Judge Dredd (001-012+)(2015-2016)(digital)(Minutemen-Thoth)/Judge Dredd (001-012+)(2015-2016)(digital)(Minutemen-Thoth).cbz
- `   45 MB`  Judge Dredd - Collections/Judge Dredd (v1-v7(2012-2015)(digital)/Judge Dredd (FCBD) (2013) (digital-Empire).cbr

### red seas — v1  — identical size  *(volume)*

- `  307 MB`  The Red Seas (v01-v02) (2015) (digital) (Ampersand)/The Red Seas v01 - Under the Banner of King Death (2015) (digital) (Ampersand).cbr
- `  307 MB`  2000AD - Collections /The Red Seas/The Red Seas v01 - Under the Banner of King Death (2015) (digital) (Ampersand).cbr

### black widow  *(issue)*

- `  421 MB`  Black Widow/Black Widow (2022) (Fan Made TPB).cbr
- `  187 MB`  Black Widow/Black Widow (2019) (Digital) (Zone-Empire).cbz

### ghost — v3  *(volume)*

- `  506 MB`  Ghost/Ghost Omnibus v03 (2012) (digital) (Son of Ultron II-Empire).cbr
- `   99 MB`  Ghost/Ghost v03 (2012-2013).cbz

### abe sapien — v9  — identical size  *(volume)*

- `  300 MB`  Hellboy/Abe Sapien TPBs/Abe Sapien v09 - Lost Lives and Other Stories (2017).cbr
- `  300 MB`  Abe Sapien/Abe Sapien v09 - Lost Lives and Other Stories (2017) (digital) (Son of Ultron-Empire).cbr

### campisi dragon incident  — identical size  *(issue)*

- `  297 MB`  Campisi - The Dragon Incident (2021) /Campisi - The Dragon Incident (2021) .cbz
- `  297 MB`  Aftershock comics/Campisi - The Dragon Incident (2021) .cbz

### 2000ad  *(issue)*

- `  113 MB`  2000AD prog/Yearbooks & Specials/FCBD/2000AD (FCBD 2015) (c2c) (Sooth&Talon-Novus-HD).cbr
- `  102 MB`  2000AD prog/Yearbooks & Specials/FCBD/2000AD (FCBD 2014) (Team-DCP).cbr
- `   82 MB`  2000AD prog/Yearbooks & Specials/FCBD/2000AD (FCBD 2016) (c2c) (HD) (Minutemen-Enceladus).cbr
- `   58 MB`  2000AD prog/Yearbooks & Specials/FCBD/2000AD (FCBD 2018) (c2c) (Minutemen-Enceladus).cbz
- `   58 MB`  2000AD prog/Yearbooks & Specials/2000AD (FCBD 2018) (c2c) (Minutemen-Enceladus).cbr
- `   51 MB`  2000AD prog/Yearbooks & Specials/FCBD/2000AD (FCBD 2013) (c2c) (DCP&Minutemen-GreenSax).cbr
- `   46 MB`  2000AD prog/Yearbooks & Specials/FCBD/2000AD (FCBD 2016) (c2c) (SD) (Minutemen-Enceladus).cbr
- `   38 MB`  2000AD prog/Yearbooks & Specials/FCBD/2000AD (FCBD 2011) (c2c) (Minutemen).cbz
- `   23 MB`  2000AD prog/Yearbooks & Specials/FCBD/2000AD (FCBD 2017) (scan) (TheMaseThing-DCP).cbr
- `   23 MB`  2000AD prog/Yearbooks & Specials/2000AD (FCBD 2017) (scan) (TheMaseThing-DCP).cbr

### 04 b.p.r.d. plague of frogs edition — v2  — identical size  *(volume)*

- `  292 MB`  Hellboy/Hellboy in reading order/04 B.P.R.D. Plague of Frogs - OMNIBUS EDITION Vol. 2 (2015) ComixLedger.cbz
- `  292 MB`  Hellboy/04 B.P.R.D. Plague of Frogs - OMNIBUS EDITION Vol. 2 (2015) ComixLedger.cbz

### bitter root — v3  *(volume)*

- `  315 MB`  Europe Comics (Collection)/Bitter Root (2021)/Bitter Root v03 - Legacy (2021) (Digital) (DR & Quinch-Empire).cbr
- `  268 MB`  Bitter Root/Bitter Root v03 - Legacy.cbz

### 2000ad presents sci fi thrillers  *(issue)*

- `  378 MB`  2000AD prog/Extras/2000AD Presents Sci-Fi Thrillers (2013) (Digital) (DR & Quinch-Empire).cbr
- `  203 MB`  2000AD prog/Yearbooks & Specials/2000AD Presents - Sci-Fi Thrillers (2013) (digital-HD) (Torquemada).cbr

### bad reception  — identical size  *(issue)*

- `  291 MB`  Bad Reception (2019)/Bad Reception (2019).cbz
- `  291 MB`  Aftershock comics/Bad Reception (2019).cbz

### essential judge dredd apocalypse war  — identical size  *(issue)*

- `  291 MB`  Judge Dredd - Collections/Essential Judge Dredd - The Apocalypse War (2021) (digital) (Torquemada).cbr
- `  291 MB`  Judge Dredd - Collections/Essential Judge Dredd/Essential Judge Dredd - The Apocalypse War (2021) (digital) (Torquemada).cbr

### hoka hey  — identical size  *(issue)*

- `  289 MB`  Hoka Hey (2022) (Scanlation) (phillywilly).cbr
- `  289 MB`  Europe Comics (Collection)/Hoka Hey (2022) (Scanlation) (phillywilly).cbr

### phantom road — v1  *(volume)*

- `  312 MB`  Phantom Road (2025)/Phantom Road v01.cbz
- `  264 MB`  Jeff Lemire/Phantom Road  (2025)/Phantom Road v01 (2023) (Digital) (DR & Quinch-Empire).cbr

### george herriman library — v2  — identical size  *(volume)*

- `  286 MB`  The George Herriman Library - Krazy and Ignatz 1916-1918/The George Herriman Library v02 - Krazy & Ignatz 1919-1921 (2020) (Digital) (Dipole-Empire).cbr
- `  286 MB`  Krazy & Ignatz /The George Herriman Library v02 - Krazy & Ignatz 1919-1921 (2020) (Digital) (Dipole-Empire).cbr

### 06 b.p.r.d. plague of frogs edition — v4  — identical size  *(volume)*

- `  286 MB`  Hellboy/Hellboy in reading order/06 B.P.R.D. Plague of Frogs - OMNIBUS EDITION Vol. 4 (2015) ComixLedger.cbz
- `  286 MB`  Hellboy/06 B.P.R.D. Plague of Frogs - OMNIBUS EDITION Vol. 4 (2015) ComixLedger.cbz

### john carpenter's tales of science fiction standoff  *(issue)*

- `  297 MB`  John Carpenter's Tales of Science Fiction/John Carpenter's Tales of Science Fiction - THE STANDOFF (2019) (digital) (DrVink-HD-DCP).cbz
- `  271 MB`  John Carpenter's Tales of Science Fiction/John Carpenter's Tales of Science Fiction - The Standoff (Fan Made TPB) (2018).cbr

### juvenile  *(issue)*

- `  367 MB`  Juvenile (2025).cbz
- `  200 MB`  Juvenile (2025) (Digital) (DR & Quinch-Empire).cbr

### 05 b.p.r.d. plague of frogs edition — v3  — identical size  *(volume)*

- `  282 MB`  Hellboy/Hellboy in reading order/05 B.P.R.D. Plague of Frogs - OMNIBUS EDITION Vol. 3 (2015) ComixLedger.cbz
- `  282 MB`  Hellboy/05 B.P.R.D. Plague of Frogs - OMNIBUS EDITION Vol. 3 (2015) ComixLedger.cbz

### lawless — v3  *(volume)*

- `  347 MB`  2000AD - Collections /Lawless/Lawless v03 - Ashes to Ashes (2021) (digital) (Torquemada).cbr
- `  217 MB`  Dan Abnett/Lawless v03 - Ashes to Ashes.cbz

### where monsters dwell phantom eagle flies savage skies  — identical size  *(issue)*

- `  282 MB`  The Phantom Eagle/Where Monsters Dwell - The Phantom Eagle Flies The Savage Skies (2015) (Digital) (Kileko-Empire).cbz
- `  282 MB`  Garth Ennis Collection/War Is Hell/Where Monsters Dwell - The Phantom Eagle Flies The Savage Skies (2015) (Digital) (Kileko-Empire).cbz

### avengers four  *(issue)*

- `  280 MB`  Avengers/Avengers - Four (2017) (Digital) (Kileko-Empire).cbr
- `  278 MB`  Avengers/Avengers Vol. 07 (001-011,672-690)(2017-2018)(digital)/Avengers - Four (2017) (digital) (Minutemen-Slayer).cbr

### shadowman by garth ennis & ashley wood getcomics.info  — identical size  *(issue)*

- `  279 MB`  Garth Ennis Collection/Shadowman/Shadowman by Garth Ennis & Ashley Wood (2016) GetComics.INFO.cbr
- `  279 MB`  Ashley Wood/Shadowman by Garth Ennis & Ashley Wood (2016) GetComics.INFO.cbr

### global frequency deluxe edition  — identical size  *(issue)*

- `  278 MB`  Warren Ellis/Global Frequency - The Deluxe Edition (2018) (digital) (Son of Ultron-Empire).cbr
- `  278 MB`  Global Frequency - The Deluxe Edition (2018) (digital) (Son of Ultron-Empire).cbr

### civil war captain america iron man  *(issue)*

- `  290 MB`  Iron Man/Civil War - Captain America - Iron Man (2016) (Digital) (F) (Kileko-Empire).cbz
- `  260 MB`  Civil War Event (001-007+Tie-Ins,Trades&Extras)(2006-2008)(digital)/Civil War - Captain America - Iron Man (2016) (Digital) (Kileko-Empire).cbz

### maria m  — identical size  *(volume)*

- `  274 MB`  Hernandez brothers/Maria M - Complete (2019) (digital) (FatNerd).cbz
- `  274 MB`  Hernandez brothers/Love and Rockets/Maria M - Complete (2019) (digital) (FatNerd).cbz

### manifest destiny — v4  *(volume)*

- `  279 MB`  Manifest Destiny/Manifest Destiny v04 - Sasquatch (2016) (digital) (Minutemen-Newt+Geist) (RC).cbz
- `  268 MB`  Manifest Destiny/Manifest Destiny v04 - Sasquatch (2016) (Digital) (Zone-Empire).cbr

### descendent  — identical size  *(issue)*

- `  273 MB`  Descendent (2019)/Descendent (2019).cbz
- `  273 MB`  Aftershock comics/Descendent (2019).cbz

### battlefields — v1  *(volume)*

- `  299 MB`  The Complete Battlefields (v01-v03)(2009-2014)(digital)(Minutemen-Slayer)/The Complete Battlefields Vol. 01 (2009) (digital) (Minutemen-Slayer).cbr
- `  240 MB`  Garth Ennis Collection/The Complete Battlefields [TPB]/The_Complete_Battlefields_vol01_(2009)_(digital-Empire).cbz

### let this one be a devil — v1  — identical size  *(volume)*

- `  269 MB`  Let This One Be A Devil/Let This One Be A Devil v01 (2025) (Collection) (Dark Horse Comics) (Digital-HD) (LeDuch).cbz
- `  269 MB`  Europe Comics (Collection)/Let This One Be A Devil v01 (2025) (Collection) (Dark Horse Comics) (Digital-HD) (LeDuch).cbz

### metal hurlant — #001  *(issue)*

- `  516 MB`  Metal Hurlant Collection/METAL HURLANT 001 (2025) (digital) (DrVink-HD-DCP).cbz
- `   21 MB`  Metal Hurlant Collection/Metal Hurlant 001-014 (2002-2004) (Humanoids) GetComics.INFO/Metal Hurlant 001.cbr

### sherlock holmes year one — v1  *(volume)*

- `  428 MB`  Sherlock Holmes - Year One v01 (2011) (digital) (The Magicians-Empire).cbr
- `  103 MB`  Sherlock/Sherlock Holmes Year One Vol. 1 (2012) (Digital TPB) (Minutemen-PhD).cbr

### arcbound — v1  *(volume)*

- `  303 MB`  Arcbound/Arcbound v01 (2024).cbz
- `  226 MB`  Arcbound/Arcbound v01 (2026) (Collection) (Dark Horse Books) (Digital-HD) (LeDuch).cbz

### clans of belari  — identical size  *(issue)*

- `  263 MB`  Clans of Belari  (2021)/Clans of Belari  (2021).cbz
- `  263 MB`  Aftershock comics/Clans of Belari  (2021).cbz

### dreaming eagles  — identical size  *(issue)*

- `  261 MB`  Dreaming Eagles (2016) (Fan Made TPB).cbr
- `  261 MB`  Aftershock comics/Dreaming Eagles (2016) (Fan Made TPB).cbr

### artemis & assassin  — identical size  *(issue)*

- `  261 MB`  Artemis & the Assassin (2020)/Artemis & the Assassin (2020).cbz
- `  261 MB`  Aftershock comics/Artemis & the Assassin (2020).cbz

### kid eternity — v1  *(volume)*

- `  316 MB`  Kid Eternity (001-016)(1993-1994)(digital)(Mr -Empire)/Kid Eternity Book 01 (2017) (digital) (Son of Ultron-Empire).cbr
- `  202 MB`  Kid Eternity (001-016)(1993-1994)(digital)(Mr -Empire)/Kid Eternity v01.cbz

### uri tupka and gods another story from lands unknown  *(issue)*

- `  347 MB`  Uri Tupka and the Gods/Uri Tupka and the Gods - Another Story from Lands Unknown (2026) (digital) (Son of Ultron-Empire).cbr
- `   85 MB`  Uri Tupka and the Gods/Uri Tupka and the Gods - Another Story from Lands Unknown (2026) (Graphic Novel) (Dark Horse Comics) (Digital-HD) (LeDuch).cbz
- `   85 MB`  Hellboy/Uri Tupka and the Gods - Another Story from Lands Unknown (2026) (Graphic Novel) (Dark Horse Comics) (Digital-HD) (LeDuch).cbz

### thrilling adventure hour martian manhunt  — identical size  *(issue)*

- `  255 MB`  The Thrilling Adventure Hour/The Thrilling Adventure Hour - Martian Manhunt (2019) (Digital) (DR & Quinch-Empire).cbr
- `  255 MB`  Martian Manhunter (2018) (Digital) (Thornn-Empire)/The Thrilling Adventure Hour - Martian Manhunt (2019) (Digital) (DR & Quinch-Empire).cbr

### clankillers  — identical size  *(issue)*

- `  251 MB`  Clankillers (2018).cbz
- `  251 MB`  Aftershock comics/Clankillers (2018).cbz

### shadow doctor  — identical size  *(issue)*

- `  251 MB`  Shadow Doctor (2021)/Shadow Doctor (2021).cbz
- `  251 MB`  Aftershock comics/Shadow Doctor (2021).cbz

### somna  *(issue)*

- `  267 MB`  Somna/Somna (2024) (Digital) (Mephisto-Empire).cbr
- `  230 MB`  Somna/Somna (2024) (DSTLRY) (digital) (DrVink-HD-DCP) (RC).cbz

### silver city  — identical size  *(issue)*

- `  249 MB`  Silver City  (2021)/Silver City  (2021).cbz
- `  249 MB`  Aftershock comics/Silver City  (2021).cbz

### killer groove  — identical size  *(issue)*

- `  247 MB`  Killer Groove (2019) /Killer Groove (2019) .cbz
- `  247 MB`  Aftershock comics/Killer Groove (2019) .cbz

### disaster inc.  — identical size  *(issue)*

- `  246 MB`  Disaster Inc. (2020)/Disaster Inc. (2020).cbz
- `  246 MB`  Aftershock comics/Disaster Inc. (2020).cbz

### avengers defenders tarot  — identical size  *(issue)*

- `  245 MB`  Defenders/Avengers-Defenders - Tarot (2020) (Digital) (Shanhara).cbz
- `  245 MB`  Avengers/Avengers-Defenders - Tarot (2020) (Digital) (Shanhara).cbz

### captain kid  — identical size  *(issue)*

- `  245 MB`  Captain Kid 001-005 (2016-2017) GetComics.INFO/Captain Kid 001-005 (2016-2017) GetComics.INFO.cbz
- `  245 MB`  Aftershock comics/Captain Kid 001-005 (2016-2017) GetComics.INFO.cbz

### ultimate comics iron man  — identical size  *(issue)*

- `  161 MB`  Ultimates/Ultimate Comics Iron Man (2013) (Digital) (Kileko-Empire).cbr
- `  161 MB`  Iron Man/Ultimate Comics Iron Man (2013) (Digital) (Kileko-Empire).cbr
- `  161 MB`  Avengers/Ultimate Comics Iron Man (2013) (Digital) (Kileko-Empire).cbr

### search for hu  — identical size  *(issue)*

- `  242 MB`  Search for Hu  (2021)/Search for Hu  (2021).cbz
- `  242 MB`  Aftershock comics/Search for Hu  (2021).cbz

### undone by blood — v1  — identical size  *(volume)*

- `  242 MB`  Undone By Blood/Undone By Blood v01 (2020).cbz
- `  242 MB`  Aftershock comics/Undone By Blood v01 (2020).cbz

### beyond breach  — identical size  *(issue)*

- `  242 MB`  Beyond the Breach (2021)/Beyond the Breach (2021).cbz
- `  242 MB`  Aftershock comics/Beyond the Breach (2021).cbz

### girls of dimension — #13  — identical size  *(issue)*

- `  240 MB`  The Girls of Dimension 13 (2021) /The Girls of Dimension 13 (2021) .cbz
- `  240 MB`  Aftershock comics/The Girls of Dimension 13 (2021) .cbz

### gotham city year one  *(issue)*

- `  272 MB`  Gotham/Gotham City - Year One (2023).cbz
- `  207 MB`  Gotham City Year One.cbz

### mars attacks — v1  — identical size  *(volume)*

- `  239 MB`  Mars Attacks (2018-2019)(digital)/Mars Attacks v01 (2019) (Digital) (DR _ Quinch-Empire).cbr
- `  239 MB`  Mars Attacks (2018-2019)(digital)/Mars Attacks v01 (2019) (Digital) (DR & Quinch-Empire).cbr

### battlefields — v2  *(volume)*

- `  350 MB`  The Complete Battlefields (v01-v03)(2009-2014)(digital)(Minutemen-Slayer)/The Complete Battlefields Vol. 02 (2011) (digital) (Minutemen-Slayer).cbr
- `  128 MB`  Garth Ennis Collection/The Complete Battlefields [TPB]/The_Complete_Battlefields_vol02_(2011)_(digital-Empire).cbz

### witchcraft — v1  — identical size  *(volume)*

- `  238 MB`  Witcraft/WitchCraft v01 (1996) (hybrid) (Marika-Empire).cbz
- `  238 MB`  WitchCraft v01 (1996) (hybrid) (Marika-Empire).cbz

### abe sapien — v8  — identical size  *(volume)*

- `  238 MB`  Hellboy/Abe Sapien TPBs/Abe Sapien v08 - The Desolate Shore (2017).cbr
- `  238 MB`  Abe Sapien/Abe Sapien v08 - The Desolate Shore (2017) (digital) (Son of Ultron-Empire).cbr

### herakles — v2  *(volume)*

- `  369 MB`  Herakles (Books 01-03)(2018-2019)(digital-Empire)/Herakles Book 02 (2019) (Digital-Empire).cbr
- `  106 MB`  Herakles (Books 01-03)(2018-2019)(digital-Empire)/Herakles Book 02 (2019) (Lion Forge Comics) (Digital-Empire).cbr

### troublemakers  *(issue)*

- `  177 MB`  The Troublemakers (2009) (digital-Empire).cbr
- `  177 MB`  Hernandez brothers/Gilbert Hernandez book digital editions/The Troublemakers (2009) (digital-Empire).cbr
- `   58 MB`  Hernandez brothers/Love and Rockets/The Troublemakers (2009) (Minutemen-DTs).cbz
- `   58 MB`  Hernandez brothers/Gilbert Hernandez - The Troublemakers (2009)/The Troublemakers (2009).cbz

### blood type — v1  *(volume)*

- `  256 MB`  Blood Type/Blood Type v1 (2026) (Digital Rip) (Hourman-DCP).cbr
- `  213 MB`  Blood Type/Blood Type v01 (2025).cbz

### marked — v2  — identical size  *(volume)*

- `  234 MB`  The Marked (2021) /The Marked v02 - Origins (2021) (Digital) (DR & Quinch-Empire).cbr
- `  234 MB`  Marked/The Marked v02 - Origins (2021) (Digital) (DR & Quinch-Empire).cbr

### i breathed a body  — identical size  *(issue)*

- `  233 MB`  I Breathed A Body (2021)/I Breathed A Body (2021).cbz
- `  233 MB`  Aftershock comics/I Breathed A Body (2021).cbz

### civil war iron man  *(issue)*

- `  338 MB`  Civil War Event (001-007+Tie-Ins,Trades&Extras)(2006-2008)(digital)/Civil War - Iron Man (2007) (Digital) (F) (Kileko-Empire).cbz
- `  128 MB`  Civil War Event (001-007+Tie-Ins,Trades&Extras)(2006-2008)(digital)/Trades/Civil War - Iron Man (2007) (Digital TPB) (Kileko-Empire).cbr

### outer darkness — v1  — identical size  *(volume)*

- `  231 MB`  Outer Darkness (2018-2019)(digital)(Zone-Empire)/Outer Darkness v01 - Each Other's Throats (2019) (Digital) (DrDoom-Empire).cbz
- `  231 MB`  Chew/Outer Darkness v01 - Each Other_s Throats (2019) (Digital) (DrDoom-Empire).cbz

### star trek harlan ellison's city on edge of forever original teleplay  *(issue)*

- `  280 MB`  Star Trek/Star Trek - Harlan Ellison's The City On The Edge of Forever The Original Teleplay (2015) (digital) (The Magicians-Empire).cbr
- `  179 MB`  Star Trek/Star Trek - City on the Edge of Forever 01-05 (2014)/Star Trek - Harlan Ellison's The City On The Edge of Forever The Original Teleplay (2015) (Digital) (TLK-EMPIRE-HD).cbr

### new world  *(issue)*

- `  270 MB`  New World (2019) (digital) (Mr -Empire).cbr
- `  189 MB`  The New World/The New World (2019) (Digital) (DR & Quinch-Empire).cbr

### god and science return of ti girls  — identical size  *(issue)*

- `  153 MB`  Hernandez brothers/Love and Rockets/God and Science - Return of the Ti-Girls (2012) (digital-Empire).cbr
- `  153 MB`  Hernandez brothers/God and Science - Return of the Ti-Girls (2012) (digital-Empire).cbr
- `  153 MB`  God and Science - Return of the Ti-Girls (2012) (digital-Empire).cbr

### abe sapien — v7  — identical size  *(volume)*

- `  229 MB`  Hellboy/Abe Sapien TPBs/Abe Sapien v07 - The Secret Fire (2016).cbr
- `  229 MB`  Abe Sapien/Abe Sapien v07 - The Secret Fire (2016) (digital) (F) (Son of Ultron-Empire).cbr

### outer darkness — v2  — identical size  *(volume)*

- `  228 MB`  Outer Darkness (2018-2019)(digital)(Zone-Empire)/Outer Darkness v02 - Castrophany of Hate (2019) (Digital) (DrDoom-Empire).cbz
- `  228 MB`  Chew/Outer Darkness v02 - Castrophany of Hate (2019) (Digital) (DrDoom-Empire).cbz

### rain like hammers sky cradle  — identical size  *(issue)*

- `  228 MB`  Rain Like Hammers - Sky Cradle (2021) (Digital) (DR & Quinch-Empire).cbr
- `  228 MB`  Brandon Graham/Rain Like Hammers - Sky Cradle (2021) (Digital) (DR & Quinch-Empire).cbr

### ring of roses  *(issue)*

- `  261 MB`  Ring of Roses (2015) (digital) (Mr -Empire).cbr
- `  194 MB`  RING of ROSES.cbr

### john carpenter's tales of science fiction redhead  *(issue)*

- `  229 MB`  John Carpenter's Tales of Science Fiction/John Carpenter's Tales of Science Fiction - REDHEAD (2020) (digital) (DrVink-HD-DCP).cbz
- `  223 MB`  John Carpenter's Tales of Science Fiction/John Carpenter's Tales of Science Fiction - Redhead (Fan Made TPB) (2020).cbr

### autumn kingdom — v1  *(volume)*

- `  266 MB`  The Autumn Kingdom - The Wraithbound Queen/The Autumn Kingdom v01 (2024).cbz
- `  184 MB`  The Autumn Kingdom - The Wraithbound Queen/The Autumn Kingdom v01 (2025) (Collection) (Oni Press) (Digital) (LeDuch-DCP).cbz

### operation overlord  — identical size  *(issue)*

- `  223 MB`  Operation Overlord (2019)/Operation Overlord (2019) (digital) (Torquemada).cbr
- `  223 MB`  2000AD - Collections /Operation Overlord (2019) (digital) (Torquemada).cbr

### phantom on scan  — identical size  *(issue)*

- `  222 MB`  Phantom on the Scan (2021) /Phantom on the Scan (2021) .cbz
- `  222 MB`  Aftershock comics/Phantom on the Scan (2021) .cbz

### project patron  — identical size  *(issue)*

- `  221 MB`  Project Patron (2021) (Digital) (Mephisto-Empire)/Project Patron (2021) (Digital) (Mephisto-Empire).cbz
- `  221 MB`  Aftershock comics/Project Patron (2021) (Digital) (Mephisto-Empire).cbz

### essential judge dredd dredd vs. death  — identical size  *(issue)*

- `  221 MB`  Judge Dredd - Collections/Essential Judge Dredd/Essential Judge Dredd - Dredd Vs. Death (2022) (digital) (Torquemada).cbr
- `  221 MB`  Essential Judge Dredd/Essential Judge Dredd - Dredd Vs. Death (2022) (Digital) (Torquemada).cbr

### grey area — v2  — identical size  *(volume)*

- `  219 MB`  Dan Abnett/Grey Area v02 - A Long Way Home (2019) (digital) (Torquemada).cbr
- `  219 MB`  2000AD - Collections /Grey Area/Grey Area v02 - A Long Way Home (2019) (digital) (Torquemada).cbr

### spider man noir eyes without a face  — identical size  *(issue)*

- `  218 MB`  Marvel Noir (2009-2011)(digital)/Spider-Man Noir - Eyes without a Face (2010) (digital TPB) (Minutemen-Faessla).cbz
- `  218 MB`  GG Studio (Collection) (2010-2012)/Marvel Noir (2009-2011)(digital)/Spider-Man Noir - Eyes without a Face (2010) (digital TPB) (Minutemen-Faessla).cbz

### fierce  — identical size  *(issue)*

- `  218 MB`  Europe Comics (Collection)/Fierce (2023) (digital) (Mr Norrell-Empire).cbr
- `  218 MB`  Europe Comics (Collection)/Fierce (2023) (Europe Comics) (Mr Norrell-Empire).cbr

### red atlantis  *(issue)*

- `  241 MB`  Red Atlantis (2020)/Red Atlantis (2020).cbz
- `  193 MB`  Red Atlantis (2020)/Red Atlantis (2020) (Fan-Made TPB).cbr

### heathens  — identical size  *(issue)*

- `  216 MB`  The Heathens (2021)/The Heathens (2021).cbz
- `  216 MB`  Aftershock comics/The Heathens (2021).cbz

### change  *(issue)*

- `  245 MB`  The Change (2024) (digital) (Son of Ultron-Empire).cbr
- `  187 MB`  Image comics/Change (2013) (Digital-Empire).cbr

### scouts honor  — identical size  *(issue)*

- `  214 MB`  Scouts Honor (2021)/Scouts Honor (2021).cbz
- `  214 MB`  Aftershock comics/Scouts Honor (2021).cbz

### james bond himeros  *(issue)*

- `  288 MB`  James Bond (2016)/James Bond - Himeros (2023) (digital) (The Magicians-Empire).cbr
- `  141 MB`  James Bond (2016)/James Bond - Himeros (2022).cbz

### spy x family — v1  *(volume)*

- `  215 MB`  Manga/Spy-x-family/Spy x Family v01 (2020) (Digital) (LuCaZ).cbz
- `  212 MB`  Spy x Family/Spy x Family v01 (2020) (Goldenagato).cbz

### mindfield — v1  *(volume)*

- `  213 MB`  Mindfield (000-006+)(2010-2012)(digital)(Minutemen-Excelsior)/Mindfield Vol. 01 (2012) (digital) (Minutemen-Excelsior).cbz
- `  211 MB`  Mindfield (000-006+)(2010-2012)(digital)(Minutemen-Excelsior)/Mindfield v01 (2011).cbz

### 03 b.p.r.d. plague of frogs edition — v1  — identical size  *(volume)*

- `  212 MB`  Hellboy/Hellboy in reading order/03 B.P.R.D. Plague of Frogs - OMNIBUS EDITION Vol. 1 (2014) ComixLedger.cbz
- `  212 MB`  Hellboy/03 B.P.R.D. Plague of Frogs - OMNIBUS EDITION Vol. 1 (2014) ComixLedger.cbz

### bronx kill  — identical size  *(issue)*

- `  141 MB`  Vertigo Crime (Collection) (2009-2011)/The Bronx Kill (2009) (Minutemen-DTs).cbr
- `  141 MB`  The Bronx Kill (2009) (Minutemen-DTs).cbr
- `  141 MB`  Bronx Kill, The (Vertigo)(2009)(c)/The Bronx Kill (2009) (Minutemen-DTs).cbr

### knock em dead  — identical size  *(issue)*

- `  211 MB`  Knock Em Dead (2020)/Knock Em Dead (2020).cbz
- `  211 MB`  Aftershock comics/Knock Em Dead (2020).cbz

### abe sapien — v4  — identical size  *(volume)*

- `  211 MB`  Hellboy/Abe Sapien TPBs/Abe Sapien v04 - The Shape of Things to Come (2014).cbr
- `  211 MB`  Abe Sapien/Abe Sapien v04 - The Shape of Things to Come (2014) (digital) (Son of Ultron-Empire).cbr

### lodger  *(issue)*

- `  220 MB`  Lodger (2018)/The Lodger (2013) (digital) (Minutemen-dask).cbr
- `  202 MB`  Stray Bullets/Lodger (David Lapham) (2018).cbz

### where monsters lie cull de sac  — identical size  *(issue)*

- `  210 MB`  Where Monsters Lie/Where Monsters Lie - Cull-de-Sac (2025) (Collection) (Dark Horse) (Digital-HD) (LeDuch).cbz
- `  210 MB`  Ice Cream Man (2020)/Where Monsters Lie - Cull-de-Sac (2025) (Collection) (Dark Horse) (Digital-HD) (LeDuch).cbz

### avengers & champions worlds collide  — identical size  *(issue)*

- `  209 MB`  Avengers/Avengers Vol. 07 (001-011,672-690)(2017-2018)(digital)/Avengers & Champions - Worlds Collide (2018) (Digital) (Kileko-Empire).cbr
- `  209 MB`  Avengers/Avengers & Champions - Worlds Collide (2018) (Digital) (Kileko-Empire).cbr

### 07 b.p.r.d.  — identical size  *(issue)*

- `  208 MB`  Hellboy/Hellboy in reading order/07 B.P.R.D. 1946-1948 - OMNIBUS EDITION (2016) ComixLedger.cbz
- `  208 MB`  Hellboy/07 B.P.R.D. 1946-1948 - OMNIBUS EDITION (2016) ComixLedger.cbz

### leviathan  *(issue)*

- `  180 MB`  Leviathan (2018).cbz
- `   69 MB`  Edington - D Israeli/Leviathan (Edington, D Israeli)(2010) (digital) (Ampersand).cbz
- `   69 MB`  Edington - D Israeli/Leviathan (2010) (digital) (Ampersand).cbz
- `   63 MB`  2000AD - Collections /Leviathan (2010) (digital) (Ampersand).cbr
- `   33 MB`  2000AD - Collections /Leviathan (Dan Dare 2000AD Remix).cbr

### batman and robin — v2  — identical size  *(volume)*

- `  207 MB`  Grant Morrison/Batman and Robin v02 - Batman vs. Robin (2010) (Digital) (Zone-Empire).cbr
- `  207 MB`  Batman/Batman and Robin v02 - Batman vs. Robin (2010) (Digital) (Zone-Empire).cbr

### essential judge dredd origins  — identical size  *(issue)*

- `  205 MB`  Judge Dredd The Megazine/Essential Judge Dredd - Origins (2021) (digital) (Torquemada).cbr
- `  205 MB`  Judge Dredd - Collections/Essential Judge Dredd/Essential Judge Dredd - Origins (2021) (digital) (Torquemada).cbr

### abe sapien — v3  — identical size  *(volume)*

- `  205 MB`  Hellboy/Abe Sapien TPBs/Abe Sapien v03 - Dark and Terrible and the New Race of Man (2013).cbr
- `  205 MB`  Abe Sapien/Abe Sapien v03 - Dark and Terrible and the New Race of Man (2013) (digital) (Son of Ultron-Empire).cbr

### hellboy bones of giants  *(issue)*

- `  216 MB`  Hellboy/Hellboy - The Bones of Giants (2022) (digital) (Son of Ultron II-Empire).cbr
- `  190 MB`  Hellboy/Hellboy - The Bones of Giants (2022) (digital) (Son of Ultron-Empire).cbr

### abe sapien — v5  — identical size  *(volume)*

- `  203 MB`  Hellboy/Abe Sapien TPBs/Abe Sapien v05 - Sacred Places (2015).cbr
- `  203 MB`  Abe Sapien/Abe Sapien v05 - Sacred Places (2015) (digital) (Son of Ultron-Empire).cbr

### nuclear family  — identical size  *(issue)*

- `  203 MB`  Nuclear Family (2021)/Nuclear Family (2021).cbz
- `  203 MB`  Aftershock comics/Nuclear Family (2021).cbz

### batman and robin — v1  — identical size  *(volume)*

- `  202 MB`  Grant Morrison/Batman and Robin v01 - Batman Reborn (2010) (Digital) (Zone-Empire).cbr
- `  202 MB`  Batman/Batman and Robin v01 - Batman Reborn (2010) (Digital) (Zone-Empire).cbr

### ballad of halo jones  *(issue)*

- `  331 MB`  2000AD - Collections /The Ballad of Halo Jones/The Ballad of Halo Jones (2013) (digital) (Ampersand).cbr
- `   72 MB`  Alan Moore/Alan Moore Collection I- English Invasion/Alan Moore Collection III- 2000 AD/2000 AD/2000 AD- Collections/The Ballad of Halo Jones.cbr

### latah  — identical size  *(issue)*

- `  201 MB`  Latah (2023) (digital) (Mr Norrell-Empire).cbr
- `  201 MB`  Europe Comics (Collection)/Latah (2023) (digital) (Mr Norrell-Empire).cbr

### chill  — identical size  *(issue)*

- `  134 MB`  Vertigo Crime (Collection) (2009-2011)/The Chill (2009) (Minutemen-DTs).cbr
- `  134 MB`  The Chill (2009) (Minutemen-DTs).cbr
- `  134 MB`  Chill, The (Vertigo)(2009)(c)/The Chill (2009) (Minutemen-DTs).cbr

### 12 hellboy — v4  — identical size  *(volume)*

- `  200 MB`  Hellboy/Hellboy in reading order/12 Hellboy Omnibus v04 - Hellboy in Hell (2018) (digital) (Son of Ultron-Empire).cbr
- `  200 MB`  Hellboy/12 Hellboy Omnibus v04 - Hellboy in Hell (2018) (digital) (Son of Ultron-Empire).cbr

### from hell  *(issue)*

- `  200 MB`  Alan Moore/Alan Moore Essentials/Alan Moore 1996- From Hell/From Hell .cbr
- `  200 MB`  Alan Moore/From Hell/From Hell.cbz

### miles to go  — identical size  *(issue)*

- `  199 MB`  Miles to Go (2020) /Miles to Go (2020) .cbz
- `  199 MB`  Aftershock comics/Miles to Go (2020) .cbz

### heavy metal — v23 — #06  — identical size  *(volume)*

- `  100 MB`  Heavy Metal/Heavy Metal Vols 01-35 (1977-2012)/Heavy Metal v23 06 (2000-01) (c2c) (Lazarus & Bluenaga).cbz
- `  100 MB`  Heavy Metal/Heavy Metal Vols 01-35 (1977-2012)/Heavy Metal v23 06 (2000-01) (c2c) (Lazarus %26 Bluenaga).cbz
- `  100 MB`  Heavy Metal/01. Main Series/Heavy Metal v23 06 (2000-01) (c2c) (Lazarus & Bluenaga).cbz
- `  100 MB`  Heavy Metal/01. Main Series/Heavy Metal v23 06 (2000-01) (c2c) (Lazarus %26 Bluenaga).cbz

### legend of shadow clan — v1  *(volume)*

- `  198 MB`  Legend of the Shadow Clan (001-005+)(2013-2014)(digital)(Minutemen-Excelsior)/Legend of the Shadow Clan Vol. 01 (2014) (digital) (Minutemen-Excelsior).cbz
- `  196 MB`  Legend of the Shadow Clan (001-005+)(2013-2014)(digital)(Minutemen-Excelsior)/Legend of the Shadow Clan v01 (2013).cbz

### eleanor & egret  — identical size  *(issue)*

- `  196 MB`  Eleanor & The Egret (001-005)(2017)(digital)(dargh-Empire)/Eleanor & The Egret (001-005)(2017)(digital)(dargh-Empire).cbz
- `  196 MB`  Aftershock comics/Eleanor & The Egret (001-005)(2017)(digital)(dargh-Empire).cbz

### koshchei in hell  — identical size  *(issue)*

- `  194 MB`  Koshchei in Hell (2023) (digital) (Son of Ultron-Empire).cbr
- `  194 MB`  Hellboy/Koshchei in Hell (2023) (digital) (Son of Ultron-Empire).cbr

### civil war road to civil war  — identical size  *(issue)*

- `  194 MB`  Civil War Event (001-007+Tie-Ins,Trades&Extras)(2006-2008)(digital)/Trades/Civil War - The Road To Civil War (2007) (digital) (Minutemen-Thoth).cbz
- `  194 MB`  Civil War Event (001-007+Tie-Ins,Trades&Extras)(2006-2008)(digital)/Civil War - The Road To Civil War (2007) (digital) (Minuteman-Thoth).cbz

### my date with monsters  — identical size  *(issue)*

- `  194 MB`  My Date With Monsters (2021)/My Date With Monsters (2021).cbz
- `  194 MB`  Aftershock comics/My Date With Monsters (2021).cbz

### batman and robin — v3  — identical size  *(volume)*

- `  193 MB`  Grant Morrison/Batman and Robin v03 - Batman and Robin Must Die! (2011) (Digital) (Zone-Empire).cbr
- `  193 MB`  Batman/Batman and Robin v03 - Batman and Robin Must Die! (2011) (Digital) (Zone-Empire).cbr

### iron man noir  *(issue)*

- `  222 MB`  Iron Man/Iron Man Noir (2011) (Digital4K-CaptainMarx).cbz
- `  161 MB`  Marvel Noir (2009-2011)(digital)/Iron Man - Noir (001-004)(2010)(digital)(G85-Empire).cbz

### gone  *(issue)*

- `  195 MB`  Gone/Gone (2024) (DSTLRY) (digital) (DrVink-HD-DCP) (RC).cbz
- `  187 MB`  Gone/Gone (2024) (Digital) (Mephisto-Empire).cbr

### hardcore — v1  *(volume)*

- `  194 MB`  Hardcore (2020)/Hardcore v01 (2021) (Fan Made TPB).cbr
- `  188 MB`  Hardcore (2020)/Hardcore v01 (2019) (Digital) (DR & Quinch-Empire).cbr

### aloha, hawaiian dick — #01  — identical size  *(issue)*

- `  190 MB`  Hawaiian Dick/Aloha, Hawaiian Dick (001-005) (2016)/Aloha, Hawaiian Dick (001-005) (2016)/Aloha, Hawaiian Dick 01.cbz
- `  190 MB`  Aster Blistok/Le Vagabond des Limbes/Aloha, Hawaiian Dick (001-005) (2016)/Aloha, Hawaiian Dick 01.cbz

### abe sapien — v6  — identical size  *(volume)*

- `  190 MB`  Hellboy/Abe Sapien TPBs/Abe Sapien v06 - A Darkness So Great (2015) (digital).cbr
- `  190 MB`  Abe Sapien/Abe Sapien v06 - A Darkness So Great (2015) (digital) (Son of Ultron-Empire).cbr

### star trek next generation hive  — identical size  *(issue)*

- `  190 MB`  Star Trek/Star Trek The Next Generation Hive (TPB)(2013)(Digital)(TLK-EMPIRE-HD).cbr
- `  190 MB`  Star Trek/Star Trek The Next Generation - Hive (2012-2013) (Digital) (TLK-EMPIRE-HD)/Star Trek The Next Generation - Hive (2013) (Digital) (TLK-EMPIRE-HD).cbr

### insurrection — v1  — identical size  *(volume)*

- `  190 MB`  Insurrection/Insurrection v01 (2013) (digital) (Torquemada).cbr
- `  190 MB`  2000AD - Collections /Insurrection/Insurrection v01 (2013) (digital) (Torquemada).cbr

### color of air  — identical size  *(issue)*

- `  127 MB`  Heavy Metal/The Color of Air (Heavy Metal compilation).cbr
- `  127 MB`  Heavy Metal/Heavy Metal Presents/The Color of Air (Heavy Metal compilation).cbr
- `  127 MB`  Heavy Metal/03. Extras/The Color of Air (Enki Bilal - Heavy Metal compilation).cbr

### aloha, hawaiian dick — #02  — identical size  *(issue)*

- `  189 MB`  Hawaiian Dick/Aloha, Hawaiian Dick (001-005) (2016)/Aloha, Hawaiian Dick (001-005) (2016)/Aloha, Hawaiian Dick 02.cbz
- `  189 MB`  Aster Blistok/Le Vagabond des Limbes/Aloha, Hawaiian Dick (001-005) (2016)/Aloha, Hawaiian Dick 02.cbz

### yiu — v3  — identical size  *(volume)*

- `  189 MB`  Yiu/Yiu v03 - Assassaints (2016) (digital) (The Magicians-Empire).cbr
- `  189 MB`  Soleil (Europe)/Yiu/Yiu v03 - Assassaints (2016) (digital) (The Magicians-Empire).cbr

### chicken devil  — identical size  *(issue)*

- `  187 MB`  Chicken Devil (2021)/Chicken Devil (2021).cbz
- `  187 MB`  Aftershock comics/Chicken Devil (2021).cbz

### heavy metal — #278  *(issue)*

- `  192 MB`  Heavy Metal/01. Main Series/Heavy Metal 278(F)(2016)(Digital)(TLK-EMPIRE-HD).cbr
- `  182 MB`  Heavy Metal/01. Main Series/Heavy Metal 278 (2016) (digital, without the gallery) (The Magicians-Empire).cbr

### bunny mask  — identical size  *(issue)*

- `  187 MB`  Bunny Mask (2021)/Bunny Mask (2021).cbz
- `  187 MB`  Aftershock comics/Bunny Mask (2021).cbz

### chew — v10  — identical size  *(volume)*

- `  186 MB`  Chew/Chew v10 - Blood Puddin_ (2015) GetComics.INFO.cbr
- `  186 MB`  Chew/Chew v10 - Blood Puddin' (2015) GetComics.INFO.cbr

### broken pieces — v1  *(volume)*

- `  187 MB`  Broken Pieces (000-005+)(2011-2013)(digital)(Minutemen-Excelsior)/Broken Pieces Vol. 01 (2013) (digital) (Minutemen-Excelsior).cbz
- `  185 MB`  Broken Pieces (000-005+)(2011-2013)(digital)(Minutemen-Excelsior)/Broken Pieces v01 (2012).cbz

### dead day  — identical size  *(issue)*

- `  186 MB`  Dead Day (2020)/Dead Day (2020).cbz
- `  186 MB`  Aftershock comics/Dead Day (2020).cbz

### fraternity  *(issue)*

- `  188 MB`  Humanoids (Europe)/Fraternity (Humanoids 2022) (webrip) (MagicMan-DCP).cbz
- `  183 MB`  Fraternity (2018) (digital) .cbr

### scars  — identical size  *(issue)*

- `  185 MB`  Warren Ellis/Scars (2015) (Digital) (EJGriffin-Empire).cbz
- `  185 MB`  Scars (2015) (Digital) (EJGriffin-Empire).cbz

### heavy metal — v15 — #06  *(volume)*

- `  147 MB`  Heavy Metal/Heavy Metal Vols 01-35 (1977-2012)/Heavy Metal v15 06 (1992).cbz
- `  147 MB`  Heavy Metal/01. Main Series/Heavy Metal v15 06 (1992).cbz
- `   76 MB`  Heavy Metal/01. Main Series/Heavy Metal v15 06 (1992-01).cbr

### chew — v1  — identical size  *(volume)*

- `  184 MB`  Chew/Chew v01 - Taster_s Choice (2009) GetComics.INFO.cbr
- `  184 MB`  Chew/Chew v01 - Taster's Choice (2009) GetComics.INFO.cbr

### yiu — v4  — identical size  *(volume)*

- `  184 MB`  Yiu/Yiu v04 - Pray That She Dies (2016) (digital) (The Magicians-Empire).cbr
- `  184 MB`  Soleil (Europe)/Yiu/Yiu v04 - Pray That She Dies (2016) (digital) (The Magicians-Empire).cbr

### almost american  *(issue)*

- `  205 MB`  Almost American/Almost American (2021) .cbz
- `  156 MB`  Almost American/Almost American (2021) (Fan-Made TPB).cbr

### abe sapien — v2  — identical size  *(volume)*

- `  181 MB`  Hellboy/Abe Sapien TPBs/Abe Sapien v02 - The Devil Does Not Jest and Other Stories (2012).cbr
- `  181 MB`  Abe Sapien/Abe Sapien v02 - The Devil Does Not Jest and Other Stories (2012) (digital) (Son of Ultron-Empire).cbr

### blasfamous hardcover  — identical size  *(issue)*

- `  180 MB`  Mirka Andolfo/Blasfamous - Hardcover (2024) (digital) (tomjoad).cbz
- `  180 MB`  Blasfamous/Blasfamous - Hardcover (2024) (digital) (tomjoad).cbz

### lawless — v4  *(volume)*

- `  222 MB`  Dan Abnett/Lawless v04 - Boom Town.cbz
- `  137 MB`  2000AD - Collections /Lawless/Lawless v04 - Boom Town (2022) (digital) (Torquemada).cbr

### olympia  *(issue)*

- `  272 MB`  Olympia (2020) (Digital) (DR & Quinch-Empire).cbr
- `   85 MB`  Europe Comics (Collection)/Olympia (2016) (digital-Empire).cbr

### love bunglers  — identical size  *(issue)*

- `  177 MB`  The Love Bunglers (2014) (digital-Empire).cbr
- `  177 MB`  Hernandez brothers/Love and Rockets/The Love Bunglers (2014) (digital-Empire).cbr

### order — v1  — identical size  *(volume)*

- `  177 MB`  The Order v01 - Die Mensch Maschine (2017) (digital) (Torquemada).cbr
- `  177 MB`  2000AD - Collections /The Order v01 - Die Mensch Maschine (2017) (digital) (Torquemada).cbr

### heavy metal — #259  *(issue)*

- `  205 MB`  Heavy Metal/01. Main Series/Heavy Metal 259(2012)(c2c)(JLBDScan).cbr
- `  146 MB`  Heavy Metal/01. Main Series/Heavy Metal 259 (2012-03) (c2c).cbr

### batman time and batman  — identical size  *(issue)*

- `  175 MB`  Grant Morrison/Batman - Time and the Batman (2011) (Digital) (Zone-Empire).cbr
- `  175 MB`  Batman/Batman - Time and the Batman (2011) (Digital) (Zone-Empire).cbr

### star trek assignment earth  — identical size  *(issue)*

- `  174 MB`  Star Trek/Star Trek Assignment Earth (TPB)(2014)(Digital)(TLK-EMPIRE-HD).cbr
- `  174 MB`  Star Trek/Star Trek - Assignment - Earth (2008)/Star Trek - Assignment Earth (TPB) (2014) (Digital) (TLK-EMPIRE-HD).cbr

### spy x family — v3  — identical size  *(volume)*

- `  174 MB`  Spy x Family/Spy x Family v03 (2020) (Digital) (LuCaZ).cbz
- `  174 MB`  Manga/Spy-x-family/Spy x Family v03 (2020) (Digital) (LuCaZ).cbz

### spy x family — v4  — identical size  *(volume)*

- `  173 MB`  Spy x Family/Spy x Family v04 (2021) (Digital) (Shizu).cbz
- `  173 MB`  Manga/Spy-x-family/Spy x Family v04 (2021) (Digital) (Shizu).cbz

### hardcore — v2  *(volume)*

- `  180 MB`  Hardcore (2020)/Hardcore v02 - Reloaded (2020) (Digital) (DR & Quinch-Empire).cbr
- `  165 MB`  Hardcore (2020)/Hardcore v02 - Reloaded (2021) (Fan Made TPB).cbr

### aloha, hawaiian dick — #04  — identical size  *(issue)*

- `  171 MB`  Hawaiian Dick/Aloha, Hawaiian Dick (001-005) (2016)/Aloha, Hawaiian Dick (001-005) (2016)/Aloha, Hawaiian Dick 04.cbz
- `  171 MB`  Aster Blistok/Le Vagabond des Limbes/Aloha, Hawaiian Dick (001-005) (2016)/Aloha, Hawaiian Dick 04.cbz

### scarlet traces — v3  — identical size  *(volume)*

- `  171 MB`  Scarlet Traces/Scarlet Traces v03 (2022).cbr
- `  171 MB`  2000AD - Collections /Scarlet Traces/Scarlet Traces v03 (2021) (digital) (Torquemada).cbr

### john carpenter's tales of science fiction surviving nuclear attack  *(issue)*

- `  196 MB`  John Carpenter's Tales of Science Fiction/John Carpenter's Tales of Science Fiction - SURVIVING NUCLEAR ATTACK (2020) (digital) (DrVink-HD-DCP).cbz
- `  145 MB`  John Carpenter's Tales of Science Fiction/John Carpenter's Tales of Science Fiction - Surviving Nuclear Attack  (2020).cbr

### fables — #1001  *(issue)*

- `  267 MB`  Fables/Fables (v01 - v22) (Digital TPB)/Fables - 1001 Nights of Snowfall (2006) (Digital TPB) (Nahga-Empire).cbr
- `   69 MB`  Fables/Specials/Fables - 1001 Nights of Snowfall.cbr

### maniac of new york  — identical size  *(issue)*

- `  168 MB`  Maniac of New York/Maniac of New York (2021) (Fan Made TPB).cbr
- `  168 MB`  Aftershock comics/Maniac of New York (2021) (Fan Made TPB).cbr

### eden  *(issue)*

- `  213 MB`  Humanoids (Europe)/Eden (Humanoids 2024) (webrip) (MagicMan-DCP).cbr
- `   61 MB`  Eden (One Shot) (2021) (Digital) (Mephisto-Empire).cbr
- `   61 MB`  Aftershock comics/Eden (One Shot) (2021) (Digital) (Mephisto-Empire).cbr

### essential judge dredd america  — identical size  *(issue)*

- `  167 MB`  Judge Dredd - Collections/Essential Judge Dredd - America (2020) (digital) (Torquemada).cbr
- `  167 MB`  Judge Dredd - Collections/Essential Judge Dredd/Essential Judge Dredd - America (2020) (digital) (Torquemada).cbr

### slaine — v8  — identical size  *(volume)*

- `  166 MB`  Slaine v08 - The Grail War (2013) (digital-SD) (Torquemada).cbr
- `  166 MB`  2000AD - Collections /SLAINE/Slaine v08 - The Grail War (2013) (digital SD) (Torquemada).cbr

### zaroff  — identical size  *(issue)*

- `  165 MB`  Europe Comics (Collection)/Zaroff (2019) (Europe Comics) (Digital-Empire).cbr
- `  165 MB`  Europe Comics (Collection)/Zaroff (2019) (Digital-Empire).cbr

### spy x family — v2  — identical size  *(volume)*

- `  165 MB`  Spy x Family/Spy x Family v02 (2020) (Digital) (LuCaZ).cbz
- `  165 MB`  Manga/Spy-x-family/Spy x Family v02 (2020) (Digital) (LuCaZ).cbz

### defenders beyond  *(issue)*

- `  270 MB`  Defenders/Defenders - Beyond (2022) (Digital) (Shan-Empire).cbz
- `   58 MB`  Defenders/Defenders Beyond (2023) (digital-SD) (Dakota Scanning).cbz

### bylines in blood  — identical size  *(issue)*

- `  164 MB`  Bylines in Blood (2022)/Bylines in Blood (2022).cbz
- `  164 MB`  Aftershock comics/Bylines in Blood (2022).cbz

### heavy metal — v35 — #05  — identical size  *(special)*

- `  162 MB`  Heavy Metal/Heavy Metal Vols 01-35 (1977-2012)/Heavy Metal v35 05 Special (2011-Summer) - War of the Worlds Special.cbr
- `  162 MB`  Heavy Metal/01. Main Series/Heavy Metal v35 05 Special (2011-Summer) - War of the Worlds Special.cbr

### love from shadows  — identical size  *(issue)*

- `  108 MB`  Love from the Shadows (2011) (digital-Empire).cbr
- `  108 MB`  Hernandez brothers/Love and Rockets/Love from the Shadows (2011) (digital-Empire).cbr
- `  108 MB`  Hernandez brothers/Gilbert Hernandez book digital editions/Love from the Shadows (2011) (digital-Empire).cbr

### george r. r. martin presents wild cards ante up  *(issue)*

- `  243 MB`  Wild/George R. R. Martin Presents Wild Cards - Ante Up (2025) (Digital) (dekabro-Empire).cbz
- `   79 MB`  George R.R. Martin/George R. R. Martin Presents Wild Cards - Ante Up (2025) (Digital) (Pyrate-DCP).cbz

### yiu — v2  — identical size  *(volume)*

- `  159 MB`  Yiu/Yiu v02 - The Promise I Made to You (2016) (digital) (The Magicians-Empire).cbr
- `  159 MB`  Soleil (Europe)/Yiu/Yiu v02 - The Promise I Made to You (2016) (digital) (The Magicians-Empire).cbr

### cross to bear  — identical size  *(issue)*

- `  159 MB`  Cross To Bear (2021)/Cross To Bear (2021).cbz
- `  159 MB`  Aftershock comics/Cross To Bear (2021).cbz

### ever way out  — identical size  *(issue)*

- `  159 MB`  Terry Moore/Ever - The Way Out (2020) (Digital) (DR & Quinch-Empire).cbr
- `  159 MB`  Ever - The Way Out (2020) (Digital) (DR & Quinch-Empire).cbr

### aloha, hawaiian dick — #05  — identical size  *(issue)*

- `  159 MB`  Hawaiian Dick/Aloha, Hawaiian Dick (001-005) (2016)/Aloha, Hawaiian Dick (001-005) (2016)/Aloha, Hawaiian Dick 05.cbz
- `  159 MB`  Aster Blistok/Le Vagabond des Limbes/Aloha, Hawaiian Dick (001-005) (2016)/Aloha, Hawaiian Dick 05.cbz

### heavy metal — v23 — #04  — identical size  *(volume)*

- `  158 MB`  Heavy Metal/Heavy Metal Vols 01-35 (1977-2012)/Heavy Metal v23 04 (1999-09).cbr
- `  158 MB`  Heavy Metal/01. Main Series/Heavy Metal v23 04 (1999-09).cbr

### wildstorm michael cray — v1  — identical size  *(volume)*

- `  158 MB`  Wild/Wildstorm - Michael Cray v01 (2018) (digital) (Son of Ultron-Empire).cbr
- `  158 MB`  The Wild Storm/Wildstorm - Michael Cray v01 (2018) (digital) (Son of Ultron-Empire).cbr

### heavy metal — v35 — #04  — identical size  *(volume)*

- `  157 MB`  Heavy Metal/Heavy Metal Vols 01-35 (1977-2012)/Heavy Metal v35 04 (2011-07).cbr
- `  157 MB`  Heavy Metal/01. Main Series/Heavy Metal v35 04 (2011-07).cbr

### luke cage noir  — identical size  *(issue)*

- `  156 MB`  Marvel Noir (2009-2011)(digital)/Luke Cage Noir (2010) (digital) (Minutemen-Faessla).cbz
- `  156 MB`  GG Studio (Collection) (2010-2012)/Marvel Noir (2009-2011)(digital)/Luke Cage Noir (2010) (digital) (Minutemen-Faessla).cbz

### doctor andromeda and kingdom of lost tomorrows  — identical size  *(issue)*

- `  156 MB`  Doctor Andromeda and the Kingdom of Lost Tomorrows (2021) (digital) (Son of Ultron-Empire).cbr
- `  156 MB`  Black Hammer/Doctor Andromeda and the Kingdom of Lost Tomorrows (2021) (digital) (Son of Ultron-Empire).cbr

### valerian — #5  *(volume)*

- `  290 MB`  Valerian and Laureline/Valerian - The Complete Collection 5 (2018) (Cinebook) (Digital-Empire).cbr
- `   21 MB`  Valerian and Laureline/Valerian - The Complete Collection 5 (2018) (Extract) (Cinebook) (Digital-Empire).cbr

### star trek deep space nine fool's gold  — identical size  *(issue)*

- `  155 MB`  Star Trek/Star Trek Deep Space Nine Fool's Gold (TPB)(2014)(Digital)(TLK-EMPIRE-HD).cbr
- `  155 MB`  Star Trek/Star Trek - Deep Space Nine (2009)/Star Trek - Deep Space Nine - Fool's Gold (2014) (Digital) (TLK-EMPIRE-HD).cbr

### colonized — v1  *(volume)*

- `  167 MB`  The Colonized (001-004+) (2013) (digital) (Minutemen-Rufio)/The Colonized v01 (2013).cbz
- `  142 MB`  The Colonized (001-004+) (2013) (digital) (Minutemen-Rufio)/The Colonized Vol. 01 (2013) (digital) (Minutemen-Rufio).cbz

### heavy metal — #269  *(issue)*

- `  224 MB`  Heavy Metal/01. Main Series/Heavy Metal 269(2014)(Digital)(TLK-EMPIRE-HD).cbr
- `   85 MB`  Heavy Metal/01. Main Series/Heavy Metal 269(2014)(c2c)(TLK-EMPIRE).cbr

### koshchei deathless  — identical size  *(issue)*

- `  154 MB`  Koshchei the Deathless (2018) (digital) (Son of Ultron-Empire).cbr
- `  154 MB`  Hellboy/Koshchei the Deathless (2018) (digital) (Son of Ultron-Empire).cbr

### heavy metal — v16 — #03  — identical size  *(volume)*

- `  154 MB`  Heavy Metal/Heavy Metal Vols 01-35 (1977-2012)/Heavy Metal v16 03 (1992) (null-DCP).cbz
- `  154 MB`  Heavy Metal/01. Main Series/Heavy Metal v16 03 (1992) (null-DCP).cbz

### human target — v2  *(volume)*

- `  270 MB`  The Human Target/The Human Target v02 (2022).cbz
- `   36 MB`  The Human Target/Human Target v02 (2003).cbz

### layla. a tale of scarlet swamp  — identical size  *(issue)*

- `  153 MB`  Scarlet (2018)/Layla. A Tale of the Scarlet Swamp (2019) (Digital-Empire).cbr
- `  153 MB`  Richard Sala/Layla. A Tale of the Scarlet Swamp (2019) (Europe Comics) (Digital-Empire).cbr

### aloha, hawaiian dick — #03  — identical size  *(issue)*

- `  153 MB`  Hawaiian Dick/Aloha, Hawaiian Dick (001-005) (2016)/Aloha, Hawaiian Dick (001-005) (2016)/Aloha, Hawaiian Dick 03.cbz
- `  153 MB`  Aster Blistok/Le Vagabond des Limbes/Aloha, Hawaiian Dick (001-005) (2016)/Aloha, Hawaiian Dick 03.cbz

### heavy metal — v35 — #07  — identical size  *(volume)*

- `  152 MB`  Heavy Metal/Heavy Metal Vols 01-35 (1977-2012)/Heavy Metal v35 07 (2011-11).cbr
- `  152 MB`  Heavy Metal/01. Main Series/Heavy Metal v35 07 (2011-11).cbr

### civil war punisher war journal  *(issue)*

- `  168 MB`  Punisher Max/Civil War - Punisher War Journal (2015) (Digital) (F) (Kileko-Empire).cbz
- `  134 MB`  Civil War Event (001-007+Tie-Ins,Trades&Extras)(2006-2008)(digital)/Trades/Civil War - Punisher War Journal (2007) (Digital TPB) (Kileko-Empire).cbr

### scene of crime  — identical size  *(issue)*

- `  151 MB`  Vertigo Crime (Collection) (2009-2011)/Scene of the Crime (2012) (Digital GN) (Fawkes-Empire).cbr
- `  151 MB`  Image comics/Scene of the Crime (2012) (Digital GN) (Fawkes-Empire).cbr

### batman and harley quinn  *(issue)*

- `  111 MB`  Harley Quinn/Batman and Harley Quinn (2018) (digital) (Son of Ultron-Empire).cbr
- `  111 MB`  Batman/Batman and Harley Quinn (2018) (digital) (Son of Ultron-Empire).cbr
- `   79 MB`  Harley Quinn/Batman and Harley Quinn  (2017).cbz

### judge dredd megazine — #385  — identical size  *(issue)*

- `  149 MB`  Judge Dredd The Megazine/Judge Dredd Megazine v5 (201-400)(2002-ongoing)/Judge Dredd Megazine 385 (2017) (digital) (juvecube).cbr
- `  149 MB`  2000AD prog/2000AD Judge Dredd January - June 2017 (juvecube)/Judge Dredd The Megazine 380-385/Judge Dredd The Megazine 385 (2017) (juvecube).cbr

### insufferable — v2  *(volume)*

- `  258 MB`  Insufferable/Insufferable v2 (01-32) (2013)/Insufferable v2 (01-32) (2013).cbz
- `   39 MB`  Insufferable/Insufferable - Extras (2012-2013)/Insufferable v02 (2012) (digital) (HD) (Son of Ultron-Empire).cbr

### yiu — v5  — identical size  *(volume)*

- `  149 MB`  Yiu/Yiu v05 - The Fall of the Evangelist Empire (2016) (digital) (The Magicians-Empire).cbr
- `  149 MB`  Soleil (Europe)/Yiu/Yiu v05 - The Fall of the Evangelist Empire (2016) (digital) (The Magicians-Empire).cbr

### zaucer of zilk  — identical size  *(volume)*

- `  148 MB`  Zaucer of Zilk Complete (2013) (digital) (Minutemen-InnerDemons).cbr
- `  148 MB`  2000AD - Collections /Zaucer of Zilk Complete (2013) (digital) (Minutemen-InnerDemons).cbr

### fireborn — #001  *(issue)*

- `  217 MB`  Fireborn/Fireborn 001 (2026) (Digital) (Zone-Empire).cbr
- `   78 MB`  Fireborn/Fireborn 001 (2026) (Series) (Image Comics) (Digital) (LeDuch).cbz

### heavy metal — v35 — #06  — identical size  *(volume)*

- `  147 MB`  Heavy Metal/Heavy Metal Vols 01-35 (1977-2012)/Heavy Metal v35 06 (2011-09).cbr
- `  147 MB`  Heavy Metal/01. Main Series/Heavy Metal v35 06 (2011-09).cbr

### yiu — v1  — identical size  *(volume)*

- `  147 MB`  Yiu/Yiu v01 - In Hell (2016) (digital) (The Magicians-Empire).cbr
- `  147 MB`  Soleil (Europe)/Yiu/Yiu v01 - In Hell (2016) (digital) (The Magicians-Empire).cbr

### abe sapien — v1  — identical size  *(volume)*

- `  145 MB`  Hellboy/Abe Sapien TPBs/Abe Sapien v01 - The Drowning (2008).cbr
- `  145 MB`  Abe Sapien/Abe Sapien v01 - The Drowning (2008) (digital) (Minutemen-Azkaban).cbr

### defenders there are no rules  *(issue)*

- `  219 MB`  Defenders/Defenders - There Are No Rules (2022) (Digital) (EJGriffin-Empire).cbz
- `   72 MB`  Defenders/Defenders - There Are No Rules (2022) (Digital-SD) (Dakota Scanning).cbz

### days — v2  *(volume)*

- `  171 MB`  Giant Days/Giant Days v02 (2017).cbz
- `  118 MB`  Giant Days/Giant Days Vol. 02 (2016) (digital) (Minutemen-Slayer).cbr

### fluorescent black  *(issue)*

- `  149 MB`  Heavy Metal/Related_Publications/Fluorescent Black (2010) (Heavy Metal).cbr
- `  140 MB`  Fluorescent Black (2010 GN) (Pudgy).cbr

### marble season  — identical size  *(issue)*

- `  144 MB`  Marble Season (2015) (digital) (FatNerd).cbz
- `  144 MB`  Hernandez brothers/Marble Season (2015) (digital) (FatNerd).cbz

### judge dredd megazine — #382  — identical size  *(issue)*

- `  144 MB`  Judge Dredd The Megazine/Judge Dredd Megazine v5 (201-400)(2002-ongoing)/Judge Dredd Megazine 382 (2017) (digital) (juvecube).cbr
- `  144 MB`  2000AD prog/2000AD Judge Dredd January - June 2017 (juvecube)/Judge Dredd The Megazine 380-385/Judge Dredd The Megazine 382 (2017) (juvecube).cbr

### genetics at heart  — identical size  *(issue)*

- `  144 MB`  Genetics at Heart (2023) (digital) (Mr Norrell-Empire).cbr
- `  144 MB`  Europe Comics (Collection)/Genetics at Heart (2023) (digital) (Mr Norrell-Empire).cbr

### burne out  — identical size  *(issue)*

- `  144 MB`  Europe Comics (Collection)/Burne Out (18 ) (2022) (Scanlation) (phillywilly-Empire).cbr
- `  144 MB`  Burne Out (18+) (2022) (Scanlation) (phillywilly-Empire).cbr

### wolverine noir  — identical size  *(issue)*

- `  143 MB`  Marvel Noir (2009-2011)(digital)/Wolverine Noir (2010) (digital) (G85-Empire).cbr
- `  143 MB`  GG Studio (Collection) (2010-2012)/Marvel Noir (2009-2011)(digital)/Wolverine Noir (2010) (digital) (G85-Empire).cbr

### tikitis — v1  *(volume)*

- `  105 MB`  Tikitis T01 The Brains War (digital-onlyorm).cbz
- `  105 MB`  Humanoids (Europe)/Tikitis T01 (03) The Brains War (digital-onlyorm).cbz
- `   75 MB`  Humanoids (Europe)/The Tikitis (v01-v03) (2010) (digital) (The Magicians-Empire)/The Tikitis v01 - The Brains War (2010) (digital) (The Magicians-Empire).cbr

### heavy metal — v13 — #05  — identical size  *(volume)*

- `  142 MB`  Heavy Metal/Heavy Metal Vols 01-35 (1977-2012)/Heavy Metal v13 05 (1989-11).cbr
- `  142 MB`  Heavy Metal/01. Main Series/Heavy Metal v13 05 (1989-11).cbr

### coraline  — identical size  *(volume)*

- `  140 MB`  Neil Gaiman Library/Coraline HC (2008) (Minutemen-Y2K).cbr
- `  140 MB`  Coraline HC (2008) (Minutemen-Y2K).cbr

### heavy metal — v25 — #002  — identical size  *(volume)*

- `  140 MB`  Heavy Metal/Heavy Metal Vols 01-35 (1977-2012)/Heavy Metal v25 002 (2001) (null-DCP).cbz
- `  140 MB`  Heavy Metal/01. Main Series/Heavy Metal v25 002 (2001) (null-DCP).cbz

### well  *(issue)*

- `  192 MB`  The Well/The Well (2025) (digital) (Mr Norrell-Empire).cbr
- `   85 MB`  The Well/The Well (2022) (digital) (DrVink).cbz

### hello darkness — #020  *(issue)*

- `  154 MB`  Hello Darkness (2024)/Hello Darkness 020 (2026) (Digital Rip) (Hourman-DCP).cbr
- `  122 MB`  Hello Darkness/Hello Darkness 020 (2026) (Digital Rip) (Hourman-DCP).cbr

### punisher noir  — identical size  *(issue)*

- `  137 MB`  Marvel Noir (2009-2011)(digital)/Punisher Noir (2010) (digital) (Minutemen-Slayer).cbr
- `  137 MB`  GG Studio (Collection) (2010-2012)/Marvel Noir (2009-2011)(digital)/Punisher Noir (2010) (digital) (Minutemen-Slayer).cbr

### judge dredd megazine — #383  — identical size  *(issue)*

- `  137 MB`  Judge Dredd The Megazine/Judge Dredd Megazine v5 (201-400)(2002-ongoing)/Judge Dredd Megazine 383 (2017) (digital) (juvecube).cbr
- `  137 MB`  2000AD prog/2000AD Judge Dredd January - June 2017 (juvecube)/Judge Dredd The Megazine 380-385/Judge Dredd The Megazine 383 (2017) (juvecube).cbr

### heavy metal — v16 — #04  — identical size  *(volume)*

- `  137 MB`  Heavy Metal/Heavy Metal Vols 01-35 (1977-2012)/Heavy Metal v16 04 (1992) (null-DCP).cbz
- `  137 MB`  Heavy Metal/01. Main Series/Heavy Metal v16 04 (1992) (null-DCP).cbz

### heavy metal — #270  *(issue)*

- `  244 MB`  Heavy Metal/01. Main Series/Heavy Metal 270(2014)(Digital)(TLK-EMPIRE-HD).cbr
- `   29 MB`  Heavy Metal/01. Main Series/Heavy Metal 270(2014)(c2c)(SkyRat).cbr

### chance in hell  — identical size  *(issue)*

- `  136 MB`  Hernandez brothers/Love and Rockets/Chance in Hell (2007) (digital) (Mr Norrell-Empire).cbr
- `  136 MB`  Hernandez brothers/Chance in Hell (2007) (Hernandez) (Mr Norrell-Empire).cbr

### coyote and snake  *(issue)*

- `  175 MB`  Europe Comics (Collection)/The Coyote and the Snake (2022) (digital) (Mr Norrell-Empire).cbr
- `   95 MB`  Europe Comics (Collection)/The Coyote and the Snake (Europe Comics 2022) (webrip) (MagicMan-DCP).cbr

### house  *(issue)*

- `  184 MB`  The House (Paco Roca 2019) (digital-Empire).cbz
- `   86 MB`  House (2008) (digital) (Mr Norrell-Empire).cbr

### wildstorm michael cray — v2  — identical size  *(volume)*

- `  134 MB`  Wild/Wildstorm - Michael Cray v02 (2018) (digital) (Son of Ultron-Empire).cbr
- `  134 MB`  The Wild Storm/Wildstorm - Michael Cray v02 (2018) (digital) (Son of Ultron-Empire).cbr

### judge dredd megazine — #384  — identical size  *(issue)*

- `  133 MB`  Judge Dredd The Megazine/Judge Dredd Megazine v5 (201-400)(2002-ongoing)/Judge Dredd Megazine 384 (2017) (digital) (juvecube).cbr
- `  133 MB`  2000AD prog/2000AD Judge Dredd January - June 2017 (juvecube)/Judge Dredd The Megazine 380-385/Judge Dredd The Megazine 384 (2017) (juvecube).cbr

### devil on her shoulder edition  — identical size  *(issue)*

- `  132 MB`  Europe Comics (Collection)/Devil on Her Shoulder - Complete Edition (2023) (digital) (Mr Norrell-Empire).cbr
- `  132 MB`  Devil on Her Shoulder - Complete Edition (2023) (digital) (Mr Norrell-Empire).cbr

### paper girls — v1  *(volume)*

- `  208 MB`  Paper Girls/Paper Girls v01 (2016) (Digital) (Zone-Empire).cbr
- `   52 MB`  Paper Girls/Paper Girls - Book 01 (Art Gallery) (2017) (Digital-HD) (Danke-Empire).cbz

### love and rockets trading cards  *(issue)*

- `  249 MB`  Hernandez brothers/Love and Rockets/Love and Rockets Trading Cards (Fantagraphics)(500dpi tiffs - to print a3).cbr
- `   10 MB`  Hernandez brothers/Love and Rockets/Love and Rockets Trading Cards (Fantagraphics).cbr

### heavy metal — v22 — #03  *(volume)*

- `   89 MB`  Heavy Metal/Heavy Metal Vols 01-35 (1977-2012)/Heavy Metal v22 03 (1999-07) (c2c) (Lazarus-DCP).cbz
- `   89 MB`  Heavy Metal/01. Main Series/Heavy Metal v22 03 (1999-07) (c2c) (Lazarus-DCP).cbz
- `   82 MB`  Heavy Metal/01. Main Series/Heavy Metal V22 03 (1998-07) (c2c) (Lazarus-DCP).cbz

### heavy metal — v16 — #02  — identical size  *(volume)*

- `  129 MB`  Heavy Metal/Heavy Metal Vols 01-35 (1977-2012)/Heavy Metal v16 02 (1992) (null-DCP).cbz
- `  129 MB`  Heavy Metal/01. Main Series/Heavy Metal v16 02 (1992) (null-DCP).cbz

### judge dredd megazine — #381  — identical size  *(issue)*

- `  128 MB`  Judge Dredd The Megazine/Judge Dredd Megazine v5 (201-400)(2002-ongoing)/Judge Dredd Megazine 381 (2017) (digital) (juvecube).cbr
- `  128 MB`  2000AD prog/2000AD Judge Dredd January - June 2017 (juvecube)/Judge Dredd The Megazine 380-385/Judge Dredd The Megazine 381 (2017) (juvecube).cbr

### mean team  *(issue)*

- `  199 MB`  2000AD - Collections /Mean Team (2013) (digital) (DR & Quinch-Empire).cbr
- `   54 MB`  Mean Team (2013) (digital) (Torquemada).cbr

### cuba my revolution  *(issue)*

- `  126 MB`  Cuba My Revolution (Vertigo)(2010)(c)/Cuba-My Revolution (ctc).cbr
- `  126 MB`  Cuba My Revolution (Vertigo)(2010)(c)/Cuba - My Revolution (eng) (2011) (c2c) (Minutemen-DTs).cbz

### lawless — v2  — identical size  *(volume)*

- `  126 MB`  Dan Abnett/Lawless v02 - Long-Range War (2018) (digital) (Torquemada).cbr
- `  126 MB`  2000AD - Collections /Lawless/Lawless v02 - Long-Range War (2018) (digital) (Torquemada).cbr

### yiu — v7  — identical size  *(volume)*

- `  125 MB`  Yiu/Yiu v07 - Final Testament (2016) (digital) (The Magicians-Empire).cbr
- `  125 MB`  Soleil (Europe)/Yiu/Yiu v07 - Final Testament (2016) (digital) (The Magicians-Empire).cbr

### judge dredd megazine — #380  — identical size  *(issue)*

- `  124 MB`  Judge Dredd The Megazine/Judge Dredd Megazine v5 (201-400)(2002-ongoing)/Judge Dredd Megazine 380 (2017) (digital) (juvecube).cbr
- `  124 MB`  2000AD prog/2000AD Judge Dredd January - June 2017 (juvecube)/Judge Dredd The Megazine 380-385/Judge Dredd The Megazine 380 (2017) (juvecube).cbr

### heavy metal — v4 — #005  — identical size  *(volume)*

- `  122 MB`  Heavy Metal/Heavy Metal Vols 01-35 (1977-2012)/Heavy Metal v04 005 (1980) (null-DCP).cbz
- `  122 MB`  Heavy Metal/01. Main Series/Heavy Metal v04 005 (1980) (null-DCP).cbz

### moon face — #01  — identical size  *(issue)*

- `  122 MB`  Jodorowsky and Moebius/Moon Face (2018) /Moon Face 01 - The Wave Tamer (2018) (Humanoids) (Digital-Empire).cbr
- `  122 MB`  Humanoids (Europe)/Moon Face/Moon Face 01 - The Wave Tamer (2018) (Humanoids) (Digital-Empire).cbr

### shakara — v2  — identical size  *(volume)*

- `  122 MB`  Shakara (v01-v02)(2008-2012)(digital-SD)(Torquemada)/Shakara v02 - The Destroyer (2012) (digital-SD) (Torquemada).cbr
- `  122 MB`  2000AD - Collections /Shakara/Shakara v02 - The Destroyer (2012) (digital SD) (Torquemada).cbr

### sickness in family  *(issue)*

- `  122 MB`  A SICKNESS IN THE FAMILY (2010) (DC VERTIGO) (c2c).cbr
- `  122 MB`  Vertigo Crime (Collection) (2009-2011)/A Sickness in the Family (2010) (Minutemen-DTs).cbr

### spider man noir  — identical size  *(issue)*

- `  122 MB`  Marvel Noir (2009-2011)(digital)/Spider-Man Noir (2009) (Digital-Empire).cbr
- `  122 MB`  GG Studio (Collection) (2010-2012)/Marvel Noir (2009-2011)(digital)/Spider-Man Noir (2009) (Digital-Empire).cbr

### dark red — v2  — identical size  *(volume)*

- `  122 MB`  Dark Red (2019)/Dark Red v02 - Where Roads Lead (2022) (digital) (Son of Ultron-Empire).cbr
- `  122 MB`  Aftershock comics/Dark Red v02 - Where Roads Lead (2022) (digital) (Son of Ultron-Empire).cbr

### ballad of halo jones — v3  *(volume)*

- `  109 MB`  2000AD - Collections /The Ballad of Halo Jones/The Ballad of Halo Jones v03 (Color) (2018) (digital) (Torquemada).cbr
- `   44 MB`  Alan Moore/Halo Jones/The Ballad of Halo Jones Book 3.cbr
- `   44 MB`  Alan Moore/Alan Moore Collection I- English Invasion/Alan Moore Collection III- 2000 AD/2000 AD/2000 AD- Reprints/The Ballad Of Halo Jones/The Ballad Of Halo Jones Book #003 TPB.cbr
- `   44 MB`  2000AD prog/Alan Moore -2000AD/The Ballad of Halo Jones/The Ballad of Halo Jones Book 3.cbr

### moon face — #04  — identical size  *(issue)*

- `  121 MB`  Jodorowsky and Moebius/Moon Face (2018) /Moon Face 04 - The Woman from the Sky (2018) (Humanoids) (Digital-Empire).cbr
- `  121 MB`  Humanoids (Europe)/Moon Face/Moon Face 04 - The Woman from the Sky (2018) (Humanoids) (Digital-Empire).cbr

### 2000ad prog 2011  *(issue)*

- `  127 MB`  2000AD prog/2000AD prog 2011 (2016) (digital) (juvecube).cbr
- `   57 MB`  2000AD prog/Yearbooks & Specials/Yearbooks (2000-2015)/2000AD Prog 2011 (2010) (John Williams-DCP).cbr
- `   57 MB`  2000AD prog/2000AD (Specials, Annuals & Poster Progs + Extras)/2000AD Yearbooks & Specials (1977 - 2013)/2000AD Yearbooks (Prog 2000 - 2013)/2000AD Prog 2011.cbr

### heavy metal — v34 — #08  — identical size  *(volume)*

- `  120 MB`  Heavy Metal/Heavy Metal Vols 01-35 (1977-2012)/Heavy Metal v34 08 (2010) (Vague Prophet and Vapor Trail).cbr
- `  120 MB`  Heavy Metal/01. Main Series/Heavy Metal v34 08 (2010) (Vague Prophet and Vapor Trail).cbr

### apache delivery service  *(issue)*

- `  130 MB`  Apache Delivery Service (2022) (digital) (Son of Ultron-Empire).cbr
- `  109 MB`  Matt Kindt/Apache Delivery Service (2022) (Matt Kindt).cbz

### heavy metal — #271  *(issue)*

- `  212 MB`  Heavy Metal/01. Main Series/Heavy Metal 271(2014)(Digital)(TLK-EMPIRE-HD).cbr
- `   27 MB`  Heavy Metal/01. Main Series/Heavy Metal 271(2014)(c2c)(SkyRat).cbr

### heavy metal presents more than human  — identical size  *(issue)*

- `   80 MB`  Heavy Metal/Heavy Metal Presents/Heavy_Metal_Presents - More Than Human.cbr
- `   80 MB`  Heavy Metal/Heavy Metal Presents/Heavy Metal Presents - More Than Human (1978).cbr
- `   80 MB`  Heavy Metal/03. Extras/Heavy Metal Presents - More Than Human (1978).cbr

### god of tremors — #001  — identical size  *(issue)*

- `  119 MB`  God of Tremors 001 (2021) (Digital) (Mephisto-Empire).cbr
- `  119 MB`  Aftershock comics/God of Tremors 001 (2021) (Digital) (Mephisto-Empire).cbr

### anibal — v2  — identical size  *(volume)*

- `  119 MB`  Jodorowsky and Moebius/Anibal_5_v2_-_Nirvana_(2015)_(Digital)_(phillywilly-Empire).cbr
- `  119 MB`  Jodorowsky and Moebius/Anibal 5 Vol. 1 - 2 (2015)/Anibal 5 v2 - Nirvana (2015) (Digital) (phillywilly-Empire).cbr

### anibal — v1  — identical size  *(volume)*

- `  118 MB`  Jodorowsky and Moebius/Anibal_5_v1_-_Subterranean_Sexcapades_(2015)_(Digital)_(phillywilly-Empire).cbr
- `  118 MB`  Jodorowsky and Moebius/Anibal 5 Vol. 1 - 2 (2015)/Anibal 5 v1 - Subterranean Sexcapades (2015) (Digital) (phillywilly-Empire).cbr

### x men noir mark of cain  — identical size  *(issue)*

- `  118 MB`  Marvel Noir (2009-2011)(digital)/X-Men Noir - Mark of Cain (2010) (Digital) (Kileko-Empire).cbr
- `  118 MB`  GG Studio (Collection) (2010-2012)/Marvel Noir (2009-2011)(digital)/X-Men Noir - Mark of Cain (2010) (Digital) (Kileko-Empire).cbr

### shakara — v1  — identical size  *(volume)*

- `  117 MB`  Shakara (v01-v02)(2008-2012)(digital-SD)(Torquemada)/Shakara v01 - The Avenger (2008) (digital-SD) (Torquemada).cbr
- `  117 MB`  2000AD - Collections /Shakara/Shakara v01 - The Avenger (2008) (digital SD) (Torquemada).cbr

### yiu — v6  — identical size  *(volume)*

- `  116 MB`  Yiu/Yiu v06 - The Apocalypse or the Book of Revelations (2016) (digital) (The Magicians-Empire).cbr
- `  116 MB`  Soleil (Europe)/Yiu/Yiu v06 - The Apocalypse or the Book of Revelations (2016) (digital) (The Magicians-Empire).cbr

### heavy metal — v16 — #01  — identical size  *(volume)*

- `  116 MB`  Heavy Metal/Heavy Metal Vols 01-35 (1977-2012)/Heavy Metal v16 01 (1992) (null-DCP).cbz
- `  116 MB`  Heavy Metal/01. Main Series/Heavy Metal v16 01 (1992) (null-DCP).cbz

### star trek countdown  *(issue)*

- `  180 MB`  Star Trek/Star Trek - Countdown (2009) (digital) (The Magicians-Empire).cbr
- `   51 MB`  Star Trek/Star Trek Countdown (2009) (digital) (SD) (Minutemen-FlynnLives).cbr

### heavy metal — v24 — #02  — identical size  *(volume)*

- `  115 MB`  Heavy Metal/Heavy Metal Vols 01-35 (1977-2012)/Heavy Metal v24 02 (2000) (null-DCP).cbz
- `  115 MB`  Heavy Metal/01. Main Series/Heavy Metal v24 02 (2000) (null-DCP).cbz

### scattered pages  *(issue)*

- `  148 MB`  Europe Comics (Collection)/Scattered Pages (2022) (digital) (Mr Norrell-Empire).cbr
- `   80 MB`  Europe Comics (Collection)/Scattered Pages (Europe Comics 2022) (webrip) (MagicMan-DCP).cbr

### domestic yapoo  — identical size  *(issue)*

- `  114 MB`  Manga/Yapoo (Shotaro Ishinomori)/The Domestic Yapoo (Shotaro Ishinomori).cbr
- `  114 MB`  Manga/The Domestic Yapoo (Shotaro Ishinomori).cbr

### hearts of steel — #001  — identical size  *(issue)*

- `  113 MB`  Hearts of Steel 001 - Debree, Cyrano, and Me (2023) (digital) (Mr Norrell-Empire).cbr
- `  113 MB`  Europe Comics (Collection)/Hearts of Steel 001 - Debree, Cyrano, and Me (2023) (digital) (Mr Norrell-Empire).cbr

### miracleman — #016  *(issue)*

- `  119 MB`  Miracleman/Miracleman v1 (001-016) (2014-2015) GetComics.INFO/Miracleman 016 (2015) (Digital) (Zone-Empire).cbr
- `   54 MB`  Alan Moore/Alan Moore Essentials/Alan Moore 1984- Miracleman/Miracleman #016.cbr
- `   54 MB`  Alan Moore/Alan Moore Collection I- English Invasion/Alan Moore Collection III- 2000 AD/Miracleman/Miracleman/Miracleman #016.cbr

### little sister  *(issue)*

- `  146 MB`  Europe Comics (Collection)/Little Sister (2021) (Europe Comics).cbr
- `   80 MB`  Europe Comics (Collection)/Little Sister (Europe Comics 2021) (webrip) (MagicMan-DCP).cbr

### 2000ad prog 2012  *(issue)*

- `   71 MB`  2000AD prog/Yearbooks & Specials/Yearbooks (2000-2015)/2000AD Prog 2012 (2011) (digital).cbz
- `   71 MB`  2000AD prog/2000AD (Specials, Annuals & Poster Progs + Extras)/2000AD Yearbooks & Specials (1977 - 2013)/2000AD Yearbooks (Prog 2000 - 2013)/2000AD Prog 2012 (Digital).cbz
- `   40 MB`  2000AD prog/2000AD prog 2012 (2016) (digital) (juvecube).cbr
- `   40 MB`  2000AD prog/2000AD Judge Dredd January - June 2017 (juvecube)/2000AD progs 2012-2037/2000AD prog 2012 (2016) (juvecube).cbr

### heavy metal — v34 — #07  — identical size  *(volume)*

- `  111 MB`  Heavy Metal/Heavy Metal Vols 01-35 (1977-2012)/Heavy Metal v34 07 (2010) (Vague Prophet and Vapor Trail).cbr
- `  111 MB`  Heavy Metal/01. Main Series/Heavy Metal v34 07 (2010) (Vague Prophet and Vapor Trail).cbr

### lovestruck  — identical size  *(volume)*

- `  111 MB`  Lovestruck GN (2011) (digital-Gux&Leifman).cbr
- `  111 MB`  Image comics/Lovestruck GN (2011) (digital-Gux&Leifman).cbr

### hewligans haircut  — identical size  *(issue)*

- `  111 MB`  Hewligans Haircut (2017) (digital) (Ampersand).cbr
- `  111 MB`  2000AD - Collections /Hewligans Haircut (2017) (digital) (Ampersand).cbr

### judge dredd heavy metal dredd  — identical size  *(issue)*

- `  111 MB`  Judge Dredd - Collections/Judge Dredd - Heavy Metal Dredd (2009) (Digital SD) (Torquemada).cbr
- `  111 MB`  Heavy Metal/Judge Dredd - Heavy Metal Dredd (2009) (digital-SD) (Torquemada).cbr

### heavy metal — v2 — #10  — identical size  *(volume)*

- `   55 MB`  Heavy Metal/Heavy Metal Vols 01-35 (1977-2012)/Heavy Metal v02 10 (1979-02) (c2c) (Foyle-DCP&Darkside).cbr
- `   55 MB`  Heavy Metal/Heavy Metal Vols 01-35 (1977-2012)/Heavy Metal v02 10 (1979-02) (c2c) (Foyle-DCP%26Darkside).cbr
- `   55 MB`  Heavy Metal/01. Main Series/Heavy Metal v02 10 (1979-02) (c2c) (Foyle-DCP&Darkside).cbr
- `   55 MB`  Heavy Metal/01. Main Series/Heavy Metal v02 10 (1979-02) (c2c) (Foyle-DCP%26Darkside).cbr

### heavy metal — v2 — #11  — identical size  *(volume)*

- `   54 MB`  Heavy Metal/Heavy Metal Vols 01-35 (1977-2012)/Heavy Metal v02 11 (1979-03) (c2c) (Foyle-DCP&Darkside).cbr
- `   54 MB`  Heavy Metal/Heavy Metal Vols 01-35 (1977-2012)/Heavy Metal v02 11 (1979-03) (c2c) (Foyle-DCP%26Darkside).cbr
- `   54 MB`  Heavy Metal/01. Main Series/Heavy Metal v02 11 (1979-03) (c2c) (Foyle-DCP&Darkside).cbr
- `   54 MB`  Heavy Metal/01. Main Series/Heavy Metal v02 11 (1979-03) (c2c) (Foyle-DCP%26Darkside).cbr

### moon face — #02  — identical size  *(issue)*

- `  109 MB`  Jodorowsky and Moebius/Moon Face (2018) /Moon Face 02 - The Invisible Cathedral (2018) (Humanoids) (Digital-Empire).cbr
- `  109 MB`  Humanoids (Europe)/Moon Face/Moon Face 02 - The Invisible Cathedral (2018) (Humanoids) (Digital-Empire).cbr

### miracleman — #001  *(issue)*

- `  123 MB`  Miracleman/Miracleman v1 (001-016) (2014-2015) GetComics.INFO/Miracleman 001 (2014) (Digital) (Darkness-Empire).cbr
- `   47 MB`  Alan Moore/Alan Moore Essentials/Alan Moore 1984- Miracleman/Miracleman #001.cbr
- `   47 MB`  Alan Moore/Alan Moore Collection I- English Invasion/Alan Moore Collection III- 2000 AD/Miracleman/Miracleman/Miracleman #001.cbr

### moon face — #05  — identical size  *(issue)*

- `  108 MB`  Jodorowsky and Moebius/Moon Face (2018) /Moon Face 05 - The Egg of the Soul (2018) (Humanoids) (Digital-Empire).cbr
- `  108 MB`  Humanoids (Europe)/Moon Face/Moon Face 05 - The Egg of the Soul (2018) (Humanoids) (Digital-Empire).cbr

### exorcism at buckingham palace — #003  — identical size  *(issue)*

- `  108 MB`  The Exorcism at Buckingham Palace/The Exorcism at Buckingham Palace 003_(2026)_(digital)_(Son_of_Ultron-Empire).cbr
- `  108 MB`  The Exorcism at Buckingham Palace/The Exorcism at Buckingham Palace 003 (2026) (digital) (Son of Ultron-Empire).cbr

### blood stain — v3  — identical size  *(volume)*

- `  108 MB`  Blood Stain/Blood Stain v03 (2017) (Digital) (DrDoom-Empire).cbz
- `  108 MB`  Bllod Stain/Blood Stain v03 (2017) (Digital) (DrDoom-Empire).cbz

### nikolai dante — #01  *(issue)*

- `  212 MB`  2000AD - Collections /The Complete Nikolai Dante/Nikolai Dante 01 - Too Cool to Kill (2011) (Digital) (DR & Quinch-Empire).cbr
- `    2 MB`  2000AD - Collections /The Complete Nikolai Dante/Covers/Nikolai Dante 01 - Too Cool to Kill (TPB Cvr Only) (2011) (Digital) (DR & Quinch-Empire).cbr

### heavy metal — v34 — #09  — identical size  *(volume)*

- `  107 MB`  Heavy Metal/Heavy Metal Vols 01-35 (1977-2012)/Heavy Metal v34 09 (2011) (Vague Prophet and Vapor Trail).cbr
- `  107 MB`  Heavy Metal/01. Main Series/Heavy Metal v34 09 (2011) (Vague Prophet and Vapor Trail).cbr

### fogtown  — identical size  *(issue)*

- `  107 MB`  Vertigo Crime (Collection) (2009-2011)/Fogtown (2010) (Minutemen-DTs).cbr
- `  107 MB`  Fogtown (2010) (c2c) (Minutemen-DTs).cbz

### hellboy in mexico  *(issue)*

- `  183 MB`  Hellboy/Hellboy in Mexico (2016) (digital) (Son of Ultron-Empire).cbr
- `   31 MB`  Hellboy/63.)  Hellboy in Mexico  (1982 AD)/Hellboy in Mexico.cbz

### deadpool pulp  — identical size  *(issue)*

- `  106 MB`  Marvel Noir (2009-2011)(digital)/Deadpool Pulp (2011) (digital) (Minutemen-Slayer).cbr
- `  106 MB`  GG Studio (Collection) (2010-2012)/Marvel Noir (2009-2011)(digital)/Deadpool Pulp (2011) (digital) (Minutemen-Slayer).cbr

### nikolai dante — #02  *(issue)*

- `  209 MB`  2000AD - Collections /The Complete Nikolai Dante/Nikolai Dante 02 - The Great Game (2014) (Digital) (DR & Quinch-Empire).cbr
- `    3 MB`  2000AD - Collections /The Complete Nikolai Dante/Covers/Nikolai Dante 02 - The Great Game (TPB Cvr Only) (2014) (Digital) (DR & Quinch-Empire).cbr

### heavy metal — v35 — #08  — identical size  *(volume)*

- `  106 MB`  Heavy Metal/Heavy Metal Vols 01-35 (1977-2012)/Heavy Metal v35 08 (2012).cbr
- `  106 MB`  Heavy Metal/01. Main Series/Heavy Metal v35 08 (2012).cbr

### fiends of eastern front — v1  *(volume)*

- `  189 MB`  Fiends of the Eastern Front/Fiends of the Eastern Front v01 (2023) (digital) (Torquemada).cbr
- `   23 MB`  2000AD - Collections /Fiends of the Eastern Front/Fiends of the Eastern Front V1 (Dan Dare 2000AD Remix).cbr

### heavy metal — v13 — #02  — identical size  *(volume)*

- `  104 MB`  Heavy Metal/Heavy Metal Vols 01-35 (1977-2012)/Heavy Metal v13 02 (1989-05).cbr
- `  104 MB`  Heavy Metal/01. Main Series/Heavy Metal v13 02 (1989-05).cbr

### avengers — #010  *(issue)*

- `  103 MB`  Avengers/Avengers (2018-2019)/Avengers 010 (2019) (Digital) (Zone-Empire).cbr
- `   65 MB`  Avengers/Avengers Vol. 07 (001-011,672-690)(2017-2018)(digital)/Avengers 010 (2017) (digital) (Minutemen-Slayer).cbr
- `   40 MB`  Alias  ( Jessica Jones , The Pulse & Appearances)/Appearances/Avengers (2010)/Avengers 010 (2011) (with Heroes for Hire #1) (Minutemen-DTs&Saxon).cbr

### heavy metal — v34 — #06  — identical size  *(volume)*

- `  104 MB`  Heavy Metal/Heavy Metal Vols 01-35 (1977-2012)/Heavy Metal v34 06 (2010) (svengali-DCP).cbz
- `  104 MB`  Heavy Metal/01. Main Series/Heavy Metal v34 06 (2010) (svengali-DCP).cbz

### kimota! miracleman companion  — identical size  *(issue)*

- `  103 MB`  Miracleman/Kimota! The Miracleman Companion (2001).cbr
- `  103 MB`  Alan Moore/Alan Moore Collection I- English Invasion/Alan Moore Collection III- 2000 AD/Miracleman/Miracleman- Extras/Kimota! The Miracleman Companion (2001) (1440 px) (MiracleScans Ltd).cbr

### judge dredd nobody apes law  — identical size  *(issue)*

- `   68 MB`  Judge Dredd - Collections/Judge Dredd - Nobody Apes the Law (2018) (digital) (JeffAlbertson-DCP).cbz
- `   68 MB`  Judge Dredd - Collections/Judge Dredd - Nobody Apes the Law (2018) (digital) (JeffAlbertson-DCP)/Judge Dredd - Nobody Apes the Law (2018) (digital) (JeffAlbertson-DCP).cbz
- `   68 MB`  2000AD - Collections /Judge Dredd/Judge Dredd - Nobody Apes the Law (2018) (2000AD) (digital) (JeffAlbertson-DCP).cbz

### moon face — #03  — identical size  *(issue)*

- `  102 MB`  Jodorowsky and Moebius/Moon Face (2018) /Moon Face 03 - The Zenith's Stone (2018) (Humanoids) (Digital-Empire).cbr
- `  102 MB`  Humanoids (Europe)/Moon Face/Moon Face 03 - The Zenith's Stone (2018) (Humanoids) (Digital-Empire).cbr

### freak angels — #003  — identical size  *(issue)*

- `  102 MB`  Warren Ellis/Freak Angels/Freak Angels 003 - collection (049-072).cbr
- `  102 MB`  Warren Ellis/2008/2008 Freak Angels/Freak Angels 003 - collection (049-072).cbr

### thargs terror tales presents necronauts & a love like blood  — identical size  *(issue)*

- `  101 MB`  Necronauts/Thargs Terror Tales Presents - Necronauts & A Love Like Blood (2011) (digital-SD) (Torquemada).cbr
- `  101 MB`  2000AD - Collections /Tharg/Thargs Terror Tales Presents - Necronauts & A Love Like Blood (2011) (digital-SD) (Torquemada).cbr

### bitter root red summer  — identical size  *(special)*

- `  101 MB`  Europe Comics (Collection)/Bitter Root (2021)/Bitter Root - Red Summer Special (2019) (Digital) (Mephisto-Empire).cbr
- `  101 MB`  Bitter Root/Bitter Root - Red Summer Special (2019) (Digital) (Mephisto-Empire).cbr

### sandman — #001  *(special)*

- `  150 MB`  The Sandman/The Sandman Special 001 (1991) (digital) (Son of Ultron-Empire).cbr
- `   51 MB`  The Sandman/Sandman Special 001 (1991) (c2c) (Pyramid).cbz

### freak angels — #001  — identical size  *(issue)*

- `  100 MB`  Warren Ellis/Freak Angels/Freak Angels 001 - collection (001-024).cbr
- `  100 MB`  Warren Ellis/2008/2008 Freak Angels/Freak Angels 001 - collection (001-024).cbr

### insurrection — v2  — identical size  *(volume)*

- `  100 MB`  Insurrection/Insurrection v02 - Liberty (2015) (digital) (Torquemada).cbr
- `  100 MB`  2000AD - Collections /Insurrection/Insurrection v02 - Liberty (2015) (digital) (Torquemada).cbr

### heavy metal — v2 — #008  — identical size  *(volume)*

- `   99 MB`  Heavy Metal/Heavy Metal Vols 01-35 (1977-2012)/Heavy Metal v02 008 (1978) (null-DCP).cbz
- `   99 MB`  Heavy Metal/01. Main Series/Heavy Metal v02 008 (1978) (null-DCP).cbz

### oz  — identical size  *(annual)*

- `   99 MB`  The Patchwork Girl of Oz/Oz Annual - Patchwork Girl (2021) (digital) (The Seeker-Empire).cbr
- `   99 MB`  Oz/Oz Annual - Patchwork Girl (2021) (digital) (The Seeker-Empire).cbr

### legion  *(issue)*

- `  176 MB`  Legion (001-005)(2018)(digital)(Zone-Empire+)/Legion (001-005)(2018)(digital)(Zone-Empire+).cbz
- `   21 MB`  Legion (one-shot) (2007) (Minutemen-Resin).cbr

### red better r.e.d. than dead  — identical size  *(issue)*

- `   98 MB`  Warren Ellis/RED - Better R.E.D. Than Dead (2011) (digital) (Son of Ultron-Empire).cbr
- `   98 MB`  RED/RED - Better R.E.D. Than Dead (2011) (digital) (Son of Ultron-Empire).cbr

### civil war captain america  *(issue)*

- `  130 MB`  Captain America/Civil War - Captain America (2007) (Digital) (F) (Kileko-Empire).cbr
- `   66 MB`  Civil War Event (001-007+Tie-Ins,Trades&Extras)(2006-2008)(digital)/Trades/Civil War - Captain America (2007) (Digital TPB) (Kileko-Empire).cbr

### heavy metal — v27 — #05  — identical size  *(volume)*

- `   98 MB`  Heavy Metal/Heavy Metal Vols 01-35 (1977-2012)/Heavy Metal v27 05 (2003) (svengali-DCP).cbz
- `   98 MB`  Heavy Metal/01. Main Series/Heavy Metal v27 05 (2003) (svengali-DCP).cbz

### heavy metal — v22 — #05  — identical size  *(volume)*

- `   97 MB`  Heavy Metal/Heavy Metal Vols 01-35 (1977-2012)/Heavy Metal v22 05 (1998-11) (c2c) (Lazarus-DCP).cbz
- `   97 MB`  Heavy Metal/01. Main Series/Heavy Metal v22 05 (1998-11) (c2c) (Lazarus-DCP).cbz

### heavy metal — v23 — #01  — identical size  *(volume)*

- `   97 MB`  Heavy Metal/Heavy Metal Vols 01-35 (1977-2012)/Heavy Metal v23 01 (1999-03) (c2c) (Lazarus-DCP).cbz
- `   97 MB`  Heavy Metal/01. Main Series/Heavy Metal v23 01 (1999-03) (c2c) (Lazarus-DCP).cbz

### heavy metal — v13 — #06  — identical size  *(volume)*

- `   97 MB`  Heavy Metal/Heavy Metal Vols 01-35 (1977-2012)/Heavy Metal v13 06 (1990-01).cbr
- `   97 MB`  Heavy Metal/01. Main Series/Heavy Metal v13 06 (1990-01).cbr

### freak angels — #004  — identical size  *(issue)*

- `   96 MB`  Warren Ellis/Freak Angels/Freak Angels 004 - collection (073-096).cbr
- `   96 MB`  Warren Ellis/2008/2008 Freak Angels/Freak Angels 004 - collection (073-096).cbr

### heavy metal — v24 — #06  — identical size  *(volume)*

- `   96 MB`  Heavy Metal/Heavy Metal Vols 01-35 (1977-2012)/Heavy Metal v24 06 (2001-01) (MetalMammoth).cbr
- `   96 MB`  Heavy Metal/01. Main Series/Heavy Metal v24 06 (2001-01) (MetalMammoth).cbr

### heavy metal — v22 — #02  — identical size  *(volume)*

- `   96 MB`  Heavy Metal/Heavy Metal Vols 01-35 (1977-2012)/Heavy Metal v22 02 (1998-05) (c2c) (Lazarus-DCP).cbz
- `   96 MB`  Heavy Metal/01. Main Series/Heavy Metal v22 02 (1998-05) (c2c) (Lazarus-DCP).cbz

### power up  *(issue)*

- `  141 MB`  Power Up (2016) (digital) (Son of Ultron-Empire).cbr
- `   50 MB`  Power Up (2009).cbz

### heavy metal — v21 — #04  — identical size  *(volume)*

- `   95 MB`  Heavy Metal/Heavy Metal Vols 01-35 (1977-2012)/Heavy Metal v21 04 (1997-09) (c2c) (Lazarus-DCP).cbz
- `   95 MB`  Heavy Metal/01. Main Series/Heavy Metal v21 04 (1997-09) (c2c) (Lazarus-DCP).cbz

### soulscape  *(issue)*

- `  125 MB`  Europe Comics (Collection)/Soulscape (2020) (digital) (Mr Norrell-Empire).cbr
- `   66 MB`  Europe Comics (Collection)/Soulscape (Europe Comics 2020) (webrip) (MagicMan-DCP).cbr

### heavy metal — v22 — #06  — identical size  *(volume)*

- `   95 MB`  Heavy Metal/Heavy Metal Vols 01-35 (1977-2012)/Heavy Metal v22 06 (1999-01) (c2c) (Lazarus-DCP).cbz
- `   95 MB`  Heavy Metal/01. Main Series/Heavy Metal v22 06 (1999-01) (c2c) (Lazarus-DCP).cbz

### heavy metal — v4 — #12  — identical size  *(volume)*

- `   95 MB`  Heavy Metal/Heavy Metal Vols 01-35 (1977-2012)/Heavy Metal v04 12 (1981-03) (glitch-DCP).cbr
- `   95 MB`  Heavy Metal/01. Main Series/Heavy Metal v04 12 (1981-03) (glitch-DCP).cbr

### noir  *(issue)*

- `  131 MB`  Europe Comics (Collection)/Noir (2017) (Europe Comics) (Digital-Empire).cbz
- `   58 MB`  Noir (2009) (Minutemen-DTs).cbr

### jenny sparks secret history of authority  *(issue)*

- `   94 MB`  The Authority/Jenny Sparks - The Secret History of the Authority 01-05 (2000).cbz
- `   94 MB`  Jenny Sparks (2025)/Jenny Sparks - The Secret History of the Authority 01-05 (2000).cbz

### heavy metal — v3 — #002  — identical size  *(volume)*

- `   94 MB`  Heavy Metal/Heavy Metal Vols 01-35 (1977-2012)/Heavy Metal v03 002 (1979) (null-DCP).cbz
- `   94 MB`  Heavy Metal/01. Main Series/Heavy Metal v03 002 (1979) (null-DCP).cbz

### nikolai dante — #11  *(issue)*

- `  186 MB`  2000AD - Collections /The Complete Nikolai Dante/Nikolai Dante 11 - Sympathy for the Devil (2012) (Digital) (DR & Quinch-Empire).cbr
- `    2 MB`  2000AD - Collections /The Complete Nikolai Dante/Covers/Nikolai Dante 11 - Sympathy for the Devil (TPB Cvr Only) (2012) (Digital) (DR & Quinch-Empire).cbr

### heavy metal — v24 — #04  — identical size  *(volume)*

- `   94 MB`  Heavy Metal/Heavy Metal Vols 01-35 (1977-2012)/Heavy Metal v24 04 (2000-09) (MetalMammoth).cbr
- `   94 MB`  Heavy Metal/01. Main Series/Heavy Metal v24 04 (2000-09) (MetalMammoth).cbr

### heavy metal — v15 — #03  — identical size  *(volume)*

- `   93 MB`  Heavy Metal/Heavy Metal Vols 01-35 (1977-2012)/Heavy Metal v15 03 (1991-07) (c2c) (Lazarus-DCP).cbz
- `   93 MB`  Heavy Metal/01. Main Series/Heavy Metal v15 03 (1991-07) (c2c) (Lazarus-DCP).cbz

### heavy metal — v3 — #10  — identical size  *(volume)*

- `   46 MB`  Heavy Metal/Heavy Metal Vols 01-35 (1977-2012)/Heavy Metal v03 10 (1980-02) (c2c) (Foyle-DCP&Darkside).cbr
- `   46 MB`  Heavy Metal/Heavy Metal Vols 01-35 (1977-2012)/Heavy Metal v03 10 (1980-02) (c2c) (Foyle-DCP%26Darkside).cbr
- `   46 MB`  Heavy Metal/01. Main Series/Heavy Metal v03 10 (1980-02) (c2c) (Foyle-DCP&Darkside).cbr
- `   46 MB`  Heavy Metal/01. Main Series/Heavy Metal v03 10 (1980-02) (c2c) (Foyle-DCP%26Darkside).cbr

### avengers — #001  *(issue)*

- `   83 MB`  Avengers/Avengers Vol. 07 (001-011,672-690)(2017-2018)(digital)/Avengers 001 (2017) (digital) (Minutemen-Slayer).cbr
- `   65 MB`  Avengers/Avengers (2018-2019)/Avengers 001 (2018) (Digital) (Zone-Empire).cbr
- `   37 MB`  Alias  ( Jessica Jones , The Pulse & Appearances)/Appearances/Avengers (2010)/Avengers 001 (2010) (8 covers) (Minutemen-Shepherd & Megan).cbz

### heavy metal — v23 — #05  — identical size  *(volume)*

- `   91 MB`  Heavy Metal/Heavy Metal Vols 01-35 (1977-2012)/Heavy Metal v23 05 (1999).cbz
- `   91 MB`  Heavy Metal/01. Main Series/Heavy Metal v23 05 (1999).cbz

### big ass sword  *(issue)*

- `  117 MB`  Big-Ass Sword/Big-Ass Sword (2025) (Graphic Novel) (Rebellion) (Digital) (LeDuch-DCP).cbz
- `   65 MB`  Big Ass Sword (2025) (digital) (Torquemada).cbz

### heavy metal — v34 — #03  — identical size  *(volume)*

- `   91 MB`  Heavy Metal/Heavy Metal Vols 01-35 (1977-2012)/Heavy Metal v34 03 (2010) (c2c) (svengali-DCP).cbr
- `   91 MB`  Heavy Metal/01. Main Series/Heavy Metal v34 03 (2010) (c2c) (svengali-DCP).cbr

### nikolai dante — #08  *(issue)*

- `  179 MB`  2000AD - Collections /The Complete Nikolai Dante/Nikolai Dante 08 - The Beast of Rudinshtein (2009) (Digital) (DR & Quinch-Empire).cbr
- `    2 MB`  2000AD - Collections /The Complete Nikolai Dante/Covers/Nikolai Dante 08 - The Beast of Rudinshtein (TPB Cvr Only) (2009) (Digital) (DR & Quinch-Empire).cbr

### insufferable — v1  *(volume)*

- `  128 MB`  Insufferable/Insufferable v1 (01-34) (2012)/Insufferable v1 (01-34) (2012).cbz
- `   54 MB`  Insufferable/Insufferable - Extras (2012-2013)/Insufferable v01 (2012) (digital) (HD) (Son of Ultron-Empire).cbr

### heavy metal — v12 — #04  — identical size  *(volume)*

- `   90 MB`  Heavy Metal/Heavy Metal Vols 01-35 (1977-2012)/Heavy Metal v12 04 (1989-Winter) (c2c) (Lazarus-DCP).cbz
- `   90 MB`  Heavy Metal/01. Main Series/Heavy Metal v12 04 (1989-Winter) (c2c) (Lazarus-DCP).cbz

### miracleman — #015  *(issue)*

- `   98 MB`  Miracleman/Miracleman v1 (001-016) (2014-2015) GetComics.INFO/Miracleman 015 (2015) (Digital) (Darkness-Empire).cbr
- `   41 MB`  Alan Moore/Alan Moore Essentials/Alan Moore 1984- Miracleman/Miracleman #015.cbr
- `   41 MB`  Alan Moore/Alan Moore Collection I- English Invasion/Alan Moore Collection III- 2000 AD/Miracleman/Miracleman/Miracleman #015.cbr

### heavy metal — v22 — #04  — identical size  *(volume)*

- `   90 MB`  Heavy Metal/Heavy Metal Vols 01-35 (1977-2012)/Heavy Metal v22 04 (1998-09) (c2c) (Lazarus-DCP).cbz
- `   90 MB`  Heavy Metal/01. Main Series/Heavy Metal v22 04 (1998-09) (c2c) (Lazarus-DCP).cbz

### sweets a new orleans crime story  — identical size  *(issue)*

- `   90 MB`  Vertigo Crime (Collection) (2009-2011)/Sweets - A New Orleans Crime Story (2011 TPB) (Pudgy-DCP).cbr
- `   90 MB`  Sweets - A New Orleans Crime Story (2011 TPB) (Pudgy-DCP).cbr

### heavy metal — v7 — #07  — identical size  *(volume)*

- `   90 MB`  Heavy Metal/Heavy Metal Vols 01-35 (1977-2012)/Heavy Metal v07 07 (1983-10) (Jnx-HaCsA).cbr
- `   90 MB`  Heavy Metal/01. Main Series/Heavy Metal v07 07 (1983-10) (Jnx-HaCsA).cbr

### corto maltese — #05  — identical size  *(issue)*

- `   89 MB`  Hugo Pratt/Corto Maltese 05 - Beyond the Windy Isles (Pratt, 2010) (Scanlation-Extended, 2015).cbr
- `   89 MB`  Corto Maltese/Corto Maltese 01-16/Corto Maltese 05 - Beyond the Windy Isles (Pratt, 2010) (Scanlation-Extended, 2015).cbr

### avengers — #034  *(issue)*

- `   65 MB`  Alias  ( Jessica Jones , The Pulse & Appearances)/Appearances/Avengers (2010)/Avengers 034 (FINAL) (c2c)(2013)(Re-em-Novus-HD).cbr
- `   46 MB`  Alias  ( Jessica Jones , The Pulse & Appearances)/Appearances/Avengers (2010)/Avengers 034 (FINAL) (c2c)(2013)(Re-em-Novus).cbr
- `   34 MB`  Alias  ( Jessica Jones , The Pulse & Appearances)/Appearances/Avengers (2010)/Avengers 034 (FINAL) (2013) (Digital) (Zone-Empire).cbr
- `   34 MB`  Alias  ( Jessica Jones , The Pulse & Appearances)/Appearances/Avengers (2010)/Avengers 034 (FINAL) (2013)(Digital)(C9-Novus).cbr

### 2000ad prog — #2270  — identical size  *(issue)*

- `   59 MB`  Dan Abnett/new Brink/2000AD prog 2270 (2022) (Digital-Empire).cbr
- `   59 MB`  2000AD prog/new Brink/2000AD prog 2270 (2022) (Digital-Empire).cbr
- `   59 MB`  2000AD prog/2000AD prog 2270 (2022) (Digital-Empire).cbr

### heavy metal — v12 — #02  — identical size  *(volume)*

- `   89 MB`  Heavy Metal/Heavy Metal Vols 01-35 (1977-2012)/Heavy Metal v12 02 (1988).cbz
- `   89 MB`  Heavy Metal/01. Main Series/Heavy Metal v12 02 (1988).cbz

### hope — v2  *(volume)*

- `  101 MB`  2000AD - Collections /Hope V2 Under Fire (Dan Dare 2000AD Remix).cbr
- `   77 MB`  2000AD - Collections /Hope/Hope v02 - ...Under Fire (2020) (digital) (Torquemada).cbr

### heavy metal — v23 — #03  — identical size  *(volume)*

- `   89 MB`  Heavy Metal/Heavy Metal Vols 01-35 (1977-2012)/Heavy Metal v23 03 (1999).cbz
- `   89 MB`  Heavy Metal/01. Main Series/Heavy Metal v23 03 (1999).cbz

### heavy metal — v21 — #05  — identical size  *(volume)*

- `   89 MB`  Heavy Metal/Heavy Metal Vols 01-35 (1977-2012)/Heavy Metal v21 05 (1997-11) (c2c) (Lazarus-DCP).cbz
- `   89 MB`  Heavy Metal/01. Main Series/Heavy Metal v21 05 (1997-11) (c2c) (Lazarus-DCP).cbz

### corto maltese — #06  — identical size  *(issue)*

- `   89 MB`  Hugo Pratt/Corto Maltese 06 - The Lagoon of Mysteries (Pratt, 2009) (Scanlation-Extended, 2016).cbr
- `   89 MB`  Corto Maltese/Corto Maltese 01-16/Corto Maltese 06 - The Lagoon of Mysteries (Pratt, 2009) (Scanlation-Extended, 2016).cbr

### heavy metal — v21 — #06  — identical size  *(volume)*

- `   89 MB`  Heavy Metal/Heavy Metal Vols 01-35 (1977-2012)/Heavy Metal v21 06 (1998-01) (c2c) (Lazarus-DCP).cbz
- `   89 MB`  Heavy Metal/01. Main Series/Heavy Metal v21 06 (1998-01) (c2c) (Lazarus-DCP).cbz

### transporter — #004  — identical size  *(issue)*

- `   89 MB`  The Transporter/The Transporter 004 - The Final Mission (2023) (digital) (Mr Norrell-Empire).cbr
- `   89 MB`  Europe Comics (Collection)/The Transporter 004 - The Final Mission (2023) (digital) (Mr Norrell-Empire).cbr

### human  — identical size  *(issue)*

- `   89 MB`  Lucas Varela/Human (2019) (webrip) (MagicMan-DCP).cbr
- `   89 MB`  Europe Comics (Collection)/Human (Europe Comics 2019) (webrip) (MagicMan-DCP).cbr

### olympic games in ancient greece  *(issue)*

- `  109 MB`  Olympic Games in Ancient Greece (2023) (digital) (Mr Norrell-Empire).cbr
- `   67 MB`  Europe Comics (Collection)/Olympic Games in Ancient Greece (Europe Comics 2023) (webrip) (MagicMan-DCP).cbr

### heavy metal — v24 — #03  — identical size  *(volume)*

- `   88 MB`  Heavy Metal/Heavy Metal Vols 01-35 (1977-2012)/Heavy Metal v24 03 (2000-07) (c2c) (Lazarus-DCP).cbz
- `   88 MB`  Heavy Metal/01. Main Series/Heavy Metal v24 03 (2000-07) (c2c) (Lazarus-DCP).cbz

### 2000ad prog — #2280  — identical size  *(issue)*

- `   58 MB`  Dan Abnett/new Brink/2000AD prog 2280 (2022) (digital) (Minutemen-juvecube).cbr
- `   58 MB`  2000AD prog/new Brink/2000AD prog 2280 (2022) (digital) (Minutemen-juvecube).cbr
- `   58 MB`  2000AD prog/2000AD prog 2280 (2022) (digital) (Minutemen-juvecube).cbr

### heavy metal — v15 — #05  — identical size  *(volume)*

- `   87 MB`  Heavy Metal/Heavy Metal Vols 01-35 (1977-2012)/Heavy Metal v15 05 (1991-11) (c2c) (Lazarus-DCP).cbz
- `   87 MB`  Heavy Metal/01. Main Series/Heavy Metal v15 05 (1991-11) (c2c) (Lazarus-DCP).cbz

### ghost of hoppers  — identical size  *(issue)*

- `   87 MB`  Hernandez brothers/Love and Rockets/Ghost of Hoppers (A Love & Rockets Book).cbr
- `   87 MB`  Hernandez brothers/Love and Rockets/Ghost of Hoppers (A Love & Rockets Book) (2006) (F).cbr

### i can sell you a body  *(issue)*

- `  109 MB`  I Can Sell You a Body (2026) (digital) (Mr Norrell-Empire).cbr
- `   64 MB`  I Can Sell You A Body (2020) (digital) (Knight Ripper-Empire)/I Can Sell You A Body (2020).cbz

### heavy metal — v14 — #02  — identical size  *(volume)*

- `   86 MB`  Heavy Metal/Heavy Metal Vols 01-35 (1977-2012)/Heavy Metal v14 02 (1990-05) (c2c) (Lazarus-DCP).cbz
- `   86 MB`  Heavy Metal/01. Main Series/Heavy Metal v14 02 (1990-05) (c2c) (Lazarus-DCP).cbz

### heavy metal — v22 — #01  — identical size  *(volume)*

- `   86 MB`  Heavy Metal/Heavy Metal Vols 01-35 (1977-2012)/Heavy Metal v22 01 (1998-03) (c2c) (Lazarus-DCP).cbz
- `   86 MB`  Heavy Metal/01. Main Series/Heavy Metal v22 01 (1998-03) (c2c) (Lazarus-DCP).cbz

### heavy metal — v4 — #08  — identical size  *(volume)*

- `   86 MB`  Heavy Metal/Heavy Metal Vols 01-35 (1977-2012)/Heavy Metal v04 08 (1980-11) (c2c) (Lazarus-DCP).cbz
- `   86 MB`  Heavy Metal/01. Main Series/Heavy Metal v04 08 (1980-11) (c2c) (Lazarus-DCP).cbz

### heavy metal — v12 — #01  — identical size  *(volume)*

- `   86 MB`  Heavy Metal/Heavy Metal Vols 01-35 (1977-2012)/Heavy Metal v12 01 (1988).cbz
- `   86 MB`  Heavy Metal/01. Main Series/Heavy Metal v12 01 (1988).cbz

### judge death 2025 mega  *(special)*

- `   86 MB`  Judge Dredd - Collections/Judge Death 2025 Mega Special (2025) (One Shot) (Rebellion) (Digital-HD) (LeDuch).cbz
- `   84 MB`  Judge Dredd - Collections/Judge Death - 2025 Mega Special (2025) (digital) (Torquemada).cbz

### heavy metal — v11 — #01  — identical size  *(volume)*

- `   85 MB`  Heavy Metal/Heavy Metal Vols 01-35 (1977-2012)/Heavy Metal v11 01 (1987) (Calexicoca).cbr
- `   85 MB`  Heavy Metal/01. Main Series/Heavy Metal v11 01 (1987) (Calexicoca).cbr

### heavy metal — #266  *(issue)*

- `   86 MB`  Heavy Metal/01. Main Series/Heavy Metal 266(2013)(c2c)(TLK-EMPIRE).cbr
- `   83 MB`  Heavy Metal/01. Main Series/Heavy Metal 266.cbr

### heavy metal — v14 — #01  — identical size  *(volume)*

- `   84 MB`  Heavy Metal/Heavy Metal Vols 01-35 (1977-2012)/Heavy Metal v14 01 (1990-03) (c2c) (Lazarus-DCP).cbz
- `   84 MB`  Heavy Metal/01. Main Series/Heavy Metal v14 01 (1990-03) (c2c) (Lazarus-DCP).cbz

### xmas  *(special)*

- `   65 MB`  Judge Dredd - Collections/Judge Dredd Collected from 2000AD progs 0001 - 1829 (1977 - 2013) (complete) (Inc  Specials & Annuals 1977 - 1999)/Judge Dredd Collected from Annuals & Specials (1977 - 1999) (- JJ -)/Xmas Special Edition (1994).cbr
- `   58 MB`  Judge Dredd - Collections/Judge Dredd Collected from 2000AD progs 0001 - 1829 (1977 - 2013) (complete) (Inc  Specials & Annuals 1977 - 1999)/Judge Dredd Collected from Annuals & Specials (1977 - 1999) (- JJ -)/Xmas Special Edition (1995).cbr
- `   45 MB`  Judge Dredd - Collections/Judge Dredd Collected from 2000AD progs 0001 - 1829 (1977 - 2013) (complete) (Inc  Specials & Annuals 1977 - 1999)/Judge Dredd Collected from Annuals & Specials (1977 - 1999) (- JJ -)/Xmas Special Edition (1999).cbr

### mercy heights — v2  — identical size  *(volume)*

- `   84 MB`  2000AD - Collections /Mercy Heights V2 (Dan Dare 2000AD Remix).cbr
- `   84 MB`  2000AD - Collections /Mercy Heights V2 (Dan Dare 2000AD Remix) (1).cbr

### heavy metal — v31 — #06  — identical size  *(volume)*

- `   84 MB`  Heavy Metal/Heavy Metal Vols 01-35 (1977-2012)/Heavy Metal v31 06 (2008) (svengali-DCP).cbz
- `   84 MB`  Heavy Metal/01. Main Series/Heavy Metal v31 06 (2008) (svengali-DCP).cbz

### heavy metal — v34 — #04  — identical size  *(volume)*

- `   84 MB`  Heavy Metal/Heavy Metal Vols 01-35 (1977-2012)/Heavy Metal v34 04 (2010) (c2c) (svengali-DCP).cbr
- `   84 MB`  Heavy Metal/01. Main Series/Heavy Metal v34 04 (2010) (c2c) (svengali-DCP).cbr

### heavy metal — v33 — #08  — identical size  *(volume)*

- `   83 MB`  Heavy Metal/Heavy Metal Vols 01-35 (1977-2012)/Heavy Metal v33 08 (2009) (Terror Special) (svengali-DCP).cbr
- `   83 MB`  Heavy Metal/01. Main Series/Heavy Metal v33 08 (2009) (Terror Special) (svengali-DCP).cbr

### filthy rich  — identical size  *(issue)*

- `   83 MB`  Vertigo Crime (Collection) (2009-2011)/Filthy Rich (2009) (Minutemen-DTs).cbr
- `   83 MB`  Filthy Rich (2009) (Minutemen-DTs).cbr

### nikolai dante — #06  *(issue)*

- `  164 MB`  2000AD - Collections /The Complete Nikolai Dante/Nikolai Dante 06 - Hell and High Water (2008) (Digital) (DR & Quinch-Empire).cbr
- `    2 MB`  2000AD - Collections /The Complete Nikolai Dante/Covers/Nikolai Dante 06 - Hell and High Water (TPB Cvr Only) (2008) (Digital) (DR & Quinch-Empire).cbr

### heavy metal — v3 — #01  — identical size  *(volume)*

- `   83 MB`  Heavy Metal/Heavy Metal Vols 01-35 (1977-2012)/Heavy Metal v03 01 (1979-05) (fixed by glitch-DCP).cbr
- `   83 MB`  Heavy Metal/01. Main Series/Heavy Metal v03 01 (1979-05) (fixed by glitch-DCP).cbr

### heavy metal — v16 — #06  — identical size  *(volume)*

- `   83 MB`  Heavy Metal/Heavy Metal Vols 01-35 (1977-2012)/Heavy Metal v16 06 (v18 05) (1993-01) (c2c) (Lazarus-DCP).cbz
- `   83 MB`  Heavy Metal/01. Main Series/Heavy Metal v16 06 (v18 05) (1993-01) (c2c) (Lazarus-DCP).cbz

### brass sun — v5  — identical size  *(volume)*

- `   83 MB`  Brass Sun/Brass Sun V5 Engine Summer (Dan Dare 2000AD Remix).cbr
- `   83 MB`  2000AD - Collections /Brass Sun/Brass Sun V5 Engine Summer (Dan Dare 2000AD Remix).cbr

### 2000ad prog 2015  *(issue)*

- `   84 MB`  2000AD prog/Yearbooks & Specials/Yearbooks (2000-2015)/2000AD Prog 2015 (2014) (digital-Empire).cbr
- `   41 MB`  2000AD prog/2000AD prog 2015 (2017) (digital) (juvecube).cbr
- `   41 MB`  2000AD prog/2000AD Judge Dredd January - June 2017 (juvecube)/2000AD progs 2012-2037/2000AD prog 2015 (2017) (juvecube).cbr

### miracleman — #002  *(issue)*

- `   82 MB`  Miracleman/Miracleman v1 (001-016) (2014-2015) GetComics.INFO/Miracleman 002 (2014) (Digital) (Darkness-Empire).cbr
- `   41 MB`  Alan Moore/Alan Moore Essentials/Alan Moore 1984- Miracleman/Miracleman #002.cbr
- `   41 MB`  Alan Moore/Alan Moore Collection I- English Invasion/Alan Moore Collection III- 2000 AD/Miracleman/Miracleman/Miracleman #002.cbr

### insufferable — v3  *(volume)*

- `  123 MB`  Insufferable/Insufferable v3 (01-18) (2014-2015)/Insufferable v3 (01-18) (2014-2015).cbz
- `   41 MB`  Insufferable/Insufferable - Extras (2012-2013)/Insufferable v03 (2012) (digital) (HD) (Son of Ultron-Empire).cbr

### transporter — #001  — identical size  *(issue)*

- `   81 MB`  The Transporter/The Transporter 001 - Nymph (2020) (digital) (Mr Norrell-Empire).cbr
- `   81 MB`  Europe Comics (Collection)/The Transporter 001 - Nymph (2020) (digital) (Mr Norrell-Empire).cbr

### new avengers — #34  *(issue)*

- `   63 MB`  Alias  ( Jessica Jones , The Pulse & Appearances)/Appearances/New Avengers (2010)/New Avengers 34(FINAL)(c2c)(2013)(Re-em-Novus-HD).cbr
- `   49 MB`  Alias  ( Jessica Jones , The Pulse & Appearances)/Appearances/New Avengers (2010)/New Avengers 34(FINAL)(c2c)(2013)(Re-em-Novus).cbr
- `   25 MB`  Alias  ( Jessica Jones , The Pulse & Appearances)/Appearances/New Avengers (2010)/New Avengers 34(FINAL)(2013) (Zone-Empire).cbr
- `   25 MB`  Alias  ( Jessica Jones , The Pulse & Appearances)/Appearances/New Avengers (2010)/New Avengers 34(FINAL)(2013)(Digital)(Tyrant Lizard King-EMPIRE).cbr

### top ten forty niners  — identical size  *(volume)*

- `   81 MB`  Alan Moore/Top Ten - The Forty-Niners HC (2005) (rougher-OCD).cbr
- `   81 MB`  Alan Moore/Top 10/The Forty-Niners/Top Ten - The Forty-Niners HC (2005) (rougher-OCD).cbr

### 2000ad prog 2008  *(issue)*

- `   60 MB`  2000AD prog/Yearbooks & Specials/Yearbooks (2000-2015)/2000AD Prog 2008 (2007) (John Williams-DCP).cbr
- `   60 MB`  2000AD prog/2000AD (Specials, Annuals & Poster Progs + Extras)/2000AD Yearbooks & Specials (1977 - 2013)/2000AD Yearbooks (Prog 2000 - 2013)/2000AD Prog 2008.cbr
- `   43 MB`  2000AD prog/2000AD prog 2008 (2016) (digital) (juvecube).cbr

### heavy metal — v14 — #06  — identical size  *(volume)*

- `   81 MB`  Heavy Metal/Heavy Metal Vols 01-35 (1977-2012)/Heavy Metal v14 06 (1991-01) (c2c) (Lazarus-DCP).cbz
- `   81 MB`  Heavy Metal/01. Main Series/Heavy Metal v14 06 (1991-01) (c2c) (Lazarus-DCP).cbz

### heavy metal — v32 — #08  — identical size  *(volume)*

- `   80 MB`  Heavy Metal/Heavy Metal Vols 01-35 (1977-2012)/Heavy Metal v32 08 (2008) (Eerie Special).cbr
- `   80 MB`  Heavy Metal/01. Main Series/Heavy Metal v32 08 (2008) (Eerie Special).cbr

### nikolai dante — #09  *(issue)*

- `  159 MB`  2000AD - Collections /The Complete Nikolai Dante/Nikolai Dante 09 - Amerika (2010) (Digital) (DR & Quinch-Empire).cbr
- `    2 MB`  2000AD - Collections /The Complete Nikolai Dante/Covers/Nikolai Dante 09 - Amerika (TPB Cvr Only) (2010) (Digital) (DR & Quinch-Empire).cbr

### heavy metal — v26 — #06  — identical size  *(volume)*

- `   80 MB`  Heavy Metal/Heavy Metal Vols 01-35 (1977-2012)/Heavy Metal v26 06 (2003) (svengali-DCP).cbz
- `   80 MB`  Heavy Metal/01. Main Series/Heavy Metal v26 06 (2003) (svengali-DCP).cbz

### ballad of halo jones — v2  *(volume)*

- `   73 MB`  2000AD - Collections /The Ballad of Halo Jones/The Ballad of Halo Jones v02 (Color) (2018) (digital) (Torquemada).cbr
- `   29 MB`  Alan Moore/Halo Jones/The Ballad of Halo Jones Book 2.cbr
- `   29 MB`  Alan Moore/Alan Moore Collection I- English Invasion/Alan Moore Collection III- 2000 AD/2000 AD/2000 AD- Reprints/The Ballad Of Halo Jones/The Ballad Of Halo Jones Book #002 TPB.cbr
- `   29 MB`  2000AD prog/Alan Moore -2000AD/The Ballad of Halo Jones/The Ballad of Halo Jones Book 2.cbr

### 08 b.p.r.d. being human comixledger  — identical size  *(issue)*

- `   80 MB`  Hellboy/Hellboy in reading order/08 B.P.R.D. Being Human (TPB) (2011) ComixLedger.cbz
- `   80 MB`  Hellboy/08 B.P.R.D. Being Human (TPB) (2011) ComixLedger.cbz

### 2000ad prog 2009  *(issue)*

- `   62 MB`  2000AD prog/Yearbooks & Specials/Yearbooks (2000-2015)/2000AD Prog 2009 (2008) (John Williams-DCP).cbr
- `   62 MB`  2000AD prog/2000AD (Specials, Annuals & Poster Progs + Extras)/2000AD Yearbooks & Specials (1977 - 2013)/2000AD Yearbooks (Prog 2000 - 2013)/2000AD Prog 2009  (John Williams-DCP).cbr
- `   35 MB`  2000AD prog/2000AD prog 2009 (2016) (digital) (juvecube).cbr

### heavy metal — v13 — #04  — identical size  *(volume)*

- `   79 MB`  Heavy Metal/Heavy Metal Vols 01-35 (1977-2012)/Heavy Metal v13 04 (1989-09) (c2c) (Lazarus-DCP).cbz
- `   79 MB`  Heavy Metal/01. Main Series/Heavy Metal v13 04 (1989-09) (c2c) (Lazarus-DCP).cbz

### button man — v2  *(volume)*

- `   82 MB`  2000AD - Collections /Button Man V2 The Confession of Harry Exton (Dan Dare 2000AD Remix).cbr
- `   77 MB`  2000AD - Collections /Button Man/Button Man v02 - The Confession of Harry Exton (2008) (digital SD) (Ampersand).cbr

### transporter — #002  — identical size  *(issue)*

- `   79 MB`  The Transporter/The Transporter 002 - City of a Thousand Spires (2021) (digital) (Mr Norrell-Empire).cbr
- `   79 MB`  Europe Comics (Collection)/The Transporter 002 - City of a Thousand Spires (2021) (digital) (Mr Norrell-Empire).cbr

### heavy metal — v20 — #02  — identical size  *(volume)*

- `   53 MB`  Heavy Metal/Heavy Metal Vols 01-35 (1977-2012)/Heavy Metal v20 02 (1996_05) (Humperdido).cbr
- `   53 MB`  Heavy Metal/Heavy Metal Vols 01-35 (1977-2012)/Heavy Metal v20 02 (1996 05) (Humperdido).cbr
- `   53 MB`  Heavy Metal/01. Main Series/Heavy Metal v20 02 (1996 05) (Humperdido).cbr

### 2000ad prog 2010  *(issue)*

- `   60 MB`  2000AD prog/Yearbooks & Specials/Yearbooks (2000-2015)/2000AD Prog 2010 (2009) (John Williams-DCP).cbr
- `   60 MB`  2000AD prog/2000AD (Specials, Annuals & Poster Progs + Extras)/2000AD Yearbooks & Specials (1977 - 2013)/2000AD Yearbooks (Prog 2000 - 2013)/2000AD Prog 2010  (16-12-09) (John Williams-DCP).cbr
- `   37 MB`  2000AD prog/2000AD prog 2010 (2016) (digital) (juvecube).cbr

### gold chase — #001  — identical size  *(issue)*

- `   79 MB`  The Gold Chase 001 (2022) (digital) (Mr Norrell-Empire).cbr
- `   79 MB`  Europe Comics (Collection)/The Gold Chase 001 (2022) (digital) (Mr Norrell-Empire).cbr

### heavy metal — v12 — #03  — identical size  *(volume)*

- `   79 MB`  Heavy Metal/Heavy Metal Vols 01-35 (1977-2012)/Heavy Metal V12 03 (1988) (c2c) (Lazarus-DCP).cbz
- `   79 MB`  Heavy Metal/01. Main Series/Heavy Metal V12 03 (1988) (c2c) (Lazarus-DCP).cbz

### 2000ad prog 2013  *(issue)*

- `   75 MB`  2000AD prog/2000AD (Specials, Annuals & Poster Progs + Extras)/2000AD Yearbooks & Specials (1977 - 2013)/2000AD Yearbooks (Prog 2000 - 2013)/2000AD Prog 2013 (Digital) (Nahga-Empire).cbr
- `   41 MB`  2000AD prog/2000AD prog 2013 (2017) (digital) (juvecube).cbr
- `   41 MB`  2000AD prog/2000AD Judge Dredd January - June 2017 (juvecube)/2000AD progs 2012-2037/2000AD prog 2013 (2017) (juvecube).cbr

### batman killing joke  *(issue)*

- `  111 MB`  Batman/Batman - The Killing Joke (1988).cbz
- `   23 MB`  Alan Moore/Batman - The Killing Joke.cbr
- `   23 MB`  Alan Moore/Alan Moore Collection II-  DC/Batman/Batman- The Killing Joke/Batman- The Killing Joke (1988).cbr

### human target  *(issue)*

- `  114 MB`  Human Target 01-04 (1999) (digital) (Son of Ultron-Empire)/Human Target 01-04 (1999) (digital) (Son of Ultron-Empire).cbz
- `   42 MB`  The Human Target/Human Target 1-4 (1999).cbz

### heavy metal — v4 — #03  — identical size  *(volume)*

- `   78 MB`  Heavy Metal/Heavy Metal Vols 01-35 (1977-2012)/Heavy Metal v04 03 (1980-06) (c2c) (Bluenaga).cbr
- `   78 MB`  Heavy Metal/01. Main Series/Heavy Metal v04 03 (1980-06) (c2c) (Bluenaga).cbr

### heavy metal — v3 — #06  — identical size  *(volume)*

- `   78 MB`  Heavy Metal/Heavy Metal Vols 01-35 (1977-2012)/Heavy Metal v03 06 (1979-10) (glitch-DCP).cbr
- `   78 MB`  Heavy Metal/01. Main Series/Heavy Metal v03 06 (1979-10) (glitch-DCP).cbr

### heavy metal — v27 — #03  — identical size  *(volume)*

- `   78 MB`  Heavy Metal/Heavy Metal Vols 01-35 (1977-2012)/Heavy Metal v27 03 (2003) (svengali-DCP).cbz
- `   78 MB`  Heavy Metal/01. Main Series/Heavy Metal v27 03 (2003) (svengali-DCP).cbz

### heavy metal — v13 — #01  — identical size  *(volume)*

- `   78 MB`  Heavy Metal/Heavy Metal Vols 01-35 (1977-2012)/Heavy Metal v13 01 (1989).cbr
- `   78 MB`  Heavy Metal/01. Main Series/Heavy Metal v13 01 (1989).cbr

### heavy metal — v15 — #02  — identical size  *(volume)*

- `   78 MB`  Heavy Metal/Heavy Metal Vols 01-35 (1977-2012)/Heavy Metal v15 02 (1991-05) (c2c) (Lazarus-DCP).cbz
- `   78 MB`  Heavy Metal/01. Main Series/Heavy Metal v15 02 (1991-05) (c2c) (Lazarus-DCP).cbz

### heavy metal — v7 — #05  — identical size  *(volume)*

- `   78 MB`  Heavy Metal/Heavy Metal Vols 01-35 (1977-2012)/Heavy Metal v07 05 (1983-08) (Jnx-HaCsA).cbr
- `   78 MB`  Heavy Metal/01. Main Series/Heavy Metal v07 05 (1983-08) (Jnx-HaCsA).cbr

### miracleman — #013  *(issue)*

- `   83 MB`  Miracleman/Miracleman v1 (001-016) (2014-2015) GetComics.INFO/Miracleman 013 (2014) (Digital) (Darkness-Empire).cbr
- `   36 MB`  Alan Moore/Alan Moore Essentials/Alan Moore 1984- Miracleman/Miracleman #013.cbr
- `   36 MB`  Alan Moore/Alan Moore Collection I- English Invasion/Alan Moore Collection III- 2000 AD/Miracleman/Miracleman/Miracleman #013.cbr

### heavy metal — v14 — #04  — identical size  *(volume)*

- `   77 MB`  Heavy Metal/Heavy Metal Vols 01-35 (1977-2012)/Heavy Metal v14 04 (1990-09) (c2c) (Lazarus-DCP).cbz
- `   77 MB`  Heavy Metal/01. Main Series/Heavy Metal v14 04 (1990-09) (c2c) (Lazarus-DCP).cbz

### ballad of halo jones — v1  *(volume)*

- `   75 MB`  2000AD - Collections /The Ballad of Halo Jones/The Ballad of Halo Jones v01 (Color) (2018) (digital) (Torquemada).cbr
- `   27 MB`  Alan Moore/Halo Jones/The Ballad of Halo Jones Book 1.cbr
- `   27 MB`  Alan Moore/Alan Moore Collection I- English Invasion/Alan Moore Collection III- 2000 AD/2000 AD/2000 AD- Reprints/The Ballad Of Halo Jones/The Ballad Of Halo Jones Book #001 TPB.cbr
- `   27 MB`  2000AD prog/Alan Moore -2000AD/The Ballad of Halo Jones/The Ballad of Halo Jones Book 1.cbr

### murena — v5  *(volume)*

- `  106 MB`  Murena/Murena T05 - The Black Goddess (2016) (digital) (The Magicians-Empire).cbr
- `   49 MB`  Murena/Murena T05 - The Black Goddess (Choky-Onairam-Tanim).cbr

### heavy metal — v4 — #04  — identical size  *(volume)*

- `   77 MB`  Heavy Metal/Heavy Metal Vols 01-35 (1977-2012)/Heavy Metal v04 04 (1980-07) (c2c) (Lazarus-DCP).cbz
- `   77 MB`  Heavy Metal/01. Main Series/Heavy Metal v04 04 (1980-07) (c2c) (Lazarus-DCP).cbz

### nikolai dante — #10  *(issue)*

- `  152 MB`  2000AD - Collections /The Complete Nikolai Dante/Nikolai Dante 10 - Hero of the Revolution (2011) (Digital) (DR & Quinch-Empire).cbr
- `    2 MB`  2000AD - Collections /The Complete Nikolai Dante/Covers/Nikolai Dante 10 - Hero of the Revolution (TPB Cvr Only) (2011) (Digital) (DR & Quinch-Empire).cbr

### freak angels — #006  — identical size  *(issue)*

- `   77 MB`  Warren Ellis/Freak Angels/Freak Angels 006 - collection (121-144).cbr
- `   77 MB`  Warren Ellis/2008/2008 Freak Angels/Freak Angels 006 - collection (121-144).cbr

### cowboys  — identical size  *(issue)*

- `   76 MB`  Vertigo Crime (Collection) (2009-2011)/Cowboys (2011) (Minutemen-DTs).cbr
- `   76 MB`  Cowboys (Vertigo)(2011)(c)/Cowboys (2011) (Minutemen-DTs).cbr

### freak angels — #002  — identical size  *(issue)*

- `   76 MB`  Warren Ellis/Freak Angels/Freak Angels 002 - collection (025-048).cbr
- `   76 MB`  Warren Ellis/2008/2008 Freak Angels/Freak Angels 002 - collection (025-048).cbr

### 10 years to death  — identical size  *(issue)*

- `   76 MB`  Aftershock comics/10 Years to Death (2021) (digital) (Son of Ultron-Empire).cbr
- `   76 MB`  10 Years to Death (2021) (digital) (Son of Ultron-Empire).cbr

### heavy metal — v5 — #04  — identical size  *(volume)*

- `   76 MB`  Heavy Metal/Heavy Metal Vols 01-35 (1977-2012)/Heavy Metal v05 04 (1981-07) (c2c) (Bluenagascan) (FIXED).cbr
- `   76 MB`  Heavy Metal/01. Main Series/Heavy Metal v05 04 (1981-07) (c2c) (Bluenagascan) (FIXED).cbr

### heavy metal — v7 — #03  — identical size  *(volume)*

- `   76 MB`  Heavy Metal/Heavy Metal Vols 01-35 (1977-2012)/Heavy Metal v07 03 (1983-06) (Jnx-HaCsA).cbr
- `   76 MB`  Heavy Metal/01. Main Series/Heavy Metal v07 03 (1983-06) (Jnx-HaCsA).cbr

### 2000ad prog 2014  *(issue)*

- `   73 MB`  2000AD prog/2000AD (Specials, Annuals & Poster Progs + Extras)/2000AD Yearbooks & Specials (1977 - 2013)/2000AD Yearbooks (Prog 2000 - 2013)/2000AD Prog 2014 (2013) (Digital) (Nahga-Empire).cbr
- `   39 MB`  2000AD prog/2000AD prog 2014 (2017) (digital) (juvecube).cbr
- `   39 MB`  2000AD prog/2000AD Judge Dredd January - June 2017 (juvecube)/2000AD progs 2012-2037/2000AD prog 2014 (2017) (juvecube).cbr

### heavy metal — v5 — #01  — identical size  *(volume)*

- `   75 MB`  Heavy Metal/Heavy Metal Vols 01-35 (1977-2012)/Heavy Metal v05 01 (1981-04) (c2c) (Lazarus-DCP).cbz
- `   75 MB`  Heavy Metal/01. Main Series/Heavy Metal v05 01 (1981-04) (c2c) (Lazarus-DCP).cbz

### heavy metal — v32 — #04  — identical size  *(volume)*

- `   75 MB`  Heavy Metal/Heavy Metal Vols 01-35 (1977-2012)/Heavy Metal v32 04 (2008) (svengali-DCP).cbr
- `   75 MB`  Heavy Metal/01. Main Series/Heavy Metal v32 04 (2008) (svengali-DCP).cbr

### heavy metal — v16 — #05  — identical size  *(volume)*

- `   75 MB`  Heavy Metal/Heavy Metal Vols 01-35 (1977-2012)/Heavy Metal v16 05 (v17 04) (1992-11) (c2c) (L74KL-DREGS).cbr
- `   75 MB`  Heavy Metal/01. Main Series/Heavy Metal v16 05 (v17 04) (1992-11) (c2c) (L74KL-DREGS).cbr

### heavy metal — v27 — #06  — identical size  *(volume)*

- `   75 MB`  Heavy Metal/Heavy Metal Vols 01-35 (1977-2012)/Heavy Metal v27 06 (2004) (svengali-DCP).cbz
- `   75 MB`  Heavy Metal/01. Main Series/Heavy Metal v27 06 (2004) (svengali-DCP).cbz

### heavy metal — v4 — #06  — identical size  *(volume)*

- `   75 MB`  Heavy Metal/Heavy Metal Vols 01-35 (1977-2012)/Heavy Metal v04 06 (1980-09) (c2c) (Lazarus-DCP).cbz
- `   75 MB`  Heavy Metal/01. Main Series/Heavy Metal v04 06 (1980-09) (c2c) (Lazarus-DCP).cbz

### nikolai dante — #04  *(issue)*

- `  147 MB`  2000AD - Collections /The Complete Nikolai Dante/Nikolai Dante 04 - Tsar Wars v01 (2006) (Digital) (DR & Quinch-Empire).cbr
- `    2 MB`  2000AD - Collections /The Complete Nikolai Dante/Covers/Nikolai Dante 04 - Tsar Wars Vol 1 (TPB Cvr Only) (2006) (Digital) (DR & Quinch-Empire).cbr

### heavy metal — v31 — #02  — identical size  *(volume)*

- `   75 MB`  Heavy Metal/Heavy Metal Vols 01-35 (1977-2012)/Heavy Metal v31 02 (2007) (svengali-DCP).cbz
- `   75 MB`  Heavy Metal/01. Main Series/Heavy Metal v31 02 (2007) (svengali-DCP).cbz

### heavy metal — v33 — #03  — identical size  *(volume)*

- `   75 MB`  Heavy Metal/Heavy Metal Vols 01-35 (1977-2012)/Heavy Metal v33 03 (2009) (svengali-DCP).cbz
- `   75 MB`  Heavy Metal/01. Main Series/Heavy Metal v33 03 (2009) (svengali-DCP).cbz

### heavy metal — v8 — #10  — identical size  *(volume)*

- `   75 MB`  Heavy Metal/Heavy Metal Vols 01-35 (1977-2012)/Heavy Metal v08 10 (1985-01) (c2c) (Lazarus-DCP).cbz
- `   75 MB`  Heavy Metal/01. Main Series/Heavy Metal v08 10 (1985-01) (c2c) (Lazarus-DCP).cbz

### 2000ad prog 2006  *(issue)*

- `   51 MB`  2000AD prog/Yearbooks & Specials/Yearbooks (2000-2015)/2000AD Prog 2006 (2005) (Jon001).cbr
- `   51 MB`  2000AD prog/2000AD (Specials, Annuals & Poster Progs + Extras)/2000AD Yearbooks & Specials (1977 - 2013)/2000AD Yearbooks (Prog 2000 - 2013)/2000AD Prog 2006.cbr
- `   47 MB`  2000AD prog/2000AD prog 2006 (2016) (digital) (juvecube).cbr

### heavy metal — v33 — #06  — identical size  *(volume)*

- `   74 MB`  Heavy Metal/Heavy Metal Vols 01-35 (1977-2012)/Heavy Metal v33 06 (2009) (svengali-DCP).cbr
- `   74 MB`  Heavy Metal/01. Main Series/Heavy Metal v33 06 (2009) (svengali-DCP).cbr

### heavy metal — v3 — #09  — identical size  *(volume)*

- `   74 MB`  Heavy Metal/Heavy Metal Vols 01-35 (1977-2012)/Heavy Metal v03 09 (1980-01) (c2c) (Lazarus-DCP).cbz
- `   74 MB`  Heavy Metal/01. Main Series/Heavy Metal v03 09 (1980-01) (c2c) (Lazarus-DCP).cbz

### heavy metal — v34 — #01  — identical size  *(volume)*

- `   74 MB`  Heavy Metal/Heavy Metal Vols 01-35 (1977-2012)/Heavy Metal v34 01 (2010) (c2c) (svengali-DCP).cbr
- `   74 MB`  Heavy Metal/01. Main Series/Heavy Metal v34 01 (2010) (c2c) (svengali-DCP).cbr

### barbara — v1  *(volume)*

- `   78 MB`  Manga/Osamu Tezuka/Barbara/Barbara v01 (2 of 2).cbr
- `   70 MB`  Manga/Osamu Tezuka/Barbara/Barbara v01 (1 of 2).cbr

### heavy metal — v2 — #01  — identical size  *(volume)*

- `   74 MB`  Heavy Metal/Heavy Metal Vols 01-35 (1977-2012)/Heavy Metal v02 01 (1978-05).cbr
- `   74 MB`  Heavy Metal/01. Main Series/Heavy Metal v02 01 (1978-05).cbr

### pixies of sixties ailith  — identical size  *(issue)*

- `   73 MB`  Pixies of the Sixties/Pixies of the Sixties - Ailith (2023) (digital) (Mr Norrell-Empire).cbr
- `   73 MB`  Humanoids (Europe)/Pixies of the Sixties - Ailith (2023) (digital) (Mr Norrell-Empire).cbr

### heavy metal — v7 — #04  — identical size  *(volume)*

- `   73 MB`  Heavy Metal/Heavy Metal Vols 01-35 (1977-2012)/Heavy Metal v07 04 (1983-07) (Jnx-HaCsA).cbr
- `   73 MB`  Heavy Metal/01. Main Series/Heavy Metal v07 04 (1983-07) (Jnx-HaCsA).cbr

### heavy metal — v27 — #02  — identical size  *(volume)*

- `   73 MB`  Heavy Metal/Heavy Metal Vols 01-35 (1977-2012)/Heavy Metal v27 02 (2003) (svengali-DCP).cbz
- `   73 MB`  Heavy Metal/01. Main Series/Heavy Metal v27 02 (2003) (svengali-DCP).cbz

### heavy metal — v7 — #06  — identical size  *(volume)*

- `   73 MB`  Heavy Metal/Heavy Metal Vols 01-35 (1977-2012)/Heavy Metal v07 06 (1983-09) (Jnx-HaCsA).cbr
- `   73 MB`  Heavy Metal/01. Main Series/Heavy Metal v07 06 (1983-09) (Jnx-HaCsA).cbr

### heavy metal — v10 — #03  — identical size  *(volume)*

- `   72 MB`  Heavy Metal/Heavy Metal Vols 01-35 (1977-2012)/Heavy Metal v10 03 (1986) (c2c) (Lazarus-DCP).cbz
- `   72 MB`  Heavy Metal/01. Main Series/Heavy Metal v10 03 (1986) (c2c) (Lazarus-DCP).cbz

### heavy metal — v4 — #10  — identical size  *(volume)*

- `   72 MB`  Heavy Metal/Heavy Metal Vols 01-35 (1977-2012)/Heavy Metal v04 10 (1981-01) (c2c) (Lazarus-DCP).cbz
- `   72 MB`  Heavy Metal/01. Main Series/Heavy Metal v04 10 (1981-01) (c2c) (Lazarus-DCP).cbz

### heavy metal — v11 — #04  — identical size  *(volume)*

- `   72 MB`  Heavy Metal/Heavy Metal Vols 01-35 (1977-2012)/Heavy Metal v11 04 (1988).cbr
- `   72 MB`  Heavy Metal/01. Main Series/Heavy Metal v11 04 (1988).cbr

### hypnotwist scarlet by starlight  — identical size  *(issue)*

- `   72 MB`  Scarlet (2018)/Hypnotwist - Scarlet by Starlight (2021) (Digital-Empire).cbr
- `   72 MB`  Hernandez brothers/Hypnotwist - Scarlet by Starlight (2021) (Digital-Empire).cbr

### corto maltese — #04  — identical size  *(issue)*

- `   72 MB`  Hugo Pratt/Corto Maltese 04 - Under the Pirate Flag (Pratt, 2010) (Scanlation-Extended, 2015).cbr
- `   72 MB`  Corto Maltese/Corto Maltese 01-16/Corto Maltese 04 - Under the Pirate Flag (Pratt, 2010) (Scanlation-Extended, 2015).cbr

### heavy metal — v27 — #04  — identical size  *(volume)*

- `   72 MB`  Heavy Metal/Heavy Metal Vols 01-35 (1977-2012)/Heavy Metal v27 04 (2003) (svengali-DCP).cbz
- `   72 MB`  Heavy Metal/01. Main Series/Heavy Metal v27 04 (2003) (svengali-DCP).cbz

### grifter midnighter uncivil union  — identical size  *(issue)*

- `   72 MB`  Warren Ellis/The Authority/Midnighter/Grifter-Midnighter - Uncivil Union (2007) (Minutemen).cbr
- `   72 MB`  The Authority/Midnighter/Grifter-Midnighter - Uncivil Union (2007) (Minutemen).cbr

### authorised happiness — #02  — identical size  *(issue)*

- `   72 MB`  Hellboy/Authorised Happiness 02 (2019) (Europe Comics) (Digital-Empire).cbr
- `   72 MB`  Europe Comics (Collection)/Authorised Happiness (Europe Comics) (Digital-Empire)/Authorised Happiness 02 (2019) (Europe Comics) (Digital-Empire).cbr

### heavy metal — v8 — #02  — identical size  *(volume)*

- `   71 MB`  Heavy Metal/Heavy Metal Vols 01-35 (1977-2012)/Heavy Metal v08 02 (1984-05) (c2c) (Lazarus-DCP).cbz
- `   71 MB`  Heavy Metal/01. Main Series/Heavy Metal v08 02 (1984-05) (c2c) (Lazarus-DCP).cbz

### heavy metal — v4 — #09  — identical size  *(volume)*

- `   71 MB`  Heavy Metal/Heavy Metal Vols 01-35 (1977-2012)/Heavy Metal v04 09 (1980-11) (c2c) (Lazarus-DCP).cbz
- `   71 MB`  Heavy Metal/01. Main Series/Heavy Metal v04 09 (1980-11) (c2c) (Lazarus-DCP).cbz

### barcelona at dawn  — identical size  *(issue)*

- `   71 MB`  SAF Comics (Europe Collection) (2019)/Barcelona at Dawn (2019) (SAF Comics) (Digital-Empire).cbr
- `   71 MB`  Barcelona at Dawn/Barcelona at Dawn (2019) (SAF Comics) (Digital-Empire).cbr

### 2000ad prog — #2271  — identical size  *(issue)*

- `   47 MB`  Dan Abnett/new Brink/2000AD prog 2271 (2022) (digital) (Minutemen-juvecube).cbr
- `   47 MB`  2000AD prog/new Brink/2000AD prog 2271 (2022) (digital) (Minutemen-juvecube).cbr
- `   47 MB`  2000AD prog/2000AD prog 2271 (2022) (digital) (Minutemen-juvecube).cbr

### heavy metal — v5 — #03  — identical size  *(volume)*

- `   71 MB`  Heavy Metal/Heavy Metal Vols 01-35 (1977-2012)/Heavy Metal v05 03 (1981-06) (c2c) (Lazarus-DCP).cbz
- `   71 MB`  Heavy Metal/01. Main Series/Heavy Metal v05 03 (1981-06) (c2c) (Lazarus-DCP).cbz

### alan moore's songbook  *(issue)*

- `   74 MB`  Alan Moore/Alan Moore Collection VI- Made For Moore/Alan Moore's Songbook/Alan Moore's Songbook (Restored).cbz
- `   68 MB`  Alan Moore/Alan Moore Collection VI- Made For Moore/Alan Moore's Songbook/Alan Moore's Songbook (c2c).cbr

### heavy metal — v7 — #02  — identical size  *(volume)*

- `   70 MB`  Heavy Metal/Heavy Metal Vols 01-35 (1977-2012)/Heavy Metal v07 02 (1983-05) (Jnx-HaCsA).cbr
- `   70 MB`  Heavy Metal/01. Main Series/Heavy Metal v07 02 (1983-05) (Jnx-HaCsA).cbr

### heavy metal — v4 — #07  — identical size  *(volume)*

- `   70 MB`  Heavy Metal/Heavy Metal Vols 01-35 (1977-2012)/Heavy Metal v04 07 (1980-10) (c2c) (Lazarus-DCP).cbz
- `   70 MB`  Heavy Metal/01. Main Series/Heavy Metal v04 07 (1980-10) (c2c) (Lazarus-DCP).cbz

### heavy metal — v8 — #12  — identical size  *(volume)*

- `   70 MB`  Heavy Metal/Heavy Metal Vols 01-35 (1977-2012)/Heavy Metal v08 12 (1985-03).cbz
- `   70 MB`  Heavy Metal/01. Main Series/Heavy Metal v08 12 (1985-03).cbz

### heavy metal — v1 — #04  — identical size  *(volume)*

- `   70 MB`  Heavy Metal/Heavy Metal Vols 01-35 (1977-2012)/Heavy Metal v01 04 (1977-07) (c2c) (Lazarus-DCP).cbz
- `   70 MB`  Heavy Metal/01. Main Series/Heavy Metal v01 04 (1977-07) (c2c) (Lazarus-DCP).cbz

### miracleman — #003  *(issue)*

- `   91 MB`  Miracleman/Miracleman v1 (001-016) (2014-2015) GetComics.INFO/Miracleman 003 (2014) (Digital) (Darkness-Empire).cbr
- `   25 MB`  Alan Moore/Alan Moore Essentials/Alan Moore 1984- Miracleman/Miracleman #003.cbr
- `   25 MB`  Alan Moore/Alan Moore Collection I- English Invasion/Alan Moore Collection III- 2000 AD/Miracleman/Miracleman/Miracleman #003.cbr

### heavy metal — v7 — #01  — identical size  *(volume)*

- `   70 MB`  Heavy Metal/Heavy Metal Vols 01-35 (1977-2012)/Heavy Metal v07 01 (1983-04) (Jnx-HaCsA).cbr
- `   70 MB`  Heavy Metal/01. Main Series/Heavy Metal v07 01 (1983-04) (Jnx-HaCsA).cbr

### heavy metal — v9 — #02  — identical size  *(volume)*

- `   70 MB`  Heavy Metal/Heavy Metal Vols 01-35 (1977-2012)/Heavy Metal v09 02 (1985-05) (c2c) (Lazarus-DCP).cbz
- `   70 MB`  Heavy Metal/01. Main Series/Heavy Metal v09 02 (1985-05) (c2c) (Lazarus-DCP).cbz

### heavy metal — v7 — #12  — identical size  *(volume)*

- `   70 MB`  Heavy Metal/Heavy Metal Vols 01-35 (1977-2012)/Heavy Metal v07 12 (1984-03) (c2c) (Lazarus-DCP).cbz
- `   70 MB`  Heavy Metal/01. Main Series/Heavy Metal v07 12 (1984-03) (c2c) (Lazarus-DCP).cbz

### heavy metal — v8 — #11  — identical size  *(volume)*

- `   70 MB`  Heavy Metal/Heavy Metal Vols 01-35 (1977-2012)/Heavy Metal v08 11 (1985-02).cbz
- `   70 MB`  Heavy Metal/01. Main Series/Heavy Metal v08 11 (1985-02).cbz

### heavy metal — v9 — #03  — identical size  *(volume)*

- `   70 MB`  Heavy Metal/Heavy Metal Vols 01-35 (1977-2012)/Heavy Metal v09 03 (1985-06) (c2c) (Lazarus-DCP).cbz
- `   70 MB`  Heavy Metal/01. Main Series/Heavy Metal v09 03 (1985-06) (c2c) (Lazarus-DCP).cbz

### miracleman — #012  *(issue)*

- `   85 MB`  Miracleman/Miracleman v1 (001-016) (2014-2015) GetComics.INFO/Miracleman 012 (2014) (Digital) (Darkness-Empire).cbr
- `   27 MB`  Alan Moore/Alan Moore Essentials/Alan Moore 1984- Miracleman/Miracleman #012.cbr
- `   27 MB`  Alan Moore/Alan Moore Collection I- English Invasion/Alan Moore Collection III- 2000 AD/Miracleman/Miracleman/Miracleman #012.cbr

### jeremiah — #007  — identical size  *(issue)*

- `   69 MB`  SAF Comics (Europe Collection) (2019)/Jeremiah 001-009 (2019) (SAF Comics)/Jeremiah 007 - Afromerica (2020) (digital) (Mr Norrell-Empire).cbr
- `   69 MB`  SAF Comics (Europe Collection) (2019)/Jeremiah 001-003 (2019) (SAF Comics)/Jeremiah 007 - Afromerica (2020) (digital) (Mr Norrell-Empire).cbr

### heavy metal — v3 — #08  — identical size  *(volume)*

- `   69 MB`  Heavy Metal/Heavy Metal Vols 01-35 (1977-2012)/Heavy Metal v03 08 (1979-12) (c2c) (Lazarus-DCP).cbz
- `   69 MB`  Heavy Metal/01. Main Series/Heavy Metal v03 08 (1979-12) (c2c) (Lazarus-DCP).cbz

### heavy metal — v2 — #03  — identical size  *(volume)*

- `   69 MB`  Heavy Metal/Heavy Metal Vols 01-35 (1977-2012)/Heavy Metal v02 03 (1978-07) (c2c) (Lazarus-DCP).cbz
- `   69 MB`  Heavy Metal/01. Main Series/Heavy Metal v02 03 (1978-07) (c2c) (Lazarus-DCP).cbz

### palestine  *(volume)*

- `   21 MB`  Palestine/Palestine GN  (1996)  (Chap 8).cbr
- `   20 MB`  Palestine/Palestine GN  (1996)  (Chap 7).cbr
- `   20 MB`  Palestine/Palestine GN  (1996)  (Chap 6).cbz
- `   18 MB`  Palestine/Palestine GN  (1996)  (Chap 4).cbz
- `   17 MB`  Palestine/Palestine GN  (1996)  (Chap 9).cbr
- `   15 MB`  Palestine/Palestine GN  (1996)  (Chap 1) .cbz
- `   14 MB`  Palestine/Palestine GN  (1996)  (Chap 3).cbz
- `   13 MB`  Palestine/Palestine GN  (1996)  (Chap 2) .cbz

### heavy metal — v3 — #11  — identical size  *(volume)*

- `   69 MB`  Heavy Metal/Heavy Metal Vols 01-35 (1977-2012)/Heavy Metal v03 11 (1980-03) (c2c) (Lazarus-DCP).cbz
- `   69 MB`  Heavy Metal/01. Main Series/Heavy Metal v03 11 (1980-03) (c2c) (Lazarus-DCP).cbz

### heavy metal — v8 — #03  — identical size  *(volume)*

- `   69 MB`  Heavy Metal/Heavy Metal Vols 01-35 (1977-2012)/Heavy Metal v08 03 (1984-06) (c2c) (Lazarus-DCP).cbz
- `   69 MB`  Heavy Metal/01. Main Series/Heavy Metal v08 03 (1984-06) (c2c) (Lazarus-DCP).cbz

### michel vaillant — #03  *(issue)*

- `   74 MB`  Michel Vaillant/Michel Vaillant 03 Beyond Control (Digital) (Europe Comics).cbr
- `   63 MB`  Michel Vaillant/Michel Vaillant 03 - Beyond Control (2021, 2nd edition) (digital) (Mr Norrell-Empire).cbr

### 2000ad prog 2005  *(issue)*

- `   48 MB`  2000AD prog/Yearbooks & Specials/Yearbooks (2000-2015)/2000AD Prog 2005 (2004).cbr
- `   48 MB`  2000AD prog/2000AD (Specials, Annuals & Poster Progs + Extras)/2000AD Yearbooks & Specials (1977 - 2013)/2000AD Yearbooks (Prog 2000 - 2013)/2000AD Prog 2005.cbr
- `   42 MB`  2000AD prog/2000AD prog 2005 (2016) (digital) (juvecube).cbr

### heavy metal — v3 — #04  — identical size  *(volume)*

- `   69 MB`  Heavy Metal/Heavy Metal Vols 01-35 (1977-2012)/Heavy Metal v03 04 (1979-08) (c2c) (Lazarus-DCP).cbz
- `   69 MB`  Heavy Metal/01. Main Series/Heavy Metal v03 04 (1979-08) (c2c) (Lazarus-DCP).cbz

### nikolai dante — #07  *(issue)*

- `  135 MB`  2000AD - Collections /The Complete Nikolai Dante/Nikolai Dante 07 - Sword of the Tsar (2008) (Digital) (DR & Quinch-Empire).cbr
- `    2 MB`  2000AD - Collections /The Complete Nikolai Dante/Covers/Nikolai Dante 07 - Sword of the Tsar (TPB Cvr Only) (2008) (Digital) (DR & Quinch-Empire).cbr

### pixies of sixties anann  — identical size  *(issue)*

- `   69 MB`  Pixies of the Sixties/Pixies of the Sixties - Anann (2023) (digital) (Mr Norrell-Empire).cbr
- `   69 MB`  Humanoids (Europe)/Pixies of the Sixties - Anann (2023) (digital) (Mr Norrell-Empire).cbr

### heavy metal — v5 — #08  — identical size  *(volume)*

- `   69 MB`  Heavy Metal/Heavy Metal Vols 01-35 (1977-2012)/Heavy Metal v05 08 (1981-11) (FPScans) (rescan).cbr
- `   69 MB`  Heavy Metal/01. Main Series/Heavy Metal v05 08 (1981-11) (FPScans) (rescan).cbr

### heavy metal — v9 — #06  — identical size  *(volume)*

- `   69 MB`  Heavy Metal/Heavy Metal Vols 01-35 (1977-2012)/Heavy Metal v09 06 (1985-09) (c2c) (Lazarus-DCP).cbz
- `   69 MB`  Heavy Metal/01. Main Series/Heavy Metal v09 06 (1985-09) (c2c) (Lazarus-DCP).cbz

### heavy metal — v8 — #07  — identical size  *(volume)*

- `   68 MB`  Heavy Metal/Heavy Metal Vols 01-35 (1977-2012)/Heavy Metal v08 07 (1984-10) (c2c) (Lazarus-DCP).cbz
- `   68 MB`  Heavy Metal/01. Main Series/Heavy Metal v08 07 (1984-10) (c2c) (Lazarus-DCP).cbz

### heavy metal — v8 — #06  — identical size  *(volume)*

- `   68 MB`  Heavy Metal/Heavy Metal Vols 01-35 (1977-2012)/Heavy Metal v08 06 (1984-09) (c2c) (Lazarus-DCP).cbz
- `   68 MB`  Heavy Metal/01. Main Series/Heavy Metal v08 06 (1984-09) (c2c) (Lazarus-DCP).cbz

### heavy metal — v4 — #02  — identical size  *(volume)*

- `   68 MB`  Heavy Metal/Heavy Metal Vols 01-35 (1977-2012)/Heavy Metal v04 02 (1980-05) (FPScans) (rescan).cbr
- `   68 MB`  Heavy Metal/01. Main Series/Heavy Metal v04 02 (1980-05) (FPScans) (rescan).cbr

### heavy metal — v4 — #11  — identical size  *(volume)*

- `   68 MB`  Heavy Metal/Heavy Metal Vols 01-35 (1977-2012)/Heavy Metal v04 11 (1981-02) (c2c) (Lazarus-DCP).cbz
- `   68 MB`  Heavy Metal/01. Main Series/Heavy Metal v04 11 (1981-02) (c2c) (Lazarus-DCP).cbz

### miracleman — #014  *(issue)*

- `   86 MB`  Miracleman/Miracleman v1 (001-016) (2014-2015) GetComics.INFO/Miracleman 014 (2015) (Digital) (Darkness-Empire).cbr
- `   25 MB`  Alan Moore/Alan Moore Essentials/Alan Moore 1984- Miracleman/Miracleman #014.cbr
- `   25 MB`  Alan Moore/Alan Moore Collection I- English Invasion/Alan Moore Collection III- 2000 AD/Miracleman/Miracleman/Miracleman #014.cbr

### heavy metal — v32 — #02  — identical size  *(volume)*

- `   68 MB`  Heavy Metal/Heavy Metal Vols 01-35 (1977-2012)/Heavy Metal v32 02 (2008-05).cbr
- `   68 MB`  Heavy Metal/01. Main Series/Heavy Metal v32 02 (2008-05).cbr

### miracleman — #005  *(issue)*

- `   74 MB`  Miracleman/Miracleman v1 (001-016) (2014-2015) GetComics.INFO/Miracleman 005 (2014) (Digital) (Darkness-Empire).cbr
- `   31 MB`  Alan Moore/Alan Moore Essentials/Alan Moore 1984- Miracleman/Miracleman #005.cbr
- `   31 MB`  Alan Moore/Alan Moore Collection I- English Invasion/Alan Moore Collection III- 2000 AD/Miracleman/Miracleman/Miracleman #005.cbr

### heavy metal — v8 — #05  — identical size  *(volume)*

- `   68 MB`  Heavy Metal/Heavy Metal Vols 01-35 (1977-2012)/Heavy Metal v08 05 (1984-08) (c2c) (Lazarus-DCP).cbz
- `   68 MB`  Heavy Metal/01. Main Series/Heavy Metal v08 05 (1984-08) (c2c) (Lazarus-DCP).cbz

### heavy metal — v7 — #11  — identical size  *(volume)*

- `   68 MB`  Heavy Metal/Heavy Metal Vols 01-35 (1977-2012)/Heavy Metal v07 11 (1984-02) (c2c) (Lazarus-DCP).cbz
- `   68 MB`  Heavy Metal/01. Main Series/Heavy Metal v07 11 (1984-02) (c2c) (Lazarus-DCP).cbz

### heavy metal — v27 — #01  — identical size  *(volume)*

- `   67 MB`  Heavy Metal/Heavy Metal Vols 01-35 (1977-2012)/Heavy Metal v27 01 (2003) (svengali-DCP).cbz
- `   67 MB`  Heavy Metal/01. Main Series/Heavy Metal v27 01 (2003) (svengali-DCP).cbz

### avengers — #009  *(issue)*

- `   77 MB`  Avengers/Avengers Vol. 07 (001-011,672-690)(2017-2018)(digital)/Avengers 009 (2017) (digital) (Minutemen-Slayer).cbr
- `   58 MB`  Avengers/Avengers (2018-2019)/Avengers 009 (2018) (Digital) (Zone-Empire).cbr

### heavy metal — v33 — #05  — identical size  *(volume)*

- `   67 MB`  Heavy Metal/Heavy Metal Vols 01-35 (1977-2012)/Heavy Metal v33 05 (2009) (Arcane Special) (svengali-DCP).cbz
- `   67 MB`  Heavy Metal/01. Main Series/Heavy Metal v33 05 (2009) (Arcane Special) (svengali-DCP).cbz

### black max — v1  — identical size  *(volume)*

- `   67 MB`  Black Max v01 (2018) (digital) (Torquemada).cbr
- `   67 MB`  2000AD - Collections /Black Max/Black Max v01 (2018) (digital) (Torquemada).cbr

### heavy metal — v3 — #07  — identical size  *(volume)*

- `   67 MB`  Heavy Metal/Heavy Metal Vols 01-35 (1977-2012)/Heavy Metal v03 07 (1979-11) (c2c).cbz
- `   67 MB`  Heavy Metal/01. Main Series/Heavy Metal v03 07 (1979-11) (c2c).cbz

### miracleman — #011  *(issue)*

- `   82 MB`  Miracleman/Miracleman v1 (001-016) (2014-2015) GetComics.INFO/Miracleman 011 (2014) (Digital) (Darkness-Empire).cbr
- `   26 MB`  Alan Moore/Alan Moore Essentials/Alan Moore 1984- Miracleman/Miracleman #011.cbr
- `   26 MB`  Alan Moore/Alan Moore Collection I- English Invasion/Alan Moore Collection III- 2000 AD/Miracleman/Miracleman/Miracleman #011.cbr

### heavy metal — v2 — #04  — identical size  *(volume)*

- `   67 MB`  Heavy Metal/Heavy Metal Vols 01-35 (1977-2012)/Heavy Metal v02 04 (1978-08).cbr
- `   67 MB`  Heavy Metal/01. Main Series/Heavy Metal v02 04 (1978-08).cbr

### heavy metal — v4 — #01  — identical size  *(volume)*

- `   66 MB`  Heavy Metal/Heavy Metal Vols 01-35 (1977-2012)/Heavy Metal v04 01 (1980-04) (c2c) (Lazarus-DCP).cbz
- `   66 MB`  Heavy Metal/01. Main Series/Heavy Metal v04 01 (1980-04) (c2c) (Lazarus-DCP).cbz

### heavy metal — v8 — #04  — identical size  *(volume)*

- `   66 MB`  Heavy Metal/Heavy Metal Vols 01-35 (1977-2012)/Heavy Metal v08 04 (1984-07) (c2c) (Lazarus-DCP).cbz
- `   66 MB`  Heavy Metal/01. Main Series/Heavy Metal v08 04 (1984-07) (c2c) (Lazarus-DCP).cbz

### heavy metal — v8 — #09  — identical size  *(volume)*

- `   66 MB`  Heavy Metal/Heavy Metal Vols 01-35 (1977-2012)/Heavy Metal v08 09 (1984-12) (c2c) (Lazarus-DCP).cbz
- `   66 MB`  Heavy Metal/01. Main Series/Heavy Metal v08 09 (1984-12) (c2c) (Lazarus-DCP).cbz

### heavy metal — v8 — #08  — identical size  *(volume)*

- `   65 MB`  Heavy Metal/Heavy Metal Vols 01-35 (1977-2012)/Heavy Metal v08 08 (1984-11) (c2c) (Lazarus-DCP).cbz
- `   65 MB`  Heavy Metal/01. Main Series/Heavy Metal v08 08 (1984-11) (c2c) (Lazarus-DCP).cbz

### freak angels — #005  — identical size  *(issue)*

- `   65 MB`  Warren Ellis/Freak Angels/Freak Angels 005 - collection (097-120).cbr
- `   65 MB`  Warren Ellis/2008/2008 Freak Angels/Freak Angels 005 - collection (097-120).cbr

### heavy metal — v9 — #01  — identical size  *(volume)*

- `   65 MB`  Heavy Metal/Heavy Metal Vols 01-35 (1977-2012)/Heavy Metal v09 01 (1985-04) (c2c) (Lazarus-DCP) (mislabel v09 13).cbz
- `   65 MB`  Heavy Metal/01. Main Series/Heavy Metal v09 01 (1985-04) (c2c) (Lazarus-DCP) (mislabel v09 13).cbz

### heavy metal — v33 — #04  — identical size  *(volume)*

- `   65 MB`  Heavy Metal/Heavy Metal Vols 01-35 (1977-2012)/Heavy Metal v33 04 (2009) (svengali-DCP).cbz
- `   65 MB`  Heavy Metal/01. Main Series/Heavy Metal v33 04 (2009) (svengali-DCP).cbz

### nikolai dante — #03  *(issue)*

- `  128 MB`  2000AD - Collections /The Complete Nikolai Dante/Nikolai Dante 03 - Love and War (2014) (Digital) (DR & Quinch-Empire).cbr
- `    2 MB`  2000AD - Collections /The Complete Nikolai Dante/Covers/Nikolai Dante 03 - Love and War (TPB Cvr Only) (2014) (Digital) (DR & Quinch-Empire).cbr

### 2000ad prog — #2272  — identical size  *(issue)*

- `   43 MB`  Dan Abnett/new Brink/2000AD prog 2272 (2022) (digital) (Minutemen-juvecube).cbr
- `   43 MB`  2000AD prog/new Brink/2000AD prog 2272 (2022) (digital) (Minutemen-juvecube).cbr
- `   43 MB`  2000AD prog/2000AD prog 2272 (2022) (digital) (Minutemen-juvecube).cbr

### heavy metal — v1 — #10  — identical size  *(volume)*

- `   65 MB`  Heavy Metal/Heavy Metal Vols 01-35 (1977-2012)/Heavy Metal v01 10 (1978-01) (Lazarus-DCP).cbz
- `   65 MB`  Heavy Metal/01. Main Series/Heavy Metal v01 10 (1978-01) (Lazarus-DCP).cbz

### button man — v3  *(volume)*

- `   70 MB`  2000AD - Collections /Button Man/Button Man v03 - Killer Killer (2009) (digital SD) (Ampersand).cbr
- `   60 MB`  2000AD - Collections /Button Man V3 Killer Killer (Dan Dare 2000AD Remix).cbr

### heavy metal presents is man good  — identical size  *(issue)*

- `   43 MB`  Jodorowsky and Moebius/Heavy Metal Presents - Is Man Good (1978) (FPScans).cbr
- `   43 MB`  Heavy Metal/Heavy Metal Presents/Heavy Metal Presents - Is Man Good (1978) (FPScans).cbr
- `   43 MB`  Heavy Metal/03. Extras/Heavy Metal Presents - Is Man Good (1978) (FPScans).cbr

### moebius stories from heavy metal  — identical size  *(issue)*

- `   64 MB`  Jodorowsky and Moebius/Moebius - Stories From Heavy Metal.cbr
- `   64 MB`  Heavy Metal/Moebius - Stories From Heavy Metal.cbr

### heavy metal — v11 — #02  — identical size  *(volume)*

- `   64 MB`  Heavy Metal/Heavy Metal Vols 01-35 (1977-2012)/Heavy Metal v11 02 (1987).cbz
- `   64 MB`  Heavy Metal/01. Main Series/Heavy Metal v11 02 (1987).cbz

### alan moore's light of thy countenance  — identical size  *(issue)*

- `   43 MB`  Light of Thy Countenance/Alan Moore's Light of Thy Countenance.cbr
- `   43 MB`  Alan Moore/Alan Moore's Light of Thy Countenance.cbr
- `   43 MB`  Alan Moore/Alan Moore Collection VI- Made For Moore/Alan Moore's Light Of Thy Countenance.cbr

### alan moore's lost girls — v1  — identical size  *(volume)*

- `   64 MB`  Alan Moore/Alan Moore Essentials/Alan Moore 1992- Lost Girls Book/Alan Moore's Lost Girls Book #001.cbr
- `   64 MB`  Alan Moore/Alan Moore Collection V- More Moore/Lost Girls Book/Lost Girls Book (3 Volume)/Alan Moore's Lost Girls Book #001.cbr

### heavy metal — v9 — #04  — identical size  *(volume)*

- `   64 MB`  Heavy Metal/Heavy Metal Vols 01-35 (1977-2012)/Heavy Metal v09 04 (1985-07) (c2c) (Lazarus-DCP).cbz
- `   64 MB`  Heavy Metal/01. Main Series/Heavy Metal v09 04 (1985-07) (c2c) (Lazarus-DCP).cbz

### judge dredd cape & cowl crimes  — identical size  *(issue)*

- `   64 MB`  Judge Dredd - Collections/Judge Dredd - Cape & Cowl Crimes (2017) (digital) (JeffAlbertson-DCP)/Judge Dredd - Cape & Cowl Crimes (2017) (digital) (JeffAlbertson-DCP).cbz
- `   64 MB`  2000AD - Collections /Judge Dredd/Judge Dredd - Cape & Cowl Crimes (2017) (2000AD) (digital) (JeffAlbertson-DCP).cbz

### alan moore's lost girls — v2  — identical size  *(volume)*

- `   64 MB`  Alan Moore/Alan Moore Essentials/Alan Moore 1992- Lost Girls Book/Alan Moore's Lost Girls Book #002.cbr
- `   64 MB`  Alan Moore/Alan Moore Collection V- More Moore/Lost Girls Book/Lost Girls Book (3 Volume)/Alan Moore's Lost Girls Book #002.cbr

### brass sun — v4  — identical size  *(volume)*

- `   64 MB`  Brass Sun/Brass Sun V4 Motor Head (Dan Dare 2000AD Remix).cbr
- `   64 MB`  2000AD - Collections /Brass Sun/Brass Sun V4 Motor Head (Dan Dare 2000AD Remix).cbr

### avengers — #011  *(issue)*

- `   66 MB`  Avengers/Avengers Vol. 07 (001-011,672-690)(2017-2018)(digital)/Avengers 011 (2017) (digital) (Minutemen-Slayer).cbr
- `   34 MB`  Avengers/Avengers (2018-2019)/Avengers 011 (2019) (Digital) (Zone-Empire).cbr
- `   27 MB`  Alias  ( Jessica Jones , The Pulse & Appearances)/Appearances/Avengers (2010)/Avengers 011 (2011) (two covers) (fixed) (Minutemen-DTs&Saxon).cbr

### heavy metal — v7 — #10  — identical size  *(volume)*

- `   64 MB`  Heavy Metal/Heavy Metal Vols 01-35 (1977-2012)/Heavy Metal v07 10 (1984-01) (c2c) (Lazarus-DCP).cbz
- `   64 MB`  Heavy Metal/01. Main Series/Heavy Metal v07 10 (1984-01) (c2c) (Lazarus-DCP).cbz

### 2000ad prog — #2278  — identical size  *(issue)*

- `   42 MB`  Dan Abnett/new Brink/2000AD prog 2278 (2022) (digital) (Minutemen-juvecube).cbr
- `   42 MB`  2000AD prog/new Brink/2000AD prog 2278 (2022) (digital) (Minutemen-juvecube).cbr
- `   42 MB`  2000AD prog/2000AD prog 2278 (2022) (digital) (Minutemen-juvecube).cbr

### heavy metal — v1 — #13  — identical size  *(volume)*

- `   63 MB`  Heavy Metal/Heavy Metal Vols 01-35 (1977-2012)/Heavy Metal v01 13 (1978-04) (c2c) (Lazarus-DCP).cbz
- `   63 MB`  Heavy Metal/01. Main Series/Heavy Metal v01 13 (1978-04) (c2c) (Lazarus-DCP).cbz

### hellboy midnight circus  *(issue)*

- `   82 MB`  Hellboy/Hellboy - The Midnight Circus (2013) (digital) (Son of Ultron II-Empire).cbr
- `   44 MB`  Hellboy/30.)  Hellboy - The Midnight Circus  (1948 AD)/Hellboy - The Midnight Circus.cbr

### heavy metal — v2 — #05  — identical size  *(volume)*

- `   63 MB`  Heavy Metal/Heavy Metal Vols 01-35 (1977-2012)/Heavy Metal v02 05 (1978-09).cbr
- `   63 MB`  Heavy Metal/01. Main Series/Heavy Metal v02 05 (1978-09).cbr

### night cry  *(issue)*

- `   77 MB`  Europe Comics (Collection)/Night Cry (2021) (digital) (Mr Norrell-Empire).cbr
- `   50 MB`  Europe Comics (Collection)/Night Cry (Europe Comics 2021) (webrip) (MagicMan-DCP).cbr

### miracleman — #006  *(issue)*

- `   73 MB`  Miracleman/Miracleman v1 (001-016) (2014-2015) GetComics.INFO/Miracleman 006 (2014) (Digital) (Darkness-Empire).cbr
- `   27 MB`  Alan Moore/Alan Moore Essentials/Alan Moore 1984- Miracleman/Miracleman #006.cbr
- `   27 MB`  Alan Moore/Alan Moore Collection I- English Invasion/Alan Moore Collection III- 2000 AD/Miracleman/Miracleman/Miracleman #006.cbr

### heavy metal — v33 — #09  — identical size  *(volume)*

- `   63 MB`  Heavy Metal/Heavy Metal Vols 01-35 (1977-2012)/Heavy Metal v33 09 (2010) (svengali-DCP).cbr
- `   63 MB`  Heavy Metal/01. Main Series/Heavy Metal v33 09 (2010) (svengali-DCP).cbr

### alan moore's lost girls — v3  — identical size  *(volume)*

- `   63 MB`  Alan Moore/Alan Moore Essentials/Alan Moore 1992- Lost Girls Book/Alan Moore's Lost Girls Book #003.cbr
- `   63 MB`  Alan Moore/Alan Moore Collection V- More Moore/Lost Girls Book/Lost Girls Book (3 Volume)/Alan Moore's Lost Girls Book #003.cbr

### heavy metal — v10 — #01  — identical size  *(volume)*

- `   63 MB`  Heavy Metal/Heavy Metal Vols 01-35 (1977-2012)/Heavy Metal v10 01 (1986-Spring) (brigus).cbr
- `   63 MB`  Heavy Metal/01. Main Series/Heavy Metal v10 01 (1986-Spring) (brigus).cbr

### clive barkers nightbreed — #006  *(issue)*

- `   65 MB`  Clive Barker/Clive Barker s Nightbreed v2 (001-012+)(2014-2017)(digital)(Minutemen-Slayer)/Clive Barkers Nightbreed 006 (2014) (digital) (Minutemen-Slayer).cbr
- `   60 MB`  Clive Barker/Clive Barker s Nightbreed 001-012 (2014-2015)/Clive Barker s Nightbreed 001-012 (2014-2015)/Clive Barkers Nightbreed 006 (2014) (Digital-Empire).cbr

### heavy metal — v13 — #03  — identical size  *(volume)*

- `   62 MB`  Heavy Metal/Heavy Metal Vols 01-35 (1977-2012)/Heavy Metal v13 03 (1989).cbr
- `   62 MB`  Heavy Metal/01. Main Series/Heavy Metal v13 03 (1989).cbr

### miracleman — #009  *(issue)*

- `   74 MB`  Miracleman/Miracleman v1 (001-016) (2014-2015) GetComics.INFO/Miracleman 009 (2014) (Digital) (Darkness-Empire).cbr
- `   26 MB`  Alan Moore/Alan Moore Essentials/Alan Moore 1984- Miracleman/Miracleman #009.cbr
- `   26 MB`  Alan Moore/Alan Moore Collection I- English Invasion/Alan Moore Collection III- 2000 AD/Miracleman/Miracleman/Miracleman #009.cbr

### 2000ad prog 2004  *(issue)*

- `   43 MB`  2000AD prog/2000AD prog 2004 (2016) (digital) (juvecube).cbr
- `   41 MB`  2000AD prog/Yearbooks & Specials/Yearbooks (2000-2015)/2000AD Prog 2004 (2003).cbr
- `   41 MB`  2000AD prog/2000AD (Specials, Annuals & Poster Progs + Extras)/2000AD Yearbooks & Specials (1977 - 2013)/2000AD Yearbooks (Prog 2000 - 2013)/2000AD Prog 2004.cbr

### 2000ad prog 2000  *(issue)*

- `   73 MB`  2000AD prog/2000AD prog 2000 (2016) (2 covers) (digital) (juvecube).cbr
- `   51 MB`  2000AD prog/2000AD (Specials, Annuals & Poster Progs + Extras)/2000AD Yearbooks & Specials (1977 - 2013)/2000AD Yearbooks (Prog 2000 - 2013)/2000AD Prog 2000.cbr

### miracleman — #010  *(issue)*

- `   78 MB`  Miracleman/Miracleman v1 (001-016) (2014-2015) GetComics.INFO/Miracleman 010 (2014) (Digital) (Darkness-Empire).cbr
- `   23 MB`  Alan Moore/Alan Moore Essentials/Alan Moore 1984- Miracleman/Miracleman #010.cbr
- `   23 MB`  Alan Moore/Alan Moore Collection I- English Invasion/Alan Moore Collection III- 2000 AD/Miracleman/Miracleman/Miracleman #010.cbr

### heavy metal — v3 — #03  — identical size  *(volume)*

- `   62 MB`  Heavy Metal/Heavy Metal Vols 01-35 (1977-2012)/Heavy Metal v03 03 (1979-07) (c2c) (Lazarus-DCP).cbz
- `   62 MB`  Heavy Metal/01. Main Series/Heavy Metal v03 03 (1979-07) (c2c) (Lazarus-DCP).cbz

### heavy metal — v7 — #09  — identical size  *(volume)*

- `   62 MB`  Heavy Metal/Heavy Metal Vols 01-35 (1977-2012)/Heavy Metal v07 09 (1983-12) (Lazarus-DCP).cbz
- `   62 MB`  Heavy Metal/01. Main Series/Heavy Metal v07 09 (1983-12) (Lazarus-DCP).cbz

### heavy metal — v26 — #02  — identical size  *(volume)*

- `   62 MB`  Heavy Metal/Heavy Metal Vols 01-35 (1977-2012)/Heavy Metal v26 02 (2002).cbr
- `   62 MB`  Heavy Metal/01. Main Series/Heavy Metal v26 02 (2002).cbr

### heavy metal — v9 — #08  — identical size  *(volume)*

- `   61 MB`  Heavy Metal/Heavy Metal Vols 01-35 (1977-2012)/Heavy Metal v09 08 (1985-11) (c2c) (Lazarus-DCP).cbz
- `   61 MB`  Heavy Metal/01. Main Series/Heavy Metal v09 08 (1985-11) (c2c) (Lazarus-DCP).cbz

### heavy metal — v7 — #08  — identical size  *(volume)*

- `   61 MB`  Heavy Metal/Heavy Metal Vols 01-35 (1977-2012)/Heavy Metal v07 08 (1983-11) (Lazarus-DCP).cbz
- `   61 MB`  Heavy Metal/01. Main Series/Heavy Metal v07 08 (1983-11) (Lazarus-DCP).cbz

### heavy metal — v9 — #09  — identical size  *(volume)*

- `   61 MB`  Heavy Metal/Heavy Metal Vols 01-35 (1977-2012)/Heavy Metal v09 09 (1985-12) (c2c) (Lazarus-DCP).cbz
- `   61 MB`  Heavy Metal/01. Main Series/Heavy Metal v09 09 (1985-12) (c2c) (Lazarus-DCP).cbz

### heavy metal — v8 — #01  — identical size  *(volume)*

- `   61 MB`  Heavy Metal/Heavy Metal Vols 01-35 (1977-2012)/Heavy Metal v08 01 (1984-04).cbr
- `   61 MB`  Heavy Metal/01. Main Series/Heavy Metal v08 01 (1984-04).cbr

### 2000ad prog — #2277  — identical size  *(issue)*

- `   41 MB`  Dan Abnett/new Brink/2000AD prog 2277 (2022) (digital) (Minutemen-juvecube).cbr
- `   41 MB`  2000AD prog/new Brink/2000AD prog 2277 (2022) (digital) (Minutemen-juvecube).cbr
- `   41 MB`  2000AD prog/2000AD prog 2277 (2022) (digital) (Minutemen-juvecube).cbr

### heavy metal — v28 — #01  — identical size  *(volume)*

- `   61 MB`  Heavy Metal/Heavy Metal Vols 01-35 (1977-2012)/Heavy Metal v28 01 (2004).cbr
- `   61 MB`  Heavy Metal/01. Main Series/Heavy Metal v28 01 (2004).cbr

### hondo city law  — identical size  *(issue)*

- `   61 MB`  Hondo City Law (2011) (digital) (JeffAlbertson-DCP).cbz
- `   61 MB`  2000AD - Collections /Hondo City/Hondo City Law (2011) (2000AD) (digital) (JeffAlbertson-DCP).cbz

### love & rockets new stories — #01  *(issue)*

- `  106 MB`  Hernandez brothers/Love and Rockets/Love & Rockets v3 New Stories (001-008)(2008-2016)(digital)/Love & Rockets - New Stories 01 (2008) (digital-Empire).cbz
- `   16 MB`  Hernandez brothers/Love and Rockets/Love & Rockets v3 New Stories (001-008)(2008-2016)(digital)/Love & Rockets - New Stories 01 (FCBD) (2009) (Minutemen-DTs).cbz

### heavy metal — v28 — #03  — identical size  *(volume)*

- `   61 MB`  Heavy Metal/Heavy Metal Vols 01-35 (1977-2012)/Heavy Metal v28 03 (2004) (Humperdido).cbr
- `   61 MB`  Heavy Metal/01. Main Series/Heavy Metal v28 03 (2004) (Humperdido).cbr

### heavy metal — v10 — #02  — identical size  *(volume)*

- `   61 MB`  Heavy Metal/Heavy Metal Vols 01-35 (1977-2012)/Heavy Metal v10 02 (1986-Summer) (Humperdido).cbr
- `   61 MB`  Heavy Metal/01. Main Series/Heavy Metal v10 02 (1986-Summer) (Humperdido).cbr

### corto maltese — #03  — identical size  *(issue)*

- `   61 MB`  Hugo Pratt/Corto Maltese 03 - Caribbean Suite (Pratt, 2009) (Scanlation-Extended, 2015).cbr
- `   61 MB`  Corto Maltese/Corto Maltese 01-16/Corto Maltese 03 - Caribbean Suite (Pratt, 2009) (Scanlation-Extended, 2015).cbr

### heavy metal — v26 — #01  — identical size  *(volume)*

- `   61 MB`  Heavy Metal/Heavy Metal Vols 01-35 (1977-2012)/Heavy Metal v26 01 (2002).cbr
- `   61 MB`  Heavy Metal/01. Main Series/Heavy Metal v26 01 (2002).cbr

### miracleman — #007  *(issue)*

- `   72 MB`  Miracleman/Miracleman v1 (001-016) (2014-2015) GetComics.INFO/Miracleman 007 (2014) (Digital) (Darkness-Empire).cbr
- `   25 MB`  Alan Moore/Alan Moore Essentials/Alan Moore 1984- Miracleman/Miracleman #007.cbr
- `   25 MB`  Alan Moore/Alan Moore Collection I- English Invasion/Alan Moore Collection III- 2000 AD/Miracleman/Miracleman/Miracleman #007.cbr

### clive barkers nightbreed — #005  *(issue)*

- `   63 MB`  Clive Barker/Clive Barker s Nightbreed v2 (001-012+)(2014-2017)(digital)(Minutemen-Slayer)/Clive Barkers Nightbreed 005 (2014) (digital) (Minutemen-Slayer).cbr
- `   58 MB`  Clive Barker/Clive Barker s Nightbreed 001-012 (2014-2015)/Clive Barker s Nightbreed 001-012 (2014-2015)/Clive Barkers Nightbreed 005 (2014) (Digital-Empire).cbr

### heavy metal — v10 — #04  — identical size  *(volume)*

- `   60 MB`  Heavy Metal/Heavy Metal Vols 01-35 (1977-2012)/Heavy Metal v10 04 (1987) (c2c) (Fixed) (CalexicoCA).cbr
- `   60 MB`  Heavy Metal/01. Main Series/Heavy Metal v10 04 (1987) (c2c) (Fixed) (CalexicoCA).cbr

### heavy metal — v9 — #10  — identical size  *(volume)*

- `   60 MB`  Heavy Metal/Heavy Metal Vols 01-35 (1977-2012)/Heavy Metal v09 10 (1986-Winter) (brigus).cbr
- `   60 MB`  Heavy Metal/01. Main Series/Heavy Metal v09 10 (1986-Winter) (brigus).cbr

### heavy metal — v3 — #05  — identical size  *(volume)*

- `   60 MB`  Heavy Metal/Heavy Metal Vols 01-35 (1977-2012)/Heavy Metal v03 05 (1979-09) (c2c).cbz
- `   60 MB`  Heavy Metal/01. Main Series/Heavy Metal v03 05 (1979-09) (c2c).cbz

### heavy metal — v33 — #07  — identical size  *(volume)*

- `   60 MB`  Heavy Metal/Heavy Metal Vols 01-35 (1977-2012)/Heavy Metal v33 07 (2009) (svengali-DCP).cbr
- `   60 MB`  Heavy Metal/01. Main Series/Heavy Metal v33 07 (2009) (svengali-DCP).cbr

### 2000ad prog — #2200  *(issue)*

- `   60 MB`  2000AD prog/2000AD prog 2200 (2020) (digital) (Minutemen-juvecube).cbr
- `   59 MB`  2000AD prog/2000AD prog 2200 (2020) (Digital-Empire).cbr

### heavy metal — v33 — #02  — identical size  *(volume)*

- `   59 MB`  Heavy Metal/Heavy Metal Vols 01-35 (1977-2012)/Heavy Metal v33 02 (2009) (Cryptic Special) (svengali-DCP).cbz
- `   59 MB`  Heavy Metal/01. Main Series/Heavy Metal v33 02 (2009) (Cryptic Special) (svengali-DCP).cbz

### heavy metal — v32 — #03  — identical size  *(volume)*

- `   59 MB`  Heavy Metal/Heavy Metal Vols 01-35 (1977-2012)/Heavy Metal v32 03 (2008) (svengali-DCP).cbr
- `   59 MB`  Heavy Metal/01. Main Series/Heavy Metal v32 03 (2008) (svengali-DCP).cbr

### nikolai dante — #05  *(issue)*

- `  116 MB`  2000AD - Collections /The Complete Nikolai Dante/Nikolai Dante 05 - Tsar Wars v02 (2007) (Digital) (DR & Quinch-Empire).cbr
- `    2 MB`  2000AD - Collections /The Complete Nikolai Dante/Covers/Nikolai Dante 05 - Tsar Wars Vol 2 (TPB Cvr Only) (2007) (Digital) (DR & Quinch-Empire).cbr

### 2000ad prog — #2276  — identical size  *(issue)*

- `   39 MB`  Dan Abnett/new Brink/2000AD prog 2276 (2022) (digital) (Minutemen-juvecube).cbr
- `   39 MB`  2000AD prog/new Brink/2000AD prog 2276 (2022) (digital) (Minutemen-juvecube).cbr
- `   39 MB`  2000AD prog/2000AD prog 2276 (2022) (digital) (Minutemen-juvecube).cbr

### heavy metal — v18 — #05  — identical size  *(volume)*

- `   59 MB`  Heavy Metal/Heavy Metal Vols 01-35 (1977-2012)/Heavy Metal v18 05 (1994-11) (Humperdido).cbr
- `   59 MB`  Heavy Metal/01. Main Series/Heavy Metal v18 05 (1994-11) (Humperdido).cbr

### creator owned heroes — #07  *(issue)*

- `   91 MB`  Image comics/Creator Owned Heroes (001-008)(2012-2013)/Creator Owned Heroes 07 (2012) (2 Covers) (Tarutaru-Novus-HD).cbr
- `   27 MB`  Image comics/Creator Owned Heroes (001-008)(2012-2013)/Creator-Owned Heroes 07 (2012) (Digital) (K6DVR-Empire).cbr

### heavy metal — v34 — #05  — identical size  *(volume)*

- `   59 MB`  Heavy Metal/Heavy Metal Vols 01-35 (1977-2012)/Heavy Metal v34 05 (2010) (Forbidden Special) (c2c) (svengali-DCP).cbr
- `   59 MB`  Heavy Metal/01. Main Series/Heavy Metal v34 05 (2010) (Forbidden Special) (c2c) (svengali-DCP).cbr

### miracleman — #004  *(issue)*

- `   53 MB`  Miracleman/Miracleman v1 (001-016) (2014-2015) GetComics.INFO/Miracleman 004 (2014) (Digital) (Darkness-Empire).cbr
- `   32 MB`  Alan Moore/Alan Moore Essentials/Alan Moore 1984- Miracleman/Miracleman #004.cbr
- `   32 MB`  Alan Moore/Alan Moore Collection I- English Invasion/Alan Moore Collection III- 2000 AD/Miracleman/Miracleman/Miracleman #004.cbr

### heavy metal — v19 — #01  — identical size  *(volume)*

- `   59 MB`  Heavy Metal/Heavy Metal Vols 01-35 (1977-2012)/Heavy Metal v19 01 (1995-03) (Humperdido).cbr
- `   59 MB`  Heavy Metal/01. Main Series/Heavy Metal v19 01 (1995-03) (Humperdido).cbr

### bettie page halloween  *(special)*

- `   65 MB`  Bettie Page/Bettie Page Halloween Special (2019) (digital) (d'argh-Empire).cbr
- `   52 MB`  Bettie Page/Bettie Page Halloween Special (2018) (digital-Empire).cbr

### heavy metal — v33 — #01  — identical size  *(volume)*

- `   58 MB`  Heavy Metal/Heavy Metal Vols 01-35 (1977-2012)/Heavy Metal v33 01 (2009) (svengali-DCP).cbr
- `   58 MB`  Heavy Metal/01. Main Series/Heavy Metal v33 01 (2009) (svengali-DCP).cbr

### interceptor  — identical size  *(issue)*

- `   58 MB`  Interceptor.cbz
- `   58 MB`  2000AD - Collections /Interceptor/Interceptor.cbz

### heavy metal — v24 — #01  — identical size  *(volume)*

- `   58 MB`  Heavy Metal/Heavy Metal Vols 01-35 (1977-2012)/Heavy Metal v24 01 (2000).cbr
- `   58 MB`  Heavy Metal/01. Main Series/Heavy Metal v24 01 (2000).cbr

### heavy metal — v9 — #05  — identical size  *(volume)*

- `   58 MB`  Heavy Metal/Heavy Metal Vols 01-35 (1977-2012)/Heavy Metal v09 05 (1985-08) (c2c) (Lazarus-DCP).cbz
- `   58 MB`  Heavy Metal/01. Main Series/Heavy Metal v09 05 (1985-08) (c2c) (Lazarus-DCP).cbz

### heavy metal — v17 — #03  — identical size  *(volume)*

- `   58 MB`  Heavy Metal/Heavy Metal Vols 01-35 (1977-2012)/Heavy Metal v17 03 (1993-07) (Humperdido).cbr
- `   58 MB`  Heavy Metal/01. Main Series/Heavy Metal v17 03 (1993-07) (Humperdido).cbr

### shadow's treasure  — identical size  *(issue)*

- `   58 MB`  The Shadow's Treasure.cbr
- `   58 MB`  Jodorowsky and Moebius/The Shadow's Treasure.cbr

### transporter — #003  *(issue)*

- `   75 MB`  Europe Comics (Collection)/The Transporter 003 - Bound by Darkness (2022) (digital) (Mr Norrell-Empire).cbr
- `   41 MB`  The Transporter/The Transporter 003 - Bound by Darkness (Europe Comics 2022) (webrip) (MagicMan-DCP).cbr

### heavy metal — v31 — #04  — identical size  *(volume)*

- `   58 MB`  Heavy Metal/Heavy Metal Vols 01-35 (1977-2012)/Heavy Metal v31 04 (2007) (svengali-DCP).cbz
- `   58 MB`  Heavy Metal/01. Main Series/Heavy Metal v31 04 (2007) (svengali-DCP).cbz

### detection club — #01  — identical size  *(issue)*

- `   58 MB`  Europe Comics (Collection)/The Detection Club 01-02 (2020)/The Detection Club 01 (2020) (webrip) (MagicMan-DCP).cbr
- `   58 MB`  Europe Comics (Collection)/The Detection Club 01 (Europe Comics 2020) (webrip) (MagicMan-DCP).cbr

### clive barkers nightbreed — #012  *(issue)*

- `   58 MB`  Clive Barker/Clive Barker s Nightbreed 001-012 (2014-2015)/Clive Barker s Nightbreed 001-012 (2014-2015)/Clive Barkers Nightbreed 012 (2015) (Digital) (Mephisto-Empire).cbr
- `   58 MB`  Clive Barker/Clive Barker s Nightbreed v2 (001-012+)(2014-2017)(digital)(Minutemen-Slayer)/Clive Barkers Nightbreed 012 (2015) (digital) (Minutemen-Slayer).cbr

### 2000ad prog — #2273  — identical size  *(issue)*

- `   38 MB`  Dan Abnett/new Brink/2000AD prog 2273 (2022) (digital) (Minutemen-juvecube).cbr
- `   38 MB`  2000AD prog/new Brink/2000AD prog 2273 (2022) (digital) (Minutemen-juvecube).cbr
- `   38 MB`  2000AD prog/2000AD prog 2273 (2022) (digital) (Minutemen-juvecube).cbr

### 2000ad prog — #2287  — identical size  *(issue)*

- `   38 MB`  Dan Abnett/new Brink/2000AD prog 2287 (2022) (digital) (Minutemen-juvecube).cbr
- `   38 MB`  2000AD prog/new Brink/2000AD prog 2287 (2022) (digital) (Minutemen-juvecube).cbr
- `   38 MB`  2000AD prog/2000AD prog 2287 (2022) (digital) (Minutemen-juvecube).cbr

### heavy metal — v19 — #03  — identical size  *(volume)*

- `   57 MB`  Heavy Metal/Heavy Metal Vols 01-35 (1977-2012)/Heavy Metal v19 03 (1995-07) (Humperdido).cbr
- `   57 MB`  Heavy Metal/01. Main Series/Heavy Metal v19 03 (1995-07) (Humperdido).cbr

### heavy metal — v24 — #05  — identical size  *(volume)*

- `   57 MB`  Heavy Metal/Heavy Metal Vols 01-35 (1977-2012)/Heavy Metal v24 05 (2000).cbr
- `   57 MB`  Heavy Metal/01. Main Series/Heavy Metal v24 05 (2000).cbr

### 2000ad prog — #2274  — identical size  *(issue)*

- `   38 MB`  Dan Abnett/new Brink/2000AD prog 2274 (2022) (digital) (Minutemen-juvecube).cbr
- `   38 MB`  2000AD prog/new Brink/2000AD prog 2274 (2022) (digital) (Minutemen-juvecube).cbr
- `   38 MB`  2000AD prog/2000AD prog 2274 (2022) (digital) (Minutemen-juvecube).cbr

### 2000ad prog — #2275  — identical size  *(issue)*

- `   38 MB`  Dan Abnett/new Brink/2000AD prog 2275 (2022) (digital) (Minutemen-juvecube).cbr
- `   38 MB`  2000AD prog/new Brink/2000AD prog 2275 (2022) (digital) (Minutemen-juvecube).cbr
- `   38 MB`  2000AD prog/2000AD prog 2275 (2022) (digital) (Minutemen-juvecube).cbr

### heavy metal — v32 — #01  — identical size  *(volume)*

- `   57 MB`  Heavy Metal/Heavy Metal Vols 01-35 (1977-2012)/Heavy Metal v32 01 (2008-03) (svengali-DCP).cbz
- `   57 MB`  Heavy Metal/01. Main Series/Heavy Metal v32 01 (2008-03) (svengali-DCP).cbz

### heavy metal presents arzach  — identical size  *(issue)*

- `   57 MB`  Heavy Metal/Heavy Metal Presents/Heavy Metal Presents - Arzach (1977) (FPScans).cbr
- `   57 MB`  Heavy Metal/03. Extras/Heavy Metal Presents - Arzach (1977) (FPScans).cbr

### 2000ad prog — #2284  — identical size  *(issue)*

- `   38 MB`  Dan Abnett/new Brink/2000AD prog 2284 (2022) (digital) (Minutemen-juvecube).cbr
- `   38 MB`  2000AD prog/new Brink/2000AD prog 2284 (2022) (digital) (Minutemen-juvecube).cbr
- `   38 MB`  2000AD prog/2000AD prog 2284 (2022) (digital) (Minutemen-juvecube).cbr

### friends of spirou  — identical size  *(issue)*

- `   56 MB`  Spirou & Fantasio/Friends of Spirou (Europe Comics 2023) (webrip) (MagicMan-DCP).cbr
- `   56 MB`  Europe Comics (Collection)/Friends of Spirou (Europe Comics 2023) (webrip) (MagicMan-DCP).cbr

### cradlegrave  — identical size  *(issue)*

- `   56 MB`  Cradlegrave (2011) (digital-SD) (Torquemada).cbr
- `   56 MB`  2000AD - Collections /Cradlegrave (2011) (digital SD) (Torquemada).cbr

### heavy metal — v18 — #06  — identical size  *(volume)*

- `   56 MB`  Heavy Metal/Heavy Metal Vols 01-35 (1977-2012)/Heavy Metal v18 06 (1995).cbr
- `   56 MB`  Heavy Metal/01. Main Series/Heavy Metal v18 06 (1995).cbr

### heavy metal — v28 — #06  — identical size  *(volume)*

- `   56 MB`  Heavy Metal/Heavy Metal Vols 01-35 (1977-2012)/Heavy Metal v28 06 (2005).cbr
- `   56 MB`  Heavy Metal/01. Main Series/Heavy Metal v28 06 (2005).cbr

### clive barkers nightbreed — #011  *(issue)*

- `   57 MB`  Clive Barker/Clive Barker s Nightbreed v2 (001-012+)(2014-2017)(digital)(Minutemen-Slayer)/Clive Barkers Nightbreed 011 (2015) (digital) (Minutemen-Slayer).cbr
- `   55 MB`  Clive Barker/Clive Barker s Nightbreed 001-012 (2014-2015)/Clive Barker s Nightbreed 001-012 (2014-2015)/Clive Barkers Nightbreed 011 (2015) (Digital-Empire).cbr

### 2000ad prog — #2279  — identical size  *(issue)*

- `   37 MB`  Dan Abnett/new Brink/2000AD prog 2279 (2022) (digital) (Minutemen-juvecube).cbr
- `   37 MB`  2000AD prog/new Brink/2000AD prog 2279 (2022) (digital) (Minutemen-juvecube).cbr
- `   37 MB`  2000AD prog/2000AD prog 2279 (2022) (digital) (Minutemen-juvecube).cbr

### heavy metal — v26 — #03  — identical size  *(volume)*

- `   56 MB`  Heavy Metal/Heavy Metal Vols 01-35 (1977-2012)/Heavy Metal v26 03 (2002).cbr
- `   56 MB`  Heavy Metal/01. Main Series/Heavy Metal v26 03 (2002).cbr

### heavy metal — v31 — #05  — identical size  *(volume)*

- `   56 MB`  Heavy Metal/Heavy Metal Vols 01-35 (1977-2012)/Heavy Metal v31 05 (2007) (svengali-DCP).cbz
- `   56 MB`  Heavy Metal/01. Main Series/Heavy Metal v31 05 (2007) (svengali-DCP).cbz

### heavy metal — v19 — #04  — identical size  *(volume)*

- `   56 MB`  Heavy Metal/Heavy Metal Vols 01-35 (1977-2012)/Heavy Metal v19 04 (1995-09) (Humperdido).cbr
- `   56 MB`  Heavy Metal/01. Main Series/Heavy Metal v19 04 (1995-09) (Humperdido).cbr

### heavy metal — v19 — #05  — identical size  *(volume)*

- `   56 MB`  Heavy Metal/Heavy Metal Vols 01-35 (1977-2012)/Heavy Metal v19 05 (1995-11) (Humperdido).cbr
- `   56 MB`  Heavy Metal/01. Main Series/Heavy Metal v19 05 (1995-11) (Humperdido).cbr

### heavy metal — v15 — #01  — identical size  *(volume)*

- `   56 MB`  Heavy Metal/Heavy Metal Vols 01-35 (1977-2012)/Heavy Metal v15 01 (1991).cbr
- `   56 MB`  Heavy Metal/01. Main Series/Heavy Metal v15 01 (1991).cbr

### heavy metal — v1 — #12  — identical size  *(volume)*

- `   56 MB`  Heavy Metal/Heavy Metal Vols 01-35 (1977-2012)/Heavy Metal v01 12 (1978-03).cbr
- `   56 MB`  Heavy Metal/01. Main Series/Heavy Metal v01 12 (1978-03).cbr

### clive barkers nightbreed — #010  *(issue)*

- `   56 MB`  Clive Barker/Clive Barker s Nightbreed v2 (001-012+)(2014-2017)(digital)(Minutemen-Slayer)/Clive Barkers Nightbreed 010 (2015) (digital) (Minutemen-Slayer).cbr
- `   55 MB`  Clive Barker/Clive Barker s Nightbreed 001-012 (2014-2015)/Clive Barker s Nightbreed 001-012 (2014-2015)/Clive Barkers Nightbreed 010 (2015) (Digital-Empire).cbr

### heavy metal — v20 — #01  — identical size  *(volume)*

- `   55 MB`  Heavy Metal/Heavy Metal Vols 01-35 (1977-2012)/Heavy Metal v20 01 (1996).cbr
- `   55 MB`  Heavy Metal/01. Main Series/Heavy Metal v20 01 (1996).cbr

### heavy metal — v19 — #02  — identical size  *(volume)*

- `   55 MB`  Heavy Metal/Heavy Metal Vols 01-35 (1977-2012)/Heavy Metal v19 02 (1995-05) (Humperdido).cbr
- `   55 MB`  Heavy Metal/01. Main Series/Heavy Metal v19 02 (1995-05) (Humperdido).cbr

### 2000ad prog — #2281  — identical size  *(issue)*

- `   37 MB`  Dan Abnett/new Brink/2000AD prog 2281 (2022) (digital) (Minutemen-juvecube).cbr
- `   37 MB`  2000AD prog/new Brink/2000AD prog 2281 (2022) (digital) (Minutemen-juvecube).cbr
- `   37 MB`  2000AD prog/2000AD prog 2281 (2022) (digital) (Minutemen-juvecube).cbr

### heavy metal — v18 — #01  — identical size  *(volume)*

- `   55 MB`  Heavy Metal/Heavy Metal Vols 01-35 (1977-2012)/Heavy Metal v18 01 (1994-03) (Humperdido).cbr
- `   55 MB`  Heavy Metal/01. Main Series/Heavy Metal v18 01 (1994-03) (Humperdido).cbr

### heavy metal — v25 — #06  — identical size  *(volume)*

- `   55 MB`  Heavy Metal/Heavy Metal Vols 01-35 (1977-2012)/Heavy Metal v25 06 (2002) (Humperdido).cbr
- `   55 MB`  Heavy Metal/01. Main Series/Heavy Metal v25 06 (2002) (Humperdido).cbr

### clive barkers nightbreed — #001  *(issue)*

- `   57 MB`  Clive Barker/Clive Barker s Nightbreed v2 (001-012+)(2014-2017)(digital)(Minutemen-Slayer)/Clive Barkers Nightbreed 001 (2014) (digital) (Minutemen-Slayer).cbr
- `   53 MB`  Clive Barker/Clive Barker s Nightbreed 001-012 (2014-2015)/Clive Barker s Nightbreed 001-012 (2014-2015)/Clive Barkers Nightbreed 001 (2014) (Digital) (Fawkes-Empire).cbr

### heavy metal — v25 — #01  — identical size  *(volume)*

- `   55 MB`  Heavy Metal/Heavy Metal Vols 01-35 (1977-2012)/Heavy Metal v25 01 (2001) (Humperdido).cbr
- `   55 MB`  Heavy Metal/01. Main Series/Heavy Metal v25 01 (2001) (Humperdido).cbr

### heavy metal — v1 — #11  — identical size  *(volume)*

- `   55 MB`  Heavy Metal/Heavy Metal Vols 01-35 (1977-2012)/Heavy Metal v01 11 (1978-02).cbr
- `   55 MB`  Heavy Metal/01. Main Series/Heavy Metal v01 11 (1978-02).cbr

### heavy metal — v17 — #05  — identical size  *(volume)*

- `   55 MB`  Heavy Metal/Heavy Metal Vols 01-35 (1977-2012)/Heavy Metal v17 05 (v18 05) (1993-11).cbr
- `   55 MB`  Heavy Metal/01. Main Series/Heavy Metal v17 05 (v18 05) (1993-11).cbr

### mamma mia! — #01  — identical size  *(issue)*

- `   55 MB`  Lewis Trondheim/Mamma Mia! 01 - Just the Girls (2019) (Europe Comics) (Digital-Empire).cbr
- `   55 MB`  Europe Comics (Collection)/Mamma Mia! 01 - Just the Girls (2019) (Europe Comics) (Digital-Empire).cbr

### heavy metal — v2 — #06  — identical size  *(volume)*

- `   55 MB`  Heavy Metal/Heavy Metal Vols 01-35 (1977-2012)/Heavy Metal v02 06 (1978-10).cbr
- `   55 MB`  Heavy Metal/01. Main Series/Heavy Metal v02 06 (1978-10).cbr

### fire  *(issue)*

- `   86 MB`  Fire (2019) (digital) (Son of Ultron-Empire).cbr
- `   23 MB`  Brian Michael Bendis - Oeming/Fire (Brian Michael Bendis).cbr

### 2000ad prog — #2282  — identical size  *(issue)*

- `   36 MB`  Dan Abnett/new Brink/2000AD prog 2282 (2022) (digital) (Minutemen-juvecube).cbr
- `   36 MB`  2000AD prog/new Brink/2000AD prog 2282 (2022) (digital) (Minutemen-juvecube).cbr
- `   36 MB`  2000AD prog/2000AD prog 2282 (2022) (digital) (Minutemen-juvecube).cbr

### batman killing joke deluxe edition  — identical size  *(issue)*

- `   55 MB`  Alan Moore/Alan Moore Essentials/Alan Moore 1988- Batman- The Killing Joke/Batman- The Killing Joke- Deluxe Edition.cbr
- `   55 MB`  Alan Moore/Alan Moore Collection II-  DC/Batman/Batman- The Killing Joke/Batman- The Killing Joke- Deluxe Edition.cbr

### all new miracleman — #001  — identical size  *(annual)*

- `   55 MB`  Miracleman/Miracleman v1 (001-016) (2014-2015) GetComics.INFO/All-New Miracleman Annual 001 (2014) (Digital) (Darkness-Empire).cbr
- `   55 MB`  Miracleman/All-New Miracleman Annual 001 (2014) (Digital) (Darkness-Empire).cbr

### heavy metal — v32 — #06  — identical size  *(volume)*

- `   54 MB`  Heavy Metal/Heavy Metal Vols 01-35 (1977-2012)/Heavy Metal v32 06 (2009) (svengali-DCP).cbr
- `   54 MB`  Heavy Metal/01. Main Series/Heavy Metal v32 06 (2009) (svengali-DCP).cbr

### heavy metal — v31 — #03  — identical size  *(volume)*

- `   54 MB`  Heavy Metal/Heavy Metal Vols 01-35 (1977-2012)/Heavy Metal v31 03 (2007) (svengali-DCP).cbz
- `   54 MB`  Heavy Metal/01. Main Series/Heavy Metal v31 03 (2007) (svengali-DCP).cbz

### heavy metal — v30 — #02  — identical size  *(volume)*

- `   54 MB`  Heavy Metal/Heavy Metal Vols 01-35 (1977-2012)/Heavy Metal v30 02 (2006-05) (svengali-DCP).cbz
- `   54 MB`  Heavy Metal/01. Main Series/Heavy Metal v30 02 (2006-05) (svengali-DCP).cbz

### heavy metal — v21 — #02  — identical size  *(volume)*

- `   54 MB`  Heavy Metal/Heavy Metal Vols 01-35 (1977-2012)/Heavy Metal v21 02 (1997).cbr
- `   54 MB`  Heavy Metal/01. Main Series/Heavy Metal v21 02 (1997).cbr

### heavy metal — v32 — #07  — identical size  *(volume)*

- `   54 MB`  Heavy Metal/Heavy Metal Vols 01-35 (1977-2012)/Heavy Metal v32 07 (2008).cbr
- `   54 MB`  Heavy Metal/01. Main Series/Heavy Metal v32 07 (2008).cbr

### heavy metal — v20 — #03  — identical size  *(volume)*

- `   54 MB`  Heavy Metal/Heavy Metal Vols 01-35 (1977-2012)/Heavy Metal v20 03 (1996-07) (Humperdido).cbr
- `   54 MB`  Heavy Metal/01. Main Series/Heavy Metal v20 03 (1996-07) (Humperdido).cbr

### judge dredd carlos ezquerra  — identical size  *(volume)*

- `   54 MB`  Judge Dredd - Collections/Judge Dredd - The Carlos Ezquerra Collection (2017) (digital) (JeffAlbertson-DCP)/Judge Dredd - The Carlos Ezquerra Collection (2017) (digital) (JeffAlbertson-DCP).cbz
- `   54 MB`  2000AD - Collections /Judge Dredd/Judge Dredd - The Carlos Ezquerra Collection (2017) (2000AD) (digital) (JeffAlbertson-DCP).cbz

### heavy metal — v17 — #01  — identical size  *(volume)*

- `   54 MB`  Heavy Metal/Heavy Metal Vols 01-35 (1977-2012)/Heavy Metal v17 01 (v19 06) (1993-03).cbr
- `   54 MB`  Heavy Metal/01. Main Series/Heavy Metal v17 01 (v19 06) (1993-03).cbr

### heavy metal — v14 — #03  — identical size  *(volume)*

- `   54 MB`  Heavy Metal/Heavy Metal Vols 01-35 (1977-2012)/Heavy Metal v14 03 (1990).cbr
- `   54 MB`  Heavy Metal/01. Main Series/Heavy Metal v14 03 (1990).cbr

### after incal — v1  *(volume)*

- `   73 MB`  Jodorowsky and Moebius/Incal/03 After the Incal/After the Incal v01 - The New Dream (2014) (Humanoids) (digital) (Lynx-Empire).cbr
- `   34 MB`  Jodorowsky and Moebius/Incal/03 After the Incal/After the Incal Vol. 01 - The New Dream (2000) (digital-SD) (Minutemen-Excelsior).cbz

### heavy metal — v9 — #07  — identical size  *(volume)*

- `   54 MB`  Heavy Metal/Heavy Metal Vols 01-35 (1977-2012)/Heavy Metal v09 07 (1985-10) (c2c) (Icarus-DCP).cbr
- `   54 MB`  Heavy Metal/01. Main Series/Heavy Metal v09 07 (1985-10) (c2c) (Icarus-DCP).cbr

### clive barkers nightbreed — #002  *(issue)*

- `   55 MB`  Clive Barker/Clive Barker s Nightbreed v2 (001-012+)(2014-2017)(digital)(Minutemen-Slayer)/Clive Barkers Nightbreed 002 (2014) (digital) (Minutemen-Slayer).cbr
- `   51 MB`  Clive Barker/Clive Barker s Nightbreed 001-012 (2014-2015)/Clive Barker s Nightbreed 001-012 (2014-2015)/Clive Barkers Nightbreed 002 (2014) (Digital) (Fawkes-Empire).cbr

### brass sun — v3  — identical size  *(volume)*

- `   53 MB`  Brass Sun/Brass Sun V3 Floating Worlds (Dan Dare 2000AD Remix).cbr
- `   53 MB`  2000AD - Collections /Brass Sun/Brass Sun V3 Floating Worlds (Dan Dare 2000AD Remix).cbr

### heavy metal — v30 — #04  — identical size  *(volume)*

- `   53 MB`  Heavy Metal/Heavy Metal Vols 01-35 (1977-2012)/Heavy Metal v30 04 (2006) (svengali-DCP).cbz
- `   53 MB`  Heavy Metal/01. Main Series/Heavy Metal v30 04 (2006) (svengali-DCP).cbz

### 2000ad prog — #2283  — identical size  *(issue)*

- `   35 MB`  Dan Abnett/new Brink/2000AD prog 2283 (2022) (digital) (Minutemen-juvecube).cbr
- `   35 MB`  2000AD prog/new Brink/2000AD prog 2283 (2022) (digital) (Minutemen-juvecube).cbr
- `   35 MB`  2000AD prog/2000AD prog 2283 (2022) (digital) (Minutemen-juvecube).cbr

### heavy metal — v18 — #02  — identical size  *(volume)*

- `   53 MB`  Heavy Metal/Heavy Metal Vols 01-35 (1977-2012)/Heavy Metal v18 02 (1994-05) (Humperdido).cbr
- `   53 MB`  Heavy Metal/01. Main Series/Heavy Metal v18 02 (1994-05) (Humperdido).cbr

### corto maltese — #10  — identical size  *(issue)*

- `   53 MB`  Hugo Pratt/Corto Maltese 10 - Fable of Venice (Pratt, 2009) (edition 1.0) (Scanlation-Concise, 2018).cbr
- `   53 MB`  Corto Maltese/Corto Maltese 01-16/Corto Maltese 10 - Fable of Venice (Pratt, 2009) (edition 1.0) (Scanlation-Concise, 2018).cbr

### judge dredd megazine — #202  — identical size  *(issue)*

- `   53 MB`  Judge Dredd The Megazine/Judge Dredd Megazine v5 (201-400)(2002-ongoing)/Judge Dredd Megazine 202 (2003) (Antscan).cbr
- `   53 MB`  Alan Moore/Alan Moore Collection I- English Invasion/Alan Moore Collection III- 2000 AD/2000 AD/2000 AD- Reprints/Judge Dredd Magazine/Judge Dredd Megazine #202 (Tharg's Future-Shocks - The Bounty Hunters!).cbr

### button man — v4  *(volume)*

- `   58 MB`  2000AD - Collections /Button Man/Button Man v04 - The Hitmans Daughter (2010) (digital SD) (Ampersand).cbr
- `   48 MB`  2000AD - Collections /Button Man V4 The Hitmans Daughter (Dan Dare 2000AD Remix).cbr

### clive barkers nightbreed — #008  *(issue)*

- `   55 MB`  Clive Barker/Clive Barker s Nightbreed v2 (001-012+)(2014-2017)(digital)(Minutemen-Slayer)/Clive Barkers Nightbreed 008 (2014) (digital) (Minutemen-Slayer).cbr
- `   51 MB`  Clive Barker/Clive Barker s Nightbreed 001-012 (2014-2015)/Clive Barker s Nightbreed 001-012 (2014-2015)/Clive Barkers Nightbreed 008 (2014) (Digital-Empire).cbr

### 2000ad prog — #2285  — identical size  *(issue)*

- `   35 MB`  Dan Abnett/new Brink/2000AD prog 2285 (2022) (digital) (Minutemen-juvecube).cbr
- `   35 MB`  2000AD prog/new Brink/2000AD prog 2285 (2022) (digital) (Minutemen-juvecube).cbr
- `   35 MB`  2000AD prog/2000AD prog 2285 (2022) (digital) (Minutemen-juvecube).cbr

### heavy metal — v18 — #04  — identical size  *(volume)*

- `   53 MB`  Heavy Metal/Heavy Metal Vols 01-35 (1977-2012)/Heavy Metal v18 04 (1994-09) (Humperdido).cbr
- `   53 MB`  Heavy Metal/01. Main Series/Heavy Metal v18 04 (1994-09) (Humperdido).cbr

### clive barkers nightbreed — #007  *(issue)*

- `   55 MB`  Clive Barker/Clive Barker s Nightbreed v2 (001-012+)(2014-2017)(digital)(Minutemen-Slayer)/Clive Barkers Nightbreed 007 (2014) (digital) (Minutemen-Slayer).cbr
- `   50 MB`  Clive Barker/Clive Barker s Nightbreed 001-012 (2014-2015)/Clive Barker s Nightbreed 001-012 (2014-2015)/Clive Barkers Nightbreed 007 (2014) (Digital-Empire).cbr

### 2000ad prog — #2286  — identical size  *(issue)*

- `   35 MB`  Dan Abnett/new Brink/2000AD prog 2286 (2022) (digital) (Minutemen-juvecube).cbr
- `   35 MB`  2000AD prog/new Brink/2000AD prog 2286 (2022) (digital) (Minutemen-juvecube).cbr
- `   35 MB`  2000AD prog/2000AD prog 2286 (2022) (digital) (Minutemen-juvecube).cbr

### heavy metal — v20 — #04  — identical size  *(volume)*

- `   53 MB`  Heavy Metal/Heavy Metal Vols 01-35 (1977-2012)/Heavy Metal v20 04 (1996-09) (Humperdido).cbr
- `   53 MB`  Heavy Metal/01. Main Series/Heavy Metal v20 04 (1996-09) (Humperdido).cbr

### heavy metal — v14 — #05  — identical size  *(volume)*

- `   52 MB`  Heavy Metal/Heavy Metal Vols 01-35 (1977-2012)/Heavy Metal v14 05 (1990).cbr
- `   52 MB`  Heavy Metal/01. Main Series/Heavy Metal v14 05 (1990).cbr

### avengers — #004  *(issue)*

- `   56 MB`  Avengers/Avengers Vol. 07 (001-011,672-690)(2017-2018)(digital)/Avengers 004 (2017) (2 covers) (digital) (Minutemen-Slayer).cbr
- `   49 MB`  Avengers/Avengers (2018-2019)/Avengers 004 (2018) (Digital) (Zone-Empire).cbr

### heavy metal — v30 — #01  — identical size  *(volume)*

- `   52 MB`  Heavy Metal/Heavy Metal Vols 01-35 (1977-2012)/Heavy Metal v30 01 (2006-03) (svengali-DCP).cbz
- `   52 MB`  Heavy Metal/01. Main Series/Heavy Metal v30 01 (2006-03) (svengali-DCP).cbz

### heavy metal — v28 — #02  — identical size  *(volume)*

- `   52 MB`  Heavy Metal/Heavy Metal Vols 01-35 (1977-2012)/Heavy Metal v28 02 (2004) (Humperdido).cbr
- `   52 MB`  Heavy Metal/01. Main Series/Heavy Metal v28 02 (2004) (Humperdido).cbr

### heavy metal — v29 — #01  — identical size  *(volume)*

- `   52 MB`  Heavy Metal/Heavy Metal Vols 01-35 (1977-2012)/Heavy Metal v29 01 (2005).cbr
- `   52 MB`  Heavy Metal/01. Main Series/Heavy Metal v29 01 (2005).cbr

### heavy metal — v32 — #05  — identical size  *(volume)*

- `   52 MB`  Heavy Metal/Heavy Metal Vols 01-35 (1977-2012)/Heavy Metal v32 05 (2008) (svengali-DCP).cbr
- `   52 MB`  Heavy Metal/01. Main Series/Heavy Metal v32 05 (2008) (svengali-DCP).cbr

### heavy metal — v17 — #02  — identical size  *(volume)*

- `   52 MB`  Heavy Metal/Heavy Metal Vols 01-35 (1977-2012)/Heavy Metal v17 02 (v30 07) (1993-05).cbr
- `   52 MB`  Heavy Metal/01. Main Series/Heavy Metal v17 02 (v30 07) (1993-05).cbr

### heavy metal — v26 — #05  — identical size  *(volume)*

- `   52 MB`  Heavy Metal/Heavy Metal Vols 01-35 (1977-2012)/Heavy Metal v26 05 (2002).cbr
- `   52 MB`  Heavy Metal/01. Main Series/Heavy Metal v26 05 (2002).cbr

### heavy metal — v1 — #05  — identical size  *(volume)*

- `   52 MB`  Heavy Metal/Heavy Metal Vols 01-35 (1977-2012)/Heavy Metal v01 05 (1977-08) (Angelheart).cbr
- `   52 MB`  Heavy Metal/01. Main Series/Heavy Metal v01 05 (1977-08) (Angelheart).cbr

### judge dredd & strontium dog judgement day 2000ad books  — identical size  *(issue)*

- `   52 MB`  Judge Dredd - Collections/Judge Dredd & Strontium Dog-Judgement Day 2000AD Books.cbr
- `   52 MB`  2000AD - Collections /Judge Dredd/Judge Dredd & Strontium Dog-Judgement Day 2000AD Books.cbr

### heavy metal — v17 — #06  — identical size  *(volume)*

- `   52 MB`  Heavy Metal/Heavy Metal Vols 01-35 (1977-2012)/Heavy Metal v17 06 (1994-01) (Humperdido).cbr
- `   52 MB`  Heavy Metal/01. Main Series/Heavy Metal v17 06 (1994-01) (Humperdido).cbr

### heavy metal — v15 — #04  — identical size  *(volume)*

- `   52 MB`  Heavy Metal/Heavy Metal Vols 01-35 (1977-2012)/Heavy Metal v15 04 (1991).cbz
- `   52 MB`  Heavy Metal/01. Main Series/Heavy Metal v15 04 (1991).cbz

### heavy metal — v5 — #06  — identical size  *(volume)*

- `   52 MB`  Heavy Metal/Heavy Metal Vols 01-35 (1977-2012)/Heavy Metal v05 06 (1981-09).cbr
- `   52 MB`  Heavy Metal/01. Main Series/Heavy Metal v05 06 (1981-09).cbr

### heavy metal — v20 — #05  — identical size  *(volume)*

- `   52 MB`  Heavy Metal/Heavy Metal Vols 01-35 (1977-2012)/Heavy Metal v20 05 (1996-11) (Humperdido).cbr
- `   52 MB`  Heavy Metal/01. Main Series/Heavy Metal v20 05 (1996-11) (Humperdido).cbr

### heavy metal — v1 — #09  — identical size  *(volume)*

- `   52 MB`  Heavy Metal/Heavy Metal Vols 01-35 (1977-2012)/Heavy Metal v01 09 (1977-12).cbr
- `   52 MB`  Heavy Metal/01. Main Series/Heavy Metal v01 09 (1977-12).cbr

### heavy metal — v29 — #04  — identical size  *(volume)*

- `   51 MB`  Heavy Metal/Heavy Metal Vols 01-35 (1977-2012)/Heavy Metal v29 04 (2005).cbz
- `   51 MB`  Heavy Metal/01. Main Series/Heavy Metal v29 04 (2005).cbz

### heavy metal — v30 — #03  — identical size  *(volume)*

- `   51 MB`  Heavy Metal/Heavy Metal Vols 01-35 (1977-2012)/Heavy Metal v30 03 (2006-07) (svengali-DCP).cbz
- `   51 MB`  Heavy Metal/01. Main Series/Heavy Metal v30 03 (2006-07) (svengali-DCP).cbz

### heavy metal — v6 — #05  — identical size  *(volume)*

- `   51 MB`  Heavy Metal/Heavy Metal Vols 01-35 (1977-2012)/Heavy Metal v06 05 (1982-08) (Jnx-HaCsA).cbr
- `   51 MB`  Heavy Metal/01. Main Series/Heavy Metal v06 05 (1982-08) (Jnx-HaCsA).cbr

### clive barkers nightbreed — #009  *(issue)*

- `   52 MB`  Clive Barker/Clive Barker s Nightbreed v2 (001-012+)(2014-2017)(digital)(Minutemen-Slayer)/Clive Barkers Nightbreed 009 (2015) (digital) (Minutemen-Slayer).cbr
- `   51 MB`  Clive Barker/Clive Barker s Nightbreed 001-012 (2014-2015)/Clive Barker s Nightbreed 001-012 (2014-2015)/Clive Barkers Nightbreed 009 (2015) (Digital-Empire).cbr

### heavy metal — v1 — #08  — identical size  *(volume)*

- `   51 MB`  Heavy Metal/Heavy Metal Vols 01-35 (1977-2012)/Heavy Metal v01 08 (1977-11).cbr
- `   51 MB`  Heavy Metal/01. Main Series/Heavy Metal v01 08 (1977-11).cbr

### heavy metal presents moebius  — identical size  *(issue)*

- `   51 MB`  Heavy Metal/Heavy Metal Presents/Heavy Metal Presents - Moebius (1981).cbr
- `   51 MB`  Heavy Metal/03. Extras/Heavy Metal Presents - Moebius (1981).cbr

### heavy metal — v25 — #04  — identical size  *(volume)*

- `   51 MB`  Heavy Metal/Heavy Metal Vols 01-35 (1977-2012)/Heavy Metal v25 04 (2001) (Humperdido).cbr
- `   51 MB`  Heavy Metal/01. Main Series/Heavy Metal v25 04 (2001) (Humperdido).cbr

### heavy metal — v20 — #06  — identical size  *(volume)*

- `   51 MB`  Heavy Metal/Heavy Metal Vols 01-35 (1977-2012)/Heavy Metal v20 06 (1997).cbr
- `   51 MB`  Heavy Metal/01. Main Series/Heavy Metal v20 06 (1997).cbr

### heavy metal — v26 — #04  — identical size  *(volume)*

- `   51 MB`  Heavy Metal/Heavy Metal Vols 01-35 (1977-2012)/Heavy Metal v26 04 (2002).cbr
- `   51 MB`  Heavy Metal/01. Main Series/Heavy Metal v26 04 (2002).cbr

### heavy metal — v25 — #05  — identical size  *(volume)*

- `   51 MB`  Heavy Metal/Heavy Metal Vols 01-35 (1977-2012)/Heavy Metal v25 05 (2001) (Humperdido).cbr
- `   51 MB`  Heavy Metal/01. Main Series/Heavy Metal v25 05 (2001) (Humperdido).cbr

### heavy metal — v30 — #06  — identical size  *(volume)*

- `   50 MB`  Heavy Metal/Heavy Metal Vols 01-35 (1977-2012)/Heavy Metal v30 06 (2007) (svengali-DCP).cbz
- `   50 MB`  Heavy Metal/01. Main Series/Heavy Metal v30 06 (2007) (svengali-DCP).cbz

### heavy metal — v19 — #06  — identical size  *(volume)*

- `   50 MB`  Heavy Metal/Heavy Metal Vols 01-35 (1977-2012)/Heavy Metal v19 06 (1996-01) (Humperdido).cbr
- `   50 MB`  Heavy Metal/01. Main Series/Heavy Metal v19 06 (1996-01) (Humperdido).cbr

### heavy metal — v18 — #03  — identical size  *(volume)*

- `   50 MB`  Heavy Metal/Heavy Metal Vols 01-35 (1977-2012)/Heavy Metal v18 03 (1994-07) (Humperdido).cbr
- `   50 MB`  Heavy Metal/01. Main Series/Heavy Metal v18 03 (1994-07) (Humperdido).cbr

### judge dredd pit  — identical size  *(issue)*

- `   50 MB`  Judge Dredd - Collections/Judge Dredd - The Pit (2008) (digital) (JeffAlbertson-DCP)/Judge Dredd - The Pit (2008) (digital) (JeffAlbertson-DCP).cbz
- `   50 MB`  2000AD - Collections /Judge Dredd/Judge Dredd - The Pit (2008) (2000AD) (digital) (JeffAlbertson-DCP).cbz

### heavy metal — v34 — #02  — identical size  *(volume)*

- `   50 MB`  Heavy Metal/Heavy Metal Vols 01-35 (1977-2012)/Heavy Metal v34 02 (2010) (Mythical Special) (svengali-DCP).cbr
- `   50 MB`  Heavy Metal/01. Main Series/Heavy Metal v34 02 (2010) (Mythical Special) (svengali-DCP).cbr

### avengers — #003  *(issue)*

- `   54 MB`  Avengers/Avengers Vol. 07 (001-011,672-690)(2017-2018)(digital)/Avengers 003 (2017) (2 covers) (digital) (Minutemen-Slayer).cbr
- `   45 MB`  Avengers/Avengers (2018-2019)/Avengers 003 (2018) (Digital) (Zone-Empire).cbr

### clive barkers nightbreed — #004  *(issue)*

- `   52 MB`  Clive Barker/Clive Barker s Nightbreed v2 (001-012+)(2014-2017)(digital)(Minutemen-Slayer)/Clive Barkers Nightbreed 004 (2014) (digital) (Minutemen-Slayer).cbr
- `   48 MB`  Clive Barker/Clive Barker s Nightbreed 001-012 (2014-2015)/Clive Barker s Nightbreed 001-012 (2014-2015)/Clive Barkers Nightbreed 004 (2014) (Digital-Empire).cbr

### clive barkers nightbreed — #003  *(issue)*

- `   51 MB`  Clive Barker/Clive Barker s Nightbreed v2 (001-012+)(2014-2017)(digital)(Minutemen-Slayer)/Clive Barkers Nightbreed 003 (2014) (digital) (Minutemen-Slayer).cbr
- `   48 MB`  Clive Barker/Clive Barker s Nightbreed 001-012 (2014-2015)/Clive Barker s Nightbreed 001-012 (2014-2015)/Clive Barkers Nightbreed 003 (2014) (Digital-Empire).cbr

### avengers — #002  *(issue)*

- `   54 MB`  Avengers/Avengers Vol. 07 (001-011,672-690)(2017-2018)(digital)/Avengers 002 (2017) (3 covers) (digital) (Minutemen-Slayer).cbr
- `   45 MB`  Avengers/Avengers (2018-2019)/Avengers 002 (2018) (Digital) (Zone-Empire).cbr

### whispers in walls — #03  *(issue)*

- `   79 MB`  Humanoids (Europe)/Whispers in the Walls/Whispers in the Walls 03 (of 03).cbr
- `   20 MB`  Humanoids (Europe)/Whispers in the Walls (Humanoids 2010)/Whispers in the Walls 03 (Humanoids 2010) (Minutemen-DTs).cbz

### heavy metal — v6 — #01  — identical size  *(volume)*

- `   49 MB`  Heavy Metal/Heavy Metal Vols 01-35 (1977-2012)/Heavy Metal v06 01 (1982-04) (Jnx-HaCsA).cbr
- `   49 MB`  Heavy Metal/01. Main Series/Heavy Metal v06 01 (1982-04) (Jnx-HaCsA).cbr

### heavy metal — v31 — #01  — identical size  *(volume)*

- `   49 MB`  Heavy Metal/Heavy Metal Vols 01-35 (1977-2012)/Heavy Metal v31 01 (2007) (svengali-DCP).cbz
- `   49 MB`  Heavy Metal/01. Main Series/Heavy Metal v31 01 (2007) (svengali-DCP).cbz

### heavy metal — v1 — #07  — identical size  *(volume)*

- `   49 MB`  Heavy Metal/Heavy Metal Vols 01-35 (1977-2012)/Heavy Metal v01 07 (1977) (null-DCP).cbz
- `   49 MB`  Heavy Metal/01. Main Series/Heavy Metal v01 07 (1977) (null-DCP).cbz

### heavy metal — v36 — #001  — identical size  *(volume)*

- `   48 MB`  Heavy Metal/Heavy Metal Vols 01-35 (1977-2012)/Heavy Metal v36 001 (2012) (hybrid) (null-DCP).cbz
- `   48 MB`  Heavy Metal/01. Main Series/Heavy Metal v36 001 (2012) (hybrid) (null-DCP).cbz

### alliance of curious — #01  — identical size  *(issue)*

- `   48 MB`  Humanoids (Europe)/The Alliance of the Curious 01 - Sapiens (2012) (Digital) (Humanoids).cbr
- `   48 MB`  Humanoids (Europe)/The Alliance of the Curious/The Alliance of the Curious 01 - Sapiens (2012) (Digital) (Humanoids).cbr

### alliance of curious — #02  — identical size  *(issue)*

- `   48 MB`  Humanoids (Europe)/The Alliance of the Curious 02 - Neandertalensis (2012) (Digital) (Humanoids).cbr
- `   48 MB`  Humanoids (Europe)/The Alliance of the Curious/The Alliance of the Curious 02 - Neandertalensis (2012) (Digital) (Humanoids).cbr

### heavy metal — v28 — #04  — identical size  *(volume)*

- `   48 MB`  Heavy Metal/Heavy Metal Vols 01-35 (1977-2012)/Heavy Metal v28 04 (2004).cbr
- `   48 MB`  Heavy Metal/01. Main Series/Heavy Metal v28 04 (2004).cbr

### heavy metal — v2 — #02  — identical size  *(volume)*

- `   48 MB`  Heavy Metal/Heavy Metal Vols 01-35 (1977-2012)/Heavy Metal v02 02 (1978-06) (misprinted as vol III).cbr
- `   48 MB`  Heavy Metal/01. Main Series/Heavy Metal v02 02 (1978-06) (misprinted as vol III).cbr

### heavy metal — v21 — #01  — identical size  *(volume)*

- `   48 MB`  Heavy Metal/Heavy Metal Vols 01-35 (1977-2012)/Heavy Metal v21 01 (1997).cbr
- `   48 MB`  Heavy Metal/01. Main Series/Heavy Metal v21 01 (1997).cbr

### heavy metal — v1 — #06  — identical size  *(volume)*

- `   48 MB`  Heavy Metal/Heavy Metal Vols 01-35 (1977-2012)/Heavy Metal v01 06 (1977) (null-DCP).cbz
- `   48 MB`  Heavy Metal/01. Main Series/Heavy Metal v01 06 (1977) (null-DCP).cbz

### heavy metal — v29 — #05  — identical size  *(volume)*

- `   47 MB`  Heavy Metal/Heavy Metal Vols 01-35 (1977-2012)/Heavy Metal v29 05 (2005-11) (svengali-DCP).cbz
- `   47 MB`  Heavy Metal/01. Main Series/Heavy Metal v29 05 (2005-11) (svengali-DCP).cbz

### heavy metal — v5 — #05  — identical size  *(volume)*

- `   47 MB`  Heavy Metal/Heavy Metal Vols 01-35 (1977-2012)/Heavy Metal v05 05 (1981-08).cbr
- `   47 MB`  Heavy Metal/01. Main Series/Heavy Metal v05 05 (1981-08).cbr

### 2000ad prog 2002  *(issue)*

- `   52 MB`  2000AD prog/2000AD (Specials, Annuals & Poster Progs + Extras)/2000AD Yearbooks & Specials (1977 - 2013)/2000AD Yearbooks (Prog 2000 - 2013)/2000AD Prog 2002.cbr
- `   42 MB`  2000AD prog/2000AD prog 2002 (2016) (digital) (juvecube).cbr

### heavy metal — v6 — #03  — identical size  *(volume)*

- `   47 MB`  Heavy Metal/Heavy Metal Vols 01-35 (1977-2012)/Heavy Metal v06 03 (1982-06) (Jnx-HaCsA).cbr
- `   47 MB`  Heavy Metal/01. Main Series/Heavy Metal v06 03 (1982-06) (Jnx-HaCsA).cbr

### heavy metal — v6 — #02  — identical size  *(volume)*

- `   47 MB`  Heavy Metal/Heavy Metal Vols 01-35 (1977-2012)/Heavy Metal v06 02 (1982-05) (Jnx-HaCsA).cbr
- `   47 MB`  Heavy Metal/01. Main Series/Heavy Metal v06 02 (1982-05) (Jnx-HaCsA).cbr

### 319 durham red island of damned  — identical size  *(issue)*

- `   47 MB`  Judge Dredd The Megazine/Judge Dredd Megazine v5 (201-400)(2002-ongoing)/J.D Megazine Supplements/319 - Durham Red - Island of the Damned.cbr
- `   47 MB`  Judge Dredd The Megazine/J.D Megazine Supplements/319 - Durham Red - Island of the Damned.cbr

### thundercats lost — #007  *(issue)*

- `   56 MB`  ThunderCats/Thundercats Lost 007 (2025) (5 Covers) (Digital) (Shan-Empire).cbz
- `   38 MB`  ThunderCats/Thundercats Lost 007 (2025) (Series) (Dynamite Entertainment) (Digital-HD) (LeDuch).cbz

### heavy metal — v5 — #09  — identical size  *(volume)*

- `   47 MB`  Heavy Metal/Heavy Metal Vols 01-35 (1977-2012)/Heavy Metal v05 09 (1981-12).cbr
- `   47 MB`  Heavy Metal/01. Main Series/Heavy Metal v05 09 (1981-12).cbr

### heavy metal — v6 — #06  — identical size  *(volume)*

- `   47 MB`  Heavy Metal/Heavy Metal Vols 01-35 (1977-2012)/Heavy Metal v06 06 (1982-09) (Jnx-HaCsA).cbr
- `   47 MB`  Heavy Metal/01. Main Series/Heavy Metal v06 06 (1982-09) (Jnx-HaCsA).cbr

### heavy metal — v6 — #12  — identical size  *(volume)*

- `   46 MB`  Heavy Metal/Heavy Metal Vols 01-35 (1977-2012)/Heavy Metal v06 12 (1983-03) (Jnx-HaCsA).cbr
- `   46 MB`  Heavy Metal/01. Main Series/Heavy Metal v06 12 (1983-03) (Jnx-HaCsA).cbr

### frankenstein's womb  *(issue)*

- `   64 MB`  Frankenstein's Womb (2009) (Digital) (EJGriffin-Empire).cbz
- `   29 MB`  Warren Ellis/2004/2004 Apparat/Frankenstein's Womb (2009).cbz

### heavy metal — v6 — #08  — identical size  *(volume)*

- `   46 MB`  Heavy Metal/Heavy Metal Vols 01-35 (1977-2012)/Heavy Metal v06 08 (1982-11) (Jnx-HaCsA).cbr
- `   46 MB`  Heavy Metal/01. Main Series/Heavy Metal v06 08 (1982-11) (Jnx-HaCsA).cbr

### heavy metal — v6 — #04  — identical size  *(volume)*

- `   46 MB`  Heavy Metal/Heavy Metal Vols 01-35 (1977-2012)/Heavy Metal v06 04 (1982-07) (Jnx-HaCsA).cbr
- `   46 MB`  Heavy Metal/01. Main Series/Heavy Metal v06 04 (1982-07) (Jnx-HaCsA).cbr

### heavy metal — v6 — #10  — identical size  *(volume)*

- `   46 MB`  Heavy Metal/Heavy Metal Vols 01-35 (1977-2012)/Heavy Metal v06 10 (1983-01) (Jnx-HaCsA).cbr
- `   46 MB`  Heavy Metal/01. Main Series/Heavy Metal v06 10 (1983-01) (Jnx-HaCsA).cbr

### heavy metal — v29 — #06  — identical size  *(volume)*

- `   46 MB`  Heavy Metal/Heavy Metal Vols 01-35 (1977-2012)/Heavy Metal v29 06 (2006) (svengali-DCP).cbz
- `   46 MB`  Heavy Metal/01. Main Series/Heavy Metal v29 06 (2006) (svengali-DCP).cbz

### thoroughly ripped with fabulous furry freak brothers  — identical size  *(issue)*

- `   45 MB`  Thoroughly Ripped with the Fabulous Furry Freak Brothers (1st Edition).cbr
- `   45 MB`  The Fabulous Furry Freak Brothers/Fabulous Furry Freak Brothers (Complete 00-13 + Special)/Thoroughly Ripped with the Fabulous Furry Freak Brothers (1st Edition).cbr

### whispers in walls — #02  *(issue)*

- `   72 MB`  Humanoids (Europe)/Whispers in the Walls/Whispers in the Walls 02 (of 03).cbr
- `   18 MB`  Humanoids (Europe)/Whispers in the Walls (Humanoids 2010)/Whispers in the Walls 02 (Humanoids 2010) (Minutemen-DTs).cbz

### heavy metal — v6 — #09  — identical size  *(volume)*

- `   45 MB`  Heavy Metal/Heavy Metal Vols 01-35 (1977-2012)/Heavy Metal v06 09 (1982-12) (Jnx-HaCsA).cbr
- `   45 MB`  Heavy Metal/01. Main Series/Heavy Metal v06 09 (1982-12) (Jnx-HaCsA).cbr

### kick ass — #003  *(issue)*

- `   53 MB`  Mark Millar/Kick-Ass (v1-v3+)(2008-2014)(digital+)/Kick-Ass 4 (2018-2019)/Kick-Ass 003 (2018) (Digital) (Zone-Empire).cbr
- `   37 MB`  Mark Millar/Kick-Ass (v1-v3+)(2008-2014)(digital+)/Kick-Ass 3 (001-008+)(2013-2014)(digital+)/scans/Kick-Ass 3 003 (2013) (c2c) (3 Covers) (Monafekk-Empire).cbr

### new avengers — #33  *(issue)*

- `   39 MB`  Alias  ( Jessica Jones , The Pulse & Appearances)/Appearances/New Avengers (2010)/New Avengers 33(c2c)(2013)(Re-em-Novus-HD).cbr
- `   28 MB`  Alias  ( Jessica Jones , The Pulse & Appearances)/Appearances/New Avengers (2010)/New Avengers 33(c2c)(2013)(Re-em-Novus).cbr
- `   23 MB`  Alias  ( Jessica Jones , The Pulse & Appearances)/Appearances/New Avengers (2010)/New Avengers 33(2013)(Digital)(C9-Novus).cbr

### heavy metal — v5 — #12  — identical size  *(volume)*

- `   45 MB`  Heavy Metal/Heavy Metal Vols 01-35 (1977-2012)/Heavy Metal v05 12 (1982-03) (Jnx-HaCsA).cbr
- `   45 MB`  Heavy Metal/01. Main Series/Heavy Metal v05 12 (1982-03) (Jnx-HaCsA).cbr

### heavy metal presents alien  — identical size  *(issue)*

- `   44 MB`  Heavy Metal/Heavy Metal Presents/Heavy Metal Presents - Alien (1979).cbz
- `   44 MB`  Heavy Metal/03. Extras/Heavy Metal Presents - Alien (1979).cbz

### heavy metal — v2 — #12  — identical size  *(volume)*

- `   44 MB`  Heavy Metal/Heavy Metal Vols 01-35 (1977-2012)/Heavy Metal v02 12 (1979-04).cbr
- `   44 MB`  Heavy Metal/01. Main Series/Heavy Metal v02 12 (1979-04).cbr

### legenderry a steampunk adventure — #002  — identical size  *(issue)*

- `   44 MB`  Legenderry/Legenderry A Steampunk Adventure 001-007 (2013-2014)/Legenderry A Steampunk Adventure 002(2014)(Digital Exclusive Edition)(TLK-EMPIRE-HD).cbr
- `   44 MB`  Legenderry/Legenderry A Steampunk Adventure 001-007 (2013-2014)/Legenderry A Steampunk Adventure 002(2014)(Digital Exclusive Edition)(TLK-EMPIRE-HD) (1).cbr

### from hell dance of gull catchers  — identical size  *(issue)*

- `   44 MB`  Alan Moore/Alan Moore Essentials/Alan Moore 1996- From Hell/From Hell Dance Of The Gull-Catchers.cbr
- `   44 MB`  Alan Moore/Alan Moore Collection V- More Moore/From Hell/From Hell- Dance Of The Gull-Catchers.cbr

### heavy metal — v28 — #05  — identical size  *(volume)*

- `   44 MB`  Heavy Metal/Heavy Metal Vols 01-35 (1977-2012)/Heavy Metal v28 05 (2004) (Humperdido).cbr
- `   44 MB`  Heavy Metal/01. Main Series/Heavy Metal v28 05 (2004) (Humperdido).cbr

### heavy metal — v6 — #07  — identical size  *(volume)*

- `   44 MB`  Heavy Metal/Heavy Metal Vols 01-35 (1977-2012)/Heavy Metal v06 07 (1982-10) (Jnx-HaCsA).cbr
- `   44 MB`  Heavy Metal/01. Main Series/Heavy Metal v06 07 (1982-10) (Jnx-HaCsA).cbr

### tim burton's nightmare before christmas shiver of christmas town — #004  — identical size  *(issue)*

- `   44 MB`  Tim Burton's The Nightmare Before Christmas - The Shiver of Christmas Town 004 (2026) (4 covers) (digital) (Salem-Empire).cbr
- `   44 MB`  Tim Burton's The Nightmare Before Christmas - The Shiver of Christmas Town/Tim Burton's The Nightmare Before Christmas - The Shiver of Christmas Town 004 (2026) (4 covers) (digital) (Salem-Empire).cbr

### brass sun — v2  — identical size  *(volume)*

- `   43 MB`  Brass Sun/Brass Sun V2 The Diamond Age (Dan Dare 2000AD Remix).cbr
- `   43 MB`  2000AD - Collections /Brass Sun/Brass Sun V2 The Diamond Age (Dan Dare 2000AD Remix).cbr

### 2000ad prog 2001  *(issue)*

- `   46 MB`  2000AD prog/2000AD (Specials, Annuals & Poster Progs + Extras)/2000AD Yearbooks & Specials (1977 - 2013)/2000AD Yearbooks (Prog 2000 - 2013)/2000AD Prog 2001.cbr
- `   41 MB`  2000AD prog/2000AD prog 2001 (2016) (digital) (juvecube).cbr

### heavy metal — v25 — #03  — identical size  *(volume)*

- `   43 MB`  Heavy Metal/Heavy Metal Vols 01-35 (1977-2012)/Heavy Metal v25 03 (2001) (Humperdido).cbr
- `   43 MB`  Heavy Metal/01. Main Series/Heavy Metal v25 03 (2001) (Humperdido).cbr

### chiaroscuro  *(issue)*

- `   82 MB`  Chiaroscuro (Vertigo)(1995)(c)/Chiaroscuro (Vertigo)(1995)(c).cbz
- `    4 MB`  Alan Moore/Alan Moore Collection VI- Made For Moore/Alan Moore's Songbook/Negative Burn/Chiaroscuro (from Negative Burn 025).cbr

### avengers — #005  *(issue)*

- `   47 MB`  Avengers/Avengers (2018-2019)/Avengers 005 (2018) (Digital) (Zone-Empire).cbr
- `   39 MB`  Avengers/Avengers Vol. 07 (001-011,672-690)(2017-2018)(digital)/Avengers 005 (2017) (digital) (Minutemen-Slayer).cbr

### avengers — #006  *(issue)*

- `   44 MB`  Avengers/Avengers (2018-2019)/Avengers 006 (2018) (Digital) (F) (Zone-Empire).cbr
- `   42 MB`  Avengers/Avengers Vol. 07 (001-011,672-690)(2017-2018)(digital)/Avengers 006 (2017) (digital) (Minutemen-Slayer).cbr

### war wolf — #006  *(issue)*

- `   47 MB`  War Wolf/War Wolf 006 (2026) (Series) (Mad Cave Studios) (Digital) (LeDuch-DCP).cbz
- `   39 MB`  War Wolf/War Wolf 006 (2026) (digital) (Knight Ripper-Empire).cbr

### whispers in walls — #01  *(issue)*

- `   67 MB`  Humanoids (Europe)/Whispers in the Walls/Whispers in the Walls 01 (of 03).cbr
- `   18 MB`  Humanoids (Europe)/Whispers in the Walls (Humanoids 2010)/Whispers in the Walls 01 (Humanoids 2010) (Minutemen-DTs).cbz

### heavy metal — v5 — #10  — identical size  *(volume)*

- `   43 MB`  Heavy Metal/Heavy Metal Vols 01-35 (1977-2012)/Heavy Metal v05 10 (1982-01) (Jnx-HaCsA).cbz
- `   43 MB`  Heavy Metal/01. Main Series/Heavy Metal v05 10 (1982-01) (Jnx-HaCsA).cbz

### 2000ad prog 2007  *(issue)*

- `   43 MB`  2000AD prog/2000AD prog 2007 (2016) (digital) (juvecube).cbr
- `   43 MB`  2000AD prog/2000AD (Specials, Annuals & Poster Progs + Extras)/2000AD Yearbooks & Specials (1977 - 2013)/2000AD Yearbooks (Prog 2000 - 2013)/2000AD Prog 2007 (2006) (John Williams-DCP).cbr

### art of moebius  *(issue)*

- `   43 MB`  Jodorowsky and Moebius/The Art of Moebius (1989).cbr
- `   43 MB`  Jodorowsky and Moebius/Moebius/The Art of Moebius.cbz

### heavy metal presents candice at sea  — identical size  *(issue)*

- `   43 MB`  Heavy Metal/Heavy Metal Presents/Heavy Metal Presents - Candice At Sea (1977) (rescan).cbr
- `   43 MB`  Heavy Metal/03. Extras/Heavy Metal Presents - Candice At Sea (1977) (rescan).cbr

### brass sun — v1  — identical size  *(volume)*

- `   42 MB`  Brass Sun/Brass Sun V1 The Wheel of Worlds (Dan Dare 2000AD Remix).cbr
- `   42 MB`  2000AD - Collections /Brass Sun/Brass Sun V1 The Wheel of Worlds (Dan Dare 2000AD Remix).cbr

### shocking futures  — identical size  *(issue)*

- `   42 MB`  2000AD prog/Alan Moore -2000AD/Shocking Futures.cbr
- `   42 MB`  2000AD prog/2000AD (Specials, Annuals & Poster Progs + Extras)/Related/Shocking Futures.cbr

### 2000ad prog 2017  — identical size  *(issue)*

- `   42 MB`  2000AD prog/2000AD prog 2017 (2017) (digital) (juvecube).cbr
- `   42 MB`  2000AD prog/2000AD Judge Dredd January - June 2017 (juvecube)/2000AD progs 2012-2037/2000AD prog 2017 (2017) (juvecube).cbr

### extinction seed — #001  *(issue)*

- `   47 MB`  GG Studio (Collection) (2010-2012)/Extinction Seed (001-003) (2011-2012)/Extinction Seed 001 (2011) (Digital) (K6-Empire).cbr
- `   37 MB`  GG Studio (Collection) (2010-2012)/Extinction Seed (001-003) (2011-2012)/Extinction Seed 001 (2011) (3 covers) (Tarutaru-DCP).cbr

### 2000ad prog 2035  — identical size  *(issue)*

- `   42 MB`  2000AD prog/2000AD prog 2035 (2017) (digital) (juvecube).cbr
- `   42 MB`  2000AD prog/2000AD Judge Dredd January - June 2017 (juvecube)/2000AD progs 2012-2037/2000AD Prog 2035 (2017) (juvecube).cbr

### heavy metal — v30 — #05  — identical size  *(volume)*

- `   42 MB`  Heavy Metal/Heavy Metal Vols 01-35 (1977-2012)/Heavy Metal v30 05 (2006) (svengali-DCP).cbz
- `   42 MB`  Heavy Metal/01. Main Series/Heavy Metal v30 05 (2006) (svengali-DCP).cbz

### mischief of magpies ashcan  — identical size  *(issue)*

- `   42 MB`  A Mischief of Magpies Ashcan (2026) (digital) (tomjoad).cbz
- `   42 MB`  A Mischief of Magpies Asan/A Mischief of Magpies Ashcan (2026) (digital) (tomjoad).cbz

### heavy metal — v1 — #01  — identical size  *(volume)*

- `   42 MB`  Heavy Metal/Heavy Metal Vols 01-35 (1977-2012)/Heavy Metal v01 01 (1977-04) (Whyld Goose).cbr
- `   42 MB`  Heavy Metal/01. Main Series/Heavy Metal v01 01 (1977-04) (Whyld Goose).cbr

### postal dossier — #001  — identical size  *(issue)*

- `   42 MB`  Image comics/Postal/Postal - The Tithe/Postal - Dossier 001 (2015) GetComics.INFO.cbr
- `   42 MB`  Image comics/Postal/Postal - Dossier 001 (2015) GetComics.INFO.cbr

### 2000ad prog 2036  — identical size  *(issue)*

- `   42 MB`  2000AD prog/2000AD prog 2036 (2017) (digital) (juvecube).cbr
- `   42 MB`  2000AD prog/2000AD Judge Dredd January - June 2017 (juvecube)/2000AD progs 2012-2037/2000AD prog 2036 (2017) (juvecube).cbr

### 2000ad prog 2018  — identical size  *(issue)*

- `   41 MB`  2000AD prog/2000AD prog 2018 (2017) (digital) (juvecube).cbr
- `   41 MB`  2000AD prog/2000AD Judge Dredd January - June 2017 (juvecube)/2000AD progs 2012-2037/2000AD prog 2018 (2017) (juvecube).cbr

### fearless dawn meets hellboy  — identical size  *(issue)*

- `   41 MB`  Hellboy/Fearless Dawn Meets Hellboy (2020) (digital) (Son of Ultron-Empire).cbr
- `   41 MB`  Fearless Dawn/Fearless Dawn Meets Hellboy (2020) (digital) (Son of Ultron-Empire).cbr

### iron man noir — #04  — identical size  *(issue)*

- `   41 MB`  GG Studio (Collection) (2010-2012)/Marvel Noir (2009-2011)(digital)/Iron Man - Noir (001-004)(2010)(digital)(G85-Empire)/Iron Man Noir 04 (of 04) (2010) (Digital) (G85-Empire).cbr
- `   41 MB`  Aster Blistok/Le Vagabond des Limbes/Iron Man - Noir (001-004)(2010)(digital)(G85-Empire)/Iron Man Noir 04 (of 04) (2010) (Digital) (G85-Empire).cbr

### harry kipling  — identical size  *(issue)*

- `   41 MB`  Harry Kipling.cbz
- `   41 MB`  2000AD - Collections /Harry Kipling/Harry Kipling.cbz

### judge dredd movie tie in action  — identical size  *(special)*

- `   27 MB`  2000AD prog/Yearbooks & Specials/Specials/Judge Dredd/Judge Dredd Movie Tie-In Action Special (1996).cbr
- `   27 MB`  2000AD prog/2000AD Yearbooks & Specials (1977 - 2013)/Judge Dredd (Specials, Poster Progs & Extras) (-JJ-)/Judge Dredd Movie Tie-In Action Special (1996).cbr
- `   27 MB`  2000AD prog/2000AD (Specials, Annuals & Poster Progs + Extras)/2000AD Yearbooks & Specials (1977 - 2013)/Judge Dredd (Specials, Poster Progs & Extras) (-JJ-)/Judge Dredd Movie Tie-In Action Special (1996).cbr

### hellboy and b.p.r.d. saturn returns — #01  — identical size  *(issue)*

- `   41 MB`  Hellboy/Hellboy and the B.P.R.D. - Saturn Returns 01-03 (2019) (digital) (Son of Ultron-Empire)/Hellboy and the B.P.R.D. - Saturn Returns 01 (of 03) (2019) (digital) (Son of Ultron-Empire).cbr
- `   41 MB`  Hellboy/Hellboy and the B.P.R.D. - Saturn Returns 01 (of 03) (2019) (digital) (Son of Ultron-Empire).cbr

### 2000ad prog 2034  — identical size  *(issue)*

- `   41 MB`  2000AD prog/2000AD prog 2034 (2017) (digital) (juvecube).cbr
- `   41 MB`  2000AD prog/2000AD Judge Dredd January - June 2017 (juvecube)/2000AD progs 2012-2037/2000AD prog 2034 (2017) (juvecube).cbr

### 2000ad prog 2016  — identical size  *(issue)*

- `   41 MB`  2000AD prog/2000AD prog 2016 (2017) (digital) (juvecube).cbr
- `   41 MB`  2000AD prog/2000AD Judge Dredd January - June 2017 (juvecube)/2000AD progs 2012-2037/2000AD prog 2016 (2017) (juvecube).cbr

### iron man noir — #01  — identical size  *(issue)*

- `   41 MB`  GG Studio (Collection) (2010-2012)/Marvel Noir (2009-2011)(digital)/Iron Man - Noir (001-004)(2010)(digital)(G85-Empire)/Iron Man Noir 01 (of 04) (2010) (Digital) (G85-Empire).cbr
- `   41 MB`  Aster Blistok/Le Vagabond des Limbes/Iron Man - Noir (001-004)(2010)(digital)(G85-Empire)/Iron Man Noir 01 (of 04) (2010) (Digital) (G85-Empire).cbr

### 2000ad prog 2026  — identical size  *(issue)*

- `   41 MB`  2000AD prog/2000AD prog 2026 (2017) (digital) (juvecube).cbr
- `   41 MB`  2000AD prog/2000AD Judge Dredd January - June 2017 (juvecube)/2000AD progs 2012-2037/2000AD prog 2026 (2017) (juvecube).cbr

### hellboy and b.p.r.d. saturn returns — #02  — identical size  *(issue)*

- `   41 MB`  Hellboy/Hellboy and the B.P.R.D. - Saturn Returns 02 (of 03) (2019) (digital) (Son of Ultron-Empire).cbr
- `   41 MB`  Hellboy/Hellboy and the B.P.R.D. - Saturn Returns 01-03 (2019) (digital) (Son of Ultron-Empire)/Hellboy and the B.P.R.D. - Saturn Returns 02 (of 03) (2019) (digital) (Son of Ultron-Empire).cbr

### 2000ad prog 2028  — identical size  *(issue)*

- `   40 MB`  2000AD prog/2000AD prog 2028 (2017) (digital) (juvecube).cbr
- `   40 MB`  2000AD prog/2000AD Judge Dredd January - June 2017 (juvecube)/2000AD progs 2012-2037/2000AD prog 2028 (2017) (juvecube).cbr

### heavy metal — v5 — #07  — identical size  *(volume)*

- `   40 MB`  Heavy Metal/Heavy Metal Vols 01-35 (1977-2012)/Heavy Metal v05 07 (1981-10).cbr
- `   40 MB`  Heavy Metal/01. Main Series/Heavy Metal v05 07 (1981-10).cbr

### dash shaw cosplayers — #001  — identical size  *(issue)*

- `   40 MB`  Dash Shaw - Cosplayers (2014)/Dash Shaw - Cosplayers 001 (2014).cbr
- `   40 MB`  Dash Shaw - Cosplayers (2014)/Dash Shaw - Cosplayers (2014)/Dash Shaw - Cosplayers 001 (2014).cbr

### avengers — #008  *(issue)*

- `   55 MB`  Avengers/Avengers (2018-2019)/Avengers 008 (2018) (Digital) (Zone-Empire).cbr
- `   25 MB`  Avengers/Avengers Vol. 07 (001-011,672-690)(2017-2018)(digital)/Avengers 008 (2017) (digital) (Minutemen-Slayer).cbr

### heavy metal — v1 — #02  — identical size  *(volume)*

- `   40 MB`  Heavy Metal/Heavy Metal Vols 01-35 (1977-2012)/Heavy Metal v01 02 (1977-05).cbr
- `   40 MB`  Heavy Metal/01. Main Series/Heavy Metal v01 02 (1977-05).cbr

### new avengers — #31  *(issue)*

- `   25 MB`  Alias  ( Jessica Jones , The Pulse & Appearances)/Appearances/New Avengers (2010)/New Avengers 31(c2c)(2012)(Re-em-DCP-HD).cbr
- `   21 MB`  Alias  ( Jessica Jones , The Pulse & Appearances)/Appearances/New Avengers (2010)/New Avengers 31(noads)(2012)(Re-em-DCP-HD).cbr
- `   19 MB`  Alias  ( Jessica Jones , The Pulse & Appearances)/Appearances/New Avengers (2010)/New Avengers 31(c2c)(2012)(Re-em-DCP).cbr
- `   15 MB`  Alias  ( Jessica Jones , The Pulse & Appearances)/Appearances/New Avengers (2010)/New Avengers 31(noads)(2012)(Re-em-DCP).cbr

### 2000ad prog 2019  — identical size  *(issue)*

- `   40 MB`  2000AD prog/2000AD prog 2019 (2017) (digital) (juvecube).cbr
- `   40 MB`  2000AD prog/2000AD Judge Dredd January - June 2017 (juvecube)/2000AD progs 2012-2037/2000AD prog 2019 (2017) (juvecube).cbr

### iron man noir — #03  — identical size  *(issue)*

- `   40 MB`  GG Studio (Collection) (2010-2012)/Marvel Noir (2009-2011)(digital)/Iron Man - Noir (001-004)(2010)(digital)(G85-Empire)/Iron Man Noir 03 (of 04) (2010) (Digital) (G85-Empire).cbr
- `   40 MB`  Aster Blistok/Le Vagabond des Limbes/Iron Man - Noir (001-004)(2010)(digital)(G85-Empire)/Iron Man Noir 03 (of 04) (2010) (Digital) (G85-Empire).cbr

### 2000ad prog 2022  — identical size  *(issue)*

- `   40 MB`  2000AD prog/2000AD prog 2022 (2017) (digital) (juvecube).cbr
- `   40 MB`  2000AD prog/2000AD Judge Dredd January - June 2017 (juvecube)/2000AD progs 2012-2037/2000AD prog 2022 (2017) (juvecube).cbr

### 302 balls brothers heroes for hire  — identical size  *(issue)*

- `   39 MB`  Judge Dredd The Megazine/Judge Dredd Megazine v5 (201-400)(2002-ongoing)/J.D Megazine Supplements/302 - The Balls Brothers - Heroes for Hire.cbr
- `   39 MB`  Judge Dredd The Megazine/J.D Megazine Supplements/302 - The Balls Brothers - Heroes for Hire.cbr

### heavy metal — v5 — #11  — identical size  *(volume)*

- `   39 MB`  Heavy Metal/Heavy Metal Vols 01-35 (1977-2012)/Heavy Metal v05 11 (1982-02) (Jnx-HaCsA).cbr
- `   39 MB`  Heavy Metal/01. Main Series/Heavy Metal v05 11 (1982-02) (Jnx-HaCsA).cbr

### 2000ad prog 2037  — identical size  *(issue)*

- `   39 MB`  2000AD prog/2000AD prog 2037 (2017) (digital) (juvecube).cbr
- `   39 MB`  2000AD prog/2000AD Judge Dredd January - June 2017 (juvecube)/2000AD progs 2012-2037/2000AD prog 2037 (2017) (juvecube).cbr

### iron man noir — #02  — identical size  *(issue)*

- `   39 MB`  GG Studio (Collection) (2010-2012)/Marvel Noir (2009-2011)(digital)/Iron Man - Noir (001-004)(2010)(digital)(G85-Empire)/Iron Man Noir 02 (of 04) (2010) (Digital) (G85-Empire).cbr
- `   39 MB`  Aster Blistok/Le Vagabond des Limbes/Iron Man - Noir (001-004)(2010)(digital)(G85-Empire)/Iron Man Noir 02 (of 04) (2010) (Digital) (G85-Empire).cbr

### 2000ad prog 2029  — identical size  *(issue)*

- `   39 MB`  2000AD prog/2000AD prog 2029 (2017) (digital) (juvecube).cbr
- `   39 MB`  2000AD prog/2000AD Judge Dredd January - June 2017 (juvecube)/2000AD progs 2012-2037/2000AD prog 2029 (2017) (juvecube).cbr

### avengers — #007  *(issue)*

- `   44 MB`  Avengers/Avengers (2018-2019)/Avengers 007 (2018) (Digital) (Zone-Empire).cbr
- `   34 MB`  Avengers/Avengers Vol. 07 (001-011,672-690)(2017-2018)(digital)/Avengers 007 (2017) (digital) (Minutemen-Slayer).cbr

### 2000ad prog 2021  — identical size  *(issue)*

- `   39 MB`  2000AD prog/2000AD prog 2021 (2017) (digital) (juvecube).cbr
- `   39 MB`  2000AD prog/2000AD Judge Dredd January - June 2017 (juvecube)/2000AD progs 2012-2037/2000AD prog 2021 (2017) (juvecube).cbr

### heavy metal — v6 — #11  — identical size  *(volume)*

- `   39 MB`  Heavy Metal/Heavy Metal Vols 01-35 (1977-2012)/Heavy Metal v06 11 (1983-02) (Jnx-HaCsA).cbr
- `   39 MB`  Heavy Metal/01. Main Series/Heavy Metal v06 11 (1983-02) (Jnx-HaCsA).cbr

### 2000ad prog 2024  — identical size  *(issue)*

- `   39 MB`  2000AD prog/2000AD prog 2024 (2017) (digital) (juvecube).cbr
- `   39 MB`  2000AD prog/2000AD Judge Dredd January - June 2017 (juvecube)/2000AD progs 2012-2037/2000AD prog 2024 (2017) (juvecube).cbr

### tank girl  — identical size  *(volume)*

- `   39 MB`  Tank Girl/18. Tank Girl - Graphic Novel (Penguin, 1991)/Tank Girl - Graphic Novel (Penguin, 1991).cbz
- `   39 MB`  Tank Girl/01. Tank Girl - Volume 1/Tank Girl - Graphic Novel (Penguin, 1991).cbz

### dredd urban warfare  — identical size  *(issue)*

- `   39 MB`  Judge Dredd - Collections/Dredd - Urban Warfare (2015) (2000AD) (digital) (JeffAlbertson-DCP)/Dredd - Urban Warfare (2015) (2000AD) (digital) (JeffAlbertson-DCP).cbz
- `   39 MB`  2000AD - Collections /Judge Dredd/Dredd - Urban Warfare (2015) (2000AD) (digital) (JeffAlbertson-DCP).cbz

### authority human on inside  — identical size  *(issue)*

- `   38 MB`  Warren Ellis/The Authority/specials/The Authority - Human on the Inside (2004).cbr
- `   38 MB`  The Authority/specials/The Authority - Human on the Inside (2004).cbr

### penny for your soul — #01  *(issue)*

- `   61 MB`  Penny For Your Soul (v1-v3+)(2010-2014)/Penny for Your Soul (v1-v3)(2010-2013)/01 Penny For Your Soul v1 (001-007+)(2010-2011)(Minutemen-Midas+)/Penny For Your Soul 01 (of 07) (2010) (Digital) (Darkness-Empire).cbr
- `   14 MB`  Penny For Your Soul (v1-v3+)(2010-2014)/Penny for Your Soul (v1-v3)(2010-2013)/01 Penny For Your Soul v1 (001-007+)(2010-2011)(Minutemen-Midas+)/Penny For Your Soul 01 (of 07) (2010) (c2c) (2 covers) (midas).cbr
- `    1 MB`  Penny For Your Soul (v1-v3+)(2010-2014)/Penny for Your Soul (v1-v3)(2010-2013)/01 Penny For Your Soul v1 (001-007+)(2010-2011)(Minutemen-Midas+)/Penny For Your Soul 01 (Develish Delight - Jay Company Comics) (Superklunker-DCP).cbr

### 2000ad prog 2025  — identical size  *(issue)*

- `   38 MB`  2000AD prog/2000AD prog 2025 (2017) (digital) (juvecube).cbr
- `   38 MB`  2000AD prog/2000AD Judge Dredd January - June 2017 (juvecube)/2000AD progs 2012-2037/2000AD prog 2025 (2017) (juvecube).cbr

### judge dredd mechchismo  — identical size  *(issue)*

- `   38 MB`  Judge Dredd - Collections/Judge Dredd - Mechchismo (2009) (digital) (JeffAlbertson-DCP)/Judge Dredd - Mechchismo (2009) (digital) (JeffAlbertson-DCP).cbz
- `   38 MB`  2000AD - Collections /Judge Dredd/Judge Dredd - Mechchismo (2009) (2000AD) (digital) (JeffAlbertson-DCP).cbz

### heavy metal — v1 — #03  — identical size  *(volume)*

- `   38 MB`  Heavy Metal/Heavy Metal Vols 01-35 (1977-2012)/Heavy Metal v01 03 (1977-06).cbr
- `   38 MB`  Heavy Metal/01. Main Series/Heavy Metal v01 03 (1977-06).cbr

### hellboy and b.p.r.d. saturn returns — #03  — identical size  *(issue)*

- `   38 MB`  Hellboy/Hellboy and the B.P.R.D. - Saturn Returns 03 (of 03) (2019) (digital) (Son of Ultron-Empire).cbr
- `   38 MB`  Hellboy/Hellboy and the B.P.R.D. - Saturn Returns 01-03 (2019) (digital) (Son of Ultron-Empire)/Hellboy and the B.P.R.D. - Saturn Returns 03 (of 03) (2019) (digital) (Son of Ultron-Empire).cbr

### heavy metal — v17 — #04  — identical size  *(volume)*

- `   38 MB`  Heavy Metal/Heavy Metal Vols 01-35 (1977-2012)/Heavy Metal v17 04 (1993-09).cbr
- `   38 MB`  Heavy Metal/01. Main Series/Heavy Metal v17 04 (1993-09).cbr

### love and rockets stories  *(issue)*

- `   38 MB`  Hernandez brothers/Love and Rockets/Love and Rockets - Stories (FCBD 2016) (digital-Minutemen).cbz
- `   38 MB`  Hernandez brothers/Gilbert Hernandez book digital editions/Love and Rockets - Stories (2016 - FCBD edition) (digital-Empire).cbr

### 2000ad prog 2003  *(issue)*

- `   42 MB`  2000AD prog/2000AD prog 2003 (2016) (digital) (juvecube).cbr
- `   33 MB`  2000AD prog/2000AD (Specials, Annuals & Poster Progs + Extras)/2000AD Yearbooks & Specials (1977 - 2013)/2000AD Yearbooks (Prog 2000 - 2013)/2000AD Prog 2003.cbr

### 2000ad prog 2020  — identical size  *(issue)*

- `   38 MB`  2000AD prog/2000AD prog 2020 (2017) (digital) (juvecube).cbr
- `   38 MB`  2000AD prog/2000AD Judge Dredd January - June 2017 (juvecube)/2000AD progs 2012-2037/2000AD prog 2020 (2017) (juvecube).cbr

### heavy metal — v2 — #07  — identical size  *(volume)*

- `   37 MB`  Heavy Metal/Heavy Metal Vols 01-35 (1977-2012)/Heavy Metal v02 07 (1978-11).cbr
- `   37 MB`  Heavy Metal/01. Main Series/Heavy Metal v02 07 (1978-11).cbr

### borgia — #2  *(issue)*

- `   41 MB`  Jodorowsky and Moebius/Borgia 1 - 4/Borgia 2 - The Power And The Incest.cbr
- `   34 MB`  Milo Manara/Borgia Milo Manara Full Comic/Borgia 2-3 - Heavy Metal version/Borgia 2 - Power and Incest (2006).cbr

### 2000ad prog 2031  — identical size  *(issue)*

- `   37 MB`  2000AD prog/2000AD prog 2031 (2017) (digital) (juvecube).cbr
- `   37 MB`  2000AD prog/2000AD Judge Dredd January - June 2017 (juvecube)/2000AD progs 2012-2037/2000AD prog 2031 (2017) (juvecube).cbr

### 2000ad prog 2027  — identical size  *(issue)*

- `   37 MB`  2000AD prog/2000AD prog 2027 (2017) (digital) (juvecube).cbr
- `   37 MB`  2000AD prog/2000AD Judge Dredd January - June 2017 (juvecube)/2000AD progs 2012-2037/2000AD prog 2027 (2017) (juvecube).cbr

### new avengers — #32  *(issue)*

- `   33 MB`  Alias  ( Jessica Jones , The Pulse & Appearances)/Appearances/New Avengers (2010)/New Avengers 32(c2c)(2013)(Re-em-Novus-HD).cbr
- `   24 MB`  Alias  ( Jessica Jones , The Pulse & Appearances)/Appearances/New Avengers (2010)/New Avengers 32(c2c)(2013)(Re-em-Novus).cbr
- `   18 MB`  Alias  ( Jessica Jones , The Pulse & Appearances)/Appearances/New Avengers (2010)/New Avengers 32(2013)(Digital)(C9-Novus).cbr

### luke cage noir — #01  — identical size  *(issue)*

- `   37 MB`  GG Studio (Collection) (2010-2012)/Marvel Noir (2009-2011)(digital)/Luke Cage Noir (001-004+)(2009-2010)(digital)(Minutemen-Faessla)/Luke Cage Noir 01 (of 4) (2009) (digital) (Minutemen-Faessla).cbz
- `   37 MB`  Aster Blistok/Le Vagabond des Limbes/Luke Cage Noir (001-004+)(2009-2010)(digital)(Minutemen-Faessla)/Luke Cage Noir 01 (of 4) (2009) (digital) (Minutemen-Faessla).cbz

### creator owned heroes — #06  *(issue)*

- `   49 MB`  Image comics/Creator Owned Heroes (001-008)(2012-2013)/Creator Owned Heroes 06 (2012) (2 Covers) (Tarutaru-Novus).cbr
- `   24 MB`  Image comics/Creator Owned Heroes (001-008)(2012-2013)/Creator-Owned Heroes 06 (2012) (Digital) (K6DVR-Empire).cbr

### avengers — #019  *(issue)*

- `   43 MB`  Avengers/Avengers (2018-2019)/Avengers 019 (2019) (Digital) (Zone-Empire).cbr
- `   30 MB`  Alias  ( Jessica Jones , The Pulse & Appearances)/Appearances/Avengers (2010)/Avengers 019 (2012) (Minutemen-DarthSax).cbr

### dredd final judgement  — identical size  *(issue)*

- `   36 MB`  Judge Dredd - Collections/Dredd - Final Judgement (2000) (digital) (JeffAlbertson-DCP)/Dredd - Final Judgement (2000) (digital) (JeffAlbertson-DCP).cbz
- `   36 MB`  2000AD - Collections /Judge Dredd/Dredd - Final Judgement (2000) (2000AD) (digital) (JeffAlbertson-DCP).cbz

### low life — v5  — identical size  *(volume)*

- `   36 MB`  2000AD - Collections /Low Life (2000AD)/Low Life V5 Creation _ More (Dan Dare 2000AD Remix).cbr
- `   36 MB`  2000AD - Collections /Low Life (2000AD)/Low Life V5 Creation & More (Dan Dare 2000AD Remix).cbr

### 2000ad prog 2033  — identical size  *(issue)*

- `   36 MB`  2000AD prog/2000AD prog 2033 (2017) (digital) (juvecube).cbr
- `   36 MB`  2000AD prog/2000AD Judge Dredd January - June 2017 (juvecube)/2000AD progs 2012-2037/2000AD prog 2033 (2017) (juvecube).cbr

### twisted times  — identical size  *(issue)*

- `   36 MB`  2000AD prog/Alan Moore -2000AD/Twisted Times.cbr
- `   36 MB`  2000AD prog/2000AD (Specials, Annuals & Poster Progs + Extras)/Related/Twisted Times.cbr

### 2000ad prog 2032  — identical size  *(issue)*

- `   36 MB`  2000AD prog/2000AD prog 2032 (2017) (digital) (juvecube).cbr
- `   36 MB`  2000AD prog/2000AD Judge Dredd January - June 2017 (juvecube)/2000AD progs 2012-2037/2000AD prog 2032 (2017) (juvecube).cbr

### alice forever after — #03  *(issue)*

- `   42 MB`  Alice Forever After/Alice Forever After 03 (of 05) (2026) (Digital) (Mephisto-Empire).cbr
- `   29 MB`  Alice Forever After/Alice Forever After 03 (of 05) (2026) (Digital Rip) (Hourman-DCP).cbr

### dash shaw cosplayers — #002  — identical size  *(issue)*

- `   35 MB`  Dash Shaw - Cosplayers (2014)/Dash Shaw - Cosplayers 002 (2014).cbr
- `   35 MB`  Dash Shaw - Cosplayers (2014)/Dash Shaw - Cosplayers (2014)/Dash Shaw - Cosplayers 002 (2014).cbr

### 2000ad prog 2023  — identical size  *(issue)*

- `   35 MB`  2000AD prog/2000AD prog 2023 (2017) (digital) (juvecube).cbr
- `   35 MB`  2000AD prog/2000AD Judge Dredd January - June 2017 (juvecube)/2000AD progs 2012-2037/2000AD prog 2023 (2017) (juvecube).cbr

### hellboy wolves of saint august  *(issue)*

- `   51 MB`  Hellboy/Hellboy - The Wolves of Saint August.cbr
- `   19 MB`  Hellboy/84.)  Hellboy - The Wolves of Saint August  (1995 AD)/Hellboy - The Wolves of Saint August.cbr

### activity — #011  *(issue)*

- `   49 MB`  Image comics/Activity (001-016)(2011-2014)/The Activity 011 (2012) (Digital-HD) (JK-Empire).cbr
- `   21 MB`  Image comics/Activity (001-016)(2011-2014)/The Activity 011 (2013) (Digital) (JK-Empire).cbz

### 282 chopper song of surfer — v1  — identical size  *(volume)*

- `   35 MB`  Judge Dredd The Megazine/Judge Dredd Megazine v5 (201-400)(2002-ongoing)/J.D Megazine Supplements/282 - Chopper - Song of the Surfer Volume 1.cbr
- `   35 MB`  Judge Dredd The Megazine/J.D Megazine Supplements/282 - Chopper - Song of the Surfer Volume 1.cbr

### steam wars — #01  *(issue)*

- `   37 MB`  Steam Wars (2013-2017) (digital) (Minutemen-The Undead)/Steam Wars (001-005) (2013-2014) (digital) (Minutemen-The Undead)/Steam Wars 01 (of 05) (2013) (digital) (Minutemen-The Undead).cbr
- `   33 MB`  Steam Wars (2013-2017) (digital) (Minutemen-The Undead)/Steam Wars 01 (FCBD Edition) (2014) (Team-DCP).cbr

### 2000ad prog 2030  — identical size  *(issue)*

- `   34 MB`  2000AD prog/2000AD prog 2030 (2017) (digital) (juvecube).cbr
- `   34 MB`  2000AD prog/2000AD Judge Dredd January - June 2017 (juvecube)/2000AD progs 2012-2037/2000AD prog 2030 (2017) (juvecube).cbr

### 321 death planet  — identical size  *(issue)*

- `   34 MB`  Judge Dredd The Megazine/Judge Dredd Megazine v5 (201-400)(2002-ongoing)/J.D Megazine Supplements/321 - Death Planet.cbr
- `   34 MB`  Judge Dredd The Megazine/J.D Megazine Supplements/321 - Death Planet.cbr

### lobster johnson a chain forged in life  *(issue)*

- `   45 MB`  Hellboy/16.)  Lobster Johnson - A Chain Forged in Life  (193- AD)/Lobster Johnson - A Chain Forged in Life.cbr
- `   23 MB`  Hellboy/Lobster Johnson/Lobster Johnson - A Chain Forged in Life (2015) (digital) (Minutemen-InnerDemons).cbr

### 322 purgatory  — identical size  *(issue)*

- `   34 MB`  Judge Dredd The Megazine/Judge Dredd Megazine v5 (201-400)(2002-ongoing)/J.D Megazine Supplements/322 - Purgatory.cbr
- `   34 MB`  Judge Dredd The Megazine/J.D Megazine Supplements/322 - Purgatory.cbr

### pustinjske skorpije — #01  — identical size  *(issue)*

- `   33 MB`  YU stripovi 2019/Korto (YU)/pustinjske skorpije 01.cbr
- `   33 MB`  Corto Maltese/pustinjske skorpije 01.cbr

### avengers — #017  *(issue)*

- `   39 MB`  Avengers/Avengers (2018-2019)/Avengers 017 (2019) (Digital) (Zone-Empire).cbr
- `   27 MB`  Alias  ( Jessica Jones , The Pulse & Appearances)/Appearances/Avengers (2010)/Avengers 017 (2011) (three covers) (Minutemen-DarthSax).cbr

### judge dredd total war  — identical size  *(issue)*

- `   33 MB`  Judge Dredd - Collections/Judge Dredd - Total War (2013) (digital) (JeffAlbertson-DCP)/Judge Dredd - Total War (2013) (digital) (JeffAlbertson-DCP).cbz
- `   33 MB`  2000AD - Collections /Judge Dredd/Judge Dredd - Total War (2013) (2000AD) (digital) (JeffAlbertson-DCP).cbz

### heavy metal — v5 — #02  — identical size  *(volume)*

- `   33 MB`  Heavy Metal/Heavy Metal Vols 01-35 (1977-2012)/Heavy Metal v05 02 (1981-05).cbr
- `   33 MB`  Heavy Metal/01. Main Series/Heavy Metal v05 02 (1981-05).cbr

### 2 batman nosferatu  — identical size  *(issue)*

- `   33 MB`  Ted McKeever (Collection) (1987-2007)/1997 - Metropolis - 1999 - Nosferatu - 2003 - Blue Amazon (DC - w R & J-M Lofficier)/2 - Batman - Nosferatu (1999).cbr
- `   33 MB`  Elseworlds/2 - Batman - Nosferatu (1999).cbr

### 313 mercy heights  — identical size  *(issue)*

- `   32 MB`  Judge Dredd The Megazine/Judge Dredd Megazine v5 (201-400)(2002-ongoing)/J.D Megazine Supplements/313 - Mercy Heights (Book 1).cbr
- `   32 MB`  Judge Dredd The Megazine/J.D Megazine Supplements/313 - Mercy Heights (Book 1).cbr

### penny for your soul death — v3 — #002  *(volume)*

- `   60 MB`  Penny For Your Soul (v1-v3+)(2010-2014)/Penny for Your Soul (v1-v3)(2010-2013)/04 Penny For Your Soul v3 - Death v3 (001-004+)(2013)(Darkness-Empire)/Penny For Your Soul - Death v3 002 (2013) (c2c) (Darkness-Empire).cbr
- `    5 MB`  Penny For Your Soul (v1-v3+)(2010-2014)/Penny for Your Soul (v1-v3)(2010-2013)/04 Penny For Your Soul v3 - Death v3 (001-004+)(2013)(Darkness-Empire)/Penny For Your Soul - Death v3 002 (2013) (Jen Broomall Cover B ONLY) (Darkness-Empire).cbr

### buck rogers — #003  *(issue)*

- `   37 MB`  Buck Rogers (2009)/Buck Rogers (001-004)(2013)(Eisenhart-DCP)/Buck Rogers 003 (2013) (Eisenhart-DCP).cbr
- `   27 MB`  Buck Rogers (2009)/Buck Rogers 003 (2009) (digital) (Son of Ultron-Empire).cbr

### buck rogers — #001  *(issue)*

- `   39 MB`  Buck Rogers (2009)/Buck Rogers (001-004)(2013)(Eisenhart-DCP)/Buck Rogers 001 (2013) (Eisenhart-DCP).cbr
- `   26 MB`  Buck Rogers (2009)/Buck Rogers 001 (2009) (digital) (Son of Ultron-Empire).cbr

### buck rogers — #002  *(issue)*

- `   39 MB`  Buck Rogers (2009)/Buck Rogers (001-004)(2013)(Eisenhart-DCP)/Buck Rogers 002 (2013) (Eisenhart-DCP).cbr
- `   26 MB`  Buck Rogers (2009)/Buck Rogers 002 (2009) (digital) (Son of Ultron-Empire).cbr

### 328 ratfink  — identical size  *(issue)*

- `   32 MB`  Judge Dredd The Megazine/Judge Dredd Megazine v5 (201-400)(2002-ongoing)/J.D Megazine Supplements/328 - Ratfink.cbr
- `   32 MB`  Judge Dredd The Megazine/J.D Megazine Supplements/328 - Ratfink.cbr

### 326 bato loco  — identical size  *(issue)*

- `   32 MB`  Judge Dredd The Megazine/Judge Dredd Megazine v5 (201-400)(2002-ongoing)/J.D Megazine Supplements/326 - Bato Loco.cbr
- `   32 MB`  Judge Dredd The Megazine/J.D Megazine Supplements/326 - Bato Loco.cbr

### 318 venus bluegenes venus on frag shell  — identical size  *(issue)*

- `   32 MB`  Judge Dredd The Megazine/Judge Dredd Megazine v5 (201-400)(2002-ongoing)/J.D Megazine Supplements/318 - Venus Bluegenes - Venus on the Frag Shell.cbr
- `   32 MB`  Judge Dredd The Megazine/J.D Megazine Supplements/318 - Venus Bluegenes - Venus on the Frag Shell.cbr

### avengers — #018  *(issue)*

- `   46 MB`  Avengers/Avengers (2018-2019)/Avengers 018 (2019) (Digital) (Zone-Empire).cbr
- `   17 MB`  Alias  ( Jessica Jones , The Pulse & Appearances)/Appearances/Avengers (2010)/Avengers 018 (2011) (two covers) (Minutemen-DarthSax).cbr

### buck rogers — #004  *(issue)*

- `   36 MB`  Buck Rogers (2009)/Buck Rogers (001-004)(2013)(Eisenhart-DCP)/Buck Rogers 004 (2013) (Eisenhart-DCP).cbr
- `   27 MB`  Buck Rogers (2009)/Buck Rogers 004 (2009) (digital) (Son of Ultron-Empire).cbr

### 280 judge dredd colin wilson  — identical size  *(volume)*

- `   31 MB`  Judge Dredd The Megazine/Judge Dredd Megazine v5 (201-400)(2002-ongoing)/J.D Megazine Supplements/280 - Judge Dredd - The Colin Wilson Collection.cbr
- `   31 MB`  Judge Dredd The Megazine/J.D Megazine Supplements/280 - Judge Dredd - The Colin Wilson Collection.cbr

### 281 pussyfoot — #5  — identical size  *(issue)*

- `   31 MB`  Judge Dredd The Megazine/Judge Dredd Megazine v5 (201-400)(2002-ongoing)/J.D Megazine Supplements/281 - Pussyfoot 5 - Alien Sex Fiend.cbr
- `   31 MB`  Judge Dredd The Megazine/J.D Megazine Supplements/281 - Pussyfoot 5 - Alien Sex Fiend.cbr

### 312 flesh chronocide  — identical size  *(issue)*

- `   31 MB`  Judge Dredd The Megazine/Judge Dredd Megazine v5 (201-400)(2002-ongoing)/J.D Megazine Supplements/312 - Flesh - Chronocide.cbr
- `   31 MB`  Judge Dredd The Megazine/J.D Megazine Supplements/312 - Flesh - Chronocide.cbr

### pustinjske skorpije — #03  — identical size  *(issue)*

- `   31 MB`  YU stripovi 2019/Korto (YU)/pustinjske skorpije 03.cbr
- `   31 MB`  Corto Maltese/pustinjske skorpije 03.cbr

### 278 canon fodder  — identical size  *(issue)*

- `   31 MB`  Judge Dredd The Megazine/Judge Dredd Megazine v5 (201-400)(2002-ongoing)/J.D Megazine Supplements/278 - Canon Fodder.cbr
- `   31 MB`  Judge Dredd The Megazine/J.D Megazine Supplements/278 - Canon Fodder.cbr

### dredd anderson deep end  — identical size  *(issue)*

- `   31 MB`  Judge Dredd - Collections/Dredd-Anderson - The Deep End (2017) (2000AD) (digital) (JeffAlbertson-DCP)/Dredd-Anderson - The Deep End (2017) (2000AD) (digital) (JeffAlbertson-DCP).cbz
- `   31 MB`  2000AD - Collections /Judge Dredd/Dredd-Anderson - The Deep End (2017) (2000AD) (digital) (JeffAlbertson-DCP).cbz

### heavy metal — v2 — #09  — identical size  *(volume)*

- `   31 MB`  Heavy Metal/Heavy Metal Vols 01-35 (1977-2012)/Heavy Metal v02 09 (1979-01) (Incomplete).cbr
- `   31 MB`  Heavy Metal/01. Main Series/Heavy Metal v02 09 (1979-01) (Incomplete).cbr

### alan moore a small killing  — identical size  *(issue)*

- `   30 MB`  Alan Moore/Alan Moore Essentials/Alan Moore 1991- A Small Killing/Alan Moore- A Small Killing.cbr
- `   30 MB`  Alan Moore/Alan Moore Collection I- English Invasion/Alan Moore Collection III- 2000 AD/Alan Moore- A Small Killing.cbr

### covjek sa kariba  — identical size  *(issue)*

- `   30 MB`  YU stripovi 2019/Korto (YU)/covjek sa kariba.cbr
- `   30 MB`  Corto Maltese/covjek sa kariba.cbr

### doktor sleepless — #11  *(issue)*

- `   31 MB`  Warren Ellis/2007/2007 Doktor Sleepless/Doktor Sleepless #11.cbz
- `   29 MB`  Warren Ellis/Warren Ellis - Doktor Sleepless/Doktor Sleepless #11.cbz

### judge dredd mandroid  — identical size  *(issue)*

- `   30 MB`  Judge Dredd - Collections/Judge Dredd - Mandroid (2007) (digital) (JeffAlbertson-DCP)/Judge Dredd - Mandroid (2007) (digital) (JeffAlbertson-DCP).cbz
- `   30 MB`  2000AD - Collections /Judge Dredd/Judge Dredd - Mandroid (2007) (2000AD) (digital) (JeffAlbertson-DCP).cbz

### aster blistok — #01  *(issue)*

- `   36 MB`  Aster Blistok/Aster Blistok 01 - Svemirska lutalica (2001)(Serbian)(c2c)(nuncio-BDS-DCP).cbr
- `   24 MB`  Aster Blistok/Aster_Blistok_-_01_-_Svemirska_lutalica.cbr

### 311 flesh legend of shamana  — identical size  *(issue)*

- `   30 MB`  Judge Dredd The Megazine/Judge Dredd Megazine v5 (201-400)(2002-ongoing)/J.D Megazine Supplements/311 - Flesh - The Legend of Shamana (Book 2).cbr
- `   30 MB`  Judge Dredd The Megazine/J.D Megazine Supplements/311 - Flesh - The Legend of Shamana (Book 2).cbr

### heavy metal — v29 — #03  — identical size  *(volume)*

- `   30 MB`  Heavy Metal/Heavy Metal Vols 01-35 (1977-2012)/Heavy Metal v29 03 (2005).cbr
- `   30 MB`  Heavy Metal/01. Main Series/Heavy Metal v29 03 (2005).cbr

### secret history of authority jenny sparks  — identical size  *(issue)*

- `   30 MB`  Warren Ellis/The Authority/specials/Secret History/Secret History of the Authority - Jenny Sparks (#1-5).cbr
- `   30 MB`  The Authority/specials/Secret History/Secret History of the Authority - Jenny Sparks (#1-5).cbr

### 315 mercy heights  — identical size  *(issue)*

- `   30 MB`  Judge Dredd The Megazine/Judge Dredd Megazine v5 (201-400)(2002-ongoing)/J.D Megazine Supplements/315 - Mercy Heights (Book 3).cbr
- `   30 MB`  Judge Dredd The Megazine/J.D Megazine Supplements/315 - Mercy Heights (Book 3).cbr

### 314 mercy heights  — identical size  *(issue)*

- `   30 MB`  Judge Dredd The Megazine/Judge Dredd Megazine v5 (201-400)(2002-ongoing)/J.D Megazine Supplements/314 - Mercy Heights (Book 2).cbr
- `   30 MB`  Judge Dredd The Megazine/J.D Megazine Supplements/314 - Mercy Heights (Book 2).cbr

### borgia — #3  — identical size  *(issue)*

- `   29 MB`  Milo Manara/Borgia Milo Manara Full Comic/Borgia 2-3 - Heavy Metal version/Borgia 3 - Flames From Hell (2009).cbr
- `   29 MB`  Jodorowsky and Moebius/Borgia 1 - 4/Borgia 3 - Flames From Hell (2009) (Pudgy).cbr

### penny for your soul death — v3 — #001  *(volume)*

- `   53 MB`  Penny For Your Soul (v1-v3+)(2010-2014)/Penny for Your Soul (v1-v3)(2010-2013)/04 Penny For Your Soul v3 - Death v3 (001-004+)(2013)(Darkness-Empire)/Penny For Your Soul - Death v3 001 (2013) (c2c-1920px) (Darkness-Empire).cbr
- `    5 MB`  Penny For Your Soul (v1-v3+)(2010-2014)/Penny for Your Soul (v1-v3)(2010-2013)/04 Penny For Your Soul v3 - Death v3 (001-004+)(2013)(Darkness-Empire)/Penny For Your Soul - Death v3 001 (2013) (Natalie Sanders Cover C ONLY) (Darkness-Empire).cbr

### heavy metal — #25  *(issue)*

- `   29 MB`  Heavy Metal/Related_Publications/HEAVY METAL - 25 Years of Classic Covers (flattermann).cbr
- `   29 MB`  Heavy Metal/Heavy Metal - 25 Years of Classic Covers (2002).cbr

### 300 armageddon bad man  — identical size  *(issue)*

- `   29 MB`  Judge Dredd The Megazine/Judge Dredd Megazine v5 (201-400)(2002-ongoing)/J.D Megazine Supplements/300 - Armageddon - The Bad Man.cbr
- `   29 MB`  Judge Dredd The Megazine/J.D Megazine Supplements/300 - Armageddon - The Bad Man.cbr

### 307 samantha slade, robo hunter furzt case  — identical size  *(issue)*

- `   29 MB`  Judge Dredd The Megazine/Judge Dredd Megazine v5 (201-400)(2002-ongoing)/J.D Megazine Supplements/307 - Samantha Slade, Robo-Hunter - The Furzt Case.cbr
- `   29 MB`  Judge Dredd The Megazine/J.D Megazine Supplements/307 - Samantha Slade, Robo-Hunter - The Furzt Case.cbr

### 301 mick mcmahon  — identical size  *(volume)*

- `   29 MB`  Judge Dredd The Megazine/Judge Dredd Megazine v5 (201-400)(2002-ongoing)/J.D Megazine Supplements/301 - The Mick McMahon Collection (Judge Dredd).cbr
- `   29 MB`  Judge Dredd The Megazine/J.D Megazine Supplements/301 - The Mick McMahon Collection (Judge Dredd).cbr

### enki bilal dormant beast  *(issue)*

- `   29 MB`  Enki Bilal/Enki Bilal - The Dormant Beast.cbr
- `   29 MB`  Enki Bilal/Enki Bilal - Dormant Beast.cbr

### promethea — #32  *(issue)*

- `   40 MB`  Alan Moore/Alan Moore Collection IV-  America's Best Comics/Promethea/Promethea Extras/Promethea #32 (Poster Form-Large).cbr
- `   17 MB`  Alan Moore/Alan Moore Collection IV-  America's Best Comics/Promethea/Promethea Extras/Promethea #32 (Poster Form-Small).cbr

### 323 harry kipling  — identical size  *(issue)*

- `   29 MB`  Judge Dredd The Megazine/Judge Dredd Megazine v5 (201-400)(2002-ongoing)/J.D Megazine Supplements/323 - Harry Kipling (Deceased).cbr
- `   29 MB`  Judge Dredd The Megazine/J.D Megazine Supplements/323 - Harry Kipling (Deceased).cbr

### official handbook of invincible universe — #01  — identical size  *(issue)*

- `   28 MB`  Robert Kirkman/Invincible (Kirkman)/The Official Handbook of the Invincible Universe/The Official Handbook of the Invincible Universe 01 (of 02) (fixed) (2006) (Minutemen-Mr.Shepherd).cbr
- `   28 MB`  Robert Kirkman/Invincible (Kirkman)/Extras/The Official Handbook of the Invincible Universe 01 (of 02).cbr

### authority vs lobo.#2.spring break massacre  — identical size  *(issue)*

- `   28 MB`  Warren Ellis/The Authority/specials/Authority vs Lobo/The Authority vs Lobo.#2.Spring Break Massacre (2005).cbr
- `   28 MB`  The Authority/specials/Authority vs Lobo/The Authority vs Lobo.#2.Spring Break Massacre (2005).cbr

### heavy metal presents swords of heaven, flowers of hell  — identical size  *(issue)*

- `   28 MB`  Heavy Metal/Heavy Metal Presents/Heavy Metal Presents - The Swords of Heaven, the Flowers of Hell (1979).cbr
- `   28 MB`  Heavy Metal/03. Extras/Heavy Metal Presents - The Swords of Heaven, the Flowers of Hell (1979).cbr

### 327 marauder  — identical size  *(issue)*

- `   28 MB`  Judge Dredd The Megazine/Judge Dredd Megazine v5 (201-400)(2002-ongoing)/J.D Megazine Supplements/327 - Marauder.cbr
- `   28 MB`  Judge Dredd The Megazine/J.D Megazine Supplements/327 - Marauder.cbr

### avengers — #015  *(issue)*

- `   36 MB`  Avengers/Avengers (2018-2019)/Avengers 015 (2019) (digital) (Oroboros-DCP).cbr
- `   20 MB`  Alias  ( Jessica Jones , The Pulse & Appearances)/Appearances/Avengers (2010)/Avengers 015 (2011) (Minutemen-TwiztidSax).cbr

### pustinjske skorpije — #02  — identical size  *(issue)*

- `   28 MB`  YU stripovi 2019/Korto (YU)/pustinjske skorpije 02.cbr
- `   28 MB`  Corto Maltese/pustinjske skorpije 02.cbr

### 303 chiaroscuro  — identical size  *(issue)*

- `   28 MB`  Judge Dredd The Megazine/Judge Dredd Megazine v5 (201-400)(2002-ongoing)/J.D Megazine Supplements/303 - Chiaroscuro.cbr
- `   28 MB`  Judge Dredd The Megazine/J.D Megazine Supplements/303 - Chiaroscuro.cbr

### amazing spider man — v2 — #672  — identical size  *(volume)*

- `   28 MB`  Alias  ( Jessica Jones , The Pulse & Appearances)/Appearances/Spider Island/Amazing Spider-Man v2 672 (2011) (Minutemen-DTs).cbz
- `   28 MB`  Alias  ( Jessica Jones , The Pulse & Appearances)/Appearances/Amazing Spider-man/Amazing Spider-Man v2 672 (2011) (Minutemen-DTs).cbz

### detection club — #02  — identical size  *(issue)*

- `   28 MB`  Europe Comics (Collection)/The Detection Club 02 (Europe Comics 2020) (webrip) (MagicMan-DCP).cbr
- `   28 MB`  Europe Comics (Collection)/The Detection Club 01-02 (2020)/The Detection Club 02 (2020) (webrip) (MagicMan-DCP).cbr

### 305 strontium dogs return of gronk  — identical size  *(issue)*

- `   28 MB`  Judge Dredd The Megazine/Judge Dredd Megazine v5 (201-400)(2002-ongoing)/J.D Megazine Supplements/305 - Strontium Dogs - Return of the Gronk.cbr
- `   28 MB`  Judge Dredd The Megazine/J.D Megazine Supplements/305 - Strontium Dogs - Return of the Gronk.cbr

### 308 samantha slade, robo hunter casino royale  — identical size  *(issue)*

- `   28 MB`  Judge Dredd The Megazine/Judge Dredd Megazine v5 (201-400)(2002-ongoing)/J.D Megazine Supplements/308 - Samantha Slade, Robo Hunter - Casino Royale.cbr
- `   28 MB`  Judge Dredd The Megazine/J.D Megazine Supplements/308 - Samantha Slade, Robo Hunter - Casino Royale.cbr

### science dog — #02  — identical size  *(special)*

- `   28 MB`  Robert Kirkman/Invincible (Kirkman)/Extras/Science Dog/Science Dog Special 02 (2011) (digital) (Minutemen-InnerDemons).cbr
- `   28 MB`  Image comics/Science Dog Special (001-002)(2010)/Science Dog Special 02 (2011) (digital) (Minutemen-InnerDemons).cbr

### official handbook of invincible universe — #02  *(issue)*

- `   28 MB`  Robert Kirkman/Invincible (Kirkman)/Extras/The Official Handbook of the Invincible Universe 02.cbz
- `   28 MB`  Robert Kirkman/Invincible (Kirkman)/The Official Handbook of the Invincible Universe/The Official Handbook of the Invincible Universe 02 (2007) (TheCaptain-DCP).cbr

### 3 wonder woman blue amazon  — identical size  *(issue)*

- `   28 MB`  Ted McKeever (Collection) (1987-2007)/1997 - Metropolis - 1999 - Nosferatu - 2003 - Blue Amazon (DC - w R & J-M Lofficier)/3 - Wonder Woman - Blue Amazon (2003).cbr
- `   28 MB`  Elseworlds/3 - Wonder Woman - Blue Amazon (2003).cbr

### street fighter & friends swimsuit — #001  *(special)*

- `   29 MB`  Street Fighter & Friends Swimsuit Special/Street Fighter & Friends Swimsuit Special 001 (2024).cbz
- `   26 MB`  Street Fighter & Friends Swimsuit Special/Street Fighter & Friends Swimsuit Special 001 (2025).cbz

### extinction seed — #000  *(issue)*

- `   32 MB`  GG Studio (Collection) (2010-2012)/Extinction Seed (001-003) (2011-2012)/Extinction Seed 000 (2011) (Digital) (K6-Empire).cbr
- `   24 MB`  GG Studio (Collection) (2010-2012)/Extinction Seed (001-003) (2011-2012)/Extinction Seed 000 (2011) (3 covers) (Minutemen-DarthSax).cbr

### amazing spider man — v2 — #670  — identical size  *(volume)*

- `   27 MB`  Alias  ( Jessica Jones , The Pulse & Appearances)/Appearances/Spider Island/Amazing Spider-Man v2 670 (2011) (Minutemen-DTs).cbz
- `   27 MB`  Alias  ( Jessica Jones , The Pulse & Appearances)/Appearances/Amazing Spider-man/Amazing Spider-Man v2 670 (2011) (Minutemen-DTs).cbz

### 310 flesh legend of shamana  — identical size  *(issue)*

- `   27 MB`  Judge Dredd The Megazine/Judge Dredd Megazine v5 (201-400)(2002-ongoing)/J.D Megazine Supplements/310 - Flesh - The Legend of Shamana (Book 1).cbr
- `   27 MB`  Judge Dredd The Megazine/J.D Megazine Supplements/310 - Flesh - The Legend of Shamana (Book 1).cbr

### planetary jla terra occulta  *(issue)*

- `   30 MB`  Warren Ellis/Planetary/Planetary-JLA - Terra Occulta (2002) (digital-Empire).cbz
- `   25 MB`  Warren Ellis/1999/1999 Planetary/Specials/Planetary - JLA - Terra Occulta.cbr

### deadpool pulp — #03  — identical size  *(issue)*

- `   27 MB`  GG Studio (Collection) (2010-2012)/Marvel Noir (2009-2011)(digital)/Deadpool Pulp (001-004)(2010-2011)(digital)(Minutemen-PhD)/Deadpool Pulp 03 (of 04) (2011) (digital) (Minutemen-PhD).cbr
- `   27 MB`  Aster Blistok/Le Vagabond des Limbes/Deadpool Pulp (001-004)(2010-2011)(digital)(Minutemen-PhD)/Deadpool Pulp 03 (of 04) (2011) (digital) (Minutemen-PhD).cbr

### 309 ian gibson  — identical size  *(volume)*

- `   27 MB`  Judge Dredd The Megazine/Judge Dredd Megazine v5 (201-400)(2002-ongoing)/J.D Megazine Supplements/309 - The Ian Gibson Collection (Judge Dredd).cbr
- `   27 MB`  Judge Dredd The Megazine/J.D Megazine Supplements/309 - The Ian Gibson Collection (Judge Dredd).cbr

### missionary man bad moon rising  — identical size  *(issue)*

- `   27 MB`  Missionary Man - Bad Moon Rising (2011) (digital) (JeffAlbertson-DCP)/Missionary Man - Bad Moon Rising (2011) (digital) (JeffAlbertson-DCP).cbz
- `   27 MB`  2000AD - Collections /Missionary Man - Bad Moon Rising (2011) (2000AD) (digital) (JeffAlbertson-DCP).cbz

### deadpool pulp — #02  — identical size  *(issue)*

- `   27 MB`  GG Studio (Collection) (2010-2012)/Marvel Noir (2009-2011)(digital)/Deadpool Pulp (001-004)(2010-2011)(digital)(Minutemen-PhD)/Deadpool Pulp 02 (of 04) (2010) (digital) (Minutemen-PhD).cbr
- `   27 MB`  Aster Blistok/Le Vagabond des Limbes/Deadpool Pulp (001-004)(2010-2011)(digital)(Minutemen-PhD)/Deadpool Pulp 02 (of 04) (2010) (digital) (Minutemen-PhD).cbr

### hellboy corpse and iron shoes  *(issue)*

- `   40 MB`  Hellboy/Hellboy - The Corpse and the Iron Shoes.cbr
- `   14 MB`  Hellboy/Hellboy - The Corpse and The Iron Shoes (1996) (digital) (Minutemen-InnerDemons).cbr

### warren ellis supergod — #04  — identical size  *(issue)*

- `   27 MB`  Warren Ellis/WARREN ELLIS - SUPERGOD 01-05/Warren_Ellis__Supergod_04__2010___two_covers___Minutemen-DTs_.cbz
- `   27 MB`  Warren Ellis/2009/2009 Supergod/Warren_Ellis__Supergod_04__2010___two_covers___Minutemen-DTs_.cbz

### 320 strontium dogs crossroads  — identical size  *(issue)*

- `   27 MB`  Judge Dredd The Megazine/Judge Dredd Megazine v5 (201-400)(2002-ongoing)/J.D Megazine Supplements/320 - Strontium Dogs - Crossroads.cbr
- `   27 MB`  Judge Dredd The Megazine/J.D Megazine Supplements/320 - Strontium Dogs - Crossroads.cbr

### sugarvirus  — identical size  *(issue)*

- `   18 MB`  Warren Ellis/Warren Ellis - Vampirella, Shi, Dracula/Sugarvirus (From Bad Blood - The Vampire Collection).cbz
- `   18 MB`  Warren Ellis/Sugarvirus (From Bad Blood - The Vampire Collection).cbz
- `   18 MB`  Warren Ellis/1993 Lazarus Churchyard + Sugarvirus/Sugarvirus (From Bad Blood - The Vampire Collection).cbz

### deadpool pulp — #01  — identical size  *(issue)*

- `   26 MB`  GG Studio (Collection) (2010-2012)/Marvel Noir (2009-2011)(digital)/Deadpool Pulp (001-004)(2010-2011)(digital)(Minutemen-PhD)/Deadpool Pulp 01 (of 04) (2010) (digital) (Minutemen-PhD).cbr
- `   26 MB`  Aster Blistok/Le Vagabond des Limbes/Deadpool Pulp (001-004)(2010-2011)(digital)(Minutemen-PhD)/Deadpool Pulp 01 (of 04) (2010) (digital) (Minutemen-PhD).cbr

### 304 armitage bodies of evidence  — identical size  *(issue)*

- `   26 MB`  Judge Dredd The Megazine/Judge Dredd Megazine v5 (201-400)(2002-ongoing)/J.D Megazine Supplements/304 - Armitage - Bodies of Evidence.cbr
- `   26 MB`  Judge Dredd The Megazine/J.D Megazine Supplements/304 - Armitage - Bodies of Evidence.cbr

### 296 best of pulp sci fi  — identical size  *(issue)*

- `   26 MB`  Judge Dredd The Megazine/Judge Dredd Megazine v5 (201-400)(2002-ongoing)/J.D Megazine Supplements/296 - The Best of Pulp Sci-Fi.cbr
- `   26 MB`  Judge Dredd The Megazine/J.D Megazine Supplements/296 - The Best of Pulp Sci-Fi.cbr

### judge dredd classics  *(issue)*

- `   45 MB`  2000AD prog/Yearbooks & Specials/FCBD/Judge Dredd Classics (FCBD 2013) (digital) (Minutemen-Thoth).cbr
- `    7 MB`  2000AD prog/Yearbooks & Specials/Specials/Judge Dredd/Judge Dredd Classics (FCBD 2013) (Reprints Dredd vs Judge Death).cbr

### 275 jock  — identical size  *(volume)*

- `   26 MB`  Judge Dredd The Megazine/Judge Dredd Megazine v5 (201-400)(2002-ongoing)/J.D Megazine Supplements/275 - The Jock Collection.cbr
- `   26 MB`  Judge Dredd The Megazine/J.D Megazine Supplements/275 - The Jock Collection.cbr

### activity — #002  *(issue)*

- `   35 MB`  Image comics/Activity (001-016)(2011-2014)/The Activity 002 (2012) (digital-Empire).cbz
- `   17 MB`  Image comics/Activity (001-016)(2011-2014)/The Activity 002 (2012) (F) (digital-Empire).cbr

### 324 tiger sun, dragon moon  — identical size  *(issue)*

- `   26 MB`  Judge Dredd The Megazine/Judge Dredd Megazine v5 (201-400)(2002-ongoing)/J.D Megazine Supplements/324 - Tiger Sun, Dragon Moon.cbr
- `   26 MB`  Judge Dredd The Megazine/J.D Megazine Supplements/324 - Tiger Sun, Dragon Moon.cbr

### wildstorm summer  — identical size  *(special)*

- `   25 MB`  Warren Ellis/The Authority/specials/Wildstorm Summer Special 2001.cbr
- `   25 MB`  The Authority/specials/Wildstorm Summer Special 2001.cbr

### heavy metal — v29 — #02  — identical size  *(volume)*

- `   25 MB`  Heavy Metal/Heavy Metal Vols 01-35 (1977-2012)/Heavy Metal v29 02 (2005).cbr
- `   25 MB`  Heavy Metal/01. Main Series/Heavy Metal v29 02 (2005).cbr

### 325 american gothic  — identical size  *(issue)*

- `   25 MB`  Judge Dredd The Megazine/Judge Dredd Megazine v5 (201-400)(2002-ongoing)/J.D Megazine Supplements/325 - American Gothic.cbr
- `   25 MB`  Judge Dredd The Megazine/J.D Megazine Supplements/325 - American Gothic.cbr

### blackhand ironhead — #001  — identical size  *(issue)*

- `   25 MB`  Blackhand Ironhead #1 - 5 (2017-2018)/Blackhand Ironhead 001-004 (2017-2018)/Blackhand Ironhead 001 (2018) (digital) (panelsyndicate.com).cbr
- `   25 MB`  Aster Blistok/Le Vagabond des Limbes/Blackhand Ironhead 001-004 (2017-2018)/Blackhand Ironhead 001 (2018) (digital) (panelsyndicate.com).cbr

### 1 superman's metropolis  — identical size  *(issue)*

- `   25 MB`  Ted McKeever (Collection) (1987-2007)/1997 - Metropolis - 1999 - Nosferatu - 2003 - Blue Amazon (DC - w R & J-M Lofficier)/1 - Superman's Metropolis (1997).cbr
- `   25 MB`  Elseworlds/1 - Superman's Metropolis (1997).cbr

### 306 strontium dogs darkest star  — identical size  *(issue)*

- `   25 MB`  Judge Dredd The Megazine/Judge Dredd Megazine v5 (201-400)(2002-ongoing)/J.D Megazine Supplements/306 - Strontium Dogs - The Darkest Star.cbr
- `   25 MB`  Judge Dredd The Megazine/J.D Megazine Supplements/306 - Strontium Dogs - The Darkest Star.cbr

### sandman midnight theatre  *(issue)*

- `   25 MB`  The Sandman/Sandman Midnight Theatre/Sandman Midnight Theatre.cbr
- `   24 MB`  The Sandman/The Sandman - Extras/Sandman - Midnight Theatre.cbz

### dc comics presents jungle line  — identical size  *(issue)*

- `   16 MB`  Alan Moore/Alan Moore Essentials/Alan Moore 1987- The Saga Of The Swamp Thing/DC Comics Presents #085- Jungle Line.cbr
- `   16 MB`  Alan Moore/Alan Moore Collection II-  DC/Swamp Thing/The Saga Of The Swamp Thing Extras/DC Comics Presents #085- Jungle Line.cbr
- `   16 MB`  Alan Moore/Alan Moore Collection II-  DC/Superman/DC Comics Presents #085- Jungle Line.cbr

### 295 strontium dogs monsters  — identical size  *(issue)*

- `   24 MB`  Judge Dredd The Megazine/Judge Dredd Megazine v5 (201-400)(2002-ongoing)/J.D Megazine Supplements/295 - Strontium Dogs - Monsters.cbr
- `   24 MB`  Judge Dredd The Megazine/J.D Megazine Supplements/295 - Strontium Dogs - Monsters.cbr

### spirit — #029  *(issue)*

- `   35 MB`  Will Eisner/The Spirit 001-087 (1983-1992)/The Spirit 029 (1987) (Kitchen Sink) (c2c) (emcee).cbr
- `   14 MB`  Will Eisner/The Spirit 001-087 (1983-1992)/The Spirit 029 (1987) (Kitchen Sink) (c2c) (brianzc-DCP).cbr

### midnighter — #06  — identical size  *(issue)*

- `   16 MB`  Warren Ellis/The Authority/Midnighter/Midnighter 06.cbr
- `   16 MB`  The Authority/Midnighter/Midnighter 06.cbr
- `   16 MB`  Garth Ennis Collection/Midnighter/Midnighter 06.cbr

### heavy metal — v23 — #02  — identical size  *(volume)*

- `   24 MB`  Heavy Metal/Heavy Metal Vols 01-35 (1977-2012)/Heavy Metal v23 02 (1999).cbr
- `   24 MB`  Heavy Metal/01. Main Series/Heavy Metal v23 02 (1999).cbr

### neonomicon — #002  — identical size  *(issue)*

- `   24 MB`  Alan Moore/Alan Moore Essentials/Alan Moore 2010- Neonomicon/Neonomicon #002.cbr
- `   24 MB`  Alan Moore/Alan Moore Collection V- More Moore/Neonomicon/Neonomicon #002.cbr

### many worlds of tesla strong  — identical size  *(issue)*

- `   24 MB`  Alan Moore/Alan Moore Essentials/Alan Moore 2006- Tom Strong/The Many Worlds of Tesla Strong (Arthur Adams and Bruce Timm covers).cbr
- `   24 MB`  Alan Moore/Alan Moore Collection IV-  America's Best Comics/Tom Strong/The Many Worlds of Tesla Strong (Arthur Adams and Bruce Timm covers).cbr

### planetary & authority ruling world  *(issue)*

- `   20 MB`  Warren Ellis/The Authority/specials/Planetary & The Authority - Ruling the World (2000).cbr
- `   20 MB`  The Authority/specials/Planetary & The Authority - Ruling the World (2000).cbr
- `    8 MB`  Warren Ellis/Planetary/Planetary & Authority Ruling The World.cbz

### science dog — #01  — identical size  *(special)*

- `   24 MB`  Robert Kirkman/Invincible (Kirkman)/Extras/Science Dog/Science Dog Special 01 (2010) (digital) (Minutemen-InnerDemons).cbr
- `   24 MB`  Image comics/Science Dog Special (001-002)(2010)/Science Dog Special 01 (2010) (digital) (Minutemen-InnerDemons).cbr

### locke & key free comic book day edition  — identical size  *(issue)*

- `   24 MB`  Locke & Key/Locke & Key - Extras/Locke & Key - Free Comic Book Day Edition (2011).cbz
- `   24 MB`  Locke & Key/Locke & Key - Extras/Locke & Key - Free Comic Book Day Edition (2011) (Minutemen).cbz

### promethea — #032  — identical size  *(issue)*

- `   24 MB`  Alan Moore/Alan Moore Essentials/Alan Moore 2005- Promethea/Promethea #032.cbr
- `   24 MB`  Alan Moore/Alan Moore Collection IV-  America's Best Comics/Promethea/Promethea/Promethea #032.cbr

### judge dredd chief judge's man  — identical size  *(issue)*

- `   24 MB`  Judge Dredd - Collections/Judge Dredd - The Chief Judge's Man (2006) (digital) (JeffAlbertson-DCP)/Judge Dredd - The Chief Judge's Man (2006) (digital) (JeffAlbertson-DCP).cbz
- `   24 MB`  2000AD - Collections /Judge Dredd/Judge Dredd - The Chief Judge's Man (2006) (2000AD) (digital) (JeffAlbertson-DCP).cbz

### 298 mean machine travels with muh shrink  — identical size  *(issue)*

- `   24 MB`  Judge Dredd The Megazine/Judge Dredd Megazine v5 (201-400)(2002-ongoing)/J.D Megazine Supplements/298 - Mean Machine - Travels with Muh Shrink.cbr
- `   24 MB`  Judge Dredd The Megazine/J.D Megazine Supplements/298 - Mean Machine - Travels with Muh Shrink.cbr

### peculia and groon grove vampires  — identical size  *(issue)*

- `   24 MB`  Richard Sala/Peculia and the Groon Grove Vampires (April 2005) [Pyramid].cbz
- `   24 MB`  Richard Sala/Evil Eye/Peculia and the Groon Grove Vampires (April 2005) [Pyramid].cbz

### amazing spider man — v2 — #673  — identical size  *(volume)*

- `   23 MB`  Alias  ( Jessica Jones , The Pulse & Appearances)/Appearances/Spider Island/Amazing Spider-Man v2 673 (2012) (Minutemen-DTs).cbz
- `   23 MB`  Alias  ( Jessica Jones , The Pulse & Appearances)/Appearances/Amazing Spider-man/Amazing Spider-Man v2 673 (2012) (Minutemen-DTs).cbz

### 214 2000ad gold — #014  — identical size  *(issue)*

- `   23 MB`  Judge Dredd The Megazine/Judge Dredd Megazine v5 (201-400)(2002-ongoing)/J.D Megazine Supplements/214 - 2000AD Gold 014 - Strontium Dog.cbr
- `   23 MB`  Judge Dredd The Megazine/J.D Megazine Supplements/214 - 2000AD Gold 014 - Strontium Dog.cbr

### 297 judge dredd raptaur  — identical size  *(issue)*

- `   23 MB`  Judge Dredd The Megazine/Judge Dredd Megazine v5 (201-400)(2002-ongoing)/J.D Megazine Supplements/297 - Judge Dredd - Raptaur.cbr
- `   23 MB`  Judge Dredd The Megazine/J.D Megazine Supplements/297 - Judge Dredd - Raptaur.cbr

### 317 tor cyan world of hurt  — identical size  *(issue)*

- `   23 MB`  Judge Dredd The Megazine/Judge Dredd Megazine v5 (201-400)(2002-ongoing)/J.D Megazine Supplements/317 - Tor Cyan - World of Hurt.cbr
- `   23 MB`  Judge Dredd The Megazine/J.D Megazine Supplements/317 - Tor Cyan - World of Hurt.cbr

### judge dredd mega screemer  — identical size  *(issue)*

- `   23 MB`  2000AD prog/2000AD Yearbooks & Specials (1977 - 2013)/Judge Dredd (Specials, Poster Progs & Extras) (-JJ-)/Judge Dredd Mega-Special (1991) [#4] SCREEMER.cbr
- `   23 MB`  2000AD prog/2000AD (Specials, Annuals & Poster Progs + Extras)/2000AD Yearbooks & Specials (1977 - 2013)/Judge Dredd (Specials, Poster Progs & Extras) (-JJ-)/Judge Dredd Mega-Special (1991) [#4] SCREEMER.cbr

### 316 mercy heights  — identical size  *(issue)*

- `   23 MB`  Judge Dredd The Megazine/Judge Dredd Megazine v5 (201-400)(2002-ongoing)/J.D Megazine Supplements/316 - Mercy Heights (Book 4).cbr
- `   23 MB`  Judge Dredd The Megazine/J.D Megazine Supplements/316 - Mercy Heights (Book 4).cbr

### judge dredd satan's island  — identical size  *(issue)*

- `   23 MB`  Judge Dredd - Collections/Judge Dredd - Satan's Island (2006) (digital) (JeffAlbertson-DCP)/Judge Dredd - Satan's Island (2006) (digital) (JeffAlbertson-DCP).cbz
- `   23 MB`  2000AD - Collections /Judge Dredd/Judge Dredd - Satan's Island (2006) (2000AD) (digital) (JeffAlbertson-DCP).cbz

### lobo paramilitary christmas  — identical size  *(special)*

- `   23 MB`  Warren Ellis/The Authority/specials/Authority vs Lobo/The Lobo Paramilitary Christmas Special (1991).cbr
- `   23 MB`  The Authority/specials/Authority vs Lobo/The Lobo Paramilitary Christmas Special (1991).cbr

### heavy metal — v11 — #03  — identical size  *(volume)*

- `   23 MB`  Heavy Metal/Heavy Metal Vols 01-35 (1977-2012)/Heavy Metal v11 03 (1987) (c2c) (fixed) (CalexicoCA).cbr
- `   23 MB`  Heavy Metal/01. Main Series/Heavy Metal v11 03 (1987) (c2c) (fixed) (CalexicoCA).cbr

### alias red band — #05  — identical size  *(issue)*

- `   23 MB`  Alias Red Band 05 (2026) (c2c) (Ori-DCP).cbr
- `   23 MB`  Alias  ( Jessica Jones , The Pulse & Appearances)/Alias Red Band 05 (2026) (c2c) (Ori-DCP).cbr

### neonomicon — #003  — identical size  *(issue)*

- `   22 MB`  Alan Moore/Alan Moore Essentials/Alan Moore 2010- Neonomicon/Neonomicon #003.cbr
- `   22 MB`  Alan Moore/Alan Moore Collection V- More Moore/Neonomicon/Neonomicon #003.cbr

### doktor sleepless — #13  — identical size  *(issue)*

- `   22 MB`  Warren Ellis/Warren Ellis - Doktor Sleepless/Doktor Sleepless #13.cbr
- `   22 MB`  Warren Ellis/2007/2007 Doktor Sleepless/Doktor Sleepless #13.cbr

### authority scorched earth  — identical size  *(issue)*

- `   15 MB`  Warren Ellis/The Authority/specials/The Authority - Scorched Earth (2003).cbr
- `   15 MB`  The Authority/specials/The Authority - Scorched Earth (2003).cbr
- `   15 MB`  The Authority/The Authority - Scorched Earth.cbr

### new avengers — #030  *(issue)*

- `   33 MB`  Alias  ( Jessica Jones , The Pulse & Appearances)/Appearances/New Avengers (2010)/New Avengers 030 (2012) (Minutemen-Meganubis).cbr
- `   11 MB`  Alias  ( Jessica Jones , The Pulse & Appearances)/Appearances/Avengers (2005)/New Avengers 030 (2007) (Kryptonia-DCP).cbr

### swamp thing — #002  — identical size  *(annual)*

- `   22 MB`  Alan Moore/Alan Moore Essentials/Alan Moore 1987- The Saga Of The Swamp Thing/Swamp Thing- Annual #002.cbz
- `   22 MB`  Alan Moore/Alan Moore Collection II-  DC/Swamp Thing/The Saga Of The Swamp Thing/Swamp Thing- Annual #002.cbz

### neonomicon — #001  — identical size  *(issue)*

- `   22 MB`  Alan Moore/Alan Moore Essentials/Alan Moore 2010- Neonomicon/Neonomicon #001.cbr
- `   22 MB`  Alan Moore/Alan Moore Collection V- More Moore/Neonomicon/Neonomicon #001.cbr

### authority vs lobo.#1.jingle hell  — identical size  *(issue)*

- `   22 MB`  Warren Ellis/The Authority/specials/Authority vs Lobo/The Authority vs Lobo.#1.Jingle Hell (2004).cbr
- `   22 MB`  The Authority/specials/Authority vs Lobo/The Authority vs Lobo.#1.Jingle Hell (2004).cbr

### heroes for hire — #04  *(issue)*

- `   24 MB`  Alias  ( Jessica Jones , The Pulse & Appearances)/Appearances/Heroes for Hire v3/Heroes for Hire 04 (2011) (two covers) (Minutemen-Sha-Hic!).cbz
- `   19 MB`  Alias  ( Jessica Jones , The Pulse & Appearances)/Appearances/Heroes for Hire v3/Heroes for Hire 04 (2011) (Minutemen-DarthScanner).cbr

### deadpool pulp — #04  — identical size  *(issue)*

- `   21 MB`  GG Studio (Collection) (2010-2012)/Marvel Noir (2009-2011)(digital)/Deadpool Pulp (001-004)(2010-2011)(digital)(Minutemen-PhD)/Deadpool Pulp 04 (of 04) (2011) (digital) (Minutemen-PhD).cbr
- `   21 MB`  Aster Blistok/Le Vagabond des Limbes/Deadpool Pulp (001-004)(2010-2011)(digital)(Minutemen-PhD)/Deadpool Pulp 04 (of 04) (2011) (digital) (Minutemen-PhD).cbr

### superman whatever happened to man of tomorrow  — identical size  *(issue)*

- `   21 MB`  Alan Moore/Superman - Whatever Happened To The Man of Tomorrow.cbr
- `   21 MB`  Alan Moore/Alan Moore Collection II-  DC/Superman/Whatever Happened To The Man Of Tomorrow/Collection/Superman- Whatever Happened To The Man Of Tomorrow.cbr

### dynamo sins of father — #05  *(issue)*

- `   27 MB`  Image comics/Dynamo 5 Sins of the Father (001-005)(2010)/Dynamo 5 - Sins of the Father 05 (2010) (Harkonnen-DCP).cbz
- `   15 MB`  Robert Kirkman/Invincible (Kirkman)/Extras/Dynamo 5/Dynamo 5 - Sins of the Father 05 (of 05) (2010) (Digital) (Li'l DR & Quinch-Empire).cbr

### heroes for hire — #03  *(issue)*

- `   23 MB`  Alias  ( Jessica Jones , The Pulse & Appearances)/Appearances/Heroes for Hire v3/Heroes for Hire 03 (2011) (two covers) (Minutemen-Sha-Hic!).cbz
- `   19 MB`  Alias  ( Jessica Jones , The Pulse & Appearances)/Appearances/Heroes for Hire v3/Heroes for Hire 03 (2011) (Minutemen-DarthScanner).cbr

### paper man  *(issue)*

- `   28 MB`  Milo Manara/Erotica - Singletons - Milo Manara (1986-1999)/The Paper Man (1986) (Pudgy-DCP).cbr
- `   13 MB`  The Paper Man (1986) (Pudgy).cbr

### dynamo sins of father — #03  *(issue)*

- `   26 MB`  Image comics/Dynamo 5 Sins of the Father (001-005)(2010)/Dynamo 5 - Sins of the Father 03 (of 5) (2010) (Harkonnen-DCP).cbz
- `   15 MB`  Robert Kirkman/Invincible (Kirkman)/Extras/Dynamo 5/Dynamo 5 - Sins of the Father 03 (of 05) (2010) (Digital) (Li'l DR & Quinch-Empire).cbr

### 299 brit cit babes  — identical size  *(issue)*

- `   21 MB`  Judge Dredd The Megazine/Judge Dredd Megazine v5 (201-400)(2002-ongoing)/J.D Megazine Supplements/299 - Brit-Cit Babes.cbr
- `   21 MB`  Judge Dredd The Megazine/J.D Megazine Supplements/299 - Brit-Cit Babes.cbr

### fiends of eastern front v2a stalingrad  — identical size  *(issue)*

- `   21 MB`  Fiends of the Eastern Front/Fiends of the Eastern Front V2a Stalingrad.cbz
- `   21 MB`  2000AD - Collections /Fiends of the Eastern Front/Fiends of the Eastern Front V2a Stalingrad.cbz

### neonomicon — #004  — identical size  *(issue)*

- `   20 MB`  Alan Moore/Alan Moore Essentials/Alan Moore 2010- Neonomicon/Neonomicon #004.cbr
- `   20 MB`  Alan Moore/Alan Moore Collection V- More Moore/Neonomicon/Neonomicon #004.cbr

### xover batman vs dredd die laughing  *(issue)*

- `   23 MB`  2000AD prog/2000AD (Specials, Annuals & Poster Progs + Extras)/2000AD Yearbooks & Specials (1977 - 2013)/Judge Dredd (Specials, Poster Progs & Extras) (-JJ-)/Xover_Batman vs Dredd (1999) - Die Laughing (part_2).cbr
- `   18 MB`  2000AD prog/2000AD (Specials, Annuals & Poster Progs + Extras)/2000AD Yearbooks & Specials (1977 - 2013)/Judge Dredd (Specials, Poster Progs & Extras) (-JJ-)/Xover_Batman vs Dredd (1998) - Die Laughing (part_1).cbr

### 294 breathing space  — identical size  *(issue)*

- `   20 MB`  Judge Dredd The Megazine/Judge Dredd Megazine v5 (201-400)(2002-ongoing)/J.D Megazine Supplements/294 - Breathing Space.cbr
- `   20 MB`  Judge Dredd The Megazine/J.D Megazine Supplements/294 - Breathing Space.cbr

### authority prime — #5  — identical size  *(issue)*

- `   20 MB`  Warren Ellis/The Authority/v4.5 Prime/The Authority Prime #5.cbr
- `   20 MB`  The Authority/v4.5 Prime/The Authority Prime #5.cbr

### warren ellis supergod — #01  — identical size  *(issue)*

- `   20 MB`  Warren Ellis/WARREN ELLIS - SUPERGOD 01-05/Warren_Ellis__Supergod_01__2009___2_Covers___Minutemen-Mantooth_.cbr
- `   20 MB`  Warren Ellis/2009/2009 Supergod/Warren_Ellis__Supergod_01__2009___2_Covers___Minutemen-Mantooth_.cbr

### dynamo sins of father — #02  *(issue)*

- `   26 MB`  Image comics/Dynamo 5 Sins of the Father (001-005)(2010)/Dynamo 5 - Sins of the Father 02 (of 5) (2010) (Harkonnen-DCP).cbz
- `   14 MB`  Robert Kirkman/Invincible (Kirkman)/Extras/Dynamo 5/Dynamo 5 - Sins of the Father 02 (of 05) (2010) (Digital) (Li'l DR & Quinch-Empire).cbr

### pigs — #03  *(issue)*

- `   28 MB`  Image comics/Pigs (001-008)(2011-2012)/Pigs 03 (2011) (C2C) (Minutemen-ThosTew).cbz
- `   12 MB`  Image comics/Pigs (001-008)(2011-2012)/Pigs 03 (2012) (digital-TheGroup).cbr

### dynamo sins of father — #01  *(issue)*

- `   25 MB`  Image comics/Dynamo 5 Sins of the Father (001-005)(2010)/Dynamo 5 - Sins of the Father 01 (of 5) (2010) (Harkonnen-DCP).cbz
- `   15 MB`  Robert Kirkman/Invincible (Kirkman)/Extras/Dynamo 5/Dynamo 5 - Sins of the Father 01 (of 05) (2010) (Digital) (Li'l DR & Quinch-Empire).cbr

### dynamo sins of father — #04  *(issue)*

- `   25 MB`  Image comics/Dynamo 5 Sins of the Father (001-005)(2010)/Dynamo 5 - Sins of the Father 04 (of 5) (2010) (Harkonnen-DCP).cbz
- `   15 MB`  Robert Kirkman/Invincible (Kirkman)/Extras/Dynamo 5/Dynamo 5 - Sins of the Father 04 (of 05) (2010) (Digital) (Li'l DR & Quinch-Empire).cbr

### wildstorm winter  — identical size  *(special)*

- `   20 MB`  Warren Ellis/The Authority/specials/Wildstorm Winter Special 2005.cbr
- `   20 MB`  The Authority/specials/Wildstorm Winter Special 2005.cbr

### blackhand ironhead — #003  — identical size  *(issue)*

- `   20 MB`  Blackhand Ironhead #1 - 5 (2017-2018)/Blackhand Ironhead 001-004 (2017-2018)/Blackhand Ironhead 003 (2018) (digital) (panelsyndicate.com).cbr
- `   20 MB`  Aster Blistok/Le Vagabond des Limbes/Blackhand Ironhead 001-004 (2017-2018)/Blackhand Ironhead 003 (2018) (digital) (panelsyndicate.com).cbr

### tom strong's terrific tales — #003  — identical size  *(issue)*

- `   19 MB`  Alan Moore/Alan Moore Essentials/Alan Moore 2006- Tom Strong/Tom Strong's Teriffic Tales/Tom Strong's Terrific Tales #003.cbz
- `   19 MB`  Alan Moore/Alan Moore Collection IV-  America's Best Comics/Tom Strong/Tom Strong's Teriffic Tales/Tom Strong's Terrific Tales #003.cbz

### authority prime — #3  — identical size  *(issue)*

- `   19 MB`  Warren Ellis/The Authority/v4.5 Prime/The Authority Prime #3.cbr
- `   19 MB`  The Authority/v4.5 Prime/The Authority Prime #3.cbr

### 2000ad prog — #0001  *(issue)*

- `   24 MB`  2000AD prog/2000AD prog 0001 (Ashkelon)(cleaned).cbr
- `   13 MB`  2000AD prog/2000AD prog 0001.cbz

### warren ellis supergod — #02  — identical size  *(issue)*

- `   18 MB`  Warren Ellis/WARREN ELLIS - SUPERGOD 01-05/Warren_Ellis__Supergod_02__2009___2_Covers___Minutemen-Mantooth_.cbr
- `   18 MB`  Warren Ellis/2009/2009 Supergod/Warren_Ellis__Supergod_02__2009___2_Covers___Minutemen-Mantooth_.cbr

### planetary batman night on earth  *(issue)*

- `   18 MB`  Warren Ellis/Planetary/Planetary - Batman - Night on Earth.cbr
- `   18 MB`  Warren Ellis/1999/1999 Planetary/Specials/Planetary - Batman - Night on Earth.cbr

### darkness — #086  *(issue)*

- `   21 MB`  Garth Ennis Collection/The Darkness/The Darkness Volume 3/The Darkness 086 (2010) (Minutemen-The Unresurrected).cbr
- `   16 MB`  Garth Ennis Collection/The Darkness/The Darkness Volume 3/The Darkness 086 (2010) (c2c) (HW-DCP).cbr

### fell — #08  *(issue)*

- `   23 MB`  Warren Ellis/Fell/Fell 08 (2007) (c2c) (theProletariat-DCP).cbr
- `   13 MB`  Warren Ellis/2005/2005 Fell/Fell #08.cbr

### midnighter — #11  — identical size  *(issue)*

- `   18 MB`  Warren Ellis/The Authority/Midnighter/Midnighter 11.cbr
- `   18 MB`  The Authority/Midnighter/Midnighter 11.cbr

### realworlds — #1  — identical size  *(issue)*

- `   18 MB`  Realworlds/Realworlds 1 - Batman.cbr
- `   18 MB`  Batman/Realworlds 1 - Batman.cbr

### new avengers — #034  *(issue)*

- `   25 MB`  Alias  ( Jessica Jones , The Pulse & Appearances)/Appearances/New Avengers (2010)/New Avengers 034 (FINAL) (2013) (Zone-Empire).cbr
- `   10 MB`  Alias  ( Jessica Jones , The Pulse & Appearances)/Appearances/Avengers (2005)/New Avengers 034 (2007) (Kryptonia-DCP).cbr

### warren ellis supergod — #03  — identical size  *(issue)*

- `   18 MB`  Warren Ellis/WARREN ELLIS - SUPERGOD 01-05/Warren_Ellis__Supergod_03__2010___2_Covers___Minutemen-Mantooth_.cbr
- `   18 MB`  Warren Ellis/2009/2009 Supergod/Warren_Ellis__Supergod_03__2010___2_Covers___Minutemen-Mantooth_.cbr

### midnighter — #13  — identical size  *(issue)*

- `   18 MB`  Warren Ellis/The Authority/Midnighter/Midnighter 13.cbr
- `   18 MB`  The Authority/Midnighter/Midnighter 13.cbr

### heavy metal lorna and her robot  — identical size  *(issue)*

- `   18 MB`  Heavy Metal/Related_Publications/Heavy_Metal-Lorna and her robot (pular).cbr
- `   18 MB`  Heavy Metal/Lorna (Heavy Metal) cbr/Heavy Metal-Lorna and her robot.cbr

### authority prime — #2  — identical size  *(issue)*

- `   18 MB`  Warren Ellis/The Authority/v4.5 Prime/The Authority Prime #2.cbr
- `   18 MB`  The Authority/v4.5 Prime/The Authority Prime #2.cbr

### new avengers — #003  *(issue)*

- `   26 MB`  Alias  ( Jessica Jones , The Pulse & Appearances)/Appearances/New Avengers (2010)/New Avengers 003 (2010) (three covers) (Minutemen-Twiztid&Saxon).cbr
- `    9 MB`  Alias  ( Jessica Jones , The Pulse & Appearances)/Appearances/Avengers (2005)/New Avengers 003 (2005) (Team-DCP).cbr

### lobster johnson prayer of neferu  — identical size  *(issue)*

- `   18 MB`  Hellboy/Lobster Johnson/Lobster Johnson - The Prayer of Neferu (2012) (digital-Empire).cbr
- `   18 MB`  Hellboy/15.)  Lobster Johnson - The Prayer of Neferu  (1933 AD)/Lobster Johnson - The Prayer of Neferu.cbr

### midnighter — #09  — identical size  *(issue)*

- `   17 MB`  Warren Ellis/The Authority/Midnighter/Midnighter 09.cbr
- `   17 MB`  The Authority/Midnighter/Midnighter 09.cbr

### tom strong's terrific tales — #009  — identical size  *(issue)*

- `   17 MB`  Alan Moore/Alan Moore Essentials/Alan Moore 2006- Tom Strong/Tom Strong's Teriffic Tales/Tom Strong's Terrific Tales #009.cbr
- `   17 MB`  Alan Moore/Alan Moore Collection IV-  America's Best Comics/Tom Strong/Tom Strong's Teriffic Tales/Tom Strong's Terrific Tales #009.cbr

### v for vendetta — #002  — identical size  *(issue)*

- `   17 MB`  Alan Moore/Alan Moore Essentials/Alan Moore 1985- V For Vendetta/V for Vendetta #002.cbr
- `   17 MB`  Alan Moore/Alan Moore Collection II-  DC/V For Vendetta/V For Vendetta/V for Vendetta #002.cbr

### heavy metal lorna mouse club  *(issue)*

- `   17 MB`  Heavy Metal/Related_Publications/Heavy_Metal-Lorna Mouse Club.cbr
- `   17 MB`  Heavy Metal/Lorna (Heavy Metal) cbr/Heavy Metal-Lorna-Mouse Club.cbr

### v for vendetta — #005  — identical size  *(issue)*

- `   17 MB`  Alan Moore/Alan Moore Essentials/Alan Moore 1985- V For Vendetta/V for Vendetta #005.cbr
- `   17 MB`  Alan Moore/Alan Moore Collection II-  DC/V For Vendetta/V For Vendetta/V for Vendetta #005.cbr

### fell — #06  *(issue)*

- `   22 MB`  Warren Ellis/Fell/Fell 06 (2006) (c2c) (theProletariat-DCP).cbr
- `   12 MB`  Warren Ellis/2005/2005 Fell/Fell #06.cbr

### man called kev — #4  — identical size  *(issue)*

- `   17 MB`  Warren Ellis/The Authority/Kev/A Man Called Kev #4.cbz
- `   17 MB`  The Authority/Kev/A Man Called Kev #4.cbz

### authority — v1 — #29  — identical size  *(volume)*

- `   17 MB`  Warren Ellis/The Authority/v1 (1999)/The Authority v1 #29.cbr
- `   17 MB`  The Authority/v1 (1999)/The Authority v1 #29.cbr

### doktor sleepless — #12  — identical size  *(issue)*

- `   17 MB`  Warren Ellis/Warren Ellis - Doktor Sleepless/Doktor Sleepless #12.cbr
- `   17 MB`  Warren Ellis/2007/2007 Doktor Sleepless/Doktor Sleepless #12.cbr

### tom strong's terrific tales — #012  — identical size  *(issue)*

- `   17 MB`  Alan Moore/Alan Moore Essentials/Alan Moore 2006- Tom Strong/Tom Strong's Teriffic Tales/Tom Strong's Terrific Tales #012.cbr
- `   17 MB`  Alan Moore/Alan Moore Collection IV-  America's Best Comics/Tom Strong/Tom Strong's Teriffic Tales/Tom Strong's Terrific Tales #012.cbr

### new avengers — #015  *(issue)*

- `   20 MB`  Alias  ( Jessica Jones , The Pulse & Appearances)/Appearances/New Avengers (2010)/New Avengers 015 (2011) (Minutemen-DarthSax).cbr
- `   13 MB`  Alias  ( Jessica Jones , The Pulse & Appearances)/Appearances/Avengers (2005)/New Avengers 015 (2006) (RIP-ODB).cbr

### lobster johnson caput mortuum  — identical size  *(issue)*

- `   17 MB`  Hellboy/Lobster Johnson/Lobster Johnson - Caput Mortuum (2012) (2 covers) (digital-Empire).cbr
- `   17 MB`  Hellboy/11.)  Lobster Johnson - Caput Mortuum  (1932 AD)/Lobster Johnson - Caput Mortuum.cbr

### blackhand ironhead — #004  — identical size  *(issue)*

- `   16 MB`  Blackhand Ironhead #1 - 5 (2017-2018)/Blackhand Ironhead 001-004 (2017-2018)/Blackhand Ironhead 004 (2018) (digital) (panelsyndicate.com).cbr
- `   16 MB`  Aster Blistok/Le Vagabond des Limbes/Blackhand Ironhead 001-004 (2017-2018)/Blackhand Ironhead 004 (2018) (digital) (panelsyndicate.com).cbr

### 284 deadlock return to termight  — identical size  *(issue)*

- `   16 MB`  Judge Dredd The Megazine/Judge Dredd Megazine v5 (201-400)(2002-ongoing)/J.D Megazine Supplements/284 - Deadlock - Return To Termight.cbr
- `   16 MB`  Judge Dredd The Megazine/J.D Megazine Supplements/284 - Deadlock - Return To Termight.cbr

### fell — #01  *(issue)*

- `   23 MB`  Warren Ellis/Fell/Fell 01 (2005) (c2c) (theProletariat-DCP).cbr
- `    9 MB`  Warren Ellis/2005/2005 Fell/Fell #01.cbr

### v for vendetta — #006  — identical size  *(issue)*

- `   16 MB`  Alan Moore/Alan Moore Essentials/Alan Moore 1985- V For Vendetta/V for Vendetta #006.cbr
- `   16 MB`  Alan Moore/Alan Moore Collection II-  DC/V For Vendetta/V For Vendetta/V for Vendetta #006.cbr

### midnighter — #02  *(issue)*

- `   11 MB`  Warren Ellis/The Authority/Midnighter/Midnighter 02.cbr
- `   11 MB`  The Authority/Midnighter/Midnighter 02.cbr
- `   11 MB`  Garth Ennis Collection/Midnighter/Midnighter 02.cbr

### midnighter — #12  — identical size  *(issue)*

- `   16 MB`  Warren Ellis/The Authority/Midnighter/Midnighter 12.cbr
- `   16 MB`  The Authority/Midnighter/Midnighter 12.cbr

### blackhand ironhead — #002  — identical size  *(issue)*

- `   16 MB`  Blackhand Ironhead #1 - 5 (2017-2018)/Blackhand Ironhead 001-004 (2017-2018)/Blackhand Ironhead 002 (2018) (digital) (panelsyndicate.com).cbr
- `   16 MB`  Aster Blistok/Le Vagabond des Limbes/Blackhand Ironhead 001-004 (2017-2018)/Blackhand Ironhead 002 (2018) (digital) (panelsyndicate.com).cbr

### saga of swamp thing — #053  — identical size  *(issue)*

- `   16 MB`  Alan Moore/Alan Moore Essentials/Alan Moore 1987- The Saga Of The Swamp Thing/Saga of the Swamp Thing #053.cbr
- `   16 MB`  Alan Moore/Alan Moore Collection II-  DC/Swamp Thing/The Saga Of The Swamp Thing/Saga of the Swamp Thing #053.cbr

### tom strong's terrific tales — #001  — identical size  *(issue)*

- `   16 MB`  Alan Moore/Alan Moore Essentials/Alan Moore 2006- Tom Strong/Tom Strong's Teriffic Tales/Tom Strong's Terrific Tales #001.cbr
- `   16 MB`  Alan Moore/Alan Moore Collection IV-  America's Best Comics/Tom Strong/Tom Strong's Teriffic Tales/Tom Strong's Terrific Tales #001.cbr

### fell — #03  *(issue)*

- `   22 MB`  Warren Ellis/Fell/Fell 03 (2005) (c2c) (theProletariat-DCP).cbr
- `    9 MB`  Warren Ellis/2005/2005 Fell/Fell #03.cbr

### wildstorm armageddon.#3.wetworks  — identical size  *(issue)*

- `   16 MB`  Warren Ellis/The Authority/v4.91 Wildstorm Armageddon/Wildstorm Armageddon.#3.Wetworks.cbr
- `   16 MB`  The Authority/v4.91 Wildstorm Armageddon/Wildstorm Armageddon.#3.Wetworks.cbr

### midnighter — #03  — identical size  *(issue)*

- `   10 MB`  Warren Ellis/The Authority/Midnighter/Midnighter 03.cbr
- `   10 MB`  The Authority/Midnighter/Midnighter 03.cbr
- `   10 MB`  Garth Ennis Collection/Midnighter/Midnighter 03.cbr

### fell — #09  *(issue)*

- `   21 MB`  Warren Ellis/Fell/Fell 09 (2008) (c2c) (theProletariat-DCP).cbr
- `   11 MB`  Warren Ellis/2005/2005 Fell/Fell #09.cbr

### secret history of authority hawksmoor — #3  — identical size  *(issue)*

- `   16 MB`  Warren Ellis/The Authority/specials/Secret History/Secret History of the Authority - Hawksmoor #3.cbr
- `   16 MB`  The Authority/specials/Secret History/Secret History of the Authority - Hawksmoor #3.cbr

### man called kev — #5  — identical size  *(issue)*

- `   16 MB`  Warren Ellis/The Authority/Kev/A Man Called Kev #5.cbz
- `   16 MB`  The Authority/Kev/A Man Called Kev #5.cbz

### midnighter — #08  — identical size  *(issue)*

- `   16 MB`  Warren Ellis/The Authority/Midnighter/Midnighter 08.cbr
- `   16 MB`  The Authority/Midnighter/Midnighter 08.cbr

### saga of swamp thing — #050  — identical size  *(issue)*

- `   16 MB`  Alan Moore/Alan Moore Essentials/Alan Moore 1987- The Saga Of The Swamp Thing/Saga of the Swamp Thing #050.cbr
- `   16 MB`  Alan Moore/Alan Moore Collection II-  DC/Swamp Thing/The Saga Of The Swamp Thing/Saga of the Swamp Thing #050.cbr

### doktor sleepless — #10  *(issue)*

- `   20 MB`  Warren Ellis/2007/2007 Doktor Sleepless/Doktor Sleepless #10.cbr
- `   11 MB`  Warren Ellis/Warren Ellis - Doktor Sleepless/doktor sleepless - #10.cbr

### midnighter — #10  — identical size  *(issue)*

- `   15 MB`  Warren Ellis/The Authority/Midnighter/Midnighter 10.cbr
- `   15 MB`  The Authority/Midnighter/Midnighter 10.cbr

### city of silence — #01  *(issue)*

- `   15 MB`  Warren Ellis/Warren Ellis - City Of Silence/City of Silence #01.cbr
- `   15 MB`  Warren Ellis/2000/City of Silence/City Of Silence 01.cbr

### authority prime — #4  — identical size  *(issue)*

- `   15 MB`  Warren Ellis/The Authority/v4.5 Prime/The Authority Prime #4.cbr
- `   15 MB`  The Authority/v4.5 Prime/The Authority Prime #4.cbr

### v for vendetta — #001  — identical size  *(issue)*

- `   15 MB`  Alan Moore/Alan Moore Essentials/Alan Moore 1985- V For Vendetta/V for Vendetta #001.cbr
- `   15 MB`  Alan Moore/Alan Moore Collection II-  DC/V For Vendetta/V For Vendetta/V for Vendetta #001.cbr

### fell — #05  *(issue)*

- `   22 MB`  Warren Ellis/Fell/Fell 05 (2006) (c2c) (theProletariat-DCP).cbr
- `    8 MB`  Warren Ellis/2005/2005 Fell/Fell #05.cbr

### korto malteze zeleni kontinent — #1  — identical size  *(issue)*

- `   15 MB`  YU stripovi 2019/Korto (YU)/Korto Malteze - Zeleni kontinent 1 - Cudotvorne gljive SA33.cbr
- `   15 MB`  Corto Maltese/Korto Malteze - Zeleni kontinent 1 - Cudotvorne gljive SA33.cbr

### tom strong's terrific tales — #010  — identical size  *(issue)*

- `   15 MB`  Alan Moore/Alan Moore Essentials/Alan Moore 2006- Tom Strong/Tom Strong's Teriffic Tales/Tom Strong's Terrific Tales #010.cbr
- `   15 MB`  Alan Moore/Alan Moore Collection IV-  America's Best Comics/Tom Strong/Tom Strong's Teriffic Tales/Tom Strong's Terrific Tales #010.cbr

### tom strong — #031  — identical size  *(issue)*

- `   15 MB`  Alan Moore/Alan Moore Essentials/Alan Moore 2006- Tom Strong/Tom Strong/Tom Strong #031.cbr
- `   15 MB`  Alan Moore/Alan Moore Collection IV-  America's Best Comics/Tom Strong/Tom Strong/Tom Strong #031.cbr

### monster pile up — #01  — identical size  *(issue)*

- `   15 MB`  Robert Kirkman/Invincible (Kirkman)/Extras/Monster Pile-Up 01 (2008) (Minutemen-ReZone).cbr
- `   15 MB`  Monster Pile-Up 01 (2008) (Minutemen-ReZone).cbr

### v for vendetta — #009  — identical size  *(issue)*

- `   15 MB`  Alan Moore/Alan Moore Essentials/Alan Moore 1985- V For Vendetta/V for Vendetta #009.cbr
- `   15 MB`  Alan Moore/Alan Moore Collection II-  DC/V For Vendetta/V For Vendetta/V for Vendetta #009.cbr

### midnighter — #04  — identical size  *(issue)*

- `   10 MB`  Warren Ellis/The Authority/Midnighter/Midnighter 04.cbr
- `   10 MB`  The Authority/Midnighter/Midnighter 04.cbr
- `   10 MB`  Garth Ennis Collection/Midnighter/Midnighter 04.cbr

### devil's night — #4  — identical size  *(issue)*

- `   15 MB`  Warren Ellis/The Authority/specials/Devil's Night (2000 Annuals)/Devil's Night #4 - WildStorm - Annual 2000.cbr
- `   15 MB`  The Authority/specials/Devil's Night (2000 Annuals)/Devil's Night #4 - WildStorm - Annual 2000.cbr

### authority — v1 — #23  — identical size  *(volume)*

- `   15 MB`  Warren Ellis/The Authority/v1 (1999)/The Authority v1 #23.cbr
- `   15 MB`  The Authority/v1 (1999)/The Authority v1 #23.cbr

### saga of swamp thing — #056  — identical size  *(issue)*

- `   15 MB`  Alan Moore/Alan Moore Essentials/Alan Moore 1987- The Saga Of The Swamp Thing/Saga of the Swamp Thing #056.cbr
- `   15 MB`  Alan Moore/Alan Moore Collection II-  DC/Swamp Thing/The Saga Of The Swamp Thing/Saga of the Swamp Thing #056.cbr

### pilot season velocity — #01  — identical size  *(issue)*

- `   15 MB`  Velocity (v1-v2+)(1995-2016)/Pilot Season - Velocity 01 (2007) (Whitewolf-DCP).cbr
- `   15 MB`  Image comics/Pilot Season (2010-2011)/Pilot Season - Velocity 01 (2007) (Whitewolf-DCP).cbr

### tom strong — #017  — identical size  *(issue)*

- `   15 MB`  Alan Moore/Alan Moore Essentials/Alan Moore 2006- Tom Strong/Tom Strong/Tom Strong #017.cbz
- `   15 MB`  Alan Moore/Alan Moore Collection IV-  America's Best Comics/Tom Strong/Tom Strong/Tom Strong #017.cbz

### v for vendetta — #010  — identical size  *(issue)*

- `   15 MB`  Alan Moore/Alan Moore Essentials/Alan Moore 1985- V For Vendetta/V for Vendetta #010.cbr
- `   15 MB`  Alan Moore/Alan Moore Collection II-  DC/V For Vendetta/V For Vendetta/V for Vendetta #010.cbr

### saga of swamp thing — #020  — identical size  *(issue)*

- `   15 MB`  Alan Moore/Alan Moore Essentials/Alan Moore 1987- The Saga Of The Swamp Thing/Saga of the Swamp Thing #020.cbr
- `   15 MB`  Alan Moore/Alan Moore Collection II-  DC/Swamp Thing/The Saga Of The Swamp Thing/Saga of the Swamp Thing #020.cbr

### heavy metal presents so beautiful so dangerous  — identical size  *(issue)*

- `   15 MB`  Heavy Metal/Heavy Metal Presents/Heavy Metal Presents - So Beautiful So Dangerous (1978).cbz
- `   15 MB`  Heavy Metal/03. Extras/Heavy Metal Presents - So Beautiful So Dangerous (1978).cbz

### tom strong — #032  — identical size  *(issue)*

- `   15 MB`  Alan Moore/Alan Moore Essentials/Alan Moore 2006- Tom Strong/Tom Strong/Tom Strong #032.cbr
- `   15 MB`  Alan Moore/Alan Moore Collection IV-  America's Best Comics/Tom Strong/Tom Strong/Tom Strong #032.cbr

### midnighter — #05  — identical size  *(issue)*

- `   10 MB`  Warren Ellis/The Authority/Midnighter/Midnighter 05.cbr
- `   10 MB`  The Authority/Midnighter/Midnighter 05.cbr
- `   10 MB`  Garth Ennis Collection/Midnighter/Midnighter 05.cbr

### tom strong — #030  — identical size  *(issue)*

- `   15 MB`  Alan Moore/Alan Moore Essentials/Alan Moore 2006- Tom Strong/Tom Strong/Tom Strong #030.cbr
- `   15 MB`  Alan Moore/Alan Moore Collection IV-  America's Best Comics/Tom Strong/Tom Strong/Tom Strong #030.cbr

### fell — #07  *(issue)*

- `   21 MB`  Warren Ellis/Fell/Fell 07 (2007) (c2c) (theProletariat-DCP).cbr
- `    8 MB`  Warren Ellis/2005/2005 Fell/Fell #07.cbr

### wildstorm revelations — #4  — identical size  *(issue)*

- `   15 MB`  Warren Ellis/The Authority/v4.92 Wildstorm Revelations/Wildstorm Revelations #4.cbr
- `   15 MB`  The Authority/v4.92 Wildstorm Revelations/Wildstorm Revelations #4.cbr

### v for vendetta — #007  — identical size  *(issue)*

- `   15 MB`  Alan Moore/Alan Moore Essentials/Alan Moore 1985- V For Vendetta/V for Vendetta #007.cbr
- `   15 MB`  Alan Moore/Alan Moore Collection II-  DC/V For Vendetta/V For Vendetta/V for Vendetta #007.cbr

### new avengers — #014  *(issue)*

- `   21 MB`  Alias  ( Jessica Jones , The Pulse & Appearances)/Appearances/New Avengers (2010)/New Avengers 014 (2011) (Minutemen-DarthSax).cbr
- `    8 MB`  Alias  ( Jessica Jones , The Pulse & Appearances)/Appearances/Avengers (2005)/New Avengers 014 (2006) (Team-DCP).cbr

### v for vendetta — #004  — identical size  *(issue)*

- `   14 MB`  Alan Moore/Alan Moore Essentials/Alan Moore 1985- V For Vendetta/V for Vendetta #004.cbr
- `   14 MB`  Alan Moore/Alan Moore Collection II-  DC/V For Vendetta/V For Vendetta/V for Vendetta #004.cbr

### doom patrol — v2 — #086  — identical size  *(volume)*

- `   14 MB`  Ted McKeever (Collection) (1987-2007)/1994 - Doom Patrol (Vertigo - w Rachael Pollack)/Doom Patrol v2 086 (Imagine Ari's Friend pt 3 - The Cup Of Knowing).cbz
- `   14 MB`  Grant Morrison/Comics/Doom Patrol/Doom Patrol v2 086 (Imagine Ari's Friend pt 3 - The Cup Of Knowing).cbz

### secret history of authority hawksmoor — #5  — identical size  *(issue)*

- `   14 MB`  Warren Ellis/The Authority/specials/Secret History/Secret History of the Authority - Hawksmoor #5.cbr
- `   14 MB`  The Authority/specials/Secret History/Secret History of the Authority - Hawksmoor #5.cbr

### v for vendetta — #008  — identical size  *(issue)*

- `   14 MB`  Alan Moore/Alan Moore Essentials/Alan Moore 1985- V For Vendetta/V for Vendetta #008.cbr
- `   14 MB`  Alan Moore/Alan Moore Collection II-  DC/V For Vendetta/V For Vendetta/V for Vendetta #008.cbr

### authority magnificent kevin — #2  — identical size  *(issue)*

- `   14 MB`  Warren Ellis/The Authority/Kev/The Authority - The Magnificent Kevin #2.cbr
- `   14 MB`  The Authority/Kev/The Authority - The Magnificent Kevin #2.cbr

### number of beast — #2  — identical size  *(issue)*

- `   14 MB`  Warren Ellis/The Authority/v4.93 Number of the Beast/Number of the Beast #2.cbr
- `   14 MB`  The Authority/v4.93 Number of the Beast/Number of the Beast #2.cbr

### wildstorm revelations — #5  — identical size  *(issue)*

- `   14 MB`  Warren Ellis/The Authority/v4.92 Wildstorm Revelations/Wildstorm Revelations #5.cbr
- `   14 MB`  The Authority/v4.92 Wildstorm Revelations/Wildstorm Revelations #5.cbr

### man called kev — #1  — identical size  *(issue)*

- `   14 MB`  Warren Ellis/The Authority/Kev/A Man Called Kev #1.cbr
- `   14 MB`  The Authority/Kev/A Man Called Kev #1.cbr

### new avengers — #033  *(issue)*

- `   18 MB`  Alias  ( Jessica Jones , The Pulse & Appearances)/Appearances/New Avengers (2010)/New Avengers 033 (2013) (Digital) (Zone-Empire).cbr
- `   10 MB`  Alias  ( Jessica Jones , The Pulse & Appearances)/Appearances/Avengers (2005)/New Avengers 033 (2007) (Kryptonia-DCP).cbr

### midnighter — #01  *(issue)*

- `   10 MB`  Warren Ellis/The Authority/Midnighter/Midnighter 01.cbr
- `   10 MB`  The Authority/Midnighter/Midnighter 01.cbr
- `    9 MB`  Garth Ennis Collection/Midnighter/Midnighter 01.cbr

### v for vendetta — #003  — identical size  *(issue)*

- `   14 MB`  Alan Moore/Alan Moore Essentials/Alan Moore 1985- V For Vendetta/V for Vendetta #003.cbr
- `   14 MB`  Alan Moore/Alan Moore Collection II-  DC/V For Vendetta/V For Vendetta/V for Vendetta #003.cbr

### authority prime — #6  — identical size  *(issue)*

- `   14 MB`  Warren Ellis/The Authority/v4.5 Prime/The Authority Prime #6.cbr
- `   14 MB`  The Authority/v4.5 Prime/The Authority Prime #6.cbr

### authority — v1 — #27  — identical size  *(volume)*

- `   14 MB`  Warren Ellis/The Authority/v1 (1999)/The Authority v1 #27.cbr
- `   14 MB`  The Authority/v1 (1999)/The Authority v1 #27.cbr

### authority — v1 — #17  — identical size  *(volume)*

- `   14 MB`  Warren Ellis/The Authority/v1 (1999)/The Authority v1 #17.cbr
- `   14 MB`  The Authority/v1 (1999)/The Authority v1 #17.cbr

### fell — #04  *(issue)*

- `   20 MB`  Warren Ellis/Fell/Fell 04 (2006) (c2c) (theProletariat-DCP).cbr
- `    8 MB`  Warren Ellis/2005/2005 Fell/Fell #04.cbr

### coup d'etat — #5  — identical size  *(issue)*

- `   14 MB`  Warren Ellis/The Authority/v2.5 Coup d'Etat/Coup d'Etat #5 - Afterword.cbr
- `   14 MB`  The Authority/v2.5 Coup d'Etat/Coup d'Etat #5 - Afterword.cbr

### tom strong's terrific tales — #011  — identical size  *(issue)*

- `   14 MB`  Alan Moore/Alan Moore Essentials/Alan Moore 2006- Tom Strong/Tom Strong's Teriffic Tales/Tom Strong's Terrific Tales #011.cbr
- `   14 MB`  Alan Moore/Alan Moore Collection IV-  America's Best Comics/Tom Strong/Tom Strong's Teriffic Tales/Tom Strong's Terrific Tales #011.cbr

### planetary extras all over world  — identical size  *(issue)*

- `   14 MB`  Warren Ellis/Planetary/Planetary TPB Extras All Over The World.cbz
- `   14 MB`  Warren Ellis/1999/1999 Planetary/Planetary TPB Extras All Over The World.cbz

### hellraiser vs nightbreed jihad  *(issue)*

- `   14 MB`  Clive Barker/Extras/Hellraiser/Hellraiser vs Nightbreed - Jihad (2).cbr
- `   13 MB`  Clive Barker/Extras/Hellraiser/Hellraiser vs Nightbreed - Jihad (1).cbr

### man called kev — #3  — identical size  *(issue)*

- `   14 MB`  Warren Ellis/The Authority/Kev/A Man Called Kev #3.cbr
- `   14 MB`  The Authority/Kev/A Man Called Kev #3.cbr

### authority more kev — #3  — identical size  *(issue)*

- `   14 MB`  Warren Ellis/The Authority/Kev/The Authority - More Kev #3.cbr
- `   14 MB`  The Authority/Kev/The Authority - More Kev #3.cbr

### authority — v1 — #18  — identical size  *(volume)*

- `   14 MB`  Warren Ellis/The Authority/v1 (1999)/The Authority v1 #18.cbr
- `   14 MB`  The Authority/v1 (1999)/The Authority v1 #18.cbr

### authority magnificent kevin — #1  — identical size  *(issue)*

- `   13 MB`  Warren Ellis/The Authority/Kev/The Authority - The Magnificent Kevin #1.cbr
- `   13 MB`  The Authority/Kev/The Authority - The Magnificent Kevin #1.cbr

### number of beast — #1  — identical size  *(issue)*

- `   13 MB`  Warren Ellis/The Authority/v4.93 Number of the Beast/Number of the Beast #1.cbr
- `   13 MB`  The Authority/v4.93 Number of the Beast/Number of the Beast #1.cbr

### tom strong's terrific tales — #006  — identical size  *(issue)*

- `   13 MB`  Alan Moore/Alan Moore Essentials/Alan Moore 2006- Tom Strong/Tom Strong's Teriffic Tales/Tom Strong's Terrific Tales #006.cbz
- `   13 MB`  Alan Moore/Alan Moore Collection IV-  America's Best Comics/Tom Strong/Tom Strong's Teriffic Tales/Tom Strong's Terrific Tales #006.cbz

### top ten — #001  — identical size  *(issue)*

- `   13 MB`  Alan Moore/Alan Moore Essentials/Alan Moore 2001- Top Ten/Top Ten #001.cbz
- `   13 MB`  Alan Moore/Alan Moore Collection IV-  America's Best Comics/Top Ten/Top Ten/Top Ten #001.cbz

### devil's night — #3  — identical size  *(issue)*

- `   13 MB`  Warren Ellis/The Authority/specials/Devil's Night (2000 Annuals)/Devil's Night #3 - The Authority - Annual 2000.cbr
- `   13 MB`  The Authority/specials/Devil's Night (2000 Annuals)/Devil's Night #3 - The Authority - Annual 2000.cbr

### wildstorm armageddon.#4.gen13  — identical size  *(issue)*

- `   13 MB`  Warren Ellis/The Authority/v4.91 Wildstorm Armageddon/Wildstorm Armageddon.#4.Gen13.cbr
- `   13 MB`  The Authority/v4.91 Wildstorm Armageddon/Wildstorm Armageddon.#4.Gen13.cbr

### top ten — #12  — identical size  *(issue)*

- `   13 MB`  Top 10/Top Ten 12.cbz
- `   13 MB`  Alan Moore/Top 10/Top Ten 12.cbz

### top ten — #012  — identical size  *(issue)*

- `   13 MB`  Alan Moore/Alan Moore Essentials/Alan Moore 2001- Top Ten/Top Ten #012.cbz
- `   13 MB`  Alan Moore/Alan Moore Collection IV-  America's Best Comics/Top Ten/Top Ten/Top Ten #012.cbz

### authority — v5 — #01  — identical size  *(volume)*

- `   13 MB`  Warren Ellis/The Authority/v5 (2008)/The Authority v5 #01.cbr
- `   13 MB`  The Authority/v5 (2008)/The Authority v5 #01.cbr

### fell — #02  *(issue)*

- `   21 MB`  Warren Ellis/Fell/Fell 02 (2005) (c2c) (theProletariat-DCP).cbr
- `    5 MB`  Warren Ellis/2005/2005 Fell/Fell #02.cbz

### maximortal — #07  — identical size  *(issue)*

- `   13 MB`  Rick Veitch/Maximortal/Maximortal 07.cbr
- `   13 MB`  Maximortal/Maximortal 01-07/Maximortal #07.cbr

### secret history of authority hawksmoor — #4  — identical size  *(issue)*

- `   13 MB`  Warren Ellis/The Authority/specials/Secret History/Secret History of the Authority - Hawksmoor #4.cbr
- `   13 MB`  The Authority/specials/Secret History/Secret History of the Authority - Hawksmoor #4.cbr

### 291 canon fodder dark matter  — identical size  *(issue)*

- `   13 MB`  Judge Dredd The Megazine/Judge Dredd Megazine v5 (201-400)(2002-ongoing)/J.D Megazine Supplements/291 - Canon Fodder - Dark Matter.cbr
- `   13 MB`  Judge Dredd The Megazine/J.D Megazine Supplements/291 - Canon Fodder - Dark Matter.cbr

### coup d'etat — #4  — identical size  *(issue)*

- `   13 MB`  Warren Ellis/The Authority/v2.5 Coup d'Etat/Coup d'Etat #4 - The Authority.cbr
- `   13 MB`  The Authority/v2.5 Coup d'Etat/Coup d'Etat #4 - The Authority.cbr

### coup d'etat — #1  — identical size  *(issue)*

- `   13 MB`  Warren Ellis/The Authority/v2.5 Coup d'Etat/Coup d'Etat #1 - Sleeper.cbr
- `   13 MB`  The Authority/v2.5 Coup d'Etat/Coup d'Etat #1 - Sleeper.cbr

### wildstorm revelations — #3  — identical size  *(issue)*

- `   13 MB`  Warren Ellis/The Authority/v4.92 Wildstorm Revelations/Wildstorm Revelations #3.cbr
- `   13 MB`  The Authority/v4.92 Wildstorm Revelations/Wildstorm Revelations #3.cbr

### desolation jones — #08  *(issue)*

- `   14 MB`  Warren Ellis/2005/2005 Desolation Jones/Desolation Jones #08.cbr
- `   12 MB`  Warren Ellis/Desolation Jones/Desolation Jones 08.cbr

### midnighter — #19  — identical size  *(issue)*

- `   13 MB`  Warren Ellis/The Authority/Midnighter/Midnighter 19.cbr
- `   13 MB`  The Authority/Midnighter/Midnighter 19.cbr

### desolation jones — #03  — identical size  *(issue)*

- `   13 MB`  Warren Ellis/Desolation Jones/Desolation Jones 03.CBr
- `   13 MB`  Warren Ellis/2005/2005 Desolation Jones/Desolation Jones #03.CBr

### wildstorm armageddon.#2.welcome to tranquility  — identical size  *(issue)*

- `   13 MB`  Warren Ellis/The Authority/v4.91 Wildstorm Armageddon/Wildstorm Armageddon.#2.Welcome to Tranquility.cbz
- `   13 MB`  The Authority/v4.91 Wildstorm Armageddon/Wildstorm Armageddon.#2.Welcome to Tranquility.cbz

### number of beast — #7  — identical size  *(issue)*

- `   13 MB`  Warren Ellis/The Authority/v4.93 Number of the Beast/Number of the Beast #7.cbr
- `   13 MB`  The Authority/v4.93 Number of the Beast/Number of the Beast #7.cbr

### authority — v1 — #28  — identical size  *(volume)*

- `   13 MB`  Warren Ellis/The Authority/v1 (1999)/The Authority v1 #28.cbr
- `   13 MB`  The Authority/v1 (1999)/The Authority v1 #28.cbr

### number of beast — #8  — identical size  *(issue)*

- `   13 MB`  Warren Ellis/The Authority/v4.93 Number of the Beast/Number of the Beast #8.cbr
- `   13 MB`  The Authority/v4.93 Number of the Beast/Number of the Beast #8.cbr

### saga of swamp thing — #022  — identical size  *(issue)*

- `   13 MB`  Alan Moore/Alan Moore Essentials/Alan Moore 1987- The Saga Of The Swamp Thing/Saga of the Swamp Thing #022.cbr
- `   13 MB`  Alan Moore/Alan Moore Collection II-  DC/Swamp Thing/The Saga Of The Swamp Thing/Saga of the Swamp Thing #022.cbr

### tom strong's terrific tales — #004  — identical size  *(issue)*

- `   13 MB`  Alan Moore/Alan Moore Essentials/Alan Moore 2006- Tom Strong/Tom Strong's Teriffic Tales/Tom Strong's Terrific Tales #004.cbz
- `   13 MB`  Alan Moore/Alan Moore Collection IV-  America's Best Comics/Tom Strong/Tom Strong's Teriffic Tales/Tom Strong's Terrific Tales #004.cbz

### authority more kev — #2  — identical size  *(issue)*

- `   13 MB`  Warren Ellis/The Authority/Kev/The Authority - More Kev #2.cbr
- `   13 MB`  The Authority/Kev/The Authority - More Kev #2.cbr

### captain atom armageddon — #1  — identical size  *(issue)*

- `   13 MB`  Warren Ellis/The Authority/v3.9 Captain Atom- Armageddon/Captain Atom - Armageddon 1.cbr
- `   13 MB`  The Authority/v3.9 Captain Atom- Armageddon/Captain Atom - Armageddon 1.cbr

### wildstorm revelations — #1  — identical size  *(issue)*

- `   13 MB`  Warren Ellis/The Authority/v4.92 Wildstorm Revelations/Wildstorm Revelations #1.cbr
- `   13 MB`  The Authority/v4.92 Wildstorm Revelations/Wildstorm Revelations #1.cbr

### wildstorm revelations — #2  — identical size  *(issue)*

- `   12 MB`  Warren Ellis/The Authority/v4.92 Wildstorm Revelations/Wildstorm Revelations #2.cbr
- `   12 MB`  The Authority/v4.92 Wildstorm Revelations/Wildstorm Revelations #2.cbr

### authority — v1 — #26  — identical size  *(volume)*

- `   12 MB`  Warren Ellis/The Authority/v1 (1999)/The Authority v1 #26.cbr
- `   12 MB`  The Authority/v1 (1999)/The Authority v1 #26.cbr

### maximortal — #05  — identical size  *(issue)*

- `   12 MB`  Rick Veitch/Maximortal/Maximortal 05.cbr
- `   12 MB`  Maximortal/Maximortal 01-07/Maximortal #05.cbr

### secret history of authority hawksmoor — #1  — identical size  *(issue)*

- `   12 MB`  Warren Ellis/The Authority/specials/Secret History/Secret History of the Authority - Hawksmoor #1.cbr
- `   12 MB`  The Authority/specials/Secret History/Secret History of the Authority - Hawksmoor #1.cbr

### number of beast — #5  — identical size  *(issue)*

- `   12 MB`  Warren Ellis/The Authority/v4.93 Number of the Beast/Number of the Beast #5.cbr
- `   12 MB`  The Authority/v4.93 Number of the Beast/Number of the Beast #5.cbr

### number of beast — #6  — identical size  *(issue)*

- `   12 MB`  Warren Ellis/The Authority/v4.93 Number of the Beast/Number of the Beast #6.cbr
- `   12 MB`  The Authority/v4.93 Number of the Beast/Number of the Beast #6.cbr

### authority — v1 — #14  — identical size  *(volume)*

- `   12 MB`  Warren Ellis/The Authority/v1 (1999)/The Authority v1 #14.cbr
- `   12 MB`  The Authority/v1 (1999)/The Authority v1 #14.cbr

### tom strong's terrific tales — #002  — identical size  *(issue)*

- `   12 MB`  Alan Moore/Alan Moore Essentials/Alan Moore 2006- Tom Strong/Tom Strong's Teriffic Tales/Tom Strong's Terrific Tales #002.cbr
- `   12 MB`  Alan Moore/Alan Moore Collection IV-  America's Best Comics/Tom Strong/Tom Strong's Teriffic Tales/Tom Strong's Terrific Tales #002.cbr

### wildstorm armageddon.#1.midnighter  — identical size  *(issue)*

- `   12 MB`  Warren Ellis/The Authority/v4.91 Wildstorm Armageddon/Wildstorm Armageddon.#1.Midnighter.cbr
- `   12 MB`  The Authority/v4.91 Wildstorm Armageddon/Wildstorm Armageddon.#1.Midnighter.cbr

### authority — v1 — #15  — identical size  *(volume)*

- `   12 MB`  Warren Ellis/The Authority/v1 (1999)/The Authority v1 #15.cbr
- `   12 MB`  The Authority/v1 (1999)/The Authority v1 #15.cbr

### devil's night — #1  — identical size  *(issue)*

- `   12 MB`  Warren Ellis/The Authority/specials/Devil's Night (2000 Annuals)/Devil's Night #1 - Gen 13 - Annual 2000.cbr
- `   12 MB`  The Authority/specials/Devil's Night (2000 Annuals)/Devil's Night #1 - Gen 13 - Annual 2000.cbr

### authority — v2 — #06  — identical size  *(volume)*

- `   12 MB`  Warren Ellis/The Authority/v2 (2003)/The Authority v2 #06.cbr
- `   12 MB`  The Authority/v2 (2003)/The Authority v2 #06.cbr

### 292 rogue trooper war machine — v1  — identical size  *(volume)*

- `   12 MB`  Judge Dredd The Megazine/Judge Dredd Megazine v5 (201-400)(2002-ongoing)/J.D Megazine Supplements/292 - Rogue Trooper - The War Machine Volume 1.cbr
- `   12 MB`  Judge Dredd The Megazine/J.D Megazine Supplements/292 - Rogue Trooper - The War Machine Volume 1.cbr

### tom strong — #029  — identical size  *(issue)*

- `   12 MB`  Alan Moore/Alan Moore Essentials/Alan Moore 2006- Tom Strong/Tom Strong/Tom Strong #029.cbr
- `   12 MB`  Alan Moore/Alan Moore Collection IV-  America's Best Comics/Tom Strong/Tom Strong/Tom Strong #029.cbr

### tom strong — #001  — identical size  *(issue)*

- `   12 MB`  Alan Moore/Alan Moore Essentials/Alan Moore 2006- Tom Strong/Tom Strong/Tom Strong #001.cbr
- `   12 MB`  Alan Moore/Alan Moore Collection IV-  America's Best Comics/Tom Strong/Tom Strong/Tom Strong #001.cbr

### saga of swamp thing — #023  — identical size  *(issue)*

- `   12 MB`  Alan Moore/Alan Moore Essentials/Alan Moore 1987- The Saga Of The Swamp Thing/Saga of the Swamp Thing #023.cbr
- `   12 MB`  Alan Moore/Alan Moore Collection II-  DC/Swamp Thing/The Saga Of The Swamp Thing/Saga of the Swamp Thing #023.cbr

### tom strong — #015  — identical size  *(issue)*

- `   12 MB`  Alan Moore/Alan Moore Essentials/Alan Moore 2006- Tom Strong/Tom Strong/Tom Strong #015.cbz
- `   12 MB`  Alan Moore/Alan Moore Collection IV-  America's Best Comics/Tom Strong/Tom Strong/Tom Strong #015.cbz

### number of beast — #3  — identical size  *(issue)*

- `   12 MB`  Warren Ellis/The Authority/v4.93 Number of the Beast/Number of the Beast #3.cbr
- `   12 MB`  The Authority/v4.93 Number of the Beast/Number of the Beast #3.cbr

### tom strong — #027  — identical size  *(issue)*

- `   12 MB`  Alan Moore/Alan Moore Essentials/Alan Moore 2006- Tom Strong/Tom Strong/Tom Strong #027.cbz
- `   12 MB`  Alan Moore/Alan Moore Collection IV-  America's Best Comics/Tom Strong/Tom Strong/Tom Strong #027.cbz

### top ten — #009  — identical size  *(issue)*

- `   12 MB`  Alan Moore/Alan Moore Essentials/Alan Moore 2001- Top Ten/Top Ten #009.cbr
- `   12 MB`  Alan Moore/Alan Moore Collection IV-  America's Best Comics/Top Ten/Top Ten/Top Ten #009.cbr

### near myths — #4  — identical size  *(issue)*

- `   12 MB`  Grant Morrison/Near Myths (Grant Morrison)/Near Myths #4 - Gideon Stargrave.cbr
- `   12 MB`  Grant Morrison/Comics/Near Myths (Galaxy 1978)/Near Myths #4 - Gideon Stargrave.cbr

### saga of swamp thing — #063  — identical size  *(issue)*

- `   12 MB`  Alan Moore/Alan Moore Essentials/Alan Moore 1987- The Saga Of The Swamp Thing/Saga of the Swamp Thing #063.cbz
- `   12 MB`  Alan Moore/Alan Moore Collection II-  DC/Swamp Thing/The Saga Of The Swamp Thing/Saga of the Swamp Thing #063.cbz

### wildstorm armageddon.#6.wildcats  — identical size  *(issue)*

- `   12 MB`  Warren Ellis/The Authority/v4.91 Wildstorm Armageddon/Wildstorm Armageddon.#6.Wildcats.cbr
- `   12 MB`  The Authority/v4.91 Wildstorm Armageddon/Wildstorm Armageddon.#6.Wildcats.cbr

### authority — v1 — #13  — identical size  *(volume)*

- `   12 MB`  Warren Ellis/The Authority/v1 (1999)/The Authority v1 #13.cbr
- `   12 MB`  The Authority/v1 (1999)/The Authority v1 #13.cbr

### saga of swamp thing — #062  — identical size  *(issue)*

- `   12 MB`  Alan Moore/Alan Moore Essentials/Alan Moore 1987- The Saga Of The Swamp Thing/Saga of the Swamp Thing #062.cbr
- `   12 MB`  Alan Moore/Alan Moore Collection II-  DC/Swamp Thing/The Saga Of The Swamp Thing/Saga of the Swamp Thing #062.cbr

### 293 rogue trooper war machine — v2  — identical size  *(volume)*

- `   12 MB`  Judge Dredd The Megazine/Judge Dredd Megazine v5 (201-400)(2002-ongoing)/J.D Megazine Supplements/293 - Rogue Trooper - The War Machine Volume 2.cbr
- `   12 MB`  Judge Dredd The Megazine/J.D Megazine Supplements/293 - Rogue Trooper - The War Machine Volume 2.cbr

### saga of swamp thing — #064  — identical size  *(issue)*

- `   12 MB`  Alan Moore/Alan Moore Essentials/Alan Moore 1987- The Saga Of The Swamp Thing/Saga of the Swamp Thing #064.cbz
- `   12 MB`  Alan Moore/Alan Moore Collection II-  DC/Swamp Thing/The Saga Of The Swamp Thing/Saga of the Swamp Thing #064.cbz

### midnighter — #07  — identical size  *(issue)*

- `   12 MB`  Warren Ellis/The Authority/Midnighter/Midnighter 07.cbr
- `   12 MB`  The Authority/Midnighter/Midnighter 07.cbr

### 288 harmony blood and snow  — identical size  *(issue)*

- `   12 MB`  Judge Dredd The Megazine/Judge Dredd Megazine v5 (201-400)(2002-ongoing)/J.D Megazine Supplements/288 - Harmony - Blood and Snow.cbr
- `   12 MB`  Judge Dredd The Megazine/J.D Megazine Supplements/288 - Harmony - Blood and Snow.cbr

### number of beast — #4  — identical size  *(issue)*

- `   11 MB`  Warren Ellis/The Authority/v4.93 Number of the Beast/Number of the Beast #4.cbr
- `   11 MB`  The Authority/v4.93 Number of the Beast/Number of the Beast #4.cbr

### authority — v1 — #24  — identical size  *(volume)*

- `   11 MB`  Warren Ellis/The Authority/v1 (1999)/The Authority v1 #24.cbr
- `   11 MB`  The Authority/v1 (1999)/The Authority v1 #24.cbr

### coup d'etat — #2  — identical size  *(issue)*

- `   11 MB`  Warren Ellis/The Authority/v2.5 Coup d'Etat/Coup d'Etat #2 - Stormwatch Team Achilles.cbr
- `   11 MB`  The Authority/v2.5 Coup d'Etat/Coup d'Etat #2 - Stormwatch Team Achilles.cbr

### tom strong — #014  — identical size  *(issue)*

- `   11 MB`  Alan Moore/Alan Moore Essentials/Alan Moore 2006- Tom Strong/Tom Strong/Tom Strong #014.cbz
- `   11 MB`  Alan Moore/Alan Moore Collection IV-  America's Best Comics/Tom Strong/Tom Strong/Tom Strong #014.cbz

### tom strong — #033  — identical size  *(issue)*

- `   11 MB`  Alan Moore/Alan Moore Essentials/Alan Moore 2006- Tom Strong/Tom Strong/Tom Strong #033.cbr
- `   11 MB`  Alan Moore/Alan Moore Collection IV-  America's Best Comics/Tom Strong/Tom Strong/Tom Strong #033.cbr

### saga of swamp thing — #061  — identical size  *(issue)*

- `   11 MB`  Alan Moore/Alan Moore Essentials/Alan Moore 1987- The Saga Of The Swamp Thing/Saga of the Swamp Thing #061.cbr
- `   11 MB`  Alan Moore/Alan Moore Collection II-  DC/Swamp Thing/The Saga Of The Swamp Thing/Saga of the Swamp Thing #061.cbr

### authority — v2 — #07  — identical size  *(volume)*

- `   11 MB`  Warren Ellis/The Authority/v2 (2003)/The Authority v2 #07.cbz
- `   11 MB`  The Authority/v2 (2003)/The Authority v2 #07.cbz

### new avengers — #031  *(issue)*

- `   13 MB`  Alias  ( Jessica Jones , The Pulse & Appearances)/Appearances/New Avengers (2010)/New Avengers 031 (2012) (Digital) (Zone-Empire).cbr
- `   10 MB`  Alias  ( Jessica Jones , The Pulse & Appearances)/Appearances/Avengers (2005)/New Avengers 031 (2007) (Kryptonia-DCP).cbr

### tom strong — #034  — identical size  *(issue)*

- `   11 MB`  Alan Moore/Alan Moore Essentials/Alan Moore 2006- Tom Strong/Tom Strong/Tom Strong #034.cbr
- `   11 MB`  Alan Moore/Alan Moore Collection IV-  America's Best Comics/Tom Strong/Tom Strong/Tom Strong #034.cbr

### saga of swamp thing — #024  — identical size  *(issue)*

- `   11 MB`  Alan Moore/Alan Moore Essentials/Alan Moore 1987- The Saga Of The Swamp Thing/Saga of the Swamp Thing #024.cbr
- `   11 MB`  Alan Moore/Alan Moore Collection II-  DC/Swamp Thing/The Saga Of The Swamp Thing/Saga of the Swamp Thing #024.cbr

### saga of swamp thing — #033  — identical size  *(issue)*

- `   11 MB`  Alan Moore/Alan Moore Essentials/Alan Moore 1987- The Saga Of The Swamp Thing/Saga of the Swamp Thing #033.cbr
- `   11 MB`  Alan Moore/Alan Moore Collection II-  DC/Swamp Thing/The Saga Of The Swamp Thing/Saga of the Swamp Thing #033.cbr

### midnighter — #18  — identical size  *(issue)*

- `   11 MB`  Warren Ellis/The Authority/Midnighter/Midnighter 18.cbr
- `   11 MB`  The Authority/Midnighter/Midnighter 18.cbr

### wildstorm revelations — #6  — identical size  *(issue)*

- `   11 MB`  Warren Ellis/The Authority/v4.92 Wildstorm Revelations/Wildstorm Revelations #6.cbr
- `   11 MB`  The Authority/v4.92 Wildstorm Revelations/Wildstorm Revelations #6.cbr

### saga of swamp thing — #025  — identical size  *(issue)*

- `   11 MB`  Alan Moore/Alan Moore Essentials/Alan Moore 1987- The Saga Of The Swamp Thing/Saga of the Swamp Thing #025.cbr
- `   11 MB`  Alan Moore/Alan Moore Collection II-  DC/Swamp Thing/The Saga Of The Swamp Thing/Saga of the Swamp Thing #025.cbr

### 283 chopper song of surfer — v2  — identical size  *(volume)*

- `   11 MB`  Judge Dredd The Megazine/Judge Dredd Megazine v5 (201-400)(2002-ongoing)/J.D Megazine Supplements/283 - Chopper - Song of the Surfer Volume 2.cbr
- `   11 MB`  Judge Dredd The Megazine/J.D Megazine Supplements/283 - Chopper - Song of the Surfer Volume 2.cbr

### top ten — #10  — identical size  *(issue)*

- `   11 MB`  Top 10/Top Ten 10.cbz
- `   11 MB`  Alan Moore/Top 10/Top Ten 10.cbz

### saga of swamp thing — #028  — identical size  *(issue)*

- `   11 MB`  Alan Moore/Alan Moore Essentials/Alan Moore 1987- The Saga Of The Swamp Thing/Saga of the Swamp Thing #028.cbr
- `   11 MB`  Alan Moore/Alan Moore Collection II-  DC/Swamp Thing/The Saga Of The Swamp Thing/Saga of the Swamp Thing #028.cbr

### top ten — #010  — identical size  *(issue)*

- `   11 MB`  Alan Moore/Alan Moore Essentials/Alan Moore 2001- Top Ten/Top Ten #010.cbr
- `   11 MB`  Alan Moore/Alan Moore Collection IV-  America's Best Comics/Top Ten/Top Ten/Top Ten #010.cbr

### desolation jones — #07  *(issue)*

- `   11 MB`  Warren Ellis/2005/2005 Desolation Jones/Desolation Jones #07.cbr
- `   11 MB`  Warren Ellis/Desolation Jones/Desolation Jones 07.cbr

### midnighter — #16  — identical size  *(issue)*

- `   11 MB`  Warren Ellis/The Authority/Midnighter/Midnighter 16.cbr
- `   11 MB`  The Authority/Midnighter/Midnighter 16.cbr

### saga of swamp thing — #032  — identical size  *(issue)*

- `   11 MB`  Alan Moore/Alan Moore Essentials/Alan Moore 1987- The Saga Of The Swamp Thing/Saga of the Swamp Thing #032.cbr
- `   11 MB`  Alan Moore/Alan Moore Collection II-  DC/Swamp Thing/The Saga Of The Swamp Thing/Saga of the Swamp Thing #032.cbr

### tom strong — #013  — identical size  *(issue)*

- `   11 MB`  Alan Moore/Alan Moore Essentials/Alan Moore 2006- Tom Strong/Tom Strong/Tom Strong #013.cbz
- `   11 MB`  Alan Moore/Alan Moore Collection IV-  America's Best Comics/Tom Strong/Tom Strong/Tom Strong #013.cbz

### saga of swamp thing — #027  — identical size  *(issue)*

- `   11 MB`  Alan Moore/Alan Moore Essentials/Alan Moore 1987- The Saga Of The Swamp Thing/Saga of the Swamp Thing #027.cbr
- `   11 MB`  Alan Moore/Alan Moore Collection II-  DC/Swamp Thing/The Saga Of The Swamp Thing/Saga of the Swamp Thing #027.cbr

### wildstorm armageddon.#5.stormwatch phd  — identical size  *(issue)*

- `   11 MB`  Warren Ellis/The Authority/v4.91 Wildstorm Armageddon/Wildstorm Armageddon.#5.Stormwatch PHD.cbr
- `   11 MB`  The Authority/v4.91 Wildstorm Armageddon/Wildstorm Armageddon.#5.Stormwatch PHD.cbr

### saga of swamp thing — #029  — identical size  *(issue)*

- `   11 MB`  Alan Moore/Alan Moore Essentials/Alan Moore 1987- The Saga Of The Swamp Thing/Saga of the Swamp Thing #029.cbr
- `   11 MB`  Alan Moore/Alan Moore Collection II-  DC/Swamp Thing/The Saga Of The Swamp Thing/Saga of the Swamp Thing #029.cbr

### authority — v1 — #19  — identical size  *(volume)*

- `   11 MB`  Warren Ellis/The Authority/v1 (1999)/The Authority v1 #19.cbr
- `   11 MB`  The Authority/v1 (1999)/The Authority v1 #19.cbr

### midnighter — #14  — identical size  *(issue)*

- `   11 MB`  Warren Ellis/The Authority/Midnighter/Midnighter 14.cbr
- `   11 MB`  The Authority/Midnighter/Midnighter 14.cbr

### authority — v1 — #16  — identical size  *(volume)*

- `   11 MB`  Warren Ellis/The Authority/v1 (1999)/The Authority v1 #16.cbr
- `   11 MB`  The Authority/v1 (1999)/The Authority v1 #16.cbr

### secret history of authority hawksmoor — #2  — identical size  *(issue)*

- `   11 MB`  Warren Ellis/The Authority/specials/Secret History/Secret History of the Authority - Hawksmoor #2.cbr
- `   11 MB`  The Authority/specials/Secret History/Secret History of the Authority - Hawksmoor #2.cbr

### shi vampirella — #01  — identical size  *(issue)*

- `   11 MB`  Warren Ellis/Warren Ellis - Vampirella, Shi, Dracula/Shi - Vampirella 01.cbr
- `   11 MB`  Warren Ellis/1997/Vampirella/Shi - Vampirella 01.cbr

### tom strong — #026  — identical size  *(issue)*

- `   11 MB`  Alan Moore/Alan Moore Essentials/Alan Moore 2006- Tom Strong/Tom Strong/Tom Strong #026.cbz
- `   11 MB`  Alan Moore/Alan Moore Collection IV-  America's Best Comics/Tom Strong/Tom Strong/Tom Strong #026.cbz

### tom strong's terrific tales — #007  — identical size  *(issue)*

- `   11 MB`  Alan Moore/Alan Moore Essentials/Alan Moore 2006- Tom Strong/Tom Strong's Teriffic Tales/Tom Strong's Terrific Tales #007.cbr
- `   11 MB`  Alan Moore/Alan Moore Collection IV-  America's Best Comics/Tom Strong/Tom Strong's Teriffic Tales/Tom Strong's Terrific Tales #007.cbr

### saga of swamp thing — #034  — identical size  *(issue)*

- `   11 MB`  Alan Moore/Alan Moore Essentials/Alan Moore 1987- The Saga Of The Swamp Thing/Saga of the Swamp Thing #034.cbr
- `   11 MB`  Alan Moore/Alan Moore Collection II-  DC/Swamp Thing/The Saga Of The Swamp Thing/Saga of the Swamp Thing #034.cbr

### authority more kev — #1  — identical size  *(issue)*

- `   11 MB`  Warren Ellis/The Authority/Kev/The Authority - More Kev #1.cbr
- `   11 MB`  The Authority/Kev/The Authority - More Kev #1.cbr

### saga of swamp thing — #043  — identical size  *(issue)*

- `   11 MB`  Alan Moore/Alan Moore Essentials/Alan Moore 1987- The Saga Of The Swamp Thing/Saga of the Swamp Thing #043.cbr
- `   11 MB`  Alan Moore/Alan Moore Collection II-  DC/Swamp Thing/The Saga Of The Swamp Thing/Saga of the Swamp Thing #043.cbr

### authority — v1 — #21  — identical size  *(volume)*

- `   11 MB`  Warren Ellis/The Authority/v1 (1999)/The Authority v1 #21.cbr
- `   11 MB`  The Authority/v1 (1999)/The Authority v1 #21.cbr

### tom strong — #025  — identical size  *(issue)*

- `   11 MB`  Alan Moore/Alan Moore Essentials/Alan Moore 2006- Tom Strong/Tom Strong/Tom Strong #025.cbz
- `   11 MB`  Alan Moore/Alan Moore Collection IV-  America's Best Comics/Tom Strong/Tom Strong/Tom Strong #025.cbz

### alan moore's courtyard — #002  — identical size  *(issue)*

- `   11 MB`  Alan Moore/Alan Moore Essentials/Alan Moore 2003- The Courtyard/Alan Moore's The Courtyard #002.cbr
- `   11 MB`  Alan Moore/Alan Moore Collection VI- Made For Moore/Alan Moore's The Courtyard/Alan Moore's The Courtyard/Alan Moore's The Courtyard #002.cbr

### authority — v5 — #02  — identical size  *(volume)*

- `   11 MB`  Warren Ellis/The Authority/v5 (2008)/The Authority v5 #02.cbr
- `   11 MB`  The Authority/v5 (2008)/The Authority v5 #02.cbr

### desolation jones — #02  *(issue)*

- `   11 MB`  Warren Ellis/2005/2005 Desolation Jones/Desolation Jones #02.cbr
- `   10 MB`  Warren Ellis/Desolation Jones/Desolation Jones 02.cbr

### tom strong — #005  — identical size  *(issue)*

- `   11 MB`  Alan Moore/Alan Moore Essentials/Alan Moore 2006- Tom Strong/Tom Strong/Tom Strong #005.cbz
- `   11 MB`  Alan Moore/Alan Moore Collection IV-  America's Best Comics/Tom Strong/Tom Strong/Tom Strong #005.cbz

### tom strong — #022  — identical size  *(issue)*

- `   11 MB`  Alan Moore/Alan Moore Essentials/Alan Moore 2006- Tom Strong/Tom Strong/Tom Strong #022.cbz
- `   11 MB`  Alan Moore/Alan Moore Collection IV-  America's Best Comics/Tom Strong/Tom Strong/Tom Strong #022.cbz

### authority more kev — #4  — identical size  *(issue)*

- `   11 MB`  Warren Ellis/The Authority/Kev/The Authority - More Kev #4.cbr
- `   11 MB`  The Authority/Kev/The Authority - More Kev #4.cbr

### coup d'etat — #3  — identical size  *(issue)*

- `   11 MB`  Warren Ellis/The Authority/v2.5 Coup d'Etat/Coup d'Etat #3 - Wildcats v3.0.cbr
- `   11 MB`  The Authority/v2.5 Coup d'Etat/Coup d'Etat #3 - Wildcats v3.0.cbr

### authority — v2 — #08  — identical size  *(volume)*

- `   11 MB`  Warren Ellis/The Authority/v2 (2003)/The Authority v2 #08.cbr
- `   11 MB`  The Authority/v2 (2003)/The Authority v2 #08.cbr

### authority magnificent kevin — #3  — identical size  *(issue)*

- `   11 MB`  Warren Ellis/The Authority/Kev/The Authority - The Magnificent Kevin #3.cbr
- `   11 MB`  The Authority/Kev/The Authority - The Magnificent Kevin #3.cbr

### midnighter — #20  — identical size  *(issue)*

- `   11 MB`  Warren Ellis/The Authority/Midnighter/Midnighter 20.cbr
- `   11 MB`  The Authority/Midnighter/Midnighter 20.cbr

### 290 armitage influential circles  — identical size  *(issue)*

- `   11 MB`  Judge Dredd The Megazine/Judge Dredd Megazine v5 (201-400)(2002-ongoing)/J.D Megazine Supplements/290 - Armitage - Influential Circles part 2.cbr
- `   11 MB`  Judge Dredd The Megazine/J.D Megazine Supplements/290 - Armitage - Influential Circles part 2.cbr

### man called kev — #2  — identical size  *(issue)*

- `   11 MB`  Warren Ellis/The Authority/Kev/A Man Called Kev #2.cbr
- `   11 MB`  The Authority/Kev/A Man Called Kev #2.cbr

### tom strong's terrific tales — #008  — identical size  *(issue)*

- `   11 MB`  Alan Moore/Alan Moore Essentials/Alan Moore 2006- Tom Strong/Tom Strong's Teriffic Tales/Tom Strong's Terrific Tales #008.cbr
- `   11 MB`  Alan Moore/Alan Moore Collection IV-  America's Best Comics/Tom Strong/Tom Strong's Teriffic Tales/Tom Strong's Terrific Tales #008.cbr

### maximortal — #03  — identical size  *(issue)*

- `   11 MB`  Rick Veitch/Maximortal/Maximortal 03.cbr
- `   11 MB`  Maximortal/Maximortal 01-07/Maximortal #03.cbr

### promethea — #031  — identical size  *(issue)*

- `   11 MB`  Alan Moore/Alan Moore Essentials/Alan Moore 2005- Promethea/Promethea #031.cbr
- `   11 MB`  Alan Moore/Alan Moore Collection IV-  America's Best Comics/Promethea/Promethea/Promethea #031.cbr

### saga of swamp thing — #039  — identical size  *(issue)*

- `   11 MB`  Alan Moore/Alan Moore Essentials/Alan Moore 1987- The Saga Of The Swamp Thing/Saga of the Swamp Thing #039.cbr
- `   11 MB`  Alan Moore/Alan Moore Collection II-  DC/Swamp Thing/The Saga Of The Swamp Thing/Saga of the Swamp Thing #039.cbr

### maximortal — #04  — identical size  *(issue)*

- `   11 MB`  Rick Veitch/Maximortal/Maximortal 04.cbr
- `   11 MB`  Maximortal/Maximortal 01-07/Maximortal #04.cbr

### midnighter — #15  — identical size  *(issue)*

- `   11 MB`  Warren Ellis/The Authority/Midnighter/Midnighter 15.cbr
- `   11 MB`  The Authority/Midnighter/Midnighter 15.cbr

### tom strong — #016  — identical size  *(issue)*

- `   11 MB`  Alan Moore/Alan Moore Essentials/Alan Moore 2006- Tom Strong/Tom Strong/Tom Strong #016.cbz
- `   11 MB`  Alan Moore/Alan Moore Collection IV-  America's Best Comics/Tom Strong/Tom Strong/Tom Strong #016.cbz

### saga of swamp thing — #041  — identical size  *(issue)*

- `   10 MB`  Alan Moore/Alan Moore Essentials/Alan Moore 1987- The Saga Of The Swamp Thing/Saga of the Swamp Thing #041.cbr
- `   10 MB`  Alan Moore/Alan Moore Collection II-  DC/Swamp Thing/The Saga Of The Swamp Thing/Saga of the Swamp Thing #041.cbr

### authority prime — #1  — identical size  *(issue)*

- `   10 MB`  Warren Ellis/The Authority/v4.5 Prime/The Authority Prime #1.cbz
- `   10 MB`  The Authority/v4.5 Prime/The Authority Prime #1.cbz

### tom strong — #018  — identical size  *(issue)*

- `   10 MB`  Alan Moore/Alan Moore Essentials/Alan Moore 2006- Tom Strong/Tom Strong/Tom Strong #018.cbz
- `   10 MB`  Alan Moore/Alan Moore Collection IV-  America's Best Comics/Tom Strong/Tom Strong/Tom Strong #018.cbz

### darkness wanted dead  *(issue)*

- `   10 MB`  Garth Ennis Collection/The Darkness/one-shots/The Darkness - Wanted Dead.cbr
- `   10 MB`  Garth Ennis Collection/The Darkness/The Darkness Volume 1/the darkness - wanted dead.cbr

### saga of swamp thing — #037  — identical size  *(issue)*

- `   10 MB`  Alan Moore/Alan Moore Essentials/Alan Moore 1987- The Saga Of The Swamp Thing/Saga of the Swamp Thing #037.cbr
- `   10 MB`  Alan Moore/Alan Moore Collection II-  DC/Swamp Thing/The Saga Of The Swamp Thing/Saga of the Swamp Thing #037.cbr

### tom strong — #003  — identical size  *(issue)*

- `   10 MB`  Alan Moore/Alan Moore Essentials/Alan Moore 2006- Tom Strong/Tom Strong/Tom Strong #003.cbz
- `   10 MB`  Alan Moore/Alan Moore Collection IV-  America's Best Comics/Tom Strong/Tom Strong/Tom Strong #003.cbz

### alan moore's courtyard — #001  — identical size  *(issue)*

- `   10 MB`  Alan Moore/Alan Moore Essentials/Alan Moore 2003- The Courtyard/Alan Moore's The Courtyard #001.cbr
- `   10 MB`  Alan Moore/Alan Moore Collection VI- Made For Moore/Alan Moore's The Courtyard/Alan Moore's The Courtyard/Alan Moore's The Courtyard #001.cbr

### authority magnificent kevin — #5  — identical size  *(issue)*

- `   10 MB`  Warren Ellis/The Authority/Kev/The Authority - The Magnificent Kevin #5.cbr
- `   10 MB`  The Authority/Kev/The Authority - The Magnificent Kevin #5.cbr

### saga of swamp thing — #059  — identical size  *(issue)*

- `   10 MB`  Alan Moore/Alan Moore Essentials/Alan Moore 1987- The Saga Of The Swamp Thing/Saga of the Swamp Thing #059.cbr
- `   10 MB`  Alan Moore/Alan Moore Collection II-  DC/Swamp Thing/The Saga Of The Swamp Thing/Saga of the Swamp Thing #059.cbr

### saga of swamp thing — #030  — identical size  *(issue)*

- `   10 MB`  Alan Moore/Alan Moore Essentials/Alan Moore 1987- The Saga Of The Swamp Thing/Saga of the Swamp Thing #030.cbr
- `   10 MB`  Alan Moore/Alan Moore Collection II-  DC/Swamp Thing/The Saga Of The Swamp Thing/Saga of the Swamp Thing #030.cbr

### tom strong — #004  — identical size  *(issue)*

- `   10 MB`  Alan Moore/Alan Moore Essentials/Alan Moore 2006- Tom Strong/Tom Strong/Tom Strong #004.cbz
- `   10 MB`  Alan Moore/Alan Moore Collection IV-  America's Best Comics/Tom Strong/Tom Strong/Tom Strong #004.cbz

### top ten — #008  — identical size  *(issue)*

- `   10 MB`  Alan Moore/Alan Moore Essentials/Alan Moore 2001- Top Ten/Top Ten #008.cbr
- `   10 MB`  Alan Moore/Alan Moore Collection IV-  America's Best Comics/Top Ten/Top Ten/Top Ten #008.cbr

### 285 judge dredd john higgins  — identical size  *(volume)*

- `   10 MB`  Judge Dredd The Megazine/Judge Dredd Megazine v5 (201-400)(2002-ongoing)/J.D Megazine Supplements/285 - Judge Dredd - The John Higgins Collection.cbr
- `   10 MB`  Judge Dredd The Megazine/J.D Megazine Supplements/285 - Judge Dredd - The John Higgins Collection.cbr

### authority magnificent kevin — #4  — identical size  *(issue)*

- `   10 MB`  Warren Ellis/The Authority/Kev/The Authority - The Magnificent Kevin #4.cbr
- `   10 MB`  The Authority/Kev/The Authority - The Magnificent Kevin #4.cbr

### top ten — #005  — identical size  *(issue)*

- `   10 MB`  Alan Moore/Alan Moore Essentials/Alan Moore 2001- Top Ten/Top Ten #005.cbr
- `   10 MB`  Alan Moore/Alan Moore Collection IV-  America's Best Comics/Top Ten/Top Ten/Top Ten #005.cbr

### tom strong — #021  — identical size  *(issue)*

- `   10 MB`  Alan Moore/Alan Moore Essentials/Alan Moore 2006- Tom Strong/Tom Strong/Tom Strong #021.cbz
- `   10 MB`  Alan Moore/Alan Moore Collection IV-  America's Best Comics/Tom Strong/Tom Strong/Tom Strong #021.cbz

### secret history of authority hawksmoor — #6  — identical size  *(issue)*

- `   10 MB`  Warren Ellis/The Authority/specials/Secret History/Secret History of the Authority - Hawksmoor #6.cbr
- `   10 MB`  The Authority/specials/Secret History/Secret History of the Authority - Hawksmoor #6.cbr

### 289 armitage influential circles  — identical size  *(issue)*

- `   10 MB`  Judge Dredd The Megazine/Judge Dredd Megazine v5 (201-400)(2002-ongoing)/J.D Megazine Supplements/289 - Armitage - Influential Circles part 1.cbr
- `   10 MB`  Judge Dredd The Megazine/J.D Megazine Supplements/289 - Armitage - Influential Circles part 1.cbr

### saga of swamp thing — #038  — identical size  *(issue)*

- `   10 MB`  Alan Moore/Alan Moore Essentials/Alan Moore 1987- The Saga Of The Swamp Thing/Saga of the Swamp Thing #038.cbr
- `   10 MB`  Alan Moore/Alan Moore Collection II-  DC/Swamp Thing/The Saga Of The Swamp Thing/Saga of the Swamp Thing #038.cbr

### top ten — #006  — identical size  *(issue)*

- `   10 MB`  Alan Moore/Alan Moore Essentials/Alan Moore 2001- Top Ten/Top Ten #006.cbr
- `   10 MB`  Alan Moore/Alan Moore Collection IV-  America's Best Comics/Top Ten/Top Ten/Top Ten #006.cbr

### top ten — #007  — identical size  *(issue)*

- `   10 MB`  Alan Moore/Alan Moore Essentials/Alan Moore 2001- Top Ten/Top Ten #007.cbr
- `   10 MB`  Alan Moore/Alan Moore Collection IV-  America's Best Comics/Top Ten/Top Ten/Top Ten #007.cbr

### saga of swamp thing — #035  — identical size  *(issue)*

- `   10 MB`  Alan Moore/Alan Moore Essentials/Alan Moore 1987- The Saga Of The Swamp Thing/Saga of the Swamp Thing #035.cbr
- `   10 MB`  Alan Moore/Alan Moore Collection II-  DC/Swamp Thing/The Saga Of The Swamp Thing/Saga of the Swamp Thing #035.cbr

### saga of swamp thing — #042  — identical size  *(issue)*

- `   10 MB`  Alan Moore/Alan Moore Essentials/Alan Moore 1987- The Saga Of The Swamp Thing/Saga of the Swamp Thing #042.cbr
- `   10 MB`  Alan Moore/Alan Moore Collection II-  DC/Swamp Thing/The Saga Of The Swamp Thing/Saga of the Swamp Thing #042.cbr

### city of silence — #02  *(issue)*

- `   10 MB`  Warren Ellis/Warren Ellis - City Of Silence/City of Silence #02.cbr
- `   10 MB`  Warren Ellis/2000/City of Silence/City Of Silence 02.cbr

### maximortal — #02  — identical size  *(issue)*

- `   10 MB`  Rick Veitch/Maximortal/Maximortal 02.cbr
- `   10 MB`  Maximortal/Maximortal 01-07/Maximortal #02.cbr

### tom strong — #006  — identical size  *(issue)*

- `   10 MB`  Alan Moore/Alan Moore Essentials/Alan Moore 2006- Tom Strong/Tom Strong/Tom Strong #006.cbr
- `   10 MB`  Alan Moore/Alan Moore Collection IV-  America's Best Comics/Tom Strong/Tom Strong/Tom Strong #006.cbr

### maximortal — #06  — identical size  *(issue)*

- `   10 MB`  Rick Veitch/Maximortal/Maximortal 06.cbr
- `   10 MB`  Maximortal/Maximortal 01-07/Maximortal #06.cbr

### doom patrol — v2 — #079  — identical size  *(volume)*

- `   10 MB`  Ted McKeever (Collection) (1987-2007)/1994 - Doom Patrol (Vertigo - w Rachael Pollack)/Doom Patrol v2 079 (The Teiresias Wars pt 5 - The Fire Sermon).cbz
- `   10 MB`  Grant Morrison/Comics/Doom Patrol/Doom Patrol v2 079 (The Teiresias Wars pt 5 - The Fire Sermon).cbz

### top ten — #011  — identical size  *(issue)*

- `   10 MB`  Alan Moore/Alan Moore Essentials/Alan Moore 2001- Top Ten/Top Ten #011.cbz
- `   10 MB`  Alan Moore/Alan Moore Collection IV-  America's Best Comics/Top Ten/Top Ten/Top Ten #011.cbz

### top ten — #11  — identical size  *(issue)*

- `   10 MB`  Top 10/Top Ten 11.cbz
- `   10 MB`  Alan Moore/Top 10/Top Ten 11.cbz

### tom strong — #010  — identical size  *(issue)*

- `   10 MB`  Alan Moore/Alan Moore Essentials/Alan Moore 2006- Tom Strong/Tom Strong/Tom Strong #010.cbz
- `   10 MB`  Alan Moore/Alan Moore Collection IV-  America's Best Comics/Tom Strong/Tom Strong/Tom Strong #010.cbz

### chiaroscuro private lives of leonardo da vinci — #00  *(issue)*

- `   17 MB`  Aster Blistok/Le Vagabond des Limbes/Chiaroscuro - The Private Lives of Leonardo da Vinci 00-10 (1995-1996) (HD-Upscaled)/Chiaroscuro - The Private Lives of Leonardo da Vinci 00 Preview (1995) (Scantron-DCP) (HD Minutemen-juvecube).cbz
- `    3 MB`  Aster Blistok/Le Vagabond des Limbes/Chiaroscuro (Vertigo)(1995)(c)/Chiaroscuro - The Private Lives of Leonardo da Vinci _00 Preview (1995) (Scantron-DCP).cbr

### saga of swamp thing — #036  — identical size  *(issue)*

- `   10 MB`  Alan Moore/Alan Moore Essentials/Alan Moore 1987- The Saga Of The Swamp Thing/Saga of the Swamp Thing #036.cbr
- `   10 MB`  Alan Moore/Alan Moore Collection II-  DC/Swamp Thing/The Saga Of The Swamp Thing/Saga of the Swamp Thing #036.cbr

### saga of swamp thing — #040  — identical size  *(issue)*

- `   10 MB`  Alan Moore/Alan Moore Essentials/Alan Moore 1987- The Saga Of The Swamp Thing/Saga of the Swamp Thing #040.cbr
- `   10 MB`  Alan Moore/Alan Moore Collection II-  DC/Swamp Thing/The Saga Of The Swamp Thing/Saga of the Swamp Thing #040.cbr

### saga of swamp thing — #051  — identical size  *(issue)*

- `   10 MB`  Alan Moore/Alan Moore Essentials/Alan Moore 1987- The Saga Of The Swamp Thing/Saga of the Swamp Thing #051.cbr
- `   10 MB`  Alan Moore/Alan Moore Collection II-  DC/Swamp Thing/The Saga Of The Swamp Thing/Saga of the Swamp Thing #051.cbr

### saga of swamp thing — #026  — identical size  *(issue)*

- `   10 MB`  Alan Moore/Alan Moore Essentials/Alan Moore 1987- The Saga Of The Swamp Thing/Saga of the Swamp Thing #026.cbr
- `   10 MB`  Alan Moore/Alan Moore Collection II-  DC/Swamp Thing/The Saga Of The Swamp Thing/Saga of the Swamp Thing #026.cbr

### authority kev  — identical size  *(issue)*

- `   10 MB`  Warren Ellis/The Authority/Kev/The Authority - Kev.cbr
- `   10 MB`  The Authority/Kev/The Authority - Kev.cbr

### saga of swamp thing — #052  — identical size  *(issue)*

- `   10 MB`  Alan Moore/Alan Moore Essentials/Alan Moore 1987- The Saga Of The Swamp Thing/Saga of the Swamp Thing #052.cbr
- `   10 MB`  Alan Moore/Alan Moore Collection II-  DC/Swamp Thing/The Saga Of The Swamp Thing/Saga of the Swamp Thing #052.cbr

### maximortal — #01  — identical size  *(issue)*

- `   10 MB`  Rick Veitch/Maximortal/Maximortal 01.cbr
- `   10 MB`  Maximortal/Maximortal 01-07/Maximortal #01.cbr

### authority — v2 — #05  — identical size  *(volume)*

- `   10 MB`  Warren Ellis/The Authority/v2 (2003)/The Authority v2 #05.cbr
- `   10 MB`  The Authority/v2 (2003)/The Authority v2 #05.cbr

### saga of swamp thing — #021  — identical size  *(issue)*

- `   10 MB`  Alan Moore/Alan Moore Essentials/Alan Moore 1987- The Saga Of The Swamp Thing/Saga of the Swamp Thing #021.cbr
- `   10 MB`  Alan Moore/Alan Moore Collection II-  DC/Swamp Thing/The Saga Of The Swamp Thing/Saga of the Swamp Thing #021.cbr

### saga of swamp thing — #054  — identical size  *(issue)*

- `   10 MB`  Alan Moore/Alan Moore Essentials/Alan Moore 1987- The Saga Of The Swamp Thing/Saga of the Swamp Thing #054.cbr
- `   10 MB`  Alan Moore/Alan Moore Collection II-  DC/Swamp Thing/The Saga Of The Swamp Thing/Saga of the Swamp Thing #054.cbr

### promethea — #030  — identical size  *(issue)*

- `   10 MB`  Alan Moore/Alan Moore Essentials/Alan Moore 2005- Promethea/Promethea #030.cbr
- `   10 MB`  Alan Moore/Alan Moore Collection IV-  America's Best Comics/Promethea/Promethea/Promethea #030.cbr

### tom strong — #011  — identical size  *(issue)*

- `   10 MB`  Alan Moore/Alan Moore Essentials/Alan Moore 2006- Tom Strong/Tom Strong/Tom Strong #011.cbz
- `   10 MB`  Alan Moore/Alan Moore Collection IV-  America's Best Comics/Tom Strong/Tom Strong/Tom Strong #011.cbz

### korto malteze u znaku jarca — #1  — identical size  *(issue)*

- `   10 MB`  YU stripovi 2019/Korto (YU)/Korto Malteze - U znaku jarca 1 - Tajna Tristana Bantama.cbr
- `   10 MB`  Corto Maltese/Korto Malteze - U znaku jarca 1 - Tajna Tristana Bantama.cbr

### tom strong — #002  — identical size  *(issue)*

- `   10 MB`  Alan Moore/Alan Moore Essentials/Alan Moore 2006- Tom Strong/Tom Strong/Tom Strong #002.cbr
- `   10 MB`  Alan Moore/Alan Moore Collection IV-  America's Best Comics/Tom Strong/Tom Strong/Tom Strong #002.cbr

### tom strong — #035  — identical size  *(issue)*

- `   10 MB`  Alan Moore/Alan Moore Essentials/Alan Moore 2006- Tom Strong/Tom Strong/Tom Strong #035.cbr
- `   10 MB`  Alan Moore/Alan Moore Collection IV-  America's Best Comics/Tom Strong/Tom Strong/Tom Strong #035.cbr

### saga of swamp thing — #047  — identical size  *(issue)*

- `   10 MB`  Alan Moore/Alan Moore Essentials/Alan Moore 1987- The Saga Of The Swamp Thing/Saga of the Swamp Thing #047.cbr
- `   10 MB`  Alan Moore/Alan Moore Collection II-  DC/Swamp Thing/The Saga Of The Swamp Thing/Saga of the Swamp Thing #047.cbr

### authority — v2 — #00  — identical size  *(volume)*

- `   10 MB`  Warren Ellis/The Authority/v2 (2003)/The Authority v2 #00.cbz
- `   10 MB`  The Authority/v2 (2003)/The Authority v2 #00.cbz

### tom strong — #008  — identical size  *(issue)*

- `   10 MB`  Alan Moore/Alan Moore Essentials/Alan Moore 2006- Tom Strong/Tom Strong/Tom Strong #008.cbz
- `   10 MB`  Alan Moore/Alan Moore Collection IV-  America's Best Comics/Tom Strong/Tom Strong/Tom Strong #008.cbz

### promethea — #028  — identical size  *(issue)*

- `   10 MB`  Alan Moore/Alan Moore Essentials/Alan Moore 2005- Promethea/Promethea #028.cbr
- `   10 MB`  Alan Moore/Alan Moore Collection IV-  America's Best Comics/Promethea/Promethea/Promethea #028.cbr

### city of silence — #03  *(issue)*

- `   10 MB`  Warren Ellis/Warren Ellis - City Of Silence/City of Silence #03.cbr
- `   10 MB`  Warren Ellis/2000/City of Silence/City Of Silence 03.cbr

### vampirella lives — #01  — identical size  *(issue)*

- `   10 MB`  Warren Ellis/Warren Ellis - Vampirella, Shi, Dracula/Vampirella Lives 01.cbr
- `   10 MB`  Warren Ellis/1997/Vampirella/Vampirella Lives 01.cbr

### desolation jones — #01  *(issue)*

- `   10 MB`  Warren Ellis/2005/2005 Desolation Jones/Desolation Jones #01.cbr
- `    9 MB`  Warren Ellis/Desolation Jones/Desolation Jones 01.cbr

### promethea — #027  — identical size  *(issue)*

- `   10 MB`  Alan Moore/Alan Moore Essentials/Alan Moore 2005- Promethea/Promethea #027.cbr
- `   10 MB`  Alan Moore/Alan Moore Collection IV-  America's Best Comics/Promethea/Promethea/Promethea #027.cbr

### you are judge dredd in house of death  — identical size  *(issue)*

- `   10 MB`  2000AD prog/2000AD Yearbooks & Specials (1977 - 2013)/Judge Dredd (Specials, Poster Progs & Extras) (-JJ-)/You are Judge Dredd in the House of Death (Diceman#1 ).cbr
- `   10 MB`  2000AD prog/2000AD (Specials, Annuals & Poster Progs + Extras)/2000AD Yearbooks & Specials (1977 - 2013)/Judge Dredd (Specials, Poster Progs & Extras) (-JJ-)/You are Judge Dredd in the House of Death (Diceman#1 ).cbr

### saga of swamp thing — #057  — identical size  *(issue)*

- `   10 MB`  Alan Moore/Alan Moore Essentials/Alan Moore 1987- The Saga Of The Swamp Thing/Saga of the Swamp Thing #057.cbr
- `   10 MB`  Alan Moore/Alan Moore Collection II-  DC/Swamp Thing/The Saga Of The Swamp Thing/Saga of the Swamp Thing #057.cbr

### saga of swamp thing — #055  — identical size  *(issue)*

- `   10 MB`  Alan Moore/Alan Moore Essentials/Alan Moore 1987- The Saga Of The Swamp Thing/Saga of the Swamp Thing #055.cbr
- `   10 MB`  Alan Moore/Alan Moore Collection II-  DC/Swamp Thing/The Saga Of The Swamp Thing/Saga of the Swamp Thing #055.cbr

### top ten — #003  — identical size  *(issue)*

- `   10 MB`  Alan Moore/Alan Moore Essentials/Alan Moore 2001- Top Ten/Top Ten #003.cbr
- `   10 MB`  Alan Moore/Alan Moore Collection IV-  America's Best Comics/Top Ten/Top Ten/Top Ten #003.cbr

### saga of swamp thing — #049  — identical size  *(issue)*

- `   10 MB`  Alan Moore/Alan Moore Essentials/Alan Moore 1987- The Saga Of The Swamp Thing/Saga of the Swamp Thing #049.cbr
- `   10 MB`  Alan Moore/Alan Moore Collection II-  DC/Swamp Thing/The Saga Of The Swamp Thing/Saga of the Swamp Thing #049.cbr

### 287 armitage first cut  — identical size  *(issue)*

- `    9 MB`  Judge Dredd The Megazine/Judge Dredd Megazine v5 (201-400)(2002-ongoing)/J.D Megazine Supplements/287 - Armitage - First Cut.cbr
- `    9 MB`  Judge Dredd The Megazine/J.D Megazine Supplements/287 - Armitage - First Cut.cbr

### saga of swamp thing — #058  — identical size  *(issue)*

- `    9 MB`  Alan Moore/Alan Moore Essentials/Alan Moore 1987- The Saga Of The Swamp Thing/Saga of the Swamp Thing #058.cbr
- `    9 MB`  Alan Moore/Alan Moore Collection II-  DC/Swamp Thing/The Saga Of The Swamp Thing/Saga of the Swamp Thing #058.cbr

### authority — v2 — #01  — identical size  *(volume)*

- `    9 MB`  Warren Ellis/The Authority/v2 (2003)/The Authority v2 #01.cbr
- `    9 MB`  The Authority/v2 (2003)/The Authority v2 #01.cbr

### captain atom armageddon — #9  — identical size  *(issue)*

- `    9 MB`  Warren Ellis/The Authority/v3.9 Captain Atom- Armageddon/Captain Atom - Armageddon 9.cbr
- `    9 MB`  The Authority/v3.9 Captain Atom- Armageddon/Captain Atom - Armageddon 9.cbr

### saga of swamp thing — #045  — identical size  *(issue)*

- `    9 MB`  Alan Moore/Alan Moore Essentials/Alan Moore 1987- The Saga Of The Swamp Thing/Saga of the Swamp Thing #045.cbr
- `    9 MB`  Alan Moore/Alan Moore Collection II-  DC/Swamp Thing/The Saga Of The Swamp Thing/Saga of the Swamp Thing #045.cbr

### authority — v2 — #02  — identical size  *(volume)*

- `    9 MB`  Warren Ellis/The Authority/v2 (2003)/The Authority v2 #02.cbr
- `    9 MB`  The Authority/v2 (2003)/The Authority v2 #02.cbr

### tom strong — #009  — identical size  *(issue)*

- `    9 MB`  Alan Moore/Alan Moore Essentials/Alan Moore 2006- Tom Strong/Tom Strong/Tom Strong #009.cbz
- `    9 MB`  Alan Moore/Alan Moore Collection IV-  America's Best Comics/Tom Strong/Tom Strong/Tom Strong #009.cbz

### saga of swamp thing — #044  — identical size  *(issue)*

- `    9 MB`  Alan Moore/Alan Moore Essentials/Alan Moore 1987- The Saga Of The Swamp Thing/Saga of the Swamp Thing #044.cbr
- `    9 MB`  Alan Moore/Alan Moore Collection II-  DC/Swamp Thing/The Saga Of The Swamp Thing/Saga of the Swamp Thing #044.cbr

### saga of swamp thing — #048  — identical size  *(issue)*

- `    9 MB`  Alan Moore/Alan Moore Essentials/Alan Moore 1987- The Saga Of The Swamp Thing/Saga of the Swamp Thing #048.cbr
- `    9 MB`  Alan Moore/Alan Moore Collection II-  DC/Swamp Thing/The Saga Of The Swamp Thing/Saga of the Swamp Thing #048.cbr

### saga of swamp thing — #031  — identical size  *(issue)*

- `    9 MB`  Alan Moore/Alan Moore Essentials/Alan Moore 1987- The Saga Of The Swamp Thing/Saga of the Swamp Thing #031.cbr
- `    9 MB`  Alan Moore/Alan Moore Collection II-  DC/Swamp Thing/The Saga Of The Swamp Thing/Saga of the Swamp Thing #031.cbr

### authority — v2 — #04  — identical size  *(volume)*

- `    9 MB`  Warren Ellis/The Authority/v2 (2003)/The Authority v2 #04.cbr
- `    9 MB`  The Authority/v2 (2003)/The Authority v2 #04.cbr

### tom strong — #028  — identical size  *(issue)*

- `    9 MB`  Alan Moore/Alan Moore Essentials/Alan Moore 2006- Tom Strong/Tom Strong/Tom Strong #028.cbz
- `    9 MB`  Alan Moore/Alan Moore Collection IV-  America's Best Comics/Tom Strong/Tom Strong/Tom Strong #028.cbz

### saga of swamp thing — #060  — identical size  *(issue)*

- `    9 MB`  Alan Moore/Alan Moore Essentials/Alan Moore 1987- The Saga Of The Swamp Thing/Saga of the Swamp Thing #060.cbr
- `    9 MB`  Alan Moore/Alan Moore Collection II-  DC/Swamp Thing/The Saga Of The Swamp Thing/Saga of the Swamp Thing #060.cbr

### desolation jones — #06  *(issue)*

- `    9 MB`  Warren Ellis/2005/2005 Desolation Jones/Desolation Jones #06.cbr
- `    9 MB`  Warren Ellis/Desolation Jones/Desolation Jones 06.cbr

### saga of swamp thing — #046  — identical size  *(issue)*

- `    9 MB`  Alan Moore/Alan Moore Essentials/Alan Moore 1987- The Saga Of The Swamp Thing/Saga of the Swamp Thing #046.cbr
- `    9 MB`  Alan Moore/Alan Moore Collection II-  DC/Swamp Thing/The Saga Of The Swamp Thing/Saga of the Swamp Thing #046.cbr

### tom strong — #007  — identical size  *(issue)*

- `    9 MB`  Alan Moore/Alan Moore Essentials/Alan Moore 2006- Tom Strong/Tom Strong/Tom Strong #007.cbz
- `    9 MB`  Alan Moore/Alan Moore Collection IV-  America's Best Comics/Tom Strong/Tom Strong/Tom Strong #007.cbz

### top ten — #004  — identical size  *(issue)*

- `    9 MB`  Alan Moore/Alan Moore Essentials/Alan Moore 2001- Top Ten/Top Ten #004.cbr
- `    9 MB`  Alan Moore/Alan Moore Collection IV-  America's Best Comics/Top Ten/Top Ten/Top Ten #004.cbr

### midnighter — #17  — identical size  *(issue)*

- `    9 MB`  Warren Ellis/The Authority/Midnighter/Midnighter 17.cbr
- `    9 MB`  The Authority/Midnighter/Midnighter 17.cbr

### tom strong's terrific tales — #005  — identical size  *(issue)*

- `    9 MB`  Alan Moore/Alan Moore Essentials/Alan Moore 2006- Tom Strong/Tom Strong's Teriffic Tales/Tom Strong's Terrific Tales #005.cbz
- `    9 MB`  Alan Moore/Alan Moore Collection IV-  America's Best Comics/Tom Strong/Tom Strong's Teriffic Tales/Tom Strong's Terrific Tales #005.cbz

### tom strong — #012  — identical size  *(issue)*

- `    9 MB`  Alan Moore/Alan Moore Essentials/Alan Moore 2006- Tom Strong/Tom Strong/Tom Strong #012.cbz
- `    9 MB`  Alan Moore/Alan Moore Collection IV-  America's Best Comics/Tom Strong/Tom Strong/Tom Strong #012.cbz

### top ten — #002  — identical size  *(issue)*

- `    9 MB`  Alan Moore/Alan Moore Essentials/Alan Moore 2001- Top Ten/Top Ten #002.cbr
- `    9 MB`  Alan Moore/Alan Moore Collection IV-  America's Best Comics/Top Ten/Top Ten/Top Ten #002.cbr

### planetary extras leavingth century  — identical size  *(issue)*

- `    9 MB`  Warren Ellis/Planetary/Planetary TPB Extras Leaving the 20th Century.cbz
- `    9 MB`  Warren Ellis/1999/1999 Planetary/Planetary TPB Extras Leaving the 20th Century.cbz

### promethea — #029  — identical size  *(issue)*

- `    9 MB`  Alan Moore/Alan Moore Essentials/Alan Moore 2005- Promethea/Promethea #029.cbr
- `    9 MB`  Alan Moore/Alan Moore Collection IV-  America's Best Comics/Promethea/Promethea/Promethea #029.cbr

### authority — v2 — #03  — identical size  *(volume)*

- `    9 MB`  Warren Ellis/The Authority/v2 (2003)/The Authority v2 #03.cbr
- `    9 MB`  The Authority/v2 (2003)/The Authority v2 #03.cbr

### authority — v4 — #02  — identical size  *(volume)*

- `    9 MB`  Warren Ellis/The Authority/v4 (2006)/The Authority v4 #02.cbr
- `    9 MB`  The Authority/v4 (2006)/The Authority v4 #02.cbr

### desolation jones — #04  — identical size  *(issue)*

- `    9 MB`  Warren Ellis/Desolation Jones/Desolation Jones 04.cbr
- `    9 MB`  Warren Ellis/2005/2005 Desolation Jones/Desolation Jones #04.cbr

### doom patrol — v2 — #075  — identical size  *(volume)*

- `    9 MB`  Ted McKeever (Collection) (1987-2007)/1994 - Doom Patrol (Vertigo - w Rachael Pollack)/Doom Patrol v2 075 (The Teiresias Wars pt 1 - A Handful Of Dust).cbz
- `    9 MB`  Grant Morrison/Comics/Doom Patrol/Doom Patrol v2 075 (The Teiresias Wars pt 1 - A Handful Of Dust).cbz

### captain atom armageddon — #2  — identical size  *(issue)*

- `    9 MB`  Warren Ellis/The Authority/v3.9 Captain Atom- Armageddon/Captain Atom - Armageddon 2.cbr
- `    9 MB`  The Authority/v3.9 Captain Atom- Armageddon/Captain Atom - Armageddon 2.cbr

### authority — v2 — #12  — identical size  *(volume)*

- `    9 MB`  Warren Ellis/The Authority/v2 (2003)/The Authority v2 #12.cbr
- `    9 MB`  The Authority/v2 (2003)/The Authority v2 #12.cbr

### authority — v2 — #14  — identical size  *(volume)*

- `    9 MB`  Warren Ellis/The Authority/v2 (2003)/The Authority v2 #14.cbr
- `    9 MB`  The Authority/v2 (2003)/The Authority v2 #14.cbr

### authority — v1 — #10  — identical size  *(volume)*

- `    6 MB`  Warren Ellis/The Authority/v1 (1999)/The Authority v1 #10.cbr
- `    6 MB`  Warren Ellis/1999/1999 The Authority/The Authority v1 #10.cbr
- `    6 MB`  The Authority/v1 (1999)/The Authority v1 #10.cbr

### dracurella — v1  — identical size  *(volume)*

- `    9 MB`  YU stripovi 2019/Drakuleta/Dracurella - T01 - ( 4 episodes ).cbz
- `    9 MB`  YU stripovi 2019/Dracurella - T01 - ( 4 episodes ).cbz

### desolation jones — #05  — identical size  *(issue)*

- `    9 MB`  Warren Ellis/Desolation Jones/Desolation Jones 05.cbr
- `    9 MB`  Warren Ellis/2005/2005 Desolation Jones/Desolation Jones #05.cbr

### doom patrol — v2 — #077  — identical size  *(volume)*

- `    9 MB`  Ted McKeever (Collection) (1987-2007)/1994 - Doom Patrol (Vertigo - w Rachael Pollack)/Doom Patrol v2 077 (The Teiresias Wars pt 3 - The Witness Trees).cbz
- `    9 MB`  Grant Morrison/Comics/Doom Patrol/Doom Patrol v2 077 (The Teiresias Wars pt 3 - The Witness Trees).cbz

### tom strong — #023  — identical size  *(issue)*

- `    8 MB`  Alan Moore/Alan Moore Essentials/Alan Moore 2006- Tom Strong/Tom Strong/Tom Strong #023.cbz
- `    8 MB`  Alan Moore/Alan Moore Collection IV-  America's Best Comics/Tom Strong/Tom Strong/Tom Strong #023.cbz

### doktor sleepless manual — #001  — identical size  *(issue)*

- `    8 MB`  Warren Ellis/Warren Ellis - Doktor Sleepless/Doktor Sleepless Manual 001.cbr
- `    8 MB`  Warren Ellis/2007/2007 Doktor Sleepless/Doktor Sleepless Manual 001.cbr

### authority — v1 — #11  — identical size  *(volume)*

- `    6 MB`  Warren Ellis/The Authority/v1 (1999)/The Authority v1 #11.cbr
- `    6 MB`  Warren Ellis/1999/1999 The Authority/The Authority v1 #11.cbr
- `    6 MB`  The Authority/v1 (1999)/The Authority v1 #11.cbr

### newuniversal — #01  *(issue)*

- `   16 MB`  Warren Ellis/2007/2007 Newuniversal/newuniversal #01 (2007) (Minutemen-LockeZone).cbr
- `    1 MB`  Warren Ellis/2007/2007 Newuniversal/newuniversal #01 (2nd print cover).cbr

### tom strong — #024  — identical size  *(issue)*

- `    8 MB`  Alan Moore/Alan Moore Essentials/Alan Moore 2006- Tom Strong/Tom Strong/Tom Strong #024.cbz
- `    8 MB`  Alan Moore/Alan Moore Collection IV-  America's Best Comics/Tom Strong/Tom Strong/Tom Strong #024.cbz

### captain atom armageddon — #3  — identical size  *(issue)*

- `    8 MB`  Warren Ellis/The Authority/v3.9 Captain Atom- Armageddon/Captain Atom - Armageddon 3.cbr
- `    8 MB`  The Authority/v3.9 Captain Atom- Armageddon/Captain Atom - Armageddon 3.cbr

### devil's night — #2  — identical size  *(issue)*

- `    8 MB`  Warren Ellis/The Authority/specials/Devil's Night (2000 Annuals)/Devil's Night #2 - Wildcats - Annual 2000.cbr
- `    8 MB`  The Authority/specials/Devil's Night (2000 Annuals)/Devil's Night #2 - Wildcats - Annual 2000.cbr

### authority — v1 — #09  — identical size  *(volume)*

- `    5 MB`  Warren Ellis/The Authority/v1 (1999)/The Authority v1 #09.cbr
- `    5 MB`  Warren Ellis/1999/1999 The Authority/The Authority v1 #09.cbr
- `    5 MB`  The Authority/v1 (1999)/The Authority v1 #09.cbr

### authority — v1 — #12  — identical size  *(volume)*

- `    5 MB`  Warren Ellis/The Authority/v1 (1999)/The Authority v1 #12.cbr
- `    5 MB`  Warren Ellis/1999/1999 The Authority/The Authority v1 #12.cbr
- `    5 MB`  The Authority/v1 (1999)/The Authority v1 #12.cbr

### doom patrol — v2 — #076  — identical size  *(volume)*

- `    8 MB`  Ted McKeever (Collection) (1987-2007)/1994 - Doom Patrol (Vertigo - w Rachael Pollack)/Doom Patrol v2 076 (The Teiresias Wars pt 2 - The Hotel Of Lost Light).cbz
- `    8 MB`  Grant Morrison/Comics/Doom Patrol/Doom Patrol v2 076 (The Teiresias Wars pt 2 - The Hotel Of Lost Light).cbz

### authority — v2 — #13  — identical size  *(volume)*

- `    8 MB`  Warren Ellis/The Authority/v2 (2003)/The Authority v2 #13.cbr
- `    8 MB`  The Authority/v2 (2003)/The Authority v2 #13.cbr

### spawn — #037  — identical size  *(issue)*

- `    8 MB`  Alan Moore/Spawn/Spawn 037.cbr
- `    8 MB`  Alan Moore/Alan Moore Collection III-  Image - Awesome Comics/Spawn/Spawn (ongoing series)/Spawn #037.cbr

### captain atom armageddon — #4  — identical size  *(issue)*

- `    8 MB`  Warren Ellis/The Authority/v3.9 Captain Atom- Armageddon/Captain Atom - Armageddon 4.cbr
- `    8 MB`  The Authority/v3.9 Captain Atom- Armageddon/Captain Atom - Armageddon 4.cbr

### captain atom armageddon — #7  — identical size  *(issue)*

- `    8 MB`  Warren Ellis/The Authority/v3.9 Captain Atom- Armageddon/Captain Atom - Armageddon 7.cbr
- `    8 MB`  The Authority/v3.9 Captain Atom- Armageddon/Captain Atom - Armageddon 7.cbr

### tom strong — #036  — identical size  *(issue)*

- `    8 MB`  Alan Moore/Alan Moore Essentials/Alan Moore 2006- Tom Strong/Tom Strong/Tom Strong #036.cbr
- `    8 MB`  Alan Moore/Alan Moore Collection IV-  America's Best Comics/Tom Strong/Tom Strong/Tom Strong #036.cbr

### captain atom armageddon — #8  — identical size  *(issue)*

- `    8 MB`  Warren Ellis/The Authority/v3.9 Captain Atom- Armageddon/Captain Atom - Armageddon 8.cbr
- `    8 MB`  The Authority/v3.9 Captain Atom- Armageddon/Captain Atom - Armageddon 8.cbr

### doom patrol — v2 — #078  — identical size  *(volume)*

- `    8 MB`  Ted McKeever (Collection) (1987-2007)/1994 - Doom Patrol (Vertigo - w Rachael Pollack)/Doom Patrol v2 078 (The Teiresias Wars pt 4 - The Path of Vanished Alphabets).cbz
- `    8 MB`  Grant Morrison/Comics/Doom Patrol/Doom Patrol v2 078 (The Teiresias Wars pt 4 - The Path of Vanished Alphabets).cbz

### authority — v1 — #25  — identical size  *(volume)*

- `    7 MB`  Warren Ellis/The Authority/v1 (1999)/The Authority v1 #25.cbr
- `    7 MB`  The Authority/v1 (1999)/The Authority v1 #25.cbr

### authority — v1 — #01  — identical size  *(volume)*

- `    5 MB`  Warren Ellis/The Authority/v1 (1999)/The Authority v1 #01.cbr
- `    5 MB`  Warren Ellis/1999/1999 The Authority/The Authority v1 #01.cbr
- `    5 MB`  The Authority/v1 (1999)/The Authority v1 #01.cbr

### authority — v2 — #10  — identical size  *(volume)*

- `    7 MB`  Warren Ellis/The Authority/v2 (2003)/The Authority v2 #10.cbr
- `    7 MB`  The Authority/v2 (2003)/The Authority v2 #10.cbr

### promethea — #026  — identical size  *(issue)*

- `    7 MB`  Alan Moore/Alan Moore Essentials/Alan Moore 2005- Promethea/Promethea #026.cbz
- `    7 MB`  Alan Moore/Alan Moore Collection IV-  America's Best Comics/Promethea/Promethea/Promethea #026.cbz

### fridayth bloodbath — #01  *(issue)*

- `   12 MB`  Friday the 13th/Friday The 13th - Bloodbath (Avatar)/Friday the 13th - Bloodbath 01 (2005) (Oroboros-DCP).cbr
- `    2 MB`  Friday the 13th/Friday The 13th - Bloodbath (Avatar)/covers/Friday the 13th - Bloodbath 01 (2006) (Platinum Foil Cover) (Oroboros-DCP).cbr
- `    1 MB`  Friday the 13th/Friday The 13th - Bloodbath (Avatar)/covers/Friday the 13th - Bloodbath 01 (2006) (Unstoppable Cover) (Oroboros-DCP).cbr

### authority — v2 — #09  — identical size  *(volume)*

- `    7 MB`  Warren Ellis/The Authority/v2 (2003)/The Authority v2 #09.cbz
- `    7 MB`  The Authority/v2 (2003)/The Authority v2 #09.cbz

### captain atom armageddon — #5  — identical size  *(issue)*

- `    7 MB`  Warren Ellis/The Authority/v3.9 Captain Atom- Armageddon/Captain Atom - Armageddon 5.cbr
- `    7 MB`  The Authority/v3.9 Captain Atom- Armageddon/Captain Atom - Armageddon 5.cbr

### star trek tng last generation — #03  *(issue)*

- `   14 MB`  Star Trek/Star Trek TNG - Last Generation (001-005)(2008-2009)/Star Trek TNG - The Last Generation 03 (of 5) (2009) (c2c) (GreenGiant-DCP).cbr
- `    1 MB`  Star Trek/Star Trek TNG - Last Generation (001-005)(2008-2009)/Star Trek TNG - The Last Generation 03 (of 5) (cover b) (2008) (WildBlueZero).cbr

### authority — v4 — #01  — identical size  *(volume)*

- `    7 MB`  Warren Ellis/The Authority/v4 (2006)/The Authority v4 #01.cbr
- `    7 MB`  The Authority/v4 (2006)/The Authority v4 #01.cbr

### captain atom armageddon — #6  — identical size  *(issue)*

- `    7 MB`  Warren Ellis/The Authority/v3.9 Captain Atom- Armageddon/Captain Atom - Armageddon 6.cbr
- `    7 MB`  The Authority/v3.9 Captain Atom- Armageddon/Captain Atom - Armageddon 6.cbr

### authority — v1 — #20  — identical size  *(volume)*

- `    7 MB`  Warren Ellis/The Authority/v1 (1999)/The Authority v1 #20.cbr
- `    7 MB`  The Authority/v1 (1999)/The Authority v1 #20.cbr

### fridayth bloodbath — #02  *(issue)*

- `   12 MB`  Friday the 13th/Friday The 13th - Bloodbath (Avatar)/Friday the 13th - Bloodbath 02 (2005) (Oroboros-DCP).cbr
- `    1 MB`  Friday the 13th/Friday The 13th - Bloodbath (Avatar)/covers/Friday the 13th - Bloodbath 02 (2006) (Die Cut Cover) (Oroboros-DCP).cbr
- `    1 MB`  Friday the 13th/Friday The 13th - Bloodbath (Avatar)/covers/Friday the 13th - Bloodbath 02 (2006) (Platinum Foil Cover) (Oroboros-DCP).cbr

### doom patrol — v2 — #081  — identical size  *(volume)*

- `    7 MB`  Ted McKeever (Collection) (1987-2007)/1994 - Doom Patrol (Vertigo - w Rachael Pollack)/Doom Patrol v2 081 (Two Mad Men With Foreheads And Boots).cbz
- `    7 MB`  Grant Morrison/Comics/Doom Patrol/Doom Patrol v2 081 (Two Mad Men With Foreheads And Boots).cbz

### authority — v2 — #11  — identical size  *(volume)*

- `    7 MB`  Warren Ellis/The Authority/v2 (2003)/The Authority v2 #11.cbr
- `    7 MB`  The Authority/v2 (2003)/The Authority v2 #11.cbr

### near myths — #5  — identical size  *(issue)*

- `    7 MB`  Grant Morrison/Near Myths (Grant Morrison)/Near Myths #5 - The Checkmate Man.cbr
- `    7 MB`  Grant Morrison/Comics/Near Myths (Galaxy 1978)/Near Myths #5 - The Checkmate Man.cbr

### authority — v1 — #04  — identical size  *(volume)*

- `    5 MB`  Warren Ellis/The Authority/v1 (1999)/The Authority v1 #04.cbr
- `    5 MB`  Warren Ellis/1999/1999 The Authority/The Authority v1 #04.cbr
- `    5 MB`  The Authority/v1 (1999)/The Authority v1 #04.cbr

### price ernie pikea — #01  — identical size  *(issue)*

- `    7 MB`  YU stripovi 2019/Korto (YU)/Price Ernie Pikea - 01 - neobicna avantura.cbr
- `    7 MB`  Corto Maltese/Price Ernie Pikea - 01 - neobicna avantura.cbr

### authority — v1 — #07  — identical size  *(volume)*

- `    4 MB`  Warren Ellis/The Authority/v1 (1999)/The Authority v1 #07.cbr
- `    4 MB`  Warren Ellis/1999/1999 The Authority/The Authority v1 #07.cbr
- `    4 MB`  The Authority/v1 (1999)/The Authority v1 #07.cbr

### authority — v1 — #08  — identical size  *(volume)*

- `    4 MB`  Warren Ellis/The Authority/v1 (1999)/The Authority v1 #08.cbr
- `    4 MB`  Warren Ellis/1999/1999 The Authority/The Authority v1 #08.cbr
- `    4 MB`  The Authority/v1 (1999)/The Authority v1 #08.cbr

### doom patrol — v2 — #085  — identical size  *(volume)*

- `    7 MB`  Ted McKeever (Collection) (1987-2007)/1994 - Doom Patrol (Vertigo - w Rachael Pollack)/Doom Patrol v2 085 (Imagine Ari's Friend pt 2 - Gates Of Light).cbz
- `    7 MB`  Grant Morrison/Comics/Doom Patrol/Doom Patrol v2 085 (Imagine Ari's Friend pt 2 - Gates Of Light).cbz

### doom patrol — v2 — #087  — identical size  *(volume)*

- `    7 MB`  Ted McKeever (Collection) (1987-2007)/1994 - Doom Patrol (Vertigo - w Rachael Pollack)/Doom Patrol v2 087 (Imagine Ari's Friend pt 4 - A Cry For The Great Face).cbz
- `    7 MB`  Grant Morrison/Comics/Doom Patrol/Doom Patrol v2 087 (Imagine Ari's Friend pt 4 - A Cry For The Great Face).cbz

### doom patrol — v2 — #084  — identical size  *(volume)*

- `    6 MB`  Ted McKeever (Collection) (1987-2007)/1994 - Doom Patrol (Vertigo - w Rachael Pollack)/Doom Patrol v2 084 (Imagine Ari's Friend pt 1 - A Song For The Small Face).cbr
- `    6 MB`  Grant Morrison/Comics/Doom Patrol/Doom Patrol v2 084 (Imagine Ari's Friend pt 1 - A Song For The Small Face).cbr

### authority — v1 — #05  — identical size  *(volume)*

- `    4 MB`  Warren Ellis/The Authority/v1 (1999)/The Authority v1 #05.cbr
- `    4 MB`  Warren Ellis/1999/1999 The Authority/The Authority v1 #05.cbr
- `    4 MB`  The Authority/v1 (1999)/The Authority v1 #05.cbr

### doom patrol — v2 — #082  — identical size  *(volume)*

- `    6 MB`  Ted McKeever (Collection) (1987-2007)/1994 - Doom Patrol (Vertigo - w Rachael Pollack)/Doom Patrol v2 082 (A Swaying Nipple And A Shower Of Gold).cbr
- `    6 MB`  Grant Morrison/Comics/Doom Patrol/Doom Patrol v2 082 (A Swaying Nipple And A Shower Of Gold).cbr

### fridayth bloodbath — #03  *(issue)*

- `   12 MB`  Friday the 13th/Friday The 13th - Bloodbath (Avatar)/Friday the 13th - Bloodbath 03 (2006) (Jormungand-DCP).cbr
- `    1 MB`  Friday the 13th/Friday The 13th - Bloodbath (Avatar)/covers/Friday the 13th - Bloodbath 03 (2006) (Platinum Foil Cover) (Oroboros-DCP).cbr

### authority — v1 — #03  — identical size  *(volume)*

- `    4 MB`  Warren Ellis/The Authority/v1 (1999)/The Authority v1 #03.cbr
- `    4 MB`  Warren Ellis/1999/1999 The Authority/The Authority v1 #03.cbr
- `    4 MB`  The Authority/v1 (1999)/The Authority v1 #03.cbr

### authority — v1 — #02  — identical size  *(volume)*

- `    4 MB`  Warren Ellis/The Authority/v1 (1999)/The Authority v1 #02.cbr
- `    4 MB`  Warren Ellis/1999/1999 The Authority/The Authority v1 #02.cbr
- `    4 MB`  The Authority/v1 (1999)/The Authority v1 #02.cbr

### authority — v1 — #06  — identical size  *(volume)*

- `    4 MB`  Warren Ellis/The Authority/v1 (1999)/The Authority v1 #06.cbr
- `    4 MB`  Warren Ellis/1999/1999 The Authority/The Authority v1 #06.cbr
- `    4 MB`  The Authority/v1 (1999)/The Authority v1 #06.cbr

### near myths — #3  — identical size  *(issue)*

- `    6 MB`  Grant Morrison/Near Myths (Grant Morrison)/Near Myths #3 - Gideon Stargrave.cbr
- `    6 MB`  Grant Morrison/Comics/Near Myths (Galaxy 1978)/Near Myths #3 - Gideon Stargrave.cbr

### 219 funeral for a friend poster mag  — identical size  *(issue)*

- `    6 MB`  Judge Dredd The Megazine/Judge Dredd Megazine v5 (201-400)(2002-ongoing)/J.D Megazine Supplements/219 - Funeral for a Friend Poster Mag (Zeg).cbr
- `    6 MB`  Judge Dredd The Megazine/J.D Megazine Supplements/219 - Funeral for a Friend Poster Mag (Zeg).cbr

### bone happy halloween  *(issue)*

- `    6 MB`  Bone/Bone - Happy Halloween (2008) (c2c) (Team-DCP).cbr
- `    6 MB`  Bone/Bone - Happy Halloween (2010) (GreenGiant-DCP).cbr

### vampirella shi — #01  — identical size  *(issue)*

- `    6 MB`  Warren Ellis/Warren Ellis - Vampirella, Shi, Dracula/Vampirella - Shi 01.cbr
- `    6 MB`  Warren Ellis/1997/Vampirella/Vampirella - Shi 01.cbr

### spawn — #008  — identical size  *(issue)*

- `    6 MB`  Alan Moore/Spawn/Spawn 008.cbr
- `    6 MB`  Alan Moore/Alan Moore Collection III-  Image - Awesome Comics/Spawn/Spawn (ongoing series)/Spawn #008.cbr

### promethea — #001  — identical size  *(issue)*

- `    6 MB`  Alan Moore/Alan Moore Essentials/Alan Moore 2005- Promethea/Promethea #001.cbr
- `    6 MB`  Alan Moore/Alan Moore Collection IV-  America's Best Comics/Promethea/Promethea/Promethea #001.cbr

### authority — v1 — #22  — identical size  *(volume)*

- `    6 MB`  Warren Ellis/The Authority/v1 (1999)/The Authority v1 #22.cbr
- `    6 MB`  The Authority/v1 (1999)/The Authority v1 #22.cbr

### promethea — #004  — identical size  *(issue)*

- `    6 MB`  Alan Moore/Alan Moore Essentials/Alan Moore 2005- Promethea/Promethea #004.cbr
- `    6 MB`  Alan Moore/Alan Moore Collection IV-  America's Best Comics/Promethea/Promethea/Promethea #004.cbr

### promethea — #003  — identical size  *(issue)*

- `    5 MB`  Alan Moore/Alan Moore Essentials/Alan Moore 2005- Promethea/Promethea #003.cbr
- `    5 MB`  Alan Moore/Alan Moore Collection IV-  America's Best Comics/Promethea/Promethea/Promethea #003.cbr

### fridayth jason vs jason x — #01  *(issue)*

- `   10 MB`  Friday the 13th/Friday The 13th - Jason Vs Jason X (Avatar)/Friday the 13th - Jason vs Jason X 01 (2006) (Jormungand-DCP).cbr
- `    1 MB`  Friday the 13th/Friday The 13th - Jason Vs Jason X (Avatar)/covers/Friday the 13th - Jason Vs Jason X 01 (2006) (Face Off Cover) (Oroboros-DCP).cbr

### promethea — #012  — identical size  *(issue)*

- `    5 MB`  Alan Moore/Alan Moore Essentials/Alan Moore 2005- Promethea/Promethea #012.cbr
- `    5 MB`  Alan Moore/Alan Moore Collection IV-  America's Best Comics/Promethea/Promethea/Promethea #012.cbr

### promethea — #015  — identical size  *(issue)*

- `    5 MB`  Alan Moore/Alan Moore Essentials/Alan Moore 2005- Promethea/Promethea #015.cbr
- `    5 MB`  Alan Moore/Alan Moore Collection IV-  America's Best Comics/Promethea/Promethea/Promethea #015.cbr

### promethea — #008  — identical size  *(issue)*

- `    5 MB`  Alan Moore/Alan Moore Essentials/Alan Moore 2005- Promethea/Promethea #008.cbr
- `    5 MB`  Alan Moore/Alan Moore Collection IV-  America's Best Comics/Promethea/Promethea/Promethea #008.cbr

### promethea — #014  — identical size  *(issue)*

- `    5 MB`  Alan Moore/Alan Moore Essentials/Alan Moore 2005- Promethea/Promethea #014.cbr
- `    5 MB`  Alan Moore/Alan Moore Collection IV-  America's Best Comics/Promethea/Promethea/Promethea #014.cbr

### globetrotting for agoraphobiacs  *(issue)*

- `    8 MB`  Alan Moore/Alan Moore Collection VI- Made For Moore/Globetrotting For Agoraphobiacs (From Eddie Campbell's Bacchus #056).cbr
- `    2 MB`  Alan Moore/Alan Moore Collection VII- Unknown/Globetrotting For Agoraphobiacs (Knockabout #009).cbr

### promethea — #006  — identical size  *(issue)*

- `    5 MB`  Alan Moore/Alan Moore Essentials/Alan Moore 2005- Promethea/Promethea #006.cbr
- `    5 MB`  Alan Moore/Alan Moore Collection IV-  America's Best Comics/Promethea/Promethea/Promethea #006.cbr

### near myths — #2  — identical size  *(issue)*

- `    5 MB`  Grant Morrison/Near Myths (Grant Morrison)/Near Myths #2 - Time Is A Four Lettered Word.cbr
- `    5 MB`  Grant Morrison/Comics/Near Myths (Galaxy 1978)/Near Myths #2 - Time Is A Four Lettered Word.cbr

### promethea — #010  — identical size  *(issue)*

- `    5 MB`  Alan Moore/Alan Moore Essentials/Alan Moore 2005- Promethea/Promethea #010.cbr
- `    5 MB`  Alan Moore/Alan Moore Collection IV-  America's Best Comics/Promethea/Promethea/Promethea #010.cbr

### promethea — #005  — identical size  *(issue)*

- `    5 MB`  Alan Moore/Alan Moore Essentials/Alan Moore 2005- Promethea/Promethea #005.cbr
- `    5 MB`  Alan Moore/Alan Moore Collection IV-  America's Best Comics/Promethea/Promethea/Promethea #005.cbr

### promethea — #009  — identical size  *(issue)*

- `    5 MB`  Alan Moore/Alan Moore Essentials/Alan Moore 2005- Promethea/Promethea #009.cbr
- `    5 MB`  Alan Moore/Alan Moore Collection IV-  America's Best Comics/Promethea/Promethea/Promethea #009.cbr

### promethea — #007  — identical size  *(issue)*

- `    5 MB`  Alan Moore/Alan Moore Essentials/Alan Moore 2005- Promethea/Promethea #007.cbr
- `    5 MB`  Alan Moore/Alan Moore Collection IV-  America's Best Comics/Promethea/Promethea/Promethea #007.cbr

### locke & key art gallery  — identical size  *(issue)*

- `    5 MB`  Locke & Key/Locke & Key - Extras/Locke & Key - Art Gallery.cbr
- `    5 MB`  Locke & Key/Locke & Key - Extras/Locke & Key - Art Gallery (2008) (Digital) (G85-Empire).cbr

### promethea — #019  — identical size  *(issue)*

- `    5 MB`  Alan Moore/Alan Moore Essentials/Alan Moore 2005- Promethea/Promethea #019.cbr
- `    5 MB`  Alan Moore/Alan Moore Collection IV-  America's Best Comics/Promethea/Promethea/Promethea #019.cbr

### sir edward grey, witchfinder murderous intent  *(issue)*

- `    8 MB`  Hellboy/5.)  Sir Edward Grey, Witchfinder - Murderous Intent  (1879 AD)/Sir Edward Grey, Witchfinder - Murderous Intent.cbr
- `    1 MB`  Sir Edward Grey, Witchfinder (Collection) (2009-2014) GetComics.INFO/Sir Edward Grey, Witchfinder (00) - Murderous Intent (2008) (from MySpace DHP 16) (digital).cbr

### promethea — #013  — identical size  *(issue)*

- `    4 MB`  Alan Moore/Alan Moore Essentials/Alan Moore 2005- Promethea/Promethea #013.cbr
- `    4 MB`  Alan Moore/Alan Moore Collection IV-  America's Best Comics/Promethea/Promethea/Promethea #013.cbr

### promethea — #025  — identical size  *(issue)*

- `    4 MB`  Alan Moore/Alan Moore Essentials/Alan Moore 2005- Promethea/Promethea #025.cbr
- `    4 MB`  Alan Moore/Alan Moore Collection IV-  America's Best Comics/Promethea/Promethea/Promethea #025.cbr

### promethea — #016  — identical size  *(issue)*

- `    4 MB`  Alan Moore/Alan Moore Essentials/Alan Moore 2005- Promethea/Promethea #016.cbr
- `    4 MB`  Alan Moore/Alan Moore Collection IV-  America's Best Comics/Promethea/Promethea/Promethea #016.cbr

### promethea — #002  — identical size  *(issue)*

- `    4 MB`  Alan Moore/Alan Moore Essentials/Alan Moore 2005- Promethea/Promethea #002.cbr
- `    4 MB`  Alan Moore/Alan Moore Collection IV-  America's Best Comics/Promethea/Promethea/Promethea #002.cbr

### promethea — #017  — identical size  *(issue)*

- `    4 MB`  Alan Moore/Alan Moore Essentials/Alan Moore 2005- Promethea/Promethea #017.cbr
- `    4 MB`  Alan Moore/Alan Moore Collection IV-  America's Best Comics/Promethea/Promethea/Promethea #017.cbr

### vampirella dracula centennial, necromance  — identical size  *(issue)*

- `    4 MB`  Warren Ellis/Warren Ellis - Vampirella, Shi, Dracula/Vampirella Dracula - The Centennial, Necromance.cbr
- `    4 MB`  Warren Ellis/1997/Vampirella/Vampirella Dracula - The Centennial, Necromance.cbr

### promethea — #022  — identical size  *(issue)*

- `    4 MB`  Alan Moore/Alan Moore Essentials/Alan Moore 2005- Promethea/Promethea #022.cbr
- `    4 MB`  Alan Moore/Alan Moore Collection IV-  America's Best Comics/Promethea/Promethea/Promethea #022.cbr

### promethea — #023  — identical size  *(issue)*

- `    4 MB`  Alan Moore/Alan Moore Essentials/Alan Moore 2005- Promethea/Promethea #023.cbr
- `    4 MB`  Alan Moore/Alan Moore Collection IV-  America's Best Comics/Promethea/Promethea/Promethea #023.cbr

### tom strong — #019  — identical size  *(issue)*

- `    4 MB`  Alan Moore/Alan Moore Essentials/Alan Moore 2006- Tom Strong/Tom Strong/Tom Strong #019.cbz
- `    4 MB`  Alan Moore/Alan Moore Collection IV-  America's Best Comics/Tom Strong/Tom Strong/Tom Strong #019.cbz

### promethea — #018  — identical size  *(issue)*

- `    4 MB`  Alan Moore/Alan Moore Essentials/Alan Moore 2005- Promethea/Promethea #018.cbr
- `    4 MB`  Alan Moore/Alan Moore Collection IV-  America's Best Comics/Promethea/Promethea/Promethea #018.cbr

### promethea — #021  — identical size  *(issue)*

- `    4 MB`  Alan Moore/Alan Moore Essentials/Alan Moore 2005- Promethea/Promethea #021.cbr
- `    4 MB`  Alan Moore/Alan Moore Collection IV-  America's Best Comics/Promethea/Promethea/Promethea #021.cbr

### promethea — #024  — identical size  *(issue)*

- `    4 MB`  Alan Moore/Alan Moore Essentials/Alan Moore 2005- Promethea/Promethea #024.cbr
- `    4 MB`  Alan Moore/Alan Moore Collection IV-  America's Best Comics/Promethea/Promethea/Promethea #024.cbr

### tom strong — #020  — identical size  *(issue)*

- `    3 MB`  Alan Moore/Alan Moore Essentials/Alan Moore 2006- Tom Strong/Tom Strong/Tom Strong #020.cbz
- `    3 MB`  Alan Moore/Alan Moore Collection IV-  America's Best Comics/Tom Strong/Tom Strong/Tom Strong #020.cbz

### promethea — #020  — identical size  *(issue)*

- `    3 MB`  Alan Moore/Alan Moore Essentials/Alan Moore 2005- Promethea/Promethea #020.cbr
- `    3 MB`  Alan Moore/Alan Moore Collection IV-  America's Best Comics/Promethea/Promethea/Promethea #020.cbr

### vampirella dracula showcase  — identical size  *(issue)*

- `    3 MB`  Warren Ellis/Warren Ellis - Vampirella, Shi, Dracula/Vampirella Dracula - Showcase.cbr
- `    3 MB`  Warren Ellis/1997/Vampirella/Vampirella Dracula - Showcase.cbr

### powers scriptbook first script only  *(issue)*

- `    3 MB`  Powers/Powers Scriptbook-First Script Only.cbr
- `    3 MB`  Powers/Extras/powers scriptbook first script only.cbr

### promethea — #011  — identical size  *(issue)*

- `    3 MB`  Alan Moore/Alan Moore Essentials/Alan Moore 2005- Promethea/Promethea #011.cbr
- `    3 MB`  Alan Moore/Alan Moore Collection IV-  America's Best Comics/Promethea/Promethea/Promethea #011.cbr

### hit girl — #01  *(issue)*

- `    2 MB`  Mark Millar/Kick-Ass (v1-v3+)(2008-2014)(digital+)/Hit Girl (001-005+)(2012-2013)(digital)(Zone-Empire)/Variant Covers/Hit-Girl 01 (2012) (Forbidden Planet.Com Variant) (Cover ONLY) (ScanDog+ArtNet).cbz
- `    1 MB`  Mark Millar/Kick-Ass (v1-v3+)(2008-2014)(digital+)/Hit Girl (001-005+)(2012-2013)(digital)(Zone-Empire)/Variant Covers/Hit-Girl 01 (2012) (Phil Noto Variant) (Cover ONLY) (ScanDog+ArtNet).cbz
- `    1 MB`  Mark Millar/Kick-Ass (v1-v3+)(2008-2014)(digital+)/Hit Girl (001-005+)(2012-2013)(digital)(Zone-Empire)/Variant Covers/Hit-Girl 01 (2012) (3rd Printing Variant) (Cover ONLY) (ScanDog).cbr
- `    1 MB`  Mark Millar/Kick-Ass (v1-v3+)(2008-2014)(digital+)/Hit Girl (001-005+)(2012-2013)(digital)(Zone-Empire)/Variant Covers/Hit-Girl 01 (2012) (John Romita Jr. Sketch Variant) (Cover ONLY) (ScanDog+ArtNet).cbz
- `    0 MB`  Mark Millar/Kick-Ass (v1-v3+)(2008-2014)(digital+)/Hit Girl (001-005+)(2012-2013)(digital)(Zone-Empire)/Variant Covers/Hit-Girl 01 (2012) (Blank Cover Variant) (Cover ONLY) (ScanDog+ArtNet).cbz

### new avengers finale — #01  *(issue)*

- `    2 MB`  Alias  ( Jessica Jones , The Pulse & Appearances)/Appearances/New Avengers Finale/New Avengers Finale 01 (2010) (2nd Printing Unmasked Variant) (Cover ONLY) (ScanDog & GG-DCP).cbr
- `    2 MB`  Alias  ( Jessica Jones , The Pulse & Appearances)/Appearances/New Avengers Finale/New Avengers Finale 01 (2010) (2nd Printing Battle Ready Variant) (Cover ONLY) (ScanDog & GG-DCP).cbr

### black summer alpha  *(issue)*

- `    2 MB`  Warren Ellis/2007/2007 Black Summer/Black Summer Alpha (Wrap Cover Only).cbr
- `    1 MB`  Warren Ellis/2007/2007 Black Summer/Black Summer Alpha (Poster Cover Only).cbr
- `    1 MB`  Warren Ellis/2007/2007 Black Summer/Black Summer Alpha (Cover Only).cbr

### hit girl — #04  *(issue)*

- `    1 MB`  Mark Millar/Kick-Ass (v1-v3+)(2008-2014)(digital+)/Hit Girl (001-005+)(2012-2013)(digital)(Zone-Empire)/Variant Covers/Hit-Girl 04 (2012) (Geof Darrow Variant) (Cover ONLY) (ScanDog+ArtNet).cbz
- `    1 MB`  Mark Millar/Kick-Ass (v1-v3+)(2008-2014)(digital+)/Hit Girl (001-005+)(2012-2013)(digital)(Zone-Empire)/Variant Covers/Hit-Girl 04 (2012) (John Romita Jr. Sketch Variant) (Cover ONLY) (ScanDog+ArtNet).cbz

### hit girl — #05  *(issue)*

- `    1 MB`  Mark Millar/Kick-Ass (v1-v3+)(2008-2014)(digital+)/Hit Girl (001-005+)(2012-2013)(digital)(Zone-Empire)/Variant Covers/Hit-Girl 05 (2013) (John Romita Jr. Sketch Variant) (Cover ONLY) (ScanDog+ArtNet).cbz
- `    1 MB`  Mark Millar/Kick-Ass (v1-v3+)(2008-2014)(digital+)/Hit Girl (001-005+)(2012-2013)(digital)(Zone-Empire)/Variant Covers/Hit-Girl 05 (2013) (Bill Sienkiewicz Variant) (Cover ONLY) (ScanDog+ArtNet).cbz

### hit girl — #03  *(issue)*

- `    1 MB`  Mark Millar/Kick-Ass (v1-v3+)(2008-2014)(digital+)/Hit Girl (001-005+)(2012-2013)(digital)(Zone-Empire)/Variant Covers/Hit-Girl 03 (2012) (John Romita Jr. Sketch Variant) (Cover ONLY) (ScanDog+ArtNet).cbz
- `    1 MB`  Mark Millar/Kick-Ass (v1-v3+)(2008-2014)(digital+)/Hit Girl (001-005+)(2012-2013)(digital)(Zone-Empire)/Variant Covers/Hit-Girl 03 (2012) (Jock Variant)(Cover ONLY) (ScanDog+ArtNet).cbz

### civil war — #002  *(issue)*

- `    1 MB`  Civil War Event (001-007+Tie-Ins,Trades&Extras)(2006-2008)(digital)/Extras/Variants/Civil War 002 (2006) (2 variants) (Ori-DCP).cbr
- `    1 MB`  Civil War Event (001-007+Tie-Ins,Trades&Extras)(2006-2008)(digital)/Extras/Variants/Civil War 002 (2006) (3rd Printing Variant) (Ori-DCP).cbr

### civil war — #003  *(issue)*

- `    1 MB`  Civil War Event (001-007+Tie-Ins,Trades&Extras)(2006-2008)(digital)/Extras/Variants/Civil War 003 (2006) (2 variants) (Ori-DCP).cbr
- `    0 MB`  Civil War Event (001-007+Tie-Ins,Trades&Extras)(2006-2008)(digital)/Extras/Variants/Civil War 003 (2006) (Sketch Variant) (Ori-DCP).cbr

### spider man noir eyes without a face — #03  — identical size  *(issue)*

- `    1 MB`  GG Studio (Collection) (2010-2012)/Marvel Noir (2009-2011)(digital)/Spider-Man Noir (v1-v2+)(2009-2010)(digital)/Variant Covers/Spider-Man Noir - Eyes Without a Face 03 (2010) (Variant Cover Only) [extracted] (Minutemen-DTs).cbr
- `    1 MB`  Aster Blistok/Le Vagabond des Limbes/Spider-Man Noir (v1-v2+)(2009-2010)(digital)/Variant Covers/Spider-Man Noir - Eyes Without a Face 03 (2010) (Variant Cover Only) [extracted] (Minutemen-DTs).cbr

### civil war — #007  *(issue)*

- `    1 MB`  Civil War Event (001-007+Tie-Ins,Trades&Extras)(2006-2008)(digital)/Extras/Variants/Civil War 007 (2007) (Michael Turner Variant) (Ori-DCP).cbr
- `    0 MB`  Civil War Event (001-007+Tie-Ins,Trades&Extras)(2006-2008)(digital)/Extras/Variants/Civil War 007 (2007) (Michael Turner Sketch Variant) (Ori-DCP).cbr

### spider man noir eyes without a face — #04  — identical size  *(issue)*

- `    1 MB`  GG Studio (Collection) (2010-2012)/Marvel Noir (2009-2011)(digital)/Spider-Man Noir (v1-v2+)(2009-2010)(digital)/Variant Covers/Spider-Man Noir - Eyes Without a Face 04 (2010) (Variant Cover Only) [extracted] (Minutemen-DTs).cbr
- `    1 MB`  Aster Blistok/Le Vagabond des Limbes/Spider-Man Noir (v1-v2+)(2009-2010)(digital)/Variant Covers/Spider-Man Noir - Eyes Without a Face 04 (2010) (Variant Cover Only) [extracted] (Minutemen-DTs).cbr

### spider man noir eyes without a face — #01  — identical size  *(issue)*

- `    1 MB`  GG Studio (Collection) (2010-2012)/Marvel Noir (2009-2011)(digital)/Spider-Man Noir (v1-v2+)(2009-2010)(digital)/Variant Covers/Spider-Man Noir - Eyes Without a Face 01 (2010) (Variant Cover Only) [extracted] (Minutemen-DTs).cbr
- `    1 MB`  Aster Blistok/Le Vagabond des Limbes/Spider-Man Noir (v1-v2+)(2009-2010)(digital)/Variant Covers/Spider-Man Noir - Eyes Without a Face 01 (2010) (Variant Cover Only) [extracted] (Minutemen-DTs).cbr

### miracle man triumphant  — identical size  *(issue)*

- `    1 MB`  Miracleman/Miracle Man Triumphant.cbr
- `    1 MB`  Alan Moore/Alan Moore Collection I- English Invasion/Alan Moore Collection III- 2000 AD/Miracleman/Miracleman- Extras/Miracle Man Triumphant (3 Pages).cbr

### civil war — #001  *(issue)*

- `    0 MB`  Civil War Event (001-007+Tie-Ins,Trades&Extras)(2006-2008)(digital)/Extras/Variants/Civil War 001 (Turner Sketch Variant) (2006) (Nero-DCP).cbr
- `    0 MB`  Civil War Event (001-007+Tie-Ins,Trades&Extras)(2006-2008)(digital)/Extras/Variants/Civil War 001 (Turner Variant) (2006) (Nero-DCP).cbr

### spider man noir eyes without a face — #02  — identical size  *(issue)*

- `    0 MB`  GG Studio (Collection) (2010-2012)/Marvel Noir (2009-2011)(digital)/Spider-Man Noir (v1-v2+)(2009-2010)(digital)/Variant Covers/Spider-Man Noir - Eyes Without a Face 02 (2010) (Variant Cover Only) [extracted] (Minutemen-DTs).cbr
- `    0 MB`  Aster Blistok/Le Vagabond des Limbes/Spider-Man Noir (v1-v2+)(2009-2010)(digital)/Variant Covers/Spider-Man Noir - Eyes Without a Face 02 (2010) (Variant Cover Only) [extracted] (Minutemen-DTs).cbr

---

## Check these by hand — 468 groups, 72.34 GB

Something here disagrees that the parser could not see: an issue number, a
subtitle, a `(Cover ONLY)` tag, or a folder claiming a different volume. That
usually means these are **different books that parse to the same key**, not
duplicates — `Terra Obscura Volume 1/#003` and `Volume 2/#003`, or
`Starhenge Book Two ... 01` and `... 03`. Read the names before touching
anything.

### woods  *(annual)*

- ` 1.25 GB`  The Woods (2019) /The Woods Yearbook Edition Book 03 (2019) (Digital) (DR & Quinch-Empire).cbr
- ` 1.17 GB`  The Woods (2019) /The Woods Yearbook Edition Book 02 (2019) (Digital) (DR & Quinch-Empire).cbr
- ` 1.16 GB`  The Woods (2019) /The Woods Yearbook Edition Book 01 (2019) (Digital) (DR & Quinch-Empire).cbr

### heavy metal  *(special)*

- `  147 MB`  Heavy Metal/02. Specials/Heavy Metal Special Edition v11 01 (1997) (null-DCP).cbz
- `  135 MB`  Heavy Metal/02. Specials/Heavy Metal Special Edition v09 02 (1995) (null-DCP).cbz
- `  130 MB`  Heavy Metal/02. Specials/Heavy Metal Special Edition v09 01 (1995) (null-DCP).cbz
- `  114 MB`  Heavy Metal/02. Specials/Heavy Metal Special Edition v11 02 (1997) (20 Years Special).cbz
- `   86 MB`  Heavy Metal/02. Specials/Heavy Metal Special Edition v13 03 (1999) (Techno Special) (c2c) (Lazarus-DCP).cbz
- `   85 MB`  Heavy Metal/02. Specials/Heavy Metal Special Edition v12 02 (1998) (The Best of Corben Special) (c2c) (Lazarus-DCP).cbz
- `   85 MB`  Heavy Metal/02. Specials/Heavy Metal Special Edition v22 03 (2008) (Eerie Special) (svengali-DCP).cbz
- `   81 MB`  Heavy Metal/02. Specials/Heavy Metal Special Edition v06 04 Fifteen Years Of Heavy Metal.cbr
- `   80 MB`  Heavy Metal/02. Specials/Heavy Metal Special Edition v12 01 (1998) (Sci-Fi Special) (c2c) (Lazarus-DCP).cbz
- `   77 MB`  Heavy Metal/02. Specials/Heavy Metal Special Edition v17 02 (2003) (Fantasy Issue) (svengali-DCP).cbz
- `   73 MB`  Heavy Metal/02. Specials/Heavy Metal Special Edition v01 03 (2003) (Cryptic Issue) (svengali-DCP).cbz
- `   72 MB`  Heavy Metal/02. Specials/Heavy Metal Special Edition v17 03 (2003) (Sorcery Issue) (svengali-DCP).cbz
- `   71 MB`  Heavy Metal/02. Specials/Heavy Metal Special Edition v18 03 (2004) (Sirens Special) (c2c) (svengali-DCP).cbr
- `   71 MB`  Heavy Metal/02. Specials/Heavy Metal Special Edition v15 01 (2001) (Taboo Special) (Humperdido).cbr
- `   69 MB`  Heavy Metal/02. Specials/Heavy Metal Special Edition v17 01 (2003) (Samurai Special) (svengali-DCP).cbz
- `   69 MB`  Heavy Metal/02. Specials/Heavy Metal Special Edition v14 01 (2000) (Erotic Special).cbr
- `   69 MB`  Heavy Metal/02. Specials/Heavy Metal Special Edition v22 02 (2008) Overload Special (c2c) (Minutemen-Nobody).cbr
- `   67 MB`  Heavy Metal/02. Specials/Heavy Metal Special Edition v18 02 (2004) (Adventure Special) (svengali-DCP).cbr
- `   67 MB`  Heavy Metal/02. Specials/Heavy Metal Special Edition v13 02 (1999) (F.A.K.K. 2 Movie Special) (BiggyBoy).cbz
- `   65 MB`  Heavy Metal/02. Specials/Heavy Metal Special Edition v19 01 (2005) (Middle Earth Special) (svengali-DCP).cbz
- `   65 MB`  Heavy Metal/02. Specials/Heavy Metal Special Edition v16 03 (2002) (25th Anniversary Special).cbr
- `   64 MB`  Heavy Metal/02. Specials/Heavy Metal Special Edition v21 01 (2007) (Genesis Special) (svengali-DCP).cbz
- `   63 MB`  Heavy Metal/02. Specials/Heavy Metal Special Edition v18 01 (2004) (Sci-Fi Special) (svengali-DCP).cbr
- `   61 MB`  Heavy Metal/02. Specials/Heavy Metal Special Edition v21 02 (2007) (Upload Special) (svengali-DCP).cbz
- `   55 MB`  Heavy Metal/02. Specials/Heavy Metal Special Edition v19 03 (2005) (Digitized Special) (svengali-DCP).cbz
- `   54 MB`  Heavy Metal/02. Specials/Heavy Metal Special Edition v10 01 (1996) (One Step Beyond) (Humperdido).cbr
- `   54 MB`  Heavy Metal/02. Specials/Heavy Metal Special Edition v15 03 (2001) (Mind Melt Special).cbr
- `   53 MB`  Heavy Metal/02. Specials/Heavy Metal Special Edition v20 02 (2006) (Sky Doll Special) (svengali-DCP).cbz
- `   53 MB`  Heavy Metal/02. Specials/Heavy Metal Special Edition v20 03 (2006) (Halloween Special) (svengali-DCP).cbz
- `   52 MB`  Heavy Metal/02. Specials/Heavy Metal Special Edition v01 01 (2003) (Fantasy Issue) (Humperdido).cbr
- `   52 MB`  Heavy Metal/02. Specials/Heavy Metal Special Edition v07 01 (1993) (Warmachine) (Humperdido).cbr
- `   52 MB`  Heavy Metal/02. Specials/Heavy Metal Special Edition v14 03 (2000) (Fantasy Special).cbr
- `   51 MB`  Heavy Metal/02. Specials/Heavy Metal Special Edition v01 02 (2003) (Sorcery Issue) (Humperdido).cbr
- `   51 MB`  Heavy Metal/02. Specials/Heavy Metal Special Edition v16 01 (2002) (Diabolic Special).cbr
- `   49 MB`  Heavy Metal/02. Specials/Heavy Metal Special Edition v19 02 (2005) (Mystery Special).cbz
- `   48 MB`  Heavy Metal/02. Specials/Heavy Metal Special Edition v16 02 (2002) (Erotica Special).cbr
- `   45 MB`  Heavy Metal/02. Specials/Heavy Metal Special Edition v17 01 - Samurai Special (2003 Spring).cbr
- `   44 MB`  Heavy Metal/02. Specials/Heavy Metal Special Edition v20 01 (2006) (Steam Punk Special).cbz
- `   43 MB`  Heavy Metal/02. Specials/Heavy Metal Special Edition v08 01 (1994) Pin-up (Humperdido).cbr
- `   41 MB`  Heavy Metal/02. Specials/Heavy Metal Special Edition v15 02 (2001) (Poster Special).cbr
- `   40 MB`  Heavy Metal/02. Specials/Heavy Metal Special Edition v22 01 (2008) (Chaos Special) (Minutemen-MAZE).cbr
- `   39 MB`  Heavy Metal/02. Specials/Heavy Metal Special Edition v08 02 (1994) (Greatest Hits) (Humperdido).cbr
- `   38 MB`  Heavy Metal/02. Specials/Heavy Metal Special Edition v10 02 (1996) (Special Edition) (Humperdido).cbr
- `   30 MB`  Heavy Metal/02. Specials/Heavy Metal Special Edition v13 01 (1999) (Crossroads Special).cbr
- `   18 MB`  Heavy Metal/02. Specials/Heavy Metal Special Edition v07 02 (1993) (Software Issue).cbr
- `    0 MB`  Heavy Metal/02. Specials/Heavy Metal Special Edition v14 02 - CD Special (2000-Summer) - Heavy Metal 2000 HyperCD Covers Only.cbr

### harley quinn — v2  *(volume)*

- `  825 MB`  Harley Quinn/Harley Quinn v02 - Friends With Detriments (2026) (digital) (Son of Ultron-Empire).cbr
- `  737 MB`  Harley Quinn/Harley Quinn v02 - Eye Don't Like Me (2024) (digital) (Son of Ultron-Empire).cbr
- `  444 MB`  Harley Quinn/Harley Quinn v02 - Keepsake (2022) (digital).cbz
- `  324 MB`  Harley Quinn/Harley Quinn Vol. 2 (New 52) (v01-v06)(2014-2016)/Harley Quinn v02 - Power Outage (2015) (digital) (Son of Ultron-Empire).cbr
- `  204 MB`  Harley Quinn/Harley Quinn Vol. 3 (Rebirth) – TPB Vol. 1 – 6 (2017-2018)/Harley Quinn (2016-) - v02 Joker Loves Harley.cbr
- `  200 MB`  Harley Quinn/Harley Quinn Vol. 7 (2018-2019)/Harley Quinn v02 - Harley Destroys the Universe (2019) (digital) (Son of Ultron-Empire).cbr

### 2000ad sci fi  *(special)*

- `  209 MB`  2000AD prog/2000AD Sci-Fi Special 2025 (2025) (AI-4320p juvecube).cbz
- `  174 MB`  2000AD - Collections /2000AD Sci-Fi Special 2026 (2026) (4320p) (juvecube).cbz
- `  113 MB`  2000AD prog/2000AD Sci-Fi Special 2020 (2020) (digital) (Minutemen-juvecube).cbr
- `  108 MB`  2000AD prog/2000AD Sci-Fi Special (2019) (Digital-Empire).cbr
- `  102 MB`  2000AD prog/Yearbooks & Specials/Specials/Sci-Fi Special (1977-)/2000AD Sci-Fi Special 2018 (2018) (digital-Empire).cbr
- `  102 MB`  2000AD prog/2000AD Sci-Fi Special (2018) (Digital-Empire).cbr
- `   96 MB`  2000AD prog/Yearbooks & Specials/Specials/Sci-Fi Special (1977-)/2000AD Sci-Fi Special 2015 (2015) (digital-Empire).cbr
- `   96 MB`  2000AD prog/2000AD Sci-Fi Special (2015) (Digital-Empire).cbr
- `   71 MB`  2000AD prog/Yearbooks & Specials/Specials/Sci-Fi Special (1977-)/2000AD Sci-Fi Special 2016 (2016) (digital-Empire).cbr
- `   71 MB`  2000AD prog/2000AD Sci-Fi Special (2016) (Digital-Empire).cbr
- `   67 MB`  2000AD prog/2000AD Sci-Fi Special 2024 (2024)(digital) (Minutemen-juvecube).cbr
- `   66 MB`  2000AD prog/Yearbooks & Specials/Specials/Sci-Fi Special (1977-)/2000AD Sci-Fi Special 2019 (2019) (digital) (Minutemen-juvecube).cbr
- `   66 MB`  2000AD prog/2000AD Sci-Fi Special 2019 (2019) (digital) (Minutemen-juvecube).cbr
- `   61 MB`  2000AD prog/2000AD Sci-Fi Special (2021) (Digital-Empire).cbr
- `   60 MB`  2000AD prog/2000AD Sci-Fi Special 2018 (2018) (digital) (Minutemen-juvecube).cbr
- `   57 MB`  2000AD prog/Yearbooks & Specials/Specials/Sci-Fi Special (1977-)/2000AD Sci-Fi Special 1979 (c2c) (StellarX.Cimmerian32).cbr
- `   41 MB`  2000AD prog/2000AD (Specials, Annuals & Poster Progs + Extras)/2000AD Yearbooks & Specials (1977 - 2013)/Specials (-JJ-)/2000AD Sci-Fi Special (1977 - 1996)/2000AD Sci-Fi Special 1992.cbr
- `   40 MB`  2000AD prog/Yearbooks & Specials/Specials/Sci-Fi Special (1977-)/2000AD Sci-Fi Special 1992 (Reiu-DCP).cbr
- `   38 MB`  2000AD prog/Yearbooks & Specials/Specials/Sci-Fi Special (1977-)/2000AD Sci-Fi Special 1985 (Antscan).cbr
- `   37 MB`  2000AD prog/2000AD (Specials, Annuals & Poster Progs + Extras)/2000AD Yearbooks & Specials (1977 - 2013)/Specials (-JJ-)/2000AD Sci-Fi Special (1977 - 1996)/2000AD Sci-Fi Special 1993.cbr
- `   36 MB`  2000AD prog/Yearbooks & Specials/Specials/Sci-Fi Special (1977-)/2000AD Sci-Fi Special 2014 (2014) (digital) (Nahga-Empire).cbr
- `   36 MB`  2000AD prog/2000AD (Specials, Annuals & Poster Progs + Extras)/2000AD Yearbooks & Specials (1977 - 2013)/Specials (-JJ-)/2000AD Sci-Fi Special (1977 - 1996)/2000AD Sci-Fi Special 1979 - (Tornado Summer Sp).cbr
- `   35 MB`  2000AD prog/Yearbooks & Specials/Specials/Sci-Fi Special (1977-)/2000AD Sci-Fi Special 1996 (Antscan).cbr
- `   34 MB`  2000AD prog/Yearbooks & Specials/Specials/Sci-Fi Special (1977-)/2000AD Sci-Fi Special 1987 (Reiu-DCP).cbr
- `   34 MB`  2000AD prog/2000AD (Specials, Annuals & Poster Progs + Extras)/2000AD Yearbooks & Specials (1977 - 2013)/Specials (-JJ-)/2000AD Sci-Fi Special (1977 - 1996)/2000AD Sci-Fi Special 1994.cbr
- `   33 MB`  2000AD prog/Yearbooks & Specials/Specials/Sci-Fi Special (1977-)/2000AD Sci-Fi Special 1990 (Youngstar)..cbr
- `   32 MB`  2000AD prog/Yearbooks & Specials/Specials/Sci-Fi Special (1977-)/2000AD Sci-Fi Special 1994 (Antscan).cbr
- `   31 MB`  2000AD prog/Yearbooks & Specials/Specials/Sci-Fi Special (1977-)/2000AD Sci-Fi Special 1995 (Judge-Julez).cbr
- `   31 MB`  2000AD prog/2000AD (Specials, Annuals & Poster Progs + Extras)/2000AD Yearbooks & Specials (1977 - 2013)/Specials (-JJ-)/2000AD Sci-Fi Special (1977 - 1996)/2000AD Sci-Fi Special 1995.cbr
- `   30 MB`  2000AD prog/2000AD (Specials, Annuals & Poster Progs + Extras)/2000AD Yearbooks & Specials (1977 - 2013)/Specials (-JJ-)/2000AD Sci-Fi Special (1977 - 1996)/2000AD Sci-Fi Special 1989.cbr
- `   30 MB`  2000AD prog/2000AD (Specials, Annuals & Poster Progs + Extras)/2000AD Yearbooks & Specials (1977 - 2013)/Specials (-JJ-)/2000AD Sci-Fi Special (1977 - 1996)/2000AD Sci-Fi Special 1990.cbr
- `   28 MB`  2000AD prog/2000AD (Specials, Annuals & Poster Progs + Extras)/2000AD Yearbooks & Specials (1977 - 2013)/Specials (-JJ-)/2000AD Sci-Fi Special (1977 - 1996)/2000AD Sci-Fi Special 1985.cbr
- `   26 MB`  2000AD prog/Yearbooks & Specials/Specials/Sci-Fi Special (1977-)/2000AD Sci-Fi Special 1977.cbr
- `   26 MB`  2000AD prog/2000AD (Specials, Annuals & Poster Progs + Extras)/2000AD Yearbooks & Specials (1977 - 2013)/Specials (-JJ-)/2000AD Sci-Fi Special (1977 - 1996)/2000AD Sci-Fi Special 1977 - (2000AD Summer Sp).cbr
- `   25 MB`  2000AD prog/Yearbooks & Specials/Specials/Sci-Fi Special (1977-)/2000AD Sci-Fi Special 1981 (Judge-Julez).cbr
- `   25 MB`  2000AD prog/2000AD (Specials, Annuals & Poster Progs + Extras)/2000AD Yearbooks & Specials (1977 - 2013)/Specials (-JJ-)/2000AD Sci-Fi Special (1977 - 1996)/2000AD Sci-Fi Special 1981.cbr
- `   25 MB`  2000AD prog/2000AD (Specials, Annuals & Poster Progs + Extras)/2000AD Yearbooks & Specials (1977 - 2013)/Specials (-JJ-)/2000AD Sci-Fi Special (1977 - 1996)/2000AD Sci-Fi Special 1996.cbr
- `   24 MB`  2000AD prog/Yearbooks & Specials/Specials/Sci-Fi Special (1977-)/2000AD Sci-Fi Special 1982 (Judge-Julez).cbr
- `   24 MB`  2000AD prog/2000AD (Specials, Annuals & Poster Progs + Extras)/2000AD Yearbooks & Specials (1977 - 2013)/Specials (-JJ-)/2000AD Sci-Fi Special (1977 - 1996)/2000AD Sci-Fi Special 1982.cbr
- `   23 MB`  2000AD prog/2000AD (Specials, Annuals & Poster Progs + Extras)/2000AD Yearbooks & Specials (1977 - 2013)/Specials (-JJ-)/2000AD Sci-Fi Special (1977 - 1996)/2000AD Sci-Fi Special 1984.cbr
- `   23 MB`  2000AD prog/2000AD (Specials, Annuals & Poster Progs + Extras)/2000AD Yearbooks & Specials (1977 - 2013)/Specials (-JJ-)/2000AD Sci-Fi Special (1977 - 1996)/2000AD Sci-Fi Special 1991.cbr
- `   23 MB`  2000AD prog/Yearbooks & Specials/Specials/Sci-Fi Special (1977-)/2000AD Sci-Fi Special 1991 (Ziggyhowie).cbr
- `   22 MB`  2000AD prog/2000AD (Specials, Annuals & Poster Progs + Extras)/2000AD Yearbooks & Specials (1977 - 2013)/Specials (-JJ-)/2000AD Sci-Fi Special (1977 - 1996)/2000AD Sci-Fi Special 1978.cbr
- `   22 MB`  2000AD prog/2000AD (Specials, Annuals & Poster Progs + Extras)/2000AD Yearbooks & Specials (1977 - 2013)/Specials (-JJ-)/2000AD Sci-Fi Special (1977 - 1996)/2000AD Sci-Fi Special 1987.cbr
- `   22 MB`  2000AD prog/2000AD (Specials, Annuals & Poster Progs + Extras)/2000AD Yearbooks & Specials (1977 - 2013)/Specials (-JJ-)/2000AD Sci-Fi Special (1977 - 1996)/2000AD Sci-Fi Special 1978 - (Starlord Summer Sp).cbr
- `   21 MB`  2000AD prog/Yearbooks & Specials/Specials/Sci-Fi Special (1977-)/2000AD Sci-Fi Special 1983 (Judge-Julez).cbr
- `   21 MB`  2000AD prog/2000AD (Specials, Annuals & Poster Progs + Extras)/2000AD Yearbooks & Specials (1977 - 2013)/Specials (-JJ-)/2000AD Sci-Fi Special (1977 - 1996)/2000AD Sci-Fi Special 1983.cbr
- `   21 MB`  2000AD prog/2000AD (Specials, Annuals & Poster Progs + Extras)/2000AD Yearbooks & Specials (1977 - 2013)/Specials (-JJ-)/2000AD Sci-Fi Special (1977 - 1996)/2000AD Sci-Fi Special 1980.cbr
- `   19 MB`  2000AD prog/2000AD (Specials, Annuals & Poster Progs + Extras)/2000AD Yearbooks & Specials (1977 - 2013)/Specials (-JJ-)/2000AD Sci-Fi Special (1977 - 1996)/2000AD Sci-Fi Special 1988.cbr
- `   15 MB`  2000AD prog/2000AD (Specials, Annuals & Poster Progs + Extras)/2000AD Yearbooks & Specials (1977 - 2013)/Specials (-JJ-)/2000AD Sci-Fi Special (1977 - 1996)/2000AD Sci-Fi Special 1986.cbr
- `   14 MB`  2000AD prog/2000AD (Specials, Annuals & Poster Progs + Extras)/2000AD Yearbooks & Specials (1977 - 2013)/Specials (-JJ-)/2000AD Sci-Fi Special (1977 - 1996)/2000AD Sci-Fi Special 1979.cbr

### harley quinn — v1  *(volume)*

- `  853 MB`  Harley Quinn/Harley Quinn v01 - Girl in a Crisis (2024) (digital) (Son of Ultron-Empire).cbr
- `  542 MB`  Harley Quinn/Harley Quinn v01 - Destructive Comics (2025) (digital) (Son of Ultron-Empire).cbr
- `  397 MB`  Harley Quinn/Harley Quinn Vol. 2 (New 52) (v01-v06)(2014-2016)/Harley Quinn v01 - Hot in the City (2014) (Digital) (Zone-Empire).cbr
- `  282 MB`  Harley Quinn/Harley Quinn Vol. 3 (Rebirth) – TPB Vol. 1 – 6 (2017-2018)/Harley Quinn (2016-) - v01 Die Laughing .cbr
- `  221 MB`  Harley Quinn/Harley Quinn Vol. 7 (2018-2019)/Harley Quinn v01 - Harley vs. Apokolips (2018) (digital) (Son of Ultron-Empire).cbr

### american caper — v1  *(volume)*

- ` 1.27 GB`  American Caper/American Caper v01 - Red-Pilled Blues (2026) (digital) (Son of Ultron-Empire).cbr
- `  871 MB`  American Caper/American Caper v01 (2026).cbz

### gantz.  *(issue)*

- `  206 MB`  Manga/Ganz/Gantz.V34.cbz
- `  203 MB`  Manga/Ganz/Gantz.V35.cbz
- `  194 MB`  Manga/Ganz/Gantz.V37.cbz
- `  170 MB`  Manga/Ganz/Gantz.V33.cbz
- `  158 MB`  Manga/Ganz/Gantz.V36.cbz
- `  102 MB`  Manga/Ganz/Gantz.V32.cbz
- `   97 MB`  Manga/Ganz/Gantz.V31.cbz
- `   68 MB`  Manga/Ganz/Gantz.V30.cbz
- `   39 MB`  Manga/Ganz/Gantz.V29.cbz
- `   30 MB`  Manga/Ganz/Gantz.V07.cbz
- `   29 MB`  Manga/Ganz/Gantz.V18.cbz
- `   27 MB`  Manga/Ganz/Gantz.V27.cbz
- `   26 MB`  Manga/Ganz/Gantz.V17.cbz
- `   26 MB`  Manga/Ganz/Gantz.V06.cbz
- `   25 MB`  Manga/Ganz/Gantz.V28.cbz
- `   25 MB`  Manga/Ganz/Gantz.V09.cbz
- `   25 MB`  Manga/Ganz/Gantz.V08.cbz
- `   24 MB`  Manga/Ganz/Gantz.V12.cbz
- `   24 MB`  Manga/Ganz/Gantz.V13.cbz
- `   24 MB`  Manga/Ganz/Gantz.V23.cbz
- `   24 MB`  Manga/Ganz/Gantz.V10.cbz
- `   23 MB`  Manga/Ganz/Gantz.V19.cbz
- `   23 MB`  Manga/Ganz/Gantz.V15.cbz
- `   23 MB`  Manga/Ganz/Gantz.V16.cbz
- `   22 MB`  Manga/Ganz/Gantz.V24.cbz
- `   22 MB`  Manga/Ganz/Gantz.V11.cbz
- `   22 MB`  Manga/Ganz/Gantz.V26.cbz
- `   21 MB`  Manga/Ganz/Gantz.V21.cbz
- `   21 MB`  Manga/Ganz/Gantz.V25.cbz
- `   21 MB`  Manga/Ganz/Gantz.V05.cbz
- `   21 MB`  Manga/Ganz/Gantz.V04.cbz
- `   21 MB`  Manga/Ganz/Gantz.V14.cbz
- `   20 MB`  Manga/Ganz/Gantz.V03.cbz
- `   20 MB`  Manga/Ganz/Gantz.V02.cbz
- `   20 MB`  Manga/Ganz/Gantz.V01.cbz
- `   19 MB`  Manga/Ganz/Gantz.V22.cbz
- `   18 MB`  Manga/Ganz/Gantz.V20.cbz

### batman — v3  *(volume)*

- `  948 MB`  Batman/Batman v03 - The Joker Year One (2024) (digital) (Son of Ultron-Empire).cbr
- `  628 MB`  Batman/Batman v03 - Ghost Stories (2021) (Digital) (EJGriffin-Empire).cbz
- `  213 MB`  Batman/Batman (v01-v04)(2017)(digital)(Zone-Empire)/Batman v03 - I Am Bane (2017) (Digital) (Zone-Empire).cbr

### harley quinn — v5  *(volume)*

- `  685 MB`  Harley Quinn/Harley Quinn v05 - Who Killed Harley Quinn (2024) (digital) (Son of Ultron-Empire).cbr
- `  633 MB`  Harley Quinn/Harley Quinn v05 - Hollywood or Die (2021) (digital) (Son of Ultron-Empire).cbr
- `  223 MB`  Harley Quinn/Harley Quinn Vol. 2 (New 52) (v01-v06)(2014-2016)/Harley Quinn v05 - The Jokers Last Laugh (2016) (digital) (Son of Ultron-Empire).cbr
- `  221 MB`  Harley Quinn/Harley Quinn Vol. 3 (Rebirth) – TPB Vol. 1 – 6 (2017-2018)/Harley Quinn (2016-) - v05 Vote Harley.cbr

### jennifer blood — v1  *(volume)*

- `  986 MB`  Jennifer Blood/Jennifer Blood Omnibus v01 (2019) (Digital) (DR & Quinch-Empire).cbr
- `  693 MB`  Jennifer Blood/Jennifer Blood v01 - A Womans Work is Never Done (2012) (digital) (DR & Quinch-Empire).cbr

### harley quinn — v3  *(volume)*

- `  777 MB`  Harley Quinn/Harley Quinn v03 - Clown About Town (2025) (digital) (Son of Ultron-Empire).cbr
- `  293 MB`  Harley Quinn/Harley Quinn Vol. 2 (New 52) (v01-v06)(2014-2016)/Harley Quinn v03 - Kiss Kiss Bang Stab (2015) (digital) (Son of Ultron-Empire).cbr
- `  252 MB`  Harley Quinn/Harley Quinn Vol. 7 (2018-2019)/Harley Quinn v03 - The Trials of Harley Quinn (2019) (digital) (Son of Ultron-Empire).cbr
- `  209 MB`  Harley Quinn/Harley Quinn Vol. 3 (Rebirth) – TPB Vol. 1 – 6 (2017-2018)/Harley Quinn (2016-) - v03 Red Meat.cbr
- `   68 MB`  Harley Quinn/Harley Quinn v03 - Verdict (2023) (digital-SD) (Dakota Scanning).cbz

### into unbeing  *(issue)*

- ` 1.16 GB`  Into the Unbeing/Into the Unbeing - Part One (2025) (digital) (Son of Ultron-Empire).cbr
- `  381 MB`  Into the Unbeing/Into the Unbeing - Part Two (2025) (digital) (Son of Ultron-Empire).cbr

### boys — v3  *(volume)*

- `  769 MB`  The Boys/The Boys TPBs/The Boys v03 (15-22) - Good for the Soul (2008) (digital) (The Magicians-Empire).cbr
- `  670 MB`  The Boys/The Boys TPBs/The Boys Omnibus v03 (2012) (F) (digital-Empire).cbz

### boys — v2  *(volume)*

- `  722 MB`  The Boys/The Boys TPBs/The Boys v02 (7-14) - Get Some (2008) (digital) (The Magicians-Empire).cbr
- `  688 MB`  The Boys/The Boys TPBs/The Boys Omnibus v02 (2012) (digital-Empire).cbz

### ghost pepper — v1  *(volume)*

- `  730 MB`  Ghost Pepper/Ghost Pepper v01.cbz
- `  667 MB`  Ghost Pepper/Ghost Pepper v01 - Flavors of Ash (2026) (Digital) (DR & Quinch-Empire).cbr

### boys — v4  *(volume)*

- `  821 MB`  The Boys/The Boys TPBs/The Boys v04 (23-30) - We Gotta Go Now (2009) (digital) (The Magicians-Empire).cbr
- `  575 MB`  The Boys/The Boys TPBs/The Boys Omnibus v04 (2019) (2 covers) (Digital) (DR & Quinch-Empire).cbr

### ghost pepper — v2  *(volume)*

- `  791 MB`  Ghost Pepper/Ghost Pepper v02 - Taste of Cinders (2026) (Digital-Empire).cbz
- `  604 MB`  Ghost Pepper/Ghost Pepper v02.cbz

### 2000ad  *(annual)*

- `  147 MB`  2000AD prog/2000AD (Specials, Annuals & Poster Progs + Extras)/2000AD Annual 2025 (2024) (digital) (Minutemen-juvecube).cbz
- `  126 MB`  2000AD prog/2000AD (Specials, Annuals & Poster Progs + Extras)/2000AD Yearbooks & Specials (1977 - 2013)/2000 AD Yearbook 1992-1995/2000AD Yearbook 1993 (c2c) (Lesueur).cbz
- `  119 MB`  2000AD prog/2000AD (Specials, Annuals & Poster Progs + Extras)/2000AD Yearbooks & Specials (1977 - 2013)/2000 AD Yearbook 1992-1995/2000AD Yearbook 1995 (c2c) (Lesueur).cbz
- `  117 MB`  2000AD prog/2000AD (Specials, Annuals & Poster Progs + Extras)/2000AD Yearbooks & Specials (1977 - 2013)/2000 AD Yearbook 1992-1995/2000AD Yearbook 1994 (c2c) (Lesueur).cbz
- `   73 MB`  2000AD prog/2000AD (Specials, Annuals & Poster Progs + Extras)/2000AD Yearbooks & Specials (1977 - 2013)/2000AD Annuals (1978 - 1995)/2000AD Annual 1993 Yearbook.cbr
- `   69 MB`  2000AD prog/2000AD (Specials, Annuals & Poster Progs + Extras)/2000AD Yearbooks & Specials (1977 - 2013)/2000AD Annuals (1978 - 1995)/2000AD Annual 1981.cbr
- `   62 MB`  2000AD prog/2000AD (Specials, Annuals & Poster Progs + Extras)/2000AD Yearbooks & Specials (1977 - 2013)/2000AD Annuals (1978 - 1995)/2000AD Annual 1978.cbr
- `   60 MB`  2000AD prog/2000AD (Specials, Annuals & Poster Progs + Extras)/2000AD Yearbooks & Specials (1977 - 2013)/2000AD Annuals (1978 - 1995)/2000AD Annual 1994 Yearbook.cbr
- `   56 MB`  2000AD prog/2000AD (Specials, Annuals & Poster Progs + Extras)/2000AD Yearbooks & Specials (1977 - 2013)/2000AD Annuals (1978 - 1995)/2000AD Annual 1979.cbr
- `   56 MB`  2000AD prog/2000AD (Specials, Annuals & Poster Progs + Extras)/2000AD Yearbooks & Specials (1977 - 2013)/2000AD Annuals (1978 - 1995)/2000AD Annual 1980.cbr
- `   50 MB`  2000AD prog/2000AD (Specials, Annuals & Poster Progs + Extras)/2000AD Yearbooks & Specials (1977 - 2013)/2000AD Annuals (1978 - 1995)/2000AD Annual 1992 Yearbook.cbr
- `   47 MB`  2000AD prog/2000AD (Specials, Annuals & Poster Progs + Extras)/2000AD Yearbooks & Specials (1977 - 2013)/2000AD Annuals (1978 - 1995)/2000AD Annual 1984.cbr
- `   46 MB`  2000AD prog/2000AD (Specials, Annuals & Poster Progs + Extras)/2000AD Yearbooks & Specials (1977 - 2013)/2000AD Annuals (1978 - 1995)/2000AD Annual 1986.cbr
- `   45 MB`  2000AD prog/2000AD (Specials, Annuals & Poster Progs + Extras)/2000AD Yearbooks & Specials (1977 - 2013)/2000AD Annuals (1978 - 1995)/2000AD Annual 1991 - Rogue Trooper.cbr
- `   42 MB`  2000AD prog/2000AD (Specials, Annuals & Poster Progs + Extras)/2000AD Yearbooks & Specials (1977 - 2013)/2000AD Annuals (1978 - 1995)/2000AD Annual 1989.cbr
- `   41 MB`  2000AD prog/2000AD (Specials, Annuals & Poster Progs + Extras)/2000AD Yearbooks & Specials (1977 - 2013)/2000AD Annuals (1978 - 1995)/2000AD Annual 1995 Yearbook.cbr
- `   39 MB`  2000AD prog/2000AD (Specials, Annuals & Poster Progs + Extras)/2000AD Yearbooks & Specials (1977 - 2013)/2000AD Annuals (1978 - 1995)/2000AD Annual 1985.cbr
- `   38 MB`  2000AD prog/2000AD (Specials, Annuals & Poster Progs + Extras)/2000AD Yearbooks & Specials (1977 - 2013)/2000AD Annuals (1978 - 1995)/2000AD Annual 1982.cbr
- `   34 MB`  2000AD prog/2000AD (Specials, Annuals & Poster Progs + Extras)/2000AD Yearbooks & Specials (1977 - 2013)/2000AD Annuals (1978 - 1995)/2000AD Annual 1983.cbr
- `   30 MB`  2000AD prog/2000AD (Specials, Annuals & Poster Progs + Extras)/2000AD Yearbooks & Specials (1977 - 2013)/2000AD Annuals (1978 - 1995)/2000AD Annual 1987.cbr
- `   30 MB`  2000AD prog/2000AD (Specials, Annuals & Poster Progs + Extras)/2000AD Yearbooks & Specials (1977 - 2013)/2000AD Annuals (1978 - 1995)/2000AD Annual 1988.cbr
- `   29 MB`  2000AD prog/2000AD (Specials, Annuals & Poster Progs + Extras)/2000AD Yearbooks & Specials (1977 - 2013)/2000AD Annuals (1978 - 1995)/2000AD Annual 1990.cbr
- `   29 MB`  2000AD prog/2000AD (Specials, Annuals & Poster Progs + Extras)/2000AD Yearbooks & Specials (1977 - 2013)/2000AD Annuals (1978 - 1995)/2000AD Annual 1991.cbr

### boys — v6  *(volume)*

- `  710 MB`  The Boys/The Boys TPBs/The Boys v06 (31-38) - The Self-Preservation Society (2010) (digital) (The Magicians-Empire).cbr
- `  615 MB`  The Boys/The Boys TPBs/The Boys Omnibus v06 (2019) (2 covers) (Digital) (DR & Quinch-Empire).cbr

### b.p.r.d. hell on earth — v2  *(volume)*

- ` 1.12 GB`  Hellboy/B.P.R.D. - Hell on Earth (v01-v15)(2011-2017)(digital)(Son of Ultron-Empire)/B.P.R.D. Hell on Earth Omnibus v02 (v04-06 2018) (digital) (Son of Ultron-Empire).cbr
- `  187 MB`  Hellboy/B.P.R.D. - Hell on Earth (v01-v15)(2011-2017)(digital)(Son of Ultron-Empire)/B.P.R.D. - Hell on Earth v02 - Gods and Monsters (2012) (digital) (Minutemen-Azkaban).cbr

### deadly class — v1  *(volume)*

- ` 1.04 GB`  Deadly Class/Deadly Class Book01 - Noise Noise Noise (2016) (Digital) (Zone-Empire).cbr
- `  219 MB`  Deadly Class/Deadly Class v01 - Reagan Youth (2014) (Digital) (DR & Quinch-Empire).cbr

### blood & thunder — v2  *(volume)*

- `  736 MB`  Blood & Thunder/Blood & Thunder v02 (2026).cbz
- `  500 MB`  Blood & Thunder/Blood & Thunder v02 - Showdown on the Outskirts of Infinity (2026) (Digital) (DR & Quinch-Empire).cbr

### black hammer — v2  *(volume)*

- `  709 MB`  Black Hammer/Black Hammer Omnibus v02 (2023) (digital) (Son of Ultron-Empire).cbr
- `  503 MB`  Black Hammer/Black Hammer v02 - The Event (2017) (digital) (Son of Ultron-Empire).cbr

### avengers — v1  *(volume)*

- `  331 MB`  Avengers/Avengers Vol. 07 (001-011,672-690)(2017-2018)(digital)/Avengers Vol. 01 - Kang War One (2017) (digital) (Minutemen-Slayer).cbr
- `  331 MB`  Avengers/Avengers (2017)/Avengers Vol. 01 - Kang War One (2017) (digital) (Minutemen-Slayer).cbr
- `  295 MB`  Avengers/Avengers Vol. 01 (2011) (digital) (Minutemen-Slayer).cbr
- `  223 MB`  Avengers/Avengers (2013-2014)/Avengers v01 - Avengers World (2013) (Digital) (F) (Zone-Empire).cbr

### books of magic — v2  *(volume)*

- `  953 MB`  Neil Gaiman Library/The Books of Magic (Neil Gaiman)/The Books Of Magic v2 - 01-75 +Annuals (1994) .cbz
- `  201 MB`  Neil Gaiman Library/The Books of Magic (Neil Gaiman)/Books of Magic v02 - Second Quarto (2020) (digital) (Son of Ultron-Empire).cbr
- `   11 MB`  Neil Gaiman Library/The Books of Magic (Neil Gaiman)/The Books Of Magic v2 - 01-75 +Annuals (1994) /The Books of Magic v2 056a Annual 03 (1999) (noads) (Obi).cbr
- `   11 MB`  Neil Gaiman Library/The Books of Magic (Neil Gaiman)/The Books Of Magic v2 - 01-75 +Annuals (1994) /The Books of Magic v2 044a Annual 02 (1998) (noads).cbr

### boys — v5  *(volume)*

- `  702 MB`  The Boys/The Boys TPBs/The Boys Omnibus v05 (2019) (2 covers) (Digital) (DR & Quinch-Empire).cbr
- `  441 MB`  The Boys/The Boys TPBs/The Boys v05 - Herogasm (2009) (digital) (The Magicians-Empire).cbr

### judge dredd  *(annual)*

- `   59 MB`  2000AD prog/Yearbooks & Specials/Annuals (1978-1995)/Judge Dredd/Judge Dredd Annual Yearbook 1993.cbr
- `   59 MB`  2000AD prog/2000AD Yearbooks & Specials (1977 - 2013)/Judge Dredd Annuals (1981 - 1995)/Judge Dredd Annual Yearbook 1993.cbr
- `   59 MB`  2000AD prog/2000AD (Specials, Annuals & Poster Progs + Extras)/2000AD Yearbooks & Specials (1977 - 2013)/Judge Dredd Annuals (1981 - 1995)/Judge Dredd Annual Yearbook 1993.cbr
- `   57 MB`  2000AD prog/2000AD (Specials, Annuals & Poster Progs + Extras)/2000AD Yearbooks & Specials (1977 - 2013)/Judge Dredd Annuals (1981 - 1995)/Judge Dredd Annual Yearbook 1994.cbr
- `   51 MB`  2000AD prog/2000AD (Specials, Annuals & Poster Progs + Extras)/2000AD Yearbooks & Specials (1977 - 2013)/Judge Dredd Annuals (1981 - 1995)/Judge Dredd Annual 1988.cbr
- `   50 MB`  2000AD prog/Yearbooks & Specials/Annuals (1978-1995)/Judge Dredd/Judge Dredd Annual 1985.cbr
- `   50 MB`  2000AD prog/2000AD (Specials, Annuals & Poster Progs + Extras)/2000AD Yearbooks & Specials (1977 - 2013)/Judge Dredd Annuals (1981 - 1995)/Judge Dredd Annual 1981.cbr
- `   49 MB`  2000AD prog/2000AD (Specials, Annuals & Poster Progs + Extras)/2000AD Yearbooks & Specials (1977 - 2013)/Judge Dredd Annuals (1981 - 1995)/Judge Dredd Annual 1991.cbr
- `   46 MB`  2000AD prog/Yearbooks & Specials/Annuals (1978-1995)/Judge Dredd/Judge Dredd Annual Yearbook 1995.cbr
- `   46 MB`  2000AD prog/2000AD Yearbooks & Specials (1977 - 2013)/Judge Dredd Annuals (1981 - 1995)/Judge Dredd Annual Yearbook 1995.cbr
- `   46 MB`  2000AD prog/2000AD (Specials, Annuals & Poster Progs + Extras)/2000AD Yearbooks & Specials (1977 - 2013)/Judge Dredd Annuals (1981 - 1995)/Judge Dredd Annual Yearbook 1995.cbr
- `   44 MB`  2000AD prog/2000AD (Specials, Annuals & Poster Progs + Extras)/2000AD Yearbooks & Specials (1977 - 2013)/Judge Dredd Annuals (1981 - 1995)/Judge Dredd Annual 1984.cbr
- `   42 MB`  2000AD prog/Yearbooks & Specials/Annuals (1978-1995)/Judge Dredd/Judge Dredd Annual Yearbook 1992.cbr
- `   42 MB`  2000AD prog/2000AD Yearbooks & Specials (1977 - 2013)/Judge Dredd Annuals (1981 - 1995)/Judge Dredd Annual Yearbook 1992.cbr
- `   42 MB`  2000AD prog/2000AD (Specials, Annuals & Poster Progs + Extras)/2000AD Yearbooks & Specials (1977 - 2013)/Judge Dredd Annuals (1981 - 1995)/Judge Dredd Annual Yearbook 1992.cbr
- `   40 MB`  2000AD prog/2000AD (Specials, Annuals & Poster Progs + Extras)/2000AD Yearbooks & Specials (1977 - 2013)/Judge Dredd Annuals (1981 - 1995)/Judge Dredd Annual 1989.cbr
- `   40 MB`  2000AD prog/Yearbooks & Specials/Annuals (1978-1995)/Judge Dredd/Judge Dredd Annual 1986.cbr
- `   40 MB`  2000AD prog/2000AD Yearbooks & Specials (1977 - 2013)/Judge Dredd Annuals (1981 - 1995)/Judge Dredd Annual 1986.cbr
- `   40 MB`  2000AD prog/2000AD (Specials, Annuals & Poster Progs + Extras)/2000AD Yearbooks & Specials (1977 - 2013)/Judge Dredd Annuals (1981 - 1995)/Judge Dredd Annual 1986.cbr
- `   39 MB`  2000AD prog/2000AD (Specials, Annuals & Poster Progs + Extras)/2000AD Yearbooks & Specials (1977 - 2013)/Judge Dredd Annuals (1981 - 1995)/Judge Dredd Annual 1990.cbr
- `   36 MB`  2000AD prog/Yearbooks & Specials/Annuals (1978-1995)/Judge Dredd/Judge Dredd Annual 1983.cbr
- `   36 MB`  2000AD prog/2000AD Yearbooks & Specials (1977 - 2013)/Judge Dredd Annuals (1981 - 1995)/Judge Dredd Annual 1983.cbr
- `   36 MB`  2000AD prog/2000AD (Specials, Annuals & Poster Progs + Extras)/2000AD Yearbooks & Specials (1977 - 2013)/Judge Dredd Annuals (1981 - 1995)/Judge Dredd Annual 1983.cbr
- `   33 MB`  2000AD prog/2000AD (Specials, Annuals & Poster Progs + Extras)/2000AD Yearbooks & Specials (1977 - 2013)/Judge Dredd Annuals (1981 - 1995)/Judge Dredd Annual 1982.cbr
- `   28 MB`  2000AD prog/2000AD (Specials, Annuals & Poster Progs + Extras)/2000AD Yearbooks & Specials (1977 - 2013)/Judge Dredd Annuals (1981 - 1995)/Judge Dredd Annual 1987.cbr

### catwoman — v5  *(volume)*

- `  664 MB`  Catwoman/Catwoman v05 - Valley of the Shadow of Death (2021) (digital) (Son of Ultron-Empire).cbr
- `  436 MB`  Catwoman/Catwoman v05 - Backward Masking (2016) (digital) (Son of Ultron-Empire).cbr

### avengers — v2  *(volume)*

- `  281 MB`  Avengers/Avengers Vol. 07 (001-011,672-690)(2017-2018)(digital)/Avengers Vol. 02 - Secret Empire (2017) (digital) (Minutemen-Slayer).cbr
- `  281 MB`  Avengers/Avengers (2017)/Avengers Vol. 02 - Secret Empire (2017) (digital) (Minutemen-Slayer).cbr
- `  261 MB`  Avengers/Avengers Vol. 02 (2012) (digital) (Minutemen-Slayer).cbr
- `  245 MB`  Avengers/Avengers (2013-2014)/Avengers v02 - The Last White Event  (2013) GetComics.INFO.cbr

### deadly class — v2  *(volume)*

- `  882 MB`  Deadly Class/Deadly Class Book02 - The Funeral Party (2018) (Digital) (Zone-Empire).cbr
- `  171 MB`  Deadly Class/Deadly Class v02 - Kids of the Black Hole (2015) (Digital) (DR & Quinch-Empire).cbr

### i hate fairyland — v1  *(volume)*

- `  826 MB`  I Hate Fairyland/I Hate Fairyland - Book One (2017) (Digital) (F) (Kileko-Empire).cbz
- `  217 MB`  I Hate Fairyland/I Hate Fairyland v01 - Madly Ever After (2016) (digital) (d'argh-Empire).cbr

### books of magic — v1  *(volume)*

- `  445 MB`  Neil Gaiman Library/The Books of Magic (Neil Gaiman)/The Books of Magic v01 (2017) (Digital) (danke-Empire).cbz
- `  329 MB`  Neil Gaiman Library/The Books of Magic (Neil Gaiman)/The Books of Magic v1 (1993) (Digital) (Zone-Empire).cbr
- `  250 MB`  Neil Gaiman Library/The Books of Magic (Neil Gaiman)/Books of Magic v01 - Moveable Type (2019) (digital) (Son of Ultron-Empire).cbr

### captain america — v1  *(volume)*

- `  394 MB`  Captain America/Captain America v01 - Castaway in Dimension Z - Book 01 (2013) (Digital) (F) (BroadCast-Empire).cbz
- `  238 MB`  Captain America/Captain America v01 - The New Deal (2002) (digital) (Minutemen-Slayer).cbr
- `  222 MB`  Captain America/Captain America vol 1-5 (2019-2021)/Captain America v01 - Winter in America (2019) (Digital) (Zone-Empire).cbr
- `  160 MB`  Captain America/Captain America (v01-v02 - Winter Soldier v1-v2) (2005-2006) (digital) (Minutemen-Slayer)/Captain America Vol. 01 - Winter Soldier Vol. 1 (2005) (digital) (Minutemen-Slayer).cbr

### love & rockets — v1  *(volume)*

- `  697 MB`  Hernandez brothers/Love and Rockets/Love & Rockets v1 (001-042)(1981-1993).cbz
- `  318 MB`  Hernandez brothers/Love and Rockets/Love & Rockets v01 - Maggie the Mechanic (2007) (digital-Empire).cbz

### captain america sam wilson — v2  *(volume)*

- `  688 MB`  Captain America/Captain America - Sam Wilson - The Complete Collection v02 (2021) (Digital) (Zone-Empire).cbr
- `  316 MB`  Captain America/Captain America - Sam Wilson v02 - Standoff (2016) (digital) (Minutemen-Slayer).cbr

### batman — v1  *(volume)*

- `  395 MB`  Batman/Batman Vol. 1 - Failsafe (2023) (digital) (Deathglobe-GetComics).cbz
- `  320 MB`  Batman/Batman v01 - Their Dark Designs (2020) (Digital) (EJGriffin-Empire).cbz
- `  263 MB`  Batman/Batman (v01-v04)(2017)(digital)(Zone-Empire)/Batman v01 - I Am Gotham (2017) (Digital) (Zone-Empire).cbr

### 2000ad winter  *(special)*

- `   92 MB`  2000AD prog/Yearbooks & Specials/Specials/Winter Special (1988-)/2000AD Winter Special 1992.cbz
- `   83 MB`  2000AD prog/Yearbooks & Specials/Specials/Winter Special (1988-)/2000AD Winter Special 1990.cbr
- `   82 MB`  2000AD prog/Yearbooks & Specials/Specials/Winter Special (1988-)/2000AD Winter Special 1995.cbz
- `   75 MB`  2000AD prog/Yearbooks & Specials/Specials/Winter Special (1988-)/2000AD Winter Special 1993.cbz
- `   71 MB`  2000AD prog/Yearbooks & Specials/Specials/Winter Special (1988-)/2000AD Winter Special 1994.cbz
- `   71 MB`  2000AD prog/2000AD (Specials, Annuals & Poster Progs + Extras)/2000AD Yearbooks & Specials (1977 - 2013)/2000 AD Winter Special 1988-2014/2000AD Winter Special 1994.cbz
- `   42 MB`  2000AD prog/2000AD Yearbooks & Specials (1977 - 2013)/Specials (-JJ-)/2000AD Winter Special/2000AD Winter Special 1992.cbr
- `   42 MB`  2000AD prog/2000AD (Specials, Annuals & Poster Progs + Extras)/2000AD Yearbooks & Specials (1977 - 2013)/Specials (-JJ-)/2000AD Winter Special/2000AD Winter Special 1992.cbr
- `   39 MB`  2000AD prog/Yearbooks & Specials/Specials/Winter Special (1988-)/2000AD Winter Special (2014) (digital) (Nahga-Empire).cbr
- `   39 MB`  2000AD prog/2000AD (Specials, Annuals & Poster Progs + Extras)/2000AD Yearbooks & Specials (1977 - 2013)/2000 AD Winter Special 1988-2014/2000AD Winter Special (2014) (Digital) (Nahga-Empire).cbr
- `   37 MB`  2000AD prog/2000AD Yearbooks & Specials (1977 - 2013)/Specials (-JJ-)/2000AD Winter Special/2000AD Winter Special 1990.cbr
- `   37 MB`  2000AD prog/2000AD (Specials, Annuals & Poster Progs + Extras)/2000AD Yearbooks & Specials (1977 - 2013)/Specials (-JJ-)/2000AD Winter Special/2000AD Winter Special 1990.cbr
- `   33 MB`  2000AD prog/2000AD Yearbooks & Specials (1977 - 2013)/Specials (-JJ-)/2000AD Winter Special/2000AD Winter Special 1995.cbr
- `   33 MB`  2000AD prog/2000AD (Specials, Annuals & Poster Progs + Extras)/2000AD Yearbooks & Specials (1977 - 2013)/Specials (-JJ-)/2000AD Winter Special/2000AD Winter Special 1995.cbr
- `   30 MB`  2000AD prog/Yearbooks & Specials/Specials/Winter Special (1988-)/2000AD Winter Special 1989 (Judge-Julez).cbr
- `   30 MB`  2000AD prog/2000AD (Specials, Annuals & Poster Progs + Extras)/2000AD Yearbooks & Specials (1977 - 2013)/Specials (-JJ-)/2000AD Winter Special/2000AD Winter Special 1989.cbr
- `   28 MB`  2000AD prog/2000AD Yearbooks & Specials (1977 - 2013)/Specials (-JJ-)/2000AD Winter Special/2000AD Winter Special 1993.cbr
- `   28 MB`  2000AD prog/2000AD (Specials, Annuals & Poster Progs + Extras)/2000AD Yearbooks & Specials (1977 - 2013)/Specials (-JJ-)/2000AD Winter Special/2000AD Winter Special 1993.cbr
- `   28 MB`  2000AD prog/Yearbooks & Specials/Specials/Winter Special (1988-)/2000AD Winter Special 1988 (c2c) (F) (Youngstar).cbr
- `   27 MB`  2000AD prog/2000AD (Specials, Annuals & Poster Progs + Extras)/2000AD Yearbooks & Specials (1977 - 2013)/Specials (-JJ-)/2000AD Winter Special/2000AD Winter Special 2005.cbr
- `   26 MB`  2000AD prog/2000AD (Specials, Annuals & Poster Progs + Extras)/2000AD Yearbooks & Specials (1977 - 2013)/Specials (-JJ-)/2000AD Winter Special/2000AD Winter Special 1988.cbr

### district  *(issue)*

- `  498 MB`  Humanoids (Europe)/District 14/District 14 - Season 2.cbz
- `  464 MB`  Humanoids (Europe)/District 14/District 14 - Season 1.cbz

### sir edward grey, witchfinder — v2  *(volume)*

- `  485 MB`  Sir Edward Grey, Witchfinder (Collection) (2009-2014) GetComics.INFO/Sir Edward Grey, Witchfinder Omnibus v02 (2021) (digital) (Son of Ultron-Empire).cbr
- `  235 MB`  Hellboy/Sir Edward Grey, Witchfinder TPBs/Sir Edward Grey, Witchfinder v02 - Lost and Gone Forever (2012) GetComics.INFO.cbr
- `  235 MB`  Hellboy/7.)  Sir Edward Grey, Witchfinder - Lost and Gone Forever #1-5  (1880 AD)/Sir Edward Grey, Witchfinder v02 - Lost and Gone Forever (2012) (digital) (Son of Ultron-Empire).cbr

### boys — v1  *(volume)*

- `  582 MB`  The Boys/The Boys TPBs/The Boys Omnibus v01 (1-22) (2012).cbz
- `  366 MB`  The Boys/The Boys TPBs/The Boys v01 (1-6) - The Name of the Game (2007) (digital) (The Magicians-Empire).cbr

### black hammer — v1  *(volume)*

- `  649 MB`  Black Hammer/Black Hammer Omnibus v01 (2022) (digital) (Son of Ultron-Empire).cbr
- `  291 MB`  Black Hammer/Black Hammer v01 - Secret Origins (2017) GetComics.INFO.cbr

### capes — v1  *(volume)*

- `  500 MB`  Capes/Capes v01 - Punching the Clock (2026) (Digital) (DR & Quinch-Empire).cbr
- `  320 MB`  Robert Kirkman/Invincible (Kirkman)/Extras/Capes v01 - Punching the Clock (2007) (Digital) (DR & Quinch-Empire).cbr
- `  120 MB`  Robert Kirkman/Invincible (Kirkman)/Extras/Capes/Capes v01 (2003).cbz

### captain america sam wilson — v1  *(volume)*

- `  678 MB`  Captain America/Captain America - Sam Wilson - The Complete Collection v01 (2020) (Digital) (Zone-Empire).cbr
- `  258 MB`  Captain America/Captain America - Sam Wilson v01 (2016) (digital) (Minutemen-Slayer).cbr

### lobster johnson — v2  *(volume)*

- `  787 MB`  Hellboy/Lobster Johnson/Lobster Johnson Omnibus v02 (2023) (digital) (Son of Ultron-Empire).cbr
- `  148 MB`  Hellboy/Lobster Johnson/Lobster Johnson v02 - The Burning Hand (2012) GetComics.INFO.cbr

### monarch — v1  *(volume)*

- `  706 MB`  Monarch v01 - Stranger From Above (2023) (Digital-Empire).cbz
- `  223 MB`  Monarch (2023) (Digital) (Zone-Empire)/Monarch v01 (2023).cbz

### jeronaton champakou  *(issue)*

- `  454 MB`  Jeronaton - Champakou (1978) [HD 2700] [HM edition] (Hoyeru).cbr
- `  454 MB`  Heavy Metal/Jeronaton - Champakou [HD 2700] [Heavy Metal edition].cbr

### star trek — v2  *(volume)*

- `  761 MB`  Star Trek/Star Trek v02 - The Red Path (2023) (digital) (The Magicians-Empire).cbr
- `  143 MB`  Star Trek/Star Trek (2012-2016)/Star Trek Vol. 02 (2012) (digital) (Minutemen-Slayer).cbr

### b.p.r.d. hell on earth — v1  *(volume)*

- `  651 MB`  Hellboy/B.P.R.D. - Hell on Earth (v01-v15)(2011-2017)(digital)(Son of Ultron-Empire)/B.P.R.D. Hell on Earth Omnibus v01 (v01-03 2017) (digital) (Son of Ultron-Empire).cbr
- `  238 MB`  Hellboy/B.P.R.D. - Hell on Earth (v01-v15)(2011-2017)(digital)(Son of Ultron-Empire)/B.P.R.D. - Hell on Earth v01 - New World (2011) (digital) (Son of Ultron-Empire).cbr

### captain america — v2  *(volume)*

- `  348 MB`  Captain America/Captain America v02 - Castaway in Dimension Z - Book 02 (2013) (Digital) (F) (BlackManta-Empire).cbz
- `  224 MB`  Captain America/Captain America vol 1-5 (2019-2021)/Captain America v02 - Captain of Nothing (2019) (Digital) (Zone-Empire).cbr
- `  174 MB`  Captain America/Captain America v02 - Extremists (2003) (Digital) (Zone-Empire).cbr
- `  131 MB`  Captain America/Captain America (v01-v02 - Winter Soldier v1-v2) (2005-2006) (digital) (Minutemen-Slayer)/Captain America Vol. 02 - Winter Soldier Vol. 2 (2006) (digital) (Minutemen-Slayer).cbr

### catwoman — v2  *(volume)*

- `  421 MB`  Catwoman/Catwoman v02 - No Easy Way Down (2013) (digital) (Son of Ultron-Empire).cbr
- `  380 MB`  Catwoman/Catwoman v02 - Never Let Them Smell Blood (2025) (digital) (Son of Ultron-Empire).cbr
- `   67 MB`  Catwoman/Catwoman v02 - Cat International (2023) (digital-SD) (Dakota Scanning).cbz

### ghost in shell — v1  *(volume)*

- `  744 MB`  Manga/Ghost in the Shell/The Ghost in the Shell v01 (2009) (digital-Empire).cbr
- `   66 MB`  Manga/Ghost in the Shell/Ghost in the Shell v01 c01-07.cbz
- `   57 MB`  Manga/Ghost in the Shell/Ghost in the Shell v01 c08-11.cbz

### kick ass — v2  *(volume)*

- `  675 MB`  Mark Millar/Kick-Ass (v1-v3+)(2008-2014)(digital+)/Kick-Ass 2 (001-007+)(2010-2012)(digital)(Zone-Empire)/Kick-Ass v2 (1-7) (2012) - The Dave Lizewski Years v03 (2018) (Digital) (XRA-Empire).cbz
- `  153 MB`  Mark Millar/Kick-Ass (v1-v3+)(2008-2014)(digital+)/Kick-Ass Book 2 - Hit-Girl (2012) (Digital-1920) (Zone-Empire).cbr

### regular show — v5  *(volume)*

- `  608 MB`  Regular Show/Regular Show v05 - The Meatening (2018) (digital) (Salem-Empire).cbr
- `  204 MB`  Regular Show/Regular Show v05 (2016) (Digital-Empire).cbr

### i hate fairyland — v2  *(volume)*

- `  561 MB`  I Hate Fairyland/I Hate Fairyland - Book Two (2019) (Digital) (Kileko-Empire).cbz
- `  230 MB`  I Hate Fairyland/I Hate Fairyland v02 - Fluff My Life (2016) GetComics.INFO.cbr

### b.p.r.d. hell on earth — v4  *(volume)*

- `  523 MB`  Hellboy/B.P.R.D. - Hell on Earth (v01-v15)(2011-2017)(digital)(Son of Ultron-Empire)/B.P.R.D. Hell on Earth Omnibus v04 (2018) (digital) (Son of Ultron-Empire).cbr
- `  241 MB`  Hellboy/B.P.R.D. - Hell on Earth (v01-v15)(2011-2017)(digital)(Son of Ultron-Empire)/B.P.R.D. - Hell on Earth v04 - The Devils Engine and the Long Death (2012) (digital) (Son of Ultron-Empire).cbr

### black hammer — v3  *(volume)*

- `  605 MB`  Black Hammer/Black Hammer Omnibus v03 (2024) (digital) (Son of Ultron-Empire).cbr
- `  154 MB`  Black Hammer/Black Hammer v03 - Age of Doom Part 1 (2018) (digital) (Son of Ultron-Empire).cbr

### b.p.r.d. hell on earth — v5  *(volume)*

- `  530 MB`  Hellboy/B.P.R.D. - Hell on Earth (v01-v15)(2011-2017)(digital)(Son of Ultron-Empire)/B.P.R.D. Hell on Earth Omnibus v05 (2019) (digital) (Son of Ultron-Empire).cbr
- `  208 MB`  Hellboy/B.P.R.D. - Hell on Earth (v01-v15)(2011-2017)(digital)(Son of Ultron-Empire)/B.P.R.D. - Hell on Earth v05 - The Pickens County Horror and Others (2013) (digital) (Son of Ultron-Empire).cbr

### iron man — v3  *(volume)*

- `  512 MB`  Iron Man/Iron Man v03 - Books of Korvac III - Cosmic Iron Man (2021) (Digital-Empire).cbr
- `  226 MB`  Iron Man/Iron Man Vol. 03 - The Secret Origin of Tony Stark Book 2 (2013) (digital) (Minutemen-Slayer).cbr

### b.p.r.d. hell on earth — v3  *(volume)*

- `  527 MB`  Hellboy/B.P.R.D. - Hell on Earth (v01-v15)(2011-2017)(digital)(Son of Ultron-Empire)/B.P.R.D. Hell on Earth Omnibus v03 (v06-09 2018) (digital) (Son of Ultron-Empire).cbr
- `  198 MB`  Hellboy/B.P.R.D. - Hell on Earth (v01-v15)(2011-2017)(digital)(Son of Ultron-Empire)/B.P.R.D. - Hell on Earth v03 - Russia (2012) (digital) (Minutemen-Azkaban).cbr

### dracula  *(issue)*

- `  328 MB`  Dracula comics/Dracula (2010) (Digital) (Zone-Empire).cbr
- `  244 MB`  Dracula comics/Dracula (Bram Stoker) (Georges Bess).cbr
- `  153 MB`  Dracula comics/The Complete Dracula (2009) (Digital) (G85-Fawkes-Empire).cbz

### regular show — v4  *(volume)*

- `  533 MB`  Regular Show/Regular Show v04 - Wrasslesplosion (2017) (digital) (Salem-Empire).cbr
- `  182 MB`  Regular Show/Regular Show v04 (2016) (Digital-Empire).cbr

### marvel — #1602  *(issue)*

- `   47 MB`  Marvel 1602 + Tie Ins (2003-2004) GetComics.INFO/Marvel 1602 Complete/1 Marvel 1602 - (001-008)/Marvel 1602 08 (of 08) (2004).cbz
- `   40 MB`  Marvel 1602 + Tie Ins (2003-2004) GetComics.INFO/Marvel 1602 Complete/1 Marvel 1602 - (001-008)/Marvel 1602 01 (of 08) (2003).cbz
- `   39 MB`  Marvel 1602 + Tie Ins (2003-2004) GetComics.INFO/Marvel 1602 Complete/5 Marvel 1602 - Witch Hunter Angela (001 - 004)/Marvel 1602 - Witch Hunter Angela 003 (2015).cbz
- `   39 MB`  Marvel 1602 + Tie Ins (2003-2004) GetComics.INFO/Marvel 1602 Complete/1 Marvel 1602 - (001-008)/Marvel 1602 06 (of 08) (2004).cbz
- `   38 MB`  Marvel 1602 + Tie Ins (2003-2004) GetComics.INFO/Marvel 1602 Complete/5 Marvel 1602 - Witch Hunter Angela (001 - 004)/Marvel 1602 - Witch Hunter Angela 001 (2015).cbr
- `   36 MB`  Marvel 1602 + Tie Ins (2003-2004) GetComics.INFO/Marvel 1602 Complete/1 Marvel 1602 - (001-008)/Marvel 1602 05 (of 08) (2004).cbz
- `   36 MB`  Marvel 1602 + Tie Ins (2003-2004) GetComics.INFO/Marvel 1602 Complete/5 Marvel 1602 - Witch Hunter Angela (001 - 004)/Marvel 1602 - Witch Hunter Angela 004 (2015).cbr
- `   35 MB`  Marvel 1602 + Tie Ins (2003-2004) GetComics.INFO/Marvel 1602 Complete/1 Marvel 1602 - (001-008)/Marvel 1602 03 (of 08) (2003).cbz
- `   33 MB`  Marvel 1602 + Tie Ins (2003-2004) GetComics.INFO/Marvel 1602 Complete/2 Marvel 1602 - New World (001 - 005)/Marvel 1602 - New World 004 (2005).cbz
- `   33 MB`  Marvel 1602 + Tie Ins (2003-2004) GetComics.INFO/Marvel 1602 Complete/5 Marvel 1602 - Witch Hunter Angela (001 - 004)/Marvel 1602 - Witch Hunter Angela 002 (2015).cbz
- `   31 MB`  Marvel 1602 + Tie Ins (2003-2004) GetComics.INFO/Marvel 1602 Complete/2 Marvel 1602 - New World (001 - 005)/Marvel 1602 - New World 005 (2006).cbz
- `   31 MB`  Marvel 1602 + Tie Ins (2003-2004) GetComics.INFO/Marvel 1602 Complete/1 Marvel 1602 - (001-008)/Marvel 1602 07 (of 08) (2004).cbz
- `   30 MB`  Marvel 1602 + Tie Ins (2003-2004) GetComics.INFO/Marvel 1602 Complete/2 Marvel 1602 - New World (001 - 005)/Marvel 1602 - New World 001 (2005).cbz
- `   29 MB`  Marvel 1602 + Tie Ins (2003-2004) GetComics.INFO/Marvel 1602 Complete/3 Marvel 1602 - Fantastick Four (001 - 005)/Marvel 1602 - Fantastick Four 002 (2006).cbz
- `   28 MB`  Marvel 1602 + Tie Ins (2003-2004) GetComics.INFO/Marvel 1602 Complete/2 Marvel 1602 - New World (001 - 005)/Marvel 1602 - New World 003 (2005).cbz
- `   28 MB`  Marvel 1602 + Tie Ins (2003-2004) GetComics.INFO/Marvel 1602 Complete/1 Marvel 1602 - (001-008)/Marvel 1602 04 (of 08) (2004).cbz
- `   28 MB`  Marvel 1602 + Tie Ins (2003-2004) GetComics.INFO/Marvel 1602 Complete/3 Marvel 1602 - Fantastick Four (001 - 005)/Marvel 1602 - Fantastick Four 004 (2007).cbz
- `   28 MB`  Marvel 1602 + Tie Ins (2003-2004) GetComics.INFO/Marvel 1602 Complete/3 Marvel 1602 - Fantastick Four (001 - 005)/Marvel 1602 - Fantastick Four 001 (2006).cbz
- `   28 MB`  Marvel 1602 + Tie Ins (2003-2004) GetComics.INFO/Marvel 1602 Complete/1 Marvel 1602 - (001-008)/Marvel 1602 02 (of 08) (2003).cbz
- `   26 MB`  Marvel 1602 + Tie Ins (2003-2004) GetComics.INFO/Marvel 1602 Complete/2 Marvel 1602 - New World (001 - 005)/Marvel 1602 - New World 002 (2005).cbz
- `   25 MB`  Marvel 1602 + Tie Ins (2003-2004) GetComics.INFO/Marvel 1602 Complete/3 Marvel 1602 - Fantastick Four (001 - 005)/Marvel 1602 - Fantastick Four 003 (2007).cbz
- `   24 MB`  Marvel 1602 + Tie Ins (2003-2004) GetComics.INFO/Marvel 1602 Complete/3 Marvel 1602 - Fantastick Four (001 - 005)/Marvel 1602 - Fantastick Four 005 (2007).cbz

### silk — v3  *(volume)*

- `  358 MB`  Silk/Silk v03 - Nightmare Boulevard (2023) (Digital) (Shan-Empire).cbz
- `  352 MB`  Silk/Silk Vol03 - The Clone Conspiracy (2017) (Digital) (Shanhara).cbz

### lobster johnson — v1  *(volume)*

- `  483 MB`  Hellboy/Lobster Johnson/Lobster Johnson Omnibus v01 (2022) (digital) (Son of Ultron-Empire).cbr
- `  225 MB`  Hellboy/Lobster Johnson/Lobster Johnson v01 - The Iron Prometheus (2008) GetComics.INFO.cbr

### manifest destiny — v6  *(volume)*

- `  472 MB`  Manifest Destiny/Manifest Destiny v06 - Fortis & Invisibilia (2016) (digital) (Minutemen-Newt) (Zone-Empire) (RC).cbz
- `  234 MB`  Manifest Destiny/Manifest Destiny v06 - Fortis _ Invisiblia (2018) (Digital) (Zone-Empire).cbr

### gambit — v1  *(volume)*

- `  246 MB`  Gambit (001-017+)(2012-2013)(digital)(Minutemen-Excelsior)/Gambit Vol. 01 - Once A Thief... (2013) (digital) (Minutemen-Slayer).cbr
- `  246 MB`  Gambit/Gambit Vol. 01 - Once A Thief... (2013) (digital) (Minutemen-Slayer).cbr
- `  208 MB`  Gambit (001-017+)(2012-2013)(digital)(Minutemen-Excelsior)/Gambit v01.cbz

### deadly class — v3  *(volume)*

- `  580 MB`  Deadly Class/Deadly Class Book03 (vol 07-10 issues 32-48).cbz
- `  119 MB`  Deadly Class/Deadly Class v03 - The Snake Pit (2015) (Digital) (DR & Quinch-Empire).cbr

### scarlet traces — v2  — identical size  *(volume)*

- `  341 MB`  Scarlet Traces/Scarlet Traces v02 (2017) GetComics.INFO.cbr
- `  341 MB`  2000AD - Collections /Scarlet Traces/Scarlet Traces v02 (2017) (F) (digital) (Torquemada).cbr

### message to adolf — v1  — identical size  *(volume)*

- `  339 MB`  Manga/Osamu Tezuka/Message to Adolf v01 (Osamu Tezuka ) 2012.cbr
- `  339 MB`  Manga/Message to Adolf v01-02 (2012) (Digital) (XRA-Empire)/Message to Adolf v01 (2012) (Digital) (XRA-Empire).cbr

### captain marvel — v2  *(volume)*

- `  262 MB`  Captain Marvel/Captain Marvel v02 - Falling Star (2020) (Digital) (Kileko-Empire).cbz
- `  203 MB`  Captain Marvel/Captain Marvel v02 - Civil War II (2017) GetComics.INFO.cbr
- `  202 MB`  Captain Marvel/Captain Marvel v02 - Down (2014) (Digital) (F) (Asgard-Empire).cbz

### black widow — v2  *(volume)*

- `  260 MB`  Black Widow/Black Widow v02 - Kiss or Kill (2011) (Digital) (F) (Asgard-Empire).cbz
- `  229 MB`  Black Widow/Black Widow v02 - No More Secrets (2017) (Digital) (Zone-Empire).cbr
- `  172 MB`  Black Widow/Black Widow Vol. 02 - The Tightly Tangled Web (2015) (digital) (Minutemen-Excelsior).cbz

### love and rockets — v4  *(volume)*

- `  417 MB`  Hernandez brothers/Love and Rockets/Love and Rockets v04 - 001-008 (2016-2020).cbz
- `  240 MB`  Hernandez brothers/Love and Rockets/Love and Rockets v04 - 091-015 (2020-2024).cbz

### black widow — v1  *(volume)*

- `  308 MB`  Black Widow/Black Widow v01 - The Name of the Rose (2010) (Digital) (F) (Asgard-Empire).cbz
- `  206 MB`  Black Widow/Black Widow v01 - S.H.I.E.L.D.s Most Wanted (2016) (Digital) (F) (Zone-Empire).cbr
- `  137 MB`  Black Widow/Black Widow Vol. 01 - The Finely Woven Thread (2014) (digital) (Minutemen-Excelsior).cbz

### captain marvel — v1  *(volume)*

- `  247 MB`  Captain Marvel/Captain Marvel v01 - Re-Entry (2019) (Digital) (Kileko-Empire).cbz
- `  219 MB`  Captain Marvel/Captain Marvel v01 - In Pursuit of Flight (2013) (Digital) (F) (Asgard-Empire).cbz
- `  184 MB`  Captain Marvel/Captain Marvel v01 - Rise of Alpha Flight (2016) (Digital) (Kileko-Empire).cbr

### demon — v1  *(volume)*

- `  445 MB`  Garth Ennis Collection/The Demon/The Demon vol. 01 - Hell's Hitman (2015) (digital TPB) (Minutemen-Ganek).cbz
- `  206 MB`  Demon (2016)/Demon v01 (2016) (Digital) (mv-DCP).cbz

### distant soil — v1  *(volume)*

- `  311 MB`  A Distant Soil/A Distant Soil v01 - The Gathering (2013) (Digital) (XRA-Empire).cbz
- `  169 MB`  A Distant Soil/3. A Distant Soil 1- 14 [1991 - 1994] Aria Press/A Distant Soil v01.cbz
- `  161 MB`  A Distant Soil/1. A Distant Soil 1-9 [1983 - 1986] WaRP Graphics/A Distant Soil v01.cbz

### planetary — v1  *(volume)*

- `  431 MB`  Warren Ellis/Planetary/Planetary Book 01 (2017) (digital) (Son of Ultron-Empire).cbr
- `  184 MB`  Warren Ellis/Planetary/Planetary Vol 1 TPB (2000) GetComics.INFO.cbr

### james bond — #007  *(issue)*

- `  416 MB`  James Bond (2016)/James Bond 007 - Your Cold, Cold Heart (2025) (digital) (The Magicians-Empire).cbr
- `   37 MB`  James Bond (2016)/James Bond - 007 003 (2022) (4 covers) (digital) (Son of Ultron-Empire).cbr
- `   34 MB`  James Bond (2016)/James Bond - 007 006 (2023) (4 covers) (digital) (Son of Ultron-Empire).cbr
- `   33 MB`  James Bond (2016)/James Bond - 007 002 (2022) (4 covers) (digital) (Son of Ultron-Empire).cbr
- `   32 MB`  James Bond (2016)/James Bond - 007 004 (2022) (4 covers) (digital) (Son of Ultron-Empire).cbr
- `   31 MB`  James Bond (2016)/James Bond - 007 001 (2022) (4 covers) (digital) (Son of Ultron-Empire).cbr
- `   31 MB`  James Bond (2016)/James Bond - 007 005 (2022) (4 covers) (digital) (Son of Ultron-Empire).cbr

### wicked + divine — v1  *(volume)*

- `  506 MB`  The Wicked + The Divine/The Wicked + The Divine - Book 01 (01-11) (2016) GetComics.INFO.cbz
- `   99 MB`  The Wicked + The Divine/The Wicked + The Divine - v01 (2018).cbz

### moebius library inside moebius  *(issue)*

- `  279 MB`  Jodorowsky and Moebius/Moebius Library - Inside Moebius Part 01 (2018) (Digital) (Bean-Empire).cbz
- `  166 MB`  Jodorowsky and Moebius/Moebius Library - Inside Moebius Part 02 (2018) (Digital) (Bean-Empire).cbz
- `  159 MB`  Jodorowsky and Moebius/Moebius Library - Inside Moebius Part 03 (2018) (Dark Horse) (Digital-Empire).cbr

### d.r. & quinch  *(issue)*

- `  220 MB`  2000AD - Collections /The Complete D.R. & Quinch (2010) (digital-HD) (Ampersand).cbr
- `  136 MB`  Alan Moore/D.R. & Quinch/D.R. & Quinch.cbz
- `  136 MB`  Alan Moore/Alan Moore Collection I- English Invasion/Alan Moore Collection III- 2000 AD/2000 AD/2000 AD- Collections/D.R. & Quinch.cbr
- `   54 MB`  Alan Moore/Alan Moore Collection I- English Invasion/Alan Moore Collection III- 2000 AD/2000 AD/2000 AD- Reprints/D.R. & Quinch/The Complete D.R. & Quinch (Black & White).cbr
- `   54 MB`  2000AD prog/Alan Moore -2000AD/D.R. & Quinch.cbr

### star trek — v4  *(volume)*

- `  440 MB`  Star Trek/Star Trek v04 - Pleroma (2025) (digital) (The Magicians-Empire).cbr
- `  156 MB`  Star Trek/Star Trek (2012-2016)/Star Trek Vol. 04 (2013) (digital) (Minutemen-Slayer).cbr

### d'orc — v1  *(volume)*

- `  317 MB`  D'Orc/D'Orc v01 - The Book of Certain Doom (2026) (Digital) (DR & Quinch-Empire).cbr
- `  277 MB`  D'Orc/D'Orc v01 (2026).cbz

### extraordinary  *(issue)*

- `  199 MB`  Europe Comics (Collection)/The Extraordinary Part 001 - Orsay's Hands (2021) (digital) (Mr Norrell-Empire).cbr
- `  198 MB`  Europe Comics (Collection)/The Extraordinary Part 002 - Juliette's Eyes (2022) (digital) (Mr Norrell-Empire).cbr
- `  191 MB`  Europe Comics (Collection)/The Extraordinary Part 003 - Melek's Head (2023) (digital) (Mr Norrell-Empire).cbr

### unbeatable squirrel girl — v2  *(volume)*

- `  399 MB`  The Unbeatable Squirrel Girl/The Unbeatable Squirrel Girl Collection v02 (2017) (Digital) (Zone-Empire).cbr
- `  187 MB`  The Unbeatable Squirrel Girl/The Unbeatable Squirrel Girl v02 - Squirrel You Know It's True (2015) (digital) (Minuteman-Slayer).cbr

### planetary — v2  *(volume)*

- `  432 MB`  Warren Ellis/Planetary/Planetary Book 02 (2018) (digital) (Son of Ultron-Empire).cbr
- `  151 MB`  Warren Ellis/Planetary/Planetary Vol 2 TPB (2001) GetComics.INFO.cbr

### catwoman — v3  *(volume)*

- `  396 MB`  Catwoman/Catwoman v03 - Under Pressure (2014) (digital) (Son of Ultron-Empire).cbr
- `  187 MB`  Catwoman/Catwoman v03 - Friend or Foe (2020) (digital) (Son of Ultron-Empire).cbr

### skin police — v1  *(volume)*

- `  403 MB`  Skin Police/Skin Police v01 - Crimes Against Nature (2025) (digital) (Son of Ultron-Empire).cbr
- `  177 MB`  Skin Police/Skin Police 2 v01 (2025).cbz

### star trek — v5  *(volume)*

- `  451 MB`  Star Trek/Star Trek v05 - When the Walls Fell (2025) (digital) (The Magicians-Empire).cbr
- `  122 MB`  Star Trek/Star Trek (2012-2016)/Star Trek Vol. 05 (2013) (Digital) (TLK-EMPIRE-HD).cbr

### unbeatable squirrel girl — v3  *(volume)*

- `  330 MB`  The Unbeatable Squirrel Girl/The Unbeatable Squirrel Girl Collection v03 (2018) (Digital) (Zone-Empire).cbr
- `  242 MB`  The Unbeatable Squirrel Girl/The Unbeatable Squirrel Girl v03 - Squirrel You Really Got Me Now (2016) (digital) (Minuteman-Slayer).cbr

### miracleman  *(issue)*

- `  549 MB`  Alan Moore/Alan Moore Collection I- English Invasion/Alan Moore Collection III- 2000 AD/Miracleman/Miracleman- TPB/The Complete Miracleman- (Alan Moore).cbr
- `    8 MB`  Alan Moore/Alan Moore Essentials/Alan Moore 1984- Miracleman/Miracleman #008- (Non-Moore).cbr
- `    8 MB`  Alan Moore/Alan Moore Collection I- English Invasion/Alan Moore Collection III- 2000 AD/Miracleman/Miracleman/Miracleman #008- (Non-Moore).cbr

### unbeatable squirrel girl — v4  *(volume)*

- `  375 MB`  The Unbeatable Squirrel Girl/The Unbeatable Squirrel Girl Collection v04 (2019) (Digital) (Zone-Empire).cbr
- `  189 MB`  The Unbeatable Squirrel Girl/The Unbeatable Squirrel Girl v04 - I Kissed a Squirrel and I Liked It (2016) (digital) (Minuteman-Slayer).cbr

### die loaded — v1  *(volume)*

- `  347 MB`  Die/Die - Loaded v01 - Zero Sessions (2026) (Digital) (DR & Quinch-Empire).cbr
- `  215 MB`  Die - Loaded/Die - Loaded v01 (2025).cbz

### skizz  *(issue)*

- `  434 MB`  2000AD - Collections /The Complete Skizz (2017) (digital) (Ampersand).cbr
- `   63 MB`  2000AD prog/Alan Moore -2000AD/Skizz.cbr
- `   63 MB`  Alan Moore/Alan Moore Collection I- English Invasion/Alan Moore Collection III- 2000 AD/2000 AD/2000 AD- Collections/Skizz.cbr

### iron man — v4  *(volume)*

- `  317 MB`  Iron Man/Iron Man v04 - Books of Korvac IV - Source Control (2022) (20-25).cbz
- `  241 MB`  Iron Man/Iron Man Vol. 04 - Iron Metropolitan (2014) (digital) (Minutemen-Slayer).cbr

### gambit — v2  *(volume)*

- `  204 MB`  Gambit (001-017+)(2012-2013)(digital)(Minutemen-Excelsior)/Gambit v02.cbz
- `  177 MB`  Gambit (001-017+)(2012-2013)(digital)(Minutemen-Excelsior)/Gambit Vol. 02 - Tombstone Blues (2013) (digital) (Minutemen-Excelsior).cbz
- `  177 MB`  Gambit/Gambit Vol. 02 - Tombstone Blues (2013) (digital) (Minutemen-Excelsior).cbz

### demon — v2  *(volume)*

- `  399 MB`  Garth Ennis Collection/The Demon/The_Demon_v02__2016___Digital___danke-Empire_ (newcomic.info).cbz
- `  149 MB`  Demon (2016)/Demon v02 (2017) (Digital) (mv-DCP).cbz

### catwoman — v1  *(volume)*

- `  356 MB`  Catwoman/Catwoman v01 - Trail of the Catwoman (2011) (digital) (Son of Ultron-Empire).cbr
- `  131 MB`  Catwoman/Catwoman v01 - Copycats (2019) (digital) (Son of Ultron-Empire).cbr
- `   60 MB`  Catwoman/Catwoman v01 - Dangerous Liaisons (2022) (Digital-SD) (Dakota Scanning).cbz

### radiant black — v8  *(volume)*

- `  440 MB`  Radiant Black (2021)/Radiant Black v08 - New Number One (2026) (Digital) (DR & Quinch-Empire).cbr
- `  103 MB`  Radiant Black (2021)/Radiant Black v08 (2025).cbz

### star trek — v1  *(volume)*

- `  400 MB`  Star Trek/Star Trek v01 - Godshock (2023) (digital) (The Magicians-Empire).cbr
- `  132 MB`  Star Trek/Star Trek (2012-2016)/Star Trek Vol. 01 (2012) (digital) (Minutemen-Slayer).cbr

### daredevil by chip zdarsky — v1  *(volume)*

- `  312 MB`  Daredevil/Daredevil by Chip Zdarsky v01 - To Heaven Through Hell (2021) (Digital-Empire).cbr
- `  219 MB`  Daredevil/Daredevil by Chip Zdarsky v01 - Know Fear (2019) (Digital) (Zone-Empire).cbr

### james bond — v2  *(volume)*

- `  335 MB`  James Bond (2016)/James Bond - 007, Book 02 - For King and Country (2024) (digital) (The Magicians-Empire).cbr
- `  189 MB`  James Bond (2016)/James Bond v02 - Eidolon (2017) (digital) (The Magicians-Empire).cbr

### cable — v1  *(volume)*

- `  199 MB`  Cable (2020)/Cable v01 - Shining Path (2002) (Digital) (Kileko-Empire).cbz
- `  175 MB`  Cable (2020)/Cable v01 - Conquest (2017) (Digital) (F) (Zone-Empire).cbz
- `  148 MB`  Cable (2020)/Cable v01 - Messiah War (2009) (Digital) (F) (Asgard-Empire).cbz

### captain america — v4  *(volume)*

- `  262 MB`  Captain America/Captain America vol 1-5 (2019-2021)/Captain America v04 - All Die Young.cbz
- `  257 MB`  Captain America/Captain America Vol 7 (2013-2014)/Captain America Vol 4 - The Iron Nail (2014) (Digital HC) (BroadCast-Empire).cbz

### grey area — v1  — identical size  *(volume)*

- `  172 MB`  Dan Abnett/Grey Area v01 - This Island Earth (2017) GetComics.INFO.cbr
- `  172 MB`  2000AD - Collections /Grey Area/Grey Area v01 - This Island Earth (2017) GetComics.INFO.cbr
- `  172 MB`  2000AD - Collections /Grey Area/Grey Area v01 - This Island Earth (2017) (digital) (Torquemada).cbr

### civil war  *(issue)*

- `  257 MB`  Civil War Event (001-007+Tie-Ins,Trades&Extras)(2006-2008)(digital)/Trades/Civil War (2007) (digital) (Minutemen-Slayer).cbr
- `  257 MB`  Civil War Event (001-007+Tie-Ins,Trades&Extras)(2006-2008)(digital)/Civil War (Mark Millar 2007) .cbr
- `    0 MB`  Civil War Event (001-007+Tie-Ins,Trades&Extras)(2006-2008)(digital)/Extras/Variants/Civil War (6 of 7) (2007) (Michael Turner Sketch Variant) (Ori-DCP).cbr

### harley quinn — v4  *(volume)*

- `  272 MB`  Harley Quinn/Harley Quinn Vol. 2 (New 52) (v01-v06)(2014-2016)/Harley Quinn v04 - A Call to Arms (2016) (digital) (Son of Ultron-Empire).cbr
- `  238 MB`  Harley Quinn/Harley Quinn v04 - The Final Trial (2020) (digital) (Son of Ultron-Empire).cbr

### unbeatable squirrel girl — v1  *(volume)*

- `  334 MB`  The Unbeatable Squirrel Girl/The Unbeatable Squirrel Girl Collection v01 (2016) (Digital) (Zone-Empire).cbr
- `  170 MB`  The Unbeatable Squirrel Girl/The Unbeatable Squirrel Girl v01 - Squirrel Power (2015) (digital) (Minuteman-Slayer).cbr

### regular show — v6  *(volume)*

- `  332 MB`  Regular Show/Regular Show v06 - Comic Conned (2018) (digital) (Salem-Empire).cbr
- `  169 MB`  Regular Show/Regular Show v06 (2016) (Digital-Empire).cbr

### batman — v4  *(volume)*

- `  319 MB`  Batman/Batman Vol 4 The Cowardly Lot.cbz
- `  179 MB`  Batman/Batman (v01-v04)(2017)(digital)(Zone-Empire)/Batman v04 - The War of Jokes and Riddles (2017) (Digital) (Zone-Empire).cbr

### shock ghosts of knightgrave  *(issue)*

- `  209 MB`  Shock - The Ghosts of Knightgrave/Shock - The Ghosts of Knightgrave - Part One (F) (2014) (Scanlation) (phillywilly).cbr
- `  172 MB`  Shock - The Ghosts of Knightgrave/Shock - The Ghosts of Knightgrave - Part Two (F) (2015) (Scanlation) (phillywilly).cbr
- `  114 MB`  Shock - The Ghosts of Knightgrave/Shock - The Ghosts of Knightgrave - Part Three (2019) (Scanlation) (phillywilly).cbr

### star trek — v3  *(volume)*

- `  347 MB`  Star Trek/Star Trek v03 - Glass and Bone (2024) (digital) (The Magicians-Empire).cbr
- `  147 MB`  Star Trek/Star Trek (2012-2016)/Star Trek Vol. 03 (2012) (digital) (Minutemen-Slayer).cbr

### heavy metal — v35 — #02  *(volume)*

- `  153 MB`  Heavy Metal/Heavy Metal Vols 01-35 (1977-2012)/Heavy Metal v35 02 (2011-05).cbr
- `  153 MB`  Heavy Metal/01. Main Series/Heavy Metal v35 02 (2011-05).cbr
- `   93 MB`  Heavy Metal/Heavy Metal Vols 01-35 (1977-2012)/Heavy Metal v35 02 (2011) (Vague Prophet and Vapor Trail).cbr
- `   93 MB`  Heavy Metal/02. Specials/Heavy Metal V35 02 (2011) Living Dead Special.cbr

### silk — v1  *(volume)*

- `  298 MB`  Silk/Silk Vol01 - Sinister (2016) (Digital) (F) (Zone-Empire).cbr
- `  192 MB`  Silk/Silk v01 - Threats And Menaces (2021) (Digital-HD).cbz

### nancy drew — v1  *(volume)*

- `  280 MB`  Nancy Drew/Nancy Drew Omnibus v01 (2022) (digital) (Son of Ultron-Empire).cbr
- `  144 MB`  Nancy Drew/Nancy Drew v01 - The Palace of Wisdom (2019) (Digital) (mv-DCP).cbr
- `   61 MB`  Nancy Drew/Nancy Drew v01-07 (2005-2006)/Nancy Drew v01 - The Demon of River Heights (2005) (DCP-Digital).cbr

### secret avengers — v1  *(volume)*

- `  263 MB`  Avengers/Secret Avengers Vol. 1 - Let's Have A Problem (2014) (Digital) (Shanhara).cbz
- `  218 MB`  Avengers/Secret Avengers v01 - Reverie (2013) (Digital) (Kileko-Empire).cbr

### batman — v2  *(volume)*

- `  206 MB`  Batman/Batman v02 - The Joker War (2021) (Digital) (EJGriffin-Empire).cbz
- `  160 MB`  Batman/Batman (v01-v04)(2017)(digital)(Zone-Empire)/Batman v02 - I Am Suicide (2017) (Digital) (Zone-Empire).cbr
- `  114 MB`  Batman/Batman v02 - The Bat-Man of Gotham (2023) (digital-SD) (Dakota Scanning).cbz

### void rivals — v1  *(volume)*

- `  310 MB`  Robert Kirkman/Void Rivals (Kirkman 2023)/Void Rivals Vol. 1.cbz
- `  168 MB`  Void Rivals/Void Rivals v01 - More Than Meets the Eye (2024) (digital) (DrVink-HD-DCP).cbz

### gambit — v3  *(volume)*

- `  160 MB`  Gambit (001-017+)(2012-2013)(digital)(Minutemen-Excelsior)/Gambit Vol. 03 - King of Thieves (2013) (digital) (Minutemen-Excelsior).cbz
- `  160 MB`  Gambit/Gambit Vol. 03 - King of Thieves (2013) (digital) (Minutemen-Excelsior).cbz
- `  153 MB`  Gambit (001-017+)(2012-2013)(digital)(Minutemen-Excelsior)/Gambit v03.cbz

### hellblazer  *(special)*

- `  245 MB`  John Constantine, Hellblazer/Hellblazer Special - Bad Blood 001-004 (2000) (digital) (Marika-Empire).cbz
- `   76 MB`  John Constantine, Hellblazer/Hellblazer Special - Chas The Knowledge (2008).cbz
- `   48 MB`  John Constantine, Hellblazer/Hellblazer Special - Lady Constantine (01-04) (2003).cbz
- `   24 MB`  John Constantine, Hellblazer/Hellblazer Special - Confessional (1993) (groveman).cbr
- `   19 MB`  John Constantine, Hellblazer/Hellblazer Special - Constantine DVD Issue (2005).cbr
- `   18 MB`  Neil Gaiman Library/The Books of Magic (Neil Gaiman)/Hellblazer Special - The Books of Magic (01 - 02) (1997 + 1998) (Pudgy).cbz
- `   18 MB`  John Constantine, Hellblazer/Hellblazer Special - The Books of Magic (01 - 02) (1997 + 1998) (Pudgy).cbz
- `   15 MB`  John Constantine, Hellblazer/Hellblazer Special - Heartland (1997) (Obi).cbr

### goon — v1  *(volume)*

- `  261 MB`  The Goon/The Goon (2022) v01 - A Ragged Return to Lonely Street (2019) (01-04).cbr
- `  200 MB`  The Goon/The Goon v01 - Nothin' But Misery (2011) (Digital) (Zone-Empire).cbr

### batman earth one — v1  *(volume)*

- `  282 MB`  Earth One (TPB Collection) (2012-2018)/Batman - Earth One v01 (2012) GetComics INFO/Batman - Earth One v01 (2012) GetComics.INFO.cbr
- `  169 MB`  Batman/Batman - Earth One v1 (2012) (digital) (Minutemen-PhD).cbr

### drifter — v1  *(volume)*

- `  228 MB`  Drifter/Drifter v01.cbz
- `  214 MB`  Drifter/Drifter v01 - Out of the Night (2015) (Digital) (Zone-Empire).cbr

### captain america — v3  *(volume)*

- `  230 MB`  Captain America/Captain America vol 1-5 (2019-2021)/Captain America v03 - The Legend of Steve (2020) (Digital) (Zone-Empire).cbr
- `  210 MB`  Captain America/Captain America Vol 7 (2013-2014)/Captain America Vol 3 - Loose Nuke v3 (2014) (Digital-TPB) (BlackManta-Empire).cbr

### silk — v2  *(volume)*

- `  248 MB`  Silk/Silk Vol02 - The Negative (2017) (Digital) (Zone-Empire).cbr
- `  192 MB`  Silk/Silk v02 - Age Of The Witch (2022) (Digital-HD).cbz

### resident alien — v2  *(volume)*

- `  322 MB`  Resident Alien/Resident Alien Omnibus v02 (2023) (digital) (DrVink-DCP).cbz
- `  114 MB`  Resident Alien/Resident Alien v02 - The Suicide Blonde (2014) (digital) (Mr Norrell-Empire).cbr

### orville  *(issue)*

- `  201 MB`  The Orville/The Orville Season 1.5 - New Beginnings (2020) (digital) (Son of Ultron-Empire).cbr
- `  122 MB`  The Orville/The Orville Season 2.5 - Digressions (2022) (digital) (Son of Ultron-Empire).cbr
- `  114 MB`  The Orville/The Orville Season 2.5 - Launch Day (2021) (digital) (Son of Ultron-Empire).cbr

### iron man — v2  *(volume)*

- `  230 MB`  Iron Man/Iron Man Vol. 02 - The Secret Origin of Tony Stark Book 1 (2013) (digital) (Minutemen-Slayer).cbr
- `  205 MB`  Iron Man/Iron Man v02 - Books of Korvac II - Overclock (2021) (Digital-Empire).cbr

### cable — v2  *(volume)*

- `  231 MB`  Cable (2020)/Cable v02 - The End (2002) (Digital) (Kileko-Empire).cbz
- `  203 MB`  Cable (2020)/Cable v02 - Waiting For the End of the World (2009) (Digital) (Asgard-Empire).cbr

### iron man — v1  *(volume)*

- `  243 MB`  Iron Man/Iron Man Vol. 01 - Believe (2013) (Digital HC) (BroadCast-Empire) (newcomic.org).cbr
- `  187 MB`  Iron Man/Iron Man v01 - Books of Korvac I - Big Iron (2021) (Digital-Empire).cbr

### harley quinn — v6  *(volume)*

- `  226 MB`  Harley Quinn/Harley Quinn Vol. 2 (New 52) (v01-v06)(2014-2016)/Harley Quinn v06 - Black, White and Red All Over (2016) (digital) (Son of Ultron-Empire).cbr
- `  203 MB`  Harley Quinn/Harley Quinn Vol. 3 (Rebirth) – TPB Vol. 1 – 6 (2017-2018)/Harley Quinn (2016-) - v06 - Angry Bird (2018) (digital) (Son of Ultron-Empire).cbr

### scarlet traces — v1  — identical size  *(volume)*

- `  212 MB`  Scarlet Traces/Scarlet Traces v01 (2017) GetComics.INFO.cbr
- `  212 MB`  2000AD - Collections /Scarlet Traces/Scarlet Traces v01 (2017) (F) (digital) (Torquemada).cbr

### barbarella — v2  *(volume)*

- `  216 MB`  Barbarella (2021)/Barbarella v02 - Hard Labor (2019) (Digital) (DR & Quinch-Empire).cbr
- `  201 MB`  Barbarella (2021)/Barbarella - v02 (2023) (Digital) (DR & Quinch-Empire).cbz

### distant soil — v2  *(volume)*

- `  342 MB`  A Distant Soil/A Distant Soil v02 - The Ascendant (2014) (Digital) (XRA-Empire).cbz
- `   73 MB`  A Distant Soil/2. A Distant Soil - [1987 - 1989] Starblaze Graphics/A Distant Soil Vol.02 - Knights of the Angel TPB (Starblaze).cbz

### resident alien — v1  *(volume)*

- `  297 MB`  Resident Alien/Resident Alien Omnibus v01 (2020) (digital) (Son of Ultron-Empire).cbr
- `  112 MB`  Resident Alien/Resident Alien v01 - Welcome to Earth! (2013) (digital) (Mr Norrell-Empire).cbr

### james bond — v1 — #007  *(volume)*

- `  309 MB`  James Bond (2016)/James Bond 007 v01 (2019) (digital) (The Magicians-Empire).cbr
- `   98 MB`  James Bond (2016)/James Bond 007 (Titan Books)(2007)/James Bond 007 Book 1 The Man with the Golden Gun (Titan Books 2004) (MickRC).cbr

### brink — v3  *(volume)*

- `  154 MB`  Dan Abnett/Brink/Brink V3 High Society (Dan Dare 2000AD Remix).cbr
- `  154 MB`  2000AD - Collections /Brink/Brink V3 High Society (Dan Dare 2000AD Remix).cbr
- `   97 MB`  Brink - Book 01-06 (2017-2026) (digital) (Torquemada)/Brink - Book 03 (2019) (digital) (Torquemada).cbr

### secret avengers — v2  *(volume)*

- `  222 MB`  Avengers/Secret Avengers v02 - Iliad (2014) (Digital) (Kileko-Empire).cbr
- `  175 MB`  Avengers/Secret Avengers Vol. 2 - The Labyrinth (2015) (Digital) (Shanhara).cbz

### doom patrol — v2  *(volume)*

- `   48 MB`  Grant Morrison/Comics/Doom Patrol/Doom Patrol v2 017a - Invasion #2.cbz
- `   46 MB`  Grant Morrison/Comics/Doom Patrol/Doom Patrol v2 018a - Invasion #3.cbz
- `   18 MB`  Grant Morrison/Comics/Doom Patrol/Doom Patrol v2 006a - Doom Patrol And Suicide Squad Special 001.cbr
- `   17 MB`  Grant Morrison/Comics/Doom Patrol/Doom Patrol V2 - 57.cbr
- `   15 MB`  Grant Morrison/Comics/Doom Patrol/Doom Patrol v2 014a - Doom Patrol v2 Annual 001.cbr
- `   14 MB`  Grant Morrison/Comics/Doom Patrol/Doom Patrol V2 - 37.cbr
- `   13 MB`  Grant Morrison/Comics/Doom Patrol/Doom Patrol V2 - 41.cbr
- `   12 MB`  Grant Morrison/Comics/Doom Patrol/Doom Patrol v2 010a - Superman v2 020.cbz
- `   11 MB`  Grant Morrison/Comics/Doom Patrol/Doom Patrol V2 - 60.cbr
- `   11 MB`  Grant Morrison/Comics/Doom Patrol/Doom Patrol V2 - 59.cbr
- `   11 MB`  Grant Morrison/Comics/Doom Patrol/Doom Patrol V2 - 46.cbr
- `   11 MB`  Grant Morrison/Comics/Doom Patrol/Doom Patrol V2 - 44.cbr
- `   11 MB`  Grant Morrison/Comics/Doom Patrol/Doom Patrol V2 - 50.cbr
- `   10 MB`  Grant Morrison/Comics/Doom Patrol/Doom Patrol V2 - 36.cbr
- `   10 MB`  Grant Morrison/Comics/Doom Patrol/Doom Patrol V2 - 38.cbr
- `   10 MB`  Grant Morrison/Comics/Doom Patrol/Doom Patrol V2 - 45.cbr
- `   10 MB`  Grant Morrison/Comics/Doom Patrol/Doom Patrol V2 - 53.cbr
- `    9 MB`  Grant Morrison/Comics/Doom Patrol/Doom Patrol V2 - 39.cbr
- `    9 MB`  Grant Morrison/Comics/Doom Patrol/Doom Patrol V2 - 52.cbr
- `    9 MB`  Grant Morrison/Comics/Doom Patrol/Doom Patrol V2 - 63.cbr
- `    8 MB`  Grant Morrison/Comics/Doom Patrol/Doom Patrol V2 - 40.cbr
- `    8 MB`  Grant Morrison/Comics/Doom Patrol/Doom Patrol V2 - 56.cbr
- `    7 MB`  Grant Morrison/Comics/Doom Patrol/Doom Patrol V2 - 47.cbr
- `    7 MB`  Grant Morrison/Comics/Doom Patrol/Doom Patrol V2 - 55.cbr
- `    7 MB`  Grant Morrison/Comics/Doom Patrol/Doom Patrol V2 - 54.cbr
- `    7 MB`  Grant Morrison/Comics/Doom Patrol/Doom Patrol V2 - 62.cbr
- `    7 MB`  Grant Morrison/Comics/Doom Patrol/Doom Patrol V2 - 61.cbr
- `    7 MB`  Grant Morrison/Comics/Doom Patrol/Doom Patrol V2 - 48.cbr
- `    7 MB`  Grant Morrison/Comics/Doom Patrol/Doom Patrol V2 - 58.cbr
- `    6 MB`  Grant Morrison/Comics/Doom Patrol/Doom Patrol V2 - 49.cbr
- `    6 MB`  Grant Morrison/Comics/Doom Patrol/Doom Patrol V2 - 51.cbr
- `    6 MB`  Grant Morrison/Comics/Doom Patrol/Doom Patrol V2 - 43.cbr
- `    5 MB`  Grant Morrison/Comics/Doom Patrol/Doom Patrol V2 - 42.cbr

### batman earth one — v2  *(volume)*

- `  196 MB`  Earth One (TPB Collection) (2012-2018)/Batman - Earth One v02 (2015) GetComics.INFO.cbr
- `  196 MB`  Batman/Batman - Earth One v2 (2015) (webrip) (Worldbreaker-DCP).cbr

### captain america — v5  *(volume)*

- `  232 MB`  Captain America/Captain America Vol 7 (2013-2014)/Captain America Vol 5 - The Tomorrow Soldier (2014) (Digital HC) (BroadCast-Empire).cbz
- `  151 MB`  Captain America/Captain America vol 1-5 (2019-2021)/Captain America v05 - All Die Young - Part Two (2022) (Digital) (EJGriffin-Empire).cbz

### locus year — v1  *(volume)*

- `  189 MB`  Locus Year/Locus Year 1 v01 (2012).cbz
- `  185 MB`  Locus Year/Locus Year 2 v01 (2012).cbz

### goon — v3  *(volume)*

- `  204 MB`  The Goon/The Goon (2022) v03 - Fishy Men, Witchy Women, Bitter Beer.cbz
- `  160 MB`  The Goon/The Goon v03 - Heaps of Ruination (2011, 2nd edition) (digital) (The Magicians-Empire).cbr

### james bond — v1  *(volume)*

- `  232 MB`  James Bond (2016)/James Bond v01 - Vargr (1-6) (2016) (digital) (The Magicians-Empire).cbr
- `  129 MB`  James Bond (2016)/James Bond - 007, Book 01 - Myrmidon (2024) (digital) (DrVink-DCP).cbz

### secret avengers — v3  *(volume)*

- `  189 MB`  Avengers/Secret Avengers v03 - How To Maim A Mockingbird (2014) (Digital) (Kileko-Empire).cbr
- `  172 MB`  Avengers/Secret Avengers Vol. 3 - God Level (2015) (Digital) (Shanhara).cbz

### corto maltese — #15  — identical size  *(issue)*

- `  176 MB`  Hugo Pratt/Corto Maltese 15 - Under the Midnight Sun (Canales-Pellejero, 2015) (edition 1.5) (Scanlation-Extended, 2018).cbr
- `  176 MB`  Corto Maltese/Corto Maltese 01-16/Corto Maltese 15 - Under the Midnight Sun _Canales-Pellejero_ 2015_ _edition 1.5_ _Scanlation-Extended_ 2018_ (newcomic.info).cbr

### kaijumax  *(issue)*

- `  193 MB`  Kaijumax/Kaijumax Season Five - The Orange Mile (2021) (digital-Empire).cbr
- `  157 MB`  Kaijumax/Kaijumax Season Six - For All Mankind (2022) (digital) (DrVink).cbz

### goon — v2  *(volume)*

- `  176 MB`  The Goon/The Goon (2022) v02 - The Deceit of a Cro-Magnon Dandy.cbz
- `  172 MB`  The Goon/The Goon v02 - My Murderous Childhood (and Other Grievous Yarns) (2010, 2nd edition) (digital) (The Magicians-Empire).cbr

### jin c001 006  *(issue)*

- `  281 MB`  Manga/Jin/Jin - c001-006 (v01) [Patreon].cbz
- `   66 MB`  Manga/Jin/Jin - c001-006 (v01) [Easy Going].cbz

### sidekicks — v2  *(volume)*

- `    6 MB`  Manga/SIDEKICKS manga/Sidekicks vol.002 ch.130 [KissManga].cbz
- `    6 MB`  Manga/SIDEKICKS manga/Sidekicks vol.002 ch.122 [KissManga].cbz
- `    6 MB`  Manga/SIDEKICKS manga/Sidekicks vol.002 ch.113 [KissManga].cbz
- `    6 MB`  Manga/SIDEKICKS manga/Sidekicks vol.002 ch.124 [KissManga].cbz
- `    6 MB`  Manga/SIDEKICKS manga/Sidekicks vol.002 ch.118 [KissManga].cbz
- `    6 MB`  Manga/SIDEKICKS manga/Sidekicks vol.002 ch.111 [KissManga].cbz
- `    6 MB`  Manga/SIDEKICKS manga/Sidekicks vol.002 ch.121 [KissManga].cbz
- `    6 MB`  Manga/SIDEKICKS manga/Sidekicks vol.002 ch.129 [KissManga].cbz
- `    6 MB`  Manga/SIDEKICKS manga/Sidekicks vol.002 ch.126 [KissManga].cbz
- `    6 MB`  Manga/SIDEKICKS manga/Sidekicks vol.002 ch.127 [KissManga].cbz
- `    6 MB`  Manga/SIDEKICKS manga/Sidekicks vol.002 ch.119 [KissManga].cbz
- `    5 MB`  Manga/SIDEKICKS manga/Sidekicks vol.002 ch.107 [KissManga].cbz
- `    5 MB`  Manga/SIDEKICKS manga/Sidekicks vol.002 ch.114 [KissManga].cbz
- `    5 MB`  Manga/SIDEKICKS manga/Sidekicks vol.002 ch.120 [KissManga].cbz
- `    5 MB`  Manga/SIDEKICKS manga/Sidekicks vol.002 ch.123 [KissManga].cbz
- `    5 MB`  Manga/SIDEKICKS manga/Sidekicks vol.002 ch.128 [KissManga] (1).cbz
- `    5 MB`  Manga/SIDEKICKS manga/Sidekicks vol.002 ch.109 [KissManga].cbz
- `    5 MB`  Manga/SIDEKICKS manga/Sidekicks vol.002 ch.116 [KissManga].cbz
- `    5 MB`  Manga/SIDEKICKS manga/Sidekicks vol.002 ch.125 [KissManga].cbz
- `    5 MB`  Manga/SIDEKICKS manga/Sidekicks vol.002 ch.117 [KissManga].cbz
- `    5 MB`  Manga/SIDEKICKS manga/Sidekicks vol.002 ch.108 [KissManga].cbz
- `    5 MB`  Manga/SIDEKICKS manga/Sidekicks vol.002 ch.061 [KissManga].cbz
- `    5 MB`  Manga/SIDEKICKS manga/Sidekicks vol.002 ch.112 [KissManga].cbz
- `    5 MB`  Manga/SIDEKICKS manga/Sidekicks vol.002 ch.104 [KissManga].cbz
- `    5 MB`  Manga/SIDEKICKS manga/Sidekicks vol.002 ch.051 [KissManga].cbz
- `    5 MB`  Manga/SIDEKICKS manga/Sidekicks vol.002 ch.064 [KissManga].cbz
- `    5 MB`  Manga/SIDEKICKS manga/Sidekicks vol.002 ch.063 [KissManga].cbz
- `    5 MB`  Manga/SIDEKICKS manga/Sidekicks vol.002 ch.073 [KissManga].cbz
- `    5 MB`  Manga/SIDEKICKS manga/Sidekicks vol.002 ch.105 [KissManga].cbz
- `    5 MB`  Manga/SIDEKICKS manga/Sidekicks vol.002 ch.115 [KissManga].cbz
- `    5 MB`  Manga/SIDEKICKS manga/Sidekicks vol.002 ch.100 [KissManga].cbz
- `    5 MB`  Manga/SIDEKICKS manga/Sidekicks vol.002 ch.086 [KissManga].cbz
- `    4 MB`  Manga/SIDEKICKS manga/Sidekicks vol.002 ch.092 [KissManga].cbz
- `    4 MB`  Manga/SIDEKICKS manga/Sidekicks vol.002 ch.089 [KissManga].cbz
- `    4 MB`  Manga/SIDEKICKS manga/Sidekicks vol.002 ch.098 [KissManga].cbz
- `    4 MB`  Manga/SIDEKICKS manga/Sidekicks vol.002 ch.103 [KissManga].cbz
- `    4 MB`  Manga/SIDEKICKS manga/Sidekicks vol.002 ch.091 [KissManga].cbz
- `    4 MB`  Manga/SIDEKICKS manga/Sidekicks vol.002 ch.059 [KissManga].cbz
- `    4 MB`  Manga/SIDEKICKS manga/Sidekicks vol.002 ch.099 [KissManga].cbz
- `    4 MB`  Manga/SIDEKICKS manga/Sidekicks vol.002 ch.101 [KissManga].cbz
- `    4 MB`  Manga/SIDEKICKS manga/Sidekicks vol.002 ch.053 [KissManga].cbz
- `    4 MB`  Manga/SIDEKICKS manga/Sidekicks vol.002 ch.090 [KissManga].cbz
- `    4 MB`  Manga/SIDEKICKS manga/Sidekicks vol.002 ch.096 [KissManga].cbz
- `    4 MB`  Manga/SIDEKICKS manga/Sidekicks vol.002 ch.067 [KissManga].cbz
- `    4 MB`  Manga/SIDEKICKS manga/Sidekicks vol.002 ch.095 [KissManga].cbz
- `    4 MB`  Manga/SIDEKICKS manga/Sidekicks vol.002 ch.072 [KissManga].cbz
- `    4 MB`  Manga/SIDEKICKS manga/Sidekicks vol.002 ch.084 [KissManga].cbz
- `    4 MB`  Manga/SIDEKICKS manga/Sidekicks vol.002 ch.093 [KissManga].cbz
- `    4 MB`  Manga/SIDEKICKS manga/Sidekicks vol.002 ch.087 [KissManga].cbz
- `    4 MB`  Manga/SIDEKICKS manga/Sidekicks vol.002 ch.094 [KissManga].cbz
- `    4 MB`  Manga/SIDEKICKS manga/Sidekicks vol.002 ch.066 [KissManga].cbz
- `    4 MB`  Manga/SIDEKICKS manga/Sidekicks vol.002 ch.062 [KissManga].cbz
- `    4 MB`  Manga/SIDEKICKS manga/Sidekicks vol.002 ch.054 [KissManga].cbz
- `    4 MB`  Manga/SIDEKICKS manga/Sidekicks vol.002 ch.102 [KissManga].cbz
- `    4 MB`  Manga/SIDEKICKS manga/Sidekicks vol.002 ch.055 [KissManga].cbz
- `    4 MB`  Manga/SIDEKICKS manga/Sidekicks vol.002 ch.106 [KissManga].cbz
- `    4 MB`  Manga/SIDEKICKS manga/Sidekicks vol.002 ch.060 [KissManga].cbz
- `    4 MB`  Manga/SIDEKICKS manga/Sidekicks vol.002 ch.052 [KissManga].cbz
- `    4 MB`  Manga/SIDEKICKS manga/Sidekicks vol.002 ch.083 [KissManga].cbz
- `    3 MB`  Manga/SIDEKICKS manga/Sidekicks vol.002 ch.085 [KissManga].cbz
- `    3 MB`  Manga/SIDEKICKS manga/Sidekicks vol.002 ch.075 [KissManga].cbz
- `    3 MB`  Manga/SIDEKICKS manga/Sidekicks vol.002 ch.082 [KissManga].cbz
- `    3 MB`  Manga/SIDEKICKS manga/Sidekicks vol.002 ch.076 [KissManga].cbz
- `    3 MB`  Manga/SIDEKICKS manga/Sidekicks vol.002 ch.097 [KissManga].cbz
- `    3 MB`  Manga/SIDEKICKS manga/Sidekicks vol.002 ch.056 [KissManga].cbz
- `    3 MB`  Manga/SIDEKICKS manga/Sidekicks vol.002 ch.071 [KissManga].cbz
- `    3 MB`  Manga/SIDEKICKS manga/Sidekicks vol.002 ch.079 [KissManga].cbz
- `    3 MB`  Manga/SIDEKICKS manga/Sidekicks vol.002 ch.079 v002 [KissManga].cbz
- `    3 MB`  Manga/SIDEKICKS manga/Sidekicks vol.002 ch.070 [KissManga].cbz
- `    3 MB`  Manga/SIDEKICKS manga/Sidekicks vol.002 ch.065 [KissManga].cbz
- `    3 MB`  Manga/SIDEKICKS manga/Sidekicks vol.002 ch.058 [KissManga].cbz
- `    3 MB`  Manga/SIDEKICKS manga/Sidekicks vol.002 ch.068 [KissManga].cbz
- `    3 MB`  Manga/SIDEKICKS manga/Sidekicks vol.002 ch.088 [KissManga].cbz
- `    3 MB`  Manga/SIDEKICKS manga/Sidekicks vol.002 ch.078 [KissManga].cbz
- `    3 MB`  Manga/SIDEKICKS manga/Sidekicks vol.002 ch.069 [KissManga].cbz
- `    3 MB`  Manga/SIDEKICKS manga/Sidekicks vol.002 ch.057 [KissManga].cbz
- `    3 MB`  Manga/SIDEKICKS manga/Sidekicks vol.002 ch.081 [KissManga].cbz
- `    3 MB`  Manga/SIDEKICKS manga/Sidekicks vol.002 ch.080 [KissManga].cbz
- `    3 MB`  Manga/SIDEKICKS manga/Sidekicks vol.002 ch.080 v002 [KissManga].cbz
- `    3 MB`  Manga/SIDEKICKS manga/Sidekicks vol.002 ch.074 [KissManga].cbz
- `    2 MB`  Manga/SIDEKICKS manga/Sidekicks vol.002 ch.050 [KissManga].cbz

### best of 2000ad  *(special)*

- `   65 MB`  2000AD prog/2000AD (Specials, Annuals & Poster Progs + Extras)/2000AD Yearbooks & Specials (1977 - 2013)/Specials (-JJ-)/Best of 2000AD Special Edition 1994.cbr
- `   59 MB`  2000AD prog/Yearbooks & Specials/Specials/Best of 2000AD Special (1999).cbr
- `   59 MB`  2000AD prog/2000AD (Specials, Annuals & Poster Progs + Extras)/2000AD Yearbooks & Specials (1977 - 2013)/Specials (-JJ-)/Best of 2000AD Special Edition 1999.cbr
- `   54 MB`  2000AD prog/2000AD (Specials, Annuals & Poster Progs + Extras)/2000AD Yearbooks & Specials (1977 - 2013)/Specials (-JJ-)/Best of 2000AD Special Edition 1993.cbr
- `   52 MB`  2000AD prog/Yearbooks & Specials/Specials/Best of 2000AD Special (2000).cbr
- `   52 MB`  2000AD prog/2000AD (Specials, Annuals & Poster Progs + Extras)/2000AD Yearbooks & Specials (1977 - 2013)/Specials (-JJ-)/Best of 2000AD Special Edition 2000.cbr

### monster  *(issue)*

- `  169 MB`  Giant Monster (2007).cbr
- `   83 MB`  Monster (2016) (digital) (Torquemada).cbr
- `   83 MB`  2000AD - Collections /Monster (2016) (digital) (Torquemada).cbr

### sleeper  *(issue)*

- `  220 MB`  Sleeper - Season Two 001-012 (2004-2005) (digital-Empire)/Sleeper - Season Two 001-012 (2004-2005) (digital-Empire).cbz
- `  114 MB`  Sleeper - Season One 01-12 (2003) (digital) (Minutemen-Annika)/Sleeper - Season One 01-12 (2003) (digital) (Minutemen-Annika).cbz

### brink — v6  *(volume)*

- `  189 MB`  Brink - Book 01-06 (2017-2026) (digital) (Torquemada)/Brink - Book 06 (2026) (digital) (Torquemada).cbz
- `  145 MB`  2000AD - Collections /Brink/Brink V6 - Consumed (inc 2405).cbz

### jin c013 018  *(issue)*

- `  255 MB`  Manga/Jin/Jin - c013-018 (v03) [Patreon].cbz
- `   72 MB`  Manga/Jin/Jin - c013-018 (v03) [Easy Going].cbz

### brink — v4  *(volume)*

- `  112 MB`  Dan Abnett/Brink/Brink V4 Hate Box (Dan Dare 2000AD Remix).cbr
- `  112 MB`  2000AD - Collections /Brink/Brink V4 Hate Box (Dan Dare 2000AD Remix).cbr
- `  101 MB`  Brink - Book 01-06 (2017-2026) (digital) (Torquemada)/Brink - Book 04 (2021) (digital) (Torquemada).cbr

### preacher  *(special)*

- `   58 MB`  Preacher/Preacher Specials/Preacher Special - The Good Old Boys.cbr
- `   55 MB`  Preacher/Preacher Specials/Preacher Special - The Story of You-Know-Who.cbr
- `   46 MB`  Preacher/Preacher Specials/Preacher Special - Tall in The Saddle.cbr
- `   29 MB`  Preacher/Preacher Specials/Preacher Special - Saint of Killers 01.cbr
- `   29 MB`  Preacher/Preacher Specials/Preacher Special - Saint of Killers 04.cbr
- `   27 MB`  Preacher/Preacher Specials/Preacher Special - One Man_s War.cbr
- `   27 MB`  Preacher/Preacher Specials/Preacher Special - One Man's War.cbr
- `   27 MB`  Preacher/Preacher Specials/Preacher Special - Saint of Killers 03.cbr
- `   27 MB`  Preacher/Preacher Specials/Preacher Special - Saint of Killers 02.cbr

### batman beyond — v3  *(volume)*

- `  163 MB`  Batman/Batman Beyond (v01-v03)(2016-2017)(digital)(Son of Ultron-Empire)/Batman Beyond v03 - Wired for Death (2017) (digital) (Son of Ultron-Empire).cbr
- `  159 MB`  Batman/Batman Beyond v03 - The Long Payback (2018) (digital) (Son of Ultron-Empire).cbr

### druillet chaos  *(issue)*

- `  163 MB`  Philippe Druillet/Druillet - Chaos part 2 (Lone Sloane).cbr
- `  159 MB`  Philippe Druillet/Druillet - Chaos part 1 (Lone Sloane).cbr

### republic of skull  *(issue)*

- `  190 MB`  Europe Comics (Collection)/Republic of the Skull Part 02 (2022) (digital) (Mr Norrell-Empire).cbr
- `  121 MB`  Europe Comics (Collection)/Republic of the Skull Part 01 (2022) (digital) (Mr Norrell-Empire).cbr

### metal hurlant — v2  *(volume)*

- `  114 MB`  Metal Hurlant Collection/Metal Hurlant Collection v02 p002 (2011) GetComics.INFO.cbr
- `  103 MB`  Metal Hurlant Collection/Metal Hurlant Collection v02 p003 (2011) GetComics.INFO.cbr
- `   91 MB`  Metal Hurlant Collection/Metal Hurlant Collection v02 p001 (2011) GetComics.INFO.cbr

### brink — v1  *(volume)*

- `  109 MB`  Dan Abnett/Brink/Brink V1 (Dan Dare 2000AD Remix).cbr
- `  109 MB`  2000AD - Collections /Brink/Brink V1 (Dan Dare 2000AD Remix).cbr
- `   85 MB`  Brink - Book 01-06 (2017-2026) (digital) (Torquemada)/Brink - Book 01 [Rebellion] (2017) (Digital) (Torquemada).cbr

### think tank — v2  *(volume)*

- `  212 MB`  Think Tank/Think Tank v2 (2013) (digital) (Minutemen-Annika).cbr
- `   92 MB`  Think Tank/Think Tank v2 Private Equity (2008) (Sosich).cbr

### days of sand  *(issue)*

- `  176 MB`  Europe Comics (Collection)/Days of Sand - Part 02 (2021) (Europe Comics) (Mr Norrell-Empire).cbr
- `  126 MB`  Europe Comics (Collection)/Days of Sand - Part 01 (2021) (Europe Comics) (Mr Norrell-Empire).cbr

### nottingham — v1  *(volume)*

- `  216 MB`  Nottingham/Nottingham v01 - Death and Taxes (2021) (Digital) (DR & Quinch-Empire).cbr
- `   76 MB`  Nottingham/Nottingham (Cinebook)v01 - The King's Ransom (2022).cbr

### sidekicks — v1  *(volume)*

- `    8 MB`  Manga/SIDEKICKS manga/Sidekicks vol.001 ch.033 [KissManga].cbz
- `    8 MB`  Manga/SIDEKICKS manga/Sidekicks vol.001 ch.049 [KissManga].cbz
- `    7 MB`  Manga/SIDEKICKS manga/Sidekicks vol.001 ch.020 [KissManga].cbz
- `    7 MB`  Manga/SIDEKICKS manga/Sidekicks vol.001 ch.023 [KissManga].cbz
- `    7 MB`  Manga/SIDEKICKS manga/Sidekicks vol.001 ch.021 [KissManga].cbz
- `    7 MB`  Manga/SIDEKICKS manga/Sidekicks vol.001 ch.029 [KissManga].cbz
- `    7 MB`  Manga/SIDEKICKS manga/Sidekicks vol.001 ch.028 [KissManga].cbz
- `    7 MB`  Manga/SIDEKICKS manga/Sidekicks vol.001 ch.025 [KissManga].cbz
- `    7 MB`  Manga/SIDEKICKS manga/Sidekicks vol.001 ch.002 [KissManga].cbz
- `    7 MB`  Manga/SIDEKICKS manga/Sidekicks vol.001 ch.046 [KissManga].cbz
- `    7 MB`  Manga/SIDEKICKS manga/Sidekicks vol.001 ch.031 [KissManga].cbz
- `    7 MB`  Manga/SIDEKICKS manga/Sidekicks vol.001 ch.032 [KissManga].cbz
- `    7 MB`  Manga/SIDEKICKS manga/Sidekicks vol.001 ch.022 [KissManga].cbz
- `    6 MB`  Manga/SIDEKICKS manga/Sidekicks vol.001 ch.040 [KissManga].cbz
- `    6 MB`  Manga/SIDEKICKS manga/Sidekicks vol.001 ch.039 [KissManga].cbz
- `    6 MB`  Manga/SIDEKICKS manga/Sidekicks vol.001 ch.037 [KissManga].cbz
- `    6 MB`  Manga/SIDEKICKS manga/Sidekicks vol.001 ch.035 [KissManga].cbz
- `    6 MB`  Manga/SIDEKICKS manga/Sidekicks vol.001 ch.044 [KissManga].cbz
- `    6 MB`  Manga/SIDEKICKS manga/Sidekicks vol.001 ch.030 [KissManga].cbz
- `    6 MB`  Manga/SIDEKICKS manga/Sidekicks vol.001 ch.047 [KissManga].cbz
- `    6 MB`  Manga/SIDEKICKS manga/Sidekicks vol.001 ch.024 [KissManga].cbz
- `    6 MB`  Manga/SIDEKICKS manga/Sidekicks vol.001 ch.034 [KissManga].cbz
- `    6 MB`  Manga/SIDEKICKS manga/Sidekicks vol.001 ch.001 [KissManga].cbz
- `    6 MB`  Manga/SIDEKICKS manga/Sidekicks vol.001 ch.026 [KissManga].cbz
- `    6 MB`  Manga/SIDEKICKS manga/Sidekicks vol.001 ch.041 [KissManga].cbz
- `    6 MB`  Manga/SIDEKICKS manga/Sidekicks vol.001 ch.045 [KissManga].cbz
- `    6 MB`  Manga/SIDEKICKS manga/Sidekicks vol.001 ch.036 [KissManga].cbz
- `    6 MB`  Manga/SIDEKICKS manga/Sidekicks vol.001 ch.011 [KissManga].cbz
- `    6 MB`  Manga/SIDEKICKS manga/Sidekicks vol.001 ch.003 [KissManga].cbz
- `    6 MB`  Manga/SIDEKICKS manga/Sidekicks vol.001 ch.038 [KissManga].cbz
- `    5 MB`  Manga/SIDEKICKS manga/Sidekicks vol.001 ch.004 [KissManga].cbz
- `    5 MB`  Manga/SIDEKICKS manga/Sidekicks vol.001 ch.014 [KissManga].cbz
- `    5 MB`  Manga/SIDEKICKS manga/Sidekicks vol.001 ch.042 [KissManga].cbz
- `    5 MB`  Manga/SIDEKICKS manga/Sidekicks vol.001 ch.017 [KissManga].cbz
- `    5 MB`  Manga/SIDEKICKS manga/Sidekicks vol.001 ch.043 [KissManga].cbz
- `    5 MB`  Manga/SIDEKICKS manga/Sidekicks vol.001 ch.000 [KissManga].cbz
- `    5 MB`  Manga/SIDEKICKS manga/Sidekicks vol.001 ch.019 [KissManga].cbz
- `    5 MB`  Manga/SIDEKICKS manga/Sidekicks vol.001 ch.027 [KissManga].cbz
- `    5 MB`  Manga/SIDEKICKS manga/Sidekicks vol.001 ch.005 [KissManga].cbz
- `    5 MB`  Manga/SIDEKICKS manga/Sidekicks vol.001 ch.006 [KissManga].cbz
- `    5 MB`  Manga/SIDEKICKS manga/Sidekicks vol.001 ch.012 [KissManga].cbz
- `    5 MB`  Manga/SIDEKICKS manga/Sidekicks vol.001 ch.018 [KissManga].cbz
- `    5 MB`  Manga/SIDEKICKS manga/Sidekicks vol.001 ch.015 [KissManga].cbz
- `    5 MB`  Manga/SIDEKICKS manga/Sidekicks vol.001 ch.013 [KissManga].cbz
- `    5 MB`  Manga/SIDEKICKS manga/Sidekicks vol.001 ch.048 [KissManga].cbz
- `    4 MB`  Manga/SIDEKICKS manga/Sidekicks vol.001 ch.010 [KissManga].cbz
- `    4 MB`  Manga/SIDEKICKS manga/Sidekicks vol.001 ch.016 [KissManga].cbz
- `    3 MB`  Manga/SIDEKICKS manga/Sidekicks vol.001 ch.009 [KissManga].cbz
- `    3 MB`  Manga/SIDEKICKS manga/Sidekicks vol.001 ch.008 [KissManga].cbz
- `    3 MB`  Manga/SIDEKICKS manga/Sidekicks vol.001 ch.007 [KissManga].cbz

### brink — v2  *(volume)*

- `  101 MB`  Dan Abnett/Brink/Brink V2 Skeleton Life (Dan Dare 2000AD Remix).cbr
- `  101 MB`  2000AD - Collections /Brink/Brink V2 Skeleton Life (Dan Dare 2000AD Remix).cbr
- `   83 MB`  Brink - Book 01-06 (2017-2026) (digital) (Torquemada)/Brink - Book 02 [Rebellion] (2018) (Digital) (Torquemada).cbr

### judge dredd  *(special)*

- `   60 MB`  2000AD prog/2000AD (Specials, Annuals & Poster Progs + Extras)/2000AD Yearbooks & Specials (1977 - 2013)/Specials (-JJ-)/Judge Dredd Special Edition 1994.cbr
- `   60 MB`  2000AD prog/2000AD (Specials, Annuals & Poster Progs + Extras)/2000AD Yearbooks & Specials (1977 - 2013)/Judge Dredd (Specials, Poster Progs & Extras) (-JJ-)/The Complete Judge Dredd Special Edition 1994.cbr
- `   58 MB`  2000AD prog/2000AD (Specials, Annuals & Poster Progs + Extras)/2000AD Yearbooks & Specials (1977 - 2013)/Specials (-JJ-)/Judge Dredd Special Edition 1995.cbr
- `   58 MB`  2000AD prog/2000AD (Specials, Annuals & Poster Progs + Extras)/2000AD Yearbooks & Specials (1977 - 2013)/Judge Dredd (Specials, Poster Progs & Extras) (-JJ-)/The Complete Judge Dredd Special Edition 1995.cbr
- `   45 MB`  2000AD prog/2000AD (Specials, Annuals & Poster Progs + Extras)/2000AD Yearbooks & Specials (1977 - 2013)/Specials (-JJ-)/Judge Dredd Special Edition 1999.cbr

### sir edward grey, witchfinder — v1  — identical size  *(volume)*

- `  140 MB`  Sir Edward Grey, Witchfinder (Collection) (2009-2014) GetComics.INFO/Sir Edward Grey, Witchfinder Vol. 01 - In the Service of Angels (2010) (digital) (Minutemen-Azkaban).cbr
- `  140 MB`  Hellboy/Sir Edward Grey, Witchfinder TPBs/Sir Edward Grey, Witchfinder v01 - In the Service of Angels (2010) GetComics.INFO.cbr

### 2000ad  *(special)*

- `  113 MB`  2000AD prog/2000AD Special (FCBD 2015) (c2c) (Sooth&Talon-Novus-HD).cbr
- `   84 MB`  2000AD prog/2000AD Special 2015 (2014) (Digital-Empire).cbr
- `   82 MB`  2000AD prog/2000AD Special (FCBD 2016) (c2c) (HD) (Minutemen-Enceladus).cbr

### howard duck — v1  *(volume)*

- `  245 MB`  Howard the Duck/Howard the Duck v01 - Duck Hunt (2016) (Digital) (F) (Zone-Empire).cbr
- `   30 MB`  Howard the Duck/Howard the Duck v001 (2024) (Digital) (Walkabout-Empire).cbz

### jin c007 012  *(issue)*

- `  216 MB`  Manga/Jin/Jin - c007-012 (v02) [Patreon].cbz
- `   57 MB`  Manga/Jin/Jin - c007-012 (v02) [Easy Going].cbz

### brain drain  *(issue)*

- `  170 MB`  Europe Comics (Collection)/Brain Drain Part 02 (2021) (Europe Comics) (Mr Norrell-Empire).cbr
- `  101 MB`  Europe Comics (Collection)/Brain Drain Part 01 (2020) (Europe Comics) (Mr Norrell-Empire).cbr

### ghost in shell arise — v1  *(volume)*

- `   89 MB`  Manga/Ghost in the Shell/Ghost in the Shell ARISE v01 c04.cbr
- `   41 MB`  Manga/Ghost in the Shell/Ghost in the Shell ARISE v01 c06.cbz
- `   39 MB`  Manga/Ghost in the Shell/Ghost in the Shell ARISE v01 c01.cbr
- `   36 MB`  Manga/Ghost in the Shell/Ghost in the Shell ARISE v01 c02.cbr
- `   36 MB`  Manga/Ghost in the Shell/Ghost in the Shell ARISE v01 c03.cbr
- `   30 MB`  Manga/Ghost in the Shell/Ghost in the Shell ARISE v01 c05.cbz

### jin c019 023  *(issue)*

- `  212 MB`  Manga/Jin/Jin - c019-023 (v04) [Patreon].cbz
- `   55 MB`  Manga/Jin/Jin - c019-023 (v04) [Easy Going].cbz

### metal hurlant — v1  *(volume)*

- `   94 MB`  Metal Hurlant Collection/Metal Hurlant Collection v01 p003 (2011) (Humanoids) GetComics.INFO.cbr
- `   93 MB`  Metal Hurlant Collection/Metal Hurlant Collection v01 p001 (2011) (Humanoids) GetComics.INFO.cbr
- `   78 MB`  Metal Hurlant Collection/Metal Hurlant Collection v01 p002 (2011) (Humanoids) GetComics.INFO.cbr

### brink — v5  — identical size  *(volume)*

- `  131 MB`  Brink - Book 01-06 (2017-2026) (digital) (Torquemada)/Brink - Book 05 (2022) (digital) (Torquemada).cbr
- `  131 MB`  2000AD - Collections /Brink/Brink V5 Mercury Retrograde (2022).cbr

### moon girl and devil dinosaur — v1  *(volume)*

- `  201 MB`  Moon Girl and Devil Dinosaur/Moon Girl and Devil Dinosaur v01 - BFF (2016) GetComics.INFO.cbr
- `   60 MB`  Moon Girl and Devil Dinosaur/Moon Girl and Devil Dinosaur v01 - Menace on Wheels (2023) (digital-SD) (Dakota Scanning).cbz

### star trek — #100  *(issue)*

- `  179 MB`  Star Trek/Star Trek 100 Page Summer Spectacular 2012 (2012) (digital) (Minutemen-Mookie).cbr
- `   76 MB`  Star Trek/Star Trek 100 Page Spectacular (2011) (c2c) (Re-em).cbr

### weapon x noir — #01  *(issue)*

- `   90 MB`  GG Studio (Collection) (2010-2012)/Marvel Noir (2009-2011)(digital)/Weapon X Noir (01+)(2010)/Weapon X Noir 01 (2010) (digital) (Shadowcat-Empire).cbz
- `   90 MB`  Aster Blistok/Le Vagabond des Limbes/Weapon X Noir (01+)(2010)/Weapon X Noir 01 (2010) (digital) (Shadowcat-Empire).cbz
- `   24 MB`  Marvel Noir (2009-2011)(digital)/Weapon X Noir 01 (2010) (2 covers) (Minutemen-DTs).cbr
- `   24 MB`  GG Studio (Collection) (2010-2012)/Marvel Noir (2009-2011)(digital)/Weapon X Noir (01+)(2010)/Weapon X Noir 01 (2010) (2 covers) (Minutemen-DTs).cbr
- `   24 MB`  Aster Blistok/Le Vagabond des Limbes/Weapon X Noir (01+)(2010)/Weapon X Noir 01 (2010) (2 covers) (Minutemen-DTs).cbr
- `    1 MB`  GG Studio (Collection) (2010-2012)/Marvel Noir (2009-2011)(digital)/Weapon X Noir (01+)(2010)/Weapon X Noir 01 (2010) (Dennis Calero Variant) (Scandog+Minutemen-Goblin).cbr
- `    1 MB`  Aster Blistok/Le Vagabond des Limbes/Weapon X Noir (01+)(2010)/Weapon X Noir 01 (2010) (Dennis Calero Variant) (Scandog+Minutemen-Goblin).cbr

### b.p.r.d. hell on earth, reign of black flame  *(issue)*

- `   53 MB`  Hellboy/152.)  B.P.R.D. - Hell on Earth #115-119, The Reign of the Black Flame, Parts 1-5  (2012 AD)/B.P.R.D. - Hell on Earth #115, The Reign of the Black Flame, Part 1.cbr
- `   50 MB`  Hellboy/152.)  B.P.R.D. - Hell on Earth #115-119, The Reign of the Black Flame, Parts 1-5  (2012 AD)/B.P.R.D. - Hell on Earth #116, The Reign of the Black Flame, Part 2.cbr
- `   50 MB`  Hellboy/152.)  B.P.R.D. - Hell on Earth #115-119, The Reign of the Black Flame, Parts 1-5  (2012 AD)/B.P.R.D. - Hell on Earth #118, The Reign of the Black Flame, Part 4.cbr
- `   50 MB`  Hellboy/152.)  B.P.R.D. - Hell on Earth #115-119, The Reign of the Black Flame, Parts 1-5  (2012 AD)/B.P.R.D. - Hell on Earth #119, The Reign of the Black Flame, Part 5.cbr
- `   48 MB`  Hellboy/152.)  B.P.R.D. - Hell on Earth #115-119, The Reign of the Black Flame, Parts 1-5  (2012 AD)/B.P.R.D. - Hell on Earth #117, The Reign of the Black Flame, Part 3.cbr

### heavy metal — #277  *(issue)*

- `  246 MB`  Heavy Metal/01. Main Series/Heavy Metal 277(2015)(Digital)(TLK-EMPIRE-HD).cbr
- `    4 MB`  Heavy Metal/01. Main Series/Heavy Metal 277 (2015) (Skinner Variant) (Cover Only) (null-DCP).cbz

### wunderwaffen — v13  — identical size  *(volume)*

- `  120 MB`  Wunderwaffen/Wunderwaffen v13 - Tokyo_ A-Bomb _2018_ _MagicMan-DCP_ (newcomic.info).cbr
- `  120 MB`  Wunderwaffen/Wunderwaffen v13 - Tokyo, A-Bomb (2018) (MagicMan-DCP).cbr

### crumb comics — v16  *(volume)*

- `  130 MB`  The Complete Crumb Comics (v01-v13,v15-v17)(1964-2009)/The Complete Crumb Comics v16 [The Mid-1980s] part 2.cbr
- `  109 MB`  The Complete Crumb Comics (v01-v13,v15-v17)(1964-2009)/The Complete Crumb Comics v16 [The Mid-1980s] part 1.cbr

### corto maltese — #16  *(issue)*

- `  119 MB`  Corto Maltese/Corto Maltese 01-16/Corto Maltese 16 - Equatoria _Canales-Pellejero_ 2017_ _edition 1.0_ _Scanlation-Extended_ 2018_ (newcomic.info).cbr
- `  119 MB`  Hugo Pratt/Corto Maltese 16 - Equatoria (Canales-Pellejero, 2017) (edition 1.2) (Scanlation-Extended, 2018).cbr

### wunderwaffen — v14  — identical size  *(volume)*

- `  119 MB`  Wunderwaffen/Wunderwaffen v14 - The_Fire_From_the_Sky__2019___MagicMan-DCP_ (newcomic.info).cbr
- `  119 MB`  Wunderwaffen/Wunderwaffen v14 - The Fire From the Sky (2019) (MagicMan-DCP).cbr

### devlin waugh — v2  *(volume)*

- `  196 MB`  Devlin Waugh/Devlin Waugh v2 - Red Tide (2015) GetComics.INFO.cbr
- `   39 MB`  2000AD - Collections /Devlin Waugh V2 Reign of Frogs (Dan Dare 2000AD Remix).cbr

### secret garden  *(issue)*

- `  104 MB`  Europe Comics (Collection)/The Secret Garden Part 01 (2021) (digital) (Mr Norrell-Empire).cbr
- `   65 MB`  Europe Comics (Collection)/The Secret Garden Part 2 (Europe Comics 2023) (webrip) (MagicMan-DCP).cbr
- `   61 MB`  Europe Comics (Collection)/The Secret Garden Part 1 (Europe Comics 2021) (webrip) (MagicMan-DCP).cbr

### noise  *(issue)*

- `  198 MB`  Manga/Noise manga/NOiSE (Complete) [Kodansha].cbz
- `   32 MB`  Manga/Noise manga/NOiSE (Complete).cbz

### gekiga kachikujin yapoo — v1  *(volume)*

- `   33 MB`  Manga/Yapoo (Shotaro Ishinomori)/Gekiga Kachikujin Yapoo Vol.001 Ch.003 An Invitation to the Universal Empire [KissManga] (1).cbz
- `   33 MB`  Manga/Gekiga_Kachikujin_Yapoo/Gekiga Kachikujin Yapoo Vol.001 Ch.003 An Invitation to the Universal Empire [KissManga] (1).cbz
- `   23 MB`  Manga/Yapoo (Shotaro Ishinomori)/Gekiga Kachikujin Yapoo Vol.001 Ch.001 Genesis - Summer 196X, Taunus West Germany [KissManga] (1).cbz
- `   23 MB`  Manga/Gekiga_Kachikujin_Yapoo/Gekiga Kachikujin Yapoo Vol.001 Ch.001 Genesis - Summer 196X, Taunus West Germany [KissManga] (1).cbz
- `   14 MB`  Manga/Yapoo (Shotaro Ishinomori)/Gekiga Kachikujin Yapoo Vol.001 Ch.008 Tornado Flies [KissManga] (1).cbz
- `   14 MB`  Manga/Gekiga_Kachikujin_Yapoo/Gekiga Kachikujin Yapoo Vol.001 Ch.008 Tornado Flies [KissManga] (1).cbz
- `   13 MB`  Manga/Yapoo (Shotaro Ishinomori)/Gekiga Kachikujin Yapoo Vol.001 Ch.007 Yapoonal Register [KissManga] (1).cbz
- `   13 MB`  Manga/Gekiga_Kachikujin_Yapoo/Gekiga Kachikujin Yapoo Vol.001 Ch.007 Yapoonal Register [KissManga] (1).cbz
- `   11 MB`  Manga/Yapoo (Shotaro Ishinomori)/Gekiga Kachikujin Yapoo Vol.001 Ch.004 Villa - Above and Below the Crystal Palace [KissManga] (1).cbz
- `   11 MB`  Manga/Gekiga_Kachikujin_Yapoo/Gekiga Kachikujin Yapoo Vol.001 Ch.004 Villa - Above and Below the Crystal Palace [KissManga] (1).cbz
- `    9 MB`  Manga/Yapoo (Shotaro Ishinomori)/Gekiga Kachikujin Yapoo Vol.001 Ch.006 Dawn of the Gods [KissManga] (1).cbz
- `    9 MB`  Manga/Gekiga_Kachikujin_Yapoo/Gekiga Kachikujin Yapoo Vol.001 Ch.006 Dawn of the Gods [KissManga] (1).cbz
- `    8 MB`  Manga/Yapoo (Shotaro Ishinomori)/Gekiga Kachikujin Yapoo Vol.001 Ch.005 A Reunion and Then [KissManga] (1).cbz
- `    8 MB`  Manga/Gekiga_Kachikujin_Yapoo/Gekiga Kachikujin Yapoo Vol.001 Ch.005 A Reunion and Then [KissManga] (1).cbz
- `    3 MB`  Manga/Yapoo (Shotaro Ishinomori)/Gekiga Kachikujin Yapoo Vol.001 Ch.002 A Discussion on the Nature of Yapoo [KissManga] (1).cbz
- `    3 MB`  Manga/Gekiga_Kachikujin_Yapoo/Gekiga Kachikujin Yapoo Vol.001 Ch.002 A Discussion on the Nature of Yapoo [KissManga] (1).cbz

### daredevil — #001  *(issue)*

- `  173 MB`  Daredevil/Daredevil (2019-2021)/Daredevil 001 - Director 's Cut (2019) (Digital) (Zone-Empire).cbr
- `   52 MB`  Daredevil/Daredevil (2019-2021)/Daredevil 001 (2019) (Oroboros-DCP).cbr

### hellboy winter  *(special)*

- `   56 MB`  Hellboy/Hellboy Winter Special 2019 (2020) (digital) (Son of Ultron-Empire).cbr
- `   46 MB`  Hellboy/Hellboy Winter Special - The Yule Cat (2023) (digital) (Son of Ultron-Empire).cbr
- `   43 MB`  Hellboy/Hellboy Winter Special (2017) (digital) (Minutemen-Faessla).cbz
- `   42 MB`  Hellboy/Hellboy Winter Special (2016) GetComics.INFO.cbr
- `   35 MB`  Hellboy/Hellboy Winter Special 2018 (2018) (digital) (Son of Ultron-Empire).cbr

### inspector canardo — #02  *(issue)*

- `  190 MB`  Inspector Canardo (000-017+)(1984-2016)/Inspector Canardo 02 - Shaggy Dog Story (Sokal, 1981) (FanScan, 2016).cbr
- `   31 MB`  Inspector Canardo (000-017+)(1984-2016)/Inspector Canardo 02 - The Mark of Rasputin (scanlation) (Team-BDS).cbr

### b.p.r.d. hell on earth, lake of fire  *(issue)*

- `   46 MB`  Hellboy/150.)  B.P.R.D. - Hell on Earth #110-114, Lake of Fire, Parts 1-5  (2012 AD)/B.P.R.D. - Hell on Earth #110, Lake of Fire, Part 1.cbr
- `   45 MB`  Hellboy/150.)  B.P.R.D. - Hell on Earth #110-114, Lake of Fire, Parts 1-5  (2012 AD)/B.P.R.D. - Hell on Earth #113, Lake of Fire, Part 4.cbr
- `   45 MB`  Hellboy/150.)  B.P.R.D. - Hell on Earth #110-114, Lake of Fire, Parts 1-5  (2012 AD)/B.P.R.D. - Hell on Earth #112, Lake of Fire, Part 3.cbr
- `   44 MB`  Hellboy/150.)  B.P.R.D. - Hell on Earth #110-114, Lake of Fire, Parts 1-5  (2012 AD)/B.P.R.D. - Hell on Earth #111, Lake of Fire, Part 2.cbr
- `   42 MB`  Hellboy/150.)  B.P.R.D. - Hell on Earth #110-114, Lake of Fire, Parts 1-5  (2012 AD)/B.P.R.D. - Hell on Earth #114, Lake of Fire, Part 5.cbr

### escape journey — v1  *(volume)*

- `   31 MB`  Manga/Escape_Journey/Escape Journey - v1 c6 [batoto].cbz
- `   26 MB`  Manga/Escape_Journey/Escape Journey - v1 c3 [batoto].cbz
- `   26 MB`  Manga/Escape_Journey/Escape Journey - v1 c4 [batoto].cbz
- `   24 MB`  Manga/Escape_Journey/Escape Journey - v1 c5 [batoto].cbz
- `   23 MB`  Manga/Escape_Journey/Escape Journey - v1 c6 - (1).cbz
- `   18 MB`  Manga/Escape_Journey/Escape Journey - v1 c3 - (1).cbz
- `   18 MB`  Manga/Escape_Journey/Escape Journey - v1 c4 - (1).cbz
- `   17 MB`  Manga/Escape_Journey/Escape Journey - v1 c5 - (1).cbz
- `   14 MB`  Manga/Escape_Journey/Escape Journey - v1 c6.1 [batoto].cbz
- `   13 MB`  Manga/Escape_Journey/Escape Journey - v1 c6.5 [batoto].cbz
- `    7 MB`  Manga/Escape_Journey/Escape Journey - v1 c6.3 [batoto].cbz
- `    3 MB`  Manga/Escape_Journey/Escape Journey - v1 c6.2 [batoto].cbz

### authority — v3  *(volume)*

- `   11 MB`  Warren Ellis/The Authority/v3 Revolution/The Authority v3 Revolution #07.cbr
- `   11 MB`  The Authority/v3 Revolution/The Authority v3 Revolution #07.cbr
- `   11 MB`  Warren Ellis/The Authority/v3 Revolution/The Authority v3 Revolution #01.cbr
- `   11 MB`  The Authority/v3 Revolution/The Authority v3 Revolution #01.cbr
- `   10 MB`  Warren Ellis/The Authority/v3 Revolution/The Authority v3 Revolution #08.cbr
- `   10 MB`  The Authority/v3 Revolution/The Authority v3 Revolution #08.cbr
- `    9 MB`  Warren Ellis/The Authority/v3 Revolution/The Authority v3 Revolution #04.cbr
- `    9 MB`  The Authority/v3 Revolution/The Authority v3 Revolution #04.cbr
- `    9 MB`  Warren Ellis/The Authority/v3 Revolution/The Authority v3 Revolution #12.cbr
- `    9 MB`  The Authority/v3 Revolution/The Authority v3 Revolution #12.cbr
- `    9 MB`  Warren Ellis/The Authority/v3 Revolution/The Authority v3 Revolution #10.cbr
- `    9 MB`  The Authority/v3 Revolution/The Authority v3 Revolution #10.cbr
- `    9 MB`  Warren Ellis/The Authority/v3 Revolution/The Authority v3 Revolution #09.cbr
- `    9 MB`  The Authority/v3 Revolution/The Authority v3 Revolution #09.cbr
- `    9 MB`  Warren Ellis/The Authority/v3 Revolution/The Authority v3 Revolution #03.cbr
- `    9 MB`  The Authority/v3 Revolution/The Authority v3 Revolution #03.cbr
- `    8 MB`  Warren Ellis/The Authority/v3 Revolution/The Authority v3 Revolution #02.cbr
- `    8 MB`  The Authority/v3 Revolution/The Authority v3 Revolution #02.cbr
- `    8 MB`  Warren Ellis/The Authority/v3 Revolution/The Authority v3 Revolution #05.cbr
- `    8 MB`  The Authority/v3 Revolution/The Authority v3 Revolution #05.cbr
- `    8 MB`  Warren Ellis/The Authority/v3 Revolution/The Authority v3 Revolution #11.cbr
- `    8 MB`  The Authority/v3 Revolution/The Authority v3 Revolution #11.cbr
- `    8 MB`  Warren Ellis/The Authority/v3 Revolution/The Authority v3 Revolution #06.cbr
- `    8 MB`  The Authority/v3 Revolution/The Authority v3 Revolution #06.cbr

### jimmy's bastards — v2  *(volume)*

- `  109 MB`  Jimmys Bastards/Jimmy's Bastards v2 - Jimmy's Little Bastards 001 (2022) (digital) (Son of Ultron-Empire).cbr
- `  102 MB`  Jimmys Bastards/Jimmy's Bastards v2 - Jimmy's Little Bastards 002 (2022) (digital) (Son of Ultron-Empire).cbr

### devlin waugh — v1  *(volume)*

- `  170 MB`  Devlin Waugh/Devlin Waugh v1 - Swimming in Blood (2014) (digital) (Ampersand).cbr
- `   38 MB`  2000AD - Collections /Devlin Waugh V1 Chasing Herod (Dan Dare 2000AD Remix).cbr

### 2000 ad  *(annual)*

- `   50 MB`  2000AD prog/2000AD (Specials, Annuals & Poster Progs + Extras)/2000AD Yearbooks & Specials (1977 - 2013)/2000 AD Yearbook 1992-1995/2000 AD Yearbook 1992.cbr
- `   47 MB`  Alan Moore/Alan Moore Collection I- English Invasion/Alan Moore Collection III- 2000 AD/2000 AD/2000 AD- Individual Issues/2000 AD- Annual/2000 AD Annual 1984 (Skizz - How He Came To Be, Rogue Trooper - First Of The Few, Ro-Busters - Stormeagles Are Go!).cbr
- `   39 MB`  Alan Moore/Alan Moore Collection I- English Invasion/Alan Moore Collection III- 2000 AD/2000 AD/2000 AD- Individual Issues/2000 AD- Annual/2000 AD Annual 1985 (The A.B.C. Warriors - Red Planet Blues).cbr
- `   38 MB`  Alan Moore/Alan Moore Collection I- English Invasion/Alan Moore Collection III- 2000 AD/2000 AD/2000 AD- Individual Issues/2000 AD- Annual/2000 AD Annual 1982 (Ro-Busters - Bax The Burner).cbr
- `   34 MB`  Alan Moore/Alan Moore Collection I- English Invasion/Alan Moore Collection III- 2000 AD/2000 AD/2000 AD- Individual Issues/2000 AD- Annual/2000 AD Annual 1983 (Ro-Busters - Old Red Eyes Is Back, Rogue Trooper - Pray For War).cbr

### jaegir — v1  *(volume)*

- `  179 MB`  2000AD - Collections /Jaegir/Jaegir v01 - Beasts Within (2015) (F) (digital) (Torquemada).cbr
- `   27 MB`  2000AD - Collections /Jaegir/Jaegir V1 Strigoi (Dan Dare 2000AD Remix).cbr

### murena — v2  *(volume)*

- `  126 MB`  Murena/Murena T02 - Death of a Sage (2024) (Scanlation) (phillywilly).cbr
- `   78 MB`  Murena/Murena T02 - Sand and Blood (Dragonz-Choky-Tanim).cbr

### spider man — #1602  *(issue)*

- `   43 MB`  Marvel 1602 + Tie Ins (2003-2004) GetComics.INFO/Marvel 1602 Complete/4 Marvel 1602 - Spider-Man (001 - 005)/Spider-Man 1602 005 (2010).cbz
- `   40 MB`  Marvel 1602 + Tie Ins (2003-2004) GetComics.INFO/Marvel 1602 Complete/4 Marvel 1602 - Spider-Man (001 - 005)/Spider-Man 1602 001 (2009).cbz
- `   40 MB`  Marvel 1602 + Tie Ins (2003-2004) GetComics.INFO/Marvel 1602 Complete/4 Marvel 1602 - Spider-Man (001 - 005)/Spider-Man 1602 002 (2010).cbz
- `   39 MB`  Marvel 1602 + Tie Ins (2003-2004) GetComics.INFO/Marvel 1602 Complete/4 Marvel 1602 - Spider-Man (001 - 005)/Spider-Man 1602 003 (2010).cbz
- `   37 MB`  Marvel 1602 + Tie Ins (2003-2004) GetComics.INFO/Marvel 1602 Complete/4 Marvel 1602 - Spider-Man (001 - 005)/Spider-Man 1602 004 (2010).cbz

### locke & key alpha — #02  *(issue)*

- `   95 MB`  Locke & Key/Locke & Key - Alpha 02 (of 02) (2013) (7 covers) (digital) (Minutemen-PhD).cbr
- `   95 MB`  Locke & Key/Locke & Key - Alpha (2013)/Locke & Key - Alpha 02 (of 02) (2013) (7 covers) (digital) (Minutemen-PhD).cbr
- `    2 MB`  Locke & Key/Locke & Key - Alpha (2013)/Variant Covers/Locke & Key - Alpha 02 (2013) (Jetpack Comics Exclusive B&W Variant Cover) (theProletariat-Novus-HD).cbz
- `    1 MB`  Locke & Key/Locke & Key - Alpha (2013)/Variant Covers/Locke & Key - Alpha 02 (2013) (Shane Leonard Photo Variant Cover) (ChairmanMao-Novus-HD).cbz

### inspector canardo — #04  *(issue)*

- `  157 MB`  Inspector Canardo (000-017+)(1984-2016)/Inspector Canardo 04 - Blue Angel (Sokal, 1991) (FanScan, 2016).cbr
- `   33 MB`  Inspector Canardo (000-017+)(1984-2016)/Inspector Canardo 04 - The Return of Rasputin (Carlsen Comics) (1984) (JJ-data9724)(repack).cbr

### kamen rider — v1  *(volume)*

- `  135 MB`  Manga/Kamen Rider/Kamen Rider v01 (digital) (ZERO-rips).cbr
- `   53 MB`  Manga/Kamen Rider/Kamen Rider v01 c01-03a.cbz

### kamen rider — v2  *(volume)*

- `  136 MB`  Manga/Kamen Rider/Kamen Rider v02 (digital) (ZERO-rips).cbr
- `   51 MB`  Manga/Kamen Rider/Kamen Rider v02 c03b-04.cbz

### devlin waugh — v3  *(volume)*

- `  156 MB`  Devlin Waugh/Devlin Waugh v3 - Blood Debt (2021) (Digital) (Torquemada).cbr
- `   31 MB`  2000AD - Collections /Devlin Waugh V3 Sirius Rising (Dan Dare 2000AD Remix).cbr

### heavy metal — v21 — #03  *(volume)*

- `   70 MB`  Heavy Metal/02. Specials/Heavy Metal v21 #03 (Fall 2007) 30th Anniversary Special.cbz
- `   56 MB`  Heavy Metal/Heavy Metal Vols 01-35 (1977-2012)/Heavy Metal v21 03 (1997).cbr
- `   56 MB`  Heavy Metal/01. Main Series/Heavy Metal v21 03 (1997).cbr

### 2000ad presents scream & misty  — identical size  *(special)*

- `   91 MB`  2000AD prog/Yearbooks & Specials/2000AD Presents - Scream & Misty Special (2017) GetComics.INFO.cbr
- `   91 MB`  2000AD prog/Yearbooks & Specials/2000AD Presents - Scream & Misty Special (2017) (digital) (Torquemada).cbr

### kamen rider — v3  *(volume)*

- `  133 MB`  Manga/Kamen Rider/Kamen Rider v03 (digital) (ZERO-rips).cbr
- `   48 MB`  Manga/Kamen Rider/Kamen Rider v03 c05-06a.cbz

### ladies with guns  *(issue)*

- `   60 MB`  Europe Comics (Collection)/Ladies with Guns, Part 3 (Europe Comics 2024) (webrip) (MagicMan-DCP).cbr
- `   59 MB`  Europe Comics (Collection)/Ladies with Guns, Part 1 (Europe Comics 2022) (webrip) (MagicMan-DCP).cbr
- `   57 MB`  Europe Comics (Collection)/Ladies with Guns, Part 2 (Europe Comics 2023) (webrip) (MagicMan-DCP).cbr

### aristotle  *(issue)*

- `   96 MB`  Europe Comics (Collection)/Aristotle, Part 1 (Europe Comics 2023) (webrip) (MagicMan-DCP).cbr
- `   81 MB`  Europe Comics (Collection)/Aristotle, Part 2 (Europe Comics 2023) (webrip) (MagicMan-DCP).cbr

### terminal — #002  *(issue)*

- `  115 MB`  Terminal/Terminal 002 Blind Bag (2026).cbz
- `   55 MB`  Terminal/Terminal 002 (2026) (Series) (Image) (Digital) (LeDuch-DCP).cbz

### kick ass — #08  *(issue)*

- `   94 MB`  Mark Millar/Kick-Ass (v1-v3+)(2008-2014)(digital+)/Kick-Ass 3 (001-008+)(2013-2014)(digital+)/Kick-Ass 3 08 (of 08) (2014) (digital-Empire).cbr
- `   39 MB`  Mark Millar/Kick-Ass (v1-v3+)(2008-2014)(digital+)/Kick-Ass 1 (001-008+)(2008-2009)(digital)(G85-Empire)/Kick-Ass 08 (of 08) (2010) (digital) (Minutemen-InnerDemons).cbr
- `   31 MB`  Mark Millar/Kick-Ass (v1-v3+)(2008-2014)(digital+)/Kick-Ass 1 (001-008+)(2008-2009)(digital)(G85-Empire)/scans/Kick-Ass 08 (of 08) (2010) (c2c) (Minutemen-DTs).cbz

### kick ass — #01  *(issue)*

- `   41 MB`  Mark Millar/Kick-Ass (v1-v3+)(2008-2014)(digital+)/Kick-Ass 1 (001-008+)(2008-2009)(digital)(G85-Empire)/scans/Kick-Ass 01 (of 08) (2008, Directors Cut) (Minutemen-Zone).cbr
- `   40 MB`  Mark Millar/Kick-Ass (v1-v3+)(2008-2014)(digital+)/Kick-Ass 3 (001-008+)(2013-2014)(digital+)/Kick-Ass 3 01 (of 08) (2013) (digital) (Minutemen-PhD).cbr
- `   39 MB`  Mark Millar/Kick-Ass (v1-v3+)(2008-2014)(digital+)/Kick-Ass 1 (001-008+)(2008-2009)(digital)(G85-Empire)/Kick-Ass 01 (of 08) (2008) (digital) (Minutemen-InnerDemons).cbr
- `   18 MB`  Mark Millar/Kick-Ass (v1-v3+)(2008-2014)(digital+)/Kick-Ass 1 (001-008+)(2008-2009)(digital)(G85-Empire)/scans/Kick-Ass 01 (of 08) (2008) (2 covers) (Minutemen-ReZone).cbr
- `    4 MB`  Mark Millar/Kick-Ass (v1-v3+)(2008-2014)(digital+)/Kick-Ass 3 (001-008+)(2013-2014)(digital+)/Variant Covers/Kick-Ass 3 01 (2013) (2nd Printing Variant Covers Poster Join) (Covers ONLY) (ScanDog+ArtNet).cbz
- `    4 MB`  Mark Millar/Kick-Ass (v1-v3+)(2008-2014)(digital+)/Kick-Ass 3 (001-008+)(2013-2014)(digital+)/Variant Covers/Kick-Ass 3 01 (2013) (Variant Covers Poster Join) (Covers ONLY) (ScanDog+ArtNet).cbz
- `    1 MB`  Mark Millar/Kick-Ass (v1-v3+)(2008-2014)(digital+)/Kick-Ass 1 (001-008+)(2008-2009)(digital)(G85-Empire)/variants/Kick-Ass 01 (of 08) (2008) (3rd Printing John Romita Jr Variant) (Minutemen-TheRain).cbr
- `    1 MB`  Mark Millar/Kick-Ass (v1-v3+)(2008-2014)(digital+)/Kick-Ass 3 (001-008+)(2013-2014)(digital+)/Variant Covers/Kick-Ass 3 01 (2013) (Marc Silvestri Colonel Stars 2nd Printing Variant) (Cover ONLY) (ScanDog+ArtNet).cbz
- `    1 MB`  Mark Millar/Kick-Ass (v1-v3+)(2008-2014)(digital+)/Kick-Ass 2 (001-007+)(2010-2012)(digital)(Zone-Empire)/variant covers/Kick-Ass 2 01 (2010) (Tommy Lee Edwards Variant) (Cover ONLY) (ScanDog).cbr
- `    1 MB`  Mark Millar/Kick-Ass (v1-v3+)(2008-2014)(digital+)/Kick-Ass 1 (001-008+)(2008-2009)(digital)(G85-Empire)/variants/Kick-Ass 01 (of 08) (2008) (Umpteenth Printing Variant) (Cover Only) (Spiritual Beggar-DCP).cbr
- `    1 MB`  Mark Millar/Kick-Ass (v1-v3+)(2008-2014)(digital+)/Kick-Ass 2 (001-007+)(2010-2012)(digital)(Zone-Empire)/variant covers/Kick-Ass 2 01 (2010) (2nd Printing Variant) (Cover ONLY) (ScanDog).cbr
- `    1 MB`  Mark Millar/Kick-Ass (v1-v3+)(2008-2014)(digital+)/Kick-Ass 2 (001-007+)(2010-2012)(digital)(Zone-Empire)/variant covers/Kick-Ass 2 01 (2010) (3rd Printing Variant) (Cover ONLY) (ScanDog).cbr
- `    1 MB`  Mark Millar/Kick-Ass (v1-v3+)(2008-2014)(digital+)/Kick-Ass 3 (001-008+)(2013-2014)(digital+)/Variant Covers/Kick-Ass 3 01 (2013) (John Romita Jr. 2nd Printing Variant) (Cover ONLY) (ScanDog+ArtNet).cbz
- `    1 MB`  Mark Millar/Kick-Ass (v1-v3+)(2008-2014)(digital+)/Kick-Ass 1 (001-008+)(2008-2009)(digital)(G85-Empire)/variants/Kick-Ass 01 (of 08) (2008) (John Romita Jr. Sketch Variant) (Cover Only) (ScanDog).cbr
- `    1 MB`  Mark Millar/Kick-Ass (v1-v3+)(2008-2014)(digital+)/Kick-Ass 3 (001-008+)(2013-2014)(digital+)/Variant Covers/Kick-Ass 3 01 (2013) (Adam Kubert Eisenhower The Dog 2nd Printing Variant) (Cover ONLY) (ScanDog+ArtNet).cbz
- `    1 MB`  Mark Millar/Kick-Ass (v1-v3+)(2008-2014)(digital+)/Kick-Ass 3 (001-008+)(2013-2014)(digital+)/Variant Covers/Kick-Ass 3 01 (2013) (Marc Silvestri Colonel Stars Variant) (Cover ONLY) (ScanDog+ArtNet).cbz
- `    1 MB`  Mark Millar/Kick-Ass (v1-v3+)(2008-2014)(digital+)/Kick-Ass 3 (001-008+)(2013-2014)(digital+)/Variant Covers/Kick-Ass 3 01 (2013) (Cully Hamner Battle-Guy & Night-Bitch 2nd Printing Variant) (Cover ONLY) (ScanDog+ArtNet).cbz
- `    1 MB`  Mark Millar/Kick-Ass (v1-v3+)(2008-2014)(digital+)/Kick-Ass 3 (001-008+)(2013-2014)(digital+)/Variant Covers/Kick-Ass 3 01 (2013) (John Romita Jr.Cover) (Cover ONLY) (ScanDog+ArtNet).cbz
- `    1 MB`  Mark Millar/Kick-Ass (v1-v3+)(2008-2014)(digital+)/Kick-Ass 3 (001-008+)(2013-2014)(digital+)/Variant Covers/Kick-Ass 3 01 (2013) (Cully Hamner Battle-Guy & Night-Bitch Variant) (Cover ONLY) (ScanDog+ArtNet).cbz
- `    1 MB`  Mark Millar/Kick-Ass (v1-v3+)(2008-2014)(digital+)/Kick-Ass 1 (001-008+)(2008-2009)(digital)(G85-Empire)/variants/Kick-Ass 01 (of 08) (2008) (2nd ptg var cvr) (Minutemen).cbr
- `    1 MB`  Mark Millar/Kick-Ass (v1-v3+)(2008-2014)(digital+)/Kick-Ass 3 (001-008+)(2013-2014)(digital+)/Variant Covers/Kick-Ass 3 01 (2013) (Adam Kubert Eisenhower The Dog Variant) (Cover ONLY) (ScanDog+ArtNet).cbz
- `    0 MB`  Mark Millar/Kick-Ass (v1-v3+)(2008-2014)(digital+)/Kick-Ass 3 (001-008+)(2013-2014)(digital+)/Variant Covers/Kick-Ass 3 01 (2013) (Adam Hughes Hit-Girl Variant) (Cover ONLY) (ScanDog+ArtNet).cbz
- `    0 MB`  Mark Millar/Kick-Ass (v1-v3+)(2008-2014)(digital+)/Kick-Ass 3 (001-008+)(2013-2014)(digital+)/Variant Covers/Kick-Ass 3 01 (2013) (Adam Hughes Hit-Girl 2nd Printing Variant) (Cover ONLY) (ScanDog+ArtNet).cbz
- `    0 MB`  Mark Millar/Kick-Ass (v1-v3+)(2008-2014)(digital+)/Kick-Ass 3 (001-008+)(2013-2014)(digital+)/Variant Covers/Kick-Ass 3 01 (2013) (Pasqual Ferry Dr. Gravity & Insect-Man 2nd Printing Variant) (Cover ONLY) (ScanDog+ArtNet).cbz
- `    0 MB`  Mark Millar/Kick-Ass (v1-v3+)(2008-2014)(digital+)/Kick-Ass 3 (001-008+)(2013-2014)(digital+)/Variant Covers/Kick-Ass 3 01 (2013) (Pasqual Ferry Dr. Gravity & Insect-Man Variant) (Cover ONLY) (ScanDog+ArtNet).cbz

### zombo — v2  *(volume)*

- `  114 MB`  2000AD - Collections /Zombo/Zombo v02 - You Smell of Crime and I'm the Deodorant (2013) (digital-SD) (Torquemada).cbr
- `   45 MB`  2000AD - Collections /Zombo/Zombo V2 Zombo's 11 (Dan Dare 2000AD Remix).cbr

### icaro  *(issue)*

- `   39 MB`  Manga/Icaro-v01.cbr
- `   39 MB`  Jodorowsky and Moebius/Icaro-v01.cbr
- `   37 MB`  Manga/Icaro-v02.cbr
- `   37 MB`  Jodorowsky and Moebius/Icaro-v02.cbr

### spirou & fantasio — #16  *(issue)*

- `   87 MB`  Spirou & Fantasio/Spirou & Fantasio 16 - Shadow of the Z (2018)_(Cinebook)_(Digital-Empire).cbr
- `   62 MB`  Spirou & Fantasio/Spirou & Fantasio 16 - The Z Rises Again (2019) (Cinebook) (Digital-Empire).cbr

### fafhrd and gray mouser of 4  *(issue)*

- `   25 MB`  Fafhrd and the Gray Mouser 1-4 (1990)/Fafhrd and the Gray Mouser 1-of-4 (c2c) (1990.Epic).cbr
- `   25 MB`  Aster Blistok/Le Vagabond des Limbes/Fafhrd and the Gray Mouser 1-4 (1990)/Fafhrd and the Gray Mouser 1-of-4 (c2c) (1990.Epic).cbr
- `   19 MB`  Fafhrd and the Gray Mouser 1-4 (1990)/Fafhrd and the Gray Mouser 2-of-4 (c2c) (1991.Epic).cbr
- `   19 MB`  Aster Blistok/Le Vagabond des Limbes/Fafhrd and the Gray Mouser 1-4 (1990)/Fafhrd and the Gray Mouser 2-of-4 (c2c) (1991.Epic).cbr
- `   17 MB`  Fafhrd and the Gray Mouser 1-4 (1990)/Fafhrd and the Gray Mouser 4-of-4 (c2c) (1991.Epic).cbr
- `   17 MB`  Aster Blistok/Le Vagabond des Limbes/Fafhrd and the Gray Mouser 1-4 (1990)/Fafhrd and the Gray Mouser 4-of-4 (c2c) (1991.Epic).cbr
- `   14 MB`  Fafhrd and the Gray Mouser 1-4 (1990)/Fafhrd and the Gray Mouser 3-of-4 (c2c) (1991.Epic).cbr
- `   14 MB`  Aster Blistok/Le Vagabond des Limbes/Fafhrd and the Gray Mouser 1-4 (1990)/Fafhrd and the Gray Mouser 3-of-4 (c2c) (1991.Epic).cbr

### b.p.r.d. hell on earth, flesh and stone  *(issue)*

- `   43 MB`  Hellboy/163.)  B.P.R.D. - Hell on Earth #125-129, Flesh and Stone, Parts 1-5  (2013 - 2014 AD)/B.P.R.D. - Hell on Earth #125, Flesh and Stone, Part 1.cbr
- `   28 MB`  Hellboy/163.)  B.P.R.D. - Hell on Earth #125-129, Flesh and Stone, Parts 1-5  (2013 - 2014 AD)/B.P.R.D. - Hell on Earth #129, Flesh and Stone, Part 5.cbr
- `   26 MB`  Hellboy/163.)  B.P.R.D. - Hell on Earth #125-129, Flesh and Stone, Parts 1-5  (2013 - 2014 AD)/B.P.R.D. - Hell on Earth #126, Flesh and Stone, Part 2.cbr
- `   25 MB`  Hellboy/163.)  B.P.R.D. - Hell on Earth #125-129, Flesh and Stone, Parts 1-5  (2013 - 2014 AD)/B.P.R.D. - Hell on Earth #128, Flesh and Stone, Part 4.cbr
- `   24 MB`  Hellboy/163.)  B.P.R.D. - Hell on Earth #125-129, Flesh and Stone, Parts 1-5  (2013 - 2014 AD)/B.P.R.D. - Hell on Earth #127, Flesh and Stone, Part 3.cbr

### star trek  *(annual)*

- `   96 MB`  Star Trek/Star Trek - Annual 2024 (2024) (Digital) (Kileko-Empire).cbz
- `   48 MB`  Star Trek/Star Trek - Annual 2023 (2023) (digital) (The Seeker-Empire).cbr

### locke & key alpha — #01  *(issue)*

- `   65 MB`  Locke & Key/Locke & Key - Alpha 01 (of 02) (2013) (digital) (Minutemen-PhD).cbr
- `   65 MB`  Locke & Key/Locke & Key - Alpha (2013)/Locke & Key - Alpha 01 (of 02) (2013) (digital) (Minutemen-PhD).cbr
- `    4 MB`  Locke & Key/Locke & Key - Alpha (2013)/Variant Covers/Locke & Key - Alpha 01 (2013) (Shane Leonard Photo Variant Only) [extracted] (theProletariat-Novus-HD).cbr
- `    1 MB`  Locke & Key/Locke & Key - Alpha (2013)/Variant Covers/Locke & Key - Alpha 01 (2013) (Mile High Comics Exclusive Variant Cover) (ChairmanMao-Novus-HD).cbz
- `    0 MB`  Locke & Key/Locke & Key - Alpha (2013)/Variant Covers/Locke & Key - Alpha 01 (2013) (Double Midnight Comics Exclusive Variant Cover) (ChairmanMao-Novus-HD).cbz
- `    0 MB`  Locke & Key/Locke & Key - Alpha (2013)/Variant Covers/Locke & Key - Alpha 01 (2013) (Hastings Exclusive 'Omega' Variant Cover) (ChairmanMao-Novus-HD).cbz

### spirou & fantasio — #19  *(issue)*

- `   77 MB`  Spirou & Fantasio/Spirou & Fantasio 19 - The Visitor from the Mezozoic (2022) (digital) (Mr Norrell-Empire).cbr
- `   54 MB`  Spirou & Fantasio/Spirou & Fantasio 19 - Baby Fever in Champignac.cbr

### absalom — v2  *(volume)*

- `   89 MB`  Absalom/Absalom v02 - Under a False Flag (2017) (digital) (Torquemada).cbr
- `   42 MB`  2000AD - Collections /Absalom/Absalom V2 (Dan Dare 2000AD Remix).cbr

### ythaq forsaken world — #02  *(issue)*

- `   65 MB`  Soleil (Europe)/Ythaq - 2008-12 - The Forsaken World (Minutemen)/Ythaq - The Forsaken World 02 (of 03) - Ophyde the Gemini (2009) (Minutemen-Lockafella).cbr
- `   64 MB`  Ythaq/Ythaq - The Forsaken World/Ythaq - The Forsaken World 02 (of 03) (comicsall.net).cbr

### kick ass — #06  *(issue)*

- `   69 MB`  Mark Millar/Kick-Ass (v1-v3+)(2008-2014)(digital+)/Kick-Ass 3 (001-008+)(2013-2014)(digital+)/Kick-Ass 3 06 (of 08) (2014) (digital) (Minutemen-PhD).cbr
- `   31 MB`  Mark Millar/Kick-Ass (v1-v3+)(2008-2014)(digital+)/Kick-Ass 1 (001-008+)(2008-2009)(digital)(G85-Empire)/Kick-Ass 06 (of 08) (2009) (digital) (Minutemen-InnerDemons).cbr
- `   29 MB`  Mark Millar/Kick-Ass (v1-v3+)(2008-2014)(digital+)/Kick-Ass 1 (001-008+)(2008-2009)(digital)(G85-Empire)/scans/Kick-Ass 06 (of 08) (2009) (c2c) (Minutemen-Delirium-Powers).cbr

### orville — #002  *(issue)*

- `   40 MB`  The Orville/The Orville 002 - New Beginnings Part 02 (of 02) (2019) (digital) (Son of Ultron-Empire).cbr
- `   32 MB`  The Orville/The Orville 002 - Digressions Part 02 (of 02) (2021) (digital) (Son of Ultron-Empire).cbr
- `   27 MB`  The Orville/The Orville 002 - Launch Day Part 02 (of 02) (2020) (digital) (Son of Ultron-Empire).cbr
- `   27 MB`  The Orville/The Orville 002 - Artifacts Part 02 (of 02) (2021) (digital) (Son of Ultron-Empire).cbr

### orville — #001  *(issue)*

- `   38 MB`  The Orville/The Orville 001 - New Beginnings Part 01 (of 02) (2019) (digital) (Son of Ultron-Empire).cbr
- `   34 MB`  The Orville/The Orville 001 - Artifacts Part 01 (of 02) (2021) (digital) (Son of Ultron-Empire).cbr
- `   27 MB`  The Orville/The Orville 001 - Launch Day Part 01 (of 02) (2020) (digital) (Son of Ultron-Empire).cbr
- `   26 MB`  The Orville/The Orville 001 - Digressions Part 01 (of 02) (2021) (digital) (Son of Ultron-Empire).cbr

### kick ass — #02  *(issue)*

- `   44 MB`  Mark Millar/Kick-Ass (v1-v3+)(2008-2014)(digital+)/Kick-Ass 3 (001-008+)(2013-2014)(digital+)/Kick-Ass 3 02 (of 08) (2013) (digital) (Minutemen-PhD).cbr
- `   43 MB`  Mark Millar/Kick-Ass (v1-v3+)(2008-2014)(digital+)/Kick-Ass 1 (001-008+)(2008-2009)(digital)(G85-Empire)/Kick-Ass 02 (of 08) (2008) (digital) (Minutemen-InnerDemons).cbr
- `   33 MB`  Mark Millar/Kick-Ass (v1-v3+)(2008-2014)(digital+)/Kick-Ass 1 (001-008+)(2008-2009)(digital)(G85-Empire)/scans/Kick-Ass 02 (of 08) (2008) (c2c) (F) (Minutemen-Zone).cbr
- `    1 MB`  Mark Millar/Kick-Ass (v1-v3+)(2008-2014)(digital+)/Kick-Ass 3 (001-008+)(2013-2014)(digital+)/Variant Covers/Kick-Ass 3 02 (2013) (Duncan Fegredo Variant) (Cover ONLY) (NN+ArtNet).cbr
- `    1 MB`  Mark Millar/Kick-Ass (v1-v3+)(2008-2014)(digital+)/Kick-Ass 1 (001-008+)(2008-2009)(digital)(G85-Empire)/variants/Kick-Ass 02 (of 08) (2008) (3rd Printing John Romita Jr Variant) (Minutemen-TheRain).cbr
- `    1 MB`  Mark Millar/Kick-Ass (v1-v3+)(2008-2014)(digital+)/Kick-Ass 1 (001-008+)(2008-2009)(digital)(G85-Empire)/variants/Kick-Ass 02 (of 08) (2008) (Umpteenth Printing Variant) (Cover Only) (Spiritual Beggar-DCP).cbr
- `    1 MB`  Mark Millar/Kick-Ass (v1-v3+)(2008-2014)(digital+)/Kick-Ass 3 (001-008+)(2013-2014)(digital+)/Variant Covers/Kick-Ass 3 02 (2013) (John Romita jr. sketch variant) (Minutemen).cbr
- `    1 MB`  Mark Millar/Kick-Ass (v1-v3+)(2008-2014)(digital+)/Kick-Ass 1 (001-008+)(2008-2009)(digital)(G85-Empire)/variants/Kick-Ass 02 (of 08) (2008) (2nd ptg var cvr) (Minutemen-BHM&Resin).cbr

### judge dredd — #01  *(issue)*

- `   65 MB`  Grant Morrison/Comics/2000 AD (Fleetway 1986)/Judge Dredd - 01 Inferno.cbz
- `   60 MB`  2000AD prog/Yearbooks & Specials/Specials/Judge Dredd/The Complete Judge Dredd 01 (1994) (Judge-Julez).cbr

### kick ass — #07  *(issue)*

- `   66 MB`  Mark Millar/Kick-Ass (v1-v3+)(2008-2014)(digital+)/Kick-Ass 3 (001-008+)(2013-2014)(digital+)/Kick-Ass 3 07 (of 08) (2014) (digital) (Zinc-Empire).cbr
- `   30 MB`  Mark Millar/Kick-Ass (v1-v3+)(2008-2014)(digital+)/Kick-Ass 1 (001-008+)(2008-2009)(digital)(G85-Empire)/Kick-Ass 07 (of 08) (2009) (digital) (Minutemen-InnerDemons).cbr
- `   28 MB`  Mark Millar/Kick-Ass (v1-v3+)(2008-2014)(digital+)/Kick-Ass 1 (001-008+)(2008-2009)(digital)(G85-Empire)/scans/Kick-Ass 07 (of 08) (2009) (c2c) (Minutemen-Delirium-Powers).cbr

### melusine — #03  *(issue)*

- `   78 MB`  Melusine/Melusine 03 - The Vampires' Ball (Cinebook) (2008) (Grodbeldekk).cbr
- `   43 MB`  Melusine/Melusine 03 - Inferno (Eng).cbr

### ythaq forsaken world — #01  *(issue)*

- `   61 MB`  Ythaq/Ythaq - The Forsaken World/Ythaq - The Forsaken World 01 (of 03) (comicsall.net).cbr
- `   60 MB`  Soleil (Europe)/Ythaq - 2008-12 - The Forsaken World (Minutemen)/Ythaq - The Forsaken World 01 (of 03) - Terra Incognita (2008) (Minutemen-Locke).cbr

### planet of sutakola — v1  *(volume)*

- `   67 MB`  Manga/The Planet of Sutakola manga/The Planet of Sutakola v1 c1.2 [batoto].cbz
- `   53 MB`  Manga/The Planet of Sutakola manga/The Planet of Sutakola v1 c1.1 [batoto].cbz

### abe sapien, dark and terrible  *(issue)*

- `   48 MB`  Hellboy/146.)  Abe Sapien #1-3, Dark and Terrible, Parts 1-3  (2012 AD)/Abe Sapien #3, Dark and Terrible, Part 3.cbr
- `   45 MB`  Hellboy/146.)  Abe Sapien #1-3, Dark and Terrible, Parts 1-3  (2012 AD)/Abe Sapien #2, Dark and Terrible, Part 2.cbr
- `   26 MB`  Hellboy/146.)  Abe Sapien #1-3, Dark and Terrible, Parts 1-3  (2012 AD)/Abe Sapien #1, Dark and Terrible, Part 1.cbr

### abe sapien, to last man  *(issue)*

- `   51 MB`  Hellboy/151.)  Abe Sapien #9-11, To the Last Man, Parts 1-3  (2012 AD)/Abe Sapien #9, To the Last Man, Part 1.cbr
- `   44 MB`  Hellboy/151.)  Abe Sapien #9-11, To the Last Man, Parts 1-3  (2012 AD)/Abe Sapien #10, To the Last Man, Part 2.cbr
- `   24 MB`  Hellboy/151.)  Abe Sapien #9-11, To the Last Man, Parts 1-3  (2012 AD)/Abe Sapien #11, To the Last Man, Part 3.cbr

### melusine — #04  *(issue)*

- `   70 MB`  Melusine/Melusine 04 - Love Potions (Cinebook) (2009) (Grodbeldekk).cbr
- `   47 MB`  Melusine/Melusine 04 - Stories to read by the fire (Scanlation) (TranslateAnon).cbr

### judge dredd mega  *(issue)*

- `   26 MB`  2000AD prog/2000AD (Specials, Annuals & Poster Progs + Extras)/2000AD Yearbooks & Specials (1977 - 2013)/Judge Dredd (Specials, Poster Progs & Extras) (-JJ-)/Judge Dredd Mega-Special (1992) [#5].cbr
- `   25 MB`  2000AD prog/2000AD (Specials, Annuals & Poster Progs + Extras)/2000AD Yearbooks & Specials (1977 - 2013)/Judge Dredd (Specials, Poster Progs & Extras) (-JJ-)/Judge Dredd Mega-Special (1990) [#3].cbr
- `   25 MB`  2000AD prog/2000AD (Specials, Annuals & Poster Progs + Extras)/2000AD Yearbooks & Specials (1977 - 2013)/Judge Dredd (Specials, Poster Progs & Extras) (-JJ-)/Judge Dredd Mega-Special (1994) [#7].cbr
- `   20 MB`  2000AD prog/2000AD (Specials, Annuals & Poster Progs + Extras)/2000AD Yearbooks & Specials (1977 - 2013)/Judge Dredd (Specials, Poster Progs & Extras) (-JJ-)/Judge Dredd Mega-Special (1989) [#2].cbr
- `   19 MB`  2000AD prog/2000AD (Specials, Annuals & Poster Progs + Extras)/2000AD Yearbooks & Specials (1977 - 2013)/Judge Dredd (Specials, Poster Progs & Extras) (-JJ-)/Judge Dredd Mega-Special (1988) [#1].cbr

### kick ass — #006  *(issue)*

- `   60 MB`  Mark Millar/Kick-Ass (v1-v3+)(2008-2014)(digital+)/Kick-Ass 3 (001-008+)(2013-2014)(digital+)/scans/Kick-Ass 3 006 (2014) (c2c) (4 Covers) (Monafekk-Empire).cbr
- `   54 MB`  Mark Millar/Kick-Ass (v1-v3+)(2008-2014)(digital+)/Kick-Ass 4 (2018-2019)/Kick-Ass 006 (2018) (Digital) (Zone-Empire).cbr

### kick ass — #05  *(issue)*

- `   50 MB`  Mark Millar/Kick-Ass (v1-v3+)(2008-2014)(digital+)/Kick-Ass 3 (001-008+)(2013-2014)(digital+)/Kick-Ass 3 05 (of 08) (2014) (digital) (Minutemen-PhD).cbr
- `   35 MB`  Mark Millar/Kick-Ass (v1-v3+)(2008-2014)(digital+)/Kick-Ass 1 (001-008+)(2008-2009)(digital)(G85-Empire)/Kick-Ass 05 (of 08) (2009) (digital) (Minutemen-InnerDemons).cbr
- `   29 MB`  Mark Millar/Kick-Ass (v1-v3+)(2008-2014)(digital+)/Kick-Ass 1 (001-008+)(2008-2009)(digital)(G85-Empire)/scans/Kick-Ass 05 (of 08) (2009) (Minutemen-Zone).cbr

### abe sapien, shadow over suwanee  *(issue)*

- `   39 MB`  Hellboy/159.)  Abe Sapien #24-26, The Shadow Over Suwanee, Parts 1-3  (2013 AD)/Abe Sapien #26, The Shadow Over Suwanee, Part 3.cbr
- `   38 MB`  Hellboy/159.)  Abe Sapien #24-26, The Shadow Over Suwanee, Parts 1-3  (2013 AD)/Abe Sapien #24, The Shadow Over Suwanee, Part 1.cbr
- `   35 MB`  Hellboy/159.)  Abe Sapien #24-26, The Shadow Over Suwanee, Parts 1-3  (2013 AD)/Abe Sapien #25, The Shadow Over Suwanee, Part 2.cbr

### judge dredd — #02  *(issue)*

- `   58 MB`  2000AD prog/Yearbooks & Specials/Specials/Judge Dredd/The Complete Judge Dredd 02 (1995) (Judge-Julez).cbr
- `   38 MB`  Grant Morrison/Comics/2000 AD (Fleetway 1986)/Judge Dredd - 02 Book of the Dead.cbz
- `   16 MB`  Judge Dredd The Megazine/Judge Dredd 001-018 (1994-1996)/Judge Dredd 02.cbr

### spirou & fantasio — #18  *(issue)*

- `   72 MB`  Spirou & Fantasio/Spirou & Fantasio 18 - Attack of the Zordolts (2021) (digital) (Mr Norrell-Empire).cbr
- `   39 MB`  Spirou & Fantasio/Spirou & Fantasio 18 - QRN over Bretzelburg.cbz

### kick ass — #005  *(issue)*

- `   62 MB`  Mark Millar/Kick-Ass (v1-v3+)(2008-2014)(digital+)/Kick-Ass 4 (2018-2019)/Kick-Ass 005 (2018) (Digital) (Zone-Empire).cbr
- `   48 MB`  Mark Millar/Kick-Ass (v1-v3+)(2008-2014)(digital+)/Kick-Ass 3 (001-008+)(2013-2014)(digital+)/scans/Kick-Ass 3 005 (2014) (c2c) (3 Covers) (Monafekk-Empire).cbr

### alef thau — #01  *(issue)*

- `   66 MB`  Jodorowsky and Moebius/Alef Thau/Alef Thau - 01 - The Limbless Child.cbr
- `   41 MB`  Heavy Metal/Related_Publications/Alef-Thau 01 Diamond (from Heavy Metal 83) (Lazarus-DCP).cbz

### dominion conflict — #1  *(issue)*

- `   22 MB`  Dominion Conflict 1 No More Noise 01-06/Dominion Conflict 1 No More Noise 6.cbr
- `   21 MB`  Dominion Conflict 1 No More Noise 01-06/Dominion Conflict 1 No More Noise 5.cbr
- `   18 MB`  Dominion Conflict 1 No More Noise 01-06/Dominion Conflict 1 No More Noise 3.cbr
- `   15 MB`  Dominion Conflict 1 No More Noise 01-06/Dominion Conflict 1 No More Noise 1.cbr
- `   15 MB`  Dominion Conflict 1 No More Noise 01-06/Dominion Conflict 1 No More Noise 4.cbr
- `   15 MB`  Dominion Conflict 1 No More Noise 01-06/Dominion Conflict 1 No More Noise 2.cbr

### silk — #002  *(issue)*

- `   53 MB`  Silk/Silk (v1-v2) (2015-2016) GetComics.INFO/Silk v2 (001-009) (2016-Ongoing) (digital) (Minutemen-Faessla)/Silk 002 (2016) (4 covers) (digital) (Minutemen-InnerDemons).cbr
- `   47 MB`  Silk/Silk (v1-v2) (2015-2016) GetComics.INFO/Silk v1 (001-007+Variant Covers) (2015) (digital) (Minutemen-Faessla)/Silk 002 (2015) (2 covers) (digital) (Minutemen-Faessla).cbz
- `    1 MB`  Silk/Silk (v1-v2) (2015-2016) GetComics.INFO/Silk v2 (001-009) (2016-Ongoing) (digital) (Minutemen-Faessla)/Variant Cover/Silk 002 (2015) (digital) (W. Scott Forbes variant) (Minutemen-Mastodon).cbz
- `    1 MB`  Silk/Silk (v1-v2) (2015-2016) GetComics.INFO/Silk v1 (001-007+Variant Covers) (2015) (digital) (Minutemen-Faessla)/Variant Covers/Silk 002 (2015) (digital) (W. Scott Forbes variant) (Minutemen-Mastodon).cbz

### factory — #002  — identical size  *(issue)*

- `   50 MB`  Jodorowsky and Moebius/Factory (2018)/Factory 002 _2018_ _Digital_ _Mephisto-Empire_ (newcomic.info).cbr
- `   50 MB`  Jodorowsky and Moebius/Factory (2018)/Factory 002 (2018) (Digital) (Mephisto-Empire).cbr

### kick ass — #03  *(issue)*

- `   38 MB`  Mark Millar/Kick-Ass (v1-v3+)(2008-2014)(digital+)/Kick-Ass 3 (001-008+)(2013-2014)(digital+)/Kick-Ass 3 03 (of 08) (2013) (digital) (Minutemen-PhD).cbr
- `   38 MB`  Mark Millar/Kick-Ass (v1-v3+)(2008-2014)(digital+)/Kick-Ass 1 (001-008+)(2008-2009)(digital)(G85-Empire)/Kick-Ass 03 (of 08) (2008) (digital) (Minutemen-InnerDemons).cbr
- `   18 MB`  Mark Millar/Kick-Ass (v1-v3+)(2008-2014)(digital+)/Kick-Ass 1 (001-008+)(2008-2009)(digital)(G85-Empire)/scans/Kick-Ass 03 (of 08) (2008) (Minutemen-ReZone).cbr
- `    1 MB`  Mark Millar/Kick-Ass (v1-v3+)(2008-2014)(digital+)/Kick-Ass 1 (001-008+)(2008-2009)(digital)(G85-Empire)/variants/Kick-Ass 03 (of 08) (2008) (3rd Printing John Romita Jr Variant) (Minutemen-TheRain).cbr
- `    1 MB`  Mark Millar/Kick-Ass (v1-v3+)(2008-2014)(digital+)/Kick-Ass 1 (001-008+)(2008-2009)(digital)(G85-Empire)/variants/Kick-Ass 03 (of 08) (2008) (Umpteenth Printing Variant) (Cover Only) (Spiritual Beggar-DCP).cbr
- `    1 MB`  Mark Millar/Kick-Ass (v1-v3+)(2008-2014)(digital+)/Kick-Ass 1 (001-008+)(2008-2009)(digital)(G85-Empire)/variants/Kick-Ass 03 (2nd printing variant cover only) (2008) (Minutemen-ReZone).cbr

### silk — #007  *(issue)*

- `   55 MB`  Silk/Silk (v1-v2) (2015-2016) GetComics.INFO/Silk v2 (001-009) (2016-Ongoing) (digital) (Minutemen-Faessla)/Silk 007 (2016) (4 covers) (digital) (Minutemen-InnerDemons).cbr
- `   43 MB`  Silk/Silk (v1-v2) (2015-2016) GetComics.INFO/Silk v1 (001-007+Variant Covers) (2015) (digital) (Minutemen-Faessla)/Silk 007 (2015) (2 covers) (digital) (Minutemen-Faessla).cbz

### silk — #003  *(issue)*

- `   47 MB`  Silk/Silk (v1-v2) (2015-2016) GetComics.INFO/Silk v1 (001-007+Variant Covers) (2015) (digital) (Minutemen-Faessla)/Silk 003 (2015) (3 covers) (digital) (Minutemen-Faessla).cbz
- `   46 MB`  Silk/Silk (v1-v2) (2015-2016) GetComics.INFO/Silk v2 (001-009) (2016-Ongoing) (digital) (Minutemen-Faessla)/Silk 003 (2016) (digital) (Minutemen-InnerDemons).cbr
- `    2 MB`  Silk/Silk (v1-v2) (2015-2016) GetComics.INFO/Silk v1 (001-007+Variant Covers) (2015) (digital) (Minutemen-Faessla)/Variant Covers/Silk 003 (2015) (digital) (Kris Anka variant) (Minutemen-Mastodon).cbz
- `    2 MB`  Silk/Silk (v1-v2) (2015-2016) GetComics.INFO/Silk v1 (001-007+Variant Covers) (2015) (digital) (Minutemen-Faessla)/Variant Covers/Silk 003 (2015) (digital) (Nick Pitarra WTD variant) (Minutemen-Mastodon).cbz

### silk — #001  *(issue)*

- `   50 MB`  Silk/Silk (v1-v2) (2015-2016) GetComics.INFO/Silk v2 (001-009) (2016-Ongoing) (digital) (Minutemen-Faessla)/Silk 001 (2016) (4 covers) (digital) (Minutemen-Faessla).cbz
- `   43 MB`  Silk/Silk (v1-v2) (2015-2016) GetComics.INFO/Silk v1 (001-007+Variant Covers) (2015) (digital) (Minutemen-Faessla)/Silk 001 (2015) (digital) (Minutemen-Faessla).cbz
- `    3 MB`  Silk/Silk (v1-v2) (2015-2016) GetComics.INFO/Silk v1 (001-007+Variant Covers) (2015) (digital) (Minutemen-Faessla)/Variant Covers/Silk 001 (2015) (digital) (Stacey Lee variant) (Minutemen-Mastodon).cbz
- `    1 MB`  Silk/Silk (v1-v2) (2015-2016) GetComics.INFO/Silk v1 (001-007+Variant Covers) (2015) (digital) (Minutemen-Faessla)/Variant Covers/Silk 001 (2015) (digital) (Skottie Young variant) (Minutemen-Mastodon).cbz

### spirit — #009  *(issue)*

- `   49 MB`  Will Eisner/The Spirit 001-087 (1983-1992)/The Spirit 009 (1985) (Kitchen Sink) (c2c) (CusterBeaton).cbr
- `   48 MB`  Will Eisner/Spirit (1950s)/The_Spirit_009__1947_.cbr

### kick ass — #04  *(issue)*

- `   40 MB`  Mark Millar/Kick-Ass (v1-v3+)(2008-2014)(digital+)/Kick-Ass 3 (001-008+)(2013-2014)(digital+)/Kick-Ass 3 04 (of 08) (2013) (digital) (Minutemen-PhD).cbr
- `   34 MB`  Mark Millar/Kick-Ass (v1-v3+)(2008-2014)(digital+)/Kick-Ass 1 (001-008+)(2008-2009)(digital)(G85-Empire)/Kick-Ass 04 (of 08) (2008) (digital) (Minutemen-InnerDemons).cbr
- `   20 MB`  Mark Millar/Kick-Ass (v1-v3+)(2008-2014)(digital+)/Kick-Ass 1 (001-008+)(2008-2009)(digital)(G85-Empire)/scans/Kick-Ass 04 (of 08) (2008) (Minutemen-ReZone).cbr
- `    1 MB`  Mark Millar/Kick-Ass (v1-v3+)(2008-2014)(digital+)/Kick-Ass 1 (001-008+)(2008-2009)(digital)(G85-Empire)/variants/Kick-Ass 04 (of 08) (2008) (Umpteenth Printing Variant) (Cover Only) (Spiritual Beggar-DCP).cbr
- `    1 MB`  Mark Millar/Kick-Ass (v1-v3+)(2008-2014)(digital+)/Kick-Ass 1 (001-008+)(2008-2009)(digital)(G85-Empire)/variants/Kick-Ass 04 (of 08) (2008) (2nd Printing John Romita Jr Variant) (Minutemen-TheRain).cbr

### archipelago on fire  *(issue)*

- `   60 MB`  The Archipelago on Fire Part 02 (2023) (digital) (Mr Norrell-Empire).cbr
- `   35 MB`  Europe Comics (Collection)/The Archipelago on Fire (Europe Comics 2022) (webrip) (MagicMan-DCP).cbr

### silk — #005  *(issue)*

- `   51 MB`  Silk/Silk (v1-v2) (2015-2016) GetComics.INFO/Silk v2 (001-009) (2016-Ongoing) (digital) (Minutemen-Faessla)/Silk 005 (2016) (digital) (Minutemen-InnerDemons).cbr
- `   44 MB`  Silk/Silk (v1-v2) (2015-2016) GetComics.INFO/Silk v1 (001-007+Variant Covers) (2015) (digital) (Minutemen-Faessla)/Silk 005 (2015) (digital) (Minutemen-Faessla).cbz

### b p r d hell on earth — #142  *(issue)*

- `   58 MB`  Hellboy/168. B.P.R.D. Hell on Earth 140-141 - The Exorcist/B P R D  Hell on Earth 142 - The Exorcist (2016) (digital) (Son of Ultron-Empire).cbr
- `   37 MB`  Hellboy/B P R D  (001-147+)(2002-)(digital)(Minutemen-PhD+InnerDemons)/B P R D  Hell on Earth 142 (2016) (digital) (Minutemen-InnerDemons).cbr

### kick ass — #001  *(issue)*

- `   54 MB`  Mark Millar/Kick-Ass (v1-v3+)(2008-2014)(digital+)/Kick-Ass 4 (2018-2019)/Kick-Ass 001 (2018) (Digital) (Zone-Empire).cbr
- `   41 MB`  Mark Millar/Kick-Ass (v1-v3+)(2008-2014)(digital+)/Kick-Ass 3 (001-008+)(2013-2014)(digital+)/scans/Kick-Ass 3 001 (2013) (6 Covers) (c2c) (Monafekk-Empire).cbr

### abe sapien, new race of man  *(issue)*

- `   50 MB`  Hellboy/147.)  Abe Sapien #4-5, The New Race of Man, Parts 1-2  (2012 AD)/Abe Sapien #5, The New Race of Man, Part 2.cbr
- `   45 MB`  Hellboy/147.)  Abe Sapien #4-5, The New Race of Man, Parts 1-2  (2012 AD)/Abe Sapien #4, The New Race of Man, Part 1.cbr

### spirit — #001  *(issue)*

- `   44 MB`  Will Eisner/Spirit (1950s)/The_Spirit_001_Vital__c2c_52p__Flattermann.cbr
- `   34 MB`  Will Eisner/Spirit (1950s)/Spirit_001_Jon_HP.cbr
- `   16 MB`  Will Eisner/The Spirit 001-087 (1983-1992)/The Spirit 001 (1983) (Kitchen Sink) (c2c).cbz

### avengers — #012  *(issue)*

- `   39 MB`  Avengers/Avengers (2018-2019)/Avengers 012 (2019) (Digital) (Zone-Empire).cbr
- `   31 MB`  Alias  ( Jessica Jones , The Pulse & Appearances)/Appearances/Avengers (2010)/Avengers 012 1 (2011) (Minutemen-TwiztidSax).cbr
- `   25 MB`  Alias  ( Jessica Jones , The Pulse & Appearances)/Appearances/Avengers (2010)/Avengers 012 (2011) (Minutemen-TwiztidSax).cbr

### kick ass — #004  *(issue)*

- `   58 MB`  Mark Millar/Kick-Ass (v1-v3+)(2008-2014)(digital+)/Kick-Ass 4 (2018-2019)/Kick-Ass 004 (2018) (Digital) (Zone-Empire).cbr
- `   36 MB`  Mark Millar/Kick-Ass (v1-v3+)(2008-2014)(digital+)/Kick-Ass 3 (001-008+)(2013-2014)(digital+)/scans/Kick-Ass 3 004 (2013) (c2c) (2 Covers) (Monafekk-Empire).cbr

### absalom — v1  *(volume)*

- `   66 MB`  Absalom/Absalom v01 - Ghosts of London (2012) (digital-SD) (Torquemada).cbr
- `   26 MB`  2000AD - Collections /Absalom/Absalom V1 Nobless Oblige (Dan Dare 2000AD Remix).cbr

### b.p.r.d. hell on earth, wasteland  *(issue)*

- `   37 MB`  Hellboy/144.)  B.P.R.D. - Hell on Earth #107-109, Wasteland, Parts 1-3  (2012 AD)/B.P.R.D. - Hell on Earth #108, Wasteland, Part 2.cbr
- `   36 MB`  Hellboy/144.)  B.P.R.D. - Hell on Earth #107-109, Wasteland, Parts 1-3  (2012 AD)/B.P.R.D. - Hell on Earth #109, Wasteland, Part 3.cbr
- `   19 MB`  Hellboy/144.)  B.P.R.D. - Hell on Earth #107-109, Wasteland, Parts 1-3  (2012 AD)/B.P.R.D. - Hell on Earth #107, Wasteland, Part 1.cbr

### kick ass — #002  *(issue)*

- `   52 MB`  Mark Millar/Kick-Ass (v1-v3+)(2008-2014)(digital+)/Kick-Ass 4 (2018-2019)/Kick-Ass 002 (2018) (Digital) (Zone-Empire).cbr
- `   41 MB`  Mark Millar/Kick-Ass (v1-v3+)(2008-2014)(digital+)/Kick-Ass 3 (001-008+)(2013-2014)(digital+)/scans/Kick-Ass 3 002 (2013) (c2c) (Monafekk-Empire).cbr

### absalom — v3  *(volume)*

- `   54 MB`  2000AD - Collections /Absalom/Absalom V3 (Dan Dare 2000AD Remix).cbr
- `   38 MB`  Absalom/Absalom v03 - Terminal Diagnosis 1.cbz

### absalom — v4  *(volume)*

- `   49 MB`  Absalom/Absalom v04 - Terminal Diagnosis 2.cbz
- `   42 MB`  2000AD - Collections /Absalom/Absalom V4 Terminal Diagnosis - Book One (Dan Dare 2000AD Remix).cbr

### six from sirius — v1  *(volume)*

- `   60 MB`  Six From Sirius 001-004/Six From Sirius v01 (1984).cbz
- `   31 MB`  Six From Sirius 2 01-04/Six From Sirius 2 v01 (1996).cbz

### spirit — #010  *(issue)*

- `   46 MB`  Will Eisner/Spirit (1950s)/The_Spirit_010__c2c_52p__Flattermann_.cbr
- `   45 MB`  Will Eisner/The Spirit 001-087 (1983-1992)/The Spirit 010 (1985) (Kitchen Sink) (c2c) (CusterBeaton).cbr

### best of judge dredd  — identical size  *(special)*

- `   45 MB`  2000AD prog/Yearbooks & Specials/Specials/Judge Dredd/Best of Judge Dredd Special Edition (1999) (Judge-Julez).cbr
- `   45 MB`  2000AD prog/2000AD (Specials, Annuals & Poster Progs + Extras)/2000AD Yearbooks & Specials (1977 - 2013)/Judge Dredd (Specials, Poster Progs & Extras) (-JJ-)/Best of Judge Dredd Special Edition 1999.cbr

### daredevil noir — #03  *(issue)*

- `   44 MB`  GG Studio (Collection) (2010-2012)/Marvel Noir (2009-2011)(digital)/Daredevil Noir (001-004+)(2009)(digital)(Minutemen-PhD)/Daredevil Noir 03 (of 04) (2009) (digital) (Minutemen-PhD).cbr
- `   44 MB`  Aster Blistok/Le Vagabond des Limbes/Daredevil Noir (001-004+)(2009)(digital)(Minutemen-PhD)/Daredevil Noir 03 (of 04) (2009) (digital) (Minutemen-PhD).cbr
- `    1 MB`  GG Studio (Collection) (2010-2012)/Marvel Noir (2009-2011)(digital)/Daredevil Noir (001-004+)(2009)(digital)(Minutemen-PhD)/covers/Daredevil Noir 03 (2009) (Variant Cover Only) [extracted] (Archangel-DCP).cbr
- `    1 MB`  Aster Blistok/Le Vagabond des Limbes/Daredevil Noir (001-004+)(2009)(digital)(Minutemen-PhD)/covers/Daredevil Noir 03 (2009) (Variant Cover Only) [extracted] (Archangel-DCP).cbr

### spirit — #007  *(issue)*

- `   45 MB`  Will Eisner/Spirit (1950s)/The_Spirit_007__c2c_52p__Flattermann_.cbr
- `   44 MB`  Will Eisner/The Spirit 001-087 (1983-1992)/The Spirit 007 (1984) (Kitchen Sink) (c2c) (CusterBeaton).cbr

### silk — #004  *(issue)*

- `   46 MB`  Silk/Silk (v1-v2) (2015-2016) GetComics.INFO/Silk v1 (001-007+Variant Covers) (2015) (digital) (Minutemen-Faessla)/Silk 004 (2015) (digital) (Minutemen-Faessla).cbz
- `   42 MB`  Silk/Silk (v1-v2) (2015-2016) GetComics.INFO/Silk v2 (001-009) (2016-Ongoing) (digital) (Minutemen-Faessla)/Silk 004 (2016) (digital) (Minutemen-InnerDemons).cbr

### daredevil noir — #02  *(issue)*

- `   44 MB`  GG Studio (Collection) (2010-2012)/Marvel Noir (2009-2011)(digital)/Daredevil Noir (001-004+)(2009)(digital)(Minutemen-PhD)/Daredevil Noir 02 (of 04) (2009) (digital) (Minutemen-PhD).cbr
- `   44 MB`  Aster Blistok/Le Vagabond des Limbes/Daredevil Noir (001-004+)(2009)(digital)(Minutemen-PhD)/Daredevil Noir 02 (of 04) (2009) (digital) (Minutemen-PhD).cbr
- `    0 MB`  GG Studio (Collection) (2010-2012)/Marvel Noir (2009-2011)(digital)/Daredevil Noir (001-004+)(2009)(digital)(Minutemen-PhD)/covers/Daredevil Noir 02 (2009) (Variant Cover Only) [extracted] (Archangel-DCP).cbr
- `    0 MB`  Aster Blistok/Le Vagabond des Limbes/Daredevil Noir (001-004+)(2009)(digital)(Minutemen-PhD)/covers/Daredevil Noir 02 (2009) (Variant Cover Only) [extracted] (Archangel-DCP).cbr

### b p r d hell on earth — #143  *(issue)*

- `   53 MB`  Hellboy/B P R D  Hell on Earth 143-147 - Cometh the Hour (2016)/B P R D  Hell on Earth 143 - Cometh the Hour (2016) (digital) (Son of Ultron-Empire).cbr
- `   35 MB`  Hellboy/B P R D  (001-147+)(2002-)(digital)(Minutemen-PhD+InnerDemons)/B P R D  Hell on Earth 143 (2016) (digital) (Minutemen-InnerDemons).cbr

### black widow — #01  *(issue)*

- `   42 MB`  Black Widow/Black Widow 1 v7 (001 - 008) (2010)/Black Widow 01 (2010) (Digital) (G85-Empire).cbr
- `   21 MB`  Black Widow/Black Widow 1 v2 - Breakdown [2001]/Black Widow 01 (of 03) (2001) (digital) (Minutemen-PhD).cbz
- `   21 MB`  Black Widow/Black Widow 1 v2 - Breakdown [2001]/Black Widow 01 (of 03) (2001) (digital) (Minutemen-PhD).cbr
- `    3 MB`  Black Widow/Black Widow 1 v7 (001 - 008) (2010)/Black Widow #01 & #02 (2010) (Variant Covers Only).cbr
- `    1 MB`  Black Widow/Black Widow 1 v7 (001 - 008) (2010)/Black Widow 01 (2010) (2nd Print Cover) (Legion-CPS).cbr

### b.p.r.d. hell on earth, return of master  *(issue)*

- `   31 MB`  Hellboy/143.)  B.P.R.D. - Hell on Earth - The Return of the Master #1-5  (2012 AD)/B.P.R.D. - Hell on Earth #100, The Return of the Master, Part 3.cbr
- `   28 MB`  Hellboy/143.)  B.P.R.D. - Hell on Earth - The Return of the Master #1-5  (2012 AD)/B.P.R.D. - Hell on Earth #101, The Return of the Master, Part 4.cbr
- `   28 MB`  Hellboy/143.)  B.P.R.D. - Hell on Earth - The Return of the Master #1-5  (2012 AD)/B.P.R.D. - Hell on Earth #102, The Return of the Master, Part 5.cbr

### ythaq forsaken world — #03  *(issue)*

- `   43 MB`  Ythaq/Ythaq - The Forsaken World/Ythaq - The Forsaken World 03 (of 03) (comicsall.net).cbr
- `   43 MB`  Soleil (Europe)/Ythaq - 2008-12 - The Forsaken World (Minutemen)/Ythaq - The Forsaken World 03 (of 03) - Sigh of the Stars (2009) (Minutemen-Locke).cbr

### daredevil noir — #04  *(issue)*

- `   41 MB`  GG Studio (Collection) (2010-2012)/Marvel Noir (2009-2011)(digital)/Daredevil Noir (001-004+)(2009)(digital)(Minutemen-PhD)/Daredevil Noir 04 (of 04) (2009) (digital) (Minutemen-PhD).cbr
- `   41 MB`  Aster Blistok/Le Vagabond des Limbes/Daredevil Noir (001-004+)(2009)(digital)(Minutemen-PhD)/Daredevil Noir 04 (of 04) (2009) (digital) (Minutemen-PhD).cbr
- `    1 MB`  GG Studio (Collection) (2010-2012)/Marvel Noir (2009-2011)(digital)/Daredevil Noir (001-004+)(2009)(digital)(Minutemen-PhD)/covers/Daredevil Noir 04 (2009) (Variant Cover Only) [extracted] (Archangel-DCP).cbr
- `    1 MB`  Aster Blistok/Le Vagabond des Limbes/Daredevil Noir (001-004+)(2009)(digital)(Minutemen-PhD)/covers/Daredevil Noir 04 (2009) (Variant Cover Only) [extracted] (Archangel-DCP).cbr

### spirit — #004  *(issue)*

- `   37 MB`  Will Eisner/Spirit (1950s)/The_Spirit_004__1945__52pg_Quality.cbz
- `   22 MB`  Will Eisner/Spirit (1950s)/Spirit_004_ctc__1953_.cbr
- `   20 MB`  Will Eisner/The Spirit 001-087 (1983-1992)/The Spirit 004 (1984) (Kitchen Sink) (c2c).cbr

### biohazard heavenly island — v5  *(volume)*

- `   11 MB`  Manga/Biohazard/Biohazard - Heavenly Island - v5 c39 [batoto].cbz
- `    8 MB`  Manga/Biohazard/Biohazard - Heavenly Island - v5 c45 [batoto].cbz
- `    8 MB`  Manga/Biohazard/Biohazard - Heavenly Island - v5 c48 [batoto].cbz
- `    7 MB`  Manga/Biohazard/Biohazard - Heavenly Island - v5 c44 [batoto].cbz
- `    7 MB`  Manga/Biohazard/Biohazard - Heavenly Island - v5 c40 [batoto].cbz
- `    7 MB`  Manga/Biohazard/Biohazard - Heavenly Island - v5 c43 [batoto].cbz
- `    6 MB`  Manga/Biohazard/Biohazard - Heavenly Island - v5 c42 [batoto].cbz
- `    6 MB`  Manga/Biohazard/Biohazard - Heavenly Island - v5 c41 [batoto].cbz
- `    6 MB`  Manga/Biohazard/Biohazard Heavenly Island Vol.005 Ch.046 The End [KissManga].cbz
- `    5 MB`  Manga/Biohazard/Biohazard Heavenly Island Vol.005 Ch.047 The Undulating Terror Approaches [KissManga].cbz
- `    5 MB`  Manga/Biohazard/Biohazard - Heavenly Island - v5 c49 [batoto].cbz
- `    4 MB`  Manga/Biohazard/Biohazard - Heavenly Island - v5 c50 [batoto].cbz

### spirit — #011  *(issue)*

- `   39 MB`  Will Eisner/Spirit (1950s)/The_Spirit_011__Quality_Snardermann.cbz
- `   39 MB`  Will Eisner/The Spirit 001-087 (1983-1992)/The Spirit 011 (1985) (Kitchen Sink) (c2c) (emcee).cbr

### skeleton story — #001  *(issue)*

- `   42 MB`  GG Studio (Collection) (2010-2012)/A Skeleton Story (001-006) (2010-2011)/A Skeleton Story 001 (2010) (Digital) (K6-Empire).cbr
- `   36 MB`  GG Studio (Collection) (2010-2012)/A Skeleton Story (001-006) (2010-2011)/A Skeleton Story 001 (2010) 32p (ocd-xandre).cbr

### b.p.r.d. hell on earth, modern prometheus  *(issue)*

- `   39 MB`  Hellboy/165.)  B.P.R.D. - Hell on Earth #133-134, Modern Prometheus, Parts 1-2  (2014 AD)/B.P.R.D. - Hell on Earth #133, Modern Prometheus, Part 1.cbr
- `   39 MB`  Hellboy/165.)  B.P.R.D. - Hell on Earth #133-134, Modern Prometheus, Parts 1-2  (2014 AD)/B.P.R.D. - Hell on Earth #134, Modern Prometheus, Part 2.cbr

### spirit — #003  *(issue)*

- `   36 MB`  Will Eisner/Spirit (1950s)/The_Spirit_003__c2c_52p_.cbr
- `   26 MB`  Will Eisner/Spirit (1950s)/Spirit_003__1952_.cbr
- `   16 MB`  Will Eisner/The Spirit 001-087 (1983-1992)/The Spirit 003 (1984) (Kitchen Sink) (c2c).cbz

### luke cage noir — #02  *(issue)*

- `   38 MB`  GG Studio (Collection) (2010-2012)/Marvel Noir (2009-2011)(digital)/Luke Cage Noir (001-004+)(2009-2010)(digital)(Minutemen-Faessla)/Luke Cage Noir 02 (of 4) (2009) (digital) (Minutemen-Faessla).cbz
- `   38 MB`  Aster Blistok/Le Vagabond des Limbes/Luke Cage Noir (001-004+)(2009-2010)(digital)(Minutemen-Faessla)/Luke Cage Noir 02 (of 4) (2009) (digital) (Minutemen-Faessla).cbz
- `    1 MB`  GG Studio (Collection) (2010-2012)/Marvel Noir (2009-2011)(digital)/Luke Cage Noir (001-004+)(2009-2010)(digital)(Minutemen-Faessla)/covers/Luke Cage Noir 02 (2009) (Variant Cover Only) [extracted] (Minutemen-D.T.Rocafella).cbr
- `    1 MB`  Aster Blistok/Le Vagabond des Limbes/Luke Cage Noir (001-004+)(2009-2010)(digital)(Minutemen-Faessla)/covers/Luke Cage Noir 02 (2009) (Variant Cover Only) [extracted] (Minutemen-D.T.Rocafella).cbr

### b.p.r.d. hell on earth — #144  *(issue)*

- `   47 MB`  Hellboy/B P R D  Hell on Earth 143-147 - Cometh the Hour (2016)/B.P.R.D. Hell on Earth 144 - Cometh the Hour (2016) (digital) (Son of Ultron-Empire).cbr
- `   30 MB`  Hellboy/B P R D  Hell on Earth 143-147 - Cometh the Hour (2016)/B.P.R.D. Hell on Earth 144 (2016) (digital) (Minutemen-Faessla).cbz

### spirit — #006  *(issue)*

- `   44 MB`  Will Eisner/Spirit (1950s)/The_Spirit_006__c2c_52p__Flattermann_.cbr
- `   32 MB`  Will Eisner/The Spirit 001-087 (1983-1992)/The Spirit 006 (1984) (Kitchen Sink) (c2c) (emcee).cbr

### daredevil noir — #01  *(issue)*

- `   37 MB`  GG Studio (Collection) (2010-2012)/Marvel Noir (2009-2011)(digital)/Daredevil Noir (001-004+)(2009)(digital)(Minutemen-PhD)/Daredevil Noir 01 (of 04) (2009) (digital) (Minutemen-PhD).cbr
- `   37 MB`  Aster Blistok/Le Vagabond des Limbes/Daredevil Noir (001-004+)(2009)(digital)(Minutemen-PhD)/Daredevil Noir 01 (of 04) (2009) (digital) (Minutemen-PhD).cbr
- `    1 MB`  GG Studio (Collection) (2010-2012)/Marvel Noir (2009-2011)(digital)/Daredevil Noir (001-004+)(2009)(digital)(Minutemen-PhD)/covers/Daredevil Noir 01 (2009) (Variant Cover Only) [extracted] (Archangel-DCP).cbr
- `    1 MB`  Aster Blistok/Le Vagabond des Limbes/Daredevil Noir (001-004+)(2009)(digital)(Minutemen-PhD)/covers/Daredevil Noir 01 (2009) (Variant Cover Only) [extracted] (Archangel-DCP).cbr

### daredevils killing ground  *(issue)*

- `   38 MB`  Alan Moore/Alan Moore Collection I- English Invasion/Alan Moore Collection II- Marvel UK/Captain Britain/Captain Britain (Marvel Comics UK)/The Daredevils/The Daredevils #004- Killing Ground.cbz
- `   37 MB`  Alan Moore/Alan Moore Collection I- English Invasion/Alan Moore Collection II- Marvel UK/Captain Britain/Captain Britain (Marvel Comics UK)/The Daredevils/The Daredevils #005- Killing Ground.cbz

### b.p.r.d. hell on earth, devils wings  *(issue)*

- `   38 MB`  Hellboy/160.)  B.P.R.D. - Hell on Earth #120-121, The Devil s Wings, Parts 1-2  (2013 AD)/B.P.R.D. - Hell on Earth #121, The Devils Wings, Part 2.cbr
- `   35 MB`  Hellboy/160.)  B.P.R.D. - Hell on Earth #120-121, The Devil s Wings, Parts 1-2  (2013 AD)/B.P.R.D. - Hell on Earth #120, The Devils Wings, Part 1.cbr

### mighty avengers — #004  — identical size  *(issue)*

- `   36 MB`  Alias  ( Jessica Jones , The Pulse & Appearances)/Appearances/Mighty Avengers/Mighty Avengers 004 INH (2013) (Digital) (Zone-Empire).cbr
- `   36 MB`  Alias  ( Jessica Jones , The Pulse & Appearances)/Appearances/Mighty Avengers/Mighty Avengers 004 (2013) (Digital) (Zone-Empire).cbr

### magic — #01  *(issue)*

- `   41 MB`  Europe Comics (Collection)/Magic 7 01 - Never Alone (Europe Comics 2019) (webrip) (MagicMan-DCP).cbr
- `   31 MB`  Europe Comics (Collection)/Magic 01 - The Girl with Purple Hair (Europe Comics 2021) (webrip) (MagicMan-DCP).cbr

### avengers — #013  *(issue)*

- `   51 MB`  Avengers/Avengers (2018-2019)/Avengers 013 (2019) (Digital) (Zone-Empire).cbr
- `   18 MB`  Alias  ( Jessica Jones , The Pulse & Appearances)/Appearances/Avengers (2010)/Avengers 013 (2011) (two covers) (Minutemen-Shepherd&Saxon).cbr
- `    2 MB`  Alias  ( Jessica Jones , The Pulse & Appearances)/Appearances/Avengers (2010)/Avengers 013 (2011) (Paul Renaud X-Men Evolutions Variant) (Minutemen-MegaJackal).cbr

### wolverine noir — #004  *(issue)*

- `   34 MB`  GG Studio (Collection) (2010-2012)/Marvel Noir (2009-2011)(digital)/Wolverine Noir (001-004+)(2009)(digital)(Minutemen-Faessla)/Wolverine Noir 004 (2009) (digital) (Minutemen-Faessla).cbz
- `   34 MB`  Aster Blistok/Le Vagabond des Limbes/Wolverine Noir (001-004+)(2009)(digital)(Minutemen-Faessla)/Wolverine Noir 004 (2009) (digital) (Minutemen-Faessla).cbz
- `    1 MB`  GG Studio (Collection) (2010-2012)/Marvel Noir (2009-2011)(digital)/Wolverine Noir (001-004+)(2009)(digital)(Minutemen-Faessla)/covers/Wolverine Noir 004 (2009) (Variant Cover Only) [extracted] (Minutemen-D.T.Rocafella).cbr
- `    1 MB`  Aster Blistok/Le Vagabond des Limbes/Wolverine Noir (001-004+)(2009)(digital)(Minutemen-Faessla)/covers/Wolverine Noir 004 (2009) (Variant Cover Only) [extracted] (Minutemen-D.T.Rocafella).cbr

### punisher noir — #03  *(issue)*

- `   35 MB`  GG Studio (Collection) (2010-2012)/Marvel Noir (2009-2011)(digital)/Punisher Noir (001-004+)(2009-2010)(digital)(Minutemen-Slayer)/Punisher Noir 03 (of 04) (2009) (digital) (Minutemen-Slayer).cbr
- `   35 MB`  Aster Blistok/Le Vagabond des Limbes/Punisher Noir (001-004+)(2009-2010)(digital)(Minutemen-Slayer)/Punisher Noir 03 (of 04) (2009) (digital) (Minutemen-Slayer).cbr
- `    1 MB`  GG Studio (Collection) (2010-2012)/Marvel Noir (2009-2011)(digital)/Punisher Noir (001-004+)(2009-2010)(digital)(Minutemen-Slayer)/covers/Punisher Noir 03 (2009) (Variant Cover Only) [extracted] (Minutemen-DTs).cbr
- `    1 MB`  Aster Blistok/Le Vagabond des Limbes/Punisher Noir (001-004+)(2009-2010)(digital)(Minutemen-Slayer)/covers/Punisher Noir 03 (2009) (Variant Cover Only) [extracted] (Minutemen-DTs).cbr

### guarding globe — #001  *(issue)*

- `   38 MB`  Image comics/Guarding the Globe v1 (001-006)(2010-2011)/Guarding the Globe 001 (2010) (Digital) (Salem-Empire).cbr
- `   32 MB`  Image comics/Guarding the Globe v2 (001-006)(2012-2013)/Guarding the Globe 001 (2012) (2 Covers) (Digital) (Zone-Empire).cbr

### punisher noir — #01  *(issue)*

- `   34 MB`  GG Studio (Collection) (2010-2012)/Marvel Noir (2009-2011)(digital)/Punisher Noir (001-004+)(2009-2010)(digital)(Minutemen-Slayer)/Punisher Noir 01 (of 04) (2009) (digital) (Minutemen-Slayer).cbr
- `   34 MB`  Aster Blistok/Le Vagabond des Limbes/Punisher Noir (001-004+)(2009-2010)(digital)(Minutemen-Slayer)/Punisher Noir 01 (of 04) (2009) (digital) (Minutemen-Slayer).cbr
- `    1 MB`  GG Studio (Collection) (2010-2012)/Marvel Noir (2009-2011)(digital)/Punisher Noir (001-004+)(2009-2010)(digital)(Minutemen-Slayer)/covers/Punisher Noir 01 (2009) (Variant Cover Only) [extracted] (Minutemen-ThePyre&Rocafella).cbr
- `    1 MB`  Aster Blistok/Le Vagabond des Limbes/Punisher Noir (001-004+)(2009-2010)(digital)(Minutemen-Slayer)/covers/Punisher Noir 01 (2009) (Variant Cover Only) [extracted] (Minutemen-ThePyre&Rocafella).cbr

### punisher noir — #04  *(issue)*

- `   34 MB`  GG Studio (Collection) (2010-2012)/Marvel Noir (2009-2011)(digital)/Punisher Noir (001-004+)(2009-2010)(digital)(Minutemen-Slayer)/Punisher Noir 04 (of 04) (2010) (digital) (Minutemen-Slayer).cbr
- `   34 MB`  Aster Blistok/Le Vagabond des Limbes/Punisher Noir (001-004+)(2009-2010)(digital)(Minutemen-Slayer)/Punisher Noir 04 (of 04) (2010) (digital) (Minutemen-Slayer).cbr
- `    1 MB`  GG Studio (Collection) (2010-2012)/Marvel Noir (2009-2011)(digital)/Punisher Noir (001-004+)(2009-2010)(digital)(Minutemen-Slayer)/covers/Punisher Noir 04 (2010) (Variant Cover Only) [extracted] (Minutemen-DTs).cbr
- `    1 MB`  Aster Blistok/Le Vagabond des Limbes/Punisher Noir (001-004+)(2009-2010)(digital)(Minutemen-Slayer)/covers/Punisher Noir 04 (2010) (Variant Cover Only) [extracted] (Minutemen-DTs).cbr

### abe sapien, shape of things to come  *(issue)*

- `   46 MB`  Hellboy/148.)  Abe Sapien #6-7, The Shape of Things to Come, Parts 1-2  (2012 AD)/Abe Sapien #6, The Shape of Things to Come, Part 1.cbr
- `   23 MB`  Hellboy/148.)  Abe Sapien #6-7, The Shape of Things to Come, Parts 1-2  (2012 AD)/Abe Sapien #7, The Shape of Things to Come, Part 2.cbr

### b.p.r.d. hell on earth, nowhere, nothing, never  *(issue)*

- `   31 MB`  Hellboy/164.)  B.P.R.D. - Hell on Earth #130-132, Nowhere, Nothing, Never, Parts 1-3  (2014 AD)/B.P.R.D. - Hell on Earth #132, Nowhere, Nothing, Never, Part 3.cbr
- `   19 MB`  Hellboy/164.)  B.P.R.D. - Hell on Earth #130-132, Nowhere, Nothing, Never, Parts 1-3  (2014 AD)/B.P.R.D. - Hell on Earth #131, Nowhere, Nothing, Never, Part 2.cbr
- `   18 MB`  Hellboy/164.)  B.P.R.D. - Hell on Earth #130-132, Nowhere, Nothing, Never, Parts 1-3  (2014 AD)/B.P.R.D. - Hell on Earth #130, Nowhere, Nothing, Never, Part 1.cbr

### orville — #004  *(issue)*

- `   36 MB`  The Orville/The Orville 004 - The Word of Avis Part 02 (of 02) (2019) (digital) (Son of Ultron-Empire).cbr
- `   31 MB`  The Orville/The Orville 004 - Heroes Part 02 (of 02) (2020) (digital) (Son of Ultron-Empire).cbr

### spirou & fantasio — #08  *(issue)*

- `   35 MB`  Spirou & Fantasio/Spirou & Fantasio 08 - The Wrong Face.cbz
- `   32 MB`  Spirou & Fantasio/Spirou & Fantasio 08 - Tough Luck Vito (2015) (Cinebook) (digital) (Lynx-Empire).cbr

### spirit — #012  *(issue)*

- `   38 MB`  Will Eisner/Spirit (1950s)/The_Spirit_012__c2c_52p__Snardermann.cbz
- `   29 MB`  Will Eisner/The Spirit 001-087 (1983-1992)/The Spirit 012 (1985) (Kitchen Sink) (c2c) (CusterBeaton).cbr

### luke cage noir — #03  *(issue)*

- `   33 MB`  GG Studio (Collection) (2010-2012)/Marvel Noir (2009-2011)(digital)/Luke Cage Noir (001-004+)(2009-2010)(digital)(Minutemen-Faessla)/Luke Cage Noir 03 (of 4) (2009) (digital) (Minutemen-Faessla).cbz
- `   33 MB`  Aster Blistok/Le Vagabond des Limbes/Luke Cage Noir (001-004+)(2009-2010)(digital)(Minutemen-Faessla)/Luke Cage Noir 03 (of 4) (2009) (digital) (Minutemen-Faessla).cbz
- `    0 MB`  GG Studio (Collection) (2010-2012)/Marvel Noir (2009-2011)(digital)/Luke Cage Noir (001-004+)(2009-2010)(digital)(Minutemen-Faessla)/covers/Luke Cage Noir 03 (2009) (Variant Cover Only) [extracted] (Minutemen-DTs).cbr
- `    0 MB`  Aster Blistok/Le Vagabond des Limbes/Luke Cage Noir (001-004+)(2009-2010)(digital)(Minutemen-Faessla)/covers/Luke Cage Noir 03 (2009) (Variant Cover Only) [extracted] (Minutemen-DTs).cbr

### love & rockets — v1 — #001  *(volume)*

- `   40 MB`  Hernandez brothers/Love and Rockets/Love & Rockets v1 (001-042)(1981-1993)/Love & Rockets v1 001 (1982) (c2c) (Pyramid).cbz
- `   26 MB`  Hernandez brothers/Love and Rockets/Love & Rockets v1 (001-042)(1981-1993)/Love & Rockets v1 001 (1992 - 3rd printing) (420-DCP).cbr

### tank girl — v2  *(volume)*

- `   17 MB`  Tank Girl/02. Tank Girl - Volume 2/Tank Girl Vol. 2 - 2 of 4 - Summer Love Sensation pt. 1 (Dark Horse, 1993).cbr
- `   17 MB`  Tank Girl/02. Tank Girl - Volume 2/Tank Girl Vol. 2 - 4 of 4 - Blue Helmet (Dark Horse, 1993).cbr
- `   17 MB`  Tank Girl/02. Tank Girl - Volume 2/Tank Girl Vol. 2 - 1 of 4 - I've Got Friends at Bell's End (Dark Horse, 1993).cbr
- `   16 MB`  Tank Girl/02. Tank Girl - Volume 2/Tank Girl Vol. 2 - 3 of 4 - Summer Love Sensation pt. 3,5 (Dark Horse, 1993).cbr

### spirit — #008  *(issue)*

- `   37 MB`  Will Eisner/The Spirit 001-087 (1983-1992)/The Spirit 008 (1985) (Kitchen Sink) (c2c) (emcee).cbr
- `   29 MB`  Will Eisner/Spirit (1950s)/The_Spirit_008__1947__52pg_Quality.cbr

### luke cage noir — #04  *(issue)*

- `   32 MB`  GG Studio (Collection) (2010-2012)/Marvel Noir (2009-2011)(digital)/Luke Cage Noir (001-004+)(2009-2010)(digital)(Minutemen-Faessla)/Luke Cage Noir 04 (of 4) (2010) (digital) (Minutemen-Faessla).cbz
- `   32 MB`  Aster Blistok/Le Vagabond des Limbes/Luke Cage Noir (001-004+)(2009-2010)(digital)(Minutemen-Faessla)/Luke Cage Noir 04 (of 4) (2010) (digital) (Minutemen-Faessla).cbz
- `    0 MB`  GG Studio (Collection) (2010-2012)/Marvel Noir (2009-2011)(digital)/Luke Cage Noir (001-004+)(2009-2010)(digital)(Minutemen-Faessla)/covers/Luke Cage Noir 04 (2010) (Variant Cover Only) [extracted] (Minutemen-DTs).cbr
- `    0 MB`  Aster Blistok/Le Vagabond des Limbes/Luke Cage Noir (001-004+)(2009-2010)(digital)(Minutemen-Faessla)/covers/Luke Cage Noir 04 (2010) (Variant Cover Only) [extracted] (Minutemen-DTs).cbr

### anna mercury — #001  *(issue)*

- `   29 MB`  Warren Ellis/2008/2008 Anna Mercury/Vol 2/Anna Mercury 2 001 (2009) (Three Covers) (Minutemen-Shamil).cbr
- `   24 MB`  Warren Ellis/2008/2008 Anna Mercury/Vol 1 [Complete]/Anna Mercury 001 (All Four Covers) (2008) (c2c) (The Ramones-DCP).cbr
- `    4 MB`  Warren Ellis/2008/2008 Anna Mercury/Vol 1 [Complete]/Anna Mercury 001 (Matt Martin Sketch Cover) (2008) (Minutemen-Special).cbr
- `    2 MB`  Warren Ellis/2008/2008 Anna Mercury/Vol 1 [Complete]/Anna Mercury 001 (NYCC Cover Only) (2008) (The Ramones-DCP).cbr
- `    2 MB`  Warren Ellis/2008/2008 Anna Mercury/Vol 1 [Complete]/Anna Mercury 001 Auxiliary (Cover Only) (2008) (The Ramones-DCP).cbr
- `    2 MB`  Warren Ellis/2008/2008 Anna Mercury/Vol 1 [Complete]/Anna Mercury 001 (WWP Variant Cover) (2008) (The Ramones-DCP).cbr
- `    2 MB`  Warren Ellis/2008/2008 Anna Mercury/Vol 1 [Complete]/Anna Mercury 001 (SDCC Variant Cover) (2008) (Steam-DCP).cbr
- `    1 MB`  Warren Ellis/2008/2008 Anna Mercury/Vol 1 [Complete]/Anna Mercury 001 (of 5) (2008) (Wizard World Chicago Variant) (Minutemen-TheRain).cbr

### wolverine noir — #003  *(issue)*

- `   32 MB`  GG Studio (Collection) (2010-2012)/Marvel Noir (2009-2011)(digital)/Wolverine Noir (001-004+)(2009)(digital)(Minutemen-Faessla)/Wolverine Noir 003 (2009) (digital) (Minutemen-Faessla).cbz
- `   32 MB`  Aster Blistok/Le Vagabond des Limbes/Wolverine Noir (001-004+)(2009)(digital)(Minutemen-Faessla)/Wolverine Noir 003 (2009) (digital) (Minutemen-Faessla).cbz
- `    1 MB`  GG Studio (Collection) (2010-2012)/Marvel Noir (2009-2011)(digital)/Wolverine Noir (001-004+)(2009)(digital)(Minutemen-Faessla)/covers/Wolverine Noir 003 (2009) (Variant Cover Only) [extracted] (Minutemen - DTs&okaza carlita).cbr
- `    1 MB`  Aster Blistok/Le Vagabond des Limbes/Wolverine Noir (001-004+)(2009)(digital)(Minutemen-Faessla)/covers/Wolverine Noir 003 (2009) (Variant Cover Only) [extracted] (Minutemen - DTs&okaza carlita).cbr

### spirit — #014  *(issue)*

- `   54 MB`  Will Eisner/Spirit (1950s)/The_Spirit_014__1948__52pg_Quality.cbz
- `   10 MB`  Will Eisner/The Spirit 001-087 (1983-1992)/The Spirit 014 (1985) (Kitchen Sink) (c2c).cbr

### locke & key welcome to lovecraft  — identical size  *(special)*

- `   32 MB`  Locke & Key/Locke & Key - Extras/Locke & Key - Welcome to Lovecraft Special Edition.cbr
- `   32 MB`  Locke & Key/Locke & Key - Extras/Locke & Key - Welcome to Lovecraft Special Edition 01 (2009) (2 covers) (c2c) (GreenEngine-DCP).cbr

### black widow — #03  *(issue)*

- `   36 MB`  Black Widow/Black Widow 1 v7 (001 - 008) (2010)/Black Widow 03 (2010) (Digital) (G85-Empire).cbr
- `   29 MB`  Black Widow/Black Widow 1 v2 - Breakdown [2001]/Black Widow 03 (of 03) (2001) (digital) (Minutemen-PhD).cbr

### orville — #003  *(issue)*

- `   35 MB`  The Orville/The Orville 003 - The Word of Avis Part 01 (of 02) (2019) (digital) (Son of Ultron-Empire).cbr
- `   28 MB`  The Orville/The Orville 003 - Heroes Part 01 (of 02) (2020) (digital) (Son of Ultron-Empire).cbr

### spider man noir — #01  *(issue)*

- `   31 MB`  GG Studio (Collection) (2010-2012)/Marvel Noir (2009-2011)(digital)/Spider-Man Noir (v1-v2+)(2009-2010)(digital)/Spider-Man Noir v1 (001-004)(2009)(digital)(Minutemen-Faessla)/Spider-Man Noir 01 (of 04) (2009) (digital) (Minutemen-Faessla).cbz
- `   31 MB`  Aster Blistok/Le Vagabond des Limbes/Spider-Man Noir (v1-v2+)(2009-2010)(digital)/Spider-Man Noir v1 (001-004)(2009)(digital)(Minutemen-Faessla)/Spider-Man Noir 01 (of 04) (2009) (digital) (Minutemen-Faessla).cbz
- `    1 MB`  GG Studio (Collection) (2010-2012)/Marvel Noir (2009-2011)(digital)/Spider-Man Noir (v1-v2+)(2009-2010)(digital)/Variant Covers/Spider-Man Noir 01 (2009) (Calero Variant Only) (Spiritual Beggar-DCP).cbr
- `    1 MB`  Aster Blistok/Le Vagabond des Limbes/Spider-Man Noir (v1-v2+)(2009-2010)(digital)/Variant Covers/Spider-Man Noir 01 (2009) (Calero Variant Only) (Spiritual Beggar-DCP).cbr

### guarding globe — #003  *(issue)*

- `   39 MB`  Image comics/Guarding the Globe v1 (001-006)(2010-2011)/Guarding the Globe 003 (2011) (2 covers) (Digital) (Salem-Empire).cbr
- `   24 MB`  Image comics/Guarding the Globe v2 (001-006)(2012-2013)/Guarding the Globe 003 (2012) (Digital) (Zone-Empire).cbr

### b.p.r.d. hell on earth, abyss of time  *(issue)*

- `   32 MB`  Hellboy/142.)  B.P.R.D. - Hell on Earth #103-104, The Abyss of Time, Parts 1-2  (2012 AD)/B.P.R.D. - Hell on Earth #103, The Abyss of Time, Part 1.cbr
- `   30 MB`  Hellboy/142.)  B.P.R.D. - Hell on Earth #103-104, The Abyss of Time, Parts 1-2  (2012 AD)/B.P.R.D. - Hell on Earth #104, The Abyss of Time, Part 2.cbr

### legend of oz wicked west — v2 — #008  *(volume)*

- `   57 MB`  The Legend of Oz (2011-2016)/The Wicked West v2 (001-018+)(2012-2014)/Legend of Oz - The Wicked West v2 008 (2013) (c2c) (Darkness-Empire).cbr
- `    5 MB`  The Legend of Oz (2011-2016)/The Wicked West v2 (001-018+)(2012-2014)/Legend of Oz - The Wicked West v2 008 (2013) (A Cover Only) (1920px) (Darkness-Empire).cbr

### x men noir — #004  *(issue)*

- `   30 MB`  GG Studio (Collection) (2010-2012)/Marvel Noir (2009-2011)(digital)/X-Men Noir (001-004+)(2009)(digital)(Salem-Empire)/X-Men Noir 004 (2009) (digital) (Salem-Empire).cbr
- `   30 MB`  Aster Blistok/Le Vagabond des Limbes/X-Men Noir (001-004+)(2009)(digital)(Salem-Empire)/X-Men Noir 004 (2009) (digital) (Salem-Empire).cbr
- `    1 MB`  GG Studio (Collection) (2010-2012)/Marvel Noir (2009-2011)(digital)/X-Men Noir (001-004+)(2009)(digital)(Salem-Empire)/covers/X-Men Noir 004 (2009) (Variant Cover Only) [extracted] (The Scangstas-DCP).cbr
- `    1 MB`  Aster Blistok/Le Vagabond des Limbes/X-Men Noir (001-004+)(2009)(digital)(Salem-Empire)/covers/X-Men Noir 004 (2009) (Variant Cover Only) [extracted] (The Scangstas-DCP).cbr

### spider man noir — #04  *(issue)*

- `   30 MB`  GG Studio (Collection) (2010-2012)/Marvel Noir (2009-2011)(digital)/Spider-Man Noir (v1-v2+)(2009-2010)(digital)/Spider-Man Noir v1 (001-004)(2009)(digital)(Minutemen-Faessla)/Spider-Man Noir 04 (of 04) (2009) (digital) (Minutemen-Faessla).cbz
- `   30 MB`  Aster Blistok/Le Vagabond des Limbes/Spider-Man Noir (v1-v2+)(2009-2010)(digital)/Spider-Man Noir v1 (001-004)(2009)(digital)(Minutemen-Faessla)/Spider-Man Noir 04 (of 04) (2009) (digital) (Minutemen-Faessla).cbz
- `    0 MB`  GG Studio (Collection) (2010-2012)/Marvel Noir (2009-2011)(digital)/Spider-Man Noir (v1-v2+)(2009-2010)(digital)/Variant Covers/Spider-Man Noir 04 (2009) (Variant Cover Only) [extracted] (Archangel-DCP).cbr
- `    0 MB`  Aster Blistok/Le Vagabond des Limbes/Spider-Man Noir (v1-v2+)(2009-2010)(digital)/Variant Covers/Spider-Man Noir 04 (2009) (Variant Cover Only) [extracted] (Archangel-DCP).cbr

### punisher noir — #02  *(issue)*

- `   29 MB`  GG Studio (Collection) (2010-2012)/Marvel Noir (2009-2011)(digital)/Punisher Noir (001-004+)(2009-2010)(digital)(Minutemen-Slayer)/Punisher Noir 02 (of 04) (2009) (digital) (Minutemen-Slayer).cbr
- `   29 MB`  Aster Blistok/Le Vagabond des Limbes/Punisher Noir (001-004+)(2009-2010)(digital)(Minutemen-Slayer)/Punisher Noir 02 (of 04) (2009) (digital) (Minutemen-Slayer).cbr
- `    1 MB`  GG Studio (Collection) (2010-2012)/Marvel Noir (2009-2011)(digital)/Punisher Noir (001-004+)(2009-2010)(digital)(Minutemen-Slayer)/covers/Punisher Noir 02 (2009) (Variant Cover Only) [extracted] (Minutemen-DeliriousKing).cbr
- `    1 MB`  Aster Blistok/Le Vagabond des Limbes/Punisher Noir (001-004+)(2009-2010)(digital)(Minutemen-Slayer)/covers/Punisher Noir 02 (2009) (Variant Cover Only) [extracted] (Minutemen-DeliriousKing).cbr

### deathco — v1  *(volume)*

- `   11 MB`  Manga/Deathco manga/Deathco - v1 c1 [batoto].cbz
- `   10 MB`  Manga/Deathco manga/Deathco - v1 c6 [batoto].cbz
- `   10 MB`  Manga/Deathco manga/Deathco - v1 c4 [batoto].cbz
- `   10 MB`  Manga/Deathco manga/Deathco - v1 c5 [batoto].cbz
- `   10 MB`  Manga/Deathco manga/Deathco - v1 c3 [batoto].cbz
- `    9 MB`  Manga/Deathco manga/Deathco - v1 c2 [batoto].cbz

### spider man noir — #03  *(issue)*

- `   29 MB`  GG Studio (Collection) (2010-2012)/Marvel Noir (2009-2011)(digital)/Spider-Man Noir (v1-v2+)(2009-2010)(digital)/Spider-Man Noir v1 (001-004)(2009)(digital)(Minutemen-Faessla)/Spider-Man Noir 03 (of 04) (2009) (digital) (Minutemen-Faessla).cbz
- `   29 MB`  Aster Blistok/Le Vagabond des Limbes/Spider-Man Noir (v1-v2+)(2009-2010)(digital)/Spider-Man Noir v1 (001-004)(2009)(digital)(Minutemen-Faessla)/Spider-Man Noir 03 (of 04) (2009) (digital) (Minutemen-Faessla).cbz
- `    1 MB`  GG Studio (Collection) (2010-2012)/Marvel Noir (2009-2011)(digital)/Spider-Man Noir (v1-v2+)(2009-2010)(digital)/Variant Covers/Spider-Man Noir 03 (2009) (Variant Cover Only) [extracted] (Archangel-DCP).cbr
- `    1 MB`  Aster Blistok/Le Vagabond des Limbes/Spider-Man Noir (v1-v2+)(2009-2010)(digital)/Variant Covers/Spider-Man Noir 03 (2009) (Variant Cover Only) [extracted] (Archangel-DCP).cbr

### spider man noir — #02  *(issue)*

- `   29 MB`  GG Studio (Collection) (2010-2012)/Marvel Noir (2009-2011)(digital)/Spider-Man Noir (v1-v2+)(2009-2010)(digital)/Spider-Man Noir v1 (001-004)(2009)(digital)(Minutemen-Faessla)/Spider-Man Noir 02 (of 04) (2009) (digital) (Minutemen-Faessla).cbz
- `   29 MB`  Aster Blistok/Le Vagabond des Limbes/Spider-Man Noir (v1-v2+)(2009-2010)(digital)/Spider-Man Noir v1 (001-004)(2009)(digital)(Minutemen-Faessla)/Spider-Man Noir 02 (of 04) (2009) (digital) (Minutemen-Faessla).cbz
- `    0 MB`  GG Studio (Collection) (2010-2012)/Marvel Noir (2009-2011)(digital)/Spider-Man Noir (v1-v2+)(2009-2010)(digital)/Variant Covers/Spider-Man Noir 02 (2009) (Variant Cover Only) [extracted] (Archangel-DCP).cbr
- `    0 MB`  Aster Blistok/Le Vagabond des Limbes/Spider-Man Noir (v1-v2+)(2009-2010)(digital)/Variant Covers/Spider-Man Noir 02 (2009) (Variant Cover Only) [extracted] (Archangel-DCP).cbr

### dalgoda — v2  *(volume)*

- `   15 MB`  Dalgoda/Dalgoda v2 Flesh and Bones 01-04/Dalgoda v2 Flesh and Bones 03.cbz
- `   15 MB`  Dalgoda/Dalgoda v2 Flesh and Bones 01-04/Dalgoda v2 Flesh and Bones 02.cbz
- `   15 MB`  Dalgoda/Dalgoda v2 Flesh and Bones 01-04/Dalgoda v2 Flesh and Bones 04.cbz
- `   14 MB`  Dalgoda/Dalgoda v2 Flesh and Bones 01-04/Dalgoda v2 Flesh and Bones 01.cbz

### spirou & fantasio — #41  *(issue)*

- `   33 MB`  Spirou & Fantasio/Spirou & Fantasio 41 (04) - Valley of the Exiles (1989, 2013) (Digital-1200) (Lynx-Empire).cbr
- `   25 MB`  Spirou & Fantasio/Spirou & Fantasio 41 - The Valley of the Banished.cbr

### amazing spider man — v2 — #654  *(volume)*

- `   32 MB`  Alias  ( Jessica Jones , The Pulse & Appearances)/Appearances/Amazing Spider-man/Amazing Spider-Man v2 654 (2011) (Minutemen-Megatonic).cbz
- `   24 MB`  Alias  ( Jessica Jones , The Pulse & Appearances)/Appearances/Amazing Spider-man/Amazing Spider-Man v2 654 1 (2011) (Minutemen-Megatonic).cbz
- `    1 MB`  Alias  ( Jessica Jones , The Pulse & Appearances)/Appearances/Amazing Spider-man/Amazing Spider-Man v2 654 (2011) (2nd Printing Variant) (Cover ONLY) (ScanDog).cbr

### guarding globe — #002  *(issue)*

- `   33 MB`  Image comics/Guarding the Globe v1 (001-006)(2010-2011)/Guarding the Globe 002 (2010) (Digital) (Salem-Empire).cbr
- `   23 MB`  Image comics/Guarding the Globe v2 (001-006)(2012-2013)/Guarding the Globe 002 (2012) (Digital) (Zone-Empire).cbr

### glory — #000  *(issue)*

- `   32 MB`  Alan Moore/Alan Moore Collection III-  Image - Awesome Comics/Glory/Glory Volume 3/Glory #000.cbr
- `   24 MB`  Alan Moore/Alan Moore Collection III-  Image - Awesome Comics/Glory/Glory Volume 2/Glory #000.cbr

### ted mckeever's metropol — v2  *(volume)*

- `   19 MB`  Ted McKeever (Collection) (1987-2007)/1992 - Metropol A.D. (Epic)/Ted McKeever's Metropol v2 A.D. #01 (1992).cbr
- `   19 MB`  Ted McKeever (Collection) (1987-2007)/1992 - Metropol A.D. (Epic)/Ted McKeever's Metropol v2 A.D. #02 (1992).cbr
- `   18 MB`  Ted McKeever (Collection) (1987-2007)/1992 - Metropol A.D. (Epic)/Ted McKeever's Metropol v2 A.D. #03 (1992).cbr

### x men noir — #002  *(issue)*

- `   28 MB`  GG Studio (Collection) (2010-2012)/Marvel Noir (2009-2011)(digital)/X-Men Noir (001-004+)(2009)(digital)(Salem-Empire)/X-Men Noir 002 (2009) (digital) (Salem-Empire).cbr
- `   28 MB`  Aster Blistok/Le Vagabond des Limbes/X-Men Noir (001-004+)(2009)(digital)(Salem-Empire)/X-Men Noir 002 (2009) (digital) (Salem-Empire).cbr
- `    0 MB`  GG Studio (Collection) (2010-2012)/Marvel Noir (2009-2011)(digital)/X-Men Noir (001-004+)(2009)(digital)(Salem-Empire)/covers/X-Men Noir 002 (2009) (Variant Cover Only) [extracted] (Archangel-DCP).cbr
- `    0 MB`  Aster Blistok/Le Vagabond des Limbes/X-Men Noir (001-004+)(2009)(digital)(Salem-Empire)/covers/X-Men Noir 002 (2009) (Variant Cover Only) [extracted] (Archangel-DCP).cbr

### wolverine noir — #001  *(issue)*

- `   27 MB`  GG Studio (Collection) (2010-2012)/Marvel Noir (2009-2011)(digital)/Wolverine Noir (001-004+)(2009)(digital)(Minutemen-Faessla)/Wolverine Noir 001 (2009) (digital) (Minutemen-Faessla).cbz
- `   27 MB`  Aster Blistok/Le Vagabond des Limbes/Wolverine Noir (001-004+)(2009)(digital)(Minutemen-Faessla)/Wolverine Noir 001 (2009) (digital) (Minutemen-Faessla).cbz
- `    1 MB`  GG Studio (Collection) (2010-2012)/Marvel Noir (2009-2011)(digital)/Wolverine Noir (001-004+)(2009)(digital)(Minutemen-Faessla)/covers/Wolverine Noir 001 (2009) (Variant Cover Only) [extracted] (Minutemen Roc'nRosie).cbr
- `    1 MB`  Aster Blistok/Le Vagabond des Limbes/Wolverine Noir (001-004+)(2009)(digital)(Minutemen-Faessla)/covers/Wolverine Noir 001 (2009) (Variant Cover Only) [extracted] (Minutemen Roc'nRosie).cbr

### wolverine noir — #002  *(issue)*

- `   27 MB`  GG Studio (Collection) (2010-2012)/Marvel Noir (2009-2011)(digital)/Wolverine Noir (001-004+)(2009)(digital)(Minutemen-Faessla)/Wolverine Noir 002 (2009) (digital) (Minutemen-Faessla).cbz
- `   27 MB`  Aster Blistok/Le Vagabond des Limbes/Wolverine Noir (001-004+)(2009)(digital)(Minutemen-Faessla)/Wolverine Noir 002 (2009) (digital) (Minutemen-Faessla).cbz
- `    1 MB`  GG Studio (Collection) (2010-2012)/Marvel Noir (2009-2011)(digital)/Wolverine Noir (001-004+)(2009)(digital)(Minutemen-Faessla)/covers/Wolverine Noir 002 (2009) (Variant Cover Only) [extracted] (MinuteMen-Delirium-Powers).cbr
- `    1 MB`  Aster Blistok/Le Vagabond des Limbes/Wolverine Noir (001-004+)(2009)(digital)(Minutemen-Faessla)/covers/Wolverine Noir 002 (2009) (Variant Cover Only) [extracted] (MinuteMen-Delirium-Powers).cbr

### hero worship — #006  *(issue)*

- `   47 MB`  Hero Worship (001-006+)(2012)(digital+) (Minutemen-Excelsior+)/Hero Worship 006 (2012) (c2c) (1920) (Archangel+Darkness-Empire).cbr
- `    7 MB`  Hero Worship (001-006+)(2012)(digital+) (Minutemen-Excelsior+)/covers/Hero Worship 006 (2012) (3 covers only) (digital) (Son of Ultron-Empire).cbr

### tangi i laverdir — #01  *(issue)*

- `   29 MB`  YU stripovi 2019/Tangi i Laverdir/Tangi i Laverdir - 01 - Skola za orlove (scansl) (Zinci&harlequin&duca-BDS-DCP).cbr
- `   26 MB`  YU stripovi 2019/Tangi i Laverdir/Tangi i Laverdir - 01 - Brzi od zvuka (iz Panorame).cbr

### boys  2012   minutemen dts  *(issue)*

- `   28 MB`  Garth Ennis Collection/The Boys/The Boys/The Boys 63--2012---Minutemen-DTs-.cbz
- `   26 MB`  Garth Ennis Collection/The Boys/The Boys/The Boys 64--2012---Minutemen-DTs-.cbz

### x men noir — #003  *(issue)*

- `   26 MB`  GG Studio (Collection) (2010-2012)/Marvel Noir (2009-2011)(digital)/X-Men Noir (001-004+)(2009)(digital)(Salem-Empire)/X-Men Noir 003 (2009) (digital) (Salem-Empire).cbr
- `   26 MB`  Aster Blistok/Le Vagabond des Limbes/X-Men Noir (001-004+)(2009)(digital)(Salem-Empire)/X-Men Noir 003 (2009) (digital) (Salem-Empire).cbr
- `    0 MB`  GG Studio (Collection) (2010-2012)/Marvel Noir (2009-2011)(digital)/X-Men Noir (001-004+)(2009)(digital)(Salem-Empire)/covers/X-Men Noir 003 (2009) (Variant Cover Only) [extracted] (Archangel-DCP).cbr
- `    0 MB`  Aster Blistok/Le Vagabond des Limbes/X-Men Noir (001-004+)(2009)(digital)(Salem-Empire)/covers/X-Men Noir 003 (2009) (Variant Cover Only) [extracted] (Archangel-DCP).cbr

### x men noir mark of cain — #01  *(issue)*

- `   26 MB`  GG Studio (Collection) (2010-2012)/Marvel Noir (2009-2011)(digital)/X-Men Noir - Mark of Cain (001-004+)(2010)(digital)(Minutemen-Faessla)/X-Men Noir - Mark of Cain 01 (of 04) (2010) (digital) (Minutemen-Faessla).cbz
- `   26 MB`  Aster Blistok/Le Vagabond des Limbes/X-Men Noir - Mark of Cain (001-004+)(2010)(digital)(Minutemen-Faessla)/X-Men Noir - Mark of Cain 01 (of 04) (2010) (digital) (Minutemen-Faessla).cbz
- `    1 MB`  GG Studio (Collection) (2010-2012)/Marvel Noir (2009-2011)(digital)/X-Men Noir - Mark of Cain (001-004+)(2010)(digital)(Minutemen-Faessla)/covers/X-Men Noir - Mark of Cain 01 (2010) (Variant Cover Only) [extracted] (Minutemen-DTs).cbr
- `    1 MB`  Aster Blistok/Le Vagabond des Limbes/X-Men Noir - Mark of Cain (001-004+)(2010)(digital)(Minutemen-Faessla)/covers/X-Men Noir - Mark of Cain 01 (2010) (Variant Cover Only) [extracted] (Minutemen-DTs).cbr

### black widow — #02  *(issue)*

- `   27 MB`  Black Widow/Black Widow 1 v2 - Breakdown [2001]/Black Widow 02 (of 03) (2001) (digital) (Minutemen-PhD).cbr
- `   25 MB`  Black Widow/Black Widow 1 v7 (001 - 008) (2010)/Black Widow 02 (2010) (Digital) (G85-Empire).cbr

### anna mercury — #002  *(issue)*

- `   26 MB`  Warren Ellis/2008/2008 Anna Mercury/Vol 2/Anna Mercury 2 002 (2009) (four covers) (Minutemen-DTs).cbz
- `   22 MB`  Warren Ellis/2008/2008 Anna Mercury/Vol 1 [Complete]/Anna Mercury 002 (All Five Covers) (2008) (The Ramones-DCP).cbr
- `    2 MB`  Warren Ellis/2008/2008 Anna Mercury/Vol 1 [Complete]/Anna Mercury 002 Auxiliary (Cover Only) (2008) (The Ramones-DCP).cbr
- `    2 MB`  Warren Ellis/2008/2008 Anna Mercury/Vol 1 [Complete]/Anna Mercury 002 (WWC Variant Cover) (2008) (Steam-DCP).cbr
- `    1 MB`  Warren Ellis/2008/2008 Anna Mercury/Vol 2/Anna Mercury 2 002 (Auxiliary Cover Only) (2009) (Steam-DCP).cbr

### legend of oz wicked west — v2 — #007  *(volume)*

- `   51 MB`  The Legend of Oz (2011-2016)/The Wicked West v2 (001-018+)(2012-2014)/Legend of Oz - The Wicked West v2 007 (2013) (1920px) (Darkness-Empire).cbr
- `    2 MB`  The Legend of Oz (2011-2016)/The Wicked West v2 (001-018+)(2012-2014)/Legend of Oz - The Wicked West v2 007 (2013) (A Cover Only) [extracted] (TaruNet-Novus-HD).cbr

### velocity — #01  *(issue)*

- `   20 MB`  Velocity (v1-v2+)(1995-2016)/Velocity v2 (001-004+)(2010-2011)(digital)(K6-Empire)/Velocity 01 (2010) (Cover B) (c2c) (OllietheOx&Archangel).cbr
- `   19 MB`  Velocity (v1-v2+)(1995-2016)/Velocity v2 (001-004+)(2010-2011)(digital)(K6-Empire)/Velocity 01 (of 04) (2010) (Digital) (K6-Empire).cbr
- `   13 MB`  Velocity (v1-v2+)(1995-2016)/Velocity v1 (001-003)(1995)/Velocity 01 (1995).cbr

### hellboy in hell, hounds of pluto  *(issue)*

- `   26 MB`  Hellboy/166.)  Hellboy in Hell #7-8, The Hounds of Pluto, Parts 1-2  (2014 AD)/Hellboy in Hell #8, The Hounds of Pluto, Part 2.cbr
- `   26 MB`  Hellboy/166.)  Hellboy in Hell #7-8, The Hounds of Pluto, Parts 1-2  (2014 AD)/Hellboy in Hell #7, The Hounds of Pluto, Part 1.cbr

### zipang — v10  *(volume)*

- `   11 MB`  Manga/Zipang/Zipang - v10 c107 [batoto - LOLScans].cbz
- `   11 MB`  Manga/Zipang/Zipang - v10 c105 [batoto - LOLScans].cbz
- `   11 MB`  Manga/Zipang/Zipang - v10 c106 [batoto - LOLScans].cbz
- `    9 MB`  Manga/Zipang/Zipang - v10 c102 [batoto - LOLScans].cbz
- `    7 MB`  Manga/Zipang/Zipang - v10 c104 [batoto - LOLScans].cbz
- `    3 MB`  Manga/Zipang/Zipang - v10 c103 [batoto - LOLScans].cbz

### x men noir — #001  *(issue)*

- `   25 MB`  GG Studio (Collection) (2010-2012)/Marvel Noir (2009-2011)(digital)/X-Men Noir (001-004+)(2009)(digital)(Salem-Empire)/X-Men Noir 001 (2009) (digital) (Salem-Empire).cbr
- `   25 MB`  Aster Blistok/Le Vagabond des Limbes/X-Men Noir (001-004+)(2009)(digital)(Salem-Empire)/X-Men Noir 001 (2009) (digital) (Salem-Empire).cbr
- `    0 MB`  GG Studio (Collection) (2010-2012)/Marvel Noir (2009-2011)(digital)/X-Men Noir (001-004+)(2009)(digital)(Salem-Empire)/covers/X-Men Noir 001 (2009) (Variant Cover Only) [extracted] (Steam-DCP).cbr
- `    0 MB`  Aster Blistok/Le Vagabond des Limbes/X-Men Noir (001-004+)(2009)(digital)(Salem-Empire)/covers/X-Men Noir 001 (2009) (Variant Cover Only) [extracted] (Steam-DCP).cbr

### 0834 0841 purgatory  *(issue)*

- `   32 MB`  Judge Dredd - Collections/Judge Dredd Collected from 2000AD progs 0001 - 1829 (1977 - 2013) (complete) (Inc  Specials & Annuals 1977 - 1999)/0834-0841 Purgatory [Reprint Meg  332].cbr
- `   18 MB`  Judge Dredd - Collections/Judge Dredd Collected from 2000AD progs 0001 - 1829 (1977 - 2013) (complete) (Inc  Specials & Annuals 1977 - 1999)/0834-0841 Purgatory (ft  Judge Grice).cbr

### spirit — #013  *(issue)*

- `   40 MB`  Will Eisner/Spirit (1950s)/Spirit_013__Quality_1948_Autumn_52p_c2c___Snardermann_.cbz
- `   10 MB`  Will Eisner/The Spirit 001-087 (1983-1992)/The Spirit 013 (1985) (Kitchen Sink) (c2c).cbr

### x men noir mark of cain — #03  *(issue)*

- `   24 MB`  GG Studio (Collection) (2010-2012)/Marvel Noir (2009-2011)(digital)/X-Men Noir - Mark of Cain (001-004+)(2010)(digital)(Minutemen-Faessla)/X-Men Noir - Mark of Cain 03 (of 04) (2010) (digital) (Minutemen-Faessla).cbz
- `   24 MB`  Aster Blistok/Le Vagabond des Limbes/X-Men Noir - Mark of Cain (001-004+)(2010)(digital)(Minutemen-Faessla)/X-Men Noir - Mark of Cain 03 (of 04) (2010) (digital) (Minutemen-Faessla).cbz
- `    1 MB`  GG Studio (Collection) (2010-2012)/Marvel Noir (2009-2011)(digital)/X-Men Noir - Mark of Cain (001-004+)(2010)(digital)(Minutemen-Faessla)/covers/X-Men Noir - Mark of Cain 03 (2010) (Variant Cover Only) [extracted] (Minutemen-DTs).cbr
- `    1 MB`  Aster Blistok/Le Vagabond des Limbes/X-Men Noir - Mark of Cain (001-004+)(2010)(digital)(Minutemen-Faessla)/covers/X-Men Noir - Mark of Cain 03 (2010) (Variant Cover Only) [extracted] (Minutemen-DTs).cbr

### x men noir mark of cain — #04  *(issue)*

- `   24 MB`  GG Studio (Collection) (2010-2012)/Marvel Noir (2009-2011)(digital)/X-Men Noir - Mark of Cain (001-004+)(2010)(digital)(Minutemen-Faessla)/X-Men Noir - Mark of Cain 04 (of 04) (2010) (digital) (Minutemen-Faessla).cbz
- `   24 MB`  Aster Blistok/Le Vagabond des Limbes/X-Men Noir - Mark of Cain (001-004+)(2010)(digital)(Minutemen-Faessla)/X-Men Noir - Mark of Cain 04 (of 04) (2010) (digital) (Minutemen-Faessla).cbz
- `    0 MB`  GG Studio (Collection) (2010-2012)/Marvel Noir (2009-2011)(digital)/X-Men Noir - Mark of Cain (001-004+)(2010)(digital)(Minutemen-Faessla)/covers/X-Men Noir - Mark of Cain 04 (2010) (Variant Cover Only) [extracted] (Minutemen-DTs).cbr
- `    0 MB`  Aster Blistok/Le Vagabond des Limbes/X-Men Noir - Mark of Cain (001-004+)(2010)(digital)(Minutemen-Faessla)/covers/X-Men Noir - Mark of Cain 04 (2010) (Variant Cover Only) [extracted] (Minutemen-DTs).cbr

### b.p.r.d. hell on earth, a cold day in hell  *(issue)*

- `   25 MB`  Hellboy/145.)  B.P.R.D. - Hell on Earth #105-106, A Cold Day in Hell, Parts 1-2  (2012 AD)/B.P.R.D. - Hell on Earth #106, A Cold Day in Hell, Part 2.cbr
- `   24 MB`  Hellboy/145.)  B.P.R.D. - Hell on Earth #105-106, A Cold Day in Hell, Parts 1-2  (2012 AD)/B.P.R.D. - Hell on Earth #105, A Cold Day in Hell, Part 1.cbr

### new avengers — #001  *(issue)*

- `   42 MB`  Alias  ( Jessica Jones , The Pulse & Appearances)/Appearances/New Avengers (2010)/New Avengers 001 (5 covers) (c2c) (2010) (Minutemen-Danger&Darth).cbr
- `    4 MB`  Alias  ( Jessica Jones , The Pulse & Appearances)/Appearances/New Avengers (2010)/New Avengers 001 (2010) (Immonen Gatefold Variant) (Cover ONLY) (ScanDog & ArtNet-DCP).cbz
- `    1 MB`  Alias  ( Jessica Jones , The Pulse & Appearances)/Appearances/New Avengers (2010)/New Avengers 001 (2010) (2nd Printing Variant) (Cover ONLY) (ScanDog).cbr
- `    1 MB`  Alias  ( Jessica Jones , The Pulse & Appearances)/Appearances/New Avengers (2010)/New Avengers 001 (2010) (Ron Chan Hero Initiative Variant) (Minutemen-PETA).cbr

### anna mercury — #003  *(issue)*

- `   24 MB`  Warren Ellis/2008/2008 Anna Mercury/Vol 2/Anna Mercury 2 003 (2009) (three covers) (fixed) (Minutemen-DTs).cbz
- `   19 MB`  Warren Ellis/2008/2008 Anna Mercury/Vol 1 [Complete]/Anna Mercury 003 (All Four Covers) (2008) (The Ramones-DCP).cbr
- `    3 MB`  Warren Ellis/2008/2008 Anna Mercury/Vol 1 [Complete]/Anna Mercury 003 (Auxiliary Cover) (2008) (Minutemen-Special).cbr
- `    2 MB`  Warren Ellis/2008/2008 Anna Mercury/Vol 1 [Complete]/Anna Mercury 003 (Design Sketch Variant) (2008) (Minutemen-Special).cbr

### spirit — #002  *(issue)*

- `   32 MB`  Will Eisner/Spirit (1950s)/Spirit_002_Jon_HP.cbz
- `   16 MB`  Will Eisner/The Spirit 001-087 (1983-1992)/The Spirit 002 (1983) (Kitchen Sink) (c2c).cbz

### abe sapien, sacred places  *(issue)*

- `   25 MB`  Hellboy/156.)  Abe Sapien #16-17, Sacred Places, Parts 1-2  (2012 AD)/Abe Sapien #16, Sacred Places, Part 1.cbr
- `   23 MB`  Hellboy/156.)  Abe Sapien #16-17, Sacred Places, Parts 1-2  (2012 AD)/Abe Sapien #17, Sacred Places, Part 2.cbr

### tank girl — v1  *(volume)*

- `   13 MB`  Tank Girl/01. Tank Girl - Volume 1/Tank Girl Vol. 1 - 1 of 4 (Dark Horse, 1991).cbr
- `   13 MB`  Tank Girl/01. Tank Girl - Volume 1/Tank Girl Vol. 1 - 2 of 4 - The Australian Job pt. 1 (Dark Horse, 1991).cbr
- `   12 MB`  Tank Girl/01. Tank Girl - Volume 1/Tank Girl Vol. 1 - 3 of 4 - The Australian Job pt. 2 (Dark Horse, 1991).cbr
- `   10 MB`  Tank Girl/01. Tank Girl - Volume 1/Tank Girl Vol. 1 - 4 of 4 - The Preposterous Bollox of the Situation (Dark Horse, 1991).cbr

### b.p.r.d. hell on earth, broken equation  *(issue)*

- `   24 MB`  Hellboy/161.)  B.P.R.D. - Hell on Earth #122-123, The Broken Equation, Parts 1-2  (2013 AD)/B.P.R.D. - Hell on Earth #122, The Broken Equation, Part 1.cbr
- `   22 MB`  Hellboy/161.)  B.P.R.D. - Hell on Earth #122-123, The Broken Equation, Parts 1-2  (2013 AD)/B.P.R.D. - Hell on Earth #123, The Broken Equation, Part 2.cbr

### boku tachi ga yarimashita — v3  *(volume)*

- `    6 MB`  Manga/Bokutachi_ga_Yarimashita/Boku-tachi ga Yarimashita - v3 c26 [batoto - Nuwang].cbz
- `    6 MB`  Manga/Bokutachi_ga_Yarimashita/Boku-tachi ga Yarimashita - v3 c19 [batoto - Nuwang].cbz
- `    5 MB`  Manga/Bokutachi_ga_Yarimashita/Boku-tachi ga Yarimashita - v3 c23 [batoto - Nuwang].cbz
- `    5 MB`  Manga/Bokutachi_ga_Yarimashita/Boku-tachi ga Yarimashita - v3 c21 [batoto - Nuwang].cbz
- `    5 MB`  Manga/Bokutachi_ga_Yarimashita/Boku-tachi ga Yarimashita - v3 c20 [batoto - Nuwang].cbz
- `    5 MB`  Manga/Bokutachi_ga_Yarimashita/Boku-tachi ga Yarimashita - v3 c25 [batoto - Nuwang].cbz
- `    5 MB`  Manga/Bokutachi_ga_Yarimashita/Boku-tachi ga Yarimashita - v3 c22 [batoto - Nuwang].cbz
- `    5 MB`  Manga/Bokutachi_ga_Yarimashita/Boku-tachi ga Yarimashita - v3 c18 [batoto - Nuwang].cbz
- `    4 MB`  Manga/Bokutachi_ga_Yarimashita/Boku-tachi ga Yarimashita - v3 c24 [batoto - Nuwang].cbz

### 2000 ad sci fi  *(special)*

- `   26 MB`  Alan Moore/Alan Moore Collection I- English Invasion/Alan Moore Collection III- 2000 AD/2000 AD/2000 AD- Individual Issues/2000 AD- Sci-Fi Special/2000 AD Sci-Fi Special 1981 (Southern Comfort (Credited To R.E. Wright Because Moore Didn't Like The Re-Write).cbr
- `   19 MB`  Alan Moore/Alan Moore Collection I- English Invasion/Alan Moore Collection III- 2000 AD/2000 AD/2000 AD- Individual Issues/2000 AD- Sci-Fi Special/2000 AD Sci-Fi Special 1980 (Tharg's Future-Shocks - A Holiday In Hell).cbr

### new avengers — #016  *(issue)*

- `   23 MB`  Alias  ( Jessica Jones , The Pulse & Appearances)/Appearances/New Avengers (2010)/New Avengers 016 1 (2011) (Minutemen-Shepherd&Saxon).cbr
- `   22 MB`  Alias  ( Jessica Jones , The Pulse & Appearances)/Appearances/New Avengers (2010)/New Avengers 016 (2011) (three covers) (Minutemen-Shepherd&Saxon).cbr

### x men noir mark of cain — #02  *(issue)*

- `   22 MB`  GG Studio (Collection) (2010-2012)/Marvel Noir (2009-2011)(digital)/X-Men Noir - Mark of Cain (001-004+)(2010)(digital)(Minutemen-Faessla)/X-Men Noir - Mark of Cain 02 (of 04) (2010) (digital) (Minutemen-Faessla).cbz
- `   22 MB`  Aster Blistok/Le Vagabond des Limbes/X-Men Noir - Mark of Cain (001-004+)(2010)(digital)(Minutemen-Faessla)/X-Men Noir - Mark of Cain 02 (of 04) (2010) (digital) (Minutemen-Faessla).cbz
- `    1 MB`  GG Studio (Collection) (2010-2012)/Marvel Noir (2009-2011)(digital)/X-Men Noir - Mark of Cain (001-004+)(2010)(digital)(Minutemen-Faessla)/covers/X-Men Noir - Mark of Cain 02 (2010) (Variant Cover Only) [extracted] (Minutemen-DTs).cbr
- `    1 MB`  Aster Blistok/Le Vagabond des Limbes/X-Men Noir - Mark of Cain (001-004+)(2010)(digital)(Minutemen-Faessla)/covers/X-Men Noir - Mark of Cain 02 (2010) (Variant Cover Only) [extracted] (Minutemen-DTs).cbr

### aria — #01  *(issue)*

- `   29 MB`  Aria (Collection) GetComics.INFO/Aria 01 - Aria Takes Off (1986) (StarBlaze).cbr
- `   15 MB`  Aria (Collection) GetComics.INFO/Aria (Image)(Avalon)/Aria #01.cbr

### judge dredd — #03  *(issue)*

- `   28 MB`  Grant Morrison/Comics/2000 AD (Fleetway 1986)/Judge Dredd - 03 Crusade.cbz
- `   15 MB`  Judge Dredd The Megazine/Judge Dredd 001-018 (1994-1996)/Judge Dredd 03.cbr

### final crisis — #01  *(issue)*

- `   27 MB`  Grant Morrison/Comics/Final Crisis (DC 2008)/Final Crisis/Final Crisis 01 (of 07) Director's Cut (2008) (Minutemen-TheBastard).cbr
- `   16 MB`  Grant Morrison/Comics/Final Crisis (DC 2008)/Final Crisis/Final Crisis 01 (of 7) (2008) (RacerX-DCP).cbr

### dead at — #17  *(issue)*

- `   12 MB`  Image comics/Dead@17 Witch Queen (001-004)(2010)/Dead At 17 Witch Queen 2(Image)(2010)(YZ1).cbr
- `   11 MB`  Image comics/Dead@17 Witch Queen (001-004)(2010)/Dead At 17 Witch Queen 3(c2c)(Image)(2010)(YZ1).cbr
- `   10 MB`  Image comics/Dead@17 Witch Queen (001-004)(2010)/Dead At 17 Witch Queen 4(c2c)(Image)(2010)(YZ1).cbr
- `    7 MB`  Image comics/Dead@17 Witch Queen (001-004)(2010)/Dead At 17 Witch Queen 1(Image)(2010)(YZ1).cbr

### escape journey — v2  *(volume)*

- `   20 MB`  Manga/Escape_Journey/Escape Journey - v2 c7 [batoto].cbz
- `   20 MB`  Manga/Escape_Journey/Escape Journey - v2 c8 [batoto].cbz

### spirit — #021  *(issue)*

- `   29 MB`  Will Eisner/Spirit (1950s)/The_Spirit_021__c2c_36p__Ten_Drafts_.cbz
- `   11 MB`  Will Eisner/The Spirit 001-087 (1983-1992)/The Spirit 021 (1986) (Kitchen Sink) (c2c) (Custer Beaton).cbr

### daredevils arrivals  *(issue)*

- `   37 MB`  Alan Moore/Alan Moore Collection I- English Invasion/Alan Moore Collection II- Marvel UK/Captain Britain/Captain Britain (Marvel Comics UK)/The Daredevils/The Daredevils #009- Arrivals.cbz
- `    2 MB`  Alan Moore/Alan Moore Collection I- English Invasion/Alan Moore Collection II- Marvel UK/Captain Britain/Captain Britain (Marvel Comics UK)/The Daredevils/The Daredevils #008- Arrivals.cbr

### spirit — #020  *(issue)*

- `   29 MB`  Will Eisner/Spirit (1950s)/The_Spirit_020__c2c_36p__Snardermann_.cbz
- `   10 MB`  Will Eisner/The Spirit 001-087 (1983-1992)/The Spirit 020 (1986) (Kitchen Sink) (c2c) (Custer Beaton).cbr

### star trek city on edge of forever — #004  *(issue)*

- `   35 MB`  Star Trek/Star Trek - City on the Edge of Forever 01-05 (2014)/Star Trek - City on the Edge of Forever 004 (2014) (Digital) (TLK-EMPIRE-HD).cbr
- `    3 MB`  Star Trek/Star Trek - City on the Edge of Forever 01-05 (2014)/Variant Covers/Star Trek - City on the Edge of Forever 004 (2014) (Variant Cover Only) [extracted] (TLK-EMPIRE-HD).cbr

### spirit — #022  *(issue)*

- `   28 MB`  Will Eisner/Spirit (1950s)/The_Spirit_022__Snardermann_.cbz
- `    9 MB`  Will Eisner/The Spirit 001-087 (1983-1992)/The Spirit 022 (1986) (Kitchen Sink) (c2c) (Custer Beaton).cbr

### spirit — #019  *(issue)*

- `   28 MB`  Will Eisner/Spirit (1950s)/The_Spirit_019__c2c__Snardermann_.cbz
- `   10 MB`  Will Eisner/The Spirit 001-087 (1983-1992)/The Spirit 019 (1986) (Kitchen Sink) (c2c) (Custer Beaton).cbr

### spirit — #015  *(issue)*

- `   27 MB`  Will Eisner/Spirit (1950s)/Spirit_015__Quality_1949_Spring_36p_c2c___Snardermann_.cbz
- `   10 MB`  Will Eisner/The Spirit 001-087 (1983-1992)/The Spirit 015 (1986) (Kitchen Sink) (c2c) (Custer Beaton).cbz

### darkness — #04  *(issue)*

- `   24 MB`  Garth Ennis Collection/The Darkness/The Darkness Volume 3/The Darkness 04 (68).cbr
- `   13 MB`  Garth Ennis Collection/The Darkness/The Darkness Volume 1/the darkness #04.cbr

### spirit — #016  *(issue)*

- `   27 MB`  Will Eisner/Spirit (1950s)/Spirit_016__Quality_1949_July_36p_c2c___Snardermann_.cbz
- `   10 MB`  Will Eisner/The Spirit 001-087 (1983-1992)/The Spirit 016 (1986) (Kitchen Sink) (c2c) (Custer Beaton).cbr

### honey & honey — v2  *(volume)*

- `    5 MB`  Manga/Honey & Honey/Honey & Honey v02 c28.cbz
- `    4 MB`  Manga/Honey & Honey/Honey & Honey v02 c30.cbz
- `    4 MB`  Manga/Honey & Honey/Honey & Honey v02 c18.cbz
- `    3 MB`  Manga/Honey & Honey/Honey & Honey v02 c29.cbz
- `    2 MB`  Manga/Honey & Honey/Honey & Honey v02 c19.cbz
- `    2 MB`  Manga/Honey & Honey/Honey & Honey v02 c34.cbz
- `    2 MB`  Manga/Honey & Honey/Honey & Honey v02 c33.cbz
- `    2 MB`  Manga/Honey & Honey/Honey & Honey v02 c31.cbz
- `    2 MB`  Manga/Honey & Honey/Honey & Honey v02 c21.cbz
- `    2 MB`  Manga/Honey & Honey/Honey & Honey v02 c32.cbz
- `    2 MB`  Manga/Honey & Honey/Honey & Honey v02 c26.cbz
- `    2 MB`  Manga/Honey & Honey/Honey & Honey v02 c24.cbz
- `    1 MB`  Manga/Honey & Honey/Honey & Honey v02 c20.cbz
- `    1 MB`  Manga/Honey & Honey/Honey & Honey v02 c22.cbz
- `    1 MB`  Manga/Honey & Honey/Honey & Honey v02 c25.cbz
- `    1 MB`  Manga/Honey & Honey/Honey & Honey v02 c23.cbz
- `    1 MB`  Manga/Honey & Honey/Honey & Honey v02 c27.cbz

### darkness — #07  *(issue)*

- `   26 MB`  Garth Ennis Collection/The Darkness/The Darkness Volume 3/The Darkness 07 - Issue 71.cbr
- `   10 MB`  Garth Ennis Collection/The Darkness/The Darkness Volume 1/the darkness #07.cbr

### spirit — #018  *(issue)*

- `   28 MB`  Will Eisner/Spirit (1950s)/The_Spirit_018__c2c_36p__Snardermann_.cbz
- `    9 MB`  Will Eisner/The Spirit 001-087 (1983-1992)/The Spirit 018 (1986) (Kitchen Sink) (c2c).cbz

### beastars — v6  *(volume)*

- `   17 MB`  Manga/Beastars manga/Beastars - v6 c47 [batoto].cbz
- `   10 MB`  Manga/Beastars manga/Beastars - v6 c46 [batoto].cbz
- `    9 MB`  Manga/Beastars manga/Beastars - v6 c45 [batoto].cbz

### darkness — #02  *(issue)*

- `   25 MB`  Garth Ennis Collection/The Darkness/The Darkness Volume 3/The Darkness 02 (66).cbr
- `   11 MB`  Garth Ennis Collection/The Darkness/The Darkness Volume 1/the darkness #02.cbr

### manara, milo venus et salome  *(issue)*

- `   19 MB`  Milo Manara/Artwork, covers etc/Manara, Milo - Venus et Salome [FRA].cbz
- `   16 MB`  Milo Manara/Artwork, covers etc/Manara, Milo - Venus et Salome [NED].cbz

### darkness — #03  *(issue)*

- `   22 MB`  Garth Ennis Collection/The Darkness/The Darkness Volume 3/The Darkness 03 (67).cbr
- `   12 MB`  Garth Ennis Collection/The Darkness/The Darkness Volume 1/the darkness #03.cbr

### darkness — #06  *(issue)*

- `   24 MB`  Garth Ennis Collection/The Darkness/The Darkness Volume 3/The Darkness 06 (70).cbr
- `   11 MB`  Garth Ennis Collection/The Darkness/The Darkness Volume 1/the darkness #06.cbr

### hero worship — #001  *(issue)*

- `   26 MB`  Hero Worship (001-006+)(2012)(digital+) (Minutemen-Excelsior+)/Hero Worship 001 (2012) (digital) (Minutemen-Excelsior).cbz
- `    8 MB`  Hero Worship (001-006+)(2012)(digital+) (Minutemen-Excelsior+)/covers/Hero Worship 001 (2012) (3 covers only) (digital) (Son of Ultron-Empire).cbr

### spirit — #005  *(issue)*

- `   21 MB`  Will Eisner/The Spirit 001-087 (1983-1992)/The Spirit 005 (1984) (Kitchen Sink) (c2c).cbr
- `   13 MB`  Will Eisner/Spirit (1950s)/Spirit_005__1953_.cbr

### darkness — #01  *(issue)*

- `   21 MB`  Garth Ennis Collection/The Darkness/The Darkness Volume 3/The Darkness 01 (65).cbr
- `   12 MB`  Garth Ennis Collection/The Darkness/The Darkness Volume 1/the darkness #01.cbr

### darkness — #09  *(issue)*

- `   23 MB`  Garth Ennis Collection/The Darkness/The Darkness Volume 3/The Darkness 09 - Issue 73.cbr
- `   11 MB`  Garth Ennis Collection/The Darkness/The Darkness Volume 1/the darkness #09.cbr

### transmetropolitan  *(special)*

- `   19 MB`  Warren Ellis/1997/Transmetropolitan/Transmetropolitan Specials & Miscellanous Stuff/Transmetropolitan Special - Filth of the City.cbz
- `   14 MB`  Warren Ellis/1997/Transmetropolitan/Transmetropolitan Specials & Miscellanous Stuff/Transmetropolitan Special - I Hate It Here.cbr

### escape journey c2  *(issue)*

- `   16 MB`  Manga/Escape_Journey/Escape Journey - c2 - (1).cbz
- `   16 MB`  Manga/Escape_Journey/Escape Journey - c2 [batoto].cbz

### hero worship — #005  *(issue)*

- `   23 MB`  Hero Worship (001-006+)(2012)(digital+) (Minutemen-Excelsior+)/Hero Worship 005 (2012) (digital) (Minutemen-Excelsior).cbz
- `    9 MB`  Hero Worship (001-006+)(2012)(digital+) (Minutemen-Excelsior+)/covers/Hero Worship 005 (2012) (3 covers only) (digital) (Son of Ultron-Empire).cbr

### faithof5  *(issue)*

- `    7 MB`  Ted McKeever (Collection) (1987-2007)/1999 - Faith (Vertigo)/Faith 4of5.cbr
- `    6 MB`  Ted McKeever (Collection) (1987-2007)/1999 - Faith (Vertigo)/Faith 5of5.cbr
- `    6 MB`  Ted McKeever (Collection) (1987-2007)/1999 - Faith (Vertigo)/Faith 1of5.cbr
- `    6 MB`  Ted McKeever (Collection) (1987-2007)/1999 - Faith (Vertigo)/Faith 3of5.cbr
- `    6 MB`  Ted McKeever (Collection) (1987-2007)/1999 - Faith (Vertigo)/Faith 2of5.cbr

### darkness — #10  *(issue)*

- `   17 MB`  Garth Ennis Collection/The Darkness/The Darkness Volume 3/The Darkness 10 - Issue 74.cbr
- `   13 MB`  Garth Ennis Collection/The Darkness/The Darkness Volume 1/the darkness #10.cbr

### penny for your soul false prophet — #01  *(issue)*

- `   30 MB`  Penny For Your Soul (v1-v3+)(2010-2014)/Penny for Your Soul (v1-v3)(2010-2013)/03 Penny for Your Soul v2 - False Prophet (001-007)(2011-2012)/Penny for Your Soul - False Prophet 01 (of 07) (2011) (c2c) (MH-DCP).cbr
- `    1 MB`  Penny For Your Soul (v1-v3+)(2010-2014)/Penny for Your Soul (v1-v3)(2010-2013)/03 Penny for Your Soul v2 - False Prophet (001-007)(2011-2012)/Penny for Your Soul - False Prophet 01 (3 variant covers ONLY).cbz

### velocity — #02  *(issue)*

- `   17 MB`  Velocity (v1-v2+)(1995-2016)/Velocity v2 (001-004+)(2010-2011)(digital)(K6-Empire)/Velocity 02 (of 04) (2010) (Digital) (K6-Empire).cbr
- `   13 MB`  Velocity (v1-v2+)(1995-2016)/Velocity v1 (001-003)(1995)/Velocity 02 (1995) (Birdbrain).cbr

### black summer — #01  *(issue)*

- `   29 MB`  Warren Ellis/2007/2007 Black Summer/Black Summer #01.cbz
- `    1 MB`  Warren Ellis/2007/2007 Black Summer/Black Summer #01 Auxiliary (Cover Only).cbr

### velocity — #03  *(issue)*

- `   17 MB`  Velocity (v1-v2+)(1995-2016)/Velocity v2 (001-004+)(2010-2011)(digital)(K6-Empire)/Velocity 03 (of 04) (2010) (Digital) (K6-Empire).cbr
- `   12 MB`  Velocity (v1-v2+)(1995-2016)/Velocity v1 (001-003)(1995)/Velocity 03 (1995) (Cooper).cbr

### hero worship — #003  *(issue)*

- `   22 MB`  Hero Worship (001-006+)(2012)(digital+) (Minutemen-Excelsior+)/Hero Worship 003 (2012) (digital) (Minutemen-Excelsior).cbz
- `    7 MB`  Hero Worship (001-006+)(2012)(digital+) (Minutemen-Excelsior+)/covers/Hero Worship 003 (2012) (3 covers only) (digital) (Son of Ultron-Empire).cbr

### hero worship — #002  *(issue)*

- `   21 MB`  Hero Worship (001-006+)(2012)(digital+) (Minutemen-Excelsior+)/Hero Worship 002 (2012) (digital) (Minutemen-Excelsior).cbz
- `    8 MB`  Hero Worship (001-006+)(2012)(digital+) (Minutemen-Excelsior+)/covers/Hero Worship 002 (2012) (4 covers only) (digital) (Son of Ultron-Empire).cbr

### hero worship — #004  *(issue)*

- `   23 MB`  Hero Worship (001-006+)(2012)(digital+) (Minutemen-Excelsior+)/Hero Worship 004 (2012) (digital) (Minutemen-Excelsior).cbz
- `    6 MB`  Hero Worship (001-006+)(2012)(digital+) (Minutemen-Excelsior+)/covers/Hero Worship 004 (2012) (3 covers only) (digital) (Son of Ultron-Empire).cbr

### star trek city on edge of forever — #003  *(issue)*

- `   26 MB`  Star Trek/Star Trek - City on the Edge of Forever 01-05 (2014)/Star Trek - City on the Edge of Forever 003 (2014) (Digital) (TLK-EMPIRE-HD).cbr
- `    3 MB`  Star Trek/Star Trek - City on the Edge of Forever 01-05 (2014)/Variant Covers/Star Trek - City on the Edge of Forever 003 (2014) (Variant Cover Only) [extracted] (TLK-EMPIRE-HD).cbr

### judge dredd megazine — v3 — #001  *(volume)*

- `   24 MB`  Judge Dredd The Megazine/Judge Dredd Megazine v3 (001-079)(1995-2001)/Judge Dredd Megazine v3 001 (1995) (bakhos).cbr
- `    4 MB`  Judge Dredd The Megazine/Judge Dredd Megazine v5 (201-400)(2002-ongoing)/J.D Megazine Supplements/Judge Dredd Megazine v3 001 (1995) (Exclusive Film Supplement Only) (1994) (Armitage).cbr

### darkness — #05  *(issue)*

- `   17 MB`  Garth Ennis Collection/The Darkness/The Darkness Volume 3/The Darkness 05 (69).cbr
- `   10 MB`  Garth Ennis Collection/The Darkness/The Darkness Volume 1/the darkness #05.cbr

### courtyard  *(issue)*

- `   21 MB`  Alan Moore/Alan Moore - Lowecraft series/[2003] The Courtyard/[2003] The Courtyard.cbz
- `    6 MB`  Alan Moore/Alan Moore Collection VI- Made For Moore/Alan Moore's The Courtyard/The Courtyard (Alan Moore's The Courtyard Companion).cbr

### batman — #670  *(issue)*

- `   25 MB`  Grant Morrison/Comics/Batman (DC 2006)/Batman 670 (2007) (Minutemen-DTs).cbz
- `    1 MB`  Grant Morrison/Comics/Batman (DC 2006)/Batman 670 (2nd printing cover) (2007) (KingDaubach-DCP).cbr

### nextwave agents of h.a.t.e. — #01  *(issue)*

- `   16 MB`  Warren Ellis/2006/2006 Nextwave/Nextwave - Agents of H.A.T.E. #01 Director's Cut.cbr
- `    9 MB`  Warren Ellis/2006/2006 Nextwave/Nextwave - Agents of H.A.T.E. #01.cbr

### black summer — #05  *(issue)*

- `   22 MB`  Warren Ellis/2007/2007 Black Summer/Black Summer #05 (Regular & Wrap Covers).cbr
- `    2 MB`  Warren Ellis/2007/2007 Black Summer/Black Summer #05 Auxiliary (Cover Only).cbr
- `    1 MB`  Warren Ellis/2007/2007 Black Summer/Black Summer #05 (Sketch Variant Cover).cbr

### star trek infestation — #02  *(issue)*

- `   24 MB`  Star Trek/Star Trek - Infestation (2011)/Star Trek - Infestation 02 (of 2) (2011) (two covers) (Minutemen-DarthTremens).cbz
- `    1 MB`  Star Trek/Star Trek - Infestation (2011)/Variant Covers/Star Trek - Infestation 02 (2011) (RI-A Cover Only) (YZ1).cbr

### star trek city on edge of forever — #002  *(issue)*

- `   22 MB`  Star Trek/Star Trek - City on the Edge of Forever 01-05 (2014)/Star Trek - City on the Edge of Forever 002 (2014) (Digital) (TLK-EMPIRE-HD).cbr
- `    3 MB`  Star Trek/Star Trek - City on the Edge of Forever 01-05 (2014)/Variant Covers/Star Trek - City on the Edge of Forever 002 (2014) (Variant Cover Only) [extracted] (TLK-EMPIRE-HD).cbr

### doktor sleepless — #06  *(issue)*

- `   21 MB`  Warren Ellis/2007/2007 Doktor Sleepless/Doktor Sleepless #06.cbr
- `    3 MB`  Warren Ellis/2007/2007 Doktor Sleepless/Doktor Sleepless #06 (Mad Scientist Cover Only).cbr

### black summer — #04  *(issue)*

- `   23 MB`  Warren Ellis/2007/2007 Black Summer/Black Summer #04 (Regular & Wrap Cover).cbr
- `    1 MB`  Warren Ellis/2007/2007 Black Summer/Black Summer #04 Auxiliary (Cover Only).cbr

### star trek infestation — #01  *(issue)*

- `   23 MB`  Star Trek/Star Trek - Infestation (2011)/Star Trek - Infestation 01 (of 2) (2011) (two covers) (Minutemen-DarthTremens).cbz
- `    1 MB`  Star Trek/Star Trek - Infestation (2011)/Variant Covers/Star Trek - Infestation 01 (2011) ( RI-B Cover Only) (YZ1).cbr
- `    1 MB`  Star Trek/Star Trek - Infestation (2011)/Variant Covers/Star Trek - Infestation 01 (2011) ( RI-A Cover Only) (YZ1).cbr

### new avengers — #012  *(issue)*

- `   22 MB`  Alias  ( Jessica Jones , The Pulse & Appearances)/Appearances/New Avengers (2010)/New Avengers 012 (2011) (two covers) (Minutemen-TwiztidSax).cbr
- `    2 MB`  Alias  ( Jessica Jones , The Pulse & Appearances)/Appearances/New Avengers (2010)/New Avengers 012 (2011) (Khoi Pham X-Men Evolutions Variant) (Minutemen-MegaJackal).cbr

### fantastic four — #1234  *(issue)*

- `    7 MB`  Grant Morrison/Comics/Fantastic Four 1234 (Marvel 2001)/Fantastic Four 1234 #04 - Mr Fantastic.cbr
- `    7 MB`  Grant Morrison/Comics/Fantastic Four 1234 (Marvel 2001)/Fantastic Four 1234 #02 - Invisible Woman.cbz
- `    5 MB`  Grant Morrison/Comics/Fantastic Four 1234 (Marvel 2001)/Fantastic Four 1234 #01 - The Thing.cbz
- `    5 MB`  Grant Morrison/Comics/Fantastic Four 1234 (Marvel 2001)/Fantastic Four 1234 #03 - Human Torch.cbz

### batman and robin — #01  *(issue)*

- `   23 MB`  Grant Morrison/Comics/Batman and Robin (DC 2009)/Batman and Robin 01 (2009) (two covers) (Minutemen-DTs).cbz
- `    1 MB`  Grant Morrison/Comics/Batman and Robin (DC 2009)/Batman and Robin 01 (2009) (2nd printing cover) (GCPD-OCD).cbr

### batman — #676  *(issue)*

- `   20 MB`  Grant Morrison/Comics/Batman (DC 2006)/Batman 676 (2008) (both covers) (Minutemen-ZonesDiva).cbr
- `    2 MB`  Grant Morrison/Comics/Batman (DC 2006)/Batman 676 (2008) (3rd Printing Variant) (Minutemen-RainsDesire).cbr
- `    1 MB`  Grant Morrison/Comics/Batman (DC 2006)/Batman 676 (2008) (2nd Printing Variant) (Minutemen-RainsDesire).cbr

### black summer — #03  *(issue)*

- `   22 MB`  Warren Ellis/2007/2007 Black Summer/Black Summer #03 (Regular & Wrap Cover).cbr
- `    1 MB`  Warren Ellis/2007/2007 Black Summer/Black Summer #03 Auxiliary (Cover Only).cbr

### star trek city on edge of forever — #001  *(issue)*

- `   21 MB`  Star Trek/Star Trek - City on the Edge of Forever 01-05 (2014)/Star Trek - City on the Edge of Forever 001 (2014) (Digital) (TLK-EMPIRE-HD).cbr
- `    2 MB`  Star Trek/Star Trek - City on the Edge of Forever 01-05 (2014)/Variant Covers/Star Trek - City on the Edge of Forever 001 (2014) (Variant Cover Only) [extracted] (TheOrions-DCP).cbr

### darkness — #08  *(issue)*

- `   13 MB`  Garth Ennis Collection/The Darkness/The Darkness Volume 3/The Darkness 08 - Issue 72.cbr
- `    9 MB`  Garth Ennis Collection/The Darkness/The Darkness Volume 1/the darkness #08.cbr

### nextwave agents of h.a.t.e. — #05  *(issue)*

- `   12 MB`  Warren Ellis/2006/2006 Nextwave/Nextwave - Agents of H.A.T.E. #05.cbr
- `   10 MB`  Warren Ellis/2006/2006 Nextwave/Nextwave - Agents of H.A.T.E. #05 (Crayon Butchery Variant).cbr

### hellboy gets married  *(issue)*

- `   11 MB`  Hellboy/41.)  Hellboy Gets Married, Parts 1-2  (1956 AD)/Hellboy Gets Married, Part 2.cbr
- `   11 MB`  Hellboy/41.)  Hellboy Gets Married, Parts 1-2  (1956 AD)/Hellboy Gets Married, Part 1.cbr

### seven soldiers — #00  *(issue)*

- `   22 MB`  Grant Morrison/Comics/Seven Soldiers (DC 2005)/Seven Soldiers 00 (2005) (Lightray-DCP).cbr
- `    1 MB`  Grant Morrison/Comics/Seven Soldiers (DC 2005)/Seven Soldiers 00 2nd Printing Cover (Apocalypse-DCP).cbr

### terra obscura — #004  *(issue)*

- `   12 MB`  Alan Moore/Alan Moore Collection IV-  America's Best Comics/Terra Obscura/Terra Obscura Volume 2/Terra Obscura #004.cbr
- `   10 MB`  Alan Moore/Alan Moore Collection IV-  America's Best Comics/Terra Obscura/Terra Obscura Volume 1/Terra Obscura #004.cbr

### spirit — #017  *(issue)*

- `   12 MB`  Will Eisner/Spirit (1950s)/The_Spirit_017__Quality___1949___Spirit__The_012_Super_Comics_1964__36p_c2c.cbr
- `   10 MB`  Will Eisner/The Spirit 001-087 (1983-1992)/The Spirit 017 (1986) (Kitchen Sink) (c2c) (Custer Beaton).cbr

### terra obscura — #005  *(issue)*

- `   12 MB`  Alan Moore/Alan Moore Collection IV-  America's Best Comics/Terra Obscura/Terra Obscura Volume 1/Terra Obscura #005.cbr
- `   10 MB`  Alan Moore/Alan Moore Collection IV-  America's Best Comics/Terra Obscura/Terra Obscura Volume 2/Terra Obscura #005.cbr

### deathco — v2  *(volume)*

- `   14 MB`  Manga/Deathco manga/Deathco - v2 c7 [batoto].cbz
- `    8 MB`  Manga/Deathco manga/Deathco - v2 c8 [batoto].cbz

### batman — #680  *(issue)*

- `   21 MB`  Grant Morrison/Comics/Batman (DC 2006)/Batman 680 (2008) (fixed) (Minutemen-Zonylie).cbz
- `    1 MB`  Grant Morrison/Comics/Batman (DC 2006)/Batman 680 (2008) (Tony Daniel variant cover) (Minutemen-Y2K).cbr

### dynamo — #5  *(issue)*

- `   11 MB`  Robert Kirkman/Invincible (Kirkman)/Extras/Dynamo 5/Dynamo 5 18 (of 25) (2008) (Digital) (Li'l DR & Quinch-Empire).cbr
- `   10 MB`  Robert Kirkman/Invincible (Kirkman)/Extras/Dynamo 5/Dynamo 5 17 (of 25) (2008) (Digital) (Li'l DR & Quinch-Empire).cbr

### excalibur — v1  *(volume)*

- `   17 MB`  Warren Ellis/1995/Excalibur/Excalibur v1 #090a - X-Men Annual 1995.cbr
- `    4 MB`  Warren Ellis/1995/Excalibur/Excalibur v1 #094a - X-Man #012.cbr

### terra obscura — #006  *(issue)*

- `   12 MB`  Alan Moore/Alan Moore Collection IV-  America's Best Comics/Terra Obscura/Terra Obscura Volume 1/Terra Obscura #006.cbr
- `    8 MB`  Alan Moore/Alan Moore Collection IV-  America's Best Comics/Terra Obscura/Terra Obscura Volume 2/Terra Obscura #006.cbr

### terra obscura — #003  *(issue)*

- `   12 MB`  Alan Moore/Alan Moore Collection IV-  America's Best Comics/Terra Obscura/Terra Obscura Volume 2/Terra Obscura #003.cbr
- `    8 MB`  Alan Moore/Alan Moore Collection IV-  America's Best Comics/Terra Obscura/Terra Obscura Volume 1/Terra Obscura #003.cbr

### penny for your soul — #03  *(issue)*

- `   18 MB`  Penny For Your Soul (v1-v3+)(2010-2014)/Penny for Your Soul (v1-v3)(2010-2013)/01 Penny For Your Soul v1 (001-007+)(2010-2011)(Minutemen-Midas+)/Penny For Your Soul 03 (of 07) (2010) (Superclunker-DCP).cbr
- `    2 MB`  Penny For Your Soul (v1-v3+)(2010-2014)/Penny for Your Soul (v1-v3)(2010-2013)/01 Penny For Your Soul v1 (001-007+)(2010-2011)(Minutemen-Midas+)/Penny For Your Soul 03 (2010) (3 Convention Covers ONLY).cbr

### terra obscura — #002  *(issue)*

- `   10 MB`  Alan Moore/Alan Moore Collection IV-  America's Best Comics/Terra Obscura/Terra Obscura Volume 2/Terra Obscura #002.cbr
- `    9 MB`  Alan Moore/Alan Moore Collection IV-  America's Best Comics/Terra Obscura/Terra Obscura Volume 1/Terra Obscura #002.cbr

### astonishing x men xenogenesis — #001  *(issue)*

- `   10 MB`  Warren Ellis/2010/Astonishing X-Men - Xenogenesis/Astonishing X-Men - Xenogenesis 001 (2010) (noads) DigitalAnarchy-CPS.cbr
- `   10 MB`  Warren Ellis/2010/Astonishing X-Men - Xenogenesis/Astonishing X-Men - Xenogenesis 001.cbr

### terra obscura — #001  *(issue)*

- `    9 MB`  Alan Moore/Alan Moore Collection IV-  America's Best Comics/Terra Obscura/Terra Obscura Volume 2/Terra Obscura #001.cbr
- `    9 MB`  Alan Moore/Alan Moore Collection IV-  America's Best Comics/Terra Obscura/Terra Obscura Volume 1/Terra Obscura #001.cbr

### anna mercury — #004  *(issue)*

- `   17 MB`  Warren Ellis/2008/2008 Anna Mercury/Vol 1 [Complete]/Anna Mercury 004 (All Four Covers) (2008) (The Ramones-DCP).cbr
- `    1 MB`  Warren Ellis/2008/2008 Anna Mercury/Vol 1 [Complete]/Anna Mercury 004 Auxiliary (Cover Only) (2008) (The Ramones-DCP).cbr

### wolfskin — #01  *(issue)*

- `   17 MB`  Warren Ellis/2006/2006 Wolfskin/Wolfskin #01.cbr
- `    1 MB`  Warren Ellis/2006/2006 Wolfskin/Wolfskin #01 (auxiliary variant).cbr

### jersey gods — #004  *(issue)*

- `   16 MB`  Jersey Gods (001-012+)(2009-2010)(digital)(Darkness-Empire)/Jersey Gods 004 (2009) (2 Covers) (Digital) (Darkness-Empire).cbr
- `    1 MB`  Jersey Gods (001-012+)(2009-2010)(digital)(Darkness-Empire)/covers/Jersey Gods 004 (2009) (Variant Cover Only) [extracted] (Darkness-Empire).cbr

### jersey gods — #003  *(issue)*

- `   16 MB`  Jersey Gods (001-012+)(2009-2010)(digital)(Darkness-Empire)/Jersey Gods 003 (2009) (2 Covers) (Digital) (Darkness-Empire).cbr
- `    1 MB`  Jersey Gods (001-012+)(2009-2010)(digital)(Darkness-Empire)/covers/Jersey Gods 003 (2009) (Variant Cover Only) [extracted] (Darkness-Empire).cbr

### jdaction — #1  *(issue)*

- `   13 MB`  Judge Dredd - Collections/Judge Dredd Collected from 2000AD progs 0001 - 1829 (1977 - 2013) (complete) (Inc  Specials & Annuals 1977 - 1999)/Judge Dredd Collected from Annuals & Specials (1977 - 1999) (- JJ -)/JDAction-Special #1 (1996) - Mean Machine.cbr
- `    5 MB`  Judge Dredd - Collections/Judge Dredd Collected from 2000AD progs 0001 - 1829 (1977 - 2013) (complete) (Inc  Specials & Annuals 1977 - 1999)/Judge Dredd Collected from Annuals & Specials (1977 - 1999) (- JJ -)/JDAction-Special #1 (1996) - Rats & Fink.cbr

### girl in heels — v4  *(volume)*

- `    6 MB`  Manga/Girl in Heels/Girl in Heels v04 c16.cbz
- `    6 MB`  Manga/Girl in Heels/Girl in Heels v04 c18.cbz
- `    5 MB`  Manga/Girl in Heels/Girl in Heels v04 c17.cbz

### penny for your soul — #02  *(issue)*

- `   16 MB`  Penny For Your Soul (v1-v3+)(2010-2014)/Penny for Your Soul (v1-v3)(2010-2013)/01 Penny For Your Soul v1 (001-007+)(2010-2011)(Minutemen-Midas+)/Penny For Your Soul 02 (of 07) (2010) (c2c) (4 covers) (Minutemen-Midas).cbr
- `    0 MB`  Penny For Your Soul (v1-v3+)(2010-2014)/Penny for Your Soul (v1-v3)(2010-2013)/01 Penny For Your Soul v1 (001-007+)(2010-2011)(Minutemen-Midas+)/Penny For Your Soul 02 (2010) (Fico Ossio convention variant cover ONLY) (Minutemen-Midas).cbr

### jersey gods — #002  *(issue)*

- `   14 MB`  Jersey Gods (001-012+)(2009-2010)(digital)(Darkness-Empire)/Jersey Gods 002 (2009) (2 Covers) (Digital) (Darkness-Empire).cbr
- `    1 MB`  Jersey Gods (001-012+)(2009-2010)(digital)(Darkness-Empire)/covers/Jersey Gods 002 (2009) (Variant Cover Only) [extracted] (Darkness-Empire).cbr

### hellboy how koshchei became deathless  *(issue)*

- `    7 MB`  Hellboy/1.)  Hellboy - How Koshchei Became Deathless, Parts 1-2  (Unknown)/Hellboy - How Koshchei Became Deathless, Part 2.cbr
- `    7 MB`  Hellboy/1.)  Hellboy - How Koshchei Became Deathless, Parts 1-2  (Unknown)/Hellboy - How Koshchei Became Deathless, Part 1.cbr

### jersey gods — #001  *(issue)*

- `   13 MB`  Jersey Gods (001-012+)(2009-2010)(digital)(Darkness-Empire)/Jersey Gods 001 (2009) (2 Covers) (Digital) (Darkness-Empire).cbr
- `    0 MB`  Jersey Gods (001-012+)(2009-2010)(digital)(Darkness-Empire)/covers/Jersey Gods 001 (2009) (Variant Cover Only) [extracted] (Minutemen-PhD).cbr

### fridayth — #001  *(special)*

- `   12 MB`  Friday the 13th/Friday the 13th Special 001 (2005) (Apocalypse-DCP)/Friday the 13th Special 001 (2005) (Apocalypse-DCP).cbr
- `    1 MB`  Friday the 13th/Friday the 13th Special 001 (2005) (Apocalypse-DCP)/Friday the 13th 001 Special - No Escape Cover (Apocalypse-DCP).cbr

### batman — #671  *(issue)*

- `   12 MB`  Grant Morrison/Comics/Batman (DC 2006)/Batman 671 (2007) (StiffUpperLip-DCP).cbr
- `    0 MB`  Grant Morrison/Comics/Batman (DC 2006)/Batman 671 (2nd printing cover) (2008) (KingDaubach-DCP).cbr

### excalibur — v1 — #103  *(volume)*

- `    7 MB`  Warren Ellis/1995/Excalibur/Excalibur v1 #103.cbz
- `    6 MB`  Warren Ellis/1995/Excalibur/Excalibur v1 #103 - X-Men Unlimited #026.cbz

### at end of road c16  *(issue)*

- `    5 MB`  Manga/At the End of the Road manga/At the End of the Road - c16 [batoto].cbz
- `    5 MB`  Manga/At the End of the Road manga/At the End of the Road - c16 [MangaGo].cbz

### densha de d — v0  *(volume)*

- `    4 MB`  Manga/Densha_de_D/Densha de D v0 c02.cbr
- `    4 MB`  Manga/Densha_de_D/Densha de D v0 c01.cbr

### at end of road c27  *(issue)*

- `    4 MB`  Manga/At the End of the Road manga/At the End of the Road - c27 [MangaGo].cbz
- `    4 MB`  Manga/At the End of the Road manga/At the End of the Road - c27 [batoto].cbz

### at end of road c24  *(issue)*

- `    4 MB`  Manga/At the End of the Road manga/At the End of the Road - c24 [MangaGo].cbz
- `    4 MB`  Manga/At the End of the Road manga/At the End of the Road - c24 [batoto].cbz

### at end of road c26  *(issue)*

- `    4 MB`  Manga/At the End of the Road manga/At the End of the Road - c26 [batoto].cbz
- `    4 MB`  Manga/At the End of the Road manga/At the End of the Road - c26 [MangaGo].cbz

### at end of road c20  *(issue)*

- `    4 MB`  Manga/At the End of the Road manga/At the End of the Road - c20 [batoto].cbz
- `    3 MB`  Manga/At the End of the Road manga/At the End of the Road - c20 [MangaGo].cbz

### at end of road c29  *(issue)*

- `    4 MB`  Manga/At the End of the Road manga/At the End of the Road - c29 [MangaGo].cbz
- `    3 MB`  Manga/At the End of the Road manga/At the End of the Road - c29 [batoto].cbz

### at end of road c28  *(issue)*

- `    3 MB`  Manga/At the End of the Road manga/At the End of the Road - c28 [MangaGo].cbz
- `    3 MB`  Manga/At the End of the Road manga/At the End of the Road - c28 [batoto].cbz

### hybrid insector — v1  *(volume)*

- `    3 MB`  Manga/Kamen Rider/Hybrid Insector/Hybrid Insector - v1 [batoto].cbz
- `    3 MB`  Manga/Kamen Rider/Hybrid Insector/Hybrid Insector - v1 c1 [batoto].cbz

### at end of road c42  *(issue)*

- `    3 MB`  Manga/At the End of the Road manga/At the End of the Road - c42 [batoto - No Group].cbz
- `    3 MB`  Manga/At the End of the Road manga/At the End of the Road - c42 [MangaGo].cbz

### at end of road c46  *(issue)*

- `    3 MB`  Manga/At the End of the Road manga/At the End of the Road - c46 [batoto - No Group].cbz
- `    2 MB`  Manga/At the End of the Road manga/At the End of the Road - c46 [MangaGo].cbz

### at end of road c47  *(issue)*

- `    3 MB`  Manga/At the End of the Road manga/At the End of the Road - c47 [batoto - No Group].cbz
- `    2 MB`  Manga/At the End of the Road manga/At the End of the Road - c47 [MangaGo].cbz

### night raven cure  *(issue)*

- `    2 MB`  Alan Moore/Alan Moore Collection I- English Invasion/Alan Moore Collection II- Marvel UK/Night Raven/Night Raven (Marvel Super-Heroes)/Night Raven- The Cure/Night Raven- The Cure Part 2 (Marvel Super-Heroes #391).cbr
- `    1 MB`  Alan Moore/Alan Moore Collection I- English Invasion/Alan Moore Collection II- Marvel UK/Night Raven/Night Raven (Marvel Super-Heroes)/Night Raven- The Cure/Night Raven- The Cure Part 1 (Marvel Super-Heroes #390).cbr

### b.p.r.d. revival  *(issue)*

- `    2 MB`  Hellboy/111.)  B.P.R.D. - Revival, Parts 1-2  (2005 AD)/B.P.R.D. - Revival, Part 2.cbr
- `    1 MB`  Hellboy/111.)  B.P.R.D. - Revival, Parts 1-2  (2005 AD)/B.P.R.D. - Revival, Part 1.cbr

### night raven white hopes, red nightmares  *(issue)*

- `    2 MB`  Alan Moore/Alan Moore Collection I- English Invasion/Alan Moore Collection II- Marvel UK/Night Raven/Night Raven (Marvel Super-Heroes)/Night Raven- White Hopes, Red Nightmares/Night Raven- White Hopes, Red Nightmares Part 1 (Marvel Super-Heroes #392).cbr
- `    1 MB`  Alan Moore/Alan Moore Collection I- English Invasion/Alan Moore Collection II- Marvel UK/Night Raven/Night Raven (Marvel Super-Heroes)/Night Raven- White Hopes, Red Nightmares/Night Raven- White Hopes, Red Nightmares Part 2 (Marvel Super-Heroes #393).cbr

### star trek legion of super heroes — #01  *(issue)*

- `    1 MB`  Star Trek/Star Trek - Legion of Super-Heroes (2011-2012)/Variant Covers/Star Trek - Legion of Super-Heroes 01 (2011) (2nd Printing Variant Only) (ScanDog).cbr
- `    1 MB`  Star Trek/Star Trek - Legion of Super-Heroes (2011-2012)/Variant Covers/Star Trek - Legion of Super-Heroes 01 (2011) (RE Cover Only) [extracted] (digital-Empire).cbr

### 2000ad — #0701  *(issue)*

- `    1 MB`  2000AD prog/2000AD (Specials, Annuals & Poster Progs + Extras)/2000AD Free Gifts/2000AD 0701 ScanCard 4 - Judge Dredd (Hydrocardiac).cbr
- `    1 MB`  2000AD prog/2000AD (Specials, Annuals & Poster Progs + Extras)/2000AD Free Gifts/2000AD 0701 ScanCard 3 - Kano (Hydrocardiac).cbr

### night raven sadie's story  *(issue)*

- `    1 MB`  Alan Moore/Alan Moore Collection I- English Invasion/Alan Moore Collection II- Marvel UK/Night Raven/Night Raven (Marvel Super-Heroes)/Night Raven- Sadie's Story/Night Raven- Sadie's Story Part 1 (Marvel Super-Heroes #394).cbr
- `    1 MB`  Alan Moore/Alan Moore Collection I- English Invasion/Alan Moore Collection II- Marvel UK/Night Raven/Night Raven (Marvel Super-Heroes)/Night Raven- Sadie's Story/Night Raven- Sadie's Story Part 2 (Marvel Super-Heroes #395).cbr

### 2000ad — #0703  *(issue)*

- `    1 MB`  2000AD prog/2000AD (Specials, Annuals & Poster Progs + Extras)/2000AD Free Gifts/2000AD 0703 ScanCard 7 - Harlem Heroes (Hydrocardiac).cbr
- `    1 MB`  2000AD prog/2000AD (Specials, Annuals & Poster Progs + Extras)/2000AD Free Gifts/2000AD 0703 ScanCard 8 - Chopper (Hydrocardiac).cbr

### 2000ad — #0828  *(issue)*

- `    1 MB`  2000AD prog/2000AD (Specials, Annuals & Poster Progs + Extras)/2000AD Free Gifts/2000AD 0828 ScanCard v2 1 - Judge Dredd (Hydrocardiac).cbr
- `    0 MB`  2000AD prog/2000AD (Specials, Annuals & Poster Progs + Extras)/2000AD Free Gifts/2000AD 0828 ScanCard v2 2 - Judge Anderson (Hydrocardiac).cbr

### 2000ad — #0700  *(issue)*

- `    0 MB`  2000AD prog/2000AD (Specials, Annuals & Poster Progs + Extras)/2000AD Free Gifts/2000AD 0700 ScanCard 1 - Rogue Trooper (Hydrocardiac).cbr
- `    0 MB`  2000AD prog/2000AD (Specials, Annuals & Poster Progs + Extras)/2000AD Free Gifts/2000AD 0700 ScanCard 2 - Judge Dredd (Hydrocardiac).cbr
