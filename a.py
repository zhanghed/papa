import os

# https://pypi.douban.com/simple # 豆瓣镜像

# https://pypi.tuna.tsinghua.edu.cn/simple # 清华镜像

mirror = " -i https://pypi.tuna.tsinghua.edu.cn/simple"

os.system("python -m pip install --upgrade pip" + mirror)  # 更新 pip

#os.system(r"pip install --target=路径 包名" + mirror)  # 安装

os.system("pip install lxml " + mirror)  # 安装
