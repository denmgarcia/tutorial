import argparse

def convert_F(c):
	convert = (9.0/5.0)*c+32
	return convert

def convert_C(f):
	convert = (f -32)*(5.0/9.0)
	return convert

if __name__ == '__main__':
	x = eval(input("Enter the number to convert: " ))

	c_to_f = convert_C(x)
	f_to_c = convert_F(x)

	print("Farenheit to Celsius: ", c_to_f) # 32F to 0C
	print("Celsius to Farenheit: ", f_to_c) # 0C ro 32