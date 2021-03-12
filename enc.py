#coding=utf-8
# PENTING : Hanya Bisa Enskripsi Pada python 3

"""
MIT License

Copyright (c) 2021 Rahmat ^_^

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
"""

"""
Cara Descrypt 

CONTOH FILE YANG SUDAH DI ENSKRIPSI

#Enskripsi By Rahmat
#Di Buat Pada Fri Mar 12 15:36:24 2021
import base64 , bz2
exec(base64.b64decode(bz2.decompress(b'BZh91AY&SY\x93\x91\x14\xf8\x00\x00\x07\x8f\x80\x00\x02\x08x \x90\x18\x81H` \x00"\x80\xd3\xd4f\xa6\xd4(i\xa6\x00\x1e\xcc`-\x81\xe2\xfc\x98\x06Z\x12\xcf\xc5\xdc\x91N\x14$$\xe4E>\x00')))

UBAH KODE DI ATAS MENJADI

#Enskripsi By Rahmat
#Di Buat Pada Fri Mar 12 15:36:24 2021
import base64 , bz2
x = base64.b64decode(bz2.decompress(b'BZh91AY&SY\x93\x91\x14\xf8\x00\x00\x07\x8f\x80\x00\x02\x08x \x90\x18\x81H` \x00"\x80\xd3\xd4f\xa6\xd4(i\xa6\x00\x1e\xcc`-\x81\xe2\xfc\x98\x06Z\x12\xcf\xc5\xdc\x91N\x14$$\xe4E>\x00'))
y = x.decode('utf-8')
open('Hasil.py','w').write(y)

LALU JALANKAN MAKA AKAN TERDAPAT FILE BARU YANG BERNAMA Hasil.py


CARA DECOMPILE Marshal

PERTAMA-TAMA SILAHKAN INSTALL MODUL uncompyle6

$ pip3 install uncompyle6

CONTOH FILE YANG SUDAH DI COMPILE MENGGUNAKAN MARSHAL

#coding=utf-8
#enskripsi By Rahmat
#Di Buat Pada Fri Mar 12 15:43:11 2021
import marshal
exec(marshal.loads(b'\xe3\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x02\x00\x00\x00@\x00\x00\x00s\x0c\x00\x00\x00e\x00d\x00\x83\x01\x01\x00d\x01S\x00)\x02Z\x05HelloN)\x01\xda\x05print\xa9\x00r\x02\x00\x00\x00r\x02\x00\x00\x00\xfa\x0b<Ayu Putri>\xda\x08<module>\x01\x00\x00\x00\xf3\x00\x00\x00\x00'))

UBAH KODE TADI MENJADI

#coding=utf-8
#enskripsi By Rahmat
#Di Buat Pada Fri Mar 12 15:43:11 2021
import marshal
from uncompyle6.main import decompile
x = marshal.loads(b'\xe3\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x02\x00\x00\x00@\x00\x00\x00s\x0c\x00\x00\x00e\x00d\x00\x83\x01\x01\x00d\x01S\x00)\x02Z\x05HelloN)\x01\xda\x05print\xa9\x00r\x02\x00\x00\x00r\x02\x00\x00\x00\xfa\x0b<Ayu Putri>\xda\x08<module>\x01\x00\x00\x00\xf3\x00\x00\x00\x00')
decompile(3.8,x,open('hasil.py','w'))

LALU JALANKAN MAKA AKAN TERDAPAT FILE BARU YANG BERNAMA Hasil.py
"""

from getpass import getpass,getuser
from socket import gethostname
from urllib.request import urlopen
from urllib.error import URLError as koneksi
from binascii import hexlify
from py_compile import compile as pycompile
from bz2 import compress as bz2
from lzma import compress as lzma
from py_compile import compile as pycompile
from base64 import b64encode , b32encode , b85encode , b16encode
from time import sleep , ctime
from os import system as sys , environ as env , W_OK as ok , stat , access , listdir , mkdir , uname
from os.path import basename , isfile , isdir , realpath
from sys import argv , platform , version , executable
from zlib import compress,decompress
from marshal import dumps
from subprocess import call
from string import ascii_lowercase as low
from random import choice

UPDATE = "10-03-2021 11:19"

# Acak Warna
warna = lambda : choice(["\033[0m","\033[90m","\033[91m","\033[92m","\033[93m","\033[94m","\033[95m","\033[96m","\033[97m"])

logo = f"\033[91m****     **** *******     **     **\n/**/**   **/**/**////**   //**   ** \n/**//** ** /**/**   /**    //** **  \n/** //***  /**/*******      //***   \n/**  //*   /**/**///**       **/**  \n/**   /    /**/**  //**     ** //** \n/**        /**/**   //**   **   //**\n//         // //     //   //     //\n\033[94m╔═════════════════════════════════════╗\n║\033[94m[\033[93m•\033[94m] \033[96mAuthor : \033[92m\033[4mMR-X JUNIOR\033[0m             \033[94m║\n║\033[94m[\033[93m•\033[94m] \033[96mGitHub : \033[97mgithub.com/MR-X-Junior  \033[94m║\n║\033[94m[\033[93m•\033[94m] \033[96mWA.    : \033[93m+62 85754629509        \033[94m ║\n║\033[94m[\033[93m•\033[94m] \033[96mUPDATE : {UPDATE}      \033[94m  ║\n║\033[94m[\033[93m•\033[94m] \033[96mPython : {warna()}{version[0:6]}                \033[94m  ║\n║\033[94m[\033[93m•\033[94m] \033[96mOS     : {warna()}{platform}                 \033[94m  ║\n║\033[94m[\033[93m•\033[94m] \033[96mHost   : {warna()}{gethostname()}             \033[94m  ║\n║\033[94m[\033[93m•\033[94m] \033[96mTeam.  : {warna()}TNT {warna()}ANONYMOUS \033[91mINDO\033[97mNESIA\033[94m ║\n\033[94m╚═════════════════════════════════════╝"

#Install pip
def install(package , pesan = '\r'):
	print (pesan)
	call([executable, "-m","pip","--disable-pip-version-chec","-q", "install", package])


# Halaman 1
page1 = f"\033[1;94m****     **** *******     **     **\n/**/**   **/**/**////**   //**   ** \n/**//** ** /**/**   /**    //** **  \n/** //***  /**/*******      //***   \n/**  //*   /**/**///**       **/**  \n/**   /    /**/**  //**     ** //** \n/**        /**/**   //**   **   //**\n//         // //     //   //     //\n╔═════════════════════════════════════╗\n║[•] Author : MR-X JUNIOR             ║\n║[•] GitHub : github.com/MR-X-Junior  ║\n║[•] WA.    : +6285754629509          ║\n║[•] UPDATE : {UPDATE}        ║\n║[•] Page   : 1                       ║\n╚═════════════════════════════════════╝\n\033[92mHalaman 1\n\033[97m===============\n\033[94m[\033[91m01\033[94m] {warna()}Base85\n\033[94m[\033[91m02\033[94m] {warna()}Base64\n\033[94m[\033[91m03\033[94m] {warna()}Base32\n\033[94m[\033[91m04\033[94m] {warna()}Base16\n\033[94m[\033[91m05\033[94m] {warna()}Zlib\n\033[94m[\033[91m06\033[94m] {warna()}Marshal\n\033[94m[\033[91m07\033[94m] {warna()}lzma\n\033[94m[\033[91m08\033[94m] {warna()}bz2\n\033[94m[\033[91m09\033[94m] {warna()}Hex\n\033[94m[\033[91m10\033[94m] {warna()}pyc\n\033[94m[\033[91m11\033[94m] {warna()}String\n\033[94m[\033[91m99\033[94m] \033[92mNext Page\n\033[94m[\033[91m00\033[94m] \033[93mBack\n\033[97m>>> "

