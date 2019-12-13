# **
# ** Unit Test Harness to test SocialSim class too see if all methods respond as it should
# **
# ** Author: Roy Dabire
# ** Date:   October 2019


from GraphsV5 import *
#Test harness inspired by Valerie's test harness from practical 2 
numPassed = 0
numTests = 0
g = SocialSim()
print("\n**** Unit Tests for SocialSim class ****\n")
print()
print("*** Creating the network and adding people ***")
print()
try:
    numTests += 1
    g.addPerson("Alpha")
    g.addPerson("Bravo")
    g.addPerson("Charlie")
    g.addPerson("Delta")
    g.addPerson("Echo")
    g.addPerson("Foxtrot")
    g.addPerson("Golf")
    g.addPerson("Hotel")
    numPassed += 1
    print("Passed")
except:
    print("Failed")
print()
print("##############################################")
print("**** Setting network probabilities ****")
try:
    numTests += 1
    g.set_probabilities(60, 30, 15, 1)
    numPassed += 1
    print("Passed")
except:
    print("Failed\n")
print()

print("##############################################")
print("**** Testing how program handles adding duplicate users ****")
print()
try:
    numTests += 1
    g.addPerson("Alpha")
    numPassed += 1
    print("Passed")
except:
    print("Failed")

print("##############################################")
print("**** Testing finding users ****")
print()
try:
    numTests += 1
    g.find("Alpha")
    numPassed += 1
    print("Passed")
except:
    print("Failed")
print()

print("##############################################")
print("**** Testing how program handles non-existent users ****")
try:
    numTests += 1
    g.find("Zulu")
    numPassed += 1
    print("Passed")
except:
    print("Failed")
print()

print("##############################################")
print("Testing posting")
try:
    numTests += 1
    g.Post("Alpha", "hello world", 1)
    g.Post("Bravo", "Trial by stone!", 1)
    g.Post("Bravo", "Have a look at the following example...", 1)
    g.Post("Charlie", "I don't believe that man's ever been to medical school!", 1)
    g.Post("Echo", "This is an intergalactic emergency. I need to commandeer your vessel to Sector 12. Who's in "
                   "charge here?.", 1)
    g.Post("Alpha", "The claw chooses who will go and who will stay.", 1)
    numPassed += 1
    print("Passed")
except:
    print("Failed")
print()

print("##############################################")
print("**** Testing removing posts ****")
try:
    numTests += 1
    g.remove_post("Bravo", "6")
    numPassed += 1
    print("Passed")
except:
    print("Failed")
print()

print("##############################################")
print("**** Testing how program handles duplicate post removal ****\n")
try:
    numTests += 1
    g.remove_post("Bravo", "3")
    numPassed += 1
    print("Passed")
except:
    print("Failed")
print()

print("##############################################")
print("**** Testing seeing all posts ****")
print()
try:
    numTests += 1
    g.See_Posts("Alpha")
    print()
    g.See_Posts("Bravo")
    print()
    g.See_Posts("Charlie")
    print()
    g.See_Posts("Echo")
    numPassed += 1
    print("Passed")
except:
    print("Failed")

print("##############################################")
print("**** Testing seeing specific post by postId number ****")
print()
try:
    numTests += 1
    g.See_SpecificPost("Alpha", "1")
    numPassed += 1
    print("Passed")
except:
    print("Failed")
print()

print("##############################################")
print("**** Testing Follow ****")
print()
try:
    numTests += 1
    g.Follow("Alpha", "Bravo")
    g.Follow("Bravo", "Alpha")
    g.Follow("Bravo", "Charlie")
    g.Follow("Charlie", "Delta")
    g.Follow("Charlie", "Alpha")
    g.Follow("Echo", "Alpha")
    g.Follow("Echo", "Bravo")
    g.Follow("Foxtrot", "Bravo")
    g.Follow("Golf", "Bravo")
    g.Follow("Hotel", "Bravo")
    numPassed += 1
    print("Passed")
except:
    print("Failed")
print()

print("##############################################")
print("**** Testing how program handles duplication followers ****")
print()
try:
    numTests += 1
    g.Follow("Charlie", "Delta")
    numPassed += 1
    print("Passed")
except:
    print("Failed")
print()

print("##############################################")
print("**** Testing followers list ****")
print()
try:
    numTests += 1
    g.List_of_followers("Alpha")
    print()
    g.List_of_followers("Charlie")
    numPassed += 1
    print("Passed")
except:
    print("Failed")
print()

print("##############################################")
print("**** Testing unfollow ****")
print()
try:
    numTests += 1
    g.List_of_followers("Alpha")
    print()
    g.unFollow("Echo", "Alpha")
    print()
    g.List_of_followers("Alpha")
    print()
    numPassed += 1
    print("Passed")
except:
    print("Failed")

print("##############################################")
print("**** Testing how program handles duplication unfollows ****")
print()
try:
    numTests += 1
    g.unFollow("Echo", "Alpha")
    numPassed += 1
    print("Passed")
except:
    print("Failed")
print()

print("##############################################")
print("**** Testing manual likes ****")
try:
    numTests += 1
    print()
    g.like_post("Bravo", "Alpha", "1")
    print()
    g.like_post("Charlie", "Alpha", "1")
    print()
    g.like_post("Delta", "Alpha", "1")
    print()
    g.like_post("Echo", "Bravo", "2")
    print()
    g.like_post("Charlie", "Bravo", "2")
    print()
    g.like_post("Bravo", "Alpha", "5")
    numPassed += 1
    print("Passed")
except:
    print("Failed")
print()

print("##############################################")
print("**** Testing total for specific user likes ****")
print()
try:
    numTests += 1
    g.likeTotal("Alpha", "1")
    print()
    g.likeTotal("Bravo", "2")
    print()
    g.likeTotal("Charlie", "3")
    numPassed += 1
    print("Passed")
except:
    print("Failed")
print()

print("##############################################")
print("**** Testing manual unlikes ****")
print()
try:
    numTests += 1
    g.likeTotal("Alpha", "1")
    print()
    g.unlike_post("Bravo", "Alpha", "1")
    print()
    g.likeTotal("Alpha", "1")
    numPassed += 1
    print("Passed")
except:
    print("Failed")
print()

print("##############################################")
print("**** Testing how program handles duplication unlikes ****")
print()
try:
    numTests += 1
    g.unlike_post("Bravo", "Alpha", "1")
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
    g.displayNetwork()
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
    g.UserStatistics("Alpha")
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
    g.network_statistics()
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
    g.Populararity()
    numPassed += 1
    print("Passed")
except:
    print("Failed")

# Print test summary
print("\nNumber PASSED: ", numPassed, "/", numTests)
print("-> ", numPassed/numTests*100, "%\n")
