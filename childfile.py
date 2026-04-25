# import parentfile
# import parentfile as p
from parentfile import Parent


class Child(Parent):
    
    def __init__(self, fn, hobby):
        super().__init__(fn)
        self.hobby = hobby
        self.gender = 'Male'
   
    def play(self):
        print(f"{self.firstname} likes to play")

child = Child('Femi', 'Coding')
# child.introduce()
# child.play()