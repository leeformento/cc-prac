class Animal():
    noise = "Grunt"
    size = "Large"
    color = "Red"
    hair = "Long"
    def get_color(self):
        return self.color
    
    def make_noise(self):
        return self.noise

dog = Animal()
dog.make_noise()
# instance::
# dog.size = "small"
# dog.color = "black"
# dog.hair = "hairless"

class Dog(Animal):
    # overriding
    name = 'Aso'
    size = "Small"
    color = "black"

clifford = Dog()
clifford.color = 'white'
clifford.name = "Clifford Red