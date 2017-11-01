from Clients.UDPClient import UDPClient
from Clients.TCPClient import TCPClient

tcpClient = TCPClient()
MCastGroup = tcpClient.InitiateTCPClient(tcpClient.serverip, tcpClient.serverport)

udpclient = UDPClient()
udpclient.ReceiveFrom(MCastGroup)




