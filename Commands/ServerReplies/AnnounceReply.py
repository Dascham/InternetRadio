class Announce:
    replyType = 1

    def __init__(self, message, currentSongList):
        #self.songname = ""
        splitMessage = message.split(",")
        self.requestedStationNumber = int(splitMessage[1])

        numberOfStations = currentSongList.__len__()
        if self.requestedStationNumber <= numberOfStations:
            self.songname = currentSongList[self.requestedStationNumber-1]
            self.RequestNotValid = False #e.g. request is valid
        else:
            self.songname = "Unknown"
            self.RequestNotValid = True

        self.announceReply = (str(self.replyType)+","+str(self.songname.count('')-1)+","+
                                  str(self.songname)).encode("ascii")


