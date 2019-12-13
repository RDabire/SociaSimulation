# **
# ** ** SocialSim_SimulationMode.py: Simulation mode. Copied from GraphsV5. Bash script kept crashing when running by
#                          import. To avoid crashing the code, the whole program was copied onto the simulation directly
# ** Author: Roy Dabire
# ** Date:   October 2019

import pickle  # Used to save objects (network state) and reload. Sourced from practical 3
import csv  # Used during the file reading process
import random  # Used to calculate probabilities
from LinkedList import *  # Used throughout to store nodes
from Heaps import *  # Used in popularity method
import matplotlib.pyplot as plt  # Used for plotting features
import sys  # Used for command line arguments
import timeit  # Used to track the time a particular method/function took to execute sourced from python org
import os  # Used in memory usage package
import psutil  # Package to calculate memory usage sourced from python org


#LinkedList from Practical 3 used throughout class
class SocialSim:

    def __init__(_self):
        _self.SocialSim = LinkedList()
        _self.numPeople = 0
        _self.postId = 1

        _self.totalposts = LinkedList()
        _self.total_posts = 0

        _self.total_likes_given = 0
        _self.likeswithoutclickbait = 0
        _self.likeswithclickbait = 0

        _self.total_followed = 0
        _self.clickbaitfollowed = 0

        _self.likeprobability = 0
        _self.followprobability = 0
        _self.dislikeprobability = 0
        _self.clickbaitfactor = 1

    def addPerson(self, name):
        new_person = User(name)
        if not self._person_exist(name):
            self.SocialSim.insertFirst(new_person)
            print(new_person.name, " has been added")
            self.numPeople += 1
        else:
            print("Username has already been taken. ^Tip use: ", name, random.randint(0, 1000))
        print()

    def delete_user(self, person):
        v1 = self._getPerson(person)
        if not self._person_exist(person):
            print(person, "does not exist. ^Tip check spelling of name")

        else:
            for users in self.SocialSim:
                if users == v1:
                    self.SocialSim.removeMiddle(users)
                    self.numPeople -= 1
                    print(person, "has been removed from the social network")

    def find(self, user):
        v1 = self._getPerson(user)
        if not self._person_exist(user):
            print(user, "does not exist. ^Tip check spelling of name")
        else:
            for users in self.SocialSim:
                if users == v1:
                    print(user, "is in the network")

    def _person_exist(self, name):
        exist = False
        for item in self.SocialSim:
            if item.name == name:
                exist = True
        return exist

    def _getPerson(self, person):
        for item in self.SocialSim:
            if item.name == person:
                return item

    def Follow(self, person1, person2, show=True):
        if not self._person_exist(person1):
            print(person1, "does not exist to be able to action a follow. ^Tip check spelling of name")
        elif not self._person_exist(person2):
            print(person2, "does not exist to be able to action a follow. ^Tip check spelling of name")

        elif self._alreadyfollowing(person1, person2) is True:
            if show is True:
                print(person1, "already following", person2)

        else:
            v1 = self._getPerson(person1)
            v2 = self._getPerson(person2)
            v1._addFollow(v2)
            v2._addFollower(v1)
            self.total_followed += 1
            if show is True:
                print(person1, "is following", person2)
        print()

    def _alreadyfollowing(self, person1, person2):
        alreadyfollowing = False
        v1 = self._getPerson(person1)
        v2 = self._getPerson(person2)

        for i in v1._check_following():
            if i == v2:
                alreadyfollowing = True
        return alreadyfollowing

    def unFollow(self, person1, person2):
        v1 = self._getPerson(person1)
        v2 = self._getPerson(person2)
        if not self._person_exist(person1):
            print("Cannot unfollow as", person1, "does not exist ^Tip check spelling of name")
        elif not self._person_exist(person2):
            print("Cannot unfollow as", person2, "does not exist ^Tip check spelling of name")

        elif v1._emptyFollowing():
            print(person1, "is not following anyone")

        elif self._alreadyUnfollowed(person1, person2) is True:
            print("Unable to unfollow as", person1, "does not follow", person2, "^Tip check spelling of name")

        else:
            v1._removeFollow(v2)
            v2._removeFollowers(v1)
            print(person1, "unfollowed", person2)

    def _alreadyUnfollowed(self, person1, person2):
        alreadyUnfollowed = True
        v1 = self._getPerson(person1)
        v2 = self._getPerson(person2)

        for i in v1._check_following():
            if i == v2:
                alreadyUnfollowed = False
        return alreadyUnfollowed

    def List_of_followers(self, person):
        v1 = self._getPerson(person)
        if not self._person_exist(person):
            print(person, "does not exist. ^Tip check spelling of name")
        else:
            v1._list_followers()

    def List_of_following(self, person):
        v1 = self._getPerson(person)
        if not self._person_exist(person):
            print(person, "does not exist. ^Tip check spelling of name")
        else:
            for i in self.SocialSim:
                if v1 in i.follower_list:
                    print(person, "follows", i.name)
            print(person, "follows a total of:", v1.totalFollowing, "user")

    def set_probabilities(self, like, follow, dislike, clickbait):
        self.likeprobability = float(like) / 100
        self.followprobability = float(follow) / 100
        self.dislikeprobability = float(dislike) / 100
        self.clickbaitfactor = int(clickbait)
        print("Probabilities of liking a post set to: ", self.likeprobability)
        print("Probability of following a user after liking a post set to: ", self.followprobability)
        print("Probabilities of disliking a post set to: ", self.dislikeprobability)
        print("Clickbait factor set to: ", self.clickbaitfactor)

    def Post(self, person, message, clickbait):
        if not self._person_exist(person):
            print(person, "does not exist to be able to action a post. ^Tip check spelling of name\n")

        else:
            v1 = self._getPerson(person)
            clickbaitFactor = float(clickbait)
            post = Post(v1, message, self.postId, clickbaitFactor)
            v1._add_post_ToUserList(post)
            self.totalposts.insertFirst(post)
            print(person, "has just posted....", "postId number is:", self.postId, "Clickbait factor is:",
                  post.clickbait)
            self.postId += 1
            self.total_posts += 1
            for people in v1._getFollowers():
                self._like_post(people.name, post.postId)
                if post.clickbait == 1:
                    self.likeswithoutclickbait += 1
                elif post.clickbait > 1:
                    self.likeswithclickbait += 1

    def remove_post(self, person, postId):
        v1 = self._getPerson(person)
        if not self._person_exist(person):
            print(person, "does not exist to be able to action a post. ^Tip check spelling of name\n")

        elif self._postExistence(person, postId) is False:
            print("Post with postId: ", postId, "does not exist. ^Tip check postId number\n")

        else:
            for i in v1._getPosts():
                if i.postId == int(postId):
                    v1._removing_post(i)
            print("PostId:", postId, "posted by", person, "has been removed")

    def _postExistence(self, person, postId):
        v1 = self._getPerson(person)
        exist = False
        for i in v1._getPosts():
            if i.postId == int(postId):
                exist = True
        return exist

    def See_Posts(self, person):
        v1 = self._getPerson(person)
        if not self._person_exist(person):
            print(person, "does not exist to be able to action a post. ^Tip check spelling of name\n")

        elif v1._emptyPosts() is True:
            print(person, "has not posted yet\n")
        else:
            posts = v1._getPosts()
            for i in posts:
                with open('User Posts.txt', 'w') as f:
                    print(i.user.name, "postId number", i.postId, ":", i.message, file=f)  # Sourced from Python Org,
                    # section: Input and Output.
                f.close()

    def See_SpecificPost(self, person, postId):
        v1 = self._getPerson(person)
        if not self._person_exist(person):
            print(person, "does not exist. ^Tip check spelling of name\n")

        elif v1._emptyPosts() is True:
            print(person, "has not not posted yet")

        else:
            for i in v1._getPosts():
                if i.postId == int(postId):
                    print(person, "postId number", postId, ":", i.message)

    def _like_post(self, user, postId, show=True):
        if not self._person_exist(user):
            print(user, "does not exist. ^Tip check spelling of name\n")

        elif self._alreadyLiked(user, postId) is True:
            print(user, "has already liked postId:", postId, "\n")

        else:

            v1 = self._getPerson(user)
            for posts in self.totalposts:
                if posts.postId == int(postId):
                    post = posts
                    if random.random() < self.likeprobability * post.clickbait:
                        post._Likes_received(user)
                        v1._has_liked_a_post()
                        v1._posts_user_likes(post)
                        self.total_likes_given += 1
                        if show is True:
                            print(user, "has liked", post.user.name, "post:", post.message)
                            print()
                        if random.random() < self.followprobability:
                            self.Follow(user, post.user.name, show=True)

    def like_post(self, person1, person2, postId):
        v1 = self._getPerson(person1)
        v2 = self._getPerson(person2)

        if self._person_exist(person1) is False:
            print("Cannot like post as", person1, "does not exist\n")
        elif self._person_exist(person2) is False:
            print("Cannot like post as", person2, "does not exist\n")

        elif self._alreadyLiked(person1, postId) is True:
            print(person1, "has already liked post by", person2, "postId:", postId)
        else:
            for i in v2._getPosts():
                if i.postId == int(postId):
                    i._Likes_received(v1)
                    self.total_likes_given += 1
                    print(person1, "has liked", person2, "post:", i.message)

    def _alreadyLiked(self, user, postId):
        alreadyliked = False
        v1 = self._getPerson(user)

        for posts in self.totalposts:
            if posts.postId == int(postId):
                if v1 in posts._Post_likes():
                    alreadyliked = True
        return alreadyliked

    def likeTotal(self, person, postId):
        v1 = self._getPerson(person)
        if not self._person_exist(person):
            print(person, "does not exist. ^Tip check spelling of name\n")
        else:
            for i in v1._getPosts():
                if i.postId == int(postId):
                    print(person, "postId number", postId, ":", i.message)
                    print("Total likes =", i.likestotal)

    def unlike_post(self, person1, person2, postId):
        v1 = self._getPerson(person1)
        v2 = self._getPerson(person2)

        if not self._person_exist(person1):
            print(person1, "does not exist. ^Tip check spelling of name\n")
        elif not self._person_exist(person2):
            print(person2, "does not exist. ^Tip check spelling of name\n")

        elif self._alreadyunliked(person2, postId) is True:
            print(person1, "does not like", person2, "postId:", postId)

        else:
            for post in v2._getPosts():
                if post.postId == int(postId):
                    if v1 in post._Post_likes():
                        post._Remove_likes(v1)
                        print(person1, "has unliked", person2, "post:", post.message)

    def _unlike_post(self, user, postId):
        if not self._person_exist(user):
            print(user, "does not exist. ^Tip check spelling of name\n")

        elif self._alreadyunliked(user, postId) is True:
            print(user, "does not like postId:", postId)

        else:
            v1 = self._getPerson(user)
            for posts in self.totalposts:
                if posts.postId == int(postId):
                    post = posts
                    if v1 in post._Post_likes():
                        if random.random() < self.dislikeprobability:
                            post._Remove_likes(v1)
                            print(user, "has unliked post:", post.message)
                            self.total_likes_given -= 1

    def _alreadyunliked(self, user, postId):
        already_unliked = False
        v1 = self._getPerson(user)

        for posts in self.totalposts:
            if posts.postId == int(postId):
                if v1 not in posts._Post_likes():
                    already_unliked = True
        return already_unliked

    def displayNetwork(self):
        with open('Network State.txt', 'w') as f:
            print("**** This social network contains", self.numPeople, "people ****\n", file=f)  # Sourced from
            # Python Org, section: Input and Output.
            for person in self.SocialSim:
                print(person.name, file=f)
            print()
            print("\n**** Adjacency list of users and who they are following ***\n", file=f)
            for user in self.SocialSim:
                print(user.name, ":", user._list_following(), file=f)
                print()
        f.close()

    def get_users_followers(self, user):
        v1 = self._getPerson(user)
        followers = v1._getFollowers()
        return followers

    def run_timesteps(self, timesteps):  # Timestep defined within the background section of report
        for timestep in range(timesteps):
            process = psutil.Process(os.getpid())
            start_usage = int(process.memory_info().rss)
            startTime = timeit.default_timer()
            for posts in self.totalposts:
                likers = posts._get_likes_received()
                for peeps in likers:
                    followers = self.get_users_followers(peeps)
                    for peeps in followers:
                        self._like_post(peeps.name, posts.postId)
                        end_usage = int(process.memory_info().rss)
                        memory_used = end_usage - start_usage
                        print()
            endTime = timeit.default_timer()
            runningTotal = endTime - startTime
            print("Timestep run time =", str(runningTotal))
            print("\nTimestep memory usage: ", process.memory_info().rss, "bytes of memory")

            print("************** Timstep", timestep, "*************\n")
            print()
            print("**** Network Overall Statistics ****\n")
            print("Total people: ", self.numPeople)
            print("Total posts: ", self.total_posts)
            print("Total follow actioned: ", self.total_followed)
            print("Total likes given: ", self.total_likes_given)
            print()

            label = ["Number of People", "Posts Made", "Total Following Actioned",
                     "Total Likes Given"]
            yvalues = [self.numPeople, self.total_posts, self.total_followed,
                       self.total_likes_given]
            index = [1, 2, 3, 4]
            plt.bar(index, yvalues, color=["rosybrown", "indianred", "salmon", "maroon"])
            plt.xlabel("Statistics measured")
            plt.ylabel("Number (total)")  # Bar plot sourced from FOP unit practical 3 and lecture 3
            plt.title("Network Statistics")
            plt.xticks(index, label, fontsize=5)
            plt.savefig('Network Statistics_Timestep' + str(timestep) + '.png')
            # plt.show()

    def network_statistics(self):
        with open('Final Network Statistics.txt', 'w') as f:
            print("**** Network Overall Statistics ****\n", file=f)
            print("Total people: ", self.numPeople, file=f)  # Sourced from Python Org, section: Input and Output.
            print("Total posts: ", self.total_posts, file=f)
            print("Total follow actioned: ", self.total_followed, file=f)
            print("Total likes given: ", self.total_likes_given, file=f)
            print()
        f.close()
        label = ["Number of People", "Posts Made", "Total Following Actioned", "Total Likes"]
        yvalues = [self.numPeople, self.total_posts, self.total_followed,
                   self.total_likes_given]
        index = [1, 2, 3, 4]
        plt.bar(index, yvalues, color=["rosybrown", "indianred", "salmon", "maroon"])
        plt.xlabel("Statistics measured")
        plt.ylabel("Number (total)")  # Bar plot sourced from FOP unit practical 3 and lecture 3
        plt.title("Network Statistics")
        plt.xticks(index, label, fontsize=5)
        plt.savefig('Final Network Statistics' + '.png')
        # plt.show()

    def UserStatistics(self, user):
        post_popularity = Heap(self.numPeople)
        v1 = self._getPerson(user)
        if self._person_exist(user) is False:
            print(user, "does not exist to be able to display statistics. ^Tip check spelling of name\n")

        # posts
        else:
            print("****", user, "Posts ****\n")
            self.See_Posts(user)
            print()

            # most liked post
            print("****", user, "Most Popular Post/s ****\n")
            like_array = [i.likestotal for i in v1._getPosts()]
            ordered_posts = post_popularity.heapSort(like_array)
            most_liked = ordered_posts[0].priority
            if v1._emptyPosts() is True:
                print("Unable to obtain most popular post as", user, "has not posted\n")

            else:
                for posts in v1._getPosts():
                    if most_liked == 0:
                        print(user, "has not received any likes on any posts")

                    if posts.likestotal == most_liked:
                        print(posts.message)
                        print("Total likes =", most_liked)
            # followers
            print()
            print("****", user, "Followers ****\n")
            v1._list_followers()
            print()
            # following
            print("****", user, "Following ****\n")
            v1 = self._getPerson(user)
            for users in self.SocialSim:
                if users.name == user:
                    print(user, "follows:", v1._list_following())
                    print()

    def Populararity(self):
        with open('Network Popularity Statistics Statistics.txt', 'a+') as f:
            post_popularity = Heap(self.total_posts)
            popular_people = Heap(self.numPeople)
            print("**** This social network had the following posts ****\n", file=f)
            for posts in self.totalposts:
                print(posts.message, file=f)
                print("Total likes =", posts.likestotal, "\n", file=f)
                print()

            print()
            print("**** Most Popular Post/s ****\n", file=f)
            startTime = timeit.default_timer()
            process = psutil.Process(os.getpid())
            start_usage = int(process.memory_info().rss)
            total_likes_posts = [i.likestotal for i in self.totalposts]
            if len(total_likes_posts) < 1:
                print("Unable to find the most popular post as no user has posted yet\n", file=f)
            else:
                ordered_posts_likes = post_popularity.heapSort(total_likes_posts)
                most_liked = ordered_posts_likes[0].priority
                for posts in self.totalposts:
                    if posts.likestotal == most_liked:
                        print(posts.message, "posted by", posts.user.name, file=f)
                        print("Total likes =", most_liked, "\n", file=f)
            endTime = timeit.default_timer()
            runningTotal = endTime - startTime
            print("Heapsort run time ordering popular posts=", str(runningTotal), file=f)

            print("**** Most Popular User/s ****\n", file=f)
            startTime = timeit.default_timer()
            popular_people_list = [people.totalfollowers for people in self.SocialSim]
            if len(popular_people_list) < 1:
                print("Unable to find most popular person as no has followed each other yet\n", file=f)
            else:
                ordered_people = popular_people.heapSort(popular_people_list)
                most_followed_user = ordered_people[0].priority
                for user in self.SocialSim:
                    if user.totalfollowers == most_followed_user:  # maybe how to get it to handle ties?
                        print(user.name, file=f)
                        print("Total followers=", most_followed_user, "\n", file=f)
                        end_usage = int(process.memory_info().rss)
                        print()
            endTime = timeit.default_timer()
            runningTotal = endTime - startTime
            memory_used = end_usage - start_usage
            print("Heapsort run time for ordering popular user =", str(runningTotal), file=f)
            print()
            print("Heapsort memory usage in ordering popular posts and users =", str(memory_used), file=f)
            f.close()

