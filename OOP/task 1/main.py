class Soda:
    def __init__(self, name="nothing"):
        self.name_additive = name

    def show_my_drink(self):
        if self.name_additive != "nothing":
            print(f"Газировка с {self.name_additive}")
        else:
            print("Обычная газировка")


obj = Soda()
obj.show_my_drink()
obj1 = Soda("шипучкой")
obj1.show_my_drink()