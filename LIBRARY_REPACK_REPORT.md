# Repacked comics — please open each one

Two different faults, fixed the same way: extract, then write a
plain stored zip. The links open the files themselves.

Page images were copied byte for byte. Nothing was re-encoded and
no quality was lost — including the WebP books, which QComicBook
turned out to be perfectly happy with once they were out of 7z.

## 11 read in the wrong order, now rebuilt

These opened perfectly well already. The issues inside them were
merged in the wrong order, so they read 1, 11, 12, 2, 3 ... Every
page is byte for byte the one that was there before; only the name
it is stored under changed.

| pages | was | size | open it |
|---|---|---|---|
| 1474 | makecbz volume | 2110 MB | [Sorcery 101 (2015).cbz](file:///mnt/extramedia/Comics/Sorcery%20101%20%28001-049%29%282014-2017%29%28digital-Empire%29/Sorcery%20101%20%282015%29.cbz) |
| 1330 | makecbz volume | 2184 MB | [Scarlet Traces - Empire of Blood (2025).cbz](file:///mnt/extramedia/Comics/Scarlet%20Traces/Scarlet%20Traces%20-%20Empire%20of%20Blood%20%282025%29/Scarlet%20Traces%20-%20Empire%20of%20Blood%20%282025%29.cbz) |
| 473 | makecbz volume | 635 MB | [Criminal 001-012 (2019-2020).cbz](file:///mnt/extramedia/Comics/Criminal/Criminal%20001-012%20%282019-2020%29.cbz) |
| 428 | makecbz volume | 170 MB | [A Distant Soil v01.cbz](file:///mnt/extramedia/Comics/A%20Distant%20Soil/3.%20A%20Distant%20Soil%201-%2014%20%5B1991%20-%201994%5D%20Aria%20Press/A%20Distant%20Soil%20v01.cbz) |
| 409 | makecbz volume | 585 MB | [Die!Die!Die!.cbz](file:///mnt/extramedia/Comics/Die%21Die%21Die%21/Die%21Die%21Die%21.cbz) |
| 399 | makecbz volume | 268 MB | [Insufferable v2 (01-32) (2013).cbz](file:///mnt/extramedia/Comics/Insufferable/Insufferable%20v2%20%2801-32%29%20%282013%29/Insufferable%20v2%20%2801-32%29%20%282013%29.cbz) |
| 377 | makecbz volume | 180 MB | [Love and Capes.cbz](file:///mnt/extramedia/Comics/Love%20and%20Capes/Love%20and%20Capes.cbz) |
| 351 | makecbz volume | 488 MB | [Ghosted in L.A. (2020).cbz](file:///mnt/extramedia/Comics/Ghosted%20in%20L.A.%20%282020%29/Ghosted%20in%20L.A.%20%282020%29.cbz) |
| 332 | makecbz volume | 1146 MB | [Igor Grom (2018).cbz](file:///mnt/extramedia/Comics/Igor%20Grom%20%282018%29/Igor%20Grom%20%282018%29.cbz) |
| 305 | makecbz volume | 463 MB | [Ignited 001-008 (2019-2020).cbz](file:///mnt/extramedia/Comics/Ignited%20001-008%20%282019-2020%29/Ignited%20001-008%20%282019-2020%29.cbz) |
| 222 | makecbz volume | 128 MB | [Insufferable v3 (01-18) (2014-2015).cbz](file:///mnt/extramedia/Comics/Insufferable/Insufferable%20v3%20%2801-18%29%20%282014-2015%29/Insufferable%20v3%20%2801-18%29%20%282014-2015%29.cbz) |

## 19 would not open in QComicBook, now repacked

These were 7z or tar wearing a `.cbr`/`.cbz` name, plus one zip that
held whole comics instead of pages. The container was the entire
objection — QComicBook reads the pages themselves fine.

| pages | was | size | open it |
|---|---|---|---|
| 234 | 7z | 320 MB | [The Living Corpse Omnibus Vol. 1 (2007).cbz](file:///mnt/extramedia/Comics/The%20Living%20Corpse%20Omnibus%20Vol.%201%20%282007%29.cbz) |
| 188 | rar | 617 MB | [The Rise and Fall of the Trigan Empire v02 (2020) (digital) (Mr Norrell-Empire).cbz](file:///mnt/extramedia/Comics/Trigan%20Empire%20/The%20Rise%20and%20Fall%20of%20the%20Trigan%20Empire%20v02%20%282020%29%20%28digital%29%20%28Mr%20Norrell-Empire%29.cbz) |
| 168 | 7z | 60 MB | [The Winter Men (2005) \[RC HQ-Scan 576p\] ComixLedger.cbz](file:///mnt/extramedia/Comics/The%20Winter%20Men%20%282005%29%20%5BRC%20HQ-Scan%20576p%5D%20ComixLedger.cbz) |
| 161 | 7z | 205 MB | [3 Guns (2013) TPB.cbz](file:///mnt/extramedia/Comics/3%20Guns%20%282013%29%20TPB.cbz) |
| 146 | zip wrapper | 311 MB | [Patience! Conviction! Revenge! (2018) .cbz](file:///mnt/extramedia/Comics/Patience%21%20Conviction%21%20Revenge%21%20%282018%29%20/Patience%21%20Conviction%21%20Revenge%21%20%282018%29%20.cbz) |
| 138 | 7z | 49 MB | [The Programme (2007) Vol. 1 \[RC HQ-Scan 720p\] ComixLedger.cbz](file:///mnt/extramedia/Comics/The%20Programme%20%282007%29%20Vol.%201-2%20%28RC%29%20ComixLedger/The%20Programme%20%282007%29%20Vol.%201%20%5BRC%20HQ-Scan%20720p%5D%20ComixLedger.cbz) |
| 137 | 7z | 48 MB | [The Programme (2007) Vol. 2 \[RC HQ-Scan 720p\] ComixLedger.cbz](file:///mnt/extramedia/Comics/The%20Programme%20%282007%29%20Vol.%201-2%20%28RC%29%20ComixLedger/The%20Programme%20%282007%29%20Vol.%202%20%5BRC%20HQ-Scan%20720p%5D%20ComixLedger.cbz) |
| 122 | rar | 475 MB | [Carbon Grey - Omnibus (2016) GetComics.INFO.cbz](file:///mnt/extramedia/Comics/Image%20comics/Carbon%20Grey/Carbon%20Grey%20-%20Omnibus%20%282016%29%20GetComics.INFO.cbz) |
| 105 | zip | 444 MB | [Lake of Fire (2017) (Digital) (XRA-Empire).cbz](file:///mnt/extramedia/Comics/Image%20comics/Lake%20of%20Fire%20%282017%29%20%28Digital%29%20%28XRA-Empire%29.cbz) |
| 50 | 7z | 99 MB | [Alix Senator v08 - The City of Poisons (2018) (Scanlation) (phillywilly).cbz](file:///mnt/extramedia/Comics/Alix%20Senator%20%20%282012-2020%29/Alix%20Senator%20v08%20-%20The%20City%20of%20Poisons%20%282018%29%20%28Scanlation%29%20%28phillywilly%29.cbz) |
| 49 | rar | 71 MB | [Stern 02 - City of Savages _2018_ _Europe Comics_ _Digital-Empire_ (newcomic.info).cbz](file:///mnt/extramedia/Comics/Europe%20Comics%20%28Collection%29/Stern/Stern%2002%20-%20City%20of%20Savages%20_2018_%20_Europe%20Comics_%20_Digital-Empire_%20%28newcomic.info%29.cbz) |
| 48 | ace | 15 MB | [Aria 07 - A Murder of Crows (Ringoscann).cbz](file:///mnt/extramedia/Comics/Aria%20%28Collection%29%20GetComics.INFO/Aria%2007%20-%20A%20Murder%20of%20Crows%20%28Ringoscann%29.cbz) |
| 42 | tar | 76 MB | [Firefly 20th Anniversary Special 001.cbz](file:///mnt/extramedia/Comics/Firefly/Firefly%2020th%20Anniversary%20Special%20001.cbz) |
| 42 | rar | 91 MB | [The Celestial Bibendum 2 (Digital) (Humanoids).cbz](file:///mnt/extramedia/Comics/The%20Celestial%20Bibendum/The%20Celestial%20Bibendum%202%20%28Digital%29%20%28Humanoids%29.cbz) |
| 38 | ace | 56 MB | [Spirou & Fantasio 19 - Baby Fever in Champignac.cbz](file:///mnt/extramedia/Comics/Spirou%20%26%20Fantasio/Spirou%20%26%20Fantasio%2019%20-%20Baby%20Fever%20in%20Champignac.cbz) |
| 20 | 7z | 14 MB | [Tales from Myth - The Fallen Lords.cbz](file:///mnt/extramedia/Comics/Tales%20from%20Myth%20-%20The%20Fallen%20Lords.cbz) |
| 7 | rar | 12 MB | [The Celestial Bibendum 3 (Digital) (Humanoids).cbz](file:///mnt/extramedia/Comics/The%20Celestial%20Bibendum/The%20Celestial%20Bibendum%203%20%28Digital%29%20%28Humanoids%29.cbz) |
| 2 | rar | 2 MB | [Anna Mercury 2 001 (2009) (Three Covers) (Minutemen-Shamil).cbz](file:///mnt/extramedia/Comics/Warren%20Ellis/2008/2008%20Anna%20Mercury/Vol%202/Anna%20Mercury%202%20001%20%282009%29%20%28Three%20Covers%29%20%28Minutemen-Shamil%29.cbz) |
| 2 | rar | 1 MB | [Where is Kiki (Europe Comics 2020) (webrip) (MagicMan-DCP).cbz](file:///mnt/extramedia/Comics/Europe%20Comics%20%28Collection%29/Where%20is%20Kiki%20%28Europe%20Comics%202020%29%20%28webrip%29%20%28MagicMan-DCP%29.cbz) |

The originals are in `/mnt/extramedia/_quarantine/`, under the
same relative path they had in the library. Nothing was deleted.

## 14 error pages moved out of the library

These were `429 Too Many Requests` HTML, not comics. See
`LIBRARY_REDOWNLOAD.md` for the list to fetch again.

