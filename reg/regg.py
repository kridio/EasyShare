# -*- coding: utf-8 -*-
import os, ctypes, sys
import winreg
import re
import subprocess

class Ez_tool:
    def __init__(self):
        print ('init ez tool')
    @staticmethod
    def isFileExisted(fileName):
        if os.path.exists(fileName):
            return True
        else:
            return False

    def Get_OS_64_32(self):
        i = ctypes.c_int()
        kernel32 = ctypes.windll.kernel32
        process = kernel32.GetCurrentProcess()
        kernel32.IsWow64Process(process, ctypes.byref(i))
        is64bit = (i.value != 0)
        if (is64bit == True):
            return "64Bit"
        else:
            return "32Bit"

    def execAdminCmd(cmd):
        result = subprocess.call(['runas', '/user:Administrator',cmd])
        print('>>>',result)
    @staticmethod
    def traverse_registry_tree(key = r'SYSTEM\CurrentControlSet\Enum\USB'):
        root_key=winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, key, 0, (winreg.KEY_WOW64_64KEY + winreg.KEY_READ))
        reg_list = []
        i = 0
        while True:
            try:
                subkey = winreg.EnumKey(root_key, i)
                reg_list.append(subkey)
                i+=1
            except WindowsError:
                return reg_list
    def ignore_case(self,usbstor_list,pattern):
        list_temp = []
        for cc1_usbstor in usbstor_list:
            result = re.search(pattern,cc1_usbstor,re.IGNORECASE)
            if(result == None):
                list_temp.append(cc1_usbstor)
        for temp in list_temp:
            if temp in usbstor_list:
                usbstor_list.remove(temp)
        return usbstor_list

def open_kkb():
    print('open kkb')
    tool = Ez_tool()
    if (Get_OS_64_32() == "64Bit"):
        print('64bit os')
    else:
        print('32 bit os')
def close_kkb():
    tool = Ez_tool()
    command = 'taskkill /F /IM KerberosApp.exe'
    result = os.system(command)
    print('>>',result)
def clear_USB_history():
    print('clear usb history')
def clear_USB_history_as_default_setting():
    print('clear usb history as default setting')

#windows path program files = Progra~1, program files(x86) = Progra~2
def command_list():
    while True:
        print('Please select option')
        print ('1. Open the kkb')
        print ('2. Close the kkb')
        print ('3. Clear USB history')
        print ('4. Clear USB history when windows boot')
        try:
            x= input(">>>")
            print (x)
            if x==1:
                open_kkb()
                break
            elif x==2:
                close_kkb()
                break
            elif x==3:
                clear_USB_history()
                break
            elif x==4:
                clear_USB_history_as_default_setting()
                break
        except:
            print ('please input right select')
            continue


def __main__():
    print (r'start clear usb history')
    tool = Ez_tool()
    #isPsexecExisted = tool.isFileExisted(r"C:\Windows\sysnative\PsExec.exe")
    isPsexecExisted = tool.isFileExisted(r"C:\Windows\System32\PsExec.exe")
    if not isPsexecExisted:
        sys.exit("Please download Pstool include Psexec from microsoft web site and move Psexec to directory \"system32\"")
    command_list()

    # usbstor = r'\USBSTOR'
    # usb = r'\USB'
    # default_reg_cc1 = r'SYSTEM\ControlSet001\Enum'
    # default_reg_cc2 = r'SYSTEM\ControlSet002\Enum'
    # default_reg_ccs = r'SYSTEM\CurrentControlSet\Enum'
    # cc1_usbstor_list = tool.traverse_registry_tree(default_reg_cc1+usbstor)
    # cc1_usb_list = tool.traverse_registry_tree(default_reg_cc1+usb)
    # cc2_usbstor_list = tool.traverse_registry_tree(default_reg_cc2+usbstor)
    # cc2_usb_list = tool.traverse_registry_tree(default_reg_cc2+usb)
    # ccs_usbstor_list = tool.traverse_registry_tree(default_reg_ccs+usbstor)
    # ccs_usb_list = tool.traverse_registry_tree(default_reg_ccs+usb)
    # ccs_control_dc_307_list = tool.traverse_registry_tree(r'SYSTEM\CurrentControlSet\Control\DeviceClasses\{53f56307-b6bf-11d0-94f2-00a0c91efb8b}')
    # ccs_control_dc_308_list = tool.traverse_registry_tree(r'SYSTEM\CurrentControlSet\Control\DeviceClasses\{53f56307-b6bf-11d0-94f2-00a0c91efb8b}')
    # vid_pattern = r'vid'
    # disk_patter = r'disk'
    #
    # cc1_usb_list = tool.ignore_case(cc1_usb_list, vid_pattern)
    # #for cc1_usbstor in cc1_usbstor_list:
    # print cc1_usb_list
if __name__ == "__main__":
    __main__()

#HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Enum\USBSTOR
# for _key in _list:
#     subprocess.call(['runas', '/user:Administrator', 'psexec -i -s -d reg delete "HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Enum\USBSTOR\Disk&Ven_SanDisk&Prod_Ultra&Rev_1.00"'])
# def regkey_value(path, name="", start_key = None):
#     if isinstance(path, str):
#         path = path.split("\\")
#     if start_key is None:
#         start_key = getattr(winreg, path[0])
#         return regkey_value(path[1:], name, start_key)
#     else:
#         subkey = path.pop(0)
#     with _winreg.OpenKey(start_key, subkey) as handle:
#         assert handle
#         if path:
#             return regkey_value(path, name, handle)
#         else:
#             desc, i = None, 0
#             while not desc or desc[0] != name:
#                 desc = _winreg.EnumValue(handle, i)
#                 i += 1
#             return desc[1]

# example usage
#bios_vendor = regkey_value(r"HKEY_LOCAL_MACHINE\HARDWARE\DESCRIPTION\System\BIOS", "BIOSVendor")
#print bios_vendor
#HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Enum\USB
#Moldex_key = 'Moldex'
#Some_Key = "HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Enum\USBSTOR"

# if (Get_OS_64_32() == "64Bit"):
#     Some_Key = _winreg.OpenKey(_winreg.HKEY_LOCAL_MACHINE,r"SYSTEM\CurrentControlSet\Enum\USB")
#     try:
#         i = 0
#         while 1:
#         #EnumValue方法用来枚举键值，EnumKey用来枚举子键
#             print Some_Key
#             name, value, type = _winreg.EnumValue(Some_Key, i)
#             print repr(name),
#             i +=1
#     except WindowsError:
#         print 'excption'
# else:
#aKey = _winreg.OpenKey(_winreg.HKEY_LOCAL_MACHINE, Some_Key, 0, _winreg.KEY_QUERY_VALUE)
#
# Moldex_Path = _winreg.QueryValueEx(aKey, Moldex_key)[0]
#
# print Moldex_Path