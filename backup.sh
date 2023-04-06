#!/usr/bin/bash

DATABASE = "app"

mysqldump -u user -p password ${DATABASE} > ./backup/app_backup.sql