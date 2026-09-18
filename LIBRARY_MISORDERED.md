# Volumes merged in the wrong page order

Every volume below was built by `makecbz.py`, which is detectable
because it leaves its `temp_extract_` folders inside the archive.

It numbered those folders without zero-padding, so `temp_extract_10_`
sorts *before* `temp_extract_1_` — `0` is 48 and `_` is 95. A volume
is therefore fine up to ten issues and scrambled from eleven, which
is why this went unnoticed for so long.

Nothing was lost. The folder name still carries the issue number, so
the reading order can be rebuilt from inside the volume itself —
the original issue files are not needed.

## 11 read in the wrong order

| issues | pages out of order | file |
|---|---|---|
| 49 | issues 2–49 | `Sorcery 101 (001-049)(2014-2017)(digital-Empire)/Sorcery 101 (2015).cbz` |
| 33 | issues 2–33 | `Insufferable/Insufferable v2 (01-32) (2013)/Insufferable v2 (01-32) (2013).cbz` |
| 23 | issues 2–23 | `Scarlet Traces/Scarlet Traces - Empire of Blood (2025)/Scarlet Traces - Empire of Blood (2025).cbz` |
| 18 | issues 2–18 | `Insufferable/Insufferable v3 (01-18) (2014-2015)/Insufferable v3 (01-18) (2014-2015).cbz` |
| 14 | issues 2–14 | `A Distant Soil/3. A Distant Soil 1- 14 [1991 - 1994] Aria Press/A Distant Soil v01.cbz` |
| 14 | issues 2–14 | `Die!Die!Die!/Die!Die!Die!.cbz` |
| 13 | issues 2–13 | `Love and Capes/Love and Capes.cbz` |
| 12 | issues 2–12 | `Criminal/Criminal 001-012 (2019-2020).cbz` |
| 12 | issues 2–12 | `Ghosted in L.A. (2020)/Ghosted in L.A. (2020).cbz` |
| 12 | issues 2–12 | `Igor Grom (2018)/Igor Grom (2018).cbz` |
| 11 | issues 2–11 | `Ignited 001-008 (2019-2020)/Ignited 001-008 (2019-2020).cbz` |

Repair them with:

```
python3 repack_comics.py --repair --execute FILE...
```

## 132 built by the same tool but still in order

Ten issues or fewer, so the unpadded index never overtook itself.
They carry the `temp_extract_` folders but read correctly.

