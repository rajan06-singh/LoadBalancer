import socket

def client(host, port, msg):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    addr = (host,port)
    s.connect(addr)
    try:
        s.sendall(msg)
    finally:
        s.close()


client('192.168.1.175', 5555, b"Test2")