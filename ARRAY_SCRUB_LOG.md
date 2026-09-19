# RAID1 scrub log — `vgextra/lvextra` (`/mnt/extramedia`)

> **Next scrub due: 2026-12-19.** Commands below.

The operational record: what each scrub measured, and how to run the next one.
The *analysis* of the 2026-09-19 result — what 768 means, the two explanations
that fit, why reading the library cannot verify it — lives in
[`LIBRARY_BROKEN_FILES.md`](LIBRARY_BROKEN_FILES.md), under
*The mirror disagrees with itself, in 96 places*. Not repeated here.

This file exists because **the absolute number is not the diagnostic — the change
in it is.** One count says little. Two counts, months apart, separate a scar from
a spreading wound:

* **Roughly unchanged** → historical damage, not spreading. Close it out.
* **Materially higher** → a leg is actively diverging. Replacement decision.

The counter resets at the start of every `check`, so each run is an independent
measurement and the comparison holds.

---

## Results

| date | mismatches | ≈ real errors | duration | after |
|---|---|---|---|---|
| 2026-09-19 | **768** | 96 × 4 KB ≈ 384 KB | 8 h 13 m | `idle`, health `mismatches exist` |

At the 60% mark the count stood at 384, so the back 40% of the array carried
roughly 1.5× the density of the front. Mildly non-uniform, nowhere near clustered
enough to point at a region. One data point — not worth reading into.

`dmesg -T` gives start and end and nothing else; there is no per-mismatch
location data to recover:

```
[Sat Sep 19 08:46:01 2026] md: data-check of RAID array mdX
[Sat Sep 19 16:59:42 2026] md: mdX: data-check done.
```

---

## Do not run `--syncaction repair`

Two copies, no parity, no checksums anywhere in the stack — nothing can identify
the correct leg. Repair copies one over the other by convention and makes the
disagreement permanent in whichever direction it happened to pick.

It would also zero the counter, which looks like a fix and would destroy the
baseline the December scrub depends on.

`mismatches exist` is a true statement about the array, not an error to clear.

---

## Drive baseline, 2026-09-19

Both `PASSED`. Every attribute that would indicate failing media is zero.

| | `/dev/sdc` | `/dev/sde` |
|---|---|---|
| Power_On_Hours | 71,234 (**8.1 years**) | 62,710 (**7.2 years**) |
| Reallocated_Sector_Ct | 0 | 0 |
| Current_Pending_Sector | 0 | 0 |
| Offline_Uncorrectable | 0 | 0 |
| UDMA_CRC_Error_Count | 0 | 0 |
| Temperature_Celsius | 23 | 23 |
| Power_Cycle_Count | 177 | 104 |
| Start_Stop_Count | 425 | 358 |
| Load_Cycle_Count | 8,316 | 6,358 |

Zero reallocations after eight years of power-on is genuinely good. It is also
eight years — past the age where continued health should be assumed, independent
of anything the scrub found.

---

## Commands

### Start a scrub

```sh
sudo lvchange --syncaction check vgextra/lvextra
```

Returns immediately — it queues the scrub rather than blocking. Read-only, needs
no free space, safe on a mounted and in-use filesystem. **Budget 8 hours**;
the 2026-09-19 run took 8 h 13 m.

Do not run a large download or repack job alongside it. Both compete for the same
two spindles, and if the count comes back surprising you want as few confounders
as possible. Saving the odd file is fine.

### Watch progress

```sh
watch -n 300 'sudo lvs -a -o name,sync_percent,raid_sync_action,raid_mismatch_count vgextra/lvextra'
```

### Read the result

```sh
sudo lvs -a -o name,raid_sync_action,raid_mismatch_count,lv_health_status vgextra
```

Done when `SyncAction` returns to `idle`.

### Start and end times

```sh
sudo dmesg -T | grep -i -E "data-check|dm-raid|resync|md[0-9]"
```

### Drive health

```sh
sudo smartctl -H -A /dev/sdc
sudo smartctl -H -A /dev/sde
```

Compare against the baseline above. For a *growing* mismatch count the rows that
matter are `Reallocated_Sector_Ct`, `Current_Pending_Sector` and
`Offline_Uncorrectable` — any of them moving off zero changes the conclusion.

---

## December checklist

- [ ] Run the scrub — **2026-12-19** or thereabouts
- [ ] Add a row to the results table above
- [ ] Re-run `smartctl` on both drives, compare to the baseline
- [ ] **≈768** → historical damage confirmed, not spreading. Close it out.
- [ ] **Materially more than 768** → a leg is diverging. Work out which drive,
      plan a replacement.
- [ ] Either way: **do not** run `--syncaction repair` to tidy the health flag.
