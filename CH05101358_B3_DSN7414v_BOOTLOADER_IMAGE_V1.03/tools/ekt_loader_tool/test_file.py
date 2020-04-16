# -*- coding:utf8 -*-
# new_str_dict = {1006: [1001, 1001], 1007: [1002, 1002], 1008: [1003, 1003], 1009: [1004, 1004], 1010: [1005, 1005]}
#
# for dsn_ver, [file1, file2] in new_str_dict.items():
#     print dsn_ver
#     print file1
#     print file2


# new_file_path = "./ekt_loader_tool-app-bootlogo-{}-{}.cfg"
#
# print new_file_path.format(1, 2)


import win32api
import time
import os


# win32api.ShellExecute(0, 'open', r'E:\HiTool-STB-5.0.45\HiTool\HiTool.exe', '', '', 1)
win32api.ShellExecute(0, 'open', r'E:\auto_burn\Flash samples\tftpd32.exe', '', '', 1)
# win32api.ShellExecute(0, 'open', r"D:\Program Files (x86)\NetSarang\Xshell 6\Xshell.exe", '', '', 1)
# win32api.ShellExecute(0, 'open', r"E:\To_IVAN\ivan_svn\7414\CH05101358_B3_DSN7414v_BOOTLOADER_IMAGE_V1.03\CH05101358_B3_DSN7414v_BOOTLOADER_IMAGE_V1.03\burn_flash_windowtool\FT_Tool.exe", '', '', 1)

time.sleep(15)

# os.system("taskkill /F /IM HiTool.exe")
# os.system("taskkill /F /IM tftpd32.exe")
# os.system("taskkill /F /IM Xshell.exe")
# os.system("taskkill /F /IM FT_Tool.exe")
