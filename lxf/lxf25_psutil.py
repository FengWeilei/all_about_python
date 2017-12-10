# -*- coding: utf-8 -*-

import psutil  # Process and System Utility 用来获取系统信息。
print(psutil.cpu_count())
print(psutil.cpu_count(logical=False))

##>>> import psutil
##>>> psutil.cpu_count()
##2
##>>> psutil.cpu_count(logical=False)
##2
##>>> 

##>>> psutil.cpu_times()   # CPU 用户/系统/空闲时间
##scputimes(user=6031.85693359375, system=4757.015625, idle=69817.28125, interrupt=346.46260833740234, dpc=400.82896423339844)
##>>> 

##>>> for x in range(10):
##	psutil.cpu_percent(interval=1, percpu=True)   # cpu使用率
##
##	
##[10.6, 7.5]
##[9.3, 7.8]
##[0.0, 3.5]
##[11.3, 9.0]
##[7.5, 10.9]
##[4.6, 7.8]
##[10.8, 6.2]
##[9.4, 14.5]
##[17.2, 9.0]
##[6.2, 6.2]
##>>> 


##>>> psutil.virtual_memory()  # 物理内存 2.5G
##svmem(total=2832576512, available=613744640, percent=78.3, used=2218831872, free=613744640)
##>>> psutil.swap_memory()  # 交换内存信息  0.5G
##sswap(total=5663395840, used=2390888448, free=3272507392, percent=42.2, sin=0, sout=0)
##>>> 



##>>> psutil.disk_partitions()  #磁盘分区
##[sdiskpart(device='C:\\', mountpoint='C:\\', fstype='NTFS', opts='rw,fixed'), sdiskpart(device='D:\\', mountpoint='D:\\', fstype='NTFS', opts='rw,fixed'), sdiskpart(device='E:\\', mountpoint='E:\\', fstype='NTFS', opts='rw,fixed'), sdiskpart(device='F:\\', mountpoint='F:\\', fstype='NTFS', opts='rw,fixed'), sdiskpart(device='G:\\', mountpoint='G:\\', fstype='', opts='cdrom')]
##>>> psutil.disk_usage('C:\\') # 磁盘使用情况
##sdiskusage(total=53694595072, used=37332566016, free=16362029056, percent=69.5)
##>>>


##>>> dir(psutil)

