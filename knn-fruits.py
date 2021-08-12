# fruits:-
# 0 -> apple
# 1 -> banana

# colors:-
# 0 -> red
# 1 -> green
# 2 -> yellow
# 3 -> black

import math
import csv

class Fruit:
    def __init__(self, height, width, color, fruit):
        self.height = height
        self.width = width
        self.color = color
        self.fruit = bool(fruit)

def main():
    fruits = []
    
    # read data set
    with open("fruits.csv", "r") as csv_file:
        dataset = csv.reader(csv_file)
        fields = next(dataset)
        for row in dataset:
            fruits.append(Fruit(int(row[0]), int(row[1]), int(row[2]), int(row[3])))
    
    #input from user
    print("This AI program will tell you if the fruit is apple or banana.")
    print("Enter the following data for a fruit.")
    height = int(input("Height(0 - 10 in meters): "))
    width = int(input("Width(0 - 10 in meters): "))
    print("""
    0 -> red
    1 -> green
    2 -> yellow
    3 -> black
    """)
    color = int(input("Color: "))
    x = Fruit(height, width, color, 0)
    
    result = knn(fruits, 3, x)
    print(result)


# KNN Algorithm
def knn(fruits, k, x):
    data = []
    for f in fruits:
        data.append({"fruit": f.fruit, "distance": calc_distance(f, x)})
    
    data.sort(key=lambda x: x["distance"])
    
    kObjects = data[:k]
    
    apple = 0
    banana = 0
    for obj in kObjects:
        if obj["fruit"]:
            banana = banana + 1
        else:
            apple = apple + 1
    
    return "banana" if banana >= apple else "apple"


def calc_distance(p1, p2):
    eq = (p2.height - p1.height)**2 + (p2.width - p1.width)**2 + (p2.color - p1.color)**2
    return math.sqrt(eq)

if __name__ == "__main__":
    main()