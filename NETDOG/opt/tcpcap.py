import os

main = True
while main:
	os.system("clear")

	print("---------------------------------------------------------------------------")
	print("""
			███    ██ ███████ ████████ ██████   ██████   ██████  
			████   ██ ██         ██    ██   ██ ██    ██ ██       
			██ ██  ██ █████      ██    ██   ██ ██    ██ ██   ███ 
			██  ██ ██ ██         ██    ██   ██ ██    ██ ██    ██ 
			██   ████ ███████    ██    ██████   ██████   ██████                                                 
		""")
	print("---------------------------------------------------------------------------")
	os.system("ip -c a")
	print("---------------------------------------------------------------------------")

	com = input(" >>> ")
	if com == "help":
		os.system("cat help.txt")
		a = input(" [*] Presione intro para continuar >>> ")

	elif com == "captcp":
		def captcp():
			active1 = True
			while active1:
				main = False
				eth = input("[+] Interfaz de red >> ")
				os.system(f"sudo tcpdump -c50 -i {eth}")
				a = input(" [*] Seleccione intro para continuar >>> ")
				sele1 = True
				while sele1:
					active1 = False
					print("""
						-----------------------
						 [x] Volver a ejecutar

						 [y] Retroceder
						-----------------------
						""")
					opt1 = input(" >>> ")
					if opt1 == "x":
						sele1 = False
						os.system("clear")
						active1 = True

					elif opt1 == "y":
						sele1 = False
						os.system("python3 tcpcap.py")

					else:
						os.system("clear")

		captcp()

	elif com == "captcp_h":
		def captcp_h():
			active2 = True
			while active2:
				main = False
				host = input("[+] Dirección ip del Host >> ")
				os.system(f"sudo tcpdump host {host}")
				a = input(" [*] Presione intro para continuar >> ")
				sele2 = True
				while sele2:
					active2 = False
					print("""
						----------------------------
						[x] Volver a ejecutar

						[y] Retroceder
						----------------------------
					""")
					opt2 = input(" >>> ")
					if opt2 == "x":
						sele2 = False
						os.system("clear")
						active2 = True

					elif opt2 == "y":
						sele2 = False
						os.system("bash tcpcap.py")

					else:
						os.system("clear")
		captcp_h()

	elif com == "captcp_c":
		def captcp_c():
			active3 = True
			while active3:
				print("""
				-----------------------
				[h] Host

				[i] Interface
				-----------------------
				""")
				sel = input(" >>> ")
				if sel == "h":
					h = input("[+] Dirección ip del host >> ")
					n = input("[+] Tamaño de la captura >> ")
					os.system(f"sudo tcpdump -c{n} host {h}")

				elif sel == "i":
					i = input("[+] Interfaz de red >> ")
					n = input("[+] Tamaño de la captura de paquetes >> ")
					os.system(f"sudo tcpdump -c{n} -i {i}")

				else:
					os.system("clear")

				a = input("Presione intro para continuar >>> ")
				sele3 = True
				while sele3:
					active3 = False
					print("""
					--------------------------
					[x] Volver a ejecutar

					[y] Retroceder
					--------------------------
					""")
					opt3 = input(" >> ")
					if opt3 == "x":
						sele3 = False
						os.system("clear")
						active3 = True

					elif opt3 == "y":
						sele3 = False
						os.system("python3 tcpcap.py")

					else:
						os.system("clear")
		captcp_c()

	elif com == "return":
		main = False
		os.system("bash ../netdog.sh")

	elif com == "exit":
		main = False

	else:
		os.system("clear")
