#!/bin/sh
# Raises a flag file when the RAID1 scrub on vgextra/lvextra falls due.
#
# Cron runs this daily. It does not notify anything itself, because this box has
# no notify-send, no `at` and no MTA — cron's usual ways of reaching a person are
# all absent. So it writes a file and something that runs on shell startup is
# what actually shows it.
#
# The due date lives in its own file rather than in here, so rescheduling after
# a scrub is one echo and not a code edit:
#
#   echo 2027-03-19 > ~/.config/array_scrub_due
#
# Background, commands and the results table: ARRAY_SCRUB_LOG.md, alongside this
# script. Installed via array_scrub_cron.txt, also alongside — if this file ever
# moves, that crontab entry has to move with it or the reminder dies silently.

DUE_FILE="$HOME/.config/array_scrub_due"
FLAG="$HOME/.array_scrub_due.flag"

[ -r "$DUE_FILE" ] || exit 0
due=$(date -d "$(cat "$DUE_FILE")" +%Y%m%d 2>/dev/null) || exit 0
[ -n "$due" ] || exit 0
[ "$(date +%Y%m%d)" -ge "$due" ] || exit 0

cat > "$FLAG" <<EOF
RAID1 scrub is due on /mnt/extramedia (was scheduled for $(cat "$DUE_FILE")).

  sudo lvchange --syncaction check vgextra/lvextra

Takes about 8 hours, read-only, safe while mounted. Do not run a big download
or repack job alongside it.

Last run 2026-09-19: 768 mismatches. The question this scrub answers is whether
that number has grown. Do NOT run --syncaction repair.

Full instructions: ~/scripts/cp_downloads2comics/ARRAY_SCRUB_LOG.md

Clear this reminder with:
  rm ~/.array_scrub_due.flag && echo <next-date> > ~/.config/array_scrub_due
EOF