# Halaman 2
page2 = f"\033[1;94m****     **** *******     **     **\n/**/**   **/**/**////**   //**   ** \n/**//** ** /**/**   /**    //** **  \n/** //***  /**/*******      //***   \n/**  //*   /**/**///**       **/**  \n/**   /    /**/**  //**     ** //** \n/**        /**/**   //**   **   //**\n//         // //     //   //     //\n╔═════════════════════════════════════╗\n║[•] Author : MR-X JUNIOR             ║\n║[•] GitHub : github.com/MR-X-Junior  ║\n║[•] WA.    : +6285754629509          ║\n║[•] UPDATE : {UPDATE}        ║\n║[•] Page   : 2                       ║\n╚═════════════════════════════════════╝\n\033[92mHalaman 2\n\033[97m====================\n\033[94m[\033[91m01\033[94m] {warna()}Base85 & Base64\n\033[94m[\033[91m02\033[94m] {warna()}Base85 & Base32\n\033[94m[\033[91m03\033[94m] {warna()}Base85 & Base16\n\033[94m[\033[91m04\033[94m] {warna()}Base85 & Zlib\n\033[94m[\033[91m05\033[94m] {warna()}Base85 & Marshal\n\033[94m[\033[91m06\033[94m] {warna()}Base85 & lzma\n\033[94m[\033[91m07\033[94m] {warna()}Base85 & bz2\n\033[94m[\033[91m08\033[94m] {warna()}Base85 & Hex\n\033[94m[\033[91m09\033[94m] {warna()}Base64 & Base32\n\033[94m[\033[91m10\033[94m] {warna()}Base64 & Base16\n\033[94m[\033[91m11\033[94m] {warna()}Base64 & zlib\n\033[94m[\033[91m12\033[94m] {warna()}Base64 & Marshal\n\033[94m[\033[91m13\033[94m] {warna()}Base64 & lzma\n\033[94m[\033[91m14\033[94m] {warna()}Base64 & bz2\n\033[94m[\033[91m15\033[94m] {warna()}Base64 & Hex\n\033[94m[\033[91m16\033[94m] {warna()}Base32 & Base16\n\033[94m[\033[91m17\033[94m] {warna()}Base32 & Zlib\n\033[94m[\033[91m18\033[94m] {warna()}Base32 & Marshal\n\033[94m[\033[91m19\033[94m] {warna()}Base32 & lzma\n\033[94m[\033[91m20\033[94m] {warna()}Base32 & bz2\n\033[94m[\033[91m21\033[94m] {warna()}Base32 & Hex\n\033[94m[\033[91m22\033[94m] {warna()}Base16 & zlib\n\033[94m[\033[91m23\033[94m] {warna()}Base16 & Marshal\n\033[94m[\033[91m24\033[94m] {warna()}Base16 & lzma\n\033[94m[\033[91m25\033[94m] {warna()}Base16 & bz2\n\033[94m[\033[91m26\033[94m] {warna()}Base16 & Hex\n\033[94m[\033[91m27\033[94m] {warna()}Zlib & Marshal\n\033[94m[\033[91m28\033[94m] {warna()}Zlib & lzma\n\033[94m[\033[91m29\033[94m] {warna()}Zlib & bz2\n\033[94m[\033[91m30\033[94m] {warna()}Zlib & Hex\n\033[94m[\033[91m31\033[94m] {warna()}Marshal & lzma\n\033[94m[\033[91m32\033[94m] {warna()}Marshal & bz2\n\033[94m[\033[91m33\033[94m] {warna()}Marshal & Hex\n\033[94m[\033[91m34\033[94m] {warna()}lzma & bz2\n\033[94m[\033[91m35\033[94m] {warna()}lzma & Hex\n\033[94m[\033[91m36\033[94m] {warna()}bz2 & Hex\n\033[94m[\033[91m99\033[94m] \033[92mNext Page\n\033[94m[\033[91m00\033[94m] \033[93mBack\n\033[97m>>> \033[91m"

# Halaman 3
page3 = f"\033[1;94m****     **** *******     **     **\n/**/**   **/**/**////**   //**   ** \n/**//** ** /**/**   /**    //** **  \n/** //***  /**/*******      //***   \n/**  //*   /**/**///**       **/**  \n/**   /    /**/**  //**     ** //** \n/**        /**/**   //**   **   //**\n//         // //     //   //     //\n╔═════════════════════════════════════╗\n║[•] Author : MR-X JUNIOR             ║\n║[•] GitHub : github.com/MR-X-Junior  ║\n║[•] WA.    : +6285754629509          ║\n║[•] UPDATE : {UPDATE}        ║\n║[•] Page   : 3                       ║\n╚═════════════════════════════════════╝\n\033[92mHalaman 3\n\033[97m===========================\n\033[94m[\033[91m01\033[94m] {warna()}Base85 & Base64 & Base32\n\033[94m[\033[91m02\033[94m] {warna()}Base85 & Base16 & Zlib\n\033[94m[\033[91m03\033[94m] {warna()}Base85 & Marshal & lzma\n\033[94m[\033[91m04\033[94m] {warna()}Base85 & bz2 & Hex\n\033[94m[\033[91m05\033[94m] {warna()}Base64 & Base32 & Base16\n\033[94m[\033[91m06\033[94m] {warna()}Base64 & Zlib & Marshal\n\033[94m[\033[91m07\033[94m] {warna()}Base64 & lzma & bz2\n\033[94m[\033[91m08\033[94m] {warna()}Base32 & Base16 & zlib\n\033[94m[\033[91m09\033[94m] {warna()}Base32 & Marshal & lzma\n\033[94m[\033[91m10\033[94m] {warna()}Base16 & zlib & Marshal\n\033[94m[\033[91m11\033[94m] {warna()}Base16 & bz2 & lzma\n\033[94m[\033[91m12\033[94m] {warna()}zlib & Marshal & lzma\n\033[94m[\033[91m13\033[94m] {warna()}zlib & bz2 & Hex\n\033[94m[\033[91m14\033[94m] {warna()}Marshal & lzma & bz2\n\033[94m[\033[91m15\033[94m] {warna()}lzma & bz2 & Hex\n\033[94m[\033[91m16\033[94m] \033[92mEnskripsi By Rahmat \033[97m[\033[93mPremium\033[97m]\n\033[94m[\033[91m00\033[94m] \033[93mBack\n\033[97m>>> "

# Get Lokasi External storage
save = env['EXTERNAL_STORAGE']

