# Tic-Tac-Toe-Simulation
A project where the user simulates a set of x games in 2D or 3D tic tac toe. As a part of the summer course DA 2005 we had to make a project and I choose to do a simulation of Tic-Tac-Toe. There are two files, basic.py and adv.py. These two code files will be uploaded once the exercises has been graded as I do not want to get into trouble in case someone takes this project before grading. The result was in line with what one could have suspected, to dominate the center is a solid strategy it turns out. It also turns out that being player one does have an advantage but that advantage is diminishing as the board is growing its dimensions. 

## The Project
This is a project in two parts, part I is in basic.py and part II in adv.py. In part one we will be simulating a number of tic-tac-toe games where we will be storing how many times a winner wins. There are two scenarios, scenario 1 is that the two players play totally randomly. Scenario 2 is that player one will start in the center and thereafter the two will play randomly. There is also the issue of how many dimensions the board should be of. The goal of this project was then to examine if player one did have an advantage from starting as well as examing how much scenario 2 would impact this as well as how much larger boards would impact the chances of player 1 winning.

For the advanced part of the project, adv.py, we extended tic-tac-toe to 3D space meaning that we can have cases of three in a row in an inclinational space. This was fairly tricky to implement at first but once you understand the logic of 3D-tic-tac-toe it is not that difficult. All that needs to be understood is that there are for each matching case in regular tic-tac-toe and additional 2 matches, taking into consideration the two inclinational cases in which one can find three in a row.

## Modules
All the modules are from the standard package aside from the matplot lib package, which is used to draw up graphs of which player has won. This module may have to be downloaded in order to try this simulation. 
