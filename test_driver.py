# create class
class TV:
    # make the test driver (TestTV)
    def __init__(self, channel, volume):
        self.channel = channel
        self.volume = volume

    def show(self):
        print(self.channel, self.volume)  
# create object of a class
tv1 = TV(30, 3)
    # call the method
tv1.show()