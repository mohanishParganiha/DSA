import heapq


class Tweet:
    def __init__(self, userId: int, tweetId: int, timestamp: int):
        self.userId = userId
        self.tweetId = tweetId
        self.timestamp = timestamp


class User:
    def __init__(self, userId: int):
        self.userId = userId
        self.followers = set()
        self.following = set()
        self.tweets = []


class Twitter:
    def __init__(self):
        self.users = dict()
        self.timestamp = 0

    def getNewsFeed(self, userId: int) -> list[int]:
        if userId not in self.users:
            return []
        counter = 0
        newsFeed = []
        # max heap to store all the tweets
        heapq.heapify(newsFeed)
        # add tweets from following of users
        for followed_id in self.users[userId].following:
            tweets = self.users[followed_id].tweets
            if tweets:
                last_tweet_idx = len(tweets)-1
                tweet = tweets[last_tweet_idx]
                heapq.heappush(
                    newsFeed, (-tweet.timestamp, -counter, last_tweet_idx, followed_id))
                counter += 1
        # add users own tweets
        if userId in self.users:
            tweets = self.users[userId].tweets
            if tweets:
                last_tweet_idx = len(tweets)-1
                tweet = tweets[last_tweet_idx]
                heapq.heappush(
                    newsFeed, (-tweet.timestamp, -counter, last_tweet_idx, userId))
                counter += 1

        user_feed = []
        while newsFeed and len(user_feed) < 10:
            _, _, last_tweet_idx, followed_id = heapq.heappop(newsFeed)
            tweets = self.users[followed_id].tweets
            user_feed.append(tweets[last_tweet_idx].tweetId)

            if last_tweet_idx > 0:
                older_tweet = tweets[last_tweet_idx-1]
                heapq.heappush(
                    newsFeed, (-older_tweet.timestamp, -counter, last_tweet_idx-1, followed_id))
                counter += 1

        return user_feed

    def postTweet(self, userId: int, tweetId: int):
        if userId not in self.users:
            self.users[userId] = User(userId)
        self.timestamp += 1
        self.users[userId].tweets.append(
            Tweet(userId, tweetId, self.timestamp))

    def follow(self, followerId: int, followeeId: int):
        # follower  started following the followee
        # add followee to followers following-list
        # add follower to followees follower-list

        # check if followee is  registered in users
        if followeeId not in self.users:
            self.users[followeeId] = User(followeeId)
        # same check if follower is registered in users
        if followerId not in self.users:
            self.users[followerId] = User(followerId)

        self.users[followerId].following.add(followeeId)
        self.users[followeeId].followers.add(followerId)

    def unfollow(self, followerId: int, followeeId: int):
        # follower unfollowed the followee
        # remove followee from followers following-list
        # remove follower from followees follower-list
        if followeeId in self.users and followerId in self.users:
            self.users[followerId].following.discard(followeeId)
            self.users[followeeId].followers.discard(followerId)


twitter = Twitter()
twitter.postTweet(1, 5)
twitter.postTweet(1, 3)
twitter.postTweet(2, 101)
twitter.postTweet(2, 13)
twitter.postTweet(6, 112)
twitter.follow(1, 2)
print(twitter.getNewsFeed(1))  # [13, 3, 5] or similar order
twitter.unfollow(1, 2)
print(twitter.getNewsFeed(1))  # [5, 3]
