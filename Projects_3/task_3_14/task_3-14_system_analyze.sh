#!/bin/bash

df -h | awk 'NR > 1 {fs=$1; use=$5; gsub(/%/,"",use); printf "Файловая система: %s, заполнена: %s%%\n", fs, use; if(use>90) print "⚠️  ПРЕДУПРЕЖДЕНИЕ: файловая система " fs " заполнена на " use "%!"}'

