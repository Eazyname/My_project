

graph = {}
graph["start"] = {}
graph["start"]["a"] = 6
graph["start"]["b"] = 2
graph["a"] = {}
graph["a"]["fin"] = 1
graph["b"] = {}
graph["b"]["a"] = 3
graph["b"]["fin"] = 5
graph["fin"] = {}

# словарь стоймости
infinity = float("inf")
costs = {}
costs["a"] = 6
costs["b"] = 2
costs["fin"] = infinity

# Словарь хеш-таблицы родителей
parents = {}
parents["a"] = "start"
parents["b"] = "start"
parents["fin"] = None

#Массив прохождения узлов
processed = []


def find_lowest_coast(costs):
    lowest_cost = float("inf") # вес
    lowest_cost_node = None  #Буква (узел) вернет нон если не проёдет иф
    for node in costs:
        cost = costs[node]
        if cost < lowest_cost and node not in processed:  #поиск меньшего значения и проверка уникальности узла
            lowest_cost = cost
            lowest_cost_node = node
    return lowest_cost_node

node = find_lowest_coast(costs)

while node is not None:
    cost = costs[node]
    for elem in graph[node]:
        new_cost = cost + graph[node][elem]
        if costs[elem] > new_cost:
            costs[elem] = new_cost
            parents[elem] = node
    processed.append(node)
    node = find_lowest_coast(costs) # Обрабатываются только те которых нет в в списке processed

print(costs)