class storage:
    def __init__(self, name, objects):
        self.name=name
        self.objects=objects
    
    def show_items(self):
        if len(self.objects)>0:
            print(f"{self.name} contains: ", end="")
            print(", ".join(self.objects))
        else: print(f"{self.name} is empty!")
       
    def move_one(self,otherstorage):
        if len(otherstorage.objects)>0:
            print("Write a number to take chosen item")
            for x, value in enumerate(otherstorage.objects,1):
                print(x, value)
            item=otherstorage.objects[int(input())-1]
            otherstorage.objects.remove(item)
            self.objects.append(item)
            print(f"{item} was moved from {otherstorage.name}")
        else: print(f"{self.name} is empty!")
        
    def move_all(self,otherstorage):
        for i in otherstorage.objects: self.objects.append(i)
        otherstorage.objects.clear()
        print(f"All items were moved to {self.name}")

chest=storage("chest",["diamond","silver coin","Titan's Gladius","gold bar"])
inventory=storage("inventory",["sabre","golden ring", "pirate hat","eye patch"])

while True:
    print ("Here are you, the pirate and your treasure chest.\nWhat do you want to do?")
    print("<store item>, <take item>, <my items>\n<examine chest>,<take all>,<store all>")
    command=""
    while True:
        command=input()
        if command=="store item": chest.move_one(inventory)
        elif command=="take item": inventory.move_one(chest)
        elif command=="take all": inventory.move_all(chest)
        elif command=="store all": chest.move_all(inventory)
        elif command=="my items": inventory.show_items()
        elif command=="examine chest": chest.show_items()
        else: print("Unknown command")
