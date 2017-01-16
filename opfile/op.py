import os
from shutil import copyfile

class exec_process:
    def move(self,src,dest):
        src_folder = src
        dest_folder = dest
        copyfile(src_folder, dest_folder)
        # os.rename("path/to/current/file.foo", "path/to/new/desination/for/file.foo")
        # shutil.move("path/to/current/file.foo", "path/to/new/destination/for/file.foo")

exec = exec_process()
exec.move(r'\\192.168.163.1\helper\賽門鐵克病毒更新.txt',r'C:\Users\sulley\Desktop\賽門鐵克病毒更新.txt')