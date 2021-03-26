#!/bin/bash

set -euo pipefail

cd ../ansible_collections/oasis_roles/system

tox -e roles-hostname-default
