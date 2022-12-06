# Crontab Entries

These are example crontab entries to start and stop the chrismas tree at given times.  Install as either the user (if permitted to run systemctl), or root.

```
0 5 * * * /bin/systemctl start rgbxmastree.service
0 0 * * * /bin/systemctl stop rgbxmastree.service
```

