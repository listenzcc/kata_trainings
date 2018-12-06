# coding: utf-8

import time


class Thing:
    def __init__(self):
        self.birth = time.time()

    def say(self, string=None):
        if string:
            print(string)
        else:
            print('I am %.0f seconds old.' % (time.time()-self.birth))

    def new_attr(self, attr, value):
        self.__setattr__(attr, value)


thing = Thing()

thing.new_attr('name', 'robot1')
print(thing.name)

time.sleep(2)
thing.say('Hello')
thing.say()
