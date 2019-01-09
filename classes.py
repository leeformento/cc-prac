class Animal():
    noise = "Grunt"
    size = "Large"
    color = "Red"
    hair = "Long"
    def get_color(self):
        return self.color + " " + abc
    @property #dont have to () after invoked
    def make_noise(self):
        return self.noise

dog = Animal()
dog.make_noise
dog.get_color("Orange")
# instance::
# dog.size = "small"
# dog.color = "black"
# dog.hair = "hairless"

# positional has to be before kwarg
# keyword arg 
# abc = "new string"
# def some_func(arg_1, arg_2, kwarg_3=None, kwarg_2="Abc"):
#     print(arg_1, arg_2)
#     if kwarg_1 != None:
#         print(kwarg_1)

# some_func("abc", "efg", kwarg_1="Nu nahh")
email_address = "mikeenriquez@gmail.com"
to_list = ['jessica@soho.com']
from  =['meltiango@gma.com', 'hello@chismis.com']

def send_email(email=email_address, to_list=to_list, from_listfrom_list):
    pass

send_email(email="hello@chismis.com", to_list['jessica@soho.com'], from_list=['jessica@soho.com'])


class Dog(Animal):
    # overriding
    name = 'Aso'
    size = "Small"
    color = "black"

clifford = Dog()
clifford.color = 'white'
clifford.name = "Clifford Red