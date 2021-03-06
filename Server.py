from Commands.ServerReplies.AnnounceReply import Announce
from Commands.ServerReplies.InvalidCommandReply import InvalidCommand
from Commands.ServerReplies.WelcomeReply import Welcome
import socket, time, wave, struct
from threading import Thread


numberOfStations = 2
#currentSongList = [None] * 2
currentSongList = ["House of the Rising Sun", "Trance 009"]

radioStations = ["224.0.105.128", ["224.0.105.129"]] #multicastgroups
timeout = 0.1
helpfulMessages = [""]
portNumber = 5786
MCastGroup_0 = "224.0.105.128" #send song data here

def HandleIndividualTCPConnections(connectionSocket, message):
    #expect HelloCommand
    if message[:1] == "0":
        welcome = Welcome(numberOfStations, MCastGroup_0, portNumber)
        welcomeReply = welcome.welcomeReply
        connectionSocket.send(welcomeReply)

        #expect AskSongCommand
        message = connectionSocket.recv(1024)
        message = message.decode("ascii")
        if message[:1] == "1":
            #check that requested radio station exists
            announce = Announce(message, currentSongList)
            if announce.RequestNotValid:
                msg = "Radio station "+str(announce.requestedStationNumber)+" does not exist"
                invalidCommand = InvalidCommand(msg)
                connectionSocket.send(invalidCommand)
                connectionSocket.close()
            else:
                #get currently playing song on station defined by message and send
                announceReply = announce.announceReply
                connectionSocket.send(announceReply)
                connectionSocket.close()
        else:
            msg = "Expected: 1 AskSongCommand"
            invalidCommand = InvalidCommand(msg)
            connectionSocket.send(invalidCommand.invalidMessage)
            connectionSocket.close()
    else:
        errormsg = "Expected HelloCommand"
        invalidcommand = InvalidCommand(errormsg)
        connectionSocket.send(invalidcommand.invalidMessage)
        connectionSocket.close()

def ListenTCPConnections():
    serverSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    serverSocket.bind(('', portNumber))
    serverSocket.listen(1)
    print("Server is good to go on TCP")

    threads = []
    #follow custom protocol from here
    while 1:
        connectionSocket, addr = serverSocket.accept()
        print("Client Connected")
        message = connectionSocket.recv(1024)
        message = message.decode("ascii")

        if message:
            thread = Thread(target=HandleIndividualTCPConnections(connectionSocket, message))
            threads.append(thread)
            thread.start()
        else:
            connectionSocket.close()

#send song data
def TransmitSongData():
    serverSocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    ttl = struct.pack("b", 32)
    serverSocket.setsockopt(socket.IPPROTO_IP, socket.IP_MULTICAST_TTL, ttl)

    serverSocket.bind(('', portNumber))
    print("Server is good to go on UDP")

    filelocation = "C:\\Users\Ruben\Desktop\\paris2.wav"
    #open file
    file = wave.open(filelocation, mode="rb")

    while 1:
        data = file.readframes(4410)
        serverSocket.sendto(data, (MCastGroup_0, portNumber))

        #reset filepointer as to repeat song, if at the end
        if file.getnframes() == file.tell():
            file.rewind()
        time.sleep(0.09)

    #somewhere, this function should update global song list of what song is currently playing on what station

try:
    thread1 = Thread(target=TransmitSongData)
    thread2 = Thread(target=ListenTCPConnections)

    print("Starting thread1")
    thread1.start()
    print("Starting thread2")
    thread2.start()
except:
    print("Could not start threads")