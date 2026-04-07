# Comic File Organizer Project

## Overview
Organizing 72 comic files from `/home/nesha/Downloads/comics_download/`
into consolidated folders in `/mnt/extramedia/Comics/` (5975+ items)

## Strategy
- Extract first part of series names (before hyphens/numbers)
- Match left panel files with right panel files
- Create consolidated series folders
- Move all related files (left + right) into series folders

## Key Files
- matching_analysis_consolidated.csv: File matching results (54 consolidations, 12 new folders)
- Input: /home/nesha/Downloads/comics_download/ (72 files)
- Output: /mnt/extramedia/Comics/ (destination)

## Models
- Haiku 4.5: Web page UI (fast, cost-effective)
- Sonnet 4.6: Escalate if Python script complexity increases

## Consolidation Examples
- Animal Stories (1 left + 1 right = /Animal Stories/)
- Ghost Pepper (1 left + 8 right = /Ghost Pepper/)
- Cruel Universe II (1 left + 5 right = /Cruel Universe II/)

## 12 Unmatched (need new folders)
Amazonia, A Mischief of Magpies, Emilie's Inheritance, Good Devils,
Quick Stops, Reborn Library, Royals, Order Of Saint Sophia, Shadower,
Uri Tupka and the Gods, WitchCraft
