#/bin/bash

mkdir -p  

echo ''
echo '↓↓↓↓ CHANGE VOLTAGE TO DEGREE↓↓↓↓'
echo ''

for file in $(ls ../*.csv); do
    python3 check.py $file >> ./result.txt
done

echo ''
echo 'FFT COMPLETED!!!'
echo ''