# Class intended to be entirely private
#LinkedList from Practical 3 used throughout class
class User:

    def __init__(_self, name):
        _self.name = name

        _self.following_list = LinkedList()
        _self.totalFollowing = 0

        _self.follower_list = LinkedList()
        _self.totalfollowers = 0

        _self.posts = LinkedList()
        _self.post_total = 0

        _self.posts_user_has_liked = LinkedList()
        _self.totalLikesGiven = 0
        _self.hasLiked_A_Post = False

    def _has_liked_a_post(self):
        self.hasLiked_A_Post = True

    def _posts_user_likes(self, post):
        self.posts_user_has_liked.insertFirst(post)
        self.totalLikesGiven += 1

    def _get_posts_user_likes(self):
        posts = self.posts_user_has_liked
        return posts

    def _emptyPosts(self):
        if self.posts._isEmpty():
            return True

    def _add_post_ToUserList(self, post):
        self.posts.insertFirst(post)
        self.post_total += 1
        return post

    def _getPosts(self):
        posts = self.posts
        return posts

    def _removing_post(self, postId):
        self.posts.removeMiddle(postId)
        self.post_total -= 1

    def _getFollowers(self):
        followers = self.follower_list
        return followers

    def _EmptyFOllowers(self):
        if self.follower_list._isEmpty():
            return True

    def _emptyFollowing(self):
        if self.following_list._isEmpty():
            return True

    def _check_following(self):
        following = self.following_list
        return following

    def _addFollow(self, person):
        self.following_list.insertFirst(person)
        self.totalFollowing += 1
        return person

    def _addFollower(self, person):
        self.follower_list.insertFirst(person)
        self.totalfollowers += 1

    def _list_followers(self):
        a = [i.name for i in self.follower_list]
        print("List of users following", self.name, ":", a)
        print(self.name, "has a total of", self.totalfollowers, "followers")

    def _list_following(self):
        a = [i.name for i in self.following_list]
        return a

    def _removeFollow(self, person):
        self.following_list.removeMiddle(person)
        self.totalFollowing -= 1

    def _removeFollowers(self, person):
        self.follower_list.removeMiddle(person)
        self.totalfollowers -= 1