# lihat Hasil Enskripsi
def show(file=argv[0]):
	try:
		a = isfile(file)
		if a:
			b = sys(f"termux-open --view {file}")
			if b != 0:
				print (f"\033[0m{basename(argv[0])} : Terjadi Kesalahan {b} :(")
				sleep(1)
			else:
				sleep(1)
		else:
			print (f"\033[94m[\033[91m!\033[94m] \033[93mFile \033[91m{file} \033[93mNot Found")
			sleep(1)
	except FileNotFoundError:
		print (f"\033[94m[\033[91m!\033[94m] \033[4m{file} \033[93mNot Found")
		sleep(0.1)

#Convert Bytes
def convert_bytes(num):
    for x in ['bytes', 'KB', 'MB', 'GB', 'TB']:
        if num < 1024.0:
            return "%3.1f %s" % (num, x)
        num /= 1024.0

# File Size
def file_size(file_path):
    if isfile(file_path):
        file_info = stat(file_path)
        return convert_bytes(file_info.st_size)
        
info_sc = lambda : print (f"{logo}\n\033[92mINFO SCRIPT\n========================\n\033[94m[\033[93m✓\033[94m] \033[96mAuthor: \033[92mRahmat adha\n\033[94m[\033[93m✓\033[94m] \033[96mTeam  : {warna()}TNT {warna()}ANONYMOUS \033[91mINDO\033[97mNESIA\n\033[94m[\033[93m✓\033[94m] \033[96mScript: {warna()}{basename(argv[0])}\n\033[94m[\033[93m✓\033[94m] \033[96mPath  : {realpath(argv[0])}\n\033[94m[\033[93m✓\033[94m] \033[96mSize  : {file_size(realpath(argv[0]))}\n\033[94m[\033[93m✓\033[94m] \033[96mLink  : {warna()}https://github.com/MR-X-Junior/enc\n\033[94m[\033[93m✓\033[94m] \033[96mUpdate: {warna()}{UPDATE}\n\033[94m[\033[93m✓\033[94m] \033[96mVersi : 0.1\n\n\033[92mContact Me ^_^\n==================\n\033[94m[\033[93m✓\033[94m] \033[96mGithub: {warna()}https://github.com/MR-X-Junior/\n\033[94m[\033[93m✓\033[94m] \033[96mFb.   : {warna()}https://www.facebook.com/Anjay.pro098\n\033[94m[\033[93m✓\033[94m] \033[96mWa.   : {warna()}+62 85754629509\n\033[94m[\033[93m✓\033[94m] \033[96mEmail : {warna()}termux.indonesia01@gmail.com\n")

def info_sys():
	try:
		 print (f"{logo}\n\033[92mINFO SYSTEM\n=================\n\033[94m[\033[93m✓\033[94m] \033[96mOS : {warna()}{platform}\n\033[94m[\033[93m✓\033[94m] \033[96mPython : {warna()}{version[0:6]}\n\033[94m[\033[93m✓\033[94m] \033[96mNodeName : {warna()}{uname().nodename}\n\033[94m[\033[93m✓\033[94m] \033[96mrelease : {warna()}{uname().release}\n\033[94m[\033[93m✓\033[94m] \033[96mVersion : {warna()}{uname().version}")
	except Exception as err:
		print (f"\033[94m[\033[93m!\033[94m] \033[93mTerjadi Kesalahan :(")
	else:
		 for me in env:
			 print (f"\033[94m[\033[93m✓\033[94m] \033[96m{me} : {warna()}{env[me]}")

# Acak Nama File 		
def acak():
	random = ''.join(choice(low) for me in range(choice([2,3,4])))
	simpan = f"{random}.py"
	return simpan

# Simpan Hasil Enskripsi
def simpan(body):
	a = access(save,ok)
	if a:
		with open(acak(),'w') as b:
			b.write(body)
			print (f"\033[92m[✓] Nama File : {basename(b.name)}\n[✓] Ukuran : {file_size(b.name)}\n[✓] File Tersimpan Di : {env['PWD']}/{b.name}")
			
	else:
		raise PermissionError(f"\033[94m[\033[91m!\033[94m] \033[93mGagal Mengakses \033[91m{save}")
    
#Input Lokasi File
def file():
	try:
		while True:
			a = input('\033[94m[\033[91m?\033[94m] \033[92mFile : \033[93m')
			try:
				b = isdir(a)
				if b:
					print ("\033[94m[\033[91m!\033[94m] \033[93mGak Bisa Enskripsi Folder Bang :(")
					sleep(0.3)
				else:
					c = open(a,'r').read()
					if len(c) == 0:
						print (f"\033[94m[\033[91m!\033[94m] \033[91mEnskripsi Gagal :(")
						sleep(0.1)
					else:
						return c
			except UnicodeDecodeError:
				print (f'\033[91m[!] File {basename(a)} Tidak Di Dukung\n[!] Coba File Yang Lain')
				sleep(0.1)
			except FileNotFoundError:
				print ('[!]',a,'\033[93mNot Found')
	except (KeyboardInterrupt , EOFError):
		exit('\033[91mexit')
		
# input Lokasi Folder
def folder():
	enc = []
	File = 0
	Fol = 0
	try:
		while True:
			a = input('\033[94m[\033[91m?\033[94m] \033[92mFolder : \033[93m')
			if bool(a) != True:
				print (f"\033[94m[\033[91m!\033[94m] \033[93mIsi Dengan Benar")
				sleep(0.1)
			else:
				try:
					b = isfile(a)
					if b:
						print (f"\033[94m[\033[91m!\033[94m] \033[93mFolder Bang Bukan File {warna()}{basename(a)} :(")
						sleep(0.1)
					else:
						if '/' not in a[-1]:
							c = a+'/'
						else:
							c = a
						d = listdir(c)
						for x in d:
							e = isfile(c+x)
							if e:
								try:
									ab = open(c+x).read()
									if len(ab) == 0:
										print (f"\033[94m[\033[91m!\033[94m] \033[93mFile {warna()}{c+x} \033[93mTidak Valid")
										sleep(0.1)
										File += 1
									else:
										enc.append(c+x)
										File += 1
								except UnicodeDecodeError:
									print (f"\033[94m[\033[91m!\033[94m] \033[93mFile {warna()}{basename(c+x)} \033[93mTidak Di Dukung")
									sleep(0.1)
									File += 1
							else:
								Fol += 1
						if File == 0:
							print (f"\033[94m[\033[91m!\033[94m] \033[93mTotal File : {warna()}{File}\n\033[94m[\033[91m!\033[94m] \033[93mTotal Folder : {warna()}{Fol}\n\033[94m[\033[91m!\033[94m] \033[92mStatus : {warna()}Enskripsi Gagal :(")
							sleep(1)
							File = 0
							Fol = 0
						else:
							info = {"Path":c,
										"File":enc}
							return info
						
				except FileNotFoundError:
					print (f"\033[93m[!] {warna()}{a} \033[93mNot Found")
					sleep(0.1)
	except PermissionError:
		print (f"\033[93m[!] {warna()}{a} \033[93mPermission Error")
		sleep(1)
		folder()
	except (EOFError , KeyboardInterrupt):
		exit('exit')
    
