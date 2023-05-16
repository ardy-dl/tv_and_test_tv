# create class
class TV:
    # make the test driver (TestTV)
    def __init__(self, name, channel, volume):
        self.name = name
        self.channel = channel
        self.volume = volume

    def show(self):
        print(self.name + "'s channel is " + str(self.channel) + " and volume level is " + str(self.volume))  
# create object of a class
tv1 = TV("tv1", 30, 3)
    # call the method
tv1.show()
