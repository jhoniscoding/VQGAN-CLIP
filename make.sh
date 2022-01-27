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


function generate {
    echo "Generating NFT from $1..."
    python generate.py -o $PROJECT_PATH/outputs/$1 -i $NUM_IT -se $NUM_IT -ii $PROJECT_PATH/samples/$1 -cutm original -cuts 128 -p "$TEXT" -s $SIZE $SIZE
    echo "Generating NFT from $1... Done"
}

#generate $LION
#generate $APE
#generate $APEG
generate $APEN1
generate $APEN2
