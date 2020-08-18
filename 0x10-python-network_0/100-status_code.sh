#!/bin/bash
# Get the HTTP status code of a URL passed
curl -so /dev/null -w "%{http_code}" "$1"
