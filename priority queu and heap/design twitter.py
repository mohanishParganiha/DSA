import heapq


class Twitter:

    def __init__(self):
        self.posts = {}
        self.following = {}
        self.global_counter = 0

    def postTweet(self, userId: int, tweetId: int) -> None:
        if userId not in self.posts:
            self.posts[userId] = []
        self.posts[userId].append((self.global_counter, tweetId))
        self.global_counter += 1

    def getNewsFeed(self, userId: int) -> list[int]:

        feed_posts = []
        heapq.heapify(feed_posts)

        # if the user posted something add him to heap
        if userId in self.posts:
            heapq.heappush(
                feed_posts, (-self.posts[userId][-1][0], self.posts[userId][-1][1], userId, len(self.posts[userId])-1))
        # seed the heap with users which were followed by userId
        for followee in self.following.get(userId, []):
            if followee in self.posts:
                heapq.heappush(
                    feed_posts, (-self.posts[followee][-1][0], self.posts[followee][-1][1], followee, len(self.posts[followee])-1))

        feed = []
        # fill the feed list and refil the heap if needed
        while len(feed) < 10 and feed_posts:
            counter, postId, user, index = heapq.heappop(feed_posts)
            feed.append(postId)
            if index > 0:
                heapq.heappush(
                    feed_posts, (-self.posts[user][index-1][0], self.posts[user][index-1][1], user, index-1))

        return feed

    def follow(self, followerId: int, followeeId: int) -> None:
        if followerId != followeeId:
            if followerId not in self.following:
                self.following[followerId] = set()
            self.following[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followerId in self.following:
            self.following[followerId].discard(followeeId)


twitter = Twitter()
twitter.postTweet(1, 1)
print(twitter.getNewsFeed(1))
twitter.follow(2, 1)
print(twitter.getNewsFeed(2))
twitter.unfollow(2, 1)
print(twitter.getNewsFeed(2))
