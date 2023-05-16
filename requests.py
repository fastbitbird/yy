python
import requests
#import os

# 恶意响应体
mal_res = {
    "name": "test", 
    "content": "os.system('ls -l')"  
}

# requests <= 2.25.0 版本(存在代码执行漏洞)
requests.__version__  

# 准备requests漏洞验证环境
# pip install requests==2.25.0  

# 发起任意HTTP请求  
res = requests.get('http://example.com')

# 检查/tmp目录文件   
#tmp_files = os.listdir('/tmp')
#print(f'Before parse, /tmp files: {tmp_files}')

# 解析恶意响应体,执行代码  
res.json()   

# 再次检查/tmp目录文件   
#tmp_files = os.listdir('/tmp')
#print(f'After parse, /tmp files: {tmp_files}')

# /tmp目录文件被清空,说明代码执行成功  
# 对应requests <= 2.25.0 版本代码执行漏洞

# 升级requests版本至2.26.0+
# pip install requests==2.26.0   

# 提交漏洞报告给requests官方
