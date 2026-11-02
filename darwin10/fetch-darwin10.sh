#!/bin/sh
# Reconstitue le dossier Darwin 10 (Mac OS X 10.6.8) depuis les sources Apple open source.
# Usage : ./fetch-darwin10.sh [dossier]   (par défaut : ./tree, ~90 Mo)
set -e
dest=${1:-tree}
mkdir -p "$dest"
for pair in xnu:xnu-1504.15.3 Libc:Libc-594.9.5 Libsystem:Libsystem-125.2.11 \
            dyld:dyld-132.13 launchd:launchd-258.25 bash:bash-86.1 Csu:Csu-79 cctools:cctools-806; do
  r=${pair%%:*}; t=${pair##*:}
  mkdir -p "$dest/$r"
  curl -fsSL "https://github.com/apple-oss-distributions/$r/archive/refs/tags/$t.tar.gz" \
    | tar xz -C "$dest/$r" --strip-components=1
  echo "ok $r ($t)"
done
