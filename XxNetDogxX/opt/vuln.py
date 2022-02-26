
import os 

active = True
while active:
    os.system("clear")
    print("-----------------------------------------------------------------------")
    print("""
        ███    ██ ███████ ████████ ██████   ██████   ██████  
        ████   ██ ██         ██    ██   ██ ██    ██ ██       
        ██ ██  ██ █████      ██    ██   ██ ██    ██ ██   ███ 
        ██  ██ ██ ██         ██    ██   ██ ██    ██ ██    ██ 
        ██   ████ ███████    ██    ██████   ██████   ██████                                                 
    """)
    print("-----------------------------------------------------------------------")
    print("-----------------------------------------------------------------------")
    os.system("ip -c a")
    print("-----------------------------------------------------------------------")
    com = input(" >>> ")
    if com == "scanvuln_auth":
        def scanvuln_auth():
            active1 = True
            while active1:
                ipv4 = input("Dirección IPV4 >> ")
                os.system(f"sudo nmap -f -sS -sV auth {ipv4} | grep open")
                os.system(f"sudo nmap -f -sS -sV auth {ipv4} | grep Service Info")
                a = input(" Presione intro apra continuar >> ")
                sele1 = True
                while sele1:
                    print ("""
                        --------------------------
                        | [x] Volver a ejecutar  |
                        |                        |
                        | [y] Retroceder         |
                        --------------------------
                        """)
                    opt1 = input(" >>> ")
                    if opt1 == "x":
                        sele1 = False

                    elif opt1 == "y":
                        sele1 = False
                        active1 = False

                    else:
                        print("Error, opción no permitida!!!!")
                        os.system("clear")

        scanvuln_auth()
    
    elif com == "scanvuln_default":
        def scanvuln_default():
            active2 = True
            while active2:
                ipv4 = input("Dirección IPV4 >> ")
                os.system(f"sudo nmap -f -sS -sV --script default {ipv4} | grep version")
                os.system(f"sudo nmap -f -sS -sV --script default {ipv4} | grep open")
                os.system(f"sudo nmap -f -sS -sC --script default {ipv4} | grep 'Service Info'")
                b = input(" Presione intro para continuar >>>  ")
                sele2 = True
                while sele2:
                    print("""
                        -------------------------
                        | [x] Volver a ejecutar |
                        |                       |
                        | [y] Retroceder        |
                        -------------------------
                        """)
                    opt2 = input(" >>> ")
                    if opt2 == "x":
                        sele2 = False

                    elif opt2 = "y":
                        sele2 = False
                        active2 = False

                    else:
                        print("Error, Opción no permitida!!!!")
                        os.system("clear")
        scanvuln_default()
    
    elif com == "scanvuln_safe":
        def scanvuln_safe():
            active3 = True
            while active3:
                ipv4 = input("Dirección IPV4 >> ")
                os.system(f"sudo nmap -f --script safe {ipv4}")
                c = input(" Presione intro para continuar >> ")
                sele3 = True
                while sele3:
                    print("""
                        -----------------------------
                        | [x] Volver a ejecuta      |
                        |                           |
                        | [y] Retroceder            |
                        -----------------------------
                        """)
                    opt3 = input(" >>> ")
                    if opt3 == "x":
                        sele3 = False

                    elif opt3 == "y":
                        sele3 = False
                        active3 = False

                    else:
                        print("Error, Opción no permitida!!!!")
        scanvuln_safe()
    
    elif com == "scanvuln_all":
        def scanvuln_all():
            active4 = True
            while active4:
                ipv4 = input("Dirección IPV4 objetiva >> ")
                os.system(f"sudo nmap -f --script all {ipv4}")
                d = input(" Presione intro para continuar >> ")
                sele4 = True
                while sele4:
                    print("""
                        -------------------------
                        | [x] Volver a ejecutar |
                        |                       |
                        | [y] Retroceder        |
                        -------------------------
                        """)
                    opt4 = input(" >>> ")
                    if opt4 == "x":
                        sele4 = False

                    elif opt4 == "y":
                        sele4 = False
                        active4 = False

                    else:
                        print("Error, Opción no permitida!!!!!")
                        os.system("clear")
        scanvuln_all()
    
    elif com == "scanvuln_pn":
        def scanvuln_pn():
            active5 = True
            while active5:
                ipv4 = input("Dirección IPV4 >> ")
                os.system(f"nmap --script vuln {ipv4}")
                e = input(" Presione intro para continuar >> ")
                sele5 = True
                while sele5:
                    print("""
                        ------------------------
                        |[x] Volver a ejecutar |
                        |                      |
                        |[y] Retroceder        |
                        ------------------------
                        """)
                    opt5 = input(" >>> ")
                    if opt5 == "x":
                        sele5 = False

                    elif opt5 == "y":
                        sele5 = False
                        active5 = False

                    else:
                        print("Error, Opción no permitida!!!!")
                        os.system("clear")
        scanvuln_pn()

    elif com == "scanvuln_massive":
        def scanvuln_massive():
            active6 = True
            while active6:
                ipv4 = input("Dirección IPV4 >> ")
                os.system(f"sudo nmap -f -sS -sV auth {ipv4} | grep open")
                os.system(f"sudo nmap -f -sS -sV auth {ipv4} | grep 'Service Info'")
                os.system(f"sudo nmap -f -sS -sV auth {ipv4} | grep version")
                os.system(f"sudo nmap --script vuln {ipv4}")
                g = input(" Dale intro para continuar >> ")
                sele6 = True
                while sele6:
                    print("""
                        ------------------------------
                        | [x] Volver a ejecutar      |
                        |                            |
                        | [y] Retroceder             |
                        ------------------------------
                        """)
                    opt5 = input(" >>> ")
                    if opt5 == "x":
                        sele6 = False

                    elif opt5 == "y":
                        sele6 = False
                        active6 = False

                    else:
                        print("Error, Opción no permitida!!!!")
                        os.system("clear")
        scanvuln_massive()

    elif com == "help":
        os.system("cat help.txt")
        c = input(" Presione intro para continuar >> ")

    elif com == "return":
        os.system("netdog.sh")
        active = False
    
    elif com == "exit":
        active = False
    
    else:
        print("Comando no permitido!!!")
