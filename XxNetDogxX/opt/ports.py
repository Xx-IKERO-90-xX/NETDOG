import os
from xmlrpc.client import FastUnmarshaller

main = True
while main:
	os.system("clear")
	print("-----------------------------------------------------------------------------------------")
	print("""
		███    ██ ███████ ████████ ██████   ██████   ██████  
		████   ██ ██         ██    ██   ██ ██    ██ ██       
		██ ██  ██ █████      ██    ██   ██ ██    ██ ██   ███ 
		██  ██ ██ ██         ██    ██   ██ ██    ██ ██    ██ 
		██   ████ ███████    ██    ██████   ██████   ██████                                           
	""")
	print("-----------------------------------------------------------------------------------------")
	os.system("ip -c a")
	print("-----------------------------------------------------------------------------------------")
	com = input(" >>> ")
	if com == "help":
		os.system("cat help.txt")
		a = input(" Dale a intro para continuar >> ")
	
	elif com == "scanport_p_range":
		active1 = True
		while active1:
			def scanport_p_range():
				main = False
				ipv4 = input("Dirección IPV4 (0.0.0.0/8) >>> ")
				port = input("Rango de purtos (20-200) >>> ")
				os.system(f"sudo nmap -p {port} {ipv4}")
				g = input("Dale a intro para continuar >> ")
				sele1 = True
				while sele1:
					active1 = False
					print("""
					------------------------
					[x] Volver a ejecutar

					[y] Retroceder
					------------------------
					""")
					opt1 = input(" >>> ")
					if opt1 == "x":
						sele1 = False
						active1 = True

					elif opt1 == "y":
						sele1 = False
						os.system("python3 ports.py")
					
					else:
						os.system("clear")

			scanport_p_range()
			
	elif com == "scanport_ack":
		def scanport_ack():
			active2 = True
			while active2:
				main = False
				ipv4 = input(" [+] Dirección IPV4 >> ")
				os.system(f"sudo nmap -sA {ipv4}")
				os.system(f"sudo nmap -sM {ipv4}")
				c = input(" Dale a intro para continuar >> ")
				sele2 = True
				while sele2:
					active2 = False
					print("""
					-----------------------
					[x] Volver a ejecutar

					[y] Retroceder
					-----------------------
					""")
					opt2 = input(" >>> ")
					if opt2 == "x":
						sele2 = False
						active2 = True

					elif opt2 == "y":
						sele2 = False
						os.system("python3 ports.py")
					
					else:
						os.system("clear")

		scanport_ack()
	
	elif com == "scanport_tcp":
		def scanport_tcp():
			active3 = True
			while active3:
				main = False
				ipv4 = input(" [+] Dirección IPV4 >> ")
				os.system(f"sudo nmap -sN {ipv4}")
				os.system(f"sudo nmap -sF {ipv4}")
				os.system(f"sudo nmap -sX {ipv4}")
				j = input("Dale a intro para continuar >> ")
				sele3 = True
				while sele3:
					print("""
					---------------------------
					[x] Volver a ejecutar

					[y] Retroceder
					---------------------------
					""")
					opt3 = input(" >>> ")
					if opt3 == "x":
						sele3 = False
						active3 = True
					
					elif opt3 == "y":
						sele3 = False
						os.system("python3 ports.py")
					
					else:
						os.system("clear")

		scanport_tcp()

	elif com == "scanport_all":
		def scanport_all():
			active4 = True
			while active4:
				main = False
				ipv4 = input("Dirección IPV4 (0.0.0.0/8) >> ")
				os.system(f"sudo nmap --top-ports 25 {ipv4} | grep open")
				os.system(f"sudo nmap --top-ports 25 {ipv4} | grep filtered")
				os.system(f"sudo nmap --top-ports 25 {ipv4} | grep closed")
				n = input(" Dale a intro para continuar >> ")
				sele4 = True
				while sele4:
					print("""
					-----------------------
					[x] Volver a ejecutar

					[y] Retroceder
 					-----------------------
					""")
					opt4 = input(" >>> ")
					if opt4 == "x":
						sele4 = False
						active4 = True
					
					elif opt4 == "y":
						sele4 = False
						os.system("python3 ports.py")
					
					else:
						os.system("clear")
	
		scanport_all()	
	
	elif com == "scanflags":
		def scanflags():
			active5 = False
			while active5:
				main = False
				ipv4 = input(" Dirección IPV4 >> ")
				os.system(f"sudo nmap -scanflags {ipv4}")
				g = input(" Dale a intro para continuar >> ")
				sele5 = True
				while sele5:
					active5 = False
					print("""
					-------------------------
					[x] Volver a ejecutar

					[y] Retroceder
 					-------------------------
					""")
					opt5 = input(" >>> ")
					if opt5 == "x":
						sele5 = False
						active5 = True
					
					elif opt5 == "y":
						sele5 == False
						os.system("python3 ports.py")
					
					else:
						os.system("clear")
		scanflags()
		
	elif com == "return":
		main = False
		os.system("bash ../netdog.sh")

	elif com == "exit":
		main = False
	
	else:
		os.system("clear")
	