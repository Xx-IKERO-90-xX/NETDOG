import os

main = True
while main:
    os.system("clear")
    print("-------------------------------------------------------------------------------------------")
    print("""
            ███    ██ ███████ ████████ ██████   ██████   ██████  
            ████   ██ ██         ██    ██   ██ ██    ██ ██       
            ██ ██  ██ █████      ██    ██   ██ ██    ██ ██   ███ 
            ██  ██ ██ ██         ██    ██   ██ ██    ██ ██    ██ 
            ██   ████ ███████    ██    ██████   ██████   ██████  
                                                     
        """)
    print("--------------------------------------------------------------------------------------------")
    os.system("ip -c a")
    print("--------------------------------------------------------------------------------------------")
    com = input(" >>> ")

    if com == "scanhost_sn":
        def scanhost_sn():
            active1 = True
            while active1:
                ipv4 = input("Dirección IPV4 >>> ")
                os.system(f"sudo nmap -sn {ipv4}")
                a = input(" Presione intro para continuar >>> ")
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
                        os.system("python3 hosts.py")
                    
                    else:
                        os.system("clear")

        scanhost_sn()

    elif com == "scanhost_l":
        def scanhost_l():
            active2 = True
            while active2:
                ipv4 = input(" Dirección IPV4 >>> ")
                os.system(f"sudo nmap -sL {ipv4}")
                b = input(" Presione intro para continuar >> ")
                sele2 = True
                while sele2:
                    active2 = False
                    print("""
                    ------------------------
                    [x] Volver a ejecutar
                    
                    [y] Retroceder
                    ------------------------
                     """)
                    opt2 = input(" >>> ")
                    if opt2 == "x":
                        sele2 = False
                        active2 = True
                    
                    elif opt2 == "y":
                        sele2 = False
                        os.system("python3 hosts.py")
                    
                    else:
                        os.system("clear")

        scanhost_l()

    elif com == "scanhost":
        def scanhost():
            active3 = True
            while active3:
                ipv4 = input("Dirección IPV4 (0.0.0.0/8) >> ")
                os.system(f"sudo nmap {ipv4}")
                c = input("Dale a intro para continuar >> ")
                sele3 = True
                while sele3:
                    active3 = False
                    print("""
                    -----------------------
                    [x] Volver a ejecutar

                    [y] Retroceder
                    ----------------------- 
                    """)
                    opt3 = input(" >>> ")
                    if opt3 == "x":
                        sele3 = False
                        active3 = True

                    elif opt3 == "y":
                        sele3 = False
                        os.system("python3 hosts.py")
                    
                    else:
                        os.system("clear")

        scanhost()
    
    elif com == "scanhost_ph":
        def scanhost_ph():
            active4 = True
            while active4:
                ipv4 = input("Dirección IPV4 >> ")
                os.system(f"sudo nmap -sS -p 80,443 {ipv4}")
                g = input(" Presiona intro para continuar >> ")
                sele4 = True
                while sele4:
                    active4 = False
                    print("""
                    ------------------------
                    [x] Volver a ejecutar
                    
                    [y] Retroceder
                    ------------------------
                    """)
                    opt4 = input(" >>> ")
                    if opt4 == "x":
                        sele4 = False
                        active4 = True
                
                    elif opt4 == "y":
                        sele4 = False
                        os.system("python3 hosts.py")
                
                    else:
                        os.system("clear")

        scanhost_ph()
    
    elif com == "scanhost_route":
        def scanhost_route():
            active5 = True
            while active5:
                ipv4 = input(" Dirección IPV4 >> ")
                os.system(f"sudo nmap {ipv4} --iflist")
                h = input(" Presione intro para continuar")
                sele5 = True
                while sele5:
                    active5 = False
                    print("""
                    -----------------------
                    [x] Volver a ejecutar

                    [y] Retroceder
                    -----------------------
                    """)
                    opt5 = input(" >>> ")
                    if opt5 == "x":
                        sele5 = False
                        active5 = True
                    
                    elif opt5 == "y":
                        sele5 = False
                        os.system("python3 hosts.py")
                    
                    else:
                        os.system("clear")

        scanhost_route()
    
    elif com == "scanhost_sys":
        def scanhost_sys():
            active6 = True
            while active6:
                ipv4 = input(" Dirección IPV4 >> ")
                os.system(f"sudo nmap -O {ipv4}")
                h = input(" Presione intro para continuar >> ")
                sele6 = True
                while sele6:
                    active6 = False
                    print("""
                    ----------------------
                    [x] Volver a ejecutar

                    [y] Retroceder
                    ----------------------  
                    """)
                    opt6 = input(" >>> ")
                    if opt6 == "x":
                        sele6 = False
                        active6 = True
                    
                    elif opt6 == "y":
                        sele6 = False
                        os.system("python3 hosts.py")

                    else:
                        os.system("clear")

        scanhost_sys()
    
    elif com == "scanhost_agresive":
        def scanhost_agresive():
            active7 = True
            while active7:
                ipv4 = input(" Dirección IPV4 >> ")
                os.system(f"sudo nmap -A {ipv4}")
                f = input(" Presione intro para continuar >> ")
                sele7 = True
                while sele7:
                    active7 = False
                    print("""
                    -----------------------
                    [x] Volver a ejecutar

                    [y] Retroceder
                    -----------------------
                    """)
                    opt7 = input(" >>> ")
                    if opt7 == "x":
                        sele7 = False
                        active7 = True
                    
                    elif opt7 == "y":
                        sele7 = False
                        os.system("python3 hosts.py")
                    
                    else:
                        os.system("clear")

        scanhost_agresive()

    elif com == "help":
        os.system("cat help.txt")
        d = input(" Presione Intro para continuar >> ")
        
    elif com == "return":
        main = False
        os.system("bash ../netdog.sh")

    elif com == "exit":
        main = False
    
    else:
        os.system("clear")