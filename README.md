# Animal Inference Project

This is a wrapper for DeepLabCut which allows the user to inference over videos of animals using SuperAnimal models

# Installation
You need anaconda(https://www.anaconda.com/download) or miniforge (https://github.com/conda-forge/miniforge) installed to run this program.

You should be able to download and create a conda environment using these commands  

git clone https://github.com/ThomasScottWhite/RatDetectionProject.git  
cd RatDetectionProject  
conda env create -f DEEPLABCUT.yaml  

once the files are downloaded and the conda environment is created you should be able to open the gui with the following commands  

conda activate DEEPLABCUT   
python main.py  