#!/bin/bash
# Script to post parameters and display the body response
curl -s --data "email=hr@holbertonschool.com&subject=I will always be here for PLD" "$1"
