import os
import time
os.system("python3 ./王XX.py")
time.sleep(60)           # 两个人连续打卡时间的间隔建议大于5s以上
os.system("python3 ./李XX.py")
time.sleep(60)
os.system("python3 ./张XX.py")
time.sleep(60)
# ··· ···
os.system("python3 ./人名.py")
time.sleep(60)
'''
os.system("python3 ./人名.py")
time.sleep(60)
 ··· ··· 无限循环往下继续写，多少人打卡就写多少套
'''


