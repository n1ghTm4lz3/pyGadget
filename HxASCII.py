"""
Title: HxASCII
Author: n1ghTm4lz3
Description:
	Transform hexadecimal to ASCII or ASCII to hexadecimal
"""

def main():
	while True:
		cipher = input("String: ")

		if cipher == "":
			exit()
		else:
			transform(cipher)

def message():
	print("+===============================================+")
	print("|        Hexadecimal & ASCII Transformer        |")
	print("|                                               |")
	print("| Input Sample: 0x3456 / 0aAbdc / 0d080125      |")
	print("| Syntax:                                       |")
	print("|   0x => Hex to ASCII                          |")
	print("|   0a => ASCII to Hex                          |")
	print("|   0d => Decimal to ASCII and Hex              |")
	print("|   ?  => Help Message                          |")
	print("+===============================================+")


def transform(cipher):
	ascii_plaintext = ""
	hex_plaintext = ""
	hxtemp = 0
	dctemp = 0

	if cipher[0] == "?":
		message()
		return
	elif cipher[0:2] == "0x":
		for i in range(2, len(cipher), 2):
			hxtemp = int(cipher[i:i+2], 16)
			if hxtemp > 31 and hxtemp < 127:
				ascii_plaintext += chr(hxtemp)
			else:
				ascii_plaintext += ' '
			hex_plaintext += hex(hxtemp)[2:] + " "
	elif cipher[0:2] == "0a":
		ascii_plaintext = cipher[2:]
		for i in range(2, len(cipher)):
			hxtemp = ord(cipher[i])
			hex_plaintext += hex(hxtemp)[2:] + " "
	elif cipher[0:2] == "0d":
		for i in range(2, len(cipher), 3):
			dctemp = int(cipher[i:i+3])
			hxtemp = int(hex(dctemp), 16)
			if hxtemp > 31 and hxtemp < 127:
				ascii_plaintext += chr(hxtemp)
			else:
				ascii_plaintext += ' '
			hex_plaintext += hex(hxtemp)[2:] + " "

	print("HEX: " + hex_plaintext)
	print("ASCII: \"" + ascii_plaintext + "\"")
	print()


if __name__ == '__main__':
	message()
	main()
