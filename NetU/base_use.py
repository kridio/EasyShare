import Pexpect

server = r'\\192.168.163.1'
username = r'user'
passwd = r'123'
netuse_cmd = r'net use '+server+' '+passwd+' /user:'+username
netuse_del_cmd = r'net use \\192.168.163.1\helper /delete'