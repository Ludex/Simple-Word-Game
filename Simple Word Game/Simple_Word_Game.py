def get_input():
    command = input(": ").split()
    verb_word = command[0]
    
    if verb_word in verb_dict:
        verb = verb_dict[verb_word]
    else:
        print("Unknown verb {}".format(verb_word))
        return

    if len(command) >= 2:
        noun_word = command[1]
        print(verb(noun_word))
    else:
        print(verb("nothing"))

def say(noun):
    return 'You said "{}"'.format(noun)


class GameObject:
    class_name = ""
    describe = ""
    objects = {}

    def __init__(self, name):
        self.name = name
        GameObject.objects[self.class_name] = self

    def get_describe(self):
        return self.class_name + "\n" + self.describe

class Cockroach(GameObject):    
    def __init__(self,name):
        self.class_name = "cockroach"
        self.health = 3
        self._describe = "A filthy creature"
        super().__init__(name)

    @property
    def describe(self):
        if self.health >= 3:
            return self._describe
        elif self.health == 2:
            health_line = "It has a wound on its knee."
        elif self.health == 1:
            health_line = "Its left arm has been cut off!"
        elif self.health <= 0:
            health_line = "It is dead"
        
        return self._describe + "\n" + health_line

    @describe.setter
    def describe(self, value):
        self._describe = value

def hit(noun):
    if noun in GameObject.objects:
        thing = GameObject.objects[noun]
        
        if type(thing) == Cockroach:
            thing.health = thing.health - 1
            
            if thing.health <= 0:
                msg = "You killed the cockroach"
            else:
                msg = "You hit the {}".format(thing.class_name)

        else:
            msg = "There is no {} here".format(noun)

        return msg

cockroach = Cockroach("Gobbly")

def examine(noun):
    if noun in GameObject.objects:
        return GameObject.objects[noun].get_describe()

    else:
        return "There is no {} here".format(noun)

verb_dict = {
    "say":say,
    "examine":examine,
    "hit":hit
    }

while True:
    get_input()