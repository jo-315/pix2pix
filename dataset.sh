#!/bin/sh

echo "setup dataset"

echo "rename"
# python3 ./rename_file.py

echo "resize"
python3 ./resize.py

echo "get contour"
python3 ./get_contour.py

echo "split data"
python3 ./split_data.py

echo "done"