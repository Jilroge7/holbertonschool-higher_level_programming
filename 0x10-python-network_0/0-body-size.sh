#!/usr/bin/env bash
# Script to takes a url, send request to it, and get body size in return.
URL = $1

curl "$URL" | grep Content-Length
