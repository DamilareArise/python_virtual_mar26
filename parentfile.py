from oop import BankAccount

class Parent:
    firstname = None
    lastname = 'Ojo'
    hobby = 'Reading'
    
    def __init__(self, fn):
        self.firstname = fn
    
    def introduce(self):
        print(f'My name is {self.firstname} {self.lastname}. I like {self.hobby}.')
        
# parent = Parent("Ade")
# parent.introduce()


# scripts, modules, library, framework

from gtts import gTTS

tts = gTTS('Hello. Welcome to my class')
tts.save('hello.mp3')