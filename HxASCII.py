"""
Title: HxASCII
Author: n1ghTm4lz3
Description:
	Transform hexadecimal to ASCII
"""

def main():
	while True:
		cipher = input("Hex: ")

		if cipher == "":
			exit()
		else:
			transform(cipher)

def transform(cipher):
	plaintext = ""
	hxtemp = 0

	for i in range(0, len(cipher), 2):
		hxtemp = int(cipher[i:i+2], 16)
		if hxtemp > 31 and hxtemp < 127:
			plaintext += chr(hxtemp)
		else:
			plaintext += ' '

	print("ASCII: \"" + plaintext + "\"")
	print()


if __name__ == '__main__':
	main()