#Enskripsi Base85
def b85(code):
    a = b85encode(bytes(code,'utf-8'))
    b = a.decode('utf-8')
    c = f"#coding=utf-8\n#enskripsi By Rahmat\n#Di Buat Pada {ctime()}\nimport base64\nexec(base64.b85decode('{b}'))"
    return c

#Enskripsi Base64
def b64(code):
	a = b64encode(bytes(code,'utf-8'))
	b = a.decode('utf-8')
	c = f"#coding=utf-8\n#enskripsi By Rahmat\n#Di Buat Pada {ctime()}\nimport base64\nexec(base64.b64decode('{b}'))"
	return c

#Enskripsi Base32
def b32(code):
	a = b32encode(bytes(code,'utf-8'))
	b = a.decode('utf-8')
	c = f"#coding=utf-8\n#enskripsi By Rahmat\n#Di Buat Pada {ctime()}\nimport base64\nexec(base64.b32decode('{b}'))"
	return c

#Enskripsi Base16
def b16(code):
	a = b16encode(bytes(code,'utf-8'))
	b = a.decode('utf-8')
	c = f"#coding=utf-8\n#enskripsi By Rahmat\n#Di Buat Pada {ctime()}\nimport base64\nexec(base64.b16decode('{b}'))"
	return c

#Enskripsi Marshal
def marshal(code):
	a = compile(code,'<Ayu Putri>','exec')
	b = dumps(a)
	c = repr(b)
	d = f"#coding=utf-8\n#enskripsi By Rahmat\n#Di Buat Pada {ctime()}\nimport marshal\nexec(marshal.loads({c}))"
	return d

#Enskripsi zlib
def zlib(code):
	a = compress(bytes(code,'utf-8'))
	b = f"#coding=utf-8\n#enskripsi By Rahmat\n#Di Buat Pada {ctime()}\nimport zlib\nexec(zlib.decompress({a}))"
	return b

#Enskripsi bz2
def bz(code):
	a = bz2(bytes(code,'utf-8'))
	b = f"#coding=utf-8\n#enskripsi By Rahmat\n#Di Buat Pada {ctime()}\nimport bz2\nexec(bz2.decompress({a}))"
	return b

#Enskripsi Hex
def Hex(code):
	a = hexlify(bytes(code,'utf-8'))
	b = a.decode('utf-8')
	c = f"#coding=utf-8\n#enskripsi By Rahmat\n#Di Buat Pada {ctime()}\nimport binascii\nexec(binascii.unhexlify('{b}'))"
	return c

#Enskripsi lzma
def lz(code):
	a = lzma(bytes(code,'utf-8'))
	b = f"#coding=utf-8\n#enskripsi By Rahmat\n#Di Buat Pada {ctime()}\nimport lzma\nexec(lzma.decompress({a}))"
	return b

#Enskripsi String
def string(code,huruf):
	a = []
	b = []
	for x in code:
		if len(code) < 30000:
			print (f"\033[94m[\033[91m!\033[94m] {warna()}{x} {warna()}> {warna()}{ord(x)}",end = '\n')
			a.append(ord(x))
		else:
			a.append(ord(x))
	else:
		for x in a:
			b.append(huruf.replace("'","").replace('"','')*x)
		else:
			data = '#coding=utf-8\n#Enskripsi By Rahmat\n#Di Buat Pada : {}\n#String : {}\ndata={};exec("".join([chr(len(i)) for i in data]))'.format(ctime(),huruf,b)
			simpan(data)
			

#Pycompile
def py():
	out = acak()+'c'
	path = input('\033[94m[\033[91m?\033[94m] \033[92mFile : \033[97m')
	if isfile(path):
		pycompile(path,out)
		print (f'\033[92m[✓] File Tersimpan : {out}')
	else:
		print ("[!]",path,"Not Found")
		sleep(0.6) ; py()
		
# Simpan Hasil Enskripsi Dir
def saveDir(body , folder = 'HasilEnskripsi'):
	a = access(save,ok)
	file = f"{folder}/{acak()}"
	try:
		mkdir(folder)
	except FileExistsError:
		pass
	if a:
		with open(file,'w') as b:
			b.write(body)
			print (f"\033[92m[✓] Nama File : {basename(b.name)}\n[✓] Ukuran : {file_size(b.name)}\n[✓] File Tersimpan Di : {b.name}\n")
			
# Enskripsi 2 lapis :v
def dua_lapis(a,b,c,d,e1,e2):
	A = a(bytes(c,'utf-8'))
	B = b(A)
	C = f'#Enskripsi By Rahmat\n#Di Buat Pada {ctime()}\nimport {d}\nexec({e1}({e2}({B})))'
	return C
	#simpan(dua_lapis(a = b64encode , b = b32encode , c = file() , d = 'base64' , e1 = "base64.b64decode" , e2 = "base64.b32decode"))
	
def tiga_lapis(a,b,c,d,e,e1,e2,e3):
	abc = marshal(d)
	A = a(bytes(abc,'utf-8'))
	B = b(A)
	C = c(B)
	D = f'#Enskripsi By Rahmat\n#Di Buat Pada {ctime()}\nimport {e}\nexec({e1}({e2}({e3}({C}))))'
	return D
	#tiga_lapis(a = b85encode , b = b64encode , c = b32encode , d = file() , e = 'base64' , e1 = 'base64.b85decode' , e2 = 'base64.b64decode' , e3 = 'base64.b32decode')
	
# Menu Utama
def menu():
	sys('clear')
	try:
		a = int(input(f"\033[1;94m****     **** *******     **     **\n/**/**   **/**/**////**   //**   ** \n/**//** ** /**/**   /**    //** **  \n/** //***  /**/*******      //***   \n/**  //*   /**/**///**       **/**  \n/**   /    /**/**  //**     ** //** \n/**        /**/**   //**   **   //**\n//         // //     //   //     //\n╔═════════════════════════════════════╗\n║[•] Author : MR-X JUNIOR             ║\n║[•] GitHub : github.com/MR-X-Junior  ║\n║[•] WA.    : +6285754629509          ║\n║[•] UPDATE : {UPDATE}        ║\n╚═════════════════════════════════════╝\n\033[92mPython 3\n\033[0m================\n\033[94m[\033[91m01\033[94m] {warna()}Compile File py\n\033[94m[\033[91m02\033[94m] \033[93mCompile File py \033[97m[\033[95mcostumize\033[97m]\n\033[94m[\033[91m03\033[94m] {warna()}Compile Dir\n\033[94m[\033[91m04\033[94m] \033[97mINFO\n\033[94m[\033[91m00\033[94m] \033[91mKeluar\n\033[97m>>> \033[0m"))
		if a == 1:
			menu1_file()
		elif a == 2:
			print ("\033[94m[\033[91m?\033[94m] \033[93mTekan Enter Untuk Skip")
			while True:
				try:
					a = int(input('\033[94m[\033[91m?\033[94m] \033[93mEnskripsi Berapa lapis : \033[93m'))
					costom(lapis = a , code = file())
					break
				except ValueError:
					print ("\033[94m[\033[91m!\033[94m] \033[93mInput Berupa angka")
					sleep(0.1)
		elif a == 3:
			menu_dir()
		elif a == 4:
			while True:
				sys('clear')
				try:
					a = int(input(f"{logo}\n\033[94m[\033[93m01\033[94m] {warna()}INFO SCRIPT\n\033[94m[\033[93m02\033[94m] {warna()}INFO SYSTEM\n\033[94m[\033[93m00\033[94m] \033[93mBack\n\033[97m>>> \033[0m"))
					if  bool(a) == False:
						sleep(0.5)
						menu()
					elif a == 1:
						sleep(0.5)
						sys('clear')
						info_sc()
						break
					elif a == 2:
						sleep(0.5)
						sys('clear')
						info_sys()
						break
					else:
						print ("\033[94m[\033[93m!\033[94m] \033[91mIsi Dengan Benar")
						sleep(0.5)
				except ValueError:
					print ("\033[94m[\033[93m!\033[94m] \033[93mInput Berupa angka")
					sleep(1.5)
		elif a == 0:
			exit ('exit')
		else:
			print ("\033[94m[\033[91m!\033[94m] \033[93mPilihan Tidak Tersedia")
			sleep(2)
			menu()
	except ValueError:
		print ("\033[94m[\033[91m!\033[94m] \033[93mInput Berupa angka")
		sleep(2)
		menu()
	except (KeyboardInterrupt , EOFError):
		exit("exit")
		
