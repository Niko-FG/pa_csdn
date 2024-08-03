import csv  
import requests  
import os  
import re  
  
# 设置请求头  
headers = {  
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36 Edg/127.0.0.0"  
}  
  
filename = './csdnurl.csv'  
  
# 读取CSV文件并处理每一行  
with open(filename, 'r', encoding='utf-8') as csvfile:  
    reader = csv.reader(csvfile)  
    next(reader)  # 跳过标题行  
    url_column = 0  # 假设URL在第一列  
  
    for index, row in enumerate(reader):  
        url = row[url_column]  # 提取URL  
        folder_path = os.path.join('./article/', f'wenzhang_{index}.html')  # 使用索引作为文件名  
  
        # 发送GET请求  
        response = requests.get(url, headers=headers)  
        if response.status_code == 200:  
            # 写入完整的HTML到文件  
            with open(folder_path, 'w', encoding='utf-8') as file:  
                file.write(response.text)  
  
            # 使用正则表达式查找匹配的标签内容  
            pattern = re.compile(r'<div id="content_views" class="htmledit_views">(.*?)</div>', re.DOTALL)  
            matches = pattern.findall(response.text)  
  
            # 如果找到匹配项，则提取内容并写入另一个文件（或覆盖原文件）  
            # 注意：这里我们可能会创建一个新的文件来存储提取的内容  
            extracted_content_path = os.path.join('./article/', f'extracted_wenzhang_{index}.txt')  
            with open(extracted_content_path, 'w', encoding='utf-8') as file:  
                for match in matches:  
                    file.write(match + '\n')  
        else:  
            print(f"Failed to fetch URL {url} with status code {response.status_code}")
