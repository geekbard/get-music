from os import system as cmd
try:
	from colorama import Fore as c
except:
	cmd("pip3 install colorama")
	from colorama import Fore as c
try:
	from requests import post , get
except:
	cmd("pip3 install requests")
	from requests import post , get

cmd("cls" or "clear")
print("-----=== [ Python Music Downloader By Meysam Gooya ] ===-----")
# Daryaft etela'at
name = input(c.WHITE + "[" + c.GREEN + "@" + c.WHITE + "]" + " Singer Name: " + c.RED)
sorted_name = name.replace(" " , "%20") + "%20"

m_name = input(c.WHITE + "[" + c.GREEN + "@" + c.WHITE + "]" + " Music Name: " + c.RED)
m_sorted = "%20" + m_name.replace(" " , "%20") + "%20"

try:
	quality = int(input(c.WHITE + "[" + c.GREEN + "@" + c.WHITE + "]" + " Quiality [ 320 - 128 ]: " + c.RED))
except:
	print(c.RED + "Lotfan faghat Adad vared konid.")
while True:
	if quality == 320 or quality == 128:
		break
	else:
		print(c.RED + "Invalid Quality")
		continue
q_sorted = "%28" + str(quality) + "%29"

# Sar ham kardan etela'at
music = sorted_name + '-' + m_sorted + q_sorted + '.mp3'

link = f'https://dls.music-fa.com/tagdl/downloads/{music}'

# Ahang mojoode?
if get(link).status_code == 404:
	print(c.RED + "Your music not found.")
else:
	print(c.WHITE + "[" + c.GREEN + "$" + c.WHITE + "]" + " Downloading... ", end="\r")
	with open(f'{name}-{m_name}.mp3' , 'wb') as myfile:
		myfile.write(get(link).content)
		print(c.WHITE + "[" + c.GREEN + "$" + c.WHITE + "]" + " Downloading... " + c.YELLOW+ "OK")
		print(c.GREEN + "[Done]: " + c.WHITE + "Your music downloaded.")
print(c.CYAN + "Python music downloader - 2022 [Meysam Gooya]" + c.RESET + "")

