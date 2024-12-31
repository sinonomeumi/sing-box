#吃瓜脚本，用于监控注册机大佬和波兰仔的爱恨情仇与生死搏斗状态
#by ：潇潇

import requests
import re
import time
import os
from playsound import playsound
from datetime import datetime, timezone, timedelta

print("正在吃瓜中。。。")

# 监控目标URL
url = "https://www.serv00.com/"

# 正则表达式，匹配 <span> 中的数值
pattern = r'(\d+) / (\d+)'

# 获取当前网页源代码并返回
def get_page_content():
    try:
        response = requests.get(url)
        if response.status_code == 200:
            return response.text
        else:
            print(f"Error: 叼毛！你的网络似乎有问题!. Status code: {response.status_code}")
            return None
    except Exception as e:
        print(f"Error: {e}")
        return None

# 解析网页内容，获取当前的账号数
def parse_account_count(page_content):
    match = re.search(pattern, page_content)
    if match:
        current_count = int(match.group(1))  # 获取当前的账号数
        print(current_count)
        return current_count
    else:
        print("Error: 波兰仔网站炸啦！.")
        return None

# 下载并播放音频
def play_sound(url):
    try:
        local_filename = "blz.mp3"
        # 下载音频
        with open(local_filename, "wb") as f:
            f.write(requests.get(url).content)
        # 播放音频
        playsound(os.path.abspath(local_filename))
        # 播放完毕后删除本地音频文件
        if os.path.exists(local_filename):
            os.remove(local_filename)
    except Exception as e:
        print(f"Error 播放声音失败: {e}")

# 主函数，监控账号数变化
def monitor_account_count():
    last_count = None

    while True:
        page_content = get_page_content()
        if page_content:
            current_count = parse_account_count(page_content)

            if current_count is not None:
                if last_count is None:
                    last_count = current_count  # 初始化时设置最后的账号数

                # 如果账号数减少
                if current_count < last_count:
                    # 获取当前北京时间
                    beijing_time = datetime.now(timezone(timedelta(hours=8)))
                    print("波兰仔开始删号啦！快跑！", beijing_time.strftime('%Y-%m-%d %H:%M:%S'))
                    play_sound("https://github.com/wdrvk/wenjian/raw/refs/heads/main/sh.mp3")

                # 如果账号数增加
                elif current_count > last_count:
                    # 获取当前北京时间
                    beijing_time = datetime.now(timezone(timedelta(hours=8)))
                    print("有人注册成功啦！快冲！", beijing_time.strftime('%Y-%m-%d %H:%M:%S'))
                    play_sound("https://github.com/wdrvk/wenjian/raw/refs/heads/main/zc.mp3")

                last_count = current_count  # 更新最后的账号数

        # 等待一分钟
        time.sleep(60)

# 启动监控
if __name__ == "__main__":
    monitor_account_count()
