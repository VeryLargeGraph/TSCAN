# Code for TSCAN Algorithm

This repository contains a reference implementation of the algorithm for Mining Stable Communities in Temporal Networks by Density-based Clustering.

## Environment Setup

Codes run on Python 2.7 or later

You may use Git to clone the repository from
GitHub and run it manually like this:

    git clone https://github.com/qinhc/tSCAN.git
    cd tSCAN
    pip install networkx
    pip install click
    python run.py 

## Dateset description
We focus on mining the temporal networks so each edges are associated with a timestamp. Temporal edges are stored at the raw data in which each line is one temporal edge.
 
| from_id | \t  | to_id    | \t  |  timestamps  |
| :----:  |:----: | :----:   |:----:   | :----: |

## Running example
You can type in dataset name, parameters epsilon, tau, miu and method name to control the program:

    Dataset name(str): chess_year
    Epsilon(float): 0.5
    Tau(int): 3
    Miu(int): 3
    Type one number to chose the algorithm: [1]TSCANB; [2]TSACNS; [3]TSCANA. (int): 1
    7301
    55899
    temporal edges:62385.0
    Runing time of SCANB:0.529084
    Cores output at: chess_year.output-0.5-3-3_SCANB

 
