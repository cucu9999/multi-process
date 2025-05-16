# subprocess，电脑的子进程管理模块
# 利用subprocess启动电脑任意程序

import subprocess

'''
func_01: use default application to open a audio file.
'''
proc_01 = subprocess.Popen(
    [
        "start",
        "C:\\Users\\yongtong\\Music\\file.mp3",
        "shell = True",
    ]
)

proc_01.communicate()

