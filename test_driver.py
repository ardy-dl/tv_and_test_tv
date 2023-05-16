# create class
class TV:
    # make the test driver (TestTV)
    def TestTV(self, channel, volume):
        self.channel = channel
        self.volume = volume
    # create functions (1 to 120 channels)
    def channel(self):
        for i in range(1, 121):
            return i
    # volume (1-7)
    def volume(self):
        for i in range(1, 8):
            return i
    # on/off
    # create object of a class
    tv1 = TV(30, 3)
    # call the method
    tv1.channel()