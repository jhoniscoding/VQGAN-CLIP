#!/bin/bash

# Usage: ./make.sh 'Storybook illustration' 5 

TEXT=$1
NUM_IT=$2
SIZE=600
APE="ape.png"
APEG="apeg.png"
LION="lion.jpg"


function generate {
    echo "Generating NFT from $1..."
    python generate.py -o ../fury_fda-labs-playground/output-$1 -i $NUM_IT -se $NUM_IT -ii samples/$1 -cutm original -cuts 128 -p "$TEXT" -s $SIZE $SIZE
    echo "Generating NFT from $1... Done"
}

generate $LION
generate $APE
generate $APEG
