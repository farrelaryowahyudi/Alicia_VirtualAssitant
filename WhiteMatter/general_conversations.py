import random

from WhiteMatter.SenseCells.tts import tts

def who_are_you():
    message = ['I am Alicia, your lovely personal assistant.', 'Alicia, havent i told you before?', 
    'You have asked that question so many times, Its Alicia.', 'Its Alicia'] 
    tts(random.choice(message))
def how_am_i():
    replies =['You are goddamn handsome!', 'My knees go weak when I see you.', 'You are sexy!', 
    'You look like the kindest person that I have met.'] 
    tts(random.choice(replies))
def tell_joke():
    jokes = ['What happens to a frogs car when it breaks down? It gets toad away.', 
    'Why was six scared of seven? Because seven ate nine.', 'No, I always forget the punch line.']
    tts(random.choice(jokes))
def who_am_i(name):
    tts('You are ' + name + ', a brilliant person. I really love you!')
def where_born():
    tts('I was created by a high school student in Indonesia, the land of wonders.')
def how_are_you():
    tts('I am fine, thank you.')
def undefined():
    tts('Sorry, I dont know what that means!')