import sys, os

def help():
	return ('''
Usage: python argv.py [--username], [--password], [--help]

--help, -h				show list of help
--username				username
--password				password
--create, -c 			create a folder

	''')


def create(folder):
	name = os.mkdir('/home/denmark/Desktop/pythontutorial/%s' %(folder))




if __name__ == '__main__':
	if(sys.argv[1] == '--help' or sys.argv[1] == '-h'):
			print(help())
	elif(sys.argv[1] == '--create' or sys.argv[1] == '-c'):
		if(os.path.exists(sys.argv[2])):
			print("This folder is already exist!")
		else:
			create(sys.argv[2])
	else:
		print('Flag is not recognized, Kindly type --help for available options')