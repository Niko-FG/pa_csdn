import requests  
import re  
import threading
import time

import json
import csv
#下面这两行我都写到文档里了，这里用urll是因为url后面有用，不确定有没有冲突
urll = "https://so.csdn.net/api/v3/search"

headers = {
    'accept' : 'application/json, text/plain, */*',
    'accept-encoding' : 'gzip, deflate, br, zstd',
    'accept-language' : 'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6',
    'connection' : 'keep-alive',
    'host' : 'so.csdn.net',
    'referer' : 'https://so.csdn.net/so/search?spm=1000.2115.3001.4498&q=pcie&t=&u=',
    'sec-ch-ua' : '"Not)A;Brand";v="99", "Microsoft Edge";v="127", "Chromium";v="127"',
    'sec-ch-ua-mobile' : '?0',
    'sec-ch-ua-platform' : '"Windows"',
    'sec-fetch-dest' : 'empty',
    'sec-fetch-mode' : 'cors',
    'sec-fetch-site' : 'same-origin',
    'user-agent' :  'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 '
                    '(KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36 Edg/127.0.0.0'
}

#构造请求参数
params = {
    'q': 'pcie',
    't' : 'all',
    'p' : '1',
    's' : '0',
    'tm' : '0',
    'lv' : '-1',
    'ft' : '0',
    'l' : '',
    'u' : '',
    'ct' : '-1',
    'pnt' : '-1',
    'ry' : '-1',
    'ss' : '-1',
    'dct' : '-1',
    'vco' : '-1',
    'cc' : '-1',
    'sc' : '-1',
    'akt' : '-1',
    'art' : '-1',
    'ca' : '-1',
    'prs' : '',
    'pre' : '',
    'ecc' : '-1',
    'ebc' : '-1',
    'ia' : '1',
    'dld' : '',
    'cl' : '-1',
    'scl' : '-1',
    'tcl' : '-1',
    'platform' : 'pc',
    'ab_test_code_overlap' : '',
    'ab_test_random_code' : '',
}

# 通过get方法请求数据
response = requests.get(urll, headers=headers, params=params)

response.encoding = 'utf-8'                  # 修改编码格式

#目前只会json的，别的不会
data_json = json.loads(response.text)        # 通过 json 解析数据
comment_list = data_json['result_vos']  # 获取result_vos下面的数据

comments = []                       # 构建空列表存数据
for i in range(len(comment_list)):  # 循环获取数据
    comment = {
        'url': comment_list[i]['url'],  # url，因为我只需要url，需要别的再写别的
    }
    comments.append(comment)  # 每页的评论数据

save_path = 'D:/csdn/csdn.csv'

# 将数据写入 csv
with open(save_path, 'a', newline='', encoding='utf-8') as fp:
    csv_header = ['url']  # 设置表头，即列名
    csv_writer = csv.DictWriter(fp, csv_header)
    # 如果文件不存在，则写入表头；如果文件已经存在，则直接追加数据不再次写入表头
    if fp.tell() == 0:
        csv_writer.writeheader()    
    csv_writer.writerows(comments)  # 写入数据



#----------------------------------------------------------------------------------
#这个是爬静态用的
#headers = {  
#    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36 Edg/127.0.0.0"  
#}  
  
# 发送GET请求并保存响应  
#response = requests.get("https://so.csdn.net/so/search?spm=1000.2115.3001.4498&q=pcie&t=&u=", headers=headers)  
# 从响应中提取HTML文本  
#html_text = response.text  
#with open('D:/csdn/url.txt', 'a') as file:  
#    file.write(html_text + '\n') 

# 使用正则表达式查找匹配的<h2>标签内容  
#result = re.findall('<h3 class="title substr">href="([^"]*)"</h2>', html_text)  

# 如果找到匹配项，则写入文件  
#with open('D:/csdn/url.txt', 'a') as file:  
#    for i in result:  
#        file.write(i + '\n') 

#def stop_task():    
#    print("Task stopped")
#timer = threading.Timer(2.0, stop_task)
#timer.start()
#-------------------------------------------------------------------------------------
