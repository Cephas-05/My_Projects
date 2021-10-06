class Bike:
    def __init__(self, model, price):
        self.model = model
        self.price = price

    def get_model(self):
        return self.model

    def get_price(self):
        return self.price

class Group:
    def __init__(self, min_price, max_price ):
        self.max_price = max_price
        self.group = []
        self.min_price = min_price

    def segregator(self, bike):
        if  bike.get_price() in range(self.min_price, self.max_price):
           holder =  bike.get_model()
           self.group.append(holder)
        else:
            print("Price is not compatible in this group")
        print(self.group)
        
Bike_1 = Bike("Raider", 75000)
Bike_2 = Bike("FZ-3", 120000)
Bike_3 = Bike("BMW S1000RR", 2200000)


Group1 = Group(0, 80000)
Group2 = Group(80000, 140000)
Group3 = Group(140000, 100000000)
Group1.segregator(Bike_1)
Group3.segregator(Bike_3)

