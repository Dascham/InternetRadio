import socket, struct, pyaudio

class UDPClient:

    def ReceiveFrom(self, mcastgroup):
        port = 5785
        clientSocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, socket.IPPROTO_UDP)
        clientSocket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        clientSocket.bind(('', port))

        mreq = struct.pack("4sl", socket.inet_aton("224.0.105.128"), socket.INADDR_ANY)

        clientSocket.setsockopt(socket.IPPROTO_IP, socket.IP_ADD_MEMBERSHIP, mreq)

        #get audio thing
        p = pyaudio.PyAudio()

        stream = p.open(format=p.get_format_from_width(2), channels=2, rate=44100, output=True)
        print("Trying audio")
        while 1:
            data = clientSocket.recvfrom(100000)
            stream.write(data)