def costom(lapis, code):
	ayu = str(code)
	int (lapis)
	Data = []
	Data.append(ayu)
	while lapis != 0:
		sleep(0.001)
		sys('clear')
		sleep(0.001)
		try:
			a = int(input(f"\033[1;91m                                 \n@@@@@@@@@@   @@@@@@@      @@@  @@@  \n@@@@@@@@@@@  @@@@@@@@     @@@  @@@  \n@@! @@! @@!  @@!  @@@     @@!  !@@  \n!@! !@! !@!  !@!  @!@     !@!  @!!  \n@!! !!@ @!@  @!@!!@!       !@@!@!   \n!@!   ! !@!  !!@!@!         @!!!    \n!!:     !!:  !!: :!!       !: :!!   \n:!:     :!:  :!:  !:!     :!:  !:!  \n:::     ::   ::   :::      ::  :::  \n:      :     :   : :      :   ::                                  \n╔═════════════════════════════════════╗\n║[•] Author : MR-X JUNIOR             ║\n║[•] GitHub : github.com/MR-X-Junior  ║\n║[•] WA.    : +6285754629509          ║\n║[•] UPDATE : 12-12-2020 20:35        ║\n║[•] Total  : {lapis}                      ║\n╚═════════════════════════════════════╝\n\033[92mPython {version[0:6]}\n\033[0m==============\n\033[94m[\033[91m1\033[94m] {warna()}Base85\n\033[94m[\033[91m2\033[94m] {warna()}Base64\n\033[94m[\033[91m3\033[94m] {warna()}Base32\n\033[94m[\033[91m4\033[94m] {warna()}Base16\n\033[94m[\033[91m5\033[94m] {warna()}Zlib\n\033[94m[\033[91m6\033[94m] {warna()}Marshal\n\033[94m[\033[91m7\033[94m] {warna()}lzma\n\033[94m[\033[91m8\033[94m] {warna()}bz2\n\033[94m[\033[91m9\033[94m] {warna()}Hex\n\033[94m[\033[91m0\033[94m] \033[93mBack\n\033[97m>>> \033[0m"))
			if a == 1:
				Data.append(b85(Data[-1]))
				lapis -= 1
				print (f"\033[92m[✓] Jenis Enskripsi : {warna()}Base85\n[✓] Total karakter : {warna()}{len(Data[-1])}\n[✓] Status : Sukses :)")
				sleep(1.5)
			elif a == 2:
				Data.append(b64(Data[-1]))
				lapis -= 1
				print (f"\033[92m[✓] Jenis Enskripsi : {warna()}Base64\n[✓] Total karakter : {warna()}{len(Data[-1])}\n[✓] Status : Sukses :)")
				sleep(1.5)
			elif a == 3:
				Data.append(b32(Data[-1]))
				lapis -= 1
				print (f"\033[92m[✓] Jenis Enskripsi : {warna()}Base32\n[✓] Total karakter : {warna()}{len(Data[-1])}\n[✓] Status : Sukses :)")
				sleep(1.5)
			elif a == 4:
				Data.append(b16(Data[-1]))
				lapis -= 1
				print (f"\033[92m[✓] Jenis Enskripsi : {warna()}Base16\n[✓] Total karakter : {warna()}{len(Data[-1])}\n[✓] Status : Sukses :)")
				sleep(1.5)
			elif a == 5:
				Data.append(zlib(Data[-1]))
				lapis -= 1
				print (f"\033[92m[✓] Jenis Enskripsi : {warna()}zlib\n[✓] Total karakter : {warna()}{len(Data[-1])}\n[✓] Status : Sukses :)")
				sleep(1.5)
			elif a == 6:
				Data.append(marshal(Data[-1]))
				lapis -= 1
				print (f"\033[92m[✓] Jenis Enskripsi : {warna()}Marshal\n[✓] Total karakter : {warna()}{len(Data[-1])}\n[✓] Status : Sukses :)")
				sleep(1.5)
			elif a == 7:
				Data.append(lz(Data[-1]))
				lapis -= 1
				print (f"\033[92m[✓] Jenis Enskripsi : {warna()}lzma\n[✓] Total karakter : {warna()}{len(Data[-1])}\n[✓] Status : Sukses :)")
				sleep(1.5)
			elif a == 8:
				Data.append(bz(Data[-1]))
				lapis -= 1
				print (f"\033[92m[✓] Jenis Enskripsi : {warna()}bz2\n[✓] Total karakter : {warna()}{len(Data[-1])}\n[✓] Status : Sukses :)")
				sleep(1.5)
			elif a == 9:
				Data.append(Hex(Data[-1]))
				lapis -= 1
				print (f"\033[92m[✓] Jenis Enskripsi : {warna()}Hexlify\n[✓] Total karakter : {warna()}{len(Data[-1])}\n[✓] Status : Sukses :)")
				sleep(1.5)
			elif a == 0:
				b = input("\033[94m[\033[91m!\033[94m] \033[93mEnskripsi Akan Di Batalkan\n\033[94m[\033[91m?\033[94m] \033[93mYakin Ingin Melanjutkan \033[97m[\033[92mY\033[95m/\033[91mn\033[97m] \033[0m").lower()
				if b == 'y':
					sys('clear')
					menu()
					break
				else:
					sys ('clear')
		except ValueError:
			print ("\033[94m[\033[91m!\033[94m] \033[93mInput Berupa Angka")
			sys('clear')
		except (KeyboardInterrupt , EOFError):
			print ("\033[94m[\033[91m!\033[94m] \033[93mMo Ke mana Lagi lu ?")
			sleep(2.5)
			sys('clear')
	else:
		simpan(Data[-1])
		
