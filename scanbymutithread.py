import socket# 导入 socket 用于网络连接
from concurrent.futures import ThreadPoolExecutor# 多线程模块
from datetime import datetime# 用于打印扫描时间

# -----------------------
# 配置项
# -----------------------

target='scanme.nmap.org'# 目标域名或 IP（不要扫描未授权网站哦~）
start_port=1# 起始端口
end_port=100# 结束端口
max_thread=100# 最大线程数（并发数）,太大容易被发现


# -----------------------
# 解析目标 IP 地址
# -----------------------

try:
    target_ip=socket.gethostbyname(target)
except socket.gaierror:
    print("[!] 无法解析目标主机名。请检查输入。")
    exit()
    
# -----------------------
# 端口扫描函数（线程调用）
# -----------------------

def port_scan(port):
    s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    s.settimeout(0.5)# 设置连接超时为 0.5 秒
    try:
        result=s.connect_ex((target_ip,port)) # 尝试连接，返回 0 表示成功
        if result==0:
            print(f"[✔] 端口 {port} 开放")
    except Exception as e:
        pass# 忽略异常
    finally:
        s.close()# 无论成功与否都关闭 socket
        

# -----------------------
# 主程序逻辑
# -----------------------

print(f"\n[*] 开始扫描目标：{target}，端口范围：{start_port}-{end_port}")
print(f"[*] 开始时间：{datetime.now()}\n")

# 创建线程池并分发任务
with ThreadPoolExecutor(max_workers=max_thread) as executor:
    for port in range(start_port,end_port+1):
        executor.submit(port_scan,port)
        
print(f"\n[*] 扫描结束时间：{datetime.now()}")



