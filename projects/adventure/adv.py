from room import Room
from player import Player
from world import World

import random
from ast import literal_eval

# Load world
world = World()


# You may uncomment the smaller graphs for development and testing purposes.
# map_file = "maps/test_line.txt"
# map_file = "maps/test_cross.txt"
# map_file = "maps/test_loop.txt"
# map_file = "maps/test_loop_fork.txt"
map_file = "maps/main_maze.txt"

# Loads the map into a dictionary
room_graph = literal_eval(open(map_file, "r").read())
world.load_graph(room_graph)

# Print an ASCII map
world.print_rooms()

player = Player(world.starting_room)

# Fill this out with directions to walk
# traversal_path = ['n', 'n']
# traversal_path = []

# # Barely passing solution! 1995 moves
# tg = {player.current_room.id: player.current_room.get_exits()}
# reverse = []
# opp_d = {"n": "s", "e": "w", "s": "n", "w": "e"}


# while len(tg) < len(world.rooms):

#     if player.current_room.id not in tg:
#         # add to traversal graph
#         tg[player.current_room.id] = player.current_room.get_exits()

#         # direction to travel
#         # remove direction on that vertex
#         direction = tg[player.current_room.id].pop()

#         # remove opposite direction on next vertex
#         player.travel(direction)
#         player.current_room.get_exits().remove(opp_d[direction])

#         # append to traversal path and reverse
#         traversal_path.append(direction)
#         reverse.append(opp_d[direction])

#     else:

#         if player.current_room.id in tg and len(tg[player.current_room.id]) > 0:
#             direction = tg[player.current_room.id].pop()

#             player.travel(direction)
#             player.current_room.get_exits().remove(opp_d[direction])

#             traversal_path.append(direction)
#             reverse.append(opp_d[direction])

#         else:
#             move_back = reverse.pop()

#             # node already visited
#             player.travel(move_back)
#             traversal_path.append(move_back)

#             if len(tg[player.current_room.id]) > 0:
#                 direction = tg[player.current_room.id].pop()

#                 player.travel(direction)
#                 player.current_room.get_exits().remove(opp_d[direction])

#                 traversal_path.append(direction)
#                 reverse.append(opp_d[direction])


# optimized
traversal_path = []

tg = {player.current_room.id: {d: "?" for d in player.current_room.get_exits()}}
opposite_dir = {"n": "s", "s": "n", "e": "w", "w": "e"}


# get available exits
def available_exits(vertex):

    available = []

    for key in tg[vertex]:

        if tg[vertex][key] == "?":

            available.append(key)

    return available


def dft(room):

    while len(available_exits(room)) != 0:

        # random dir
        direction = random.choice(available_exits(room))

        # previous room reference
        prev_room = player.current_room.id

        # move and append
        player.travel(direction)
        traversal_path.append(direction)

        # insert new room in tg
        cur_room = player.current_room.id

        if cur_room not in tg:
            tg[cur_room] = {d: "?" for d in player.current_room.get_exits()}

        tg[cur_room][opposite_dir[direction]] = prev_room
        tg[prev_room][direction] = cur_room

        room = cur_room


def bft_nearest_room(s_room):

    q = [s_room]
    visited = set()

    target = None

    while len(q) > 0:

        room = q.pop(0)

        if room not in visited:

            visited.add(room)

            if len(available_exits(room)) > 0:

                target = room

                return target

            for next_room in list(tg[room].values()):
                q.append(next_room)


def bfs(target, s_room):

    q = [[s_room]]
    visited = set()

    final_path = []

    while len(q) > 0:

        room_path = q.pop(0)

        if room_path[-1] not in visited:
            visited.add(room_path[-1])

            if room_path[-1] == target:
                final_path = room_path
                break

            for r in list(tg[room_path[-1]].values()):

                new_rpath = list(room_path) + [r]
                q.append(new_rpath)

    path = []

    for i in range(len(final_path) - 1):

        for d in tg[final_path[i]]:

            if tg[final_path[i]][d] == final_path[i + 1]:

                path.append(d)

    return path

# times = 500
# moves = []
# lowest_times = 500
# lowest_moves = []


# # run once
while len(tg) != len(world.rooms):

    dft(player.current_room.id)
    nearest = bft_nearest_room(player.current_room.id)
    path_to_nearest = bfs(nearest, player.current_room.id)

    for d in path_to_nearest:

        player.travel(d)
        traversal_path.append(d)


# # run 1000 times
# while lowest_times > 0:

#     while times > 0:

#         tg = {player.current_room.id: {
#             d: "?" for d in player.current_room.get_exits()}}

#         while len(tg) != len(world.rooms):

#             dft(player.current_room.id)
#             nearest = bft_nearest_room(player.current_room.id)
#             path_to_nearest = bfs(nearest, player.current_room.id)

#             for d in path_to_nearest:

#                 player.travel(d)
#                 traversal_path.append(d)

#         moves.append(len(traversal_path))

#         traversal_path = []
#         times -= 1

#     lowest_moves.append(min(moves))
#     moves = []
#     times = 100
#     lowest_times -= 1


# print(min(lowest_moves))
# print(max(lowest_moves))
# print(lowest_moves)


# TRAVERSAL TEST
visited_rooms = set()
player.current_room = world.starting_room
visited_rooms.add(player.current_room)

for move in traversal_path:
    player.travel(move)
    visited_rooms.add(player.current_room)

if len(visited_rooms) == len(room_graph):
    print(
        f"TESTS PASSED: {len(traversal_path)} moves, {len(visited_rooms)} rooms visited")
else:
    print("TESTS FAILED: INCOMPLETE TRAVERSAL")
    print(f"{len(room_graph) - len(visited_rooms)} unvisited rooms")


#######
# UNCOMMENT TO WALK AROUND
#######
# player.current_room.print_room_description(player)
# while True:
#     cmds = input("-> ").lower().split(" ")
#     if cmds[0] in ["n", "s", "e", "w"]:
#         player.travel(cmds[0], True)
#     elif cmds[0] == "q":
#         break
#     else:
#         print("I did not understand that command.")
