# import library socket karena akan menggunakan IPC socket
import socket

# definisikan alamat IP binding  yang akan digunakan 
ip = "172.20.10.4"

# definisikan port number binding  yang akan digunakan 
port = 12345

# definisikan ukuran buffer untuk mengirimkan pesan
buffer_size = 32

# buat socket bertipe TCP
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# lakukan bind
s.bind((ip, port))

# server akan listen menunggu hingga ada koneksi dari client
s.listen(5)

# lakukan loop forever
while 1:
	# menerima koneksi
    c, addr = s.accept()
	
	# menampilkan koneksi berupa IP dan port client yang terhubung menggunakan print
    print("Mendapatkan koneksi dari ", addr)
	
	# menerima data berdasarkan ukuran buffer
    data = c.recv(buffer_size).decode()
	
	# menampilkan pesan yang diterima oleh server menggunakan print
    print("Menerima data : ", data)
	
	# mengirim kembali data yang diterima dari client kepada client
    c.send(data.encode())

# tutup koneksi	
c.close()
