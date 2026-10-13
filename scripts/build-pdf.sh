#!/usr/bin/env bash
# Build the distribution PDF from paper.md.
#
# U+2194 (<->) and U+03C1 (rho, prose only) have no glyph in Latin
# Modern; map them to math mode before typesetting. The build then
# asserts ZERO "could not represent" warnings: a dropped glyph is
# silent, still produces a PDF, and ends up as a misspelled word in
# the published record — assert the count, never eyeball it.
set -euo pipefail
cd "$(dirname "$0")/.."

# Keep a failed or interrupted build from replacing the distribution PDF.
# Build beside the destination so the final rename stays on one filesystem.
mkdir -p .scratch
build_dir=$(mktemp -d .scratch/paper-build.XXXXXX)
trap 'rm -rf "$build_dir"' EXIT
sed -e 's/↔/$\\leftrightarrow$/g' -e 's/ρ/$\\rho$/g' paper.md > "$build_dir/paper.md"

if pandoc "$build_dir/paper.md" -o "$build_dir/paper.pdf" \
  --pdf-engine=tectonic --from=markdown+tex_math_dollars+raw_html \
  -V geometry:margin=1.1in -V fontsize=11pt > "$build_dir/build.log" 2>&1; then
  :
else
  status=$?
  cat "$build_dir/build.log" >&2
  echo "error: PDF build failed; distribution PDF was not replaced" >&2
  exit "$status"
fi

if grep -Ei 'could not represent|missing character:' "$build_dir/build.log" >&2; then
  echo "error: unrepresentable characters above — fix before distributing" >&2
  exit 1
fi
[ -s "$build_dir/paper.pdf" ] || { echo "error: no PDF produced" >&2; exit 1; }
cat "$build_dir/build.log"
mv "$build_dir/paper.pdf" digital-proprioception.pdf
echo "built digital-proprioception.pdf"
