#!/usr/bin/env bash
# Build the distribution PDF from paper.md.
#
# U+2194 (<->) has no glyph in Latin Modern; map it to math-mode
# \leftrightarrow before typesetting. The build then asserts ZERO
# "could not represent" warnings: a dropped glyph is silent, still
# produces a PDF, and ends up as a misspelled word in the published
# record — assert the count, never eyeball it.
set -euo pipefail
cd "$(dirname "$0")/.."

tmp="$(mktemp -t paper-build).md"
sed 's/↔/$\\leftrightarrow$/g' paper.md > "$tmp"

log=$(pandoc "$tmp" -o digital-proprioception.pdf \
  --pdf-engine=tectonic --from=markdown+tex_math_dollars+raw_html \
  -V geometry:margin=1.1in -V fontsize=11pt 2>&1 || true)
rm -f "$tmp"

if printf '%s' "$log" | grep -q "could not represent"; then
  printf '%s\n' "$log" | grep "could not represent" >&2
  echo "error: unrepresentable characters above — fix before distributing" >&2
  exit 1
fi
[ -s digital-proprioception.pdf ] || { echo "error: no PDF produced" >&2; exit 1; }
echo "built digital-proprioception.pdf"
