#/usr/bin/bash

echo "Updating data"

while :
do
  python3 /home/dnaneet/ComputationalMechanicsPlayGround/SHM/data.py
  git add .
  git commit -m "updating data"
  git push -u origin master
  sleep 5
done 
