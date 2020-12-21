from random import shuffle
from util import Queue


class User:
    def __init__(self, name):
        self.name = name


class SocialGraph:
    def __init__(self):
        self.last_id = 0
        self.users = {}
        self.friendships = {}

    def add_friendship(self, user_id, friend_id):
        """
        Creates a bi-directional friendship
        """
        if user_id == friend_id:
            print("WARNING: You cannot be friends with yourself")
        elif friend_id in self.friendships[user_id] or user_id in self.friendships[friend_id]:
            print("WARNING: Friendship already exists")
        else:
            self.friendships[user_id].add(friend_id)
            self.friendships[friend_id].add(user_id)

    def add_user(self, name):
        """
        Create a new user with a sequential integer ID
        """
        self.last_id += 1  # automatically increment the ID to assign the new user
        self.users[self.last_id] = User(name)
        self.friendships[self.last_id] = set()

    def populate_graph(self, num_users, avg_friendships):
        """
        Takes a number of users and an average number of friendships
        as arguments

        Creates that number of users and a randomly distributed friendships
        between those users.

        The number of users must be greater than the average number of friendships.
        """
        # Reset graph
        self.last_id = 0
        self.users = {}
        self.friendships = {}
        # !!!! IMPLEMENT ME

        # Add users
        for i in range(0, num_users):
            self.add_user(f"User {i}")

        # Create friendships
        possible_friendships = []

        for user_id in self.users:
            for friend_id in range(user_id + 1, self.last_id + 1):
                possible_friendships.append((user_id, friend_id))

        shuffle(possible_friendships)

        for i in range(num_users * avg_friendships // 2):
            friendship = possible_friendships[i]

            self.add_friendship(friendship[0], friendship[1])

    # function to return extended network list that I can loop to create keys for my result dictionary
    def bft(self, vertex):
        q = Queue()
        visited = set()

        q.enqueue(vertex)

        # extended network of given vertex
        network = []

        while q.size() > 0:
            user = q.dequeue()

            if user not in visited:
                visited.add(user)

                # append user to network list that'll represent extended network of vertex(user_id)
                network.append(user)

                for friend in self.friendships[user]:
                    q.enqueue(friend)

        return network

    # function to get paths from user_id to each user in network list
    def bfs(self, fromUser, toUser):
        q = Queue()
        visited = set()

        q.enqueue([fromUser])

        while q.size() > 0:
            path = q.dequeue()
            user = path[-1]

            if user == toUser:
                return path

            if user not in visited:
                visited.add(user)

                for friend in self.friendships[user]:
                    new_path = list(path)
                    new_path.append(friend)
                    q.enqueue(new_path)

    def get_all_social_paths(self, user_id):
        """
        Takes a user's user_id as an argument

        Returns a dictionary containing every user in that user's
        extended network with the shortest friendship path between them.

        The key is the friend's ID and the value is the path.
        """
        visited = {}  # Note that this is a dictionary, not a set
        # !!!! IMPLEMENT ME

        # create keys in visited for each user in user_id's extended network
        for user in self.bft(user_id):
            # for each user, value will be path from user_id to each keys
            visited[user] = self.bfs(user_id, user)

        return visited

    # Chris Solution

    # def get_neighbors(self, user_id):
    #     """
    #     Get all friends/neighbors (edges) of a vertex/user.
    #     """
    #     return self.friendships[user_id]

    # def get_all_social_paths(self, user_id):
    #     """
    #     Takes a user's user_id as an argument
    #     Returns a dictionary containing every user in that user's
    #     extended network with the shortest friendship path between them.
    #     The key is the friend's ID and the value is the path.
    #     """
    #     visited = {}  # Note that this is a dictionary, not a set
    #     # !!!! IMPLEMENT ME
    #     q = Queue()
    #     q.enqueue([user_id])

    #     while q.size() > 0:

    #         path = q.dequeue()
    #         last_id = path[-1]

    #         if last_id not in visited:
    #             visited[last_id] = path
    #         for next_id in self.get_neighbors(last_id):
    #             neighbor_path = path.copy()
    #             neighbor_path.append(next_id)

    #             q.enqueue(neighbor_path)

    #     return visited


if __name__ == '__main__':
    sg = SocialGraph()

    sg.populate_graph(10, 2)
    print(sg.friendships)

    connections = sg.get_all_social_paths(5)
    print(connections)
