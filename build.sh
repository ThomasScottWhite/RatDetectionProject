#!/bin/bash

# Build the executable using PyInstaller
pyinstaller main.py --add-data "/home/thomas/miniforge3/envs/DEEPLABCUT/lib/python3.10/site-packages/deeplabcut:deeplabcut"
rm -rf dist/main/_internal/libcudnn_graph.so.9
# Optional: Clean up the build files and dist folder
# Uncomment the next lines if you want to clean up after building
#rm -rf build
#rm -rf dist
#rm -f main.spec

echo "Build completed!"
