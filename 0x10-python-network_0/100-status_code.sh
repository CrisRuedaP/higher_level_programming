#!/bin/bash
# Get the HTTP status code of a URL passed
curl "$1" -sI -o /dev/null -w "%{http_code}"
