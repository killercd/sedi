#!/usr/bin/env python3
import socket 
import argparse

ESC_ANSI = "\033["
FONT_GREEN = "32m"
FONT_BLUE = "34m"
STYLE_RESET = "\033[0m"
SOCKET_TIME = 5
request_list = [
    "GET / HTTP/1.0\r\n\r\n", 
    "GET / HTTP/1.0\r\nHost: %HOST%\r\n\r\n"
]

def port_list(value):
    return [int(x.strip()) for x in value.split(",") if x.strip()]
def hosts_list(value):
    return [x.strip() for x in value.split(",") if x.strip()]
    
if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="Service Discovery")
    parser.add_argument("ip", help="target ip")
    parser.add_argument("--ports", type=port_list, default=[], help="ports comma separated list")
    parser.add_argument("--hosts", type=hosts_list, default=[], help="hosts comma separated list")

    args = parser.parse_args()
    dest_ip = args.ip
    port_list = args.ports
    host_list = args.hosts
    
    
    if(len(host_list)<=0):
        host_list.append(dest_ip)
    
    for port in port_list:
        for idstring in request_list:
            for host in host_list:
                rep_idstring = idstring.replace("%HOST%",host)
                s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                print(f"--> {dest_ip}:{port}")
                print(f"{ESC_ANSI}{FONT_GREEN}{rep_idstring}{STYLE_RESET}")
                try:
                    s.settimeout(SOCKET_TIME)
                    s.connect((dest_ip, port))
                    s.send(rep_idstring.encode())
                    print(f"<-- {dest_ip}:{port}")
                    retdata = s.recv(5000).decode("utf-8",errors="replace")[:1000]
                    print(f"{ESC_ANSI}{FONT_BLUE}{retdata}{STYLE_RESET}")
                    s.close()
                except ConnectionRefusedError:
                    print("Connection refused")
                except TimeoutError:
                    print("Connection timeout")
                except OSError as ex:
                    print("Connection error: ",ex) 

