from Commands.Clients.TCPClient import TCPClient
from Commands.Clients.UDPClient import UDPClient



tcpClient = TCPClient()
MCastGroup = tcpClient.InitiateTCPClient(tcpClient.serverip, tcpClient.serverport)

udpclient = UDPClient()
udpclient.ReceiveFrom(MCastGroup)




