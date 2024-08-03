import requests  
import json
import csv

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

#构造请求参数，这些有没有用不知道
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
data_json = json.loads(response.text)        # 通过 json 解析数据
comment_list = data_json['result_vos']  # 获取result_vos下面的数据

comments = []                       # 构建空列表保存数据
for i in range(len(comment_list)):  # 循环获取每条的数据
    comment = {
        'url': comment_list[i]['url'],  # url标签
    }
    comments.append(comment)  # 输出

#-------------------输出到txt感觉不是特别好用----------------
#output_file = "D:/csdn/csdn.txt"
#with open(output_file, 'w') as f:
#    sys.stdout = f
#    print(comments)
#-----------------------------------------------------------
    
save_path = './csdnurl.csv'

# 将数据写入 csv, a是追加模式，w就是重定向模式
with open(save_path, 'a', newline='', encoding='utf-8') as fp:
    csv_header = ['url']  # 设置表头，即列名
    csv_writer = csv.DictWriter(fp, csv_header)
    # 如果文件不存在，则写入表头；如果文件已经存在，则直接追加数据不再次写入表头
    if fp.tell() == 0:
        csv_writer.writeheader()    
    csv_writer.writerows(comments)  # 写入数据
