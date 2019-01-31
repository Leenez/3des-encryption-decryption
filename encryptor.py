import codecs, zlib
from Cryptodome.Cipher import DES3

avain = b'aX!;ioklamnsedg'
tiedosto = input('Salattava tiedosto:\n')

def pad(text):
  text = bytes(text, encoding='utf-8')
  while len(text) % 8 != 0:
   text += bytes(' ', encoding='utf-8')
  return text

def salaus(tiedosto, avain):
 file = open(tiedosto, 'r')
 salattava = file.read().strip()
 salattava = pad(salattava)
 file.close() 

 des = DES3.new(avain, DES3.MODE_ECB)
 salattu = des.encrypt(salattava)
 salattu = zlib.compress(salattu)
 salattu = codecs.encode(salattu, 'hex')
 
 salattu = salattu.decode('utf-8')
   
 file2 = open('salattu.txt', 'w')
 file2.write(salattu)
 file2.close()

salaus(tiedosto, avain)
