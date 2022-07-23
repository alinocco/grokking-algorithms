from collections import deque
from time import sleep


class Node:
    def __init__(self, name, current_path: list):
        self.name = name
        self.current_path = current_path

    def __str__(self) -> str:
        return str(self.name, self.current_path)


def breadth_first_search(graph: dict, start, find):
    closest_path = [start]

    search_queue = deque()
    search_queue += [Node(friend, closest_path + [friend])
                     for friend in graph[start]]

    searched = []

    while search_queue:
        person = search_queue.popleft()

        if person.name not in searched:
            if person.name == find:
                closest_path = person.current_path
                return closest_path
            elif person.name in list(graph.keys()):
                # Put all the person's friends in search_queue if there are not in person's current_path. If the friend is already mentioned in current_path, we should not add him/her again.
                search_queue += [
                    Node(friend, person.current_path + [friend]) for friend in graph[person.name]
                    if friend not in person.current_path]
                searched.append(person)

    return False


graph = {
    'yaroslav': ['timur'],
    'vadim': ['timur', 'yaroslav', 'dmitrii'],
    'alina': ['vadim', 'aziza', 'daria', 'aizada'],
    'aziza': ['daria', 'artem', 'alina'],
}

start = 'yaroslav'
find = 'timur'

result = breadth_first_search(graph, start, find)

if result is False:
    print("The closest '%s' can not be found." % find)
else:
    print("The closest '%s' can be found this way %s." %
          (find, result))
