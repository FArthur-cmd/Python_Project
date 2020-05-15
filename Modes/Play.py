from collections import deque

from Battle.Battle_ import Battle
from Battle.army import Army
from Map.Medium import MediumMap
from Map.Quick import QuickMap
from Map.Work_with_resources.Hero_resouces import Resources
from Map.Work_with_resources.Miner import Miner
from Map.imports import ways, resources, building_array, improving_skills_list, \
    miner_array
from Working_with_textures.drow_map import drow_map
from Working_with_textures.show_info_in_modes import show_resources, show_moves
from Working_with_textures.wait_klick import wait_klick


class Play:
    def __init__(self, first: Army, second: Army, Mode: str, window,
                 fullscreen, width, height, k):
        self.walked_points = 0
        self.window = window
        self.fullscreen = fullscreen
        self.width = width
        self.height = height
        self.first_army = first
        self.k = k
        self.first_resources = Resources(first.hero.name)
        self.second_resources = Resources(second.hero.name)
        self.second_army = second
        if Mode == "Quick":
            M = QuickMap(self.first_army, self.second_army)
            self.Map = M.Map
            self.first_neutral_army = M.neutral_first
            self.second_neutral_army = M.neutral_second
        else:
            M = MediumMap(self.first_army, self.second_army)
            self.Map = M.Map
            self.first_neutral_army = M.neutral_first
            self.second_neutral_army = M.neutral_second
        self.miners = []
        for i in range(len(self.Map)):
            for j in range(len(self.Map[0])):
                if self.Map[i][j] in miner_array:
                    miner = Miner(self.Map[i][j].split("_")[0], [i, j])
                    miner.add_hero_resources(self.first_resources)
                    miner.add_hero_resources(self.second_resources)
                    self.miners += [miner]
        self.first_player_turn = True
        self.day = 0
        self.playing()

    def draw_all_info(self):
        for i in range(len(self.Map)):
            for j in range(len(self.Map[0])):
                if self.first_player_turn:
                    if self.Map[i][j] == self.first_army.hero.name:
                        button_list_ = drow_map(self.window, self.fullscreen,
                                               "grass",
                                               i, j, self.Map, self.width,
                                               self.height, self.k)
                        hero_coordinads_ = [i, j]
                        show_resources(self.window,
                                       self.first_resources.reserve,
                                       self.width,
                                       self.height)
                        show_moves(self.window,
                                   self.first_army.hero.movement -
                                   self.walked_points,
                                   self.width,
                                   self.height,
                                   self.k)
                        break
                else:
                    if self.Map[i][j] == self.second_army.hero.name:
                        button_list_ = drow_map(self.window, self.fullscreen,
                                               "grass",
                                               i, j, self.Map, self.width,
                                               self.height, self.k)
                        hero_coordinads_ = [i, j]
                        show_resources(self.window,
                                       self.second_resources.reserve,
                                       self.width,
                                       self.height)
                        show_moves(self.window,
                                   self.first_army.hero.movement -
                                   self.walked_points,
                                   self.width,
                                   self.height,
                                   self.k)
                        break
        return hero_coordinads_, button_list_

    def playing(self):
        hero_coordinads, button_list = self.draw_all_info()
        command = [""]
        while command[0] != "end" and command[0] != "Exit":
            command = wait_klick(button_list, self.width, self.height)
            command = command.split()
            if command[0] == "move":
                path = self.make_path([hero_coordinads[0], hero_coordinads[1]],
                                      [int(command[1]), int(command[2])])
                if self.first_player_turn:
                    command[0] = self.move(path, self.first_army.hero.name)
                else:
                    command[0] = self.move(path, self.second_army.hero.name)
                try:
                    for items in self.first_resources.reserve.items():
                        print(items[0], items[1])
                    for items in self.first_resources.increasing.items():
                        print(items[0], items[1])
                    hero_coordinads, button_list = self.draw_all_info()
                except:
                    command[0] = "Exit"
            else:
                print("command is not move in playing")
        print("left")
        if command[0] != "Exit":
            self.next_turn()
        else:
            self.end(self.first_player_turn)

    def next_turn(self):
        self.walked_points = 0
        if self.first_player_turn:
            self.first_resources.next_turn()
            self.first_player_turn = False
            self.day += 1
        else:
            self.second_resources.next_turn()
            self.first_player_turn = True
            if self.day == 7:
                self.day = 0
        self.playing()

    def move(self, path, hero_name):
        already_moved = self.walked_points
        cur_pos = [0, 0]
        print(path)
        if len(path) > 1:
            while self.walked_points < self.first_army.hero.movement and  \
                    cur_pos != path[1]:
                self.walked_points += 1
                cur_pos = path[- self.walked_points + already_moved]
                if self.walked_points - already_moved != 1:
                    self.Map[path[
                        -self.walked_points + 1 + already_moved
                        ][0]][path[-self.walked_points + 1 + already_moved][
                        1]] = "Road"
                self.Map[cur_pos[0]][cur_pos[1]] = hero_name
                self.draw_all_info()
            if self.walked_points < self.first_army.hero.movement:
                self.walked_points += 1
                if self.Map[path[0][0]][path[0][1]] == "Road":
                    print("Road_")
                    self.Map[path[1][0]][path[1][1]] = "Road"
                    self.Map[path[0][0]][path[0][1]] = hero_name
                elif self.Map[path[0][0]][path[0][1]].split("Count")[0] in \
                        resources:
                    print("res")
                    string = self.Map[path[0][0]][path[0][1]].split("Count")
                    if self.first_player_turn:
                        self.first_resources.add_resource(string[0], string[1])
                    else:
                        self.second_resources.add_resource(string[0],
                                                           string[1])
                    self.Map[path[0][0]][path[0][1]] = "Road"
                elif self.Map[path[0][0]][path[0][1]] in building_array:
                    print("in buildings")
                    if self.first_player_turn:
                        print(self.first_army.hero.improve_skill(
                            improving_skills_list[
                                building_array.index(
                                    self.Map[path[0][0]][path[0][1]])
                            ],
                            2
                        ))
                    else:
                        print(self.second_army.hero.improve_skill(
                            improving_skills_list[
                                building_array.index(
                                    self.Map[path[0][0]][path[0][1]])
                            ],
                            2
                        ))
                    self.Map[path[0][0]][path[0][1]] = "Road"
                elif self.Map[path[0][0]][path[0][1]] in miner_array:
                    print("miner")
                    for miner in self.miners:
                        if miner.position_on_map == [path[0][0], path[0][1]]:
                            if self.first_player_turn:
                                miner.get_under_control(
                                    self.first_army.hero.name)
                            else:
                                miner.get_under_control(
                                    self.second_army.hero.name)
                            break
                elif self.Map[path[0][0]][path[0][1]] == \
                        self.first_army.hero.name and \
                        not self.first_player_turn or \
                        self.Map[path[0][0]][
                            path[0][1]] == self.second_army.hero.name and \
                        self.first_player_turn:
                    print("hero_fight")
                    battle = Battle(self.first_army, self.second_army,
                                    self.window,
                                    self.fullscreen, self.width, self.height,
                                    self.k)
                    if battle.win:
                        print("First Win")
                        self.end(self.first_player_turn)
                    else:
                        print("Second Win")
                        self.end(self.first_player_turn)
                    return "Exit"
                else:
                    neutral_army = None
                    print("fight")
                    for creature in self.first_neutral_army.creatures:
                        if creature.name == self.Map[path[0][0]][path[0][1]]:
                            neutral_army = Army(None, [creature])
                            break
                    for creature in self.second_neutral_army.creatures:
                        if creature.name == self.Map[path[0][0]][path[0][1]]:
                            neutral_army = Army(None, [creature])
                            break
                    if neutral_army is not None:
                        if self.first_player_turn:
                            if Battle(self.first_army, neutral_army,
                                      self.window, self.fullscreen, self.width,
                                      self.height, self.k).win:
                                print("Win")
                                self.Map[path[0][0]][path[0][1]] = \
                                    self.first_army.hero.name
                                self.Map[path[1][0]][path[1][1]] = "Road"
                            else:
                                print("Loose")
                                self.end(not self.first_player_turn)
                                return "Exit"
                        else:
                            if Battle(self.second_army, neutral_army,
                                      self.window, self.fullscreen, self.width,
                                      self.height, self.k).win:
                                print("Win")
                                self.Map[path[0][0]][path[0][1]] = \
                                    self.second_army.hero.name
                                self.Map[path[1][0]][path[1][1]] = "Road"
                            else:
                                print("Loose")
                                self.end(self.first_player_turn)
                                return "Exit"

    def make_path(self, coordinates_from, coordinates_to):
        print("make path")
        print(coordinates_to)
        if 10 <= coordinates_from[0] < len(self.Map) - 12:
            coordinates_to[0] += coordinates_from[0] - 10
        elif coordinates_from[0] > len(self.Map) - 22:
            coordinates_to[0] += len(self.Map) - 21
        if coordinates_from[1] >= 10:
            coordinates_to[1] += len(self.Map[0]) - 11
        print(coordinates_from)
        print(coordinates_to)
        curr_coord = coordinates_from
        parent_map = [[]]
        queue = deque()
        add_counter, wave_counter = 0, 1
        queue.append(curr_coord)
        for i in range(len(self.Map[0])):
            parent_map[0] += [[-1, -1]]
        for j in range(len(self.Map)):
            parent_map += [parent_map[0][::]]
        while curr_coord != coordinates_to and \
                not len(queue) == 0:
            if wave_counter == 0:
                wave_counter = add_counter

            curr_coord = queue.popleft()
            wave_counter -= 1

            for i in range(8):
                tmp = [curr_coord[0] + ways[i][0], curr_coord[1] + ways[i][1]]
                if (0 < tmp[0] < len(self.Map) - 1 and 0 < tmp[1] < len(
                        self.Map[0]) - 1 and
                    self.Map[tmp[0]][tmp[1]] == "Road" or
                    tmp == coordinates_to) and parent_map[tmp[0]][tmp[1]] == \
                        [-1, -1]:

                    if tmp == coordinates_to:
                        print(self.Map[coordinates_to[0]][coordinates_to[1]])
                        if self.Map[coordinates_to[0]][coordinates_to[1]] == \
                                "NoWay":
                            coordinates_to = curr_coord
                        else:
                            parent_map[tmp[0]][tmp[1]] = curr_coord
                    else:
                        parent_map[tmp[0]][tmp[1]] = curr_coord
                        queue.append(tmp)
                        add_counter += 1

        if parent_map[coordinates_to[0]][coordinates_to[1]] == [-1, -1]:
            return []
        else:
            curr_coord = coordinates_to
            path = []
            while curr_coord != coordinates_from:
                path += [curr_coord]
                curr_coord = parent_map[curr_coord[0]][curr_coord[1]]
            path += [coordinates_from]
            return path

    def end(self, turn):
        if turn:
            print(self.first_army.hero.name)
        else:
            print(self.second_army.hero.name)
