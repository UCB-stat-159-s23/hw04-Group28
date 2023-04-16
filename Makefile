# This is the makefile to build a jupyterbook for the repo. 



## clean - target to clean up all the build files
.PHONY: clean
clean:
    rm -rf figures
    rm -rf audio 
    rm -rf _build/html/
    rm -rf _build

## html - to build the jupyterbook
.PHONY: html
html:
    jupyter-book build .
    
## env - creates a conda environment
# uses oneshell command to allow for all lines in an operation to be run in one bash shell
.ONESHELL:
SHELL = /bin/bash

env :
    source /srv/conda/etc/profile.d/conda.sh
    conda env create -f environment.yml 
    conda activate notebook
    conda install ipykernel
    python -m ipykernel install --user --name make-env --display-name "IPython - Make"
