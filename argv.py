import sys, os

def help():
	return ('''
Usage: python argv.py [--username], [--password], [--help]

--help, -h				show list of help
--username				username
--password				password
--create, -c 			create a folder
--delete, -d 			delete a foler

	''')


def create(folder):
	name = os.mkdir('/home/denmark/Desktop/pythontutorial/%s' %(folder), mode = 0o000)




if __name__ == '__main__':
	if(sys.argv[1] == '--help' or sys.argv[1] == '-h'):
			print(help())
	elif(sys.argv[1] == '--create' or sys.argv[1] == '-c'):
		if(os.path.exists(sys.argv[2])):
			print("This folder is already exist!")
		else:
			create(sys.argv[2])
	elif(sys.argv[1] == '--delete' or sys.argv[1] == '-d'):
		try:
			if(os.rmdir(sys.argv[2])):
				print("Deleted directory %s" % sys.argv[2])
		except FileNotFoundError:
			print("File was not found or have been already deleted!")
	else:
		print('Flag is not recognized, Kindly type --help for available options')