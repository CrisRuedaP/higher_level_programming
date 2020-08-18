#!/bin/bash
#Get the HTTP status code of a URL passed
curl -so "$1"/dev/null -w "%{http_code}" "$1"
