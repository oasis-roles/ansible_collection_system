#!/bin/bash

set -euo pipefail

echo "--- starting tests.."

cd ../ansible_collections/oasis_roles/system

echo "--- here we are:"

pwd

echo "+++ :one-does-not-simply: lets go!"

tox -e roles-hostname-default
