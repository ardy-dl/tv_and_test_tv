# create class
class TV:
    # make the test driver (TestTV)
    def __init__(self, name = "Default TV", channel = 98, volume = 4):
        self.name = name
        self.channel = channel
        self.volume = volume
        self.is_on = False

    def show(self):
        print(self.name + "'s channel is " + str(self.channel) + " and volume level is " + str(self.volume)) 

    # method for status
    def status(self):
        print(self.name, "Status: ON" if self.is_on else "Status: OFF")
    # turn on
    def turn_on(self):
        self.is_on = True
        print(self.name, "is turned ON.")
    # turn off
    def turn_off(self):
        self.is_on = False
        print(self.name, "is turned OFF.")
    # returns channel


    # set a new channel
    # get volume level
    # set a new volume level
    # increase channel  
    # decrease channel
    # increase volume
    # decrease volume  
# create object of a class
default_tv = TV()
tv1 = TV("tv1", 30, 3)
tv2 = TV("tv2", 3, 2)
# call the method
tv1.show()  
tv2.show()
default_tv.show()
default_tv.turn_off()
default_tv.status()
