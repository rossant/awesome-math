#!/bin/bash

# --------------------------------- Create the pdf directory if not exists --
if [ ! -d pdf ]; then
    mkdir pdf
fi

# ---------------------------------------- Add pdf directory to .gitignore --
if [ ! -f .gitignore ]; then
    echo pdf > .gitignore
else
    grep -q -F 'pdf' .gitignore || echo 'pdf' >> .gitignore
fi

# ---------------------------------------- Download pdf file if not exists --
for f in `sed -rn 's/.*(http.+\.pdf).*/\1/pg' README.md`
do
    if [ ! -f "pdf/${f##*/}" ]; then
        wget --tries=3 \
            --timeout=5 \
            --waitretry=1 \
            --retry-connrefused \
            "$f" -P pdf
    fi
done
