#!/bin/sh

. venv/bin/activate
LOG_DIR="/var/log/telegram_bot"
mkdir -p $LOG_DIR
script -c ./telegram_bot.py -f $LOG_DIR/telegram_bot.log > /dev/null &

