class Twitter:
    def __init__(self):
        self.count = 0
        self.tweetMap = defaultdict(list)   # userId -> list of (count, tweetId)
        self.followMap = defaultdict(set)   # userId -> set of followeeId

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.count += 1
        tweets = self.tweetMap[userId]
        tweets.append((self.count, tweetId))

        # capping the history to 10 tweets
        if len(tweets) > 10: tweets.pop(0)

    def getNewsFeed(self, userId: int) -> List[int]:
        res = []
        heap = []

        self.followMap[userId].add(userId)

        for followeeId in self.followMap[userId]:
            tweets = self.tweetMap.get(followeeId)
            if tweets:
                idx = len(tweets) - 1
                count, tweetId = tweets[idx]
                heapq.heappush_max(heap, (count, tweetId, followeeId, idx - 1))

        while heap and len(res) < 10:
            count, tweetId, followeeId, idx = heapq.heappop_max(heap)
            res.append(tweetId)
            if idx >= 0:
                count, tweetId = self.tweetMap[followeeId][idx]
                heapq.heappush_max(heap, (count, tweetId, followeeId, idx - 1))

        return res

    def follow(self, followerId: int, followeeId: int) -> None:
        self.followMap[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.followMap[followerId]:
            self.followMap[followerId].remove(followeeId)
 