#Menu Compile Dir
def menu_dir():
	sys('clear')
	try:
		a = int(input(f"\033[1;94m****     **** *******     **     **\n/**/**   **/**/**////**   //**   ** \n/**//** ** /**/**   /**    //** **  \n/** //***  /**/*******      //***   \n/**  //*   /**/**///**       **/**  \n/**   /    /**/**  //**     ** //** \n/**        /**/**   //**   **   //**\n//         // //     //   //     //\n╔═════════════════════════════════════╗\n║[•] Author : MR-X JUNIOR             ║\n║[•] GitHub : github.com/MR-X-Junior  ║\n║[•] WA.    : +6285754629509          ║\n║[•] UPDATE : {UPDATE}        ║\n╚═════════════════════════════════════╝\n\033[94m[\033[91m01\033[94m] {warna()}Base85 \n\033[94m[\033[91m02\033[94m] {warna()}Base64 \n\033[94m[\033[91m03\033[94m] {warna()}Base32 \n\033[94m[\033[91m04\033[94m] {warna()}Base16 \n\033[94m[\033[91m05\033[94m] {warna()}Zlib \n\033[94m[\033[91m06\033[94m] {warna()}Marshal \n\033[94m[\033[91m07\033[94m] {warna()}lzma \n\033[94m[\033[91m08\033[94m] {warna()}bz2 \n\033[94m[\033[91m09\033[94m] {warna()}Hex \n\033[94m[\033[91m10\033[94m] {warna()}pyc\n\033[94m[\033[91m99\033[94m] \033[93mBack\n\033[97m>>> \033[0m"))
		if a == 1:
			get = folder()
			print ('\n')
			for x in get['File']:
				y = x
				print (warna()+y)
				saveDir(body = b85(open(y).read()))
		elif a == 2:
			get = folder()
			print ('\n')
			for x in get['File']:
				y = x
				print (warna()+y)
				saveDir(body = b64(open(y).read()))
		elif a == 3:
			get = folder()
			print ('\n')
			for x in get['File']:
				y = x
				print (warna()+y)
				saveDir(body = b32(open(y).read()))
		elif a == 4:
			get = folder()
			print ('\n')
			for x in get['File']:
				y = x
				print (warna()+y)
				saveDir(body = b16(open(y).read()))
		elif a == 5:
			get = folder()
			print ('\n')
			for x in get['File']:
				y = x
				print (warna()+y)
				saveDir(body = zlib(open(y).read()))
		elif a == 6:
			get = folder()
			print ('\n')
			for x in get['File']:
				y = x
				print (warna()+y)
				saveDir(body = marshal(open(y).read()))
		elif a == 7:
			get = folder()
			print ('\n')
			for x in get['File']:
				y = x
				print (warna()+y)
				saveDir(body = lz(open(y).read()))
		elif a == 8:
			get = folder()
			print ('\n')
			for x in get['File']:
				y = x
				print (warna()+y)
				saveDir(body = bz(open(y).read()))
		elif a == 9:
			get = folder()
			print ('\n')
			for x in get['File']:
				y = x
				print (warna()+y)
				saveDir(body = Hex(open(y).read()))
		elif a == 10:
			get = folder()
			print ('\n')
			for x in get['File']:
				y = x
				try:
					mkdir ('Pycompile')
				except FileExistsError:
					pass
				out = f"{get['Path']}Pycompile/{acak()}"
				print ('\033[94m[\033[91m!\033[94m] \033[93mCompiling :',warna(),y,end='\r')
				try:
					pycompile(y,out)
				except:
					print (f"\033[94m[\033[91m!\033[94m] \03[91mGagal {y}")
		elif a == 99:
			sleep(0.1)
			menu()
		else:
			print ('\033[94m[\033[91m!\033[94m] \033[93mPilihan Tidak Tersedia')
			sleep(0.5)
			menu_dir()
	except ValueError:
		print ("\033[94m[\033[91m!\033[94m] \033[93mInput Berupa angka")
		sleep(2)
		menu_dir()
	except (EOFError , KeyboardInterrupt):
		exit('exit')
		
# Menu 1
def menu1_file():
	sys('clear')
	try:
		a = int(input(f"{page1}"))
		if a == 1:
			simpan(b85(file()))
		elif a == 2:
			simpan(b64(file()))
		elif a == 3:
			simpan(b32(file()))
		elif a == 4:
			simpan(b16(file()))
		elif a == 5:
			simpan(zlib(file()))
		elif a == 6:
			simpan(marshal(file()))
		elif a == 7:
			simpan(lz(file()))
		elif a == 8:
			simpan(bz(file()))
		elif a == 9:
			simpan(Hex(file()))
		elif a == 10:
			py()
		elif a == 11:
			a = file()
			c = low + low.upper()
			while True:
				b = input(f'\033[94m[\033[91m?\033[94m] \033[93mString : {warna()}')
				if len(b) == 0:
					print ("\033[94m[\033[91m!\033[94m] \033[93mGak Boleh Kosong :(")
					sleep(0.5)
				elif len(b) > 1:
					print ('\033[94m[\033[91m!\033[94m] \033[93mMaksimal Hanya "Satu" karakter')
					sleep(0.5)
				elif ' ' in b[0]:
					print ("\033[94m[\033[91m!\033[94m] \033[93mGak Boleh Pake Spasi :(")
					sleep(0.5)
				elif b[0] not in c:
					print (f"\033[94m[\033[91m!\033[94m] \033[93mHanya Boleh Menggunakan string contoh : {warna()}{choice(c)}")
					sleep(0.5)
				else:
					string(a,b)
					break
		elif a == 0:
			menu()
		elif a == 99:
			menu2_file()
		else:
			print ("\033[94m[\033[91m!\033[94m] \033[93mPilihan Tidak Tersedia")
			sleep(1.5) ; menu1_file()
	except ValueError:
		print ("\033[94m[\033[91m!\033[94m] \033[93mInput Berupa Angka")
		sleep(1.5)
		menu1_file()
	except (EOFError , KeyboardInterrupt):
		exit('exit')

