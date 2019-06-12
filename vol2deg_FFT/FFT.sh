#/bin/bash

mkdir -p processed

echo ''
echo '↓↓↓↓ CHANGE VOLTAGE TO DEGREE↓↓↓↓'
echo ''

for file in $(ls ../*.csv); do
    python3 change.py $file > ./processed/${file:3}
done


mkdir -p windowed

for file in $(ls processed/*.csv); do
    python3 multiply_window.py $file hamming_window.csv > windowed/${file:10}
done


mkdir -p fouriered

for file in $(ls windowed/*.csv); do
    echo $file
    python3 FFT.py $file > fouriered/${file:9}
done

echo ''
echo 'FFT COMPLETED!!!'
echo ''
