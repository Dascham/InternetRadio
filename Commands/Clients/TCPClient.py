from Commands.ClientCommands.AskSongCommand import AskSong
from Commands.ClientCommands.HelloCommand import Hello
import socket
class TCPClient:
    serverIP = "2.109.204.102"
    serverPort = 5786

def InitiateTCPClient(serverIP, serverPort):
    clienSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    clienSocket.connect((serverIP, serverPort))

    #step 1 of protocol: say hello
    hello = Hello()
    clienSocket.send(hello.helloCommand)

    #expect WelcomeReply
    serverReply = clienSocket.recv(1024)
    serverReply = serverReply.decode("ascii")
    print(serverReply)
    if serverReply[:1] != 0:
        print("0 did not receive WelcomeReply")

    #send AskSongCommand
    asksong = AskSong(1)
    clienSocket.send(asksong.askSongCommand)

    #expect AnnounceReply
    serverReply1 = clienSocket.recv(1024)
    serverReply1 = serverReply1.decode("ascii")
    print(serverReply1)
    if serverReply[:1] != 1:
        print("1 did not receive AnnounceReply")

    clienSocket.close()
