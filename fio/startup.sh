#!/bin/bash

export PATH="/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:/usr/games:/usr/local/games"

while true; do
    rm evict randread spike
    export RUNTIME=$(((RANDOM % 570) + 30))
    export WIOPS=$((((RANDOM % 9) + 1) * 100))
    export RIOPS=$((((RANDOM % 4) + 1) * 100))
    export SDELAY=$(((RANDOM % 180 ) + 180))
    export SIOPS=$((((RANDOM % 4 ) + 1) * 1000))
    fio workload.fio
    sleep $(((RANDOM % 270) + 30))
done
