#!/bin/sh

echo "start setup.sh"

# create folder
echo "create ./chainer-pix2pix/generate_tmp folder"
mkdir -p ./chainer-pix2pix/generate_tmp

echo "create ./images folder"
mkdir -p ./images
mkdir -p ./images/canny
mkdir -p ./images/generate
mkdir -p ./images/original
mkdir -p ./images/resized
mkdir -p ./images/test/base
mkdir -p ./images/test/label
mkdir -p ./images/train/base
mkdir -p ./images/train/label

echo "create ./results folder"
mkdir -p ./results
mkdir -p ./results/generate/preview
mkdir -p ./results/npz
mkdir -p ./results/preview

echo "complete setup.sh"