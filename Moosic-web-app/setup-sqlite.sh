#!/bin/bash
set -euo pipefail

cur_dir="$(dirname "$(readlink -f "${BASH_SOURCE[0]:-.}")")"

main() {
  source "${cur_dir}/.venv/bin/activate"
  rm -f app.db
  flask fab create-db
  flask fab create-admin \
    --firstname Shahi \
    --lastname Winderling \
    --email s.winderling@posteo.de \
    --username shahi \
    --password 'shahi'
}

main "$@"

# vim: ft=sh
