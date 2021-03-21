#coding=utf-8
import os,sys,time,random,datetime,calendar

acak = lambda :random.choice(["\033[91m","\033[92m","\033[93m","\033[94m","\033[95m","\033[96m","\033[97m"])
os.system('clear')
teks = "Hallo Nama Saya %s\nSekarang Saya Sedang Berada Di %s\nAtau Sedang Berada Di Folder %s\n\nINFO TENTANG KAMU" % (os.path.basename(sys.argv[0]) , os.path.realpath(os.getcwd()) , os.path.basename(os.getcwd()))

for x in teks + '\n':
   sys.stdout.write(acak() + x)
   sys.stdout.flush()
   time.sleep(0.04)
   
print ("="*20)
for x in os.environ:
	print ("%s : %s" % (x,acak() + os.environ[x]))
	
print ("\nCALENDAR")
print ("="*20)
for x in range(1,13):
	print (acak() + calendar.month(datetime.datetime.now().year,x))
