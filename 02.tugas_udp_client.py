# import library socket karena akan menggunakan IPC socket
import socket

# definisikan target IP server yang akan dituju
ip = "127.0.0.1"

# definisikan target port number server yang akan dituju
port = 12345

#print ("target IP:", UDP_IP)
print("target ip : ", "127.0.0.1")
#print ("target port:", UDP_PORT)
print("target port : ", 12345)
#print ("pesan:", PESAN)
print("pesan : ", "test UDP")
# buat socket bertipe UDP
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
# lakukan loop 10 kali
for x in range (10):
    # definisikan pesan yang akan dikirim
    pesan = "Hello UDP"
    
    # kirim pesan    
    s.sendto(pesan.encode(), (ip,port))