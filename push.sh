#!/bin/bash
git add .
git reset set_pass.sh
read -p "Commit message:" message
set pass "vodafone20!"
git commit -m $message
git push
exec /root/playbooks/set_pass.sh

