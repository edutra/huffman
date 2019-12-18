import sys


def compress(file_name):
	print("c")
	return 1
def decompress(compressed_file_name, binaries):
	print("d")
	return 1

def main():

	

	argument_quantity = len(sys.argv)

	arg_number = 1

	while( arg_number < argument_quantity ):
		
		option = sys.argv[arg_number]
		arg_number = arg_number + 1
		print(option)
		
		if option == "-c":
			arg_number = arg_number + 1
			file = sys.argv[arg_number]
			compressed_file = compress(file)

		elif option == "-d":    
			arg_number = arg_number + 1
			file = sys.argv[arg_number]
			arg_number = arg_number + 1
			binaries = sys.argv[arg_number]
			uncompressed_file = decompress(file, binaries)







main()
