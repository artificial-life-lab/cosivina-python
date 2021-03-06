# cosivina-python

**I am looking for collaborators that would like to work with me to import Cosivina code base from Matlab to python.**

**Contents**
+ [Call for collaboration](#call-for-collaboration)
+ [Installation](#installation)

## Call for collaboration

This is a python library to Compose, Simulate and Visualize Neurodynamic Architectures (COSIVINA).
The approach of constructing dynamic field architectures is described in the book <a href="https://dynamicfieldtheory.org/book" target="_blank"> Dynamic Thinking - A Primer on Dynamic Field Theory</a>.

The original Matlab code can be found at <a href="https://bitbucket.org/sschneegans/cosivina" target="_blank">https://bitbucket.org/sschneegans/cosivina</a>.

The goal is to extend this codebase for other artificial life experiments such as connecting population dynamics to agent evolution and adaptability.

At the moment, I can't devote much time to this project due to my other projects and funding issues, which is quite common of researchers in Artificial Life.
However, I would be very happpy if someone finds this approach interesting and wants to work with me to work on this project.

## Installation

1. Create conda environment
```
conda env create -f environment.yml
```
2. Activate the environment
```
source activate cosivina
```
3. Install momos as a package within environment
```
python install_package.py develop
```
