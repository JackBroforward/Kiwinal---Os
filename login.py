import os
import time

print("""

███████████████████████████████████████████████████████████████████
█▄─█─▄█▄─▄█▄─█▀▀▀█─▄█▄─▄█▄─▀█▄─▄██▀▄─██▄─▄█████▀▀▀▀▀████─▄▄─█─▄▄▄▄█
██─▄▀███─███─█─█─█─███─███─█▄▀─███─▀─███─██▀████████████─██─█▄▄▄▄─█
▀▄▄▀▄▄▀▄▄▄▀▀▄▄▄▀▄▄▄▀▀▄▄▄▀▄▄▄▀▀▄▄▀▄▄▀▄▄▀▄▄▄▄▄▀▀▀▀▀▀▀▀▀▀▀▀▄▄▄▄▀▄▄▄▄▄▀
""")

print("Kiwinal Os is Booting")
time.sleep(3)

print("Checking Res")
time.sleep(5)

print("[OK] Res")
time.sleep(0.5)

print("Checking Boot")
time.sleep(13)

print("[OK] Boot")
time.sleep(1)

print("Starting Kiwinal-os")
time.sleep(8)

login_pass = open('Res/password.pass')
login_name = open('Res/dataname.pass')
l_p = login_pass.read()
l_n = login_name.read()
print("""

███████████████████████████████████████████████████████████████████
█▄─█─▄█▄─▄█▄─█▀▀▀█─▄█▄─▄█▄─▀█▄─▄██▀▄─██▄─▄█████▀▀▀▀▀████─▄▄─█─▄▄▄▄█
██─▄▀███─███─█─█─█─███─███─█▄▀─███─▀─███─██▀████████████─██─█▄▄▄▄─█
▀▄▄▀▄▄▀▄▄▄▀▀▄▄▄▀▄▄▄▀▀▄▄▄▀▄▄▄▀▀▄▄▀▄▄▀▄▄▀▄▄▄▄▄▀▀▀▀▀▀▀▀▀▀▀▀▄▄▄▄▀▄▄▄▄▄▀

████████████████▀█████████████
█▄─▄███─▄▄─█─▄▄▄▄█▄─▄█▄─▀█▄─▄█
██─██▀█─██─█─██▄─██─███─█▄▀─██
▀▄▄▄▄▄▀▄▄▄▄▀▄▄▄▄▄▀▄▄▄▀▄▄▄▀▀▄▄▀
""")

while True:
	log = input("Enter Password To " + l_n + " To Login: ")

	if log == l_p:
		print("Opening Home Page...")
		time.sleep(0.5)
		os.startfile("home.py")
		break

	else:
		print("Wrong Passowrd To " + l_n)
