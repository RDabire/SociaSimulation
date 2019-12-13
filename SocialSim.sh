#
# SocialSim.sh: Paramater Sweep for simulation 
#		Creates a directory for the experiment 
#		processes the command line arguments
#		then has loops to go through the paramaters
#

#!/bin/bash

SocialSim_dir="Simulation"`date "+%Y-%m-%d_%H:%M:%S"`

mkdir $SocialSim_dir
cp SocialSim.py $SocialSim_dir
cp SocialSim_SimulationMode.py $SocialSim_dir
cp GraphsV5.py $SocialSIm_dir
cp LinkedList.py $SocialSim_dir
cp Heaps.py $SocialSim_dir
cp networkTS1b.csv $SocialSim_dir
cp eventsTS1b.csv $SocialSim_dir
cp TheDarkCrystal_Event.csv $SocialSim_dir
cp TheDarkCrystal_Network.csv $SocialSim_dir
cd $SocialSim_dir

echo "**** Parameters ****"
echo "Network file: " $2
echo "Event file: " $3
echo "Probability of a like: " $4
echo "Probability of a follow: " $5
echo "Number of timesteps: "$6

for t in $6
do
    for f in $5;
    do
        for l in $4;
        do
            for e in $3;
            do 
                for n in $2;
                do
                    echo "*** Runninning paramater sweep ***"
                    outfile="simulation_network"$2".txt"
                    python3 SocialSim_SimulationMode.py $2 $3 $4 $5 $6 > $outfile
                done
            done
        done
    done
done   






