#blueprints when we want to create something (objects)
class Vehicle: #capitalize first for classes
    def __init__(self, make, model):
        self.make = make
        self.model = model
        
    def moves(self):
        print('Moves along..')
    
    def get_make_model(self):
        print(f"I'm a {self.make} {self.model}.")
        
my_car = Vehicle('Tesla', 'Model 3')

# print(my_car.make)
# print(my_car.model)
my_car.get_make_model()
my_car.moves()

your_car = Vehicle('Cadillac', 'Escalade')
your_car.get_make_model()
your_car.moves()

# inheritance
class Airplane(Vehicle):
    def __init__(self, make, model, faa_id):
        super().__init__(make, model)
        self.faa_id = faa_id
        
    def moves(self):
        print('Flies along..')
        
class Truck(Vehicle):
    def moves(self):
        print('Rumbles along..')
        
class GolfCart(Vehicle):
    pass

cessna = Airplane('Cessna', 'Skyhawk','N-12345')
mack = Truck('Mack', 'Pinnacle')
golfwagon = GolfCart('Yamaha', 'GC100')

cessna.get_make_model()
cessna.moves()
mack.get_make_model()
mack.moves()
golfwagon.get_make_model()
golfwagon.moves()


print("\n\n")

#polymorphism - we're giving the same input but they all behave differently based on how they're built
for v in (my_car, your_car, cessna, mack, golfwagon):
    v.get_make_model()
    v.moves()