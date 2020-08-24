#!/bin/bash
# Script to get status code only
curl -o /dev/null -s --write-out '%{http_code}' "$1"
