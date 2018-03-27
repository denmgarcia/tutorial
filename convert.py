from func import convert_C, convert_F
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('--celsius', help="convert farenheit to celsius")
parser.add_argument('--farenheit', help="convert celsius to farenheit")

args = parser.parse_args()

x = float(args.farenheit)

if args.celsius:
	cel = convert_F(float(args.celsius))
	print(cel, 'F')
elif args.farenheit:
	far = convert_C(x)
	print(far,'C')
