# **
# ** SocialSim: Interactive Mode of social simulation
# **
# ** Author: Roy Dabire
# ** Date:   October 2019


import pickle  # Used to save objects (network state) and reload
import csv  # Used during the file reading process
from GraphsV5 import *  # The main program used to run the methods
import sys  # Used in reading file process
import timeit  # Used to track the time a particular method/function took to execute



def usage():
    print("################### WELCOME ###################")
    print()
    print("To start interactive mode enter:")
    print("python3 SocialSim.py -i\n")
    print("To start simulation mode enter:")
    print("bash SocialSim.sh -s networkfile eventfile prob_like prob_follow timesteps\n")


interactive_mode = False


def Interactive_Mode():
    simulation = SocialSim()
    while interactive_mode is True:
        print("*** Main Menu *** ")
        print("(1) To load the network file\n"
              "(2) To set probabilities\n"
              "(3) User operations(find,add,remove) \n"
              "(4) Edge operations (like/follow - add/remove)\n"
              "(5) New post \n"
              "(6) To display network and statistics\n"
              "(7) Update(run a timestep)\n"
              "(8) Save network \n"
              "(X) To exit")
        choice = input("Selection: ")

        if choice == "1":
            print("*** Which file would you like to load ***")
            print("(1) Default network and event file")
            print("(2) Custom network and event file")
            print("(3) Saved Network")
            print("Press <enter> to return to main menu\n")
            file = input("Selection: ")

            if file == "1":
                try:
                    with open("networkTS1b.csv", "r") as network:
                        reader = csv.reader(network, delimiter=":")  # Sourced from Python Org, section: CSV File
                                                                    # Reading and Writing.
                        print("\n**** Reading Default Network File ****\n")
                        for lines in reader:
                            startTime = timeit.default_timer()
                            if len(lines) == 1:
                                simulation.addPerson(lines[0])
                            elif len(lines) == 2:
                                simulation.Follow(lines[0], lines[1])
                            else:
                                print("Unable to read", "networkTS1b.csv")
                        print()
                        endTime = timeit.default_timer()
                        runningTotal = endTime - startTime
                        print("Run time =", str(runningTotal))

                    with open(str("eventsTS1b.csv"), "r") as events:
                        reader = csv.reader(events, delimiter=":")  # Sourced from Python Org, section: CSV File
                                                                    # Reading and Writing.
                        print("\n**** Reading Default Event File ****\n")
                        for lines in reader:
                            startTime = timeit.default_timer()
                            if lines[0] == "F":
                                simulation.Follow(lines[1], lines[2])
                            elif lines[0] == "A":
                                simulation.addPerson(lines[1])
                            elif lines[0] == "P":  # need to implement the prob
                                if len(lines) == 3:
                                    simulation.Post(lines[1], lines[2], 1)
                                if len(lines) == 4:
                                    simulation.Post_clickbait(lines[1], lines[2], float(lines[3]))
                                if len(lines) > 4:
                                    print("Unable to post", lines[1],
                                          "message. ^Tip the lines should be: p:user:message:clickbait "
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
                except Exception as e:
                    print("Unable to read the file. Check format of file and try again. ^Tip :", e)

            elif file == "2":
                a = str(input("Enter network file name: "))
                b = str(input("Enter event file name: "))
                try:
                    with open(a, "r") as network:
                        reader = csv.reader(network, delimiter=":")  # Sourced from Python Org, section: CSV File
                                                                    # Reading and Writing.
                        print("\n**** Reading", str(a), "Network File ****\n")
                        for lines in reader:
                            startTime = timeit.default_timer()
                            if len(lines) == 1:
                                simulation.addPerson(lines[0])
                            elif len(lines) == 2:
                                simulation.Follow(lines[0], lines[1])
                            else:
                                print("Unable to read line. ^Tip line may be empty")
                        endTime = timeit.default_timer()
                        runningTotal = endTime - startTime
                        print("Run time =", str(runningTotal))

                    with open(b, "r") as events:
                        reader = csv.reader(events, delimiter=":")  # Sourced from Python Org, section: CSV File
                                                                    # Reading and Writing.
                        print("\n**** Reading", b, "Event File ****\n")
                        for lines in reader:
                            startTime = timeit.default_timer()
                            if lines[0] == "F":
                                simulation.Follow(lines[1], lines[2])
                            elif lines[0] == "A":
                                simulation.addPerson(lines[1])
                            elif lines[0] == "P":  # need to implement the prob
                                if len(lines) == 3:
                                    simulation.Post(lines[1], lines[2], 1)
                                if len(lines) == 4:
                                    simulation.Post_clickbait(lines[1], lines[2], float(lines[3]))
                                if len(lines) > 4:
                                    print("Unable to post", lines[1],
                                          "message. ^Tip the lines should be: p:user:message:clickbait "
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
                except Exception as e:
                    print("Unable to read the file. Check format of file and try again. ^Tip :", e)

            elif file == "3":
                a = str(input("Enter network file name: "))
                try:
                    with open(a, "rb") as PickleFile:
                        Loaded_object = pickle.load(PickleFile)
                        simulation = Loaded_object
                except Exception as e:
                    print("Unable to read the file. Check format of file and try again. ^Tip :", e)
                print()

        elif choice == "2":
            print("*** Setting Network Probabilities ***")
            a = input("Enter like probability (e.g. 10 represents 10%): ")
            b = input("Enter follow probability after a like: ")
            c = input("Enter dislike probability: ")
            d = input("Enter clickbait factor (^Tip enter 1 if unsure): ")
            print("Press <enter> to return to main menu\n")
            simulation.set_probabilities(a, b, c, d)

        elif choice == "3":
            print("*** Which user operation would you like to carry out ***")
            print("(1) Add\n"
                  "(2) Find\n"
                  "(3) Remove\n")
            print("Press <enter> to return to main menu\n")
            UserOp = input("Selection: ")

            if UserOp == "1":
                simulation.addPerson(str(input("Enter user name: ")))
                print()
            elif UserOp == "2":
                simulation.find(str(input("Enter user you are looking for: ")))
                print()
            elif UserOp == "3":
                simulation.delete_user(str(input("Enter user you would like to remove: ")))
                print()

        elif choice == "4":
            print("*** Which edge operation would you like to carry out ***")
            print("(1) Like a post\n"
                  "(2) Unlike a post\n"
                  "(3) Follow a user\n"
                  "(4) Unfollow a user\n")
            print("Press <enter> to return to main menu\n")
            edgeOp = input("Selection: ")

            if edgeOp == "1":
                print("*** Post likes ***")
                print("Press <enter> to return to main menu\n")
                a = input("Enter the user name that will like the post: ")
                b = input("Enter the user name that will receive the like: ")
                c = input("Enter the postId number for the post: ")
                simulation.like_post(a, b, c)

            elif edgeOp == "2":
                print("*** Post unlikes ***")
                print("Press <enter> to return to main menu\n")
                a = input("Enter the user name that will unlike the post: ")
                b = input("Enter the user name that will receive the unlike: ")
                c = input("Enter the postId number for the post: \n")
                simulation.unlike_post(a, b, c)

            elif edgeOp == "3":
                print("*** Following a user ***")
                print("Press <enter> to return to main menu: ")
                a = input("Enter the user name that will action the follow: ")
                b = input("Enter the user name that will receive the follow: ")
                simulation.Follow(a, b)

            elif edgeOp == "4":
                print("*** Unfollowing a user ***")
                print("Press <enter> to return to main menu\n")
                a = input("Enter the user name that will action the unfollow: ")
                b = input("Enter the user name that will receive the unfollow: ")
                simulation.unFollow(a, b)

        elif choice == "5":
            print("*** New Post ***")
            print("Press <enter> to return to main menu\n")
            a = input("Enter the user name: ")
            b = input("Enter the message: ")
            c = input("Enter clickbait factor ^If unsure enter 1: ")
            simulation.Post(a, b, c)
            print()

        elif choice == "6":
            print("*** Network and User Statistics ***")
            print("(1) Display Network\n"
                  "(2) Display Network Statistics\n"
                  "(3) Display User Statistics\n"
                  "(4) Display Popularity\n")
            print("Press <enter> to return to main menu\n")
            NetOp = input("Selection: ")

            if NetOp == "1":
                simulation.displayNetwork()
                print()
            elif NetOp == "2":
                simulation.network_statistics()
            elif NetOp == "3":
                a = input("Enter user name: ")
                simulation.UserStatistics(a)
            elif NetOp == "4":
                simulation.Populararity()
            else:
                print("Invalid input")

        elif choice == "7":
            new_network = SocialSim()
            print("*** Running Timesteps *** \n")
            a = int(input("Enter number of timesteps: "))
            simulation.run_timesteps(a)

        elif choice == "8":
            with open("SavedNetwork", "wb") as PickleFile:
                pickle.dump(simulation, PickleFile)
            print("\n **** Network has been saved **** \n")

        elif choice == "X".lower():
            print("Thank you and Goodbye!\n")
            break

        else:
            print("Invalid input")
            print()


if len(sys.argv) < 2:
    usage()

elif sys.argv[1] == "-i":
    interactive_mode = True
    try:
        Interactive_Mode()
    except Exception as e:
        print("Error in running interactive mode. ^Tip: ", e)
else:
    print("\n*** Invalid input ***\n")
    usage()
