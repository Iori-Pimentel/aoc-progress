#!/bin/bash

[[ -z $AOC_COOKIE ]] && echo 'error: $AOC_COOKIE is empty' >&2 && exit 1

CURL_ARGS=(
	--cookie "${AOC_COOKIE}"
	--fail --fail-early
	--parallel --create-dirs --skip-existing
	'https://adventofcode.com/[2015-2024]/day/[1-25]/input'
	--output 'inputs/#1-#2.txt'
)
curl "${CURL_ARGS[@]}"
