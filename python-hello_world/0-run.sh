#!/bin/bash
if [ ! -f "$PYFILE" ]; then
    touch "$PYFILE"
fi

python3 "$PYFILE"
