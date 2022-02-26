#!/bin/bash
clear
echo "<----------------------------------------------------------------------------->"
echo " ▄▄        ▄  ▄▄▄▄▄▄▄▄▄▄▄  ▄▄▄▄▄▄▄▄▄▄▄  ▄▄▄▄▄▄▄▄▄▄   ▄▄▄▄▄▄▄▄▄▄▄  ▄▄▄▄▄▄▄▄▄▄▄  "  
echo "▐░░▌      ▐░▌▐░░░░░░░░░░░▌▐░░░░░░░░░░░▌▐░░░░░░░░░░▌ ▐░░░░░░░░░░░▌▐░░░░░░░░░░░▌ "
echo "▐░▌░▌     ▐░▌▐░█▀▀▀▀▀▀▀▀▀  ▀▀▀▀█░█▀▀▀▀ ▐░█▀▀▀▀▀▀▀█░▌▐░█▀▀▀▀▀▀▀█░▌▐░█▀▀▀▀▀▀▀▀▀  "
echo "▐░▌▐░▌    ▐░▌▐░▌               ▐░▌     ▐░▌       ▐░▌▐░▌       ▐░▌▐░▌           "
echo "▐░▌ ▐░▌   ▐░▌▐░█▄▄▄▄▄▄▄▄▄      ▐░▌     ▐░▌       ▐░▌▐░▌       ▐░▌▐░▌ ▄▄▄▄▄▄▄▄  "
echo "▐░▌  ▐░▌  ▐░▌▐░░░░░░░░░░░▌     ▐░▌     ▐░▌       ▐░▌▐░▌       ▐░▌▐░▌▐░░░░░░░░▌ "
echo "▐░▌   ▐░▌ ▐░▌▐░█▀▀▀▀▀▀▀▀▀      ▐░▌     ▐░▌       ▐░▌▐░▌       ▐░▌▐░▌ ▀▀▀▀▀▀█░▌ "
echo "▐░▌    ▐░▌▐░▌▐░▌               ▐░▌     ▐░▌       ▐░▌▐░▌       ▐░▌▐░▌       ▐░▌ "
echo "▐░▌     ▐░▐░▌▐░█▄▄▄▄▄▄▄▄▄      ▐░▌     ▐░█▄▄▄▄▄▄▄█░▌▐░█▄▄▄▄▄▄▄█░▌▐░█▄▄▄▄▄▄▄█░▌ "
echo "▐░▌      ▐░░▌▐░░░░░░░░░░░▌     ▐░▌     ▐░░░░░░░░░░▌ ▐░░░░░░░░░░░▌▐░░░░░░░░░░░▌ "
echo " ▀        ▀▀  ▀▀▀▀▀▀▀▀▀▀▀       ▀       ▀▀▀▀▀▀▀▀▀▀   ▀▀▀▀▀▀▀▀▀▀▀  ▀▀▀▀▀▀▀▀▀▀▀  "
echo "<----------------------------------------------------------------------------->"
echo "                                 V 2.0                                         "
echo "<----------------------------------------------------------------------------->"
echo "Este programa se usa para controlar tu red domestica o de                      "
echo "empresa de una forma que podrás saber quienes usan tu red,                     "
echo "que puertos estan abiertos y mas. Escriban el comando 'help'                   "
echo "aquí on en una opción para poder ver los comandos de cada                      "
echo "opción.                                                                        "
echo "<----------------------------------------------------------------------------->"
echo "  [0] Instalación de requisitos                                                "
echo "<----------------------------------------------------------------------------->"
echo "                                                                               "
echo "        [1] < ESCANEAR PUERTOS >                                               "
echo "                                                                               "
echo "        [2] < HOSTS DE LA RED >                                                "
echo "                                                                               "
echo "        [3] < BUSCAR VULNERABILIDADES >                                        "
echo "                                                                               "
echo "        [4] < SACAR INFORMACIÓN A UN DOMINIO/DNS >                             "
echo "                                                                               "
echo "        [5] < CAPTURAR PAQUETES/TRAFICO >                                      "
echo "                                                                               "
echo "<----------------------------------------------------------------------------->"
echo "[*] Escoge una opción >>: " 
read -r opt

if [ $opt = "0" ]; then
sudo apt-get install nmap
sudo apt-get install bind9
sudo apt-get install tcpdump -y
bash netdog.sh

elif [ $opt = "1" ]; then
    if [ -d /usr/share/nmap ]; then
    clear
    python3 ports.py
    else
    echo "Error > No tienes instalado el programa NMAP, selecciona la opción [0]."
    echo ">> : "
    bash /opt/netdog.sh
    fi

elif [ $opt = "2" ]; then
    if [ -d /usr/share/nmap ]; then
    python3 /opt/hosts.py
    else
    echo "Error > No tienes instalado el programa NMAP, selecciona la opción [0]"
    echo ">> : "
    bash /opt/netdog.sh
    fi

elif [ $opt = "3" ]; then
    if [ -d /usr/share/nmap ]; then
    python3 /opt/vuln.py
    else
    echo "Error > No tienes instalado el programa NMAP, selecciona la opción [0]"
    echo "Deseas continuar? >> "
    bash netdog.sh
    fi

elif [ $opt = "4" ]; then
    if [ -d /usr/share/nmap ]; then
    python3 /opt/dns.py
    else
    echo "Error > No tienes instalado el programa NMAP, selecciona la opción [0]"
    echo "Deseas continuar? >> "
    bash netdog.sh
    fi

elif [ $otp = "5" ]; then
    bash /opt/tcpscan.py

elif [ $opt = "help" ]; then
    cat /opt/help.txt
    echo "Presione cualquier tecla para continuar: "
    clear
    bash netdog.sh

elif [ $opt = "exit" ]; then
    exit

else
  clear
  bash netdog.sh
fi
