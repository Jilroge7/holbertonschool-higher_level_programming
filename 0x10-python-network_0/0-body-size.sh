#!/usr/bin/bash
# Script to takes a url, send request to it, and get body size in return.
curl -sI "$1" | grep Content-Length | cut --complement -d ' ' -f1
