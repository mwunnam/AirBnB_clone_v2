#!/bin/bash

if [ "$#" -eq 0 ]; then
    echo "Adding all"
    git add .
else
    git add "$@"
fi

read -p "Commit message: " COMMIT

git commit -m"$COMMIT"


git push
