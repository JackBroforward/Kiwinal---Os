import os
import time

with open('Res/info.data', 'w') as f:
	f.writelines("1")

print("""

███████████████████████████████████████████████████████████████████
█▄─█─▄█▄─▄█▄─█▀▀▀█─▄█▄─▄█▄─▀█▄─▄██▀▄─██▄─▄█████▀▀▀▀▀████─▄▄─█─▄▄▄▄█
██─▄▀███─███─█─█─█─███─███─█▄▀─███─▀─███─██▀████████████─██─█▄▄▄▄─█
▀▄▄▀▄▄▀▄▄▄▀▀▄▄▄▀▄▄▄▀▀▄▄▄▀▄▄▄▀▀▄▄▀▄▄▀▄▄▀▄▄▄▄▄▀▀▀▀▀▀▀▀▀▀▀▀▄▄▄▄▀▄▄▄▄▄▀

████████████████████████████████
█─▄▄▄▄█▄─▄▄─█─▄─▄─█▄─██─▄█▄─▄▄─█
█▄▄▄▄─██─▄█▀███─████─██─███─▄▄▄█
▀▄▄▄▄▄▀▄▄▄▄▄▀▀▄▄▄▀▀▀▄▄▄▄▀▀▄▄▄▀▀▀
""")

name = input("Please Enter Your Username To Be Displayed: ")
pas = input("Please Enter Your Password To Login: ")

with open('Res/dataname.pass', 'w') as f:
	f.writelines(name)

with open('Res/password.pass', 'w') as f:
	f.writelines(pas)

print("Setup Complete!!!")
print("Opening Login Page...")
time.sleep(0.5)
os.startfile('login.py')
