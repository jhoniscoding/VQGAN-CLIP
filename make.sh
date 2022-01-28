#!/bin/bash

# Usage: ./make.sh 'Storybook illustration' 5 

# Args
TEXT=$1
NUM_IT=$2

# Configs
SIZE=600
PROJECT_PATH="../fury_fda-labs-playground"

# Sample images
APE="ape.png"
APEG="apeg.png"
LION="lion.jpg"
APEN1="ney1.png"
APEN2="ney2.png"
CHART="chart.png"


function generate {
    echo "Generating $1 NFT $2..."
    python generate.py -o ./outputs/$2 -i $NUM_IT -se $NUM_IT -ii $PROJECT_PATH/samples/$1 -cutm original -cuts 128 -p "$TEXT" -s $SIZE $SIZE
    echo "Generating NFT from $1... Done"
}

#generate $LION
for i in {1..2}
do
   generate $APEN1 $i
   generate $APEN2 $(($i+2))
done

