
import time
from abc import ABC,abstractmethod
from datetime import datetime


class Ligth:
    @staticmethod
    def turn_on():
        print('ligth on')

    @staticmethod
    def turn_off():
        print('ligth off')

class ISwotch(ABC):

    @staticmethod
    @abstractmethod
    def execute():
        pass

class SwitchOnCommand(ISwotch):

    def __init__(self,ligth):
        self._ligth = ligth

    def execute(self):
        self._ligth.turn_on()


class SwitchOffCommand(ISwotch):

    def __init__(self, ligth):
        self._ligth = ligth

    def execute(self):
        self._ligth.turn_off()

class Switch:

    def __init__(self):
        self._commands = {}
        self._history = []

    def register(self,command_name,command):
        self._commands[command_name] = command

    def execute(self,command_name):
        if command_name in self._commands.keys():
            self._commands[command_name].execute()
            self._history.append((time.time(),command_name))
        else:
            print(f'Unknow command - {command_name}')


    def show_history(self):
        for row in self._history:
            print(f'{datetime.fromtimestamp(row[0]).strftime("%Y-%m-%d %H:%M:%S")} : {row[1]}')

    def replay_last(self):
        command = self._history[-1]
        self._commands[command[1]].execute()
        self._history.append((time.time(), command[1]))

ligth = Ligth()
switch_on = SwitchOnCommand(Ligth)
switch_off = SwitchOffCommand(ligth)

switch = Switch()
switch.register('ON', switch_on)
switch.register('OFF',switch_off)

switch.execute('ON')
switch.execute('OFF')
switch.execute('ON')

switch.replay_last()

switch.show_history()

