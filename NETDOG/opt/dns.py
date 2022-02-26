import os

main = True
while main:
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
    os.system("ip -c a")
    print("-----------------------------------------------------------------------")
    com = input(" >>> ")
    if com == "getnsinfo":
        def getnsinfo():
            active1 = True
            while active1:
                main = False
                ns = input(" DNS objetiva >> ")
                os.system(f"nslookup {ns}")
                a = input("Presione intro para continuar >> ")
                sele1 = True
                while sele1:
                    active1 = False
                    print("""
                    ---------------------------
                    | [x] Volver a ejecutar   |
                    |                         |
                    | [y] Retroceder          |
                    ---------------------------
                    """)
                    opt = input(" >>> ")
                    if opt == "x":
                        sele1 = False
                        active1 = True
                        os.system("clear")

                    elif opt == "y":
                        sele1 = False
                        active1 = False
                        os.system("python3 dns.py")

                    else:
                        print("Error, opción no permitida!!!")
                        os.system("clear")

        getnsinfo()
    

    elif com == "getnsinfo_ns":
        def getnsinfo_ns():
            active2 = True
            while active2:
                main = False
                os.system("clear")
                ns = input("DNS objetiva >> ")
                os.system(f"nslookup -type=NS {ns}")
                b = input("Presione intro para continuar >> ")
                sele2 = True
                while sele2:
                    active2 = False
                    print("""
                    -------------------------
                    | [x] Volver a ejecutar |
                    |                       |
                    | [y] Retroceder        |
                    -------------------------
                    """)
                    opt2 = input(" >>> ")
                    if opt2 == "x":
                        os.system("clear")
                        sele2 = False
                        active2 = True

                    elif opt2 == "y":
                        sele2 = False
                        active2 = False
                        os.system("python3 dns.py")

                    else:
                        print("Error, Opción no permitida!!!!!")
                        os.system("clear")

        getnsinfo_ns()
    
    elif com == "getnsinfo_ip":
        def getnsinfo_ip():
            active3 = True
            while active3:
                main = False
                os.system("clear")
                ns = input("DNS objetiva >> ")
                os.system(f"nslookup {ns} -trace | grep A")
                c = input("Presione intro para continuar >> ")
                sele3 = True
                while sele3:
                    print("""
                        ------------------------
                        |[x] Volver a ejecutar |
                        |                      |
                        |[y] Retroceder        |
                        ------------------------
                        """)
                    opt3 = input(" >>> ")
                    if opt3 == "x":
                        sele3 = False
                        active3 = True
                        os.system("clear")

                    elif opt3 == "y":
                        sele3 = False
                        active3 = False
                        os.system("python3 dns.py")

                    else:
                        print("Error, Opción no permitida!!!")
                        os.system("clear")

        getnsinfo_ip()

    elif com == "getnsinfo_local_A":
        def getnsinfo_local_A():
            active4 = True
            while active4:
                main = False
                os.system("clear")
                dns = input("Escriba el DNS local a consultar >> ")
                host = input("Escriba el nombre del host a consultar >> ")
                os.system(f"nslookup {host}.{dns}")
                a = input(" Presione intro para continuar >> ")
                sele4 = True
                while sele4:
                    active4 = False
                    print("""
                    -------------------------- 
                    | [x] Volver a ejecutar  |
                    |                        | 
                    | [y] Retroceder         |
                    --------------------------
                    """)
                    opt4 = input(" >> ")
                    if opt4 == "x":
                        sele4 = False
                        active4 = True
                        os.system("clear")

                    elif opt4 == "y":
                        sele4 = False
                        active4 = False
                        os.system("python3 dns.py")

                    else:
                        print("Error: Opción no permitida!!")
                        os.system("clear")

        getnsinfo_local_A()

    elif com == "getnsinfo_local_cname":
        def getnsinfo_local_cname():
            active5 = True
            while active5:
                main = False
                os.system("clear")
                dns = input("Escriba el DNS local a consultar >> ")
                cname = input("Escriba el nombre del registro CNAME a consultar (www,ftp,etc.) >> ")
                os.system(f"nslookup {cname}.{dns}")
                a = input(" Presione intro para continuar >> ")
                sele5 = True
                while sele5:
                    print("""
                    ---------------------------
                    | [x] Volver a ejecutar   |
                    |                         |
                    | [y] Retroceder          |
                    ---------------------------
                    """)
                    opt5 = input(" >> ")
                    if opt5 == "x":
                        os.system("clear")
                        sele5 = False
                        active5 = True

                    elif opt5 == "y":
                        sele5 = False
                        active5 = False
                        os.system("python3 dns.py")
                   
                    else:
                        print("Error: Opción no permitida!!!")
                        os.system("clear")

        getnsinfo_local_cname()
    
    elif com == "help":
        os.system("cat help.txt")
        a = input(" Presione intro para continuar >> ")
    
    elif com == "return":
        main = False
        os.system("bash ../netdog.sh")

    elif com == "exit":
        main = False
    
    else:
        os.system("clear")