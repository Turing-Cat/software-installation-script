import os
"""
实现思路：
1、读取一个软件列表文件(暂定为txt)
2、判断是否安装
3、安装完毕！
"""
installCommand  = "winget install -e --location C:\winget\software --id"
software_list = []
with open("installation-list.txt","r") as file:
    for item in file:
        software_list.append(item.strip())
print(software_list)
for software_name in software_list:
    os.system(f"{installCommand} {software_name}")
print("Installation completed !!!")