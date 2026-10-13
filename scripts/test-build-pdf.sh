#!/usr/bin/env bash
# Regression checks: a failed compiler must never publish a stale or partial PDF.
set -euo pipefail
cd "$(dirname "$0")/.."
mkdir -p .scratch
test_dir=$(mktemp -d .scratch/pdf-build-test.XXXXXX)
trap 'rm -rf "$test_dir"' EXIT
mkdir -p "$test_dir/repo/scripts" "$test_dir/bin"
cp scripts/build-pdf.sh "$test_dir/repo/scripts/"
printf '# Test paper\n' > "$test_dir/repo/paper.md"
cat > "$test_dir/bin/pandoc" <<'STUB'
#!/usr/bin/env bash
set -eu
while [ "$#" -gt 0 ]; do
  if [ "$1" = '-o' ]; then
    output=$2
    break
  fi
  shift
done
case "$PDF_BUILD_TEST_CASE" in
  failure) printf 'partial PDF' > "$output"; echo 'compiler failed' >&2; exit 42 ;;
  glyph) printf 'invalid PDF' > "$output"; echo 'could not represent character' >&2 ;;
  missing) printf 'invalid PDF' > "$output"; echo 'Missing character: unsupported glyph' >&2 ;;
  empty) : > "$output" ;;
  success) printf 'new PDF' > "$output" ;;
esac
STUB
chmod +x "$test_dir/bin/pandoc"
test_bin=$(cd "$test_dir/bin" && pwd)
for test_case in failure glyph missing empty; do
  for previous in absent present; do
    rm -f "$test_dir/repo/digital-proprioception.pdf"
    if [ "$previous" = present ]; then
      printf 'previous PDF' > "$test_dir/repo/digital-proprioception.pdf"
    fi
    if PDF_BUILD_TEST_CASE="$test_case" PATH="$test_bin:$PATH" \
      bash "$test_dir/repo/scripts/build-pdf.sh" > "$test_dir/result.log" 2>&1; then
      echo "FAIL: $test_case was reported as success ($previous PDF)" >&2
      exit 1
    fi
    if [ "$previous" = present ]; then
      [ "$(cat "$test_dir/repo/digital-proprioception.pdf")" = 'previous PDF' ]
    else
      [ ! -e "$test_dir/repo/digital-proprioception.pdf" ]
    fi
  done
done
PDF_BUILD_TEST_CASE=success PATH="$test_bin:$PATH" \
  bash "$test_dir/repo/scripts/build-pdf.sh" > "$test_dir/result.log" 2>&1
[ "$(cat "$test_dir/repo/digital-proprioception.pdf")" = 'new PDF' ]
[ -z "$(find "$test_dir/repo/.scratch" -mindepth 1 -print -quit)" ]
echo 'PASS: 8 failed-build preservation cases, successful replacement, cleanup'
