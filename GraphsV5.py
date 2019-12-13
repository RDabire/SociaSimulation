# **
# ** SocialSimV5: Implementation of Graphs algorithm to create social simulation
# **
# ** Author: Roy Dabire
# ** Date:   October 2019


import random  # Used to calculate probabilities
from LinkedList import *  # Used throughout to store nodes referenced and implemented in practical 3
from Heaps import *  # Used in popularity method referenced and implemented in practical 7
import matplotlib.pyplot as plt  # Used for plotting features
import os  # Used in memory usage package
import psutil  # Package to calculate memory usage sourced from python org
import timeit  # Used to track the time a particular method/function took to execute sourced from python org


class SocialSim:

    def __init__(_self):
        _self.SocialSim = LinkedList() #LinkedList from Practical 3
        _self.numPeople = 0
        _self.postId = 1

        _self.totalposts = LinkedList() #LinkedList from Practical 3
        _self.total_posts = 0

        _self.total_likes_given = 0
        _self.likeswithoutclickbait = 0  #Results did not look correct so ommited from investigation
        _self.likeswithclickbait = 0     #Results did not look correct so ommited from investigation

        _self.total_followed = 0

        _self.likeprobability = 0
        _self.followprobability = 0
        _self.dislikeprobability = 0
        _self.clickbaitfactor = 1 #default value

    def addPerson(self, name):
        new_person = User(name)
        if not self._person_exist(name):
            self.SocialSim.insertFirst(new_person) #LinkedList from Practical 3
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
                    self.SocialSim.removeMiddle(users) #LinkedList from Practical 3
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

    def set_probabilities(self, like, follow, dislike, clickbait):  # clickbait will be set to 1 as a default value
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
                    self.likeswithoutclickbait += 1  # This was an attempt to track the likes coming from posts
                    # with/out clickbait factor.
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
                print(i.user.name, "postId number", i.postId, ":", i.message)

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

    def _like_post(self, user, postId, show=True):  # Private and used when a post is created
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
                            self.Follow(user, post.user.name, show=False)

    def like_post(self, person1, person2, postId):  # Public and used for manual likes
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

    def unlike_post(self, person1, person2, postId):  # Public use for manual unlikes/dislikes
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

    def _unlike_post(self, user, postId):  # Private use
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
        print("**** This social network contains", self.numPeople, "people ****\n")
        for person in self.SocialSim:
            print(person.name)
        print()
        print("\n**** Adjacency list of users and who they are following ***\n")
        for user in self.SocialSim:
            print(user.name, ":", user._list_following())
            print()

    def _get_users_followers(self, user):
        if not self._person_exist(user):
            print(user, "does not exist to be able to action a post. ^Tip check spelling of name\n")
        else:
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
                    followers = self._get_users_followers(peeps)
                    for peeps in followers:
                        self._like_post(peeps.name, posts.postId)
                        end_usage = int(process.memory_info().rss)
                        memory_used = end_usage - start_usage
                        print()
            endTime = timeit.default_timer()
            runningTotal = endTime - startTime
            print("Timestep run time =", str(runningTotal))
            print("\nTimestep memory usage: ", process.memory_info().rss, "byes of memory")

            print("************** Timstep", timestep, "*************\n")
            self.network_statistics()

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
            # plt.show()     #User may chose to uncomment this if they would like to display to screen

    def network_statistics(self):
        print("**** Network Overall Statistics ****\n")
        print("Total people: ", self.numPeople)
        print("Total posts: ", self.total_posts)
        print("Total follow actioned: ", self.total_followed)
        print("Total likes given: ", self.total_likes_given)
        label = ["Number of People", "Posts Made", "Total Following Actioned", "Total likes"]
        yvalues = [self.numPeople, self.total_posts, self.total_followed,
                   self.total_likes_given]
        index = [1, 2, 3, 4]
        plt.bar(index, yvalues, color=["rosybrown", "indianred", "salmon", "maroon"])
        plt.xlabel("Statistics measured")
        plt.ylabel("Number (total)")   # Bar plot sourced from FOP unit practical 3 and lecture 3
        plt.title("Network Statistics")
        plt.xticks(index, label, fontsize=5)
        plt.savefig('Final Network Statistics' + '.png')
        # plt.show()    #User may chose to uncomment this if they would like to display to screen

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
            print("**** Most Popular Post/s ****\n", file=f)  #Returns the most popular user by index
            startTime = timeit.default_timer()
            process = psutil.Process(os.getpid())
            start_usage = int(process.memory_info().rss)
            total_likes_posts = [i.likestotal for i in self.totalposts]
            if len(total_likes_posts) < 1:
                print("Unable to find the most popular post as no user has posted yet\n", file=f)
            else:
                ordered_posts_likes = post_popularity.heapSort(total_likes_posts)  #Returns the most popular user by index
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
                    if user.totalfollowers == most_followed_user:  
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

    def __init__(self, name):
        self.name = name

        self.following_list = LinkedList() 
        self.totalFollowing = 0

        self.follower_list = LinkedList()  
        self.totalfollowers = 0

        self.posts = LinkedList()
        self.post_total = 0

        self.posts_user_has_liked = LinkedList() 
        self.totalLikesGiven = 0
        self.hasLiked_A_Post = False

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

    def _emptyFollowing(self):
        if self.following_list._isEmpty():
            return True

    def _check_following(self):
        following = self.following_list
        return following

    def _addFollow(self, person):
        self.following_list.insertFirst(person)
        self.totalFollowing += 1

    def _addFollower(self, person):
        self.follower_list.insertFirst(person)
        self.totalfollowers += 1

    def _list_followers(self):
        a = [i.name for i in self.follower_list]  # List comprehension approved by Valerie (displays the adjacency list)
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

    def __init__(self, user, message, postId, clickbait):
        self.user = user
        self.message = message
        self.postId = postId
        self.clickbait = clickbait

        self.likes = LinkedList()
        self.likestotal = 0

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
