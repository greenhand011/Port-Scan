import socket#导入socket库
from datetime import datetime#用于记录开始时间

#设置目标主机可以是域名可以是IP地址
target='scanme.nmap.org'
#target=127.0.0.1

#设置要扫描的端口范围
start_port=20
end_port=1024

print(f"开始扫描目标：{target}")
print(f"端口范围：{start_port}-{end_port}")
print(f"开始时间：{datetime.now()}")
print('-' * 50)

# 获取目标主机的 IP 地址（解析域名）
try:
    target_ip=socket.gethostbyname(target)
except socket.gaierror:
     print("无法解析主机名。请检查目标地址是否正确。")
     exit()
     
# 开始扫描指定端口范围
for port in range(start_port,end_port+1):
    s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)# 创建一个 TCP 套接字
    s.settimeout(0.5)# 设置超时时间为 0.5 秒，避免长时间等待

    result=s.connect_ex((target_ip,port))# 尝试连接端口，返回 0 表示成功
    if result==0:
        print(f'端口{port}开放')
    s.close()#关闭套接字
    
    
print('-'*50)
print(f'扫描结束时间：{datetime.now()}')