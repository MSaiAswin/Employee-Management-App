# Task 8

## Steps
 - Here I have created a shell script to backup the app database, using a tool called mysqldump
 - To execute it at repeated intervals, we can use cron.
 - For that, in the mysql sever, we edit the crontab.
 - There we add the line "0 0 * * * /path/to/script.sh"
 - Now backups will be taken everyday at 12:00 AM.
