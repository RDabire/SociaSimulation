# SociaSimulation
Data Structure and Algorithm Project 

GraphsV5.py - Main program containing all classes and methods used in running the interactive and simulation mode of program

Heap_test.py - Unit test for Heap python program

Heaps.py - Python program imported into GraphsV5 for heap sort algorithm

Import_File.py - Code for handling file reading for import, also contains test unit for file import 

LinkedList.py - Python program imported into GraphsV5 for Linked list data structure 

LinkedList_Test.py - Unit test for linked list program

Project_TestHarnss.py - Unit test Harness for the GraphsV5.py program to handle 23 tests. To run the test user should input the following on the command line: python3 Project_TestHarnss.py

SocialSim.py - The interactive mode of the program. Imports from GraphsV5.py all classes and methods. To run the interactive mode user should input on the command line: python3 SocialSim.py -i

SocialSim_SimulationMode.py - The simulation mode of the program. To run this mode user should input on the command line: bash SocialSim.sh -s <networkfilename> <eventfilename> <prob_like> <prob_follow> <timesteps>

SocialSim.sh - Driver script for parameter sweep

TheDarkCrystal_Event, TheDarkCrystal_Network, networkTS1b, eventsTS1b - Network and event file names that can be loaded onto the program via interactive mode or inputed on the command line for the simulation mode. Ensure to only input the matching pairs 

UML - UML class diagram used in planning the program

## Dependencies
Numpy
Python version 3
Matplotlib.pyplot
Random
Os
Psutil
Timeit 
CSV
Pickle

## Version information
<27/10/2019> - Final version for submission
