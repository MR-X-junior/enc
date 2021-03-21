#coding=utf-8
# Enskripsi For Python2

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
from binascii import hexlify as Hex
from socket import gethostname
from py_compile import compile as pyc
from os import system as sys , open as buka , O_CREAT , O_WRONLY , path , write , close , remove , environ
from bz2 import compress as bz2
from zlib import compress as zlib
from marshal import dumps
from base64 import *
from time import sleep
from sys import argv , platform , version , executable
from random import choice
from string import ascii_lowercase as low
from subprocess import call

acak = lambda : ''.join(choice(low) for x in range(3))

UPDATE = "18-03-2021 09:11"
logo = "\033[91m****     **** *******     **     **\n/**/**   **/**/**////**   //**   ** \n/**//** ** /**/**   /**    //** **  \n/** //***  /**/*******      //***   \n/**  //*   /**/**///**       **/**  \n/**   /    /**/**  //**     ** //** \n/**        /**/**   //**   **   //**\n//         // //     //   //     //\n\033[94m╔═════════════════════════════════════╗\n║\033[94m[\033[93m•\033[94m] \033[96mAuthor : \033[92m\033[4mMR-X JUNIOR\033[0m             \033[94m║\n║\033[94m[\033[93m•\033[94m] \033[96mGitHub : \033[97mgithub.com/MR-X-Junior  \033[94m║\n║\033[94m[\033[93m•\033[94m] \033[96mWA.    : \033[93m+62 85754629509        \033[94m ║\n║\033[94m[\033[93m•\033[94m] \033[96mUPDATE : %s      \033[94m  ║\n║\033[94m[\033[93m•\033[94m] \033[96mPython : %s                \033[94m  ║\n║\033[94m[\033[93m•\033[94m] \033[96mOS     : %s                \033[94m  ║\n║\033[94m[\033[93m•\033[94m] \033[96mHost   : %s             \033[94m  ║\n║\033[94m[\033[93m•\033[94m] \033[96mTeam.  : TNT ANONYMOUS \033[91mINDO\033[97mNESIA\033[94m ║\n\033[94m╚═════════════════════════════════════╝" % (UPDATE , version[0:6] , platform , gethostname())

def install(package):
	print "Mengistall",package
	get = call([executable, "-m","pip","--disable-pip-version-chec","-q", "install", package])
	if get != 0:
		exit('Gagal Mengistall',package)
	else:
		print "Berhasil Mengistall %s ^_^" % (package)
		
try:
	from tqdm import tqdm
except:
	install("tqdm")
	from tqdm import tqdm

def file():
	while True:
		try:
			a = raw_input('\033[94m[\033[93m?\033[94m] \033[92mFile : \033[93m')
			b = path.isdir(a)
			if b:
				print "\033[94m[\033[93m!\033[94m] \033[93mFile Bank Bukan Folder :("
				sleep(0.5)
			else:
				c = open(a).read()
				if len(c) == 0:
					print "\033[94m[\033[93m!\033[94m] \033[93mEnskripsi Gagal :("
					exit()
				else:
					return c
		except IOError:
			print "\033[94m[\033[93m!\033[94m] \033[93mFile \033[91m%s \033[93mTidak Di Temukan" % (a)
			sleep(0.5)
			
def shal(code):
	a = compile(code,'<Ayu Putri>','exec')
	b = dumps(a)
	c = repr(b)
	d = "#coding=utf-8\n#Enskripsi By Rahmat\nimport marshal\nexec(marshal.loads({}))".format(c)
	return d
			
def main(code , cout):
	save = acak() + '.py'
	huruf = lambda : choice(['0','1'])
	aa = []
	ab= []
	ac = []
	try:
		print "\033[94m[\033[93m!\033[94m] \033[93mLoading"
		kay = "#coding=utf-8\n#Enskripsi By Rahmat ^_^\n#Python Version : {}\nimport binascii\nexec(binascii.unhexlify('{}'))".format(version[0:6] , Hex(code))
		a = "#coding=utf-8\n#Enskripsi By Rahmat ^_^\n#Python Version : {}\nimport base64\nexec(base64.b64decode('{}'))".format(version[0:6] , b64encode(kay))
		b = "#coding=utf-8\n#Enskripsi By Rahmat ^_^\n#Python Version : {}\nimport base64\nexec(base64.b32decode('{}'))".format(version[0:6] , b32encode(a))
		c = "#coding=utf-8\n#Enskripsi By Rahmat ^_^\n#Python Version : {}\nimport base64\nexec(base64.b16decode('{}'))".format(version[0:6] , b16encode(b))
		d = "#coding=utf-8\n#Enskripsi By Rahmat ^_^\n#Python Version : {}\nimport bz2\nexec(bz2.decompress({}))".format(version[0:6] , repr(bz2(c)))
		e = "#coding=utf-8\n#Enskripsi By Rahmat ^_^\n#Python Version : {}\nimport zlib\nexec(zlib.decompress({}))".format(version[0:6] , repr(zlib(d)))
		for x in e:
			aa.append(ord(x))
		for x in aa:
			ab.append(huruf().replace("'","").replace('"','')*x)
		f = "#coding=utf-8\ndata = {};exec ''.join(chr(len(i)) for i in data)".format(ab)
		bar = tqdm(total=cout)
		while cout != 0:
			if len(ac) == 0:
				ac.append(shal(f))
				cout -= 1
				bar.update(1)
			else:
				shal(ac[-1])
				cout -= 1
				bar.update(1)
		else:
			open('a.py','w').write(ac[-1])
			pyc('a.py','a.pyc')
			a = open('a.pyc').read()
			b = buka(save,O_CREAT | O_WRONLY)
			write(b,a)
			write(b,'\n\nCATATAN : SCRIPT INI HANYA BISA DI RUN MENGGUNAKAN PYTHON VERSI : {}'.format(version[0:6]))
			write(b,'\n# Script Di Enskripsi Menggunakan : https://github.com/MR-X-Junior/enc\n\nContact Me ^_^\n=====================\nAuthor : Rahmat adha\nWhatsApp : +62 85754629509\nFacebook : https://www.facebook.com/Anjay.pro098\nEmail : termux.indonesia01@gmail.com\nGithub : https://github.com/MR-X-Junior/\n\nINFO SYSTEM\n====================\n')
			for x in environ:
				write(b,'%s : %s\n' % (x , environ[x]))
			close(b)
			for x in ['a.py','a.pyc']:
				try:
					remove(x)
				except:
					pass 
			bar.close()
			print "\033[92m[✓] SUKSES :",path.realpath(save)
	except (KeyboardInterrupt , EOFError):
		exit('exit')

if __name__=="__main__":
	sys('clear')
	print logo
	a = file()
	while True:
		try:
			b = int(raw_input('\033[94m[\033[93m?\033[94m] \033[93mcout : \033[97m'))
			if b <= 0:
				raise ValueError()
			else:
				main(a,b)
				break
		except ValueError:
			print "\033[94m[\033[93m!\033[94m] \033[93mIsi Dengah Benar"
			sleep(0.5)