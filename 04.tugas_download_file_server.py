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


# buka file bernama "file_didownload.txt
f = open("file_didownload.txt","rb")
# masih hard code, file harus ada dalam folder yang sama dengan script python


try:
    # baca file tersebut sebesar buffer 
    byte=f.read(buffer_size)
    
    # selama tidak END OF FILE; pada pyhton EOF adalah b''
    while byte != b'':
        # kirim hasil pembacaan file dari server ke client
        print('sending')
        c.send(byte)
        
        # baca sisa file hingga EOF
        byte= f.read(buffer_size)
        
finally:
    print ("end sending")
    
    # tutup file jika semua file telah  dibaca
    f.close()

# tutup socket
s.close()

# tutup koneksi