#Menu2
def menu2_file():
	sys('clear')
	try:
		a = int(input(f"{page2}"))
		if a == 1:
			simpan(dua_lapis(a = b85encode , b = b64encode , c = file() , d = 'base64' , e1 = "base64.b85decode" , e2 = "base64.b64decode"))
		elif a == 2:
			simpan(dua_lapis(a = b85encode , b = b32encode , c = file() , d = 'base64' , e1 = "base64.b85decode" , e2 = "base64.b32decode"))
		elif a == 3:
			simpan(dua_lapis(a = b85encode , b = b16encode , c = file() , d = 'base64' , e1 = "base64.b85decode" , e2 = "base64.b16decode"))
		elif a == 4:
			simpan(dua_lapis(a = b85encode , b = compress , c = file() , d = 'base64 , zlib' , e1 = "base64.b85decode" , e2 = "zlib.decompress"))
		elif a == 5:
			simpan(b85(marshal(file())))
		elif a == 6:
			simpan(dua_lapis(a = b85encode , b = lzma , c = file() , d = 'base64 , lzma' , e1 = "base64.b85decode" , e2 = "lzma.decompress"))
		elif a == 7:
			simpan(dua_lapis(a = b85encode , b = bz2 , c = file() , d = 'base64 , bz2' , e1 = "base64.b85decode" , e2 = "bz2.decompress"))
		elif a == 8:
			simpan(dua_lapis(a = b85encode , b = hexlify , c = file() , d = 'base64,binascii' , e1 = "base64.b85decode" , e2 = "binascii.unhexlify"))
		elif a == 9:
			simpan(dua_lapis(a = b64encode , b = b32encode , c = file() , d = 'base64' , e1 = "base64.b64decode" , e2 = "base64.b32decode"))
		elif a == 10:
			simpan(dua_lapis(a = b64encode , b = b16encode , c = file() , d = 'base64' , e1 = "base64.b64decode" , e2 = "base64.b16decode"))
		elif a == 11:
			simpan(dua_lapis(a = b64encode , b = compress , c = file() , d = 'base64 , zlib' , e1 = "base64.b64decode" , e2 = "zlib.decompress"))
		elif a == 12:
			simpan(b64(marshal(file())))
		elif a == 13:
			simpan(dua_lapis(a = b64encode , b = lzma , c = file() , d = 'base64 , lzma' , e1 = "base64.b64decode" , e2 = "lzma.decompress"))
		elif a == 14:
			simpan(dua_lapis(a = b64encode , b = bz2 , c = file() , d = 'base64 , bz2' , e1 = "base64.b64decode" , e2 = "bz2.decompress"))
		elif a == 15:
			simpan(dua_lapis(a = b64encode , b = hexlify , c = file() , d = 'base64,binascii' , e1 = "base64.b64decode" , e2 = "binascii.unhexlify"))
		elif a == 16:
			simpan(dua_lapis(a = b32encode , b = b16encode , c = file() , d = 'base64' , e1 = "base64.b32decode" , e2 = "base64.b16decode"))
		elif a == 17:
			simpan(dua_lapis(a = b32encode , b = compress , c = file() , d = 'base64 , zlib' , e1 = "base64.b32decode" , e2 = "zlib.decompress"))
		elif a == 18:
			simpan(b32(marshal(file())))
		elif a == 19:
			simpan(dua_lapis(a = b32encode , b = lzma , c = file() , d = 'base64 , lzma' , e1 = "base64.b32decode" , e2 = "lzma.decompress"))
		elif a == 20:
			simpan(dua_lapis(a = b32encode , b = bz2 , c = file() , d = 'base64 , bz2' , e1 = "base64.b32decode" , e2 = "bz2.decompress"))
		elif a == 21:
			simpan(dua_lapis(a = b32encode , b = hexlify , c = file() , d = 'base64,binascii' , e1 = "base64.b32decode" , e2 = "binascii.unhexlify"))
		elif a == 22:
			simpan(dua_lapis(a = b16encode , b = compress , c = file() , d = 'base64 , zlib' , e1 = "base64.b16decode" , e2 = "zlib.decompress"))
		elif a == 23:
			simpan(b16(marshal(file())))
		elif a == 24:
			simpan(dua_lapis(a = b16encode , b = lzma , c = file() , d = 'base64 , lzma' , e1 = "base64.b16decode" , e2 = "lzma.decompress"))
		elif a == 25:
			simpan(dua_lapis(a = b16encode , b = bz2 , c = file() , d = 'base64 , bz2' , e1 = "base64.b16decode" , e2 = "bz2.decompress"))
		elif a == 26:
			simpan(dua_lapis(a = b16encode , b = hexlify , c = file() , d = 'base64,binascii' , e1 = "base64.b16decode" , e2 = "binascii.unhexlify"))
		elif a == 27:
			simpan(zlib(marshal(file())))
		elif a == 28:
			simpan(dua_lapis(a = compress , b = lzma , c = file() , d = 'zlib,lzma' , e1 = "zlib.decompress" , e2 = "lzma.decompress"))
		elif a == 29:
			simpan(dua_lapis(a = compress , b = bz2 , c = file() , d = 'zlib,bz2' , e1 = "zlib.decompress" , e2 = "bz2.decompress"))
		elif a == 30:
			simpan(dua_lapis(a = compress , b = hexlify , c = file() , d = 'zlib\nimport binascii' , e1 = "zlib.decompress" , e2 = "binascii.unhexlify"))
		elif a == 31:
			simpan(lz(marshal(file())))
		elif a == 32:
			simpan(bz(marshal(file())))
		elif a == 33:
			simpan(Hex(marshal(file())))
		elif a == 34:
			simpan(dua_lapis(a = lzma , b = bz2 , c = file() , d = 'lzma\nimport bz2' , e1 = "lzma.decompress" , e2 = "bz2.decompress"))
		elif a == 35:
			simpan(dua_lapis(a = lzma , b = hexlify , c = file() , d = 'lzma\nimport binascii' , e1 = "lzma.decompress" , e2 = "binascii.unhexlify"))
		elif a == 36:
			simpan(dua_lapis(a = bz2 , b = hexlify , c = file() , d = 'bz2\nimport binascii' , e1 = "bz2.decompress" , e2 = "binascii.unhexlify"))
		elif a == 0:
			menu1_file()
		elif a == 99:
			menu3_file()
		else:
			print ("\033[94m[\033[91m!\033[94m] \033[93mPilihan Tidak Tersedia")
			sleep(1.5)
			menu2_file()
	except ValueError:
		print ("\033[94m[\033[91m!\033[94m] \033[93mInput Berupa Angka")
		sleep(1.5) ; menu2_file()
	except EOFError:
		menu1_file()
		
