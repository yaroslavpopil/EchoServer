import socket

def Main():
        host = '54.236.5.59'
        port = 5000

        s = socket.socket()
        s.connect((host,port))

        message = raw_input("-> ")
        while message != 'q':
            s.send(message)
            data = s.recv(1024)
            print 'Received from server: ' + str(data)
            message = raw_input("-> ")
        s.close()

if __name__ == '__main__':
    Main()
