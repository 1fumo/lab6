#!/bin/bash
echo "hello world!"
echo "testign 123"
echo "Second part question 6"
df -h | awk '$NF=="/"{printf "Disk Usage: %d/%dGB (%s)\n", $3,$2,$5}'
top -bn1 | grep load | awk '{printf "CPU Load: (%.2f%%)\n", $(NF-2)}'
