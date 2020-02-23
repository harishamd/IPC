# import library socket karena akan menggunakan IPC socket
import socket

# definisikan alamat IP bind dari server
ip = "172.20.10.4"

# definisikan port number untuk bind dari server
port = 12345

# buat socket bertipe UDP
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# lakukan bind
s.bind((ip,port))

# loop forever
while True:
    # terima pesan dari client
    pesan, addr = s.recvfrom(1024)
    
    # menampilkan hasil pesan dari client
    print("received data from : ", pesan)
    #print (addr)
    print(addr)
    
