#/usr/bin/bash

echo "Updating data"

while :
do
  git add .
  git commit -m "updating data"
  git push -u origin master
  sleep 5
done 
