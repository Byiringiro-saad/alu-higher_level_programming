#!/bin/bash
# Displays all HTTP methods the server accepts
curl -sI "$1" | grep "Allow:" | cut -d' ' -f2-
