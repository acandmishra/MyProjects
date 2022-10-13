import subprocess
import schedule
def tasks():
    subprocess.call("excel.exe") # using call method of subprocess module to call executable files
schedule.every(10).seconds.do(tasks())
