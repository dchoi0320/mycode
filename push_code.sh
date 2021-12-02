#!/bin/bash

COMMENT="$1"

cd /home/dchoi/trainings/Python_API/mycode
git add *
#git commit -m "serving cookies"
git commit -m ${COMMENT}
git push origin main
