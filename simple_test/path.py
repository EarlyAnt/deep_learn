import os
import sys

# 获取当前脚本所在的项目根目录
root_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
print(f"root path: {root_path}\n")

sys.path.append(f"{root_path}\\utils")
print(f"sys path: {sys.path}\n")

import utils.datetime_util as dt
print(f"date time: {dt.date_time_full()}")