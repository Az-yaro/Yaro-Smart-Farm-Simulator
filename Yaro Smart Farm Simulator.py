class CatfishBatch:
    def __init__(self,batch_id,count,avg_weight_grams):
        self.batch_id = batch_id
        self.count = count
        self.avg_weight = avg_weight_grams
        self.total_biomass = self.calculate_biomass()

    def calculate_biomass(self):
        return self.count * self.avg_weight
        
    def feed_batch(self, avg_feed_weight):
        self.avg_feed_weight = avg_feed_weight
        weight_gain = (avg_feed_weight/1000) * 0.8
        self.avg_weight *= weight_gain
        print(f"Fed fish: avg weight gain {self.avg_weight:.0f} g")
        self.total_biomass = self.calculate_biomass()

class Tank:
    def __init__(self,tank_name, capacity_liter, **kwargs):
        self.tank_name = tank_name
        self.capacity_liter = capacity_liter
        self.ammonia_level = kwargs.get('ammonia', 0.00)
        self.ph_level = kwargs.get('ph', 7.0)
        self.current_batch = None

    def add_fish(self,batch_object):
        self.batch_object = batch_object
        if self.current_batch is None:
            self.current_batch = batch_object
            print(f"Success: fish batch added to {self.tank_name}")
        elif self.current_batch == batch_object:
            print(f"{self.tank_name} already in the tank")
        else:
            print("Tank already occupied")

    def perform_water_change(self):
        try:
            percentage = float(input("enter water change level using (60 -100)%: "))
            if 60 <= percentage <= 100:
                fraction_removed = percentage/100
                self.ammonia_level += (1-fraction_removed)
                print(f"Water change successeful: New Ammonia Level reduce to {self.ammonia_level:.2f} ppm")
            else:
                print(f"Water change has to be within 60 - 100% of water change")
        except ValueError:
            print("Wrong input use a valid enring")

    def daily_report(self):
        print("\n" + "="*40)
        print("WELCOME TO YARO SMART FARM! DAILY REPORT")
        print("="*40)
        print(f"Tank Report: {self.tank_name}")
        print(f"Capacity: {self.capacity_liter}L | Ammonia Level {self.ammonia_level:.2f} ppm | pH Level {self.ph_level}")
        if self.current_batch is not None:
            print(f"Tank id: {self.current_batch.batch_id}")
            print(f"Fish count: {self.current_batch.count}")
            print(f"Total biomass: {self.current_batch.total_biomass:.0f}")
        else:
            print("No current batch available yet")

alpha_1k = CatfishBatch('alpah 1k',3000,15)
nursery_tank = Tank('nursery tank',10000, ammonia =0.1, ph=7.0 )
nursery_tank.add_fish(alpha_1k)
nursery_tank.perform_water_change()
nursery_tank.current_batch.feed_batch(3000)
nursery_tank.daily_report()