def menu3_file():
	sys('clear')
	try:
		a = int(input(page3))
		if a == 1:
			simpan(tiga_lapis(a = b85encode , b = b64encode , c = b32encode , d = file() , e = 'base64' , e1 = 'base64.b85decode' , e2 = 'base64.b64decode' , e3 = 'base64.b32decode'))
		elif a == 2:
			simpan(tiga_lapis(a = b85encode , b = b16encode , c = compress , d = file() , e = 'base64 , zlib' , e1 = 'base64.b85decode' , e2 = 'base64.b16decode' , e3 = 'zlib.decompress'))
		elif a == 3:
			a = marshal(file())
			b = dua_lapis(a = b85encode , b = lzma , c = a , d = "base64,lzma" , e1 = "base64.b85decode" , e2 = "lzma.decompress")
			simpan(marshal(b))
		elif a == 4:
			simpan(tiga_lapis(a = b85encode , b = bz2 , c = hexlify , d = file() , e = 'base64,bz2,binascii' , e1 = 'base64.b85decode' , e2 = 'bz2.decompress' , e3 = 'binascii.unhexlify'))
		elif a == 5:
			simpan(tiga_lapis(a = b85encode , b = b32encode , c = b16encode , d = file() , e = 'base64' , e1 = 'base64.b85decode' , e2 = 'base64.b32decode' , e3 = 'base64.b16decode'))
		elif a == 6:
			a = marshal(file())
			b = dua_lapis(a = b64encode , b = compress , c = a , d = "base64,zlib" , e1 = "base64.b64decode" , e2 = "zlib.decompress")
			simpan(marshal(b))
		elif a == 7:
			simpan(tiga_lapis(a = b64encode , b = lzma , c = bz2 , d = file() , e = 'base64,lzma,bz2' , e1 = 'base64.b64decode' , e2 = 'lzma.decompress' , e3 = 'bz2.decompress'))
		elif a == 8:
			simpan(tiga_lapis(a = b32encode , b = b16encode , c = compress , d = file() , e = 'base64,zlib' , e1 = 'base64.b32decode' , e2 = 'base64.b16decode' , e3 = 'zlib.decompress'))
		elif a == 9:
			a = marshal(file())
			b = dua_lapis(a = b32encode , b = lzma , c = a , d = "base64,lzma" , e1 = "base64.b32decode" , e2 = "lzma.decompress")
			simpan(marshal(b))
		elif a == 10:
			a = marshal(file())
			b = dua_lapis(a = b16encode , b = compress , c = a , d = "base64,zlib" , e1 = "base64.b16decode" , e2 = "zlib.decompress")
			simpan(marshal(b))
		elif a == 11:
			simpan(tiga_lapis(a = b16encode , b = lzma , c = bz2 , d = file() , e = 'base64,lzma,bz2' , e1 = 'base64.b16decode' , e2 = 'lzma.decompress' , e3 = 'bz2.decompress'))
		elif a == 12:
			a = marshal(file())
			b = dua_lapis(a = compress , b = lzma , c = a , d = "lzma,zlib" , e1 = "zlib.decompress" , e2 = "lzma.decompress")
			simpan(marshal(b))
		elif a == 13:
			simpan(tiga_lapis(a = compress , b = bz2 , c = hexlify , d = file() , e = 'binascii,bz2,zlib' , e1 = 'zlib.decompress' , e2 = 'bz2.decompress' , e3 = 'binascii.unhexlify'))
		elif a == 14:
			a = marshal(file())
			b = dua_lapis(a = lzma , b = bz2 , c = a , d = "lzma,bz2" , e1 = "lzma.decompress" , e2 = "bz2.decompress")
			simpan(marshal(b))
		elif a == 15:
			simpan(tiga_lapis(a = lzma , b = bz2 , c = hexlify , d = file() , e = 'binascii,bz2,lzma' , e1 = 'lzma.decompress' , e2 = 'bz2.decompress' , e3 = 'binascii.unhexlify'))
		elif a == 0:
			menu2_file()
		elif a == 16:
			login()
		else:
			print ("\033[94m[\033[91m!\033[94m] \033[93mPilihan Tidak Tersedia")
			sleep(1.5)
			menu3_file()
	except ValueError:
		print ("\033[94m[\033[91m!\033[94m] \033[93mInput Berupa Angka")
		sleep(1.5) ; menu3_file()
	except EOFError:
		menu2_file()

def login():
	string = '?'
	save = acak()
	ayu = True
	sys ('clear')
	total = 0
	print (logo)
	coba = 0
	print (f"\033[94m[\033[93m?\033[94m] \033[97mUsername : {warna()}{getuser()}")
	try:
		while ayu:
			coba += 1
			pwd = getpass(f"\033[94m[\033[93m?\033[94m] \033[97mPassword : {warna()}")
			print ("\033[94m[\033[93m!\033[94m] \033[97mSedang Login")
			sleep(0.2)
			if len(pwd) == 0:
				total += 1
				print ("\033[94m[\033[93m!\033[94m] \033[93mPassword Tidak Valid :(")
				sleep(0.5)
			elif pwd != urlopen('https://pastebin.com/raw/YVyxMsqW').read().decode('utf-8'):
				total += 1
				print ("\033[94m[\033[93m!\033[94m] \033[91mPassword Salah :(")
				sleep(0.5)
				if coba == 3:
					tik = int(total+coba/2)
					while coba == 3:
						if tik == 0:
							coba = 0
						else:
							tik -= 1
							print ("\033[94m[\033[93m!\033[94m] \033[92mCoba Lagi Dalam :",warna(),tik,end='\r')
							sleep(1)
					else:
						print ("\033[92m[✓] Silahkan Coba Lagi ^_^")
						sleep(0.5)
			else:
				print ("\033[92m[✓] Selamat Datang Bang :)")
				sleep(1.5)
				ayu = False
				ayu = True
				while ayu:
					try:
						cout = int(input('\033[94m[\033[93m!\033[94m] \033[93mCout : \033[0m'))
						if bool(cout)== False:
							print ("\033[94m[\033[93m!\033[94m] \033[93mIsi Dengan Benar :(")
							sleep(0.5)
						elif cout < 0:
							raise ValueError("Isi Dengan Benar :(")
						else:
							ayu = False
							Data = []
							Data.append(file())
							print ('\033[94m[\033[93m✓\033[94m] \033[93mTotal Karakter :',warna(),len(Data[-1]))
							print ('\033[94m[\033[93m!\033[94m] \033[91mLoading....')
							while cout != 0:
								cout -= 1
								print ("\033[94m[\033[93m!\033[94m] \033[92mEnskripsi Selesai Dalam :",warna(),cout,end='\r')
								if len(Data) == 1:
									Data.append(marshal(b85(b64(b32(b16(marshal(zlib(bz(lz(Hex(Data[-1])))))))))))
									
								else:
									a = []
									b = []
									for x in Data[-1]:
										a.append(ord(x))
									else:
										for x in a:
											b.append(string.replace("'","").replace('"','')*x)
										else:
											if len(Data[-1]) < 35000:
												enc = 'data={};exec("".join([chr(len(i)) for i in data]))'.format(b)
												Data.append(marshal(enc))
											else:
												Data.append(marshal(Data[-1]))
							else:
								print ("\n\033[94m[\033[93m✓\033[94m] \033[93mSelesai ^_^")
								with open(save,'w') as b:
									b.write(Data[-1])
									print (f"\033[92m[✓] Nama File : {basename(b.name)}\n[✓] Ukuran : {file_size(b.name)}\n[✓] File Tersimpan Di : {env['PWD']}/{b.name}")
								print ("\033[92m[✓] Total Karakter :",len(Data[-1]))
								Data.clear()
								nanya = input("\033[94m[\033[93m?\033[94m] \033[93mLihat Hasil Enskripsi \033[97m[\033[92mY\033[0m/\033[91mn\033[97m] \033[0m").lower()
								if nanya == 'y':
									show(save)
								else:
									exit()
					except PermissionError:
						print ("\033[94m[\033[93m!\033[94m] \033[91mGagal Mengakses Penyimpanan :(")
						exit()
					except ValueError as var:
						print (f"\033[94m[\033[93m!\033[94m] \033[91m{var}")
						sleep(0.5)
					
	except koneksi:
		print ("\033[94m[\033[93m!\033[94m] \033[93mTidak Ada Koneksi :(")
		sleep(0.2)
	except TimeoutError:
		print ("\033[94m[\033[93m!\033[94m] \033[93mKoneksi Lambat :(")
		sleep(0.2)
	except (KeyboardInterrupt , EOFError):
		exit('Keluar')
		

if __name__=="__main__":
	menu()