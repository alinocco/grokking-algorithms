
class Item:
    def __init__(self, name, weight, price):
        self.name = name
        self.weight = weight
        self.price = price


class ResultCell:
    def __init__(self, price, weight, items):
        self.price = price
        self.weight = weight
        self.items = items

    def __str__(self):
        return str(self.price)

    def copy(self):
        return ResultCell(self.price, self.weight, self.items)


knapsack = 4
items = [
    Item('guitar', 1, 1500),
    Item('laptop', 3, 2000),
    Item('stereo', 4, 3000),
]

results = [[ResultCell(0, 0, [])]*knapsack for _ in items]

for i in range(len(results)):
    for j in range(len(results[i])):
        if i == 0:
            results[i][j].price = items[i].price
            results[i][j].weight = items[i].weight
            results[i][j].items = [items[i].name]
        elif j == 0:
            if items[i].weight == 1 and results[i-1][j].price < results[i][j].price:
                results[i][j].price = items[i].price
                results[i][j].weight = items[i].weight
                results[i][j].items = [items[i].name]
            else:
                results[i][j] = results[i-1][j].copy()
        elif items[i].weight <= j + 1:
            previous_max_item = results[i-1][j]
            additional_item = results[i-1][j + 1 - items[i].weight] if j + \
                1 - items[i].weight > 0 else None

            if additional_item is None or previous_max_item.price >= items[i].price + additional_item.price:
                results[i][j] = previous_max_item.copy()
            else:
                results[i][j].price = items[i].price + \
                    additional_item.price
                results[i][j].weight = items[i].weight + \
                    additional_item.weight
                results[i][j].items = [items[i]] + additional_item.items

for i in results:
    for j in i:
        print(j, end=" ")
    print(end="\n")
