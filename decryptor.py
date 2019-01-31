import codecs, zlib
from Cryptodome.Cipher import DES3

avain = b'aX!;e@zh7Lklvn%p2r!su0a8'
tiedosto = input('Purettava tiedosto:\n')

def purku(tiedosto, avain):
 file = open(tiedosto, 'r')
 purettava = file.read().strip()
 purettava = bytes(purettava, encoding = 'utf8')
 
 purettava = codecs.decode(purettava, 'hex')
 file.close() 

 des = DES3.new(avain, DES3.MODE_ECB)
 purettava = zlib.decompress(purettava)
 avattu = des.decrypt(purettava)
 avattu = str(avattu, 'utf-8').strip()
  
 file2 = open('purettu.txt', 'w')
 file2.write(avattu)
 file2.close()

purku(tiedosto, avain)
