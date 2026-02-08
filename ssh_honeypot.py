# Libraries
import logging
import logging.handlers
from logging.handlers import RotatingFileHandler
import socket
import paramiko
import threading
import os

# Constants
logging_format = logging.Formatter(
    '%(asctime)s | %(levelname)s | %(name)s | %(message)s')
SSH_BANNER = "SSH-2.0-OpenSSH_8.2p1 Ubuntu-4ubuntu0.5"
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
HOST_KEY_PATH = os.path.join(BASE_DIR, "host.key")
host_key = paramiko.RSAKey(filename=HOST_KEY_PATH)

# Loggers & Logging Files
funnel_logger = logging.getLogger('FunnelLogger')
funnel_logger.setLevel(logging.INFO)

if not funnel_logger.handlers:
    funnel_handler = RotatingFileHandler(
        'audits.log', maxBytes=2000, backupCount=5
    )
    funnel_handler.setFormatter(logging_format)
    funnel_logger.addHandler(funnel_handler)

creds_logger = logging.getLogger('CredsLogger')
creds_logger.setLevel(logging.INFO)

if not creds_logger.handlers:
    creds_handler = RotatingFileHandler(
        'cmd_audits.log', maxBytes=2000, backupCount=5
    )
    creds_handler.setFormatter(logging_format)
    creds_logger.addHandler(creds_handler)

funnel_logger.propagate = False
creds_logger.propagate = False


# Emulated Shell

def emulated_shell(channel, client_ip):
    channel.send(b"confadmin1 ")
    command = b""

    while True:
        try:
            data = channel.recv(1024)
            if not data:
                break

            channel.send(data)
            command += data

            if b"\r" in command:
                cmd = command.strip().decode(errors="ignore")

                if cmd == "exit":
                    channel.send(b"\r\nAdios!\r\n")
                    break

                elif cmd == "pwd":
                    response = b"/usr/local\r\n"
                    creds_logger.info(
                        f'Command {command.strip()}' + 'executed by' + f'{client_ip}')
                elif cmd == "whoami":
                    response = b"a fool\r\n"
                    creds_logger.info(
                        f'Command {command.strip()}' + 'executed by' + f'{client_ip}')
                elif cmd == "ls":
                    response = b"prvdoc.conf1\r\n"
                    creds_logger.info(
                        f'Command {command.strip()}' + 'executed by' + f'{client_ip}')
                elif cmd == "cat prvdoc.conf1":
                    response = b"Why would I let you see this it's confidential\r\n"
                    creds_logger.info(
                        f'Command {command.strip()}' + 'executed by' + f'{client_ip}')
                elif cmd == "mkdir":
                    response = b"LEBRRRRROOOONNNNN\r\n"
                    creds_logger.info(
                        f'Command {command.strip()}' + 'executed by' + f'{client_ip}')
                elif cmd == "rmdir":
                    response = b"Honestly I'm good.\r\n"
                    creds_logger.info(
                        f'Command {command.strip()}' + 'executed by' + f'{client_ip}')
                elif cmd == "cd":
                    response = b"Compact Discs were created on October 1, 1982, starting in Japan\r\n"
                    creds_logger.info(
                        f'Command {command.strip()}' + 'executed by' + f'{client_ip}')
                else:
                    response = f"{cmd}: command not found\r\n".encode()
                    creds_logger.info(
                        f'Command {command.strip()}' + 'executed by' + f'{client_ip}')

                channel.send(b"\r\n" + response)
                channel.send(b"confadmin1 ")
                command = b""

        except Exception:
            break

    channel.close()

# SSH Server + Sockets


class Server(paramiko.ServerInterface):

    def __init__(self, client_ip, input_username=None, input_password=None):
        self.event = threading.Event()
        self.client_ip = client_ip
        self.input_username = input_username
        self.input_password = input_password

    def check_channel_request(self, kind: str, chanid: int) -> int:
        if kind == 'session':
            return paramiko.OPEN_SUCCEEDED

    def check_auth_password(self, username, password):
        funnel_logger.info(f'Client {self.client_ip} attempted connection with' +
                           f'username: {username},' + f'password: {password}')
        creds_logger.info(f'{self.client_ip}, {username}, {password}')
        if self.input_username is not None and self.input_password is not None:
            if username == self.input_username and password == self.input_password:
                return paramiko.AUTH_SUCCESSFUL
            else:
                return paramiko.AUTH_FAILED
        else:
            return paramiko.AUTH_SUCCESSFUL

    def get_allowed_auths(self, username):
        return "password"

    def check_channel_shell_request(self, channel):
        self.event.set()
        return True

    def check_channel_pty_request(self, channel, term, width, height, pixelwidth, pixelheight, modes):
        return True

    def check_channel_exec_request(self, channel, command):
        command = str(command)
        return True


def client_handle(client, addr, username, password):
    client_ip = addr[0]
    print(f"{client_ip} has connected to the server.")

    try:
        transport = paramiko.Transport(client)
        transport.local_version = SSH_BANNER

        server = Server(client_ip=client_ip,
                        input_username=username, input_password=password)

        transport.add_server_key(host_key)
        transport.start_server(server=server)

        channel = transport.accept(100)
        if channel is None:
            print("No channel was opened.")
            return

        standard_banner = "Welcome to Windows 24H2 (Dr. Victor Von Doom)|\r\n\r\n"
        channel.send(standard_banner)

        emulated_shell(channel, client_ip=client_ip)

    except Exception as error:
        print(error)
        print("!!! ERROR !!!")

    finally:
        try:
            transport.close()
        except Exception as error:
            print(error)
            print("!!! ERROR !!!")
        client.close()


# Provision SSH-based Honeypot

def honeypot(address, port, username, password):
    socks = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    socks.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    socks.bind((address, port))
    socks.listen(100)

    print(f"SSH server is listening on port {port}.")

    while True:
        try:
            client, addr = socks.accept()
            ssh_honeypot_thread = threading.Thread(
                target=client_handle, args=(client, addr, username, password))
            ssh_honeypot_thread.start()
        except Exception as error:
            print(error)


honeypot('127.0.0.1', 2223, username=None, password=None)
