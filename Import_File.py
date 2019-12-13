# **
# ** Unit Test Harness to test file imports into the SocialSim and timesteps
# **
# ** Author: Roy Dabire
# ** Date:   October 2019

from GraphsV5 import *  # The main program used to run the methods
import csv  # Used during the file reading process
import timeit  # Used to track the time a particular method/function took to execute

simulation = SocialSim()


def Network_fileIO(filename):
    with open(str(filename), "r") as network:
        reader = csv.reader(network, delimiter=":")   # Sourced from Python Org, section: CSV File Reading and Writing.

        for lines in reader:
            startTime = timeit.default_timer()
            print("##############################################")
            if len(lines) == 1:
                simulation.addPerson(lines[0])
            elif len(lines) == 2:
                simulation.Follow(lines[0], lines[1])
            else:
                print("Unable to read", filename)
        print()
        endTime = timeit.default_timer()
        runningTotal = endTime - startTime
        print("Run time =", str(runningTotal))


def Events_fileIO(filename):
    with open(str(filename), "r") as network:
        reader = csv.reader(network, delimiter=":")   # Sourced from Python Org, section: CSV File Reading and Writing.
        for lines in reader:
            startTime = timeit.default_timer()
            print("##############################################")
            if lines[0] == "F":
                simulation.Follow(lines[1], lines[2])

            elif lines[0] == "A":
                simulation.addPerson(lines[1])

            elif lines[0] == "P":  # need to implement the prob
                if len(lines) == 3:
                    simulation.Post(lines[1], lines[2], 1)
                if len(lines) == 4:
                    simulation.Post(lines[1], lines[2], float(lines[3]))
                if len(lines) > 4:
                    print("Unable to post", lines[1], "message. ^Tip the lines should be: p:user:message:clickbait "
                                                      "factor")
            elif lines[0] == "U":
                simulation.unFollow(lines[1], lines[2])

            elif lines[0] == "R":
                simulation.delete_user(lines[1])

            else:
                print("Unable to read line. ^Tip line may be empty")
        print()
        endTime = timeit.default_timer()
        runningTotal = endTime - startTime
        print("Run time =", str(runningTotal))



numPassed = 0
numTests = 0

print("##############################################")
print("**** Setting network probabilities ****")
try:
    numTests += 1
    simulation.set_probabilities(60, 30, 15, 1)
    numPassed += 1
    print("Passed")
except:
    print("Failed\n")
print()

print("##############################################")
print("**** Testing file import  ****")
print()
try:
    numTests += 1
    print("********************* Network Simulation ********************* \n")
    Network_fileIO("networkTS1b.csv")
    print("********************* Events Simulation ********************* \n")
    Events_fileIO("eventsTS1b.csv")
    numPassed += 1
    print("Passed")
except:
    print("Failed")

print("##############################################")
print("**** Testing timesteps  ****")
print()
try:
    numTests += 1
    simulation.run_timesteps(10)
    numPassed += 1
    print("Passed")
except:
    print("Failed")
print()

print("##############################################")
print("**** Displaying the network ****")
print()
try:
    numTests += 1
    simulation.displayNetwork()
    numPassed += 1
    print("Passed")
except:
    print("Failed")
print()

print("##############################################")
print("**** Testing User Statistics ****")
print()
try:
    numTests += 1
    simulation.UserStatistics("Alpha")
    numPassed += 1
    print("Passed")
except:
    print("Failed")
print()

print("##############################################")
print("**** Testing Network Statistics ****")
print()
try:
    numTests += 1
    simulation.network_statistics()
    numPassed += 1
    print("Passed")
except:
    print("Failed")
print()

print("##############################################")
print("**** Testing Popularity  ****")
print()
try:
    numTests += 1
    simulation.Populararity()
    numPassed += 1
    print("Passed")
except:
    print("Failed")

# Print test summary
print("\nNumber PASSED: ", numPassed, "/", numTests)
print("-> ", numPassed / numTests * 100, "%\n")
