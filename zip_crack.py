import zipfile

def zCRACKER(z_FILE, Password):
	try:
		with zipfile.ZipFile(z_FILE, 'r') as ZFILES:
			zCRACK = ZFILES.extractall(pwd=Password)
		
		print '[+] Password Found: ' + '\'' + Password + '\''
	except RuntimeError:
		pass 

def main():
	zFILE = 'evil.zip'
	zPASS = open('dictionary.txt')
	for password in zPASS.readlines():
		zCRACKER(zFILE, password.strip('\n'))

if __name__ == '__main__':
	main()