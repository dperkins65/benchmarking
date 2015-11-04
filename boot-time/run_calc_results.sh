#!/bin/bash

for dir in ./boottimes-*/
do
  dir=${dir%*/}  
  echo "Processing directory ${dir##*/}..." 
  python calc_results.py -d $dir -o ${dir##*/}.csv
done

