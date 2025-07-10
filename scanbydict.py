import socket
from datetime import datetime

#目标主机地址（IP 或域名）
target='scanme.nmap.org'# 示例地址，可改为你自己的主机或靶机
# 定义你要扫描的端口字典（端口号: 服务名称）
port_dict = {
    21: "FTP",
    22: "SSH",
    23: "Telnet",
    25: "SMTP",
    53: "DNS",
    80: "HTTP",
    110: "POP3",
    143: "IMAP",
    443: "HTTPS",
    3306: "MySQL",
    3389: "RDP"
}

# 解析目标 IP
try:
    target_ip=socket.gethostbyname(target)
except socket.gaierror:
    print("[!] 目标域名解析失败！")
    exit()
    
# 开始扫描
print(f"[*] 扫描开始时间：{datetime.now()}")
print("-" * 50)

# 遍历字典中的端口并进行扫描
for port,service in port_dict.items():
    s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    s.settimeout(0.5)# 设置超时时间为 0.5 秒
    result=s.connect_ex((target_ip,port))# 连接端口
    if result==0:
        print(f"[✔] {service} 服务端口 {port} 开放 ✅")
    else:
        print(f"[✘] {service} 服务端口 {port} 未开放")
    s.close()
    

print("-" * 50)
print(f"[*] 扫描结束时间：{datetime.now()}")
    