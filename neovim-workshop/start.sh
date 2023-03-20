#!/bin/bash

# start ssh
/usr/sbin/sshd &

# hold docker container
/usr/bin/tail -f /dev/null
