#!/bin/bash
# script that take in a URL as an argument, sends a GET request to the URL, and displays the body of the response
curl -s "$1" -H "X-School-User-Id: 98"