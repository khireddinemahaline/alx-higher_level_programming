#!/bin/bash
# script display the status code of url
curl -s -o /dev/null -w "%{http_code}" "$1"
