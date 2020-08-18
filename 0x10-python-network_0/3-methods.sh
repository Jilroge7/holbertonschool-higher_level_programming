#!/bin/bash
# Script to display response of all http methods
curl -sI "$1" | grep Allow | cut --complement -d ' ' -f1
