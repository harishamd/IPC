# import library socket karena menggunakan IPC socket
import socket

# definisikan IP untuk binding
ip = "172.20.10.4"

# definisikan port untuk binding
port = 12345

# definisikan ukuran buffer untuk menerima pesan
buffer_size = 1024

# buat socket (bertipe UDP atau TCP?)
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# lakukan binding ke IP dan port
s.bind((ip, port))

# lakukan listen
s.listen(5)

#  siap menerima koneksi
c, addr = s.accept()
print ('Connection address:', addr)

# buka/buat file bernama hasil_upload.txt untuk menyimpan hasil dari file yang dikirim server
f = open("hasil_upload.txt","wb")
# masih hardcoded nama file, bertipe byte




# loop forever
while 1:
    # terima pesan dari client
    data1 = c.recv(1024)
    
    # tulis pesan yang diterima dari client ke file kita (result.txt)
    f.write(data1)
    
    # berhenti jika sudah tidak ada pesan yang dikirim
    if not data1: break
    
# tutup file result.txt    
f.close()

#tutup socket
s.close()

# tutup koneksi
c.close()
