# Mars Rover Problem

This repository contains a program that takes in commands and moves one or more robots around Mars.  

The program was written in Python 3.8.8. To run the program, ensure you have Python 3 installed on your machine.

## Instructions

1. Clone the repo using:

`git clone git@github.com:karolinelende/mars-rover-kl.git`

2. Using the command line editor of your choice, navigate to the folder where the repo is cloned and run the following command:

`python mars-rover.py`

3. You will now be prompted for a series of inputs.

    * First, enter the grid size of Mars as two integers separated by a space. Example input: `4 8`.

    * Then, enter the initial position of your first robot as two integers and an orientation. The orientation should be a letter, either `N`, `E`, `S` or `W`. Example input: `2 3 E`.

    * Now enter the series of movement commands for your robot. The available commands are `F` (forward), `R` (turn right) or `L` (turn left). Example input: `LFRFF`.

4. The final position of your robot will be printed. To enter the inital position and commands for another robot, press return. To end the program, hit `x` then return.