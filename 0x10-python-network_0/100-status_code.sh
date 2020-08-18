#!/bin/bash
#Get the HTTP status code of a URL passed
curl -w %{http_code} -s -o /dev/null $1
