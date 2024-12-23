#!/bin/zsh

year=$1 day=$2
lang=py
root=~/aoc
inputlink=https://adventofcode.com/${year}/day/${day}/input
inputfile=${root}/${year}/${day}-input.txt
codefile=${root}/${year}/${lang}/${day}-code.${lang}
templatefile=${root}/template.${lang}

[[ -f ${templatefile} ]] || { echo "${templatefile}: not found" && exit 1; }
[[ -z ${AOC_SESSION} ]] && { echo "no session cookie found" && exit 1; }

mkdir -p ${codefile:h} ${inputfile:h}
[[ -f ${inputfile} ]] || curl --cookie ${AOC_SESSION} ${inputlink}  > ${inputfile}
[[ -f ${codefile} ]] || cp ${templatefile} ${codefile}

export inputfile
$EDITOR ${codefile} ${inputfile}
