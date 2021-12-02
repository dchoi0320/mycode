#!/bin/bash
# push the code to GitHub

COMMENT="$1"
WORKING_PATH="/home/dchoi/trainings/Python_API/mycode"

#cd /home/dchoi/trainings/Python_API/mycode
cd ${WORKING_PATH}
git add *
#git commit -m "serving cookies"
git commit -m ${COMMENT}
git push origin main