# Class intended to be entirely private
#LinkedList from Practical 3 used throughout class
class Post:

    def __init__(_self, user, message, postId, clickbait):
        _self.user = user
        _self.message = message
        _self.postId = postId
        _self.clickbait = clickbait

        _self.likes = LinkedList()
        _self.likestotal = 0

    def _Likes_received(self, user):
        self.likes.insertFirst(user)
        self.likestotal += 1

    def _get_likes_received(self):
        likes = self.likes
        return likes

    def _Post_likes(self):
        likes = self.likes
        return likes

    def _Remove_likes(self, user):
        self.likes.removeMiddle(user)
        self.likestotal -= 1


simulation = SocialSim()
netfile = sys.argv[1]
eventfile = sys.argv[2]
prob_like = sys.argv[3]
prob_foll = sys.argv[4]
time_steps = int(sys.argv[5])

simulation.set_probabilities(prob_like, prob_foll, 0, 1)  # Prob unlike set to 0 as default
# Clickbait factor set 1 as default
try:
    with open(str(netfile), "r") as network:
        reader = csv.reader(network, delimiter=":")  # Sourced from Python Org, section: CSV File Reading and Writing.
        print("\n**** Reading", str(netfile), "Network File ****\n")
        Readingprocess = psutil.Process(os.getpid())
        for lines in reader:
            startTime = timeit.default_timer()
            if len(lines) == 1:
                simulation.addPerson(lines[0])
            elif len(lines) == 2:
                simulation.Follow(lines[0], lines[1])
            else:
                print("Unable to read line. ^Tip line may be empty")

    with open(str(eventfile), "r") as events:
        reader = csv.reader(events, delimiter=":")  # Sourced from Python Org, section: CSV File Reading and Writing.
        print("\n**** Reading", str(eventfile), "Event File ****\n")

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
        print("\nReading network and event file has used: ", Readingprocess.memory_info().rss, "bytes of memory")
        print("File reading run time =", str(runningTotal))
        print()
        simulation.run_timesteps(time_steps)
        simulation.network_statistics()
        simulation.displayNetwork()
        simulation.Populararity()
        print()
        endTime = timeit.default_timer()
        runningTotal = endTime - startTime  #sourced from python org
        print("Simulation run time =", str(runningTotal))
        process = psutil.Process(os.getpid())  # Package installed to calculate memory usage of simulation
        print("\nThis simulation has used: ", process.memory_info().rss, "bytes of memory")  # memory in bytes
except Exception as e:
    print("Unable to read the file. Check format of file and try again. ^Tip :", e)

with open("SimulationNetwork", "wb") as Simulation_modePickle:  
    pickle.dump(simulation, Simulation_modePickle)
print("\n **** Network has been saved as 'SimulationNetwork' **** \